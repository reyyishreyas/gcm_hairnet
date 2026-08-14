from typing import Dict, Optional

import numpy as np
import torch
from torchvision import transforms


class IdentityTransform:
    def __call__(self, sample: Dict) -> Dict:
        return sample


class NormalizeImage:
    def __init__(self, mean: Optional[list] = None, std: Optional[list] = None):
        self.mean = torch.tensor(mean).view(-1, 1, 1) if mean else None
        self.std = torch.tensor(std).view(-1, 1, 1) if std else None

    def __call__(self, sample: Dict) -> Dict:
        image = sample["image"]
        if self.mean is not None and self.std is not None:
            image = (image - self.mean) / (self.std + 1e-8)
        sample["image"] = image
        return sample


class RandomHorizontalFlip:
    def __init__(self, p: float = 0.5):
        self.p = p

    def __call__(self, sample: Dict) -> Dict:
        if torch.rand(1).item() < self.p:
            sample["image"] = torch.flip(sample["image"], dims=[2])
            sample["gis"] = torch.flip(sample["gis"], dims=[2])
            sample["label"] = torch.flip(sample["label"], dims=[2])
        return sample


class RandomVerticalFlip:
    def __init__(self, p: float = 0.5):
        self.p = p

    def __call__(self, sample: Dict) -> Dict:
        if torch.rand(1).item() < self.p:
            sample["image"] = torch.flip(sample["image"], dims=[1])
            sample["gis"] = torch.flip(sample["gis"], dims=[1])
            sample["label"] = torch.flip(sample["label"], dims=[1])
        return sample


class RandomRotation90:
    def __call__(self, sample: Dict) -> Dict:
        k = torch.randint(0, 4, (1,)).item()
        if k > 0:
            sample["image"] = torch.rot90(sample["image"], k, dims=[1, 2])
            sample["gis"] = torch.rot90(sample["gis"], k, dims=[1, 2])
            sample["label"] = torch.rot90(sample["label"], k, dims=[1, 2])
        return sample


class RandomColorJitter:
    def __init__(self, brightness: float = 0.2, contrast: float = 0.2, saturation: float = 0.2):
        self.brightness = brightness
        self.contrast = contrast
        self.saturation = saturation

    def __call__(self, sample: Dict) -> Dict:
        image = sample["image"]
        if torch.rand(1).item() < 0.5:
            image = transforms.functional.adjust_brightness(
                image, 1.0 + torch.empty(1).uniform_(-self.brightness, self.brightness).item()
            )
        if torch.rand(1).item() < 0.5:
            image = transforms.functional.adjust_contrast(
                image, 1.0 + torch.empty(1).uniform_(-self.contrast, self.contrast).item()
            )
        if torch.rand(1).item() < 0.5:
            image = transforms.functional.adjust_saturation(
                image, 1.0 + torch.empty(1).uniform_(-self.saturation, self.saturation).item()
            )
        sample["image"] = torch.clamp(image, 0.0, 1.0)
        return sample


class RandomGaussianNoise:
    def __init__(self, std: float = 0.01, p: float = 0.3):
        self.std = std
        self.p = p

    def __call__(self, sample: Dict) -> Dict:
        if torch.rand(1).item() < self.p:
            noise = torch.randn_like(sample["image"]) * self.std
            sample["image"] = torch.clamp(sample["image"] + noise, 0.0, 1.0)
        return sample


class Compose:
    def __init__(self, transforms: list):
        self.transforms = transforms

    def __call__(self, sample: Dict) -> Dict:
        for t in self.transforms:
            sample = t(sample)
        return sample


def get_train_transforms(normalization_stats: Optional[Dict] = None) -> Compose:
    transforms_list = [
        RandomHorizontalFlip(p=0.5),
        RandomVerticalFlip(p=0.5),
        RandomRotation90(),
        RandomColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
        RandomGaussianNoise(std=0.01, p=0.3),
    ]
    if normalization_stats:
        mean = [normalization_stats.get(f"channel_{i}", {}).get("mean", 0.5) for i in range(3)]
        std = [normalization_stats.get(f"channel_{i}", {}).get("std", 0.5) for i in range(3)]
        transforms_list.append(NormalizeImage(mean=mean, std=std))
    return Compose(transforms_list)


def get_val_transforms(normalization_stats: Optional[Dict] = None) -> Compose:
    if normalization_stats:
        mean = [normalization_stats.get(f"channel_{i}", {}).get("mean", 0.5) for i in range(3)]
        std = [normalization_stats.get(f"channel_{i}", {}).get("std", 0.5) for i in range(3)]
        return Compose([NormalizeImage(mean=mean, std=std)])
    return Compose([IdentityTransform()])
