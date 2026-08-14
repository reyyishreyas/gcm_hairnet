from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import numpy as np
import torch
from torch.utils.data import Dataset
from PIL import Image


class BaseDataset(Dataset, ABC):
    def __init__(self, root_dir: str, split: str = "train", transforms: Optional[Any] = None):
        self.root_dir = Path(root_dir)
        self.split = split
        self.transforms = transforms
        self.samples = self._load_split()

    def _load_split(self) -> list:
        splits_file = self.root_dir / "splits.json"
        if not splits_file.exists():
            raise FileNotFoundError(f"splits.json not found at {splits_file}")
        import json
        with open(splits_file, "r") as f:
            splits = json.load(f)
        if self.split not in splits:
            raise ValueError(f"Split '{self.split}' not found in splits.json")
        return splits[self.split]

    @abstractmethod
    def _load_sample(self, city_name: str) -> Dict[str, Any]:
        pass

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int) -> Dict[str, Any]:
        city_name = self.samples[idx]
        sample = self._load_sample(city_name)
        if self.transforms:
            sample = self.transforms(sample)
        return sample


class GCMHAIRNetDataset(BaseDataset):
    def __init__(
        self,
        root_dir: str,
        split: str = "train",
        transforms: Optional[Any] = None,
        normalization_stats: Optional[str] = None,
    ):
        self.normalization_stats = normalization_stats
        self.stats = self._load_normalization_stats() if normalization_stats else None
        super().__init__(root_dir, split, transforms)

    def _load_normalization_stats(self) -> Optional[Dict[str, Any]]:
        if not self.normalization_stats:
            return None
        path = Path(self.normalization_stats)
        if not path.exists():
            return None
        import json
        with open(path, "r") as f:
            return json.load(f)

    def _load_sample(self, city_name: str) -> Dict[str, Any]:
        base_path = self.root_dir
        image_path = base_path / "images" / f"{city_name}_image.npy"
        gis_path = base_path / "gis" / f"{city_name}_gis.npy"
        label_path = base_path / "labels" / f"{city_name}_risk.npy"
        metadata_path = base_path / "metadata" / f"{city_name}_metadata.json"

        if not image_path.exists():
            raise FileNotFoundError(f"Image file not found: {image_path}")
        if not gis_path.exists():
            raise FileNotFoundError(f"GIS file not found: {gis_path}")
        if not label_path.exists():
            raise FileNotFoundError(f"Label file not found: {label_path}")

        image = np.load(image_path).astype(np.float32)
        if image.max() > 1.0:
            image = image / 255.0
        if image.shape[0] != 256 or image.shape[1] != 256:
            image_tensor = torch.from_numpy(image).permute(2, 0, 1).unsqueeze(0)
            image_tensor = torch.nn.functional.interpolate(image_tensor, size=(256, 256), mode="bilinear", align_corners=False)
            image = image_tensor.squeeze(0).permute(1, 2, 0).numpy()
        if image.max() > 0.0:
            image = image / image.max()
        gis = np.load(gis_path).astype(np.float32)
        label = np.load(label_path).astype(np.float32)
        if label.shape[0] != 256 or label.shape[1] != 256:
            label = np.array(Image.fromarray((label * 255).astype(np.uint8)).resize((256, 256), Image.BILINEAR)).astype(np.float32) / 255.0

        if image.ndim == 3:
            image = np.transpose(image, (2, 0, 1))
        if gis.ndim == 3:
            gis = np.transpose(gis, (2, 0, 1))
        if label.ndim == 2:
            label = np.expand_dims(label, axis=0)

        image = torch.from_numpy(image)
        gis = torch.from_numpy(gis)
        label = torch.from_numpy(label)

        metadata = {}
        if metadata_path.exists():
            import json
            with open(metadata_path, "r") as f:
                metadata = json.load(f)

        return {
            "image": image,
            "gis": gis,
            "label": label,
            "city_name": city_name,
            "metadata": metadata,
        }

    def get_city_names(self) -> list:
        return self.samples
