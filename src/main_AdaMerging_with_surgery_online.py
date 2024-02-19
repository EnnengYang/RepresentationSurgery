import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import sys
src_root_path = '/root/'
checkpoint_path = '/root/checkpoint/'
dataset_path = '/root/dataset/'
sys.path.append(src_root_path)

import math
import time
import tqdm
import torch
from task_vectors import TaskVector
from args import parse_arguments
from utils import create_log_dir

from eval import eval_single_dataset, eval_single_dataset_head, eval_single_dataset_preprocess_head, eval_single_dataset_preprocess_mapping_head
from datasets.registry import get_dataset
from datasets.common import maybe_dictionarize, get_dataloader_shuffle
from merging_model import ModelWrapper, AlphaWrapper, make_functional

# Config
exam_datasets = ['SUN397', 'Cars', 'RESISC45', 'EuroSAT', 'SVHN', 'GTSRB', 'MNIST', 'DTD'] # SUN397 | Cars | RESISC45 | EuroSAT | SVHN | GTSRB | MNIST | DTD
learn_datasets = ['SUN397', 'Cars', 'RESISC45', 'EuroSAT', 'SVHN', 'GTSRB', 'MNIST', 'DTD']

method_name = 'lw_adamerging' # choose: weight_averaging | task_arithmetic | ties_merging | tw_adamerging | lw_adamerging | tw_adamergingpp | lw_adamergingpp
model_name = 'ViT-B-32'  #  choose: ViT-B-32 | ViT-B-16 | ViT-L-14

is_visualization = False
iterations = 500
eval_iterations = 100

args = parse_arguments()
args.method_name = method_name
args.model_name = model_name
args.data_location = dataset_path
args.save = checkpoint_path + model_name

if is_visualization:
    args.logs_path = src_root_path + 'src/logs/visualization/' + model_name
else:
    args.logs_path = src_root_path + 'src/logs/online/' + model_name

pretrained_checkpoint = checkpoint_path + model_name+'/zeroshot.pt'

log = create_log_dir(args.logs_path, 'log_{}_{}_{}_{}.txt'.format(str(__file__.split("/")[-1].split(".")[0]), method_name, model_name, time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))))
log.info(str(args))

# Create the task vectors
if method_name in ['ties_merging', 'tw_adamergingpp', 'lw_adamergingpp']:
    # TIES Merging
    from ties_merging_utils import *

    ft_checks = [torch.load(checkpoint_path + model_name + '/' + dataset_name + '/finetuned.pt').state_dict() for dataset_name in exam_datasets]
    ptm_check = torch.load(pretrained_checkpoint).state_dict()
    check_parameterNamesMatch(ft_checks + [ptm_check])
    remove_keys = []

    flat_ft = torch.vstack([state_dict_to_vector(check, remove_keys) for check in ft_checks])
    flat_ptm = state_dict_to_vector(ptm_check, remove_keys)

    tv_flat_checks = flat_ft - flat_ptm
    assert check_state_dicts_equal(vector_to_state_dict(flat_ptm, ptm_check, remove_keys), ptm_check)
    assert all([check_state_dicts_equal(vector_to_state_dict(flat_ft[i], ptm_check, remove_keys), ft_checks[i]) for i in range(len(ft_checks))])
    selected_entries, merged_tv = ties_merging_split(tv_flat_checks, reset_thresh=20, merge_func="dis-sum", )

    ties_task_vectors = []
    for vector_ in selected_entries:
        t_state_dict = vector_to_state_dict(vector_, ptm_check, remove_keys=remove_keys)
        ref_model = torch.load(pretrained_checkpoint)
        ref_model.load_state_dict(t_state_dict, strict=False)
        ties_task_vectors.append(ref_model.state_dict())

elif method_name in ['weight_averaging', 'task_arithmetic', 'tw_adamerging', 'lw_adamerging']:
    # Task Vector
    task_vectors = [TaskVector(pretrained_checkpoint, checkpoint_path + model_name + '/' + dataset_name + '/finetuned.pt') for dataset_name in exam_datasets]

else:
    print('method name error!')
    exit(-1)


pretrained_model = torch.load(pretrained_checkpoint)
pretrained_model_dic = pretrained_model.state_dict()

model = ModelWrapper(pretrained_model)
model = model.to(args.device)
_, names = make_functional(model)

paramslist = []
paramslist += [tuple(v.detach().requires_grad_().cpu() for _, v in pretrained_model_dic.items())] # pretrain
if method_name in ['ties_merging', 'tw_adamergingpp', 'lw_adamergingpp']:
    paramslist += [tuple(v.detach().requires_grad_().cpu() for _, v in sd.items())  for i, sd in enumerate(ties_task_vectors)] # task vectors
elif method_name in ['weight_averaging', 'task_arithmetic', 'tw_adamerging', 'lw_adamerging']:
    paramslist += [tuple(v.detach().requires_grad_().cpu() for _, v in sd.vector.items()) for i, sd in enumerate(task_vectors)]  # task vectors

torch.cuda.empty_cache()
alpha_model = AlphaWrapper(paramslist, model, names, exam_datasets, args)

optimizer = torch.optim.Adam(alpha_model.collect_trainable_params(), lr=1e-3, betas=(0.9, 0.999), weight_decay=0.)
loss_func = torch.nn.L1Loss()

for dataset_name in learn_datasets:
    # shuffled test data, batch_size=1
    dataset = get_dataset(dataset_name, pretrained_model.val_preprocess, location=args.data_location, batch_size=1)
    dataloader = get_dataloader_shuffle(dataset)

    finetuned = torch.load(checkpoint_path + args.model_name + '/' + dataset_name + '/finetuned.pt')
    finetuned = finetuned.to(args.device)
    finetuned.eval()

    eval_iter = [
                 int(0.01*len(dataloader)),
                 int(0.1*len(dataloader)),
                 int(0.2*len(dataloader)),
                 int(0.3*len(dataloader)),
                 int(0.4*len(dataloader)),
                 int(0.5*len(dataloader)),
                 int(0.6*len(dataloader)),
                 int(0.7*len(dataloader)),
                 int(0.8*len(dataloader)),
                 int(0.9*len(dataloader)),
                 int(1.0*len(dataloader))
                 ]

    log.info(dataset_name+' Eval step:')
    log.info(eval_iter)

    # Each sample is only passed once.
    for i, data in enumerate(tqdm.tqdm(dataloader)):
        data = maybe_dictionarize(data)
        x = data['images'].to(args.device)

        outputs, features, _, _ = alpha_model(x, dataset_name)
        finetuned_features = finetuned(x).detach()

        loss = loss_func(features, finetuned_features)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # Evaluate
        if (i+1) in eval_iter:
            image_encoder = alpha_model.get_image_encoder()
            classification_head = alpha_model.get_classification_head(dataset_name)
            down_proj, up_proj = alpha_model.get_feature_mapping_to_head(dataset_name)
            metrics = eval_single_dataset_preprocess_mapping_head(image_encoder, classification_head, dataset_name, args, down_proj, up_proj)
            log.info('Eval: ratio: ' + str((i+1)/len(dataloader))+ ' step:'+ str(i+1) + ' dataset: ' + str(dataset_name) + ' ACC: ' + str(metrics['top1']))
