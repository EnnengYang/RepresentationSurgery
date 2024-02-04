import os
import torch
from torchvision.datasets import SVHN as PyTorchSVHN
import numpy as np

import random
from torch.utils.data import Subset, Dataset

class SVHN:
    def __init__(self,
                 preprocess,
                 location=os.path.expanduser('~/data'),
                 batch_size=128,
                 num_workers=0,
                 subset_data_ratio=1.0):

        # to fit with repo conventions for location
        modified_location = os.path.join(location, 'svhn')

        self.train_dataset = PyTorchSVHN(
            root=modified_location,
            download=True,
            split='train',
            transform=preprocess
        )

        self.train_loader = torch.utils.data.DataLoader(
            self.train_dataset,
            batch_size=batch_size,
            shuffle=True,
            num_workers=num_workers
        )

        if subset_data_ratio < 1.0:
            random.seed(42)
            random_indexs = random.sample(range(len(self.train_dataset)),
                                          int(subset_data_ratio * len(self.train_dataset)))
            print('svhn subset_data_ratio:' + str(subset_data_ratio))
            print('svhn random_indexs:' + str(random_indexs))
            self.train_dataset_sub = Subset(self.train_dataset, random_indexs)
        else:
            self.train_dataset_sub = self.train_dataset

        self.train_loader_sub = torch.utils.data.DataLoader(
            self.train_dataset_sub,
            shuffle=True,
            batch_size=batch_size,
            num_workers=num_workers,
        )


        self.test_dataset = PyTorchSVHN(
            root=modified_location,
            download=True,
            split='test',
            transform=preprocess
        )

        self.test_loader = torch.utils.data.DataLoader(
            self.test_dataset,
            batch_size=batch_size,
            shuffle=False,
            num_workers=num_workers
        )
        self.test_loader_shuffle = torch.utils.data.DataLoader(
            self.test_dataset,
            batch_size=batch_size,
            shuffle=True,
            num_workers=num_workers
        )

        self.classnames = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
