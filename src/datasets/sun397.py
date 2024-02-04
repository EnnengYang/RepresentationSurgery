import os
import torch
import torchvision.datasets as datasets

import random
from torch.utils.data import Subset, Dataset

class SUN397:
    def __init__(self,
                 preprocess,
                 location=os.path.expanduser('~/data'),
                 batch_size=32,
                 num_workers=0,
                 subset_data_ratio=1.0):
        # Data loading code
        traindir = os.path.join(location, 'sun397', 'train')
        valdir = os.path.join(location, 'sun397', 'test')


        self.train_dataset = datasets.ImageFolder(traindir, transform=preprocess)

        self.train_loader = torch.utils.data.DataLoader(
            self.train_dataset,
            shuffle=True,
            batch_size=batch_size,
            num_workers=num_workers,
        )

        if subset_data_ratio < 1.0:
            random.seed(42)
            random_indexs = random.sample(range(len(self.train_dataset)),
                                          int(subset_data_ratio * len(self.train_dataset)))
            print('sun397 subset_data_ratio:' + str(subset_data_ratio))
            print('sun397 random_indexs:' + str(random_indexs))
            self.train_dataset_sub = Subset(self.train_dataset, random_indexs)
        else:
            self.train_dataset_sub = self.train_dataset

        self.train_loader_sub = torch.utils.data.DataLoader(
            self.train_dataset_sub,
            shuffle=True,
            batch_size=batch_size,
            num_workers=num_workers,
        )

        self.test_dataset = datasets.ImageFolder(valdir, transform=preprocess)
        self.test_loader = torch.utils.data.DataLoader(
            self.test_dataset,
            batch_size=batch_size,
            num_workers=num_workers
        )
        self.test_loader_shuffle = torch.utils.data.DataLoader(
            self.test_dataset,
            shuffle=True,
            batch_size=batch_size,
            num_workers=num_workers
        )
        idx_to_class = dict((v, k) for k, v in self.train_dataset.class_to_idx.items())
        self.classnames = [idx_to_class[i][2:].replace('_', ' ') for i in range(len(idx_to_class))]
