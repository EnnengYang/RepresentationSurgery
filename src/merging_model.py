import os
import torch
import math
import random
import numpy as np
import time
import sys
import tqdm

from heads import get_classification_head as get_finetuned_classification_head
from merging_cofficient import get_merging_cofficients


# Utilities to make nn.Module functional
def del_attr(obj, names):
    if len(names) == 1:
        delattr(obj, names[0])
    else:
        del_attr(getattr(obj, names[0]), names[1:])

def set_attr(obj, names, val):
    if len(names) == 1:
        setattr(obj, names[0], val)
    else:
        set_attr(getattr(obj, names[0]), names[1:], val)

def make_functional(mod):
    orig_params = tuple(mod.parameters())
    # Remove all the parameters in the model
    names = []
    for name, p in list(mod.named_parameters()):
        del_attr(mod, name.split("."))
        names.append(name)
    return orig_params, names

def load_weights(mod, names, params):
    for name, p in zip(names, params):
        set_attr(mod, name.split("."), p)

def softmax_entropy(x):
    """Entropy of softmax distribution from logits."""
    return -(x.softmax(1) * x.log_softmax(1)).sum(1)

class ModelWrapper(torch.nn.Module):
    def __init__(self, model, initial_weights=None):
        super(ModelWrapper, self).__init__()
        self.model = model

        # Note: modified. Get rid of the language part.
        if hasattr(self.model, 'transformer'):
            delattr(self.model, 'transformer')

    def forward(self, images):
        features = self.model(images)
        return features

class AlphaWrapper(torch.nn.Module):
    def __init__(self, paramslist, model, names, exam_datasets, args):
        super(AlphaWrapper, self).__init__()
        self.paramslist = paramslist
        self.model = model
        self.names = names
        self.exam_datasets = exam_datasets
        self.args = args

        ralpha = get_merging_cofficients(args.method_name, args.model_name)

        self.alpha = torch.Tensor(ralpha)

        self.non_linear_func = torch.nn.ReLU()

        for dataset_name in exam_datasets:
            # mapping
            # ViT-B/32 and ViT-B/16
            down_proj = torch.nn.Linear(512, 16, bias=False)
            up_proj = torch.nn.Linear(16, 512, bias=False)
            # ViT-L/14
            # down_proj = torch.nn.Linear(768, 16, bias=False)
            # up_proj = torch.nn.Linear(16, 768, bias=False)
            torch.nn.init.kaiming_uniform_(down_proj.weight, a=math.sqrt(5))
            torch.nn.init.zeros_(up_proj.weight)
            self.add_module('feature_mapping_to_head_down_proj_{}'.format(dataset_name), down_proj.to(args.device))
            self.add_module('feature_mapping_to_head_up_proj_{}'.format(dataset_name), up_proj.to(args.device))

            # classifier
            classification_head = get_finetuned_classification_head(args, dataset_name)
            layer_name = 'classifier_{}'.format(dataset_name)
            self.add_module(layer_name, classification_head.to(args.device))

    def collect_trainable_params(self):
        trainable_params = []

        # surgery parameter
        for dataset_name in self.exam_datasets:
            down_proj = getattr(self, 'feature_mapping_to_head_down_proj_{}'.format(dataset_name))
            up_proj = getattr(self, 'feature_mapping_to_head_up_proj_{}'.format(dataset_name))
            trainable_params.append(down_proj.weight)
            trainable_params.append(up_proj.weight)
        return trainable_params

    def get_classification_head(self, dataset_name):
        layer_name = 'classifier_{}'.format(dataset_name)
        classification_head = getattr(self, layer_name)
        return classification_head

    def get_feature_mapping_to_head(self, dataset_name):
        down_proj = getattr(self, 'feature_mapping_to_head_down_proj_{}'.format(dataset_name))
        up_proj = getattr(self, 'feature_mapping_to_head_up_proj_{}'.format(dataset_name))
        return down_proj, up_proj

    def get_image_encoder(self):
        if self.alpha.size()[0] == 1:# task-wise merging
            params = tuple(sum(tuple(pi * alphai for pi, alphai in zip(p, self.alpha[0].cpu()))) for j, p in enumerate(zip(*self.paramslist)))
        else: # layer-wise merging
            params = tuple(sum(tuple(pi * alphai for pi, alphai in zip(p, self.alpha[j].cpu()))) for j, p in enumerate(zip(*self.paramslist)))

        params = tuple(p.cuda(0) for p in params)
        load_weights(self.model, self.names, params)
        return self.model

    def forward(self, inp, dataset_name):
        # raw feature
        if self.alpha.size()[0] == 1: # task-wise merging
            params = tuple(sum(tuple(pi * alphai for pi, alphai in zip(p, self.alpha[0].cpu()))) for j, p in enumerate(zip(*self.paramslist)))
        else: # layer-wise merging
            params = tuple(sum(tuple(pi * alphai for pi, alphai in zip(p, self.alpha[j].cpu()))) for j, p in enumerate(zip(*self.paramslist)))

        params = tuple(p.cuda(0) for p in params)
        load_weights(self.model, self.names, params)
        feature = self.model(inp)
        feature0 = feature

        # feature bias
        down_proj = getattr(self, 'feature_mapping_to_head_down_proj_{}'.format(dataset_name))
        up_proj = getattr(self, 'feature_mapping_to_head_up_proj_{}'.format(dataset_name))
        feature_sub = down_proj(feature)
        feature_sub = self.non_linear_func(feature_sub)
        feature_sub = up_proj(feature_sub)

        # surgery feature
        feature = feature0 - feature_sub

        # classifier
        layer_name = 'classifier_{}'.format(dataset_name)
        classification_head = getattr(self, layer_name)
        out = classification_head(feature)

        return out, feature, feature0, feature_sub
