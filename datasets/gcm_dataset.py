import random
from typing import Optional, Tuple

import numpy as np
import torch
from torch.utils.data import DataLoader, Subset

from .base import GCMHAIRNetDataset


class _TransformSubset(Subset):
    def __init__(self, dataset, indices, transform=None):
        super().__init__(dataset, indices)
        self.transform = transform

    def __getitem__(self, idx):
        sample = self.dataset[self.indices[idx]]
        if self.transform is not None:
            sample = self.transform(sample)
        return sample


def build_dataloader(
    dataset: GCMHAIRNetDataset,
    batch_size: int,
    shuffle: bool = True,
    num_workers: int = 0,
    pin_memory: bool = False,
    prefetch_factor: int = 2,
    drop_last: bool = True,
    collate_fn: Optional[callable] = None,
) -> DataLoader:
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=num_workers,
        pin_memory=pin_memory,
        prefetch_factor=prefetch_factor if num_workers > 0 else None,
        drop_last=drop_last,
        collate_fn=collate_fn,
    )


def build_crossval_dataloaders(
    root_dir: str,
    fold: int,
    num_folds: int = 5,
    batch_size: int = 16,
    num_workers: int = 0,
    seed: int = 42,
    transforms_train: Optional[callable] = None,
    transforms_val: Optional[callable] = None,
) -> Tuple[DataLoader, DataLoader]:
    base_dataset = GCMHAIRNetDataset(root_dir=root_dir, split="train", transforms=None)
    city_names = base_dataset.get_city_names()

    rng = random.Random(seed)
    rng.shuffle(city_names)

    fold_size = len(city_names) // num_folds
    val_start = fold * fold_size
    val_end = val_start + fold_size if fold < num_folds - 1 else len(city_names)
    val_cities = city_names[val_start:val_end]
    train_cities = city_names[:val_start] + city_names[val_end:]

    train_indices = [i for i, city in enumerate(base_dataset.samples) if city in train_cities]
    val_indices = [i for i, city in enumerate(base_dataset.samples) if city in val_cities]

    train_subset = _TransformSubset(base_dataset, train_indices, transforms_train)
    val_subset = _TransformSubset(base_dataset, val_indices, transforms_val)

    train_loader = build_dataloader(
        train_subset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
    )
    val_loader = build_dataloader(
        val_subset,
        batch_size=batch_size * 2,
        shuffle=False,
        num_workers=num_workers,
        drop_last=False,
    )

    return train_loader, val_loader
