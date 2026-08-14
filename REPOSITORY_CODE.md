# GCM-HAIRNet Repository Code

Complete repository source code organized by module, with file descriptions and full implementations.

---

### `configs/__init__.py`

**Purpose:** Implementation of `__init__.py`.

```python
from utils.experiment import ConfigManager

__all__ = ["ConfigManager"]
```

---

### `data/Ahmedabad/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Ahmedabad"
base_path = r"./data\Ahmedabad\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Bannerghatta/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Bannerghatta"
base_path = r"./data\Bannerghatta\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Bhubaneswar/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Bhubaneswar"
base_path = r"./data\Bhubaneswar\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Chennai/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Chennai"
base_path = r"./data\Chennai\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Chennai_Port/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Chennai_Port"
base_path = r"./data\Chennai_Port\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Chikkaballapur/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Chikkaballapur"
base_path = r"./data\Chikkaballapur\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Delhi/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Delhi"
base_path = r"./data\Delhi\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Electronic_City/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Electronic_City"
base_path = r"./data\Electronic_City\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Hoskote/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Hoskote"
base_path = r"./data\Hoskote\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Hosur/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Hosur"
base_path = r"./data\Hosur\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Hyderabad/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Hyderabad"
base_path = r"./data\Hyderabad\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Mandya/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Mandya"
base_path = r"./data\Mandya\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Mumbai/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Mumbai"
base_path = r"./data\Mumbai\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Mysuru/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Mysuru"
base_path = r"./data\Mysuru\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Peenya/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Peenya"
base_path = r"./data\Peenya\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Pune/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Pune"
base_path = r"./data\Pune\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Ramanagara/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Ramanagara"
base_path = r"./data\Ramanagara\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `data/Whitefield/qgis/load_layers.py`

**Purpose:** Implementation of `load_layers.py`.

```python
# Batch script to load layers in QGIS
# Run in QGIS Python Console

import os
import qgis.core

aoi = "Whitefield"
base_path = r"./data\Whitefield\qgis"

# Load layers
layers = [
    ("Risk Map", os.path.join(base_path, f"{aoi}_risk.tif")),
    ("Human Exposure", os.path.join(base_path, f"{aoi}_Human_Exposure.tif")),
    ("Infrastructure", os.path.join(base_path, f"{aoi}_Infrastructure.tif")),
    ("Urban Activity", os.path.join(base_path, f"{aoi}_Urban_Activity.tif")),
    ("Environmental Buffer", os.path.join(base_path, f"{aoi}_Environmental_Buffer.tif")),
    ("Grid", os.path.join(base_path, f"{aoi}_grid.geojson")),
]

for name, path in layers:
    if os.path.exists(path):
        layer = qgis.core.QgsRasterLayer(path, name)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
            print(f"Failed to load: {path}")
```

---

### `datasets/__init__.py`

**Purpose:** Implementation of `__init__.py`.

```python
from .base import GCMHAIRNetDataset
from .gcm_dataset import build_dataloader, build_crossval_dataloaders
from .transforms import get_train_transforms, get_val_transforms

__all__ = [
    "GCMHAIRNetDataset",
    "build_dataloader",
    "build_crossval_dataloaders",
    "get_train_transforms",
    "get_val_transforms",
]
```

---

### `datasets/base.py`

**Purpose:** Defines `BaseDataset` module/class.

```python
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
```

---

### `datasets/collate.py`

**Purpose:** Contains `collate_fn` function.

```python
from typing import Any, Dict

import torch


def collate_fn(batch: list) -> Dict[str, Any]:
    images = torch.stack([b["image"] for b in batch], dim=0)
    gis = torch.stack([b["gis"] for b in batch], dim=0)
    labels = torch.stack([b["label"] for b in batch], dim=0)
    city_names = [b["city_name"] for b in batch]
    metadata = [b["metadata"] for b in batch]
    return {
        "image": images,
        "gis": gis,
        "label": labels,
        "city_name": city_names,
        "metadata": metadata,
    }
```

---

### `datasets/gcm_dataset.py`

**Purpose:** Defines `_TransformSubset` module/class.

```python
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
```

---

### `datasets/transforms.py`

**Purpose:** Defines `IdentityTransform:` module/class.

```python
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
```

---

### `docs/__init__.py`

**Purpose:** Implementation of `__init__.py`.

```python

```

---

### `engine/__init__.py`

**Purpose:** Implementation of `__init__.py`.

```python
from .trainer import Trainer
from .validator import Validator
from .tester import Tester
from .inferencer import Inferencer

__all__ = ["Trainer", "Validator", "Tester", "Inferencer"]
```

---

### `engine/engine.py`

**Purpose:** Defines `Engine:` module/class.

```python
import torch

class Engine:
    def __init__(self, model, optimizer, scheduler, loss_fn, device, gradient_clip_val=None, gradient_accumulation_steps=1):
        self.model = model
        self.optimizer = optimizer
        self.scheduler = scheduler
        self.loss_fn = loss_fn
        self.device = device
        self.gradient_clip_val = gradient_clip_val
        self.gradient_accumulation_steps = gradient_accumulation_steps
        self.step = 0
    
    def train_step(self, batch):
        self.model.train()
        image = batch["image"].to(self.device)
        gis = batch["gis"].to(self.device)
        label = batch["label"].to(self.device)
        
        preds = self.model(image, gis)
        loss = self.loss_fn(preds, label)
        loss = loss / self.gradient_accumulation_steps
        loss.backward()
        
        if (self.step + 1) % self.gradient_accumulation_steps == 0:
            if self.gradient_clip_val:
                torch.nn.utils.clip_grad_norm_(self.model.parameters(), self.gradient_clip_val)
            self.optimizer.step()
            self.optimizer.zero_grad()
            if self.scheduler and not isinstance(self.scheduler, torch.optim.lr_scheduler.ReduceLROnPlateau):
                self.scheduler.step()
        
        self.step += 1
        return {"loss": loss.item() * self.gradient_accumulation_steps}
    
    def validation_step(self, batch):
        self.model.eval()
        with torch.no_grad():
            image = batch["image"].to(self.device)
            gis = batch["gis"].to(self.device)
            label = batch["label"].to(self.device)
            
            preds = self.model(image, gis)
            loss = self.loss_fn(preds, label)
            
            return {
                "val_loss": loss.item(),
                "preds": torch.sigmoid(preds).cpu(),
                "targets": label.cpu()
            }
```

---

### `engine/inferencer.py`

**Purpose:** Defines `Inferencer:` module/class.

```python
from pathlib import Path
from typing import Any, Dict, Optional

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from utils.misc import get_device
from visualization import save_prediction_plots


class Inferencer:
    def __init__(
        self,
        model: nn.Module,
        data_loader: DataLoader,
        checkpoint_path: Optional[str] = None,
        device: Optional[torch.device] = None,
        output_dir: str = "./outputs/inference",
        save_predictions: bool = True,
        save_visualizations: bool = True,
    ):
        self.model = model
        self.data_loader = data_loader
        self.device = device or get_device()
        self.output_dir = Path(output_dir)
        self.save_predictions = save_predictions
        self.save_visualizations = save_visualizations
        self.output_dir.mkdir(parents=True, exist_ok=True)

        if checkpoint_path:
            self._load_checkpoint(checkpoint_path)

        self.model.to(self.device)
        self.model.eval()

    def _load_checkpoint(self, path: str):
        checkpoint = torch.load(path, map_location=self.device)
        ckpt_state = checkpoint["model_state_dict"]
        model_state = self.model.state_dict()
        new_state = {}
        matched = 0
        skipped = 0
        for key, param in ckpt_state.items():
            if key in model_state:
                if param.shape == model_state[key].shape:
                    new_state[key] = param
                    matched += 1
                else:
                    skipped += 1
            else:
                skipped += 1
        result = self.model.load_state_dict(new_state, strict=False)
        if result.missing_keys or result.unexpected_keys:
            print(f"Warning: Partial checkpoint load - missing: {result.missing_keys}, unexpected: {result.unexpected_keys}")
        if skipped > 0:
            print(f"Info: Loaded {matched} layers, skipped {skipped} incompatible layers from checkpoint")

    @torch.no_grad()
    def run(self) -> Dict[str, Any]:
        all_preds = []
        all_metadata = []

        for batch in self.data_loader:
            image = batch["image"].to(self.device, non_blocking=True)
            gis = batch["gis"].to(self.device, non_blocking=True)

            preds = self.model(image, gis)
            all_preds.append(torch.sigmoid(preds).cpu().numpy())
            all_metadata.extend(batch.get("metadata", []))

        predictions = np.concatenate(all_preds, axis=0)

        if self.save_predictions:
            np.save(self.output_dir / "predictions.npy", predictions)

        if self.save_visualizations and all_metadata:
            save_prediction_plots(predictions, all_metadata, str(self.output_dir))

        return {"predictions": predictions}
```

---

### `engine/tester.py`

**Purpose:** Defines `Tester:` module/class.

```python
from typing import Any, Dict, Optional

import torch
import torch.nn as nn
from torch.utils.data import DataLoader


class Tester:
    def __init__(self, model: nn.Module, test_loader: DataLoader, loss_fn: nn.Module, device: torch.device, metrics: Any, logger: Any):
        self.model = model
        self.test_loader = test_loader
        self.loss_fn = loss_fn
        self.device = device
        self.metrics = metrics
        self.logger = logger

    @torch.no_grad()
    def test(self) -> Dict[str, float]:
        self.model.eval()
        total_loss = 0.0
        num_batches = 0
        all_preds = []
        all_targets = []
        all_city_names = []

        for batch in self.test_loader:
            image = batch["image"].to(self.device, non_blocking=True)
            gis = batch["gis"].to(self.device, non_blocking=True)
            label = batch["label"].to(self.device, non_blocking=True)

            preds = self.model(image, gis)
            loss = self.loss_fn(preds, label)

            total_loss += loss.item()
            num_batches += 1
            all_preds.append(torch.sigmoid(preds).cpu().numpy())
            all_targets.append(label.cpu().numpy())
            if "city_name" in batch:
                all_city_names.extend(batch["city_name"])

        avg_loss = total_loss / max(num_batches, 1)
        metrics = {"test_loss": avg_loss}

        if all_preds:
            preds = __import__("numpy").concatenate(all_preds, axis=0)
            targets = __import__("numpy").concatenate(all_targets, axis=0)
            metrics.update(self.metrics(preds, targets))

        return metrics, all_preds, all_targets, all_city_names
```

---

### `engine/trainer.py`

**Purpose:** Defines `Trainer:` module/class.

```python
import numpy as np
from typing import Any, Dict, Optional

import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from datasets.collate import collate_fn
from losses.combined import build_loss
from metrics.regression_metrics import RegressionMetrics
from utils.checkpoint import CheckpointManager
from utils.logger import Logger
from utils.seed import count_parameters, set_seed
from .engine import Engine


class Trainer:
    def __init__(
        self,
        model: nn.Module,
        train_loader: DataLoader,
        val_loader: DataLoader,
        config: Any,
        device: torch.device,
        vis_dir: Optional[str] = None,
    ):
        self.model = model
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.config = config
        self.device = device
        self.epoch = 0
        self.global_step = 0
        self.vis_dir = vis_dir

        self._setup_training()

    def _setup_training(self):
        set_seed(self.config.get("experiment", {}).get("seed", 42))

        self.optimizer = torch.optim.AdamW(
            self.model.parameters(),
            lr=self.config.get("training", {}).get("optimizer", {}).get("lr", 1e-4),
            weight_decay=self.config.get("training", {}).get("optimizer", {}).get("weight_decay", 1e-4),
            betas=tuple(self.config.get("training", {}).get("optimizer", {}).get("betas", [0.9, 0.999])),
        )

        scheduler_config = self.config.get("training", {}).get("scheduler", {})
        self.warmup_epochs = scheduler_config.get("warmup_epochs", 0)
        self.base_lr = self.config.get("training", {}).get("optimizer", {}).get("lr", 1e-4)
        if scheduler_config.get("type") == "cosine_annealing":
            self.scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
                self.optimizer,
                T_max=scheduler_config.get("T_max", 100),
                eta_min=scheduler_config.get("eta_min", 1e-6),
            )
        else:
            self.scheduler = None

        self.loss_fn = build_loss(self.config.get("training", {}).get("loss", {}))

        checkpoint_config = self.config.get("checkpoint", {})
        self.checkpoint_manager = CheckpointManager(
            checkpoint_dir=checkpoint_config.get("dir", "./checkpoints"),
            monitor=checkpoint_config.get("monitor", "val_loss"),
            mode=checkpoint_config.get("mode", "min"),
            save_top_k=checkpoint_config.get("save_top_k", 5),
            save_last=checkpoint_config.get("save_last", True),
            every_n_epochs=checkpoint_config.get("every_n_epochs", 1),
        )

        logger_config = self.config.get("logger", {})
        self.logger = Logger(
            log_dir=logger_config.get("log_dir", "./logs"),
            experiment_name=self.config.get("experiment", {}).get("name", "gcm_hairnet"),
            use_tensorboard=True,
            config=self.config.to_dict() if hasattr(self.config, "to_dict") else dict(self.config),
        )

        self.metric_fn = RegressionMetrics()
        self.num_epochs = self.config.get("training", {}).get("epochs", 100)

    def train_epoch(self) -> Dict[str, float]:
        self.model.train()
        total_loss = 0.0
        num_batches = 0

        for batch in self.train_loader:
            metrics = self.engine.train_step(batch)
            total_loss += metrics["loss"]
            num_batches += 1

            if self.global_step % self.config.get("logger", {}).get("log_every_n_steps", 50) == 0:
                self.logger.log_metrics({"train_loss_step": metrics["loss"]}, self.global_step, prefix="train")

        avg_loss = total_loss / max(num_batches, 1)
        self.logger.log_metrics({"train_loss_epoch": avg_loss}, self.epoch, prefix="train")
        return {"train_loss": avg_loss}

    @torch.no_grad()
    def validate_epoch(self) -> Dict[str, float]:
        self.model.eval()
        total_loss = 0.0
        num_batches = 0
        all_preds = []
        all_targets = []

        for batch in self.val_loader:
            result = self.engine.validation_step(batch)
            total_loss += result["val_loss"]
            num_batches += 1
            all_preds.append(result["preds"].numpy())
            all_targets.append(result["targets"].numpy())

        avg_loss = total_loss / max(num_batches, 1)

        if all_preds:
            preds = np.concatenate(all_preds, axis=0)
            targets = np.concatenate(all_targets, axis=0)
            metrics = self.metric_fn(preds, targets)
            metrics["val_loss"] = avg_loss
            self.logger.log_metrics(metrics, self.epoch, prefix="val")
            if self.vis_dir and hasattr(self.model, "use_gcm") and self.model.use_gcm:
                try:
                    from visualization import save_gcm_priors, save_gcm_attention_maps, save_scene_weights
                    sample_batch = next(iter(self.val_loader))
                    sample_image = sample_batch["image"].to(self.device)
                    sample_gis = sample_batch["gis"].to(self.device)
                    with torch.no_grad():
                        inter = self.model.get_intermediate_features(sample_image, sample_gis)
                    if "gcm_attention" in inter:
                        save_gcm_attention_maps(inter["gcm_attention"], self.vis_dir, self.epoch)
                    if hasattr(self.model.gcm.grm, "scene_weight_predictor"):
                        scene_weights = self.model.gcm.grm.scene_weight_predictor(sample_gis)
                        save_scene_weights(scene_weights, self.vis_dir, self.epoch)
                except Exception:
                    pass
            return metrics

        self.logger.log_metrics({"val_loss": avg_loss}, self.epoch, prefix="val")
        return {"val_loss": avg_loss}

    def fit(self, epoch_callback=None):
        self.model.to(self.device)
        self.engine = Engine(
            model=self.model,
            optimizer=self.optimizer,
            scheduler=self.scheduler,
            loss_fn=self.loss_fn,
            device=self.device,
            gradient_clip_val=self.config.get("training", {}).get("gradient_clip_val"),
            gradient_accumulation_steps=self.config.get("training", {}).get("gradient_accumulation_steps", 1),
        )

        param_info = count_parameters(self.model)
        print(f"Total parameters: {param_info['total']:,}")
        print(f"Trainable parameters: {param_info['trainable']:,}")

        early_stopping_config = self.config.get("training", {}).get("early_stopping", {})
        patience = early_stopping_config.get("patience", 0)
        monitor = early_stopping_config.get("monitor", "val_loss")
        mode = early_stopping_config.get("mode", "min")
        best_value = float("inf") if mode == "min" else float("-inf")
        epochs_no_improve = 0

        for epoch in range(self.epoch, self.num_epochs):
            self.epoch = epoch

            if self.scheduler:
                if epoch < self.warmup_epochs:
                    lr_scale = (epoch + 1) / self.warmup_epochs
                    for param_group in self.optimizer.param_groups:
                        param_group["lr"] = self.base_lr * lr_scale

            train_metrics = self.train_epoch()
            val_metrics = self.validate_epoch()

            val_loss = val_metrics.get("val_loss", float("inf"))
            print(f"Epoch {epoch:03d} | Train Loss: {train_metrics['train_loss']:.4f} | Val Loss: {val_loss:.4f}")

            if epoch_callback is not None:
                epoch_callback(epoch, val_metrics)

            checkpoint_state = {
                "epoch": epoch,
                "model_state_dict": self.model.state_dict(),
                "optimizer_state_dict": self.optimizer.state_dict(),
                "metrics": val_metrics,
            }
            self.checkpoint_manager.save(checkpoint_state, epoch, val_metrics)

            current_value = val_metrics.get(monitor, val_metrics.get("val_loss", float("inf")))
            if mode == "min":
                improved = current_value < best_value
            else:
                improved = current_value > best_value

            if improved:
                best_value = current_value
                epochs_no_improve = 0
            else:
                epochs_no_improve += 1

            if patience > 0 and epochs_no_improve >= patience:
                print(f"Early stopping triggered at epoch {epoch}. Best {monitor}: {best_value:.4f}")
                break

            if self.scheduler and epoch >= self.warmup_epochs:
                self.scheduler.step()

        self.logger.close()

    def resume(self, checkpoint_path: Optional[str] = None):
        path = checkpoint_path or self.checkpoint_manager.get_last_checkpoint()
        if path:
            start_epoch, metrics = self.checkpoint_manager.load(path, self.model, self.optimizer, self.device)
            self.epoch = start_epoch
            print(f"Resumed from epoch {start_epoch}")
```

---

### `engine/validator.py`

**Purpose:** Defines `Validator:` module/class.

```python
from typing import Any, Dict, Optional

import torch
import torch.nn as nn
from torch.utils.data import DataLoader


class Validator:
    def __init__(self, model: nn.Module, val_loader: DataLoader, loss_fn: nn.Module, device: torch.device, metrics: Any, logger: Any):
        self.model = model
        self.val_loader = val_loader
        self.loss_fn = loss_fn
        self.device = device
        self.metrics = metrics
        self.logger = logger

    @torch.no_grad()
    def validate(self) -> Dict[str, float]:
        self.model.eval()
        total_loss = 0.0
        num_batches = 0
        all_preds = []
        all_targets = []

        for batch in self.val_loader:
            image = batch["image"].to(self.device, non_blocking=True)
            gis = batch["gis"].to(self.device, non_blocking=True)
            label = batch["label"].to(self.device, non_blocking=True)

            preds = self.model(image, gis)
            loss = self.loss_fn(preds, label)

            total_loss += loss.item()
            num_batches += 1
            all_preds.append(torch.sigmoid(preds).cpu().numpy())
            all_targets.append(label.cpu().numpy())

        avg_loss = total_loss / max(num_batches, 1)
        metrics = {"val_loss": avg_loss}

        if all_preds:
            preds = __import__("numpy").concatenate(all_preds, axis=0)
            targets = __import__("numpy").concatenate(all_targets, axis=0)
            metrics.update(self.metrics(preds, targets))

        return metrics
```

---

### `losses/__init__.py`

**Purpose:** Implementation of `__init__.py`.

```python
from .base import BaseLoss, L1Loss, FocalLoss
from .mse import MSELoss
from .ssim import SSIMLoss
from .edge_loss import EdgeLoss
from .combined import CombinedLoss, build_loss

__all__ = [
    "BaseLoss",
    "MSELoss",
    "L1Loss",
    "FocalLoss",
    "SSIMLoss",
    "EdgeLoss",
    "CombinedLoss",
    "build_loss",
]
```

---

### `losses/base.py`

**Purpose:** Defines `BaseLoss` module/class.

```python
from abc import ABC, abstractmethod
from typing import Dict

import torch
import torch.nn as nn
import torch.nn.functional as F


class BaseLoss(nn.Module, ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def forward(self, preds: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        pass

    @abstractmethod
    def get_components(self) -> Dict[str, torch.Tensor]:
        pass


class MSELoss(BaseLoss):
    def __init__(self, reduction: str = "mean"):
        super().__init__()
        self.reduction = reduction
        self.mse = nn.MSELoss(reduction=reduction)

    def forward(self, preds: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        return self.mse(preds, targets)

    def get_components(self) -> Dict[str, torch.Tensor]:
        return {"mse_loss": self.forward(torch.tensor(0.0), torch.tensor(0.0))}


class L1Loss(BaseLoss):
    def __init__(self, reduction: str = "mean"):
        super().__init__()
        self.reduction = reduction
        self.l1 = nn.L1Loss(reduction=reduction)

    def forward(self, preds: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        return self.l1(preds, targets)

    def get_components(self) -> Dict[str, torch.Tensor]:
        return {"l1_loss": self.forward(torch.tensor(0.0), torch.tensor(0.0))}


class FocalLoss(BaseLoss):
    def __init__(self, alpha: float = 0.25, gamma: float = 2.0, reduction: str = "mean"):
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.reduction = reduction

    def forward(self, preds: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        bce = F.binary_cross_entropy_with_logits(preds, targets, reduction="none")
        p_t = torch.exp(-bce)
        focal_weight = self.alpha * (1 - p_t) ** self.gamma
        loss = focal_weight * bce
        if self.reduction == "mean":
            return loss.mean()
        elif self.reduction == "sum":
            return loss.sum()
        return loss

    def get_components(self) -> Dict[str, torch.Tensor]:
        return {"focal_loss": self.forward(torch.tensor(0.0), torch.tensor(0.0))}
```

---

### `losses/combined.py`

**Purpose:** Defines `HuberLoss` module/class.

```python
from typing import Dict

import torch
import torch.nn as nn
import torch.nn.functional as F

from .base import BaseLoss, L1Loss, FocalLoss
from .mse import MSELoss
from .ssim import SSIMLoss


class HuberLoss(BaseLoss):
    def __init__(self, delta: float = 0.1, reduction: str = "mean"):
        super().__init__()
        self.delta = delta
        self.reduction = reduction

    def forward(self, preds: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        diff = torch.abs(preds - targets)
        mask = diff < self.delta
        loss = torch.where(mask, 0.5 * diff ** 2, self.delta * (diff - 0.5 * self.delta))
        if self.reduction == "mean":
            return loss.mean()
        elif self.reduction == "sum":
            return loss.sum()
        return loss

    def get_components(self) -> Dict[str, torch.Tensor]:
        return {"huber_loss": self.forward(torch.tensor(0.0), torch.tensor(0.0))}


class CombinedLoss(BaseLoss):
    def __init__(
        self,
        mse_weight: float = 1.0,
        l1_weight: float = 0.5,
        focal_weight: float = 0.0,
        focal_alpha: float = 0.25,
        focal_gamma: float = 2.0,
        huber_weight: float = 0.5,
        huber_delta: float = 0.1,
        ssim_weight: float = 0.0,
        ssim_window_size: int = 11,
    ):
        super().__init__()
        self.mse_weight = mse_weight
        self.l1_weight = l1_weight
        self.focal_weight = focal_weight
        self.huber_weight = huber_weight
        self.ssim_weight = ssim_weight
        self.mse_loss = MSELoss()
        self.l1_loss = L1Loss()
        self.focal_loss = FocalLoss(alpha=focal_alpha, gamma=focal_gamma)
        self.huber_loss = HuberLoss(delta=huber_delta)
        self.ssim_loss = SSIMLoss(window_size=ssim_window_size)

    def forward(self, preds: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        probs = torch.sigmoid(preds)
        mse = self.mse_loss(probs, targets) * self.mse_weight
        l1 = self.l1_loss(probs, targets) * self.l1_weight
        huber = self.huber_loss(probs, targets) * self.huber_weight
        focal = self.focal_loss(preds, targets) * self.focal_weight
        total = mse + l1 + huber + focal
        if self.ssim_weight > 0:
            ssim = self.ssim_loss(probs, targets) * self.ssim_weight
            total = total + ssim
        return total

    def get_components(self) -> Dict[str, torch.Tensor]:
        dummy = torch.tensor(0.0)
        return {
            "mse_loss": self.mse_loss.forward(dummy, dummy),
            "l1_loss": self.l1_loss.forward(dummy, dummy),
            "huber_loss": self.huber_loss.forward(dummy, dummy),
            "focal_loss": self.focal_loss.forward(dummy, dummy),
            "total_loss": torch.tensor(0.0),
        }


def build_loss(config: Dict) -> nn.Module:
    loss_type = config.get("type", "combined")
    if loss_type == "mse":
        return nn.MSELoss()
    elif loss_type == "l1":
        return nn.L1Loss()
    elif loss_type == "focal":
        return nn.BCEWithLogitsLoss()
    elif loss_type == "smooth_l1":
        return nn.SmoothL1Loss(beta=config.get("smooth_l1_beta", 0.1))
    elif loss_type == "combined":
        return CombinedLoss(
            mse_weight=config.get("mse_weight", 1.0),
            l1_weight=config.get("l1_weight", 0.5),
            focal_weight=config.get("focal_weight", 0.0),
            focal_alpha=config.get("focal_alpha", 0.25),
            focal_gamma=config.get("focal_gamma", 2.0),
            huber_weight=config.get("huber_weight", 0.5),
            huber_delta=config.get("huber_delta", 0.1),
            ssim_weight=config.get("ssim_weight", 0.0),
            ssim_window_size=config.get("ssim_window_size", 11),
        )
    else:
        raise ValueError(f"Unknown loss type: {loss_type}")
```

---

### `losses/edge_loss.py`

**Purpose:** Defines `EdgeLoss` module/class.

```python
from typing import Dict

import torch
import torch.nn as nn
import torch.nn.functional as F


class EdgeLoss(nn.Module):
    def __init__(self, reduction: str = "mean"):
        super().__init__()
        self.reduction = reduction
        sobel_x = torch.tensor([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=torch.float32)
        sobel_y = torch.tensor([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=torch.float32)
        self.register_buffer("sobel_x", sobel_x.view(1, 1, 3, 3))
        self.register_buffer("sobel_y", sobel_y.view(1, 1, 3, 3))

    def forward(self, preds: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        if preds.numel() == 1:
            return torch.tensor(0.0, device=preds.device)
        if preds.ndim == 3:
            preds = preds.unsqueeze(1)
        if targets.ndim == 3:
            targets = targets.unsqueeze(1)

        sobel_x = self.sobel_x.to(preds.device)
        sobel_y = self.sobel_y.to(preds.device)

        preds_grad_x = F.conv2d(preds, sobel_x, padding=1)
        preds_grad_y = F.conv2d(preds, sobel_y, padding=1)
        preds_edge = torch.sqrt(preds_grad_x ** 2 + preds_grad_y ** 2 + 1e-8)

        targets_grad_x = F.conv2d(targets, sobel_x, padding=1)
        targets_grad_y = F.conv2d(targets, sobel_y, padding=1)
        targets_edge = torch.sqrt(targets_grad_x ** 2 + targets_grad_y ** 2 + 1e-8)

        return F.l1_loss(preds_edge, targets_edge, reduction=self.reduction)

    def get_components(self) -> Dict[str, torch.Tensor]:
        return {"edge_loss": self.forward(torch.tensor(0.0), torch.tensor(0.0))}
```

---

### `losses/mse.py`

**Purpose:** Defines `MSELoss` module/class.

```python
from typing import Dict

import torch
import torch.nn as nn


class MSELoss(nn.Module):
    def __init__(self, reduction: str = "mean"):
        super().__init__()
        self.reduction = reduction
        self.mse = nn.MSELoss(reduction=reduction)

    def forward(self, preds: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        return self.mse(preds, targets)

    def get_components(self) -> Dict[str, torch.Tensor]:
        return {"mse_loss": self.forward(torch.tensor(0.0), torch.tensor(0.0))}
```

---

### `losses/ssim.py`

**Purpose:** Contains `create_window` function.

```python
from typing import Dict

import torch
import torch.nn as nn
import torch.nn.functional as F


def create_window(window_size: int, channel: int, device: torch.device) -> torch.Tensor:
    gauss = torch.Tensor(
        [torch.exp(torch.tensor(-((x - window_size // 2) ** 2) / (2 * 1.5**2))) for x in range(window_size)]
    )
    gauss = gauss / gauss.sum()
    window = gauss.unsqueeze(0).unsqueeze(0).repeat(channel, 1, 1, 1)
    return window.to(device)


def ssim(
    preds: torch.Tensor,
    targets: torch.Tensor,
    window_size: int = 11,
    reduction: str = "mean",
    device: torch.device = None,
) -> torch.Tensor:
    if device is None:
        device = preds.device

    C1 = 0.01**2
    C2 = 0.03**2

    channel = preds.shape[1]
    window = create_window(window_size, channel, device)
    mu1 = F.conv2d(preds, window, padding=window_size // 2, groups=channel)
    mu2 = F.conv2d(targets, window, padding=window_size // 2, groups=channel)

    mu1_sq = mu1.pow(2)
    mu2_sq = mu2.pow(2)
    mu1_mu2 = mu1 * mu2

    sigma1_sq = F.conv2d(preds.pow(2), window, padding=window_size // 2, groups=channel) - mu1_sq
    sigma2_sq = F.conv2d(targets.pow(2), window, padding=window_size // 2, groups=channel) - mu2_sq
    sigma12 = F.conv2d(preds * targets, window, padding=window_size // 2, groups=channel) - mu1_mu2

    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / (
        (mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2)
    )

    if reduction == "mean":
        return ssim_map.mean()
    elif reduction == "sum":
        return ssim_map.sum()
    return ssim_map


class SSIMLoss(nn.Module):
    def __init__(self, window_size: int = 11, reduction: str = "mean"):
        super().__init__()
        self.window_size = window_size
        self.reduction = reduction

    def forward(self, preds: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        return 1.0 - ssim(preds, targets, self.window_size, self.reduction, preds.device)

    def get_components(self) -> Dict[str, torch.Tensor]:
        return {"ssim_loss": self.forward(torch.tensor(0.0), torch.tensor(0.0))}
```

---

### `metrics/__init__.py`

**Purpose:** Implementation of `__init__.py`.

```python
from .base import BaseMetric, MSEMetric, MAEMetric, R2Metric, Evaluator, AccuracyMetric, F1Metric, PrecisionMetric, RecallMetric, IoUMetric
from .regression_metrics import RegressionMetrics
from .classification_metrics import ClassificationMetrics
from .mse import MSEMetric as MSEMetricV2
from .mae import MAEMetric as MAEMetricV2
from .rmse import RMSEMetric
from .ssim import SSIMMetric
from .psnr import PSNRMetric
from .pearson import PearsonMetric
from .spearman import SpearmanMetric
from .moran import MoranMetric

__all__ = [
    "BaseMetric",
    "MSEMetric",
    "MAEMetric",
    "R2Metric",
    "Evaluator",
    "AccuracyMetric",
    "F1Metric",
    "PrecisionMetric",
    "RecallMetric",
    "IoUMetric",
    "RegressionMetrics",
    "ClassificationMetrics",
    "MSEMetricV2",
    "MAEMetricV2",
    "RMSEMetric",
    "SSIMMetric",
    "PSNRMetric",
    "PearsonMetric",
    "SpearmanMetric",
    "MoranMetric",
]
```

---

### `metrics/base.py`

**Purpose:** Defines `BaseMetric:` module/class.

```python
import numpy as np
from typing import Dict, List, Optional


class BaseMetric:
    def __init__(self, name: str):
        self.name = name
        self.values = []

    def reset(self) -> None:
        self.values = []

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        raise NotImplementedError

    def compute(self) -> float:
        raise NotImplementedError

    def __call__(self, preds: np.ndarray, targets: np.ndarray) -> float:
        self.update(preds, targets)
        return self.compute()


class MSEMetric(BaseMetric):
    def __init__(self):
        super().__init__("mse")
        self._sum = 0.0
        self._count = 0

    def reset(self) -> None:
        self._sum = 0.0
        self._count = 0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        self._sum += np.mean((preds - targets) ** 2)
        self._count += 1

    def compute(self) -> float:
        return self._sum / max(self._count, 1)


class MAEMetric(BaseMetric):
    def __init__(self):
        super().__init__("mae")
        self._sum = 0.0
        self._count = 0

    def reset(self) -> None:
        self._sum = 0.0
        self._count = 0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        self._sum += np.mean(np.abs(preds - targets))
        self._count += 1

    def compute(self) -> float:
        return self._sum / max(self._count, 1)


class R2Metric(BaseMetric):
    def __init__(self):
        super().__init__("r2")
        self._preds = []
        self._targets = []

    def reset(self) -> None:
        self._preds = []
        self._targets = []

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        self._preds.append(preds.flatten())
        self._targets.append(targets.flatten())

    def compute(self) -> float:
        preds = np.concatenate(self._preds)
        targets = np.concatenate(self._targets)
        ss_res = np.sum((targets - preds) ** 2)
        ss_tot = np.sum((targets - np.mean(targets)) ** 2)
        return 1 - ss_res / (ss_tot + 1e-8)


class AccuracyMetric(BaseMetric):
    def __init__(self, threshold: float = 0.5):
        super().__init__("accuracy")
        self.threshold = threshold
        self._sum = 0.0
        self._count = 0

    def reset(self) -> None:
        self._sum = 0.0
        self._count = 0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        preds_bin = (preds > self.threshold).astype(int)
        targets_bin = (targets > self.threshold).astype(int)
        self._sum += np.mean(preds_bin == targets_bin)
        self._count += 1

    def compute(self) -> float:
        return self._sum / max(self._count, 1)


class F1Metric(BaseMetric):
    def __init__(self, threshold: float = 0.5):
        super().__init__("f1")
        self.threshold = threshold
        self._tp = 0.0
        self._fp = 0.0
        self._fn = 0.0

    def reset(self) -> None:
        self._tp = 0.0
        self._fp = 0.0
        self._fn = 0.0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        preds_bin = (preds > self.threshold).astype(int)
        targets_bin = (targets > self.threshold).astype(int)
        self._tp += np.sum((preds_bin == 1) & (targets_bin == 1))
        self._fp += np.sum((preds_bin == 1) & (targets_bin == 0))
        self._fn += np.sum((preds_bin == 0) & (targets_bin == 1))

    def compute(self) -> float:
        prec = self._tp / (self._tp + self._fp + 1e-8)
        rec = self._tp / (self._tp + self._fn + 1e-8)
        return 2 * prec * rec / (prec + rec + 1e-8)


class PrecisionMetric(BaseMetric):
    def __init__(self, threshold: float = 0.5):
        super().__init__("precision")
        self.threshold = threshold
        self._tp = 0.0
        self._fp = 0.0

    def reset(self) -> None:
        self._tp = 0.0
        self._fp = 0.0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        preds_bin = (preds > self.threshold).astype(int)
        targets_bin = (targets > self.threshold).astype(int)
        self._tp += np.sum((preds_bin == 1) & (targets_bin == 1))
        self._fp += np.sum((preds_bin == 1) & (targets_bin == 0))

    def compute(self) -> float:
        return self._tp / (self._tp + self._fp + 1e-8)


class RecallMetric(BaseMetric):
    def __init__(self, threshold: float = 0.5):
        super().__init__("recall")
        self.threshold = threshold
        self._tp = 0.0
        self._fn = 0.0

    def reset(self) -> None:
        self._tp = 0.0
        self._fn = 0.0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        preds_bin = (preds > self.threshold).astype(int)
        targets_bin = (targets > self.threshold).astype(int)
        self._tp += np.sum((preds_bin == 1) & (targets_bin == 1))
        self._fn += np.sum((preds_bin == 0) & (targets_bin == 1))

    def compute(self) -> float:
        return self._tp / (self._tp + self._fn + 1e-8)


class IoUMetric(BaseMetric):
    def __init__(self, threshold: float = 0.5):
        super().__init__("iou")
        self.threshold = threshold
        self._tp = 0.0
        self._union = 0.0

    def reset(self) -> None:
        self._tp = 0.0
        self._union = 0.0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        preds_bin = (preds > self.threshold).astype(int)
        targets_bin = (targets > self.threshold).astype(int)
        self._tp += np.sum((preds_bin == 1) & (targets_bin == 1))
        self._union += np.sum((preds_bin == 1) | (targets_bin == 1))

    def compute(self) -> float:
        return self._tp / (self._union + 1e-8)


class Evaluator:
    def __init__(self, metrics: Optional[List[BaseMetric]] = None, threshold: float = 0.5):
        if metrics is not None:
            self.metrics = metrics
        else:
            self.metrics = [
                MSEMetric(),
                MAEMetric(),
                R2Metric(),
                AccuracyMetric(threshold),
                F1Metric(threshold),
                PrecisionMetric(threshold),
                RecallMetric(threshold),
                IoUMetric(threshold),
            ]

    def reset(self) -> None:
        for m in self.metrics:
            m.reset()

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        for m in self.metrics:
            m.update(preds, targets)

    def compute_all(self) -> Dict[str, float]:
        return {m.name: m.compute() for m in self.metrics}

    def __call__(self, preds: np.ndarray, targets: np.ndarray) -> Dict[str, float]:
        self.update(preds, targets)
        return self.compute_all()
```

---

### `metrics/classification_metrics.py`

**Purpose:** Defines `ClassificationMetrics:` module/class.

```python
import numpy as np
from typing import Dict, List


class ClassificationMetrics:
    @staticmethod
    def accuracy(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        preds_bin = (preds > threshold).astype(int)
        targets_bin = (targets > threshold).astype(int)
        return float(np.mean(preds_bin == targets_bin))

    @staticmethod
    def precision(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        preds_bin = (preds > threshold).astype(int)
        targets_bin = (targets > threshold).astype(int)
        tp = np.sum((preds_bin == 1) & (targets_bin == 1))
        fp = np.sum((preds_bin == 1) & (targets_bin == 0))
        return float(tp / (tp + fp + 1e-8))

    @staticmethod
    def recall(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        preds_bin = (preds > threshold).astype(int)
        targets_bin = (targets > threshold).astype(int)
        tp = np.sum((preds_bin == 1) & (targets_bin == 1))
        fn = np.sum((preds_bin == 0) & (targets_bin == 1))
        return float(tp / (tp + fn + 1e-8))

    @staticmethod
    def f1(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        precision = ClassificationMetrics.precision(preds, targets, threshold)
        recall = ClassificationMetrics.recall(preds, targets, threshold)
        return float(2 * precision * recall / (precision + recall + 1e-8))

    @staticmethod
    def iou(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        preds_bin = (preds > threshold).astype(int)
        targets_bin = (targets > threshold).astype(int)
        intersection = np.sum((preds_bin == 1) & (targets_bin == 1))
        union = np.sum((preds_bin == 1) | (targets_bin == 1))
        return float(intersection / (union + 1e-8))

    @staticmethod
    def specificity(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        preds_bin = (preds > threshold).astype(int)
        targets_bin = (targets > threshold).astype(int)
        tn = np.sum((preds_bin == 0) & (targets_bin == 0))
        fp = np.sum((preds_bin == 1) & (targets_bin == 0))
        return float(tn / (tn + fp + 1e-8))

    def __call__(self, preds, targets) -> Dict[str, float]:
        return {
            "accuracy": self.accuracy(preds, targets),
            "precision": self.precision(preds, targets),
            "recall": self.recall(preds, targets),
            "f1": self.f1(preds, targets),
            "iou": self.iou(preds, targets),
            "specificity": self.specificity(preds, targets),
        }
```

---

### `metrics/mae.py`

**Purpose:** Defines `MAEMetric:` module/class.

```python
import numpy as np
from typing import Optional


class MAEMetric:
    def __init__(self):
        self._sum = 0.0
        self._count = 0

    def reset(self) -> None:
        self._sum = 0.0
        self._count = 0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        self._sum += np.mean(np.abs(preds - targets))
        self._count += 1

    def compute(self) -> float:
        return self._sum / max(self._count, 1)

    @staticmethod
    def compute_static(preds: np.ndarray, targets: np.ndarray) -> float:
        return float(np.mean(np.abs(preds - targets)))
```

---

### `metrics/moran.py`

**Purpose:** Defines `MoranMetric:` module/class.

```python
from typing import Optional

import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.csgraph import laplacian


class MoranMetric:
    @staticmethod
    def compute(preds: np.ndarray, targets: np.ndarray) -> float:
        try:
            x = targets.flatten()
            n = len(x)
            if n < 4:
                return 0.0
            
            mean = np.mean(x)
            x_centered = x - mean
            variance = np.var(x)
            if variance < 1e-8:
                return 0.0
            
            spatial_lag = np.zeros(n)
            grid_size = int(np.sqrt(n))
            for i in range(n):
                row, col = i // grid_size, i % grid_size
                neighbors = []
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < grid_size and 0 <= nc < grid_size:
                        neighbors.append(nr * grid_size + nc)
                if neighbors:
                    spatial_lag[i] = np.mean([x_centered[j] for j in neighbors])
            
            moran = np.sum(x_centered * spatial_lag) / (np.sum(x_centered ** 2) / n)
            return float(np.clip(moran, -1.0, 1.0))
        except Exception:
            return 0.0
```

---

### `metrics/mse.py`

**Purpose:** Defines `MSEMetric:` module/class.

```python
import numpy as np
from typing import Optional


class MSEMetric:
    def __init__(self):
        self._sum = 0.0
        self._count = 0

    def reset(self) -> None:
        self._sum = 0.0
        self._count = 0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        self._sum += np.mean((preds - targets) ** 2)
        self._count += 1

    def compute(self) -> float:
        return self._sum / max(self._count, 1)

    @staticmethod
    def compute_static(preds: np.ndarray, targets: np.ndarray) -> float:
        return float(np.mean((preds - targets) ** 2))
```

---

### `metrics/pearson.py`

**Purpose:** Defines `PearsonMetric:` module/class.

```python
from typing import Optional

import numpy as np
from scipy.stats import pearsonr


class PearsonMetric:
    @staticmethod
    def compute(preds: np.ndarray, targets: np.ndarray) -> float:
        preds_flat = preds.flatten()
        targets_flat = targets.flatten()
        if len(preds_flat) < 2:
            return 0.0
        corr, _ = pearsonr(preds_flat, targets_flat)
        return float(corr) if not np.isnan(corr) else 0.0
```

---

### `metrics/psnr.py`

**Purpose:** Defines `PSNRMetric:` module/class.

```python
import numpy as np
from typing import Optional


class PSNRMetric:
    def __init__(self, max_val: float = 1.0):
        self.max_val = max_val

    def compute(self, preds: np.ndarray, targets: np.ndarray) -> float:
        mse = np.mean((preds - targets) ** 2)
        if mse == 0:
            return 100.0
        return 20 * np.log10(self.max_val / np.sqrt(mse))
```

---

### `metrics/regression_metrics.py`

**Purpose:** Defines `RegressionMetrics:` module/class.

```python
import numpy as np
from typing import Dict, List


class RegressionMetrics:
    @staticmethod
    def mse(preds: np.ndarray, targets: np.ndarray) -> float:
        return float(np.mean((preds - targets) ** 2))

    @staticmethod
    def mae(preds: np.ndarray, targets: np.ndarray) -> float:
        return float(np.mean(np.abs(preds - targets)))

    @staticmethod
    def rmse(preds: np.ndarray, targets: np.ndarray) -> float:
        return float(np.sqrt(np.mean((preds - targets) ** 2)))

    @staticmethod
    def r2(preds: np.ndarray, targets: np.ndarray) -> float:
        ss_res = np.sum((targets - preds) ** 2)
        ss_tot = np.sum((targets - np.mean(targets)) ** 2)
        return float(1 - ss_res / (ss_tot + 1e-8))

    @staticmethod
    def mape(preds: np.ndarray, targets: np.ndarray) -> float:
        return float(np.mean(np.abs((targets - preds) / (targets + 1e-8))) * 100)

    @staticmethod
    def accuracy(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        preds_bin = (preds > threshold).astype(int)
        targets_bin = (targets > threshold).astype(int)
        return float(np.mean(preds_bin == targets_bin))

    @staticmethod
    def precision(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        preds_bin = (preds > threshold).astype(int)
        targets_bin = (targets > threshold).astype(int)
        tp = np.sum((preds_bin == 1) & (targets_bin == 1))
        fp = np.sum((preds_bin == 1) & (targets_bin == 0))
        return float(tp / (tp + fp + 1e-8))

    @staticmethod
    def recall(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        preds_bin = (preds > threshold).astype(int)
        targets_bin = (targets > threshold).astype(int)
        tp = np.sum((preds_bin == 1) & (targets_bin == 1))
        fn = np.sum((preds_bin == 0) & (targets_bin == 1))
        return float(tp / (tp + fn + 1e-8))

    @staticmethod
    def f1(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        precision = RegressionMetrics.precision(preds, targets, threshold)
        recall = RegressionMetrics.recall(preds, targets, threshold)
        return float(2 * precision * recall / (precision + recall + 1e-8))

    @staticmethod
    def iou(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        preds_bin = (preds > threshold).astype(int)
        targets_bin = (targets > threshold).astype(int)
        intersection = np.sum((preds_bin == 1) & (targets_bin == 1))
        union = np.sum((preds_bin == 1) | (targets_bin == 1))
        return float(intersection / (union + 1e-8))

    def __call__(self, preds, targets):
        """Make class callable"""
        return {
            "mse": self.mse(preds, targets),
            "mae": self.mae(preds, targets),
            "rmse": self.rmse(preds, targets),
            "r2": self.r2(preds, targets),
            "mape": self.mape(preds, targets),
            "accuracy": self.accuracy(preds, targets),
            "f1": self.f1(preds, targets),
            "precision": self.precision(preds, targets),
            "recall": self.recall(preds, targets),
            "iou": self.iou(preds, targets),
        }
```

---

### `metrics/rmse.py`

**Purpose:** Defines `RMSEMetric:` module/class.

```python
import numpy as np
from typing import Optional


class RMSEMetric:
    def __init__(self):
        self._sum = 0.0
        self._count = 0

    def reset(self) -> None:
        self._sum = 0.0
        self._count = 0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        self._sum += np.sqrt(np.mean((preds - targets) ** 2))
        self._count += 1

    def compute(self) -> float:
        return self._sum / max(self._count, 1)

    @staticmethod
    def compute_static(preds: np.ndarray, targets: np.ndarray) -> float:
        return float(np.sqrt(np.mean((preds - targets) ** 2)))
```

---

### `metrics/spearman.py`

**Purpose:** Defines `SpearmanMetric:` module/class.

```python
from typing import Optional

import numpy as np
from scipy.stats import spearmanr


class SpearmanMetric:
    @staticmethod
    def compute(preds: np.ndarray, targets: np.ndarray) -> float:
        preds_flat = preds.flatten()
        targets_flat = targets.flatten()
        if len(preds_flat) < 2:
            return 0.0
        corr, _ = spearmanr(preds_flat, targets_flat)
        return float(corr) if not np.isnan(corr) else 0.0
```

---

### `metrics/ssim.py`

**Purpose:** Defines `SSIMMetric:` module/class.

```python
from typing import Optional

import numpy as np
import torch
import torch.nn as nn


class SSIMMetric:
    def __init__(self, data_range: float = 1.0):
        self.data_range = data_range

    def _ssim_torch(self, preds: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        C1 = (0.01 * self.data_range) ** 2
        C2 = (0.03 * self.data_range) ** 2

        kernel_size = 11
        sigma = 1.5
        channels = preds.shape[1]
        kernel = self._create_gaussian_kernel(kernel_size, sigma, channels).to(preds.device)

        mu1 = torch.nn.functional.conv2d(preds, kernel, padding=kernel_size // 2, groups=channels)
        mu2 = torch.nn.functional.conv2d(targets, kernel, padding=kernel_size // 2, groups=channels)

        mu1_sq = mu1 ** 2
        mu2_sq = mu2 ** 2
        mu1_mu2 = mu1 * mu2

        sigma1_sq = torch.nn.functional.conv2d(preds ** 2, kernel, padding=kernel_size // 2, groups=channels) - mu1_sq
        sigma2_sq = torch.nn.functional.conv2d(targets ** 2, kernel, padding=kernel_size // 2, groups=channels) - mu2_sq
        sigma12 = torch.nn.functional.conv2d(preds * targets, kernel, padding=kernel_size // 2, groups=channels) - mu1_mu2

        ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2))
        return ssim_map.mean()

    def _create_gaussian_kernel(self, kernel_size: int, sigma: float, channels: int) -> torch.Tensor:
        x = torch.arange(kernel_size, dtype=torch.float32) - kernel_size // 2
        g = torch.exp(-x ** 2 / (2 * sigma ** 2))
        g = g / g.sum()
        kernel = g.unsqueeze(0) * g.unsqueeze(1)
        kernel = kernel.expand(channels, 1, kernel_size, kernel_size).contiguous()
        return kernel

    def compute(self, preds: np.ndarray, targets: np.ndarray) -> float:
        try:
            if preds.ndim == 2:
                preds = preds[np.newaxis, np.newaxis, ...]
                targets = targets[np.newaxis, np.newaxis, ...]
            elif preds.ndim == 3:
                preds = preds[np.newaxis, ...]
                targets = targets[np.newaxis, ...]

            preds_tensor = torch.from_numpy(preds).float()
            targets_tensor = torch.from_numpy(targets).float()

            if preds_tensor.shape[1] == 1:
                preds_tensor = preds_tensor.repeat(1, 3, 1, 1)
                targets_tensor = targets_tensor.repeat(1, 3, 1, 1)

            ssim_val = self._ssim_torch(preds_tensor, targets_tensor)
            return float(ssim_val.item())
        except Exception:
            return 0.0
```

---

### `models/__init__.py`

**Purpose:** Contains `build_model` function.

```python
from typing import Dict

from .base import BaseModel
from .encoders.swin import SwinTransformerEncoder
from .encoders.gis_encoder import GISEncoder
from .fusion.gct import GatedCrossAttention
from .gcm.grm import GeographicRelationMatrix
from .graph_relation import GraphRelationModule
from .decoder.risk_decoder import Decoder
from .gcm_hairnet import GCMHAIRNet
from .baselines.tiny_cnn import TinyRiskCNN
from .baselines.baseline_model import BaselineModel
from .baselines.ablation_model import AblationModel
from .baselines.gcm_hairnet_baseline import GCMHAIRNetBaseline
from .baselines.modality_models import ImageOnlyModel, GISOnlyModel


def build_model(config: Dict):
    model_name = config.get("name", "GCM-HAIRNet")
    if model_name == "GCM-HAIRNet":
        return GCMHAIRNet(config)
    elif model_name == "TinyRiskCNN":
        return TinyRiskCNN(config)
    elif model_name == "BaselineModel":
        return BaselineModel(config)
    elif model_name == "AblationModel":
        return AblationModel(config)
    elif model_name == "GCMHAIRNetBaseline":
        return GCMHAIRNetBaseline(config)
    elif model_name == "ImageOnlyModel":
        return ImageOnlyModel(config)
    elif model_name == "GISOnlyModel":
        return GISOnlyModel(config)
    else:
        raise ValueError(f"Unknown model: {model_name}")


__all__ = [
    "BaseModel",
    "SwinTransformerEncoder",
    "GISEncoder",
    "GatedCrossAttention",
    "GeographicRelationMatrix",
    "GraphRelationModule",
    "Decoder",
    "GCMHAIRNet",
    "TinyRiskCNN",
    "BaselineModel",
    "AblationModel",
    "GCMHAIRNetBaseline",
    "ImageOnlyModel",
    "GISOnlyModel",
    "build_model",
]
```

---

### `models/base.py`

**Purpose:** Defines `BaseModel` module/class.

```python
from abc import ABC, abstractmethod
from typing import Dict, Optional, Tuple

import torch
import torch.nn as nn


class BaseModel(nn.Module, ABC):
    def __init__(self, config: Optional[Dict] = None):
        super().__init__()
        self.config = config or {}

    @abstractmethod
    def forward(self, image: torch.Tensor, gis: torch.Tensor) -> torch.Tensor:
        pass

    @abstractmethod
    def get_intermediate_features(self, image: torch.Tensor, gis: torch.Tensor) -> Dict[str, torch.Tensor]:
        pass
```

---

### `models/baselines/__init__.py`

**Purpose:** Implementation of `__init__.py`.

```python
from .tiny_cnn import TinyRiskCNN
from .gcm_hairnet_baseline import GCMHAIRNetBaseline

__all__ = ["TinyRiskCNN", "GCMHAIRNetBaseline"]
```

---

### `models/baselines/ablation_model.py`

**Purpose:** Defines `AblationModel` module/class.

```python
from typing import Dict

import torch
import torch.nn as nn

from ..base import BaseModel
from ..encoders.swin import SwinTransformerEncoder
from ..encoders.gis_encoder import GISEncoder
from ..fusion.gct import GatedCrossAttention
from .fusion import (
    ConcatFusion,
    AdditionFusion,
    GatedFusion,
    CrossAttentionFusion,
    MultiHeadCrossAttentionFusion,
    BilinearFusion,
)
from ..graph_relation import GraphRelationModule
from ..decoder.risk_decoder import Decoder


class AblationModel(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.image_encoder = SwinTransformerEncoder(config.get("image_encoder", {}))
        self.gis_encoder = GISEncoder(config.get("gis_encoder", {}))
        self.hidden_dim = config.get("decoder", {}).get("hidden_dim", 128)

        gct_config = dict(config.get("gct", {}))
        gct_config.setdefault("gis_input_dim", self.gis_encoder.output_dim)
        self.use_gct = config.get("gct", {}).get("enable", True)
        self.fusion_type = config.get("gct", {}).get("type", "gated_cross_attention")

        if self.use_gct and self.fusion_type == "gated_cross_attention":
            self.fusion = GatedCrossAttention(gct_config)
        else:
            self.fusion = None
            self.simple_fusion = self._build_simple_fusion(config.get("fusion", {}))

        gcm_config = config.get("gcm", {})
        self.use_gcm = gcm_config.get("enable", True)
        if self.use_gcm:
            from models.gcm.gcm_block import GCMBlock
            self.gcm = GCMBlock(gcm_config)
            self.gcm_proj = nn.Conv2d(
                self.image_encoder.embed_dim + self.gis_encoder.input_channels,
                gcm_config.get("embed_dim", 512),
                kernel_size=1,
            )
            self.decoder_proj = nn.Conv2d(
                gcm_config.get("embed_dim", 512),
                self.hidden_dim,
                kernel_size=1,
            )

        self.grm = GraphRelationModule(config.get("grm", {}))
        self.decoder = Decoder(config.get("decoder", {}))

    def _build_simple_fusion(self, fusion_config: Dict):
        fusion_type = fusion_config.get("type", "concat")
        dropout = fusion_config.get("dropout", 0.1)
        img_dim = self.image_encoder.embed_dim
        gis_dim = self.gis_encoder.output_dim

        if fusion_type == "concat":
            return ConcatFusion(img_dim, gis_dim, self.hidden_dim, dropout)
        elif fusion_type == "addition":
            return AdditionFusion(img_dim, gis_dim, self.hidden_dim, dropout)
        elif fusion_type == "gated":
            return GatedFusion(img_dim, gis_dim, self.hidden_dim, dropout)
        elif fusion_type == "cross_attention":
            return CrossAttentionFusion(img_dim, gis_dim, self.hidden_dim, dropout)
        elif fusion_type == "multihead_cross_attention":
            return MultiHeadCrossAttentionFusion(img_dim, gis_dim, self.hidden_dim, fusion_config.get("num_heads", 8), dropout)
        elif fusion_type == "bilinear":
            return BilinearFusion(img_dim, gis_dim, self.hidden_dim, fusion_config.get("rank", 32), dropout)
        else:
            return ConcatFusion(img_dim, gis_dim, self.hidden_dim, dropout)

    def forward(self, image: torch.Tensor, gis: torch.Tensor) -> torch.Tensor:
        image_feats = self.image_encoder(image)
        gis_feats = self.gis_encoder(gis)

        if self.fusion is not None:
            fused_feats = self.fusion(image_feats, gis_feats)
        else:
            fused_feats = self.simple_fusion(image_feats, gis_feats)

        B, N, C = fused_feats.shape
        H = W = int(N ** 0.5)
        spatial_feats = fused_feats.transpose(1, 2).reshape(B, C, H, W)

        if self.use_gcm:
            upsampled_gis = nn.functional.interpolate(gis, size=(H, W), mode="bilinear", align_corners=False)
            concat_feats = torch.cat([spatial_feats, upsampled_gis], dim=1)
            projected = self.gcm_proj(concat_feats)
            projected = nn.functional.layer_norm(projected, projected.shape[1:])
            B, C, H, W = projected.shape
            tokens = projected.flatten(2).transpose(1, 2)
            gis_for_priors = nn.functional.interpolate(gis, size=(H, W), mode="bilinear", align_corners=False)
            gis_embeddings = None
            if hasattr(self.gis_encoder, "encoder"):
                with torch.no_grad():
                    gis_embeddings = self.gis_encoder(gis_for_priors)
            tokens, _ = self.gcm(tokens, gis_for_priors, gis_embeddings)
            spatial_feats = tokens.transpose(1, 2).reshape(B, C, H, W)
            spatial_feats = self.decoder_proj(spatial_feats)

        B, C, H, W = spatial_feats.shape
        tokens = spatial_feats.flatten(2).transpose(1, 2)
        refined_tokens = self.grm(tokens)
        spatial_feats = refined_tokens.transpose(1, 2).reshape(B, C, H, W)

        output = self.decoder(spatial_feats, spatial_size=(256, 256))
        return output

    def get_intermediate_features(self, image: torch.Tensor, gis: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = {}
        features["image_encoder"] = self.image_encoder.get_intermediate_features(image)
        features["gis_encoder"] = self.gis_encoder.get_intermediate_features(gis)
        image_feats = features["image_encoder"]["final"]
        gis_feats = features["gis_encoder"]["final"]

        if self.fusion is not None:
            features["gct"] = self.fusion.get_intermediate_features(image_feats, gis_feats) if hasattr(self.fusion, "get_intermediate_features") else {"gct_output": self.fusion(image_feats, gis_feats)}
            fused_feats = features["gct"]["gct_output"] if "gct_output" in features["gct"] else self.fusion(image_feats, gis_feats)
        else:
            features["fusion"] = {"fusion_output": self.simple_fusion(image_feats, gis_feats)}
            fused_feats = features["fusion"]["fusion_output"]

        B, N, C = fused_feats.shape
        H = W = int(N ** 0.5)
        spatial_feats = fused_feats.transpose(1, 2).reshape(B, C, H, W)

        if self.use_gcm:
            upsampled_gis = nn.functional.interpolate(gis, size=(H, W), mode="bilinear", align_corners=False)
            concat_feats = torch.cat([spatial_feats, upsampled_gis], dim=1)
            projected = self.gcm_proj(concat_feats)
            projected = nn.functional.layer_norm(projected, projected.shape[1:])
            B, C, H, W = projected.shape
            tokens = projected.flatten(2).transpose(1, 2)
            features["gcm_input"] = tokens
            gis_for_priors = nn.functional.interpolate(gis, size=(H, W), mode="bilinear", align_corners=False)
            gis_embeddings = None
            if hasattr(self.gis_encoder, "encoder"):
                with torch.no_grad():
                    gis_embeddings = self.gis_encoder(gis_for_priors)
            gcm_out, gcm_attn_maps = self.gcm(tokens, gis_for_priors, gis_embeddings)
            features["gcm_output"] = gcm_out
            features["gcm_attention"] = gcm_attn_maps
            spatial_feats = gcm_out.transpose(1, 2).reshape(B, C, H, W)
            spatial_feats = self.decoder_proj(spatial_feats)

        features["graph_relation_input"] = spatial_feats.flatten(2).transpose(1, 2)
        refined_tokens = self.grm(features["graph_relation_input"])
        features["graph_relation_output"] = refined_tokens
        B, C, H, W = spatial_feats.shape
        spatial_feats = refined_tokens.transpose(1, 2).reshape(B, C, H, W)

        features["decoder_input"] = spatial_feats
        features["decoder"] = self.decoder.get_intermediate_features(spatial_feats, (256, 256))
        return features
```

---

### `models/baselines/baseline_model.py`

**Purpose:** Defines `BaselineModel` module/class.

```python
from typing import Dict

import torch
import torch.nn as nn

from ..base import BaseModel
from ..encoders.swin import SwinTransformerEncoder
from ..encoders.gis_encoder import GISEncoder
from ..graph_relation import GraphRelationModule
from ..decoder.risk_decoder import Decoder
from .fusion import (
    ConcatFusion,
    AdditionFusion,
    GatedFusion,
    CrossAttentionFusion,
    MultiHeadCrossAttentionFusion,
    BilinearFusion,
)


class BaselineModel(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.image_encoder = SwinTransformerEncoder(config.get("image_encoder", {}))
        self.gis_encoder = GISEncoder(config.get("gis_encoder", {}))
        self.hidden_dim = config.get("decoder", {}).get("hidden_dim", 128)

        fusion_config = config.get("fusion", {})
        fusion_type = fusion_config.get("type", "concat")
        dropout = fusion_config.get("dropout", 0.1)

        if fusion_type == "concat":
            self.fusion = ConcatFusion(
                image_dim=self.image_encoder.embed_dim,
                gis_dim=self.gis_encoder.output_dim,
                output_dim=self.hidden_dim,
                dropout=dropout,
            )
        elif fusion_type == "addition":
            self.fusion = AdditionFusion(
                image_dim=self.image_encoder.embed_dim,
                gis_dim=self.gis_encoder.output_dim,
                output_dim=self.hidden_dim,
                dropout=dropout,
            )
        elif fusion_type == "gated":
            self.fusion = GatedFusion(
                image_dim=self.image_encoder.embed_dim,
                gis_dim=self.gis_encoder.output_dim,
                output_dim=self.hidden_dim,
                dropout=dropout,
            )
        elif fusion_type == "cross_attention":
            self.fusion = CrossAttentionFusion(
                image_dim=self.image_encoder.embed_dim,
                gis_dim=self.gis_encoder.output_dim,
                output_dim=self.hidden_dim,
                dropout=dropout,
            )
        elif fusion_type == "multihead_cross_attention":
            self.fusion = MultiHeadCrossAttentionFusion(
                image_dim=self.image_encoder.embed_dim,
                gis_dim=self.gis_encoder.output_dim,
                output_dim=self.hidden_dim,
                num_heads=fusion_config.get("num_heads", 8),
                dropout=dropout,
            )
        elif fusion_type == "bilinear":
            self.fusion = BilinearFusion(
                image_dim=self.image_encoder.embed_dim,
                gis_dim=self.gis_encoder.output_dim,
                output_dim=self.hidden_dim,
                rank=fusion_config.get("rank", 32),
                dropout=dropout,
            )
        else:
            raise ValueError(f"Unknown fusion type: {fusion_type}")

        self.grm = GraphRelationModule(config.get("grm", {}))
        self.decoder = Decoder(config.get("decoder", {}))

    def forward(self, image: torch.Tensor, gis: torch.Tensor) -> torch.Tensor:
        image_feats = self.image_encoder(image)
        gis_feats = self.gis_encoder(gis)
        fused = self.fusion(image_feats, gis_feats)

        B, N, C = fused.shape
        H = W = int(N ** 0.5)
        spatial_feats = fused.transpose(1, 2).reshape(B, C, H, W)

        tokens = spatial_feats.flatten(2).transpose(1, 2)
        refined_tokens = self.grm(tokens)
        spatial_feats = refined_tokens.transpose(1, 2).reshape(B, C, H, W)

        output = self.decoder(spatial_feats, spatial_size=(256, 256))
        return output

    def get_intermediate_features(self, image: torch.Tensor, gis: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = {}
        features["image_encoder"] = self.image_encoder.get_intermediate_features(image)
        features["gis_encoder"] = self.gis_encoder.get_intermediate_features(gis)
        image_feats = features["image_encoder"]["final"]
        gis_feats = features["gis_encoder"]["final"]
        features["fusion"] = self.fusion(image_feats, gis_feats)
        features["fusion_input"] = {"image": image_feats, "gis": gis_feats}

        B, N, C = features["fusion"].shape
        H = W = int(N ** 0.5)
        spatial_feats = features["fusion"].transpose(1, 2).reshape(B, C, H, W)
        features["graph_relation_input"] = spatial_feats.flatten(2).transpose(1, 2)
        refined_tokens = self.grm(features["graph_relation_input"])
        features["graph_relation_output"] = refined_tokens
        spatial_feats = refined_tokens.transpose(1, 2).reshape(B, C, H, W)
        features["decoder_input"] = spatial_feats
        features["decoder"] = self.decoder.get_intermediate_features(spatial_feats, (256, 256))
        return features
```

---

### `models/baselines/fusion.py`

**Purpose:** Defines `ConcatFusion` module/class.

```python
from typing import Dict

import torch
import torch.nn as nn


class ConcatFusion(nn.Module):
    def __init__(self, image_dim: int = 128, gis_dim: int = 64, output_dim: int = 128, dropout: float = 0.1):
        super().__init__()
        self.proj = nn.Sequential(
            nn.Linear(image_dim + gis_dim, output_dim),
            nn.LayerNorm(output_dim),
            nn.Dropout(dropout),
        )

    def forward(self, image_feats: torch.Tensor, gis_feats: torch.Tensor) -> torch.Tensor:
        if gis_feats.shape[1] != image_feats.shape[1]:
            gis_feats = nn.functional.interpolate(
                gis_feats.transpose(1, 2).reshape(gis_feats.shape[0], gis_feats.shape[2], int(gis_feats.shape[1] ** 0.5), int(gis_feats.shape[1] ** 0.5)),
                size=(int(image_feats.shape[1] ** 0.5), int(image_feats.shape[1] ** 0.5)),
                mode="bilinear",
                align_corners=False,
            ).flatten(2).transpose(1, 2)
        concat = torch.cat([image_feats, gis_feats], dim=-1)
        return self.proj(concat)


class AdditionFusion(nn.Module):
    def __init__(self, image_dim: int = 128, gis_dim: int = 64, output_dim: int = 128, dropout: float = 0.1):
        super().__init__()
        self.image_proj = nn.Linear(image_dim, output_dim)
        self.gis_proj = nn.Linear(gis_dim, output_dim)
        self.norm = nn.LayerNorm(output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, image_feats: torch.Tensor, gis_feats: torch.Tensor) -> torch.Tensor:
        if gis_feats.shape[1] != image_feats.shape[1]:
            B, N, C = gis_feats.shape
            side = int(N ** 0.5)
            gis_feats = nn.functional.interpolate(
                gis_feats.transpose(1, 2).reshape(B, C, side, side),
                size=(int(image_feats.shape[1] ** 0.5), int(image_feats.shape[1] ** 0.5)),
                mode="bilinear",
                align_corners=False,
            ).flatten(2).transpose(1, 2)
        img = self.image_proj(image_feats)
        gis = self.gis_proj(gis_feats)
        fused = img + gis
        return self.norm(fused)


class GatedFusion(nn.Module):
    def __init__(self, image_dim: int = 128, gis_dim: int = 64, output_dim: int = 128, dropout: float = 0.1):
        super().__init__()
        self.gate = nn.Sequential(
            nn.Linear(image_dim + gis_dim, output_dim),
            nn.Sigmoid(),
        )
        self.image_proj = nn.Linear(image_dim, output_dim)
        self.gis_proj = nn.Linear(gis_dim, output_dim)
        self.norm = nn.LayerNorm(output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, image_feats: torch.Tensor, gis_feats: torch.Tensor) -> torch.Tensor:
        if gis_feats.shape[1] != image_feats.shape[1]:
            B, N, C = gis_feats.shape
            side = int(N ** 0.5)
            gis_feats = nn.functional.interpolate(
                gis_feats.transpose(1, 2).reshape(B, C, side, side),
                size=(int(image_feats.shape[1] ** 0.5), int(image_feats.shape[1] ** 0.5)),
                mode="bilinear",
                align_corners=False,
            ).flatten(2).transpose(1, 2)
        concat = torch.cat([image_feats, gis_feats], dim=-1)
        g = self.gate(concat)
        img = self.image_proj(image_feats)
        gis = self.gis_proj(gis_feats)
        fused = g * img + (1 - g) * gis
        return self.norm(fused)


class CrossAttentionFusion(nn.Module):
    def __init__(self, image_dim: int = 128, gis_dim: int = 64, output_dim: int = 128, dropout: float = 0.1):
        super().__init__()
        self.q_proj = nn.Linear(image_dim, output_dim)
        self.k_proj = nn.Linear(gis_dim, output_dim)
        self.v_proj = nn.Linear(gis_dim, output_dim)
        self.out_proj = nn.Linear(output_dim, output_dim)
        self.norm = nn.LayerNorm(output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, image_feats: torch.Tensor, gis_feats: torch.Tensor) -> torch.Tensor:
        if gis_feats.shape[1] != image_feats.shape[1]:
            B, N, C = gis_feats.shape
            side = int(N ** 0.5)
            target_side = int(image_feats.shape[1] ** 0.5)
            gis_feats = nn.functional.interpolate(
                gis_feats.transpose(1, 2).reshape(B, C, side, side),
                size=(target_side, target_side),
                mode="bilinear",
                align_corners=False,
            ).flatten(2).transpose(1, 2)
        q = self.q_proj(image_feats)
        k = self.k_proj(gis_feats)
        v = self.v_proj(gis_feats)
        attn = torch.matmul(q, k.transpose(-2, -1)) / (self.q_proj.out_features ** 0.5)
        attn = torch.softmax(attn, dim=-1)
        attn = self.dropout(attn)
        out = torch.matmul(attn, v)
        out = self.out_proj(out)
        return self.norm(out + image_feats)


class MultiHeadCrossAttentionFusion(nn.Module):
    def __init__(self, image_dim: int = 128, gis_dim: int = 64, output_dim: int = 128, num_heads: int = 8, dropout: float = 0.1):
        super().__init__()
        assert output_dim % num_heads == 0
        self.num_heads = num_heads
        self.head_dim = output_dim // num_heads
        self.q_proj = nn.Linear(image_dim, output_dim)
        self.k_proj = nn.Linear(gis_dim, output_dim)
        self.v_proj = nn.Linear(gis_dim, output_dim)
        self.out_proj = nn.Linear(output_dim, output_dim)
        self.norm = nn.LayerNorm(output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, image_feats: torch.Tensor, gis_feats: torch.Tensor) -> torch.Tensor:
        if gis_feats.shape[1] != image_feats.shape[1]:
            B, N, C = gis_feats.shape
            side = int(N ** 0.5)
            gis_feats = nn.functional.interpolate(
                gis_feats.transpose(1, 2).reshape(B, C, side, side),
                size=(int(image_feats.shape[1] ** 0.5), int(image_feats.shape[1] ** 0.5)),
                mode="bilinear",
                align_corners=False,
            ).flatten(2).transpose(1, 2)
        B, N, _ = image_feats.shape
        q = self.q_proj(image_feats).reshape(B, N, self.num_heads, self.head_dim).transpose(1, 2)
        k = self.k_proj(gis_feats).reshape(B, -1, self.num_heads, self.head_dim).transpose(1, 2)
        v = self.v_proj(gis_feats).reshape(B, -1, self.num_heads, self.head_dim).transpose(1, 2)
        attn = torch.matmul(q, k.transpose(-2, -1)) / (self.head_dim ** 0.5)
        attn = torch.softmax(attn, dim=-1)
        attn = self.dropout(attn)
        out = torch.matmul(attn, v)
        out = out.transpose(1, 2).reshape(B, N, -1)
        out = self.out_proj(out)
        return self.norm(out + image_feats)


class BilinearFusion(nn.Module):
    def __init__(self, image_dim: int = 128, gis_dim: int = 64, output_dim: int = 128, rank: int = 32, dropout: float = 0.1):
        super().__init__()
        self.image_proj = nn.Linear(image_dim, rank)
        self.gis_proj = nn.Linear(gis_dim, rank)
        self.out_proj = nn.Sequential(
            nn.Linear(rank, output_dim),
            nn.LayerNorm(output_dim),
            nn.Dropout(dropout),
        )
        self.norm = nn.LayerNorm(output_dim)

    def forward(self, image_feats: torch.Tensor, gis_feats: torch.Tensor) -> torch.Tensor:
        if gis_feats.shape[1] != image_feats.shape[1]:
            B, N, C = gis_feats.shape
            side = int(N ** 0.5)
            gis_feats = nn.functional.interpolate(
                gis_feats.transpose(1, 2).reshape(B, C, side, side),
                size=(int(image_feats.shape[1] ** 0.5), int(image_feats.shape[1] ** 0.5)),
                mode="bilinear",
                align_corners=False,
            ).flatten(2).transpose(1, 2)
        img = self.image_proj(image_feats)
        gis = self.gis_proj(gis_feats)
        bilinear = img * gis
        out = self.out_proj(bilinear)
        return self.norm(out + image_feats)
```

---

### `models/baselines/gcm_hairnet_baseline.py`

**Purpose:** Defines `GCMHAIRNetBaseline` module/class.

```python
from typing import Dict, Optional

import torch
import torch.nn as nn

from ..base import BaseModel
from ..encoders.swin import SwinTransformerEncoder
from ..encoders.gis_encoder import GISEncoder
from ..baselines.fusion import AdditionFusion, ConcatFusion
from ..graph_relation import GraphRelationModule
from ..decoder.risk_decoder import Decoder
from ..relation import build_relation_module


class GCMHAIRNetBaseline(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.image_encoder = SwinTransformerEncoder(config.get("image_encoder", {}))
        self.gis_encoder = GISEncoder(config.get("gis_encoder", {}))
        self.hidden_dim = config.get("decoder", {}).get("hidden_dim", 128)
        self.image_size = config.get("image_size", 256)
        self.gis_size = config.get("gis_size", 32)

        fusion_config = config.get("fusion", {})
        fusion_type = fusion_config.get("type", "addition")
        fusion_dropout = fusion_config.get("dropout", 0.2)

        if fusion_type == "addition":
            self.fusion = AdditionFusion(
                image_dim=self.image_encoder.embed_dim,
                gis_dim=self.gis_encoder.output_dim,
                output_dim=self.hidden_dim,
                dropout=fusion_dropout,
            )
        elif fusion_type == "concat":
            self.fusion = ConcatFusion(
                image_dim=self.image_encoder.embed_dim,
                gis_dim=self.gis_encoder.output_dim,
                output_dim=self.hidden_dim,
                dropout=fusion_dropout,
            )
        else:
            self.fusion = AdditionFusion(
                image_dim=self.image_encoder.embed_dim,
                gis_dim=self.gis_encoder.output_dim,
                output_dim=self.hidden_dim,
                dropout=fusion_dropout,
            )

        gcm_config = config.get("gcm", {})
        self.use_gcm = gcm_config.get("enable", True)
        self.relation_type = "gcm" if self.use_gcm else config.get("relation_module", {}).get("type", "vit")

        if self.use_gcm:
            rel_config = dict(gcm_config)
            rel_config["type"] = "gcm"
            rel_config["hidden_dim"] = self.hidden_dim
            self.relation_module = build_relation_module(rel_config)

            gcm_embed_dim = gcm_config.get("embed_dim", 512)
            self.gcm_proj = nn.Conv2d(
                self.image_encoder.embed_dim + self.gis_encoder.input_channels,
                gcm_embed_dim,
                kernel_size=1,
            )
            self.decoder_proj = nn.Conv2d(
                gcm_embed_dim,
                self.hidden_dim,
                kernel_size=1,
            )
        else:
            rel_config = dict(config.get("relation_module", {}))
            rel_config["type"] = self.relation_type
            rel_config["hidden_dim"] = self.hidden_dim
            rel_config["num_heads"] = self.hidden_dim // 16
            self.relation_module = build_relation_module(rel_config)

        self.graph_relation_module = GraphRelationModule(config.get("grm", {}))
        self.decoder = Decoder(config.get("decoder", {}))

    @property
    def swin(self):
        return self.image_encoder

    @property
    def grm(self):
        return self.graph_relation_module

    def forward(self, image: torch.Tensor, gis: torch.Tensor) -> torch.Tensor:
        image_feats = self.image_encoder(image)
        gis_feats = self.gis_encoder(gis)

        fused_feats = self.fusion(image_feats, gis_feats)

        B, N, C = fused_feats.shape
        H = W = int(N ** 0.5)
        spatial_feats = fused_feats.transpose(1, 2).reshape(B, C, H, W)

        if self.use_gcm:
            upsampled_gis = nn.functional.interpolate(
                gis, size=(H, W), mode="bilinear", align_corners=False
            )
            concat_feats = torch.cat([spatial_feats, upsampled_gis], dim=1)
            projected = self.gcm_proj(concat_feats)
            projected = nn.functional.layer_norm(projected, projected.shape[1:])
            B, C, H, W = projected.shape
            tokens = projected.flatten(2).transpose(1, 2)

            gis_for_priors = nn.functional.interpolate(
                gis, size=(H, W), mode="bilinear", align_corners=False
            )
            gis_embeddings = None
            if hasattr(self.gis_encoder, "encoder"):
                with torch.no_grad():
                    gis_embeddings = self.gis_encoder(gis_for_priors)

            tokens, _ = self.relation_module(tokens, gis_for_priors, gis_embeddings)
            spatial_feats = tokens.transpose(1, 2).reshape(B, C, H, W)
            spatial_feats = self.decoder_proj(spatial_feats)
        else:
            tokens = spatial_feats.flatten(2).transpose(1, 2)
            tokens = self.relation_module(tokens)
            spatial_feats = tokens.transpose(1, 2).reshape(B, -1, H, W)

        B, C, H, W = spatial_feats.shape
        tokens = spatial_feats.flatten(2).transpose(1, 2)
        refined_tokens = self.graph_relation_module(tokens)
        spatial_feats = refined_tokens.transpose(1, 2).reshape(B, C, H, W)

        output = self.decoder(spatial_feats, spatial_size=(self.image_size, self.image_size))
        return output

    def get_intermediate_features(self, image: torch.Tensor, gis: torch.Tensor) -> Dict:
        features = {}
        features["image_encoder"] = self.image_encoder.get_intermediate_features(image)
        features["gis_encoder"] = self.gis_encoder.get_intermediate_features(gis)
        image_feats = features["image_encoder"]["final"]
        gis_feats = features["gis_encoder"]["final"]
        fused_feats = self.fusion(image_feats, gis_feats)

        B, N, C = fused_feats.shape
        H = W = int(N ** 0.5)
        spatial_feats = fused_feats.transpose(1, 2).reshape(B, C, H, W)

        if self.use_gcm:
            upsampled_gis = nn.functional.interpolate(
                gis, size=(H, W), mode="bilinear", align_corners=False
            )
            concat_feats = torch.cat([spatial_feats, upsampled_gis], dim=1)
            projected = self.gcm_proj(concat_feats)
            projected = nn.functional.layer_norm(projected, projected.shape[1:])
            B, C, H, W = projected.shape
            tokens = projected.flatten(2).transpose(1, 2)
            features["gcm_input"] = tokens
            gis_for_priors = nn.functional.interpolate(
                gis, size=(H, W), mode="bilinear", align_corners=False
            )
            gis_embeddings = None
            if hasattr(self.gis_encoder, "encoder"):
                with torch.no_grad():
                    gis_embeddings = self.gis_encoder(gis_for_priors)
            gcm_out, gcm_attn_maps = self.relation_module(tokens, gis_for_priors, gis_embeddings)
            features["gcm_output"] = gcm_out
            features["gcm_attention"] = gcm_attn_maps
            spatial_feats = gcm_out.transpose(1, 2).reshape(B, C, H, W)
            spatial_feats = self.decoder_proj(spatial_feats)
        else:
            features["relation_input"] = spatial_feats.flatten(2).transpose(1, 2)
            rel_out = self.relation_module(features["relation_input"])
            features["relation_output"] = rel_out
            spatial_feats = rel_out.transpose(1, 2).reshape(B, -1, H, W)

        features["graph_relation_input"] = spatial_feats.flatten(2).transpose(1, 2)
        refined_tokens = self.graph_relation_module(features["graph_relation_input"])
        features["graph_relation_output"] = refined_tokens
        B, C, H, W = spatial_feats.shape
        spatial_feats = refined_tokens.transpose(1, 2).reshape(B, C, H, W)

        features["decoder_input"] = spatial_feats
        features["decoder"] = self.decoder.get_intermediate_features(spatial_feats, (self.image_size, self.image_size))
        return features
```

---

### `models/baselines/modality_models.py`

**Purpose:** Defines `ImageOnlyModel` module/class.

```python
from typing import Dict

import torch
import torch.nn as nn

from ..base import BaseModel
from ..encoders.swin import SwinTransformerEncoder
from ..encoders.gis_encoder import GISEncoder
from ..graph_relation import GraphRelationModule
from ..decoder.risk_decoder import Decoder


class ImageOnlyModel(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.image_encoder = SwinTransformerEncoder(config.get("image_encoder", {}))
        self.grm = GraphRelationModule(config.get("grm", {}))
        self.decoder = Decoder(config.get("decoder", {}))
        self.proj = nn.Linear(self.image_encoder.embed_dim, self.decoder.hidden_dim)

    def forward(self, image: torch.Tensor, gis: torch.Tensor) -> torch.Tensor:
        feats = self.image_encoder(image)
        B, N, C = feats.shape
        H = W = int(N ** 0.5)
        spatial = self.proj(feats).transpose(1, 2).reshape(B, self.decoder.hidden_dim, H, W)
        tokens = spatial.flatten(2).transpose(1, 2)
        refined = self.grm(tokens)
        spatial = refined.transpose(1, 2).reshape(B, self.decoder.hidden_dim, H, W)
        return self.decoder(spatial, spatial_size=(256, 256))

    def get_intermediate_features(self, image: torch.Tensor, gis: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = {}
        features["image_encoder"] = self.image_encoder.get_intermediate_features(image)
        feats = features["image_encoder"]["final"]
        B, N, C = feats.shape
        H = W = int(N ** 0.5)
        spatial = self.proj(feats).transpose(1, 2).reshape(B, self.decoder.hidden_dim, H, W)
        features["decoder_input"] = spatial
        features["decoder"] = self.decoder.get_intermediate_features(spatial, (256, 256))
        return features


class GISOnlyModel(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.gis_encoder = GISEncoder(config.get("gis_encoder", {}))
        self.grm = GraphRelationModule(config.get("grm", {}))
        self.decoder = Decoder(config.get("decoder", {}))
        self.proj = nn.Linear(self.gis_encoder.output_dim, self.decoder.hidden_dim)

    def forward(self, image: torch.Tensor, gis: torch.Tensor) -> torch.Tensor:
        feats = self.gis_encoder(gis)
        B, N, C = feats.shape
        H = W = int(N ** 0.5)
        spatial = self.proj(feats).transpose(1, 2).reshape(B, self.decoder.hidden_dim, H, W)
        tokens = spatial.flatten(2).transpose(1, 2)
        refined = self.grm(tokens)
        spatial = refined.transpose(1, 2).reshape(B, self.decoder.hidden_dim, H, W)
        return self.decoder(spatial, spatial_size=(256, 256))

    def get_intermediate_features(self, image: torch.Tensor, gis: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = {}
        features["gis_encoder"] = self.gis_encoder.get_intermediate_features(gis)
        feats = features["gis_encoder"]["final"]
        B, N, C = feats.shape
        H = W = int(N ** 0.5)
        spatial = self.proj(feats).transpose(1, 2).reshape(B, self.decoder.hidden_dim, H, W)
        features["decoder_input"] = spatial
        features["decoder"] = self.decoder.get_intermediate_features(spatial, (256, 256))
        return features
```

---

### `models/baselines/tiny_cnn.py`

**Purpose:** Defines `TinyRiskCNN` module/class.

```python
from typing import Dict

import torch
import torch.nn as nn

from ..base import BaseModel


class TinyRiskCNN(BaseModel):
    """Minimal CNN baseline for tiny datasets. Works well with heavy augmentation."""
    def __init__(self, config: Dict):
        super().__init__(config)
        input_channels = config.get("input_channels", 18)
        hidden_dim = config.get("hidden_dim", 32)
        dropout = config.get("dropout", 0.3)

        self.encoder = nn.Sequential(
            nn.Conv2d(3, hidden_dim, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Dropout2d(dropout),
            nn.Conv2d(hidden_dim, hidden_dim * 2, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Dropout2d(dropout),
            nn.Conv2d(hidden_dim * 2, hidden_dim * 2, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Dropout2d(dropout),
        )

        self.gis_encoder = nn.Sequential(
            nn.Conv2d(input_channels, hidden_dim, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Dropout2d(dropout),
            nn.Conv2d(hidden_dim, hidden_dim * 2, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Dropout2d(dropout),
        )

        self.fusion = nn.Sequential(
            nn.Conv2d(hidden_dim * 4, hidden_dim * 2, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Dropout2d(dropout),
            nn.Conv2d(hidden_dim * 2, hidden_dim, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Dropout2d(dropout),
            nn.Conv2d(hidden_dim, 1, kernel_size=1),
        )

    def forward(self, image: torch.Tensor, gis: torch.Tensor) -> torch.Tensor:
        img_feats = self.encoder(image)
        gis_feats = self.gis_encoder(gis)

        if gis_feats.shape[-2:] != img_feats.shape[-2:]:
            gis_feats = nn.functional.interpolate(gis_feats, size=img_feats.shape[-2:], mode="bilinear", align_corners=False)

        concat = torch.cat([img_feats, gis_feats], dim=1)
        out = self.fusion(concat)
        return out

    def get_intermediate_features(self, image: torch.Tensor, gis: torch.Tensor) -> Dict[str, torch.Tensor]:
        img_feats = self.encoder(image)
        gis_feats = self.gis_encoder(gis)
        if gis_feats.shape[-2:] != img_feats.shape[-2:]:
            gis_feats = nn.functional.interpolate(gis_feats, size=img_feats.shape[-2:], mode="bilinear", align_corners=False)
        concat = torch.cat([img_feats, gis_feats], dim=1)
        out = self.fusion(concat)
        return {"encoder": img_feats, "gis_encoder": gis_feats, "final": out}
```

---

### `models/decoder/__init__.py`

**Purpose:** Implementation of `__init__.py`.

```python

```

---

### `models/decoder/risk_decoder.py`

**Purpose:** Defines `Decoder` module/class.

```python
from typing import Dict

import torch
import torch.nn as nn

from ..base import BaseModel


class Decoder(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.hidden_dim = config.get("hidden_dim", 128)
        self.num_classes = config.get("num_classes", 1)
        self.dropout = config.get("dropout", 0.1)
        self._build_decoder()

    def _build_decoder(self):
        self.up1 = nn.Sequential(
            nn.ConvTranspose2d(self.hidden_dim, self.hidden_dim // 2, kernel_size=2, stride=2),
            nn.ReLU(),
            nn.Dropout2d(self.dropout),
        )
        self.up2 = nn.Sequential(
            nn.ConvTranspose2d(self.hidden_dim // 2, self.hidden_dim // 4, kernel_size=2, stride=2),
            nn.ReLU(),
            nn.Dropout2d(self.dropout),
        )
        self.up3 = nn.Sequential(
            nn.ConvTranspose2d(self.hidden_dim // 4, self.hidden_dim // 8, kernel_size=2, stride=2),
            nn.ReLU(),
            nn.Dropout2d(self.dropout),
        )
        self.final = nn.Sequential(
            nn.Conv2d(self.hidden_dim // 8, self.num_classes, kernel_size=1),
        )

    def forward(self, feats: torch.Tensor, spatial_size: tuple) -> torch.Tensor:
        if feats.shape[1] != self.hidden_dim:
            raise ValueError(
                f"Decoder expected input with {self.hidden_dim} channels, "
                f"but got tensor with {feats.shape[1]} channels. "
                f"Ensure encoder/GCM output channels match decoder hidden_dim."
            )
        x = feats
        x = self.up1(x)
        x = self.up2(x)
        x = self.up3(x)
        x = nn.functional.interpolate(x, size=spatial_size, mode="bilinear", align_corners=False)
        x = self.final(x)
        return x

    def get_intermediate_features(self, feats: torch.Tensor, spatial_size: tuple) -> Dict[str, torch.Tensor]:
        if feats.shape[1] != self.hidden_dim:
            raise ValueError(
                f"Decoder expected input with {self.hidden_dim} channels, "
                f"but got tensor with {feats.shape[1]} channels."
            )
        features = {}
        x = feats
        for i, layer in enumerate([self.up1, self.up2, self.up3]):
            x = layer(x)
            features[f"decoder_up_{i}"] = x
        x = nn.functional.interpolate(x, size=spatial_size, mode="bilinear", align_corners=False)
        features["decoder_output"] = self.final(x)
        return features
```

---

### `models/encoders/__init__.py`

**Purpose:** Implementation of `__init__.py`.

```python

```

---

### `models/encoders/gis_encoder.py`

**Purpose:** Defines `GISEncoder` module/class.

```python
from typing import Dict

import torch
import torch.nn as nn

from ..base import BaseModel


class GISEncoder(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.input_channels = config.get("input_channels", 18)
        self.hidden_dim = config.get("hidden_dim", 128)
        self.output_dim = config.get("output_dim", 128)
        self.dropout = config.get("dropout", 0.1)
        self._build_encoder()

    def _build_encoder(self):
        self.encoder = nn.Sequential(
            nn.Conv2d(self.input_channels, self.hidden_dim, kernel_size=3, padding=1),
            nn.BatchNorm2d(self.hidden_dim),
            nn.ReLU(),
            nn.Conv2d(self.hidden_dim, self.hidden_dim, kernel_size=3, padding=1),
            nn.BatchNorm2d(self.hidden_dim),
            nn.ReLU(),
            nn.Conv2d(self.hidden_dim, self.output_dim, kernel_size=3, padding=1),
            nn.AdaptiveAvgPool2d((16, 16)),
        )
        self.out_norm = nn.LayerNorm(self.output_dim)

    def forward(self, gis: torch.Tensor) -> torch.Tensor:
        x = self.encoder(gis)
        x = x.flatten(2).transpose(1, 2)
        x = self.out_norm(x)
        return x

    def get_intermediate_features(self, gis: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = {}
        x = gis
        for i, layer in enumerate(self.encoder):
            x = layer(x)
            features[f"gis_enc_{i}"] = x
        x = x.flatten(2).transpose(1, 2)
        x = self.out_norm(x)
        features["final"] = x
        return features
```

---

### `models/encoders/swin.py`

**Purpose:** Defines `SwinTransformerEncoder` module/class.

```python
from typing import Dict

import timm
import torch
import torch.nn as nn

from ..base import BaseModel


class SwinTransformerEncoder(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.embed_dim = config.get("embed_dim", 128)
        self.pretrained = config.get("pretrained", False)
        self.model_name = config.get("type", "swinv2_tiny_window16_256")
        self.depths = config.get("depths", None)
        self.num_heads = config.get("num_heads", None)
        self.window_size = config.get("window_size", None)
        self.img_size = config.get("img_size", 256)

        available_models = {
            "swinv2_tiny": "swinv2_tiny_window16_256",
            "swinv2_small": "swinv2_small_window16_256",
            "swinv2_base": "swinv2_base_window16_256",
        }

        if self.depths is not None and self.num_heads is not None and self.window_size is not None:
            from timm.models.swin_transformer_v2 import SwinTransformerV2

            self.swin = SwinTransformerV2(
                img_size=self.img_size,
                patch_size=4,
                in_chans=3,
                num_classes=0,
                embed_dim=self.embed_dim,
                depths=self.depths,
                num_heads=self.num_heads,
                window_size=self.window_size,
                drop_path_rate=config.get("drop_path_rate", 0.2),
                strict_img_size=False,
            )
            self.feature_dim = self.swin.num_features
        else:
            timm_model_name = available_models.get(self.model_name, self.model_name)
            try:
                self.swin = timm.create_model(timm_model_name, pretrained=self.pretrained, num_classes=0)
                self.feature_dim = self.swin.num_features
            except Exception:
                self.swin = timm.create_model("swinv2_tiny_window16_256", pretrained=self.pretrained, num_classes=0)
                self.feature_dim = 768

        self.proj = nn.Linear(self.feature_dim, self.embed_dim) if self.feature_dim != self.embed_dim else nn.Identity()

    def forward(self, image: torch.Tensor) -> torch.Tensor:
        features = self.swin.forward_features(image)
        features = features.flatten(1, 2)
        return self.proj(features)

    def get_intermediate_features(self, image: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = self.forward(image)
        return {"final": features}
```

---

### `models/fusion/__init__.py`

**Purpose:** Implementation of `__init__.py`.

```python

```

---

### `models/fusion/gct.py`

**Purpose:** Defines `GatedCrossAttention` module/class.

```python
from typing import Dict

import torch
import torch.nn as nn

from ..base import BaseModel


class GatedCrossAttention(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.hidden_dim = config.get("hidden_dim", 128)
        self.gis_input_dim = config.get("gis_input_dim", self.hidden_dim)
        self.num_heads = config.get("num_heads", 8)
        self.dropout_rate = config.get("dropout", 0.1)
        self.max_tokens = config.get("max_tokens", 256)
        self.rel_pos_scale = config.get("rel_pos_scale", 0.0)
        self._build_module()

    def _build_module(self):
        assert self.hidden_dim % self.num_heads == 0, (
            f"hidden_dim ({self.hidden_dim}) must be divisible by num_heads ({self.num_heads})"
        )
        self.head_dim = self.hidden_dim // self.num_heads
        self.q_proj = nn.Linear(self.hidden_dim, self.hidden_dim)
        self.k_proj = nn.Linear(self.gis_input_dim, self.hidden_dim)
        self.v_proj = nn.Linear(self.gis_input_dim, self.hidden_dim)
        self.out_proj = nn.Linear(self.hidden_dim, self.hidden_dim)
        self.norm = nn.LayerNorm(self.hidden_dim)
        self.dropout = nn.Dropout(self.dropout_rate)
        self.gate = nn.Sequential(
            nn.Linear(self.hidden_dim * 2, self.hidden_dim),
            nn.Tanh(),
            nn.Linear(self.hidden_dim, self.hidden_dim),
            nn.Sigmoid(),
        )
        for p in self.parameters():
            if p.dim() > 1:
                nn.init.xavier_uniform_(p)

        coords = self._generate_2d_coords(self.max_tokens)
        spatial_dist = torch.cdist(coords, coords, p=2)
        init_bias = -spatial_dist * self.rel_pos_scale
        self.register_buffer("rel_pos_bias", init_bias)

    @staticmethod
    def _generate_2d_coords(num_tokens: int) -> torch.Tensor:
        side = int(num_tokens ** 0.5)
        if side * side != num_tokens:
            side = 16
        x = torch.arange(side, dtype=torch.float32)
        y = torch.arange(side, dtype=torch.float32)
        xx, yy = torch.meshgrid(x, y, indexing="ij")
        coords = torch.stack([xx.flatten(), yy.flatten()], dim=-1)
        return coords

    def forward(self, image_feats: torch.Tensor, gis_feats: torch.Tensor) -> torch.Tensor:
        B, N, C = image_feats.shape

        if gis_feats.shape[1] != N:
            B2, N2, C2 = gis_feats.shape
            side = int(N2 ** 0.5)
            target_side = int(N ** 0.5)
            gis_feats = nn.functional.interpolate(
                gis_feats.transpose(1, 2).reshape(B2, C2, side, side),
                size=(target_side, target_side),
                mode="bilinear",
                align_corners=False,
            ).flatten(2).transpose(1, 2)

        q = self.q_proj(image_feats).view(B, N, self.num_heads, self.head_dim).transpose(1, 2)
        k = self.k_proj(gis_feats).view(B, N, self.num_heads, self.head_dim).transpose(1, 2)
        v = self.v_proj(gis_feats).view(B, N, self.num_heads, self.head_dim).transpose(1, 2)

        attn = torch.matmul(q, k.transpose(-2, -1)) / (self.head_dim ** 0.5)
        if N <= self.max_tokens:
            bias = self.rel_pos_bias[:N, :N].unsqueeze(0)
            attn = attn + bias
        attn = torch.softmax(attn, dim=-1)
        attn = self.dropout(attn)

        out = torch.matmul(attn, v)
        out = out.transpose(1, 2).contiguous().view(B, N, C)
        concat = torch.cat([image_feats, out], dim=-1)
        gating = self.gate(concat)
        fused = image_feats * gating + out * (1 - gating)
        fused = self.out_proj(fused)
        fused = self.norm(fused + image_feats)
        return fused

    def get_intermediate_features(self, image_feats: torch.Tensor, gis_feats: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = {"gct_input": image_feats, "gis_input": gis_feats}
        features["gct_output"] = self.forward(image_feats, gis_feats)
        return features
```

---

### `models/gcm/__init__.py`

**Purpose:** Implementation of `__init__.py`.

```python
from .distance_prior import SpatialDistancePrior
from .feature_similarity import FeatureSimilarityPrior
from .road_connectivity import RoadConnectivityPrior
from .urban_similarity import UrbanSimilarityPrior
from .learned_relation import LearnedRelation
from .scene_weight_predictor import SceneWeightPredictor
from .grm import GeographicRelationMatrix
from .geographic_attention import SemanticGeographicAttention
from .gcm_block import GCMBlock
from .gcm_transformer import GCMTransformer, GCMTransformerBlock

__all__ = [
    "SpatialDistancePrior",
    "FeatureSimilarityPrior",
    "RoadConnectivityPrior",
    "UrbanSimilarityPrior",
    "LearnedRelation",
    "SceneWeightPredictor",
    "GeographicRelationMatrix",
    "SemanticGeographicAttention",
    "GCMBlock",
    "GCMTransformer",
    "GCMTransformerBlock",
]
```

---

### `models/gcm/distance_prior.py`

**Purpose:** Defines `SpatialDistancePrior` module/class.

```python
from typing import Optional, Tuple

import torch
import torch.nn as nn


class SpatialDistancePrior(nn.Module):
    def __init__(self, grid_size: int = 16, sigma: float = 1.0):
        super().__init__()
        self.grid_size = grid_size
        self.sigma = sigma
        self.num_tokens = grid_size * grid_size
        coords = self._generate_coords(grid_size)
        self.register_buffer("coords", coords)
        self.register_buffer("distance_matrix", self._compute_distance_matrix())

    def _generate_coords(self, grid_size: int) -> torch.Tensor:
        x = torch.arange(grid_size, dtype=torch.float32)
        y = torch.arange(grid_size, dtype=torch.float32)
        xx, yy = torch.meshgrid(x, y, indexing="ij")
        coords = torch.stack([xx.flatten(), yy.flatten()], dim=-1)
        return coords

    def _compute_distance_matrix(self) -> torch.Tensor:
        dist = torch.cdist(self.coords, self.coords, p=2)
        dist = dist / (2 * self.sigma**2)
        D = torch.exp(-dist)
        D = D / (D.sum(dim=-1, keepdim=True) + 1e-8)
        return D

    def forward(self, batch_size: int) -> torch.Tensor:
        return self.distance_matrix.unsqueeze(0).expand(batch_size, -1, -1)
```

---

### `models/gcm/feature_similarity.py`

**Purpose:** Defines `FeatureSimilarityPrior` module/class.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F


class FeatureSimilarityPrior(nn.Module):
    def __init__(self, feature_dim: int = 64, eps: float = 1e-8):
        super().__init__()
        self.feature_dim = feature_dim
        self.eps = eps

    def forward(self, gis_embeddings: torch.Tensor) -> torch.Tensor:
        if gis_embeddings.dim() == 4:
            B, C, H, W = gis_embeddings.shape
            gis_embeddings = gis_embeddings.flatten(2).transpose(1, 2)
        gis_norm = F.normalize(gis_embeddings, dim=-1, eps=self.eps)
        S = torch.bmm(gis_norm, gis_norm.transpose(1, 2))
        row_max = S.max(dim=-1, keepdim=True)[0]
        row_min = S.min(dim=-1, keepdim=True)[0]
        denom = (row_max - row_min).clamp(min=self.eps)
        S = (S - row_min) / denom
        return S
```

---

### `models/gcm/gcm_block.py`

**Purpose:** Defines `GCMBlock` module/class.

```python
from typing import Dict, Optional, Tuple

import torch
import torch.nn as nn

from .gcm_transformer import GCMTransformer


class GCMBlock(nn.Module):
    def __init__(self, config: Dict):
        super().__init__()
        self.gcm_transformer = GCMTransformer(
            embed_dim=config.get("embed_dim", 512),
            num_heads=config.get("num_heads", 8),
            num_blocks=config.get("num_blocks", 4),
            num_semantic_heads=config.get("num_semantic_heads", 5),
            mlp_ratio=config.get("mlp_ratio", 4.0),
            dropout=config.get("dropout", 0.1),
            gate_init=config.get("gate_init", 0.1),
            gis_channels=config.get("gis_channels", 18),
            gis_feature_dim=config.get("gis_feature_dim", 64),
            grid_size=config.get("grid_size", 16),
            sigma_distance=config.get("sigma_distance", 1.0),
            scene_weight_hidden=config.get("scene_weight_hidden", 32),
            enable_distance=config.get("enable_distance", True),
            enable_similarity=config.get("enable_similarity", True),
            enable_road=config.get("enable_road", True),
            enable_urban=config.get("enable_urban", True),
            enable_learned=config.get("enable_learned", True),
            enable_scene_weights=config.get("enable_scene_weights", True),
        )

    def forward(
        self,
        x: torch.Tensor,
        gis_features: torch.Tensor,
        gis_embeddings: Optional[torch.Tensor] = None,
    ) -> Tuple[torch.Tensor, list]:
        return self.gcm_transformer(x, gis_features, gis_embeddings)
```

---

### `models/gcm/gcm_transformer.py`

**Purpose:** Defines `GCMTransformerBlock` module/class.

```python
from typing import Dict, List, Optional, Tuple

import torch
import torch.nn as nn


class GCMTransformerBlock(nn.Module):
    def __init__(
        self,
        embed_dim: int = 512,
        num_heads: int = 8,
        num_semantic_heads: int = 5,
        mlp_ratio: float = 4.0,
        dropout: float = 0.1,
        gate_init: float = 0.1,
        enable_scene_weights: bool = True,
    ):
        super().__init__()
        self.norm1 = nn.LayerNorm(embed_dim)
        from models.gcm.geographic_attention import SemanticGeographicAttention
        self.attn = SemanticGeographicAttention(
            embed_dim=embed_dim,
            num_heads=num_heads,
            num_semantic_heads=num_semantic_heads,
            dropout=dropout,
            gate_init=gate_init,
            enable_scene_weights=enable_scene_weights,
        )
        self.norm2 = nn.LayerNorm(embed_dim)
        self.mlp = nn.Sequential(
            nn.Linear(embed_dim, int(embed_dim * mlp_ratio)),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(int(embed_dim * mlp_ratio), embed_dim),
            nn.Dropout(dropout),
        )

    def forward(
        self,
        x: torch.Tensor,
        grg: torch.Tensor,
        priors: Optional[Dict[str, torch.Tensor]] = None,
    ) -> Tuple[torch.Tensor, Dict[str, torch.Tensor]]:
        attn_out, attn_maps = self.attn(self.norm1(x), grg, priors)
        x = x + attn_out
        x = x + self.mlp(self.norm2(x))
        return x, attn_maps


class GCMTransformer(nn.Module):
    def __init__(
        self,
        embed_dim: int = 512,
        num_heads: int = 8,
        num_blocks: int = 4,
        num_semantic_heads: int = 5,
        mlp_ratio: float = 4.0,
        dropout: float = 0.1,
        gate_init: float = 0.1,
        gis_channels: int = 18,
        gis_feature_dim: int = 64,
        grid_size: int = 16,
        sigma_distance: float = 1.0,
        scene_weight_hidden: int = 32,
        enable_distance: bool = True,
        enable_similarity: bool = True,
        enable_road: bool = True,
        enable_urban: bool = True,
        enable_learned: bool = True,
        enable_scene_weights: bool = True,
    ):
        super().__init__()
        self.num_blocks = num_blocks
        self.grid_size = grid_size
        self.num_tokens = grid_size * grid_size

        from models.gcm.grm import GeographicRelationMatrix
        self.grm = GeographicRelationMatrix(
            embed_dim=embed_dim,
            gis_channels=gis_channels,
            gis_feature_dim=gis_feature_dim,
            grid_size=grid_size,
            sigma_distance=sigma_distance,
            scene_weight_hidden=scene_weight_hidden,
            enable_distance=enable_distance,
            enable_similarity=enable_similarity,
            enable_road=enable_road,
            enable_urban=enable_urban,
            enable_learned=enable_learned,
            enable_scene_weights=enable_scene_weights,
        )

        self.blocks = nn.ModuleList([
            GCMTransformerBlock(
                embed_dim=embed_dim,
                num_heads=num_heads,
                num_semantic_heads=num_semantic_heads,
                mlp_ratio=mlp_ratio,
                dropout=dropout,
                gate_init=gate_init,
                enable_scene_weights=enable_scene_weights,
            )
            for _ in range(num_blocks)
        ])

        self.norm = nn.LayerNorm(embed_dim)

    def forward(
        self,
        x: torch.Tensor,
        gis_features: torch.Tensor,
        gis_embeddings: Optional[torch.Tensor] = None,
    ) -> Tuple[torch.Tensor, List[Dict[str, torch.Tensor]]]:
        B, N, C = x.shape
        grg, priors = self.grm(x, gis_features, gis_embeddings)

        all_attn_maps = []
        for block in self.blocks:
            x, attn_maps = block(x, grg, priors)
            all_attn_maps.append(attn_maps)

        x = self.norm(x)
        return x, all_attn_maps
```

---

### `models/gcm/geographic_attention.py`

**Purpose:** Defines `SemanticGeographicAttention` module/class.

```python
from typing import Dict, Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F


class SemanticGeographicAttention(nn.Module):
    def __init__(
        self,
        embed_dim: int = 512,
        num_heads: int = 8,
        num_semantic_heads: int = 5,
        dropout: float = 0.1,
        gate_init: float = 0.1,
        enable_scene_weights: bool = True,
        prior_scale: float = 4.0,
    ):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.num_semantic_heads = num_semantic_heads
        self.head_dim = embed_dim // num_heads
        self.enable_scene_weights = enable_scene_weights
        assert embed_dim % num_heads == 0

        self.q_proj = nn.Linear(embed_dim, embed_dim)
        self.k_proj = nn.Linear(embed_dim, embed_dim)
        self.v_proj = nn.Linear(embed_dim, embed_dim)
        self.out_proj = nn.Linear(embed_dim, embed_dim)
        self.dropout = nn.Dropout(dropout)
        self.beta_gate = nn.Parameter(torch.tensor(gate_init))

        self.prior_scale = nn.Parameter(torch.tensor(prior_scale))

        self.semantic_projections = nn.ModuleList([
            nn.Linear(embed_dim, embed_dim) for _ in range(num_semantic_heads)
        ])
        self.semantic_grg_projections = nn.ModuleList([
            nn.Linear(embed_dim, embed_dim) for _ in range(num_semantic_heads)
        ])

    def _apply_semantic_attention(
        self,
        Q: torch.Tensor,
        K: torch.Tensor,
        V: torch.Tensor,
        G: torch.Tensor,
    ) -> torch.Tensor:
        B, H, N, D = Q.shape
        attn_scores = torch.bmm(Q, K.transpose(1, 2)) / (self.head_dim ** 0.5)
        attn_scores = attn_scores + G
        attn_weights = F.softmax(attn_scores, dim=-1)
        attn_weights = self.dropout(attn_weights)
        attn_output = torch.bmm(attn_weights, V)
        return attn_output

    def forward(
        self,
        x: torch.Tensor,
        grg: torch.Tensor,
        priors: Optional[Dict[str, torch.Tensor]] = None,
    ) -> Tuple[torch.Tensor, Dict[str, torch.Tensor]]:
        B, N, C = x.shape
        H = self.num_heads
        D = self.head_dim

        Q = self.q_proj(x).view(B, N, H, D).transpose(1, 2)
        K = self.k_proj(x).view(B, N, H, D).transpose(1, 2)
        V = self.v_proj(x).view(B, N, H, D).transpose(1, 2)

        attention_maps = {}
        outputs = []
        prior_names = ["distance", "similarity", "road", "urban", "learned"]

        scaled_grg = grg * self.prior_scale

        for head_idx in range(H):
            q_h = Q[:, head_idx, :, :]
            k_h = K[:, head_idx, :, :]
            v_h = V[:, head_idx, :, :]

            if head_idx < self.num_semantic_heads:
                prior_name = prior_names[head_idx]
                G = priors.get(prior_name, torch.zeros(B, N, N, device=x.device)) if priors else torch.zeros(B, N, N, device=x.device)
                G = G * self.prior_scale
            else:
                G = scaled_grg

            attn_scores = torch.bmm(q_h, k_h.transpose(1, 2)) / (D ** 0.5)
            attn_scores = attn_scores + G
            attn_weights = F.softmax(attn_scores, dim=-1)
            attn_weights = attn_weights * (1.0 + self.beta_gate * G)
            attn_weights = self.dropout(attn_weights)
            attn_output = torch.bmm(attn_weights, v_h)

            outputs.append(attn_output)

            if head_idx < self.num_semantic_heads:
                attention_maps[f"head_{head_idx}_{prior_name}"] = G.detach()

        attn_output = torch.cat(outputs, dim=-1)
        attn_output = attn_output.view(B, N, C)
        attn_output = self.out_proj(attn_output)
        return attn_output, attention_maps
```

---

### `models/gcm/grm.py`

**Purpose:** Defines `GeographicRelationMatrix` module/class.

```python
from typing import Dict, Optional, Tuple

import torch
import torch.nn as nn

from .distance_prior import SpatialDistancePrior
from .feature_similarity import FeatureSimilarityPrior
from .learned_relation import LearnedRelation
from .road_connectivity import RoadConnectivityPrior
from .scene_weight_predictor import SceneWeightPredictor
from .urban_similarity import UrbanSimilarityPrior


class GeographicRelationMatrix(nn.Module):
    def __init__(self, config: Optional[Dict] = None, **kwargs):
        super().__init__()
        if config is None:
            config = kwargs
        else:
            config = dict(config)
            config.update(kwargs)
        embed_dim = config.get("embed_dim", 512)
        gis_channels = config.get("gis_channels", 18)
        gis_feature_dim = config.get("gis_feature_dim", 64)
        grid_size = config.get("grid_size", 16)
        sigma_distance = config.get("sigma_distance", 1.0)
        scene_weight_hidden = config.get("scene_weight_hidden", 32)
        enable_distance = config.get("enable_distance", True)
        enable_similarity = config.get("enable_similarity", True)
        enable_road = config.get("enable_road", True)
        enable_urban = config.get("enable_urban", True)
        enable_learned = config.get("enable_learned", True)
        enable_scene_weights = config.get("enable_scene_weights", True)

        self.num_tokens = grid_size * grid_size
        self.sigma_distance = sigma_distance
        self.scene_weight_hidden = scene_weight_hidden
        self.enable_distance = enable_distance
        self.enable_similarity = enable_similarity
        self.enable_road = enable_road
        self.enable_urban = enable_urban
        self.enable_learned = enable_learned
        self.enable_scene_weights = enable_scene_weights

        if self.enable_distance:
            self.distance_prior = SpatialDistancePrior(grid_size=grid_size, sigma=sigma_distance)
        if self.enable_similarity:
            self.similarity_prior = FeatureSimilarityPrior(feature_dim=gis_feature_dim)
        if self.enable_road:
            self.road_prior = RoadConnectivityPrior(grid_size=grid_size)
        if self.enable_urban:
            self.urban_prior = UrbanSimilarityPrior(gis_channels=gis_channels, latent_dim=16)
        if self.enable_learned:
            self.learned_relation = LearnedRelation(embed_dim=embed_dim, rank=64)
        if self.enable_scene_weights:
            self.scene_weight_predictor = SceneWeightPredictor(
                gis_channels=gis_channels,
                hidden_dim=64,
                scene_hidden=scene_weight_hidden,
                output_dim=5,
            )
            self.register_parameter("alpha", nn.Parameter(torch.tensor(0.2)))
            self.register_parameter("beta", nn.Parameter(torch.tensor(0.2)))
            self.register_parameter("gamma", nn.Parameter(torch.tensor(0.2)))
            self.register_parameter("delta", nn.Parameter(torch.tensor(0.2)))
            self.register_parameter("epsilon", nn.Parameter(torch.tensor(0.2)))
        else:
            self.alpha = nn.Parameter(torch.tensor(0.2))
            self.beta = nn.Parameter(torch.tensor(0.2))
            self.gamma = nn.Parameter(torch.tensor(0.2))
            self.delta = nn.Parameter(torch.tensor(0.2))
            self.epsilon = nn.Parameter(torch.tensor(0.2))

    def forward(
        self,
        tokens: torch.Tensor,
        gis_features: Optional[torch.Tensor] = None,
        gis_embeddings: Optional[torch.Tensor] = None,
    ) -> Tuple[torch.Tensor, Dict[str, torch.Tensor]]:
        if gis_features is None:
            gis_features = torch.zeros(tokens.shape[0], 18, 16, 16, device=tokens.device)
        B = tokens.shape[0]
        N = tokens.shape[1]
        actual_grid_size = int(N ** 0.5)
        priors = {}
        embed_dim = tokens.shape[-1]
        device = tokens.device

        if self.enable_distance:
            if hasattr(self, "distance_prior") and self.distance_prior.num_tokens == N:
                D = self.distance_prior(B)
            else:
                D = SpatialDistancePrior(grid_size=actual_grid_size, sigma=self.sigma_distance).to(device)(B)
            priors["distance"] = D
        else:
            D = torch.zeros(B, N, N, device=device)

        if self.enable_similarity and gis_embeddings is not None:
            if gis_embeddings.dim() == 3:
                B, N, C = gis_embeddings.shape
                side = int(N ** 0.5)
                gis_embeddings_4d = gis_embeddings.transpose(1, 2).reshape(B, C, side, side)
            else:
                gis_embeddings_4d = gis_embeddings
            if gis_embeddings_4d.shape[2] != actual_grid_size or gis_embeddings_4d.shape[3] != actual_grid_size:
                gis_embeddings_4d = torch.nn.functional.interpolate(gis_embeddings_4d, size=actual_grid_size, mode="bilinear", align_corners=False)
            S = self.similarity_prior(gis_embeddings_4d)
            priors["similarity"] = S
        else:
            S = torch.zeros_like(D)

        if self.enable_road:
            gis_for_road = torch.nn.functional.interpolate(gis_features, size=actual_grid_size, mode="bilinear", align_corners=False)
            R = self.road_prior(gis_for_road)
            priors["road"] = R
        else:
            R = torch.zeros_like(D)

        if self.enable_urban:
            gis_for_urban = torch.nn.functional.interpolate(gis_features, size=actual_grid_size, mode="bilinear", align_corners=False)
            U = self.urban_prior(gis_for_urban)
            priors["urban"] = U
        else:
            U = torch.zeros_like(D)

        if self.enable_learned:
            L = self.learned_relation(tokens)
            priors["learned"] = L
        else:
            L = torch.zeros_like(D)

        if self.enable_scene_weights:
            weights = self.scene_weight_predictor(gis_features)
            alpha = weights[:, 0].view(B, 1, 1)
            beta = weights[:, 1].view(B, 1, 1)
            gamma = weights[:, 2].view(B, 1, 1)
            delta = weights[:, 3].view(B, 1, 1)
            epsilon = weights[:, 4].view(B, 1, 1)
            priors["scene_weights"] = weights
        else:
            alpha = self.alpha.view(1, 1, 1)
            beta = self.beta.view(1, 1, 1)
            gamma = self.gamma.view(1, 1, 1)
            delta = self.delta.view(1, 1, 1)
            epsilon = self.epsilon.view(1, 1, 1)

        G = alpha * D + beta * S + gamma * R + delta * U + epsilon * L
        G = G / (G.sum(dim=-1, keepdim=True) + 1e-8)
        priors["grg"] = G

        return G, priors

    def get_intermediate_features(self, feats: torch.Tensor, gis_features: Optional[torch.Tensor] = None) -> Dict[str, torch.Tensor]:
        features = {"grm_input": feats}
        features["grm_output"] = self.forward(feats, gis_features)[0]
        return features
```

---

### `models/gcm/learned_relation.py`

**Purpose:** Defines `LearnedRelation` module/class.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F


class LearnedRelation(nn.Module):
    def __init__(self, embed_dim: int = 512, rank: int = 64, eps: float = 1e-8):
        super().__init__()
        self.rank = rank
        self.eps = eps
        self.relation_encoder = self._build_encoder(embed_dim)

    def _build_encoder(self, embed_dim: int):
        return nn.Sequential(
            nn.Linear(embed_dim, embed_dim),
            nn.ReLU(),
            nn.Linear(embed_dim, embed_dim // 2),
            nn.ReLU(),
            nn.Linear(embed_dim // 2, embed_dim // 4),
            nn.ReLU(),
            nn.Linear(embed_dim // 4, self.rank),
        )

    def forward(self, tokens: torch.Tensor) -> torch.Tensor:
        actual_dim = tokens.shape[-1]
        if self.relation_encoder[0].in_features != actual_dim:
            self.relation_encoder = self._build_encoder(actual_dim).to(tokens.device)
            self.reset_relu_flags = True
        E = self.relation_encoder(tokens)
        E = F.normalize(E, dim=-1, eps=self.eps)
        L = torch.bmm(E, E.transpose(1, 2))
        L = L / (L.max(dim=-1, keepdim=True)[0] + self.eps)
        return L
```

---

### `models/gcm/road_connectivity.py`

**Purpose:** Defines `RoadConnectivityPrior` module/class.

```python
from pathlib import Path
from typing import Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F


class RoadConnectivityPrior(nn.Module):
    def __init__(self, grid_size: int = 16, eps: float = 1e-8, precomputed_path: Optional[str] = None):
        super().__init__()
        self.grid_size = grid_size
        self.num_tokens = grid_size * grid_size
        self.eps = eps
        self.precomputed_path = precomputed_path
        self.register_buffer("precomputed_R", torch.zeros(1, grid_size * grid_size, grid_size * grid_size))

        if precomputed_path and Path(precomputed_path).exists():
            self.load_precomputed(precomputed_path)

    def load_precomputed(self, path: str):
        state = torch.load(path, map_location="cpu")
        if "road_connectivity" in state:
            R = state["road_connectivity"]
        else:
            R = state
        if R.ndim == 2:
            R = R.unsqueeze(0)
        self.register_buffer("precomputed_R", R)

    def _density_fallback(self, gis_features: torch.Tensor) -> torch.Tensor:
        road_density = gis_features[:, 2, :, :]
        B, H, W = road_density.shape
        N = H * W
        road_density = road_density.view(B, N)
        road_sim = torch.bmm(road_density.unsqueeze(-1), road_density.unsqueeze(-1).transpose(1, 2))
        diagonal = torch.diagonal(road_sim, dim1=-2, dim2=-1)
        max_vals = diagonal.max(dim=-1, keepdim=True)[0].unsqueeze(-1)
        R = road_sim / (max_vals + self.eps)
        identity = torch.eye(N, device=gis_features.device).unsqueeze(0)
        R = R * (1 - identity)
        R = R / (R.sum(dim=-1, keepdim=True) + self.eps)
        return R

    def forward(self, gis_features: torch.Tensor) -> torch.Tensor:
        if self.precomputed_R.sum() > 0:
            R = self.precomputed_R.to(gis_features.device)
            if R.shape[1] != gis_features.shape[2] * gis_features.shape[3]:
                return self._density_fallback(gis_features)
            return R.expand(gis_features.shape[0], -1, -1)
        return self._density_fallback(gis_features)
```

---

### `models/gcm/scene_weight_predictor.py`

**Purpose:** Defines `SceneWeightPredictor` module/class.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F


class SceneWeightPredictor(nn.Module):
    def __init__(self, gis_channels: int = 18, hidden_dim: int = 64, scene_hidden: int = 32, output_dim: int = 5):
        super().__init__()
        self.scene_encoder = nn.Sequential(
            nn.Conv2d(gis_channels, hidden_dim, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(hidden_dim, hidden_dim // 2, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
            nn.Linear(hidden_dim // 2, scene_hidden),
            nn.ReLU(),
            nn.Linear(scene_hidden, output_dim),
        )

    def forward(self, gis_features: torch.Tensor) -> torch.Tensor:
        logits = self.scene_encoder(gis_features)
        weights = F.softmax(logits, dim=-1)
        return weights
```

---

### `models/gcm/urban_similarity.py`

**Purpose:** Defines `UrbanSimilarityPrior` module/class.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F


class UrbanSimilarityPrior(nn.Module):
    def __init__(self, gis_channels: int = 18, hidden_dim: int = 64, latent_dim: int = 16, eps: float = 1e-8):
        super().__init__()
        self.urban_encoder = nn.Sequential(
            nn.Conv2d(gis_channels, hidden_dim, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(hidden_dim, hidden_dim // 2, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(hidden_dim // 2, latent_dim, kernel_size=3, padding=1),
        )
        self.latent_dim = latent_dim
        self.eps = eps

    def forward(self, gis_features: torch.Tensor) -> torch.Tensor:
        B, C, H, W = gis_features.shape
        latent = self.urban_encoder(gis_features)
        latent = F.normalize(latent, dim=1, eps=self.eps)
        latent = latent.view(B, self.latent_dim, H * W).transpose(1, 2)
        U = torch.bmm(latent, latent.transpose(1, 2))
        row_max = U.max(dim=-1, keepdim=True)[0]
        row_min = U.min(dim=-1, keepdim=True)[0]
        U = (U - row_min) / (row_max - row_min + self.eps)
        return U
```

---

### `models/gcm_hairnet.py`

**Purpose:** Defines `GCMHAIRNet` module/class.

```python
from typing import Dict, List, Optional, Tuple

import torch
import torch.nn as nn

from .base import BaseModel
from .encoders.swin import SwinTransformerEncoder
from .encoders.gis_encoder import GISEncoder
from .fusion.gct import GatedCrossAttention
from .graph_relation import GraphRelationModule
from .decoder.risk_decoder import Decoder


class GCMHAIRNet(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.image_encoder = SwinTransformerEncoder(config.get("image_encoder", {}))
        self.gis_encoder = GISEncoder(config.get("gis_encoder", {}))
        gct_config = dict(config.get("gct", {}))
        gct_config.setdefault("gis_input_dim", self.gis_encoder.output_dim)
        self.gct = GatedCrossAttention(gct_config)
        self.graph_relation_module = GraphRelationModule(config.get("grm", {}))
        self.decoder = Decoder(config.get("decoder", {}))
        self.image_size = config.get("image_size", 256)
        self.gis_size = config.get("gis_size", 32)

        gcm_config = config.get("gcm", {})
        self.gcm_config = gcm_config
        self.use_gcm = gcm_config.get("enable", True)
        if self.use_gcm:
            from models.gcm.gcm_block import GCMBlock

            self.gcm = GCMBlock(gcm_config)
            self.gcm_proj = nn.Conv2d(
                self.image_encoder.embed_dim + self.gis_encoder.input_channels,
                gcm_config.get("embed_dim", 512),
                kernel_size=1,
            )
            self.decoder_proj = nn.Conv2d(
                gcm_config.get("embed_dim", 512),
                self.decoder.hidden_dim,
                kernel_size=1,
            )

    @property
    def swin(self):
        return self.image_encoder

    @property
    def grm(self):
        return self.graph_relation_module

    def forward(self, image: torch.Tensor, gis: torch.Tensor) -> torch.Tensor:
        image_feats = self.image_encoder(image)
        gis_feats = self.gis_encoder(gis)
        fused_feats = self.gct(image_feats, gis_feats)

        B, N, C = fused_feats.shape
        H = W = int(N ** 0.5)
        spatial_feats = fused_feats.transpose(1, 2).reshape(B, C, H, W)

        if self.use_gcm:
            upsampled_gis = nn.functional.interpolate(
                gis, size=(H, W), mode="bilinear", align_corners=False
            )
            concat_feats = torch.cat([spatial_feats, upsampled_gis], dim=1)
            projected = self.gcm_proj(concat_feats)
            projected = nn.functional.layer_norm(projected, projected.shape[1:])
            B, C, H, W = projected.shape
            tokens = projected.flatten(2).transpose(1, 2)
            gis_for_priors = nn.functional.interpolate(
                gis, size=(H, W), mode="bilinear", align_corners=False
            )
            gis_embeddings = None
            if hasattr(self.gis_encoder, "encoder"):
                with torch.no_grad():
                    gis_embeddings = self.gis_encoder(gis_for_priors)
            tokens, _ = self.gcm(tokens, gis_for_priors, gis_embeddings)
            spatial_feats = tokens.transpose(1, 2).reshape(B, C, H, W)
            spatial_feats = self.decoder_proj(spatial_feats)

        B, C, H, W = spatial_feats.shape
        tokens = spatial_feats.flatten(2).transpose(1, 2)
        refined_tokens = self.graph_relation_module(tokens)
        spatial_feats = refined_tokens.transpose(1, 2).reshape(B, C, H, W)

        output = self.decoder(spatial_feats, spatial_size=(256, 256))
        return output

    def get_intermediate_features(self, image: torch.Tensor, gis: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = {}
        features["image_encoder"] = self.image_encoder.get_intermediate_features(image)
        features["gis_encoder"] = self.gis_encoder.get_intermediate_features(gis)
        image_feats = features["image_encoder"]["final"]
        gis_feats = features["gis_encoder"]["final"]
        features["gct"] = self.gct.get_intermediate_features(image_feats, gis_feats)

        B, N, C = features["gct"]["gct_output"].shape
        H = W = int(N ** 0.5)
        spatial_feats = features["gct"]["gct_output"].transpose(1, 2).reshape(B, C, H, W)

        if self.use_gcm:
            upsampled_gis = nn.functional.interpolate(
                gis, size=(H, W), mode="bilinear", align_corners=False
            )
            concat_feats = torch.cat([spatial_feats, upsampled_gis], dim=1)
            projected = self.gcm_proj(concat_feats)
            projected = nn.functional.layer_norm(projected, projected.shape[1:])
            B, C, H, W = projected.shape
            tokens = projected.flatten(2).transpose(1, 2)
            features["gcm_input"] = tokens
            gis_for_priors = nn.functional.interpolate(
                gis, size=(H, W), mode="bilinear", align_corners=False
            )
            gis_embeddings = None
            if hasattr(self.gis_encoder, "encoder"):
                with torch.no_grad():
                    gis_embeddings = self.gis_encoder(gis_for_priors)
            gcm_out, gcm_attn_maps = self.gcm(tokens, gis_for_priors, gis_embeddings)
            features["gcm_output"] = gcm_out
            features["gcm_attention"] = gcm_attn_maps
            spatial_feats = gcm_out.transpose(1, 2).reshape(B, C, H, W)
            spatial_feats = self.decoder_proj(spatial_feats)

        features["graph_relation_input"] = spatial_feats.flatten(2).transpose(1, 2)
        refined_tokens = self.graph_relation_module(features["graph_relation_input"])
        features["graph_relation_output"] = refined_tokens
        B, C, H, W = spatial_feats.shape
        spatial_feats = refined_tokens.transpose(1, 2).reshape(B, C, H, W)

        features["decoder_input"] = spatial_feats
        features["decoder"] = self.decoder.get_intermediate_features(spatial_feats, (256, 256))
        return features
```

---

### `models/graph_relation.py`

**Purpose:** Defines `GraphRelationModule` module/class.

```python
from typing import Dict

import torch
import torch.nn as nn


class GraphRelationModule(nn.Module):
    def __init__(self, config: Dict):
        super().__init__()
        self.hidden_dim = config.get("hidden_dim", 128)
        self.num_relations = config.get("num_relations", 4)
        self.num_layers = config.get("num_layers", 3)
        self.dropout = config.get("dropout", 0.1)

        self.relation_embeddings = nn.Embedding(self.num_relations, self.hidden_dim)
        self.layers = nn.ModuleList()
        for _ in range(self.num_layers):
            self.layers.append(
                nn.ModuleList(
                    [
                        nn.Linear(self.hidden_dim, self.hidden_dim),
                        nn.LayerNorm(self.hidden_dim),
                        nn.Dropout(self.dropout),
                    ]
                )
            )
        self.norm = nn.LayerNorm(self.hidden_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if x.shape[-1] != self.hidden_dim:
            raise ValueError(
                f"GraphRelationModule expected input with {self.hidden_dim} features, "
                f"but got tensor with {x.shape[-1]} features."
            )
        for proj, norm, drop in self.layers:
            rel_weights = torch.softmax(
                torch.matmul(x, self.relation_embeddings.weight.T), dim=-1
            )
            rel_messages = torch.matmul(rel_weights, self.relation_embeddings.weight)
            h = proj(x + rel_messages)
            h = torch.nn.functional.relu(h)
            h = drop(h)
            x = norm(x + h)
        return self.norm(x)

    def get_intermediate_features(self, x: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = {"grm_input": x}
        features["grm_output"] = self.forward(x)
        return features
```

---

### `models/relation/__init__.py`

**Purpose:** Defines `RelationModule` module/class.

```python
from typing import Optional

import torch
import torch.nn as nn

from .vit import ViTRelationModule
from .swin import SwinRelationModule
from .graphsage import GraphSAGERelationModule
from .mha import MHARelationModule
from .non_local import NonLocalRelationModule


class RelationModule(nn.Module):
    def __init__(self, hidden_dim: int = 128, num_heads: int = 8, dropout: float = 0.1):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
        self.dropout = dropout

    def forward(
        self,
        x: torch.Tensor,
        gis_features: Optional[torch.Tensor] = None,
        gis_embeddings: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        raise NotImplementedError

    def get_intermediate_features(self, x: torch.Tensor, gis_features=None, gis_embeddings=None) -> dict:
        return {"input": x, "output": self.forward(x, gis_features, gis_embeddings)}


def build_relation_module(config: dict) -> nn.Module:
    rel_type = config.get("type", "gcm")
    hidden_dim = config.get("hidden_dim", 128)
    num_heads = config.get("num_heads", 8)
    dropout = config.get("dropout", 0.1)

    if rel_type == "vit":
        return ViTRelationModule(hidden_dim, num_heads, dropout, num_layers=config.get("num_layers", 4))
    elif rel_type == "swin":
        return SwinRelationModule(hidden_dim, num_heads, dropout, num_layers=config.get("num_layers", 4))
    elif rel_type == "graphsage":
        return GraphSAGERelationModule(hidden_dim, dropout, num_layers=config.get("num_layers", 3))
    elif rel_type == "mha":
        return MHARelationModule(hidden_dim, num_heads, dropout, num_layers=config.get("num_layers", 4))
    elif rel_type == "nonlocal":
        return NonLocalRelationModule(hidden_dim, num_heads, dropout, num_layers=config.get("num_layers", 4))
    elif rel_type == "gcm":
        from ..gcm.gcm_block import GCMBlock
        gcm_config = dict(config)
        gcm_config.pop("type", None)
        gcm_config.pop("hidden_dim", None)
        gcm_config.pop("num_heads", None)
        gcm_config.setdefault("embed_dim", hidden_dim * 4 if hidden_dim > 128 else 512)
        gcm_config.setdefault("num_blocks", config.get("num_blocks", 4))
        gcm_config.setdefault("num_semantic_heads", 5)
        gcm_config.setdefault("mlp_ratio", 4.0)
        gcm_config.setdefault("dropout", dropout)
        gcm_config.setdefault("gate_init", 0.1)
        gcm_config.setdefault("gis_channels", 18)
        gcm_config.setdefault("gis_feature_dim", 64)
        gcm_config.setdefault("grid_size", 16)
        gcm_config.setdefault("sigma_distance", 1.0)
        gcm_config.setdefault("scene_weight_hidden", 32)
        gcm_config.setdefault("enable", True)
        gcm_config.setdefault("enable_distance", True)
        gcm_config.setdefault("enable_similarity", True)
        gcm_config.setdefault("enable_road", True)
        gcm_config.setdefault("enable_urban", True)
        gcm_config.setdefault("enable_learned", True)
        gcm_config.setdefault("enable_scene_weights", True)
        return GCMBlock(gcm_config)
    else:
        raise ValueError(f"Unknown relation module type: {rel_type}")


__all__ = [
    "RelationModule",
    "build_relation_module",
    "ViTRelationModule",
    "SwinRelationModule",
    "GraphSAGERelationModule",
    "MHARelationModule",
    "NonLocalRelationModule",
]
```

---

### `models/relation/graphsage.py`

**Purpose:** Defines `GraphSAGELayer` module/class.

```python
from typing import Optional

import torch
import torch.nn as nn
import torch.nn.functional as F


class GraphSAGELayer(nn.Module):
    def __init__(self, in_dim: int, out_dim: int, dropout: float = 0.1):
        super().__init__()
        self.linear = nn.Linear(in_dim, out_dim)
        self.agg_linear = nn.Linear(in_dim * 2, out_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor, adj: torch.Tensor) -> torch.Tensor:
        B, N, C = x.shape
        neighbor_agg = torch.bmm(adj, x)
        combined = torch.cat([x, neighbor_agg], dim=-1)
        out = self.agg_linear(combined)
        out = self.dropout(F.relu(out))
        return out


class GraphSAGERelationModule(nn.Module):
    def __init__(self, hidden_dim: int = 128, dropout: float = 0.1, num_layers: int = 3):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.layers = nn.ModuleList()
        for _ in range(num_layers):
            self.layers.append(GraphSAGELayer(hidden_dim, hidden_dim, dropout))
        self.norm = nn.LayerNorm(hidden_dim)
        self.proj = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim),
        )

    @staticmethod
    def _compute_adjacency(x: torch.Tensor) -> torch.Tensor:
        B, N, C = x.shape
        x_norm = F.normalize(x, dim=-1)
        adj = torch.bmm(x_norm, x_norm.transpose(1, 2))
        adj = F.relu(adj)
        adj = adj + torch.eye(N, device=x.device).unsqueeze(0)
        row_sum = adj.sum(dim=-1, keepdim=True).clamp(min=1.0)
        adj = adj / row_sum
        return adj

    def forward(
        self,
        x: torch.Tensor,
        gis_features: Optional[torch.Tensor] = None,
        gis_embeddings: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        adj = self._compute_adjacency(x)
        for layer in self.layers:
            x = layer(x, adj)
        x = self.norm(x)
        return self.proj(x) + x
```

---

### `models/relation/mha.py`

**Purpose:** Defines `MHARelationModule` module/class.

```python
from typing import Optional

import torch
import torch.nn as nn
import torch.nn.functional as F


class MHARelationModule(nn.Module):
    def __init__(self, hidden_dim: int = 128, num_heads: int = 8, dropout: float = 0.1, num_layers: int = 4):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
        self.head_dim = hidden_dim // num_heads
        assert hidden_dim % num_heads == 0

        self.layers = nn.ModuleList()
        for _ in range(num_layers):
            self.layers.append(MHALayer(hidden_dim, num_heads, dropout))

        self.norm = nn.LayerNorm(hidden_dim)
        self.proj = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim),
        )

    def forward(
        self,
        x: torch.Tensor,
        gis_features: Optional[torch.Tensor] = None,
        gis_embeddings: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        for layer in self.layers:
            x = layer(x)
        x = self.norm(x)
        return self.proj(x) + x


class MHALayer(nn.Module):
    def __init__(self, hidden_dim: int, num_heads: int, dropout: float = 0.1):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = hidden_dim // num_heads
        self.q_proj = nn.Linear(hidden_dim, hidden_dim)
        self.k_proj = nn.Linear(hidden_dim, hidden_dim)
        self.v_proj = nn.Linear(hidden_dim, hidden_dim)
        self.out_proj = nn.Linear(hidden_dim, hidden_dim)
        self.norm = nn.LayerNorm(hidden_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, N, C = x.shape
        H = self.num_heads
        D = self.head_dim

        residual = x
        x = self.norm(x)

        q = self.q_proj(x).view(B, N, H, D).transpose(1, 2)
        k = self.k_proj(x).view(B, N, H, D).transpose(1, 2)
        v = self.v_proj(x).view(B, N, H, D).transpose(1, 2)

        scores = torch.matmul(q, k.transpose(-2, -1)) / (D ** 0.5)
        attn = F.softmax(scores, dim=-1)
        attn = self.dropout(attn)

        out = torch.matmul(attn, v)
        out = out.transpose(1, 2).contiguous().view(B, N, C)
        out = self.out_proj(out)

        return residual + self.dropout(out)
```

---

### `models/relation/non_local.py`

**Purpose:** Defines `NonLocalRelationModule` module/class.

```python
from typing import Optional

import torch
import torch.nn as nn
import torch.nn.functional as F


class NonLocalRelationModule(nn.Module):
    def __init__(self, hidden_dim: int = 128, num_heads: int = 8, dropout: float = 0.1, num_layers: int = 4):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
        self.head_dim = hidden_dim // num_heads
        assert hidden_dim % num_heads == 0

        self.layers = nn.ModuleList()
        for _ in range(num_layers):
            self.layers.append(NonLocalBlock(hidden_dim, num_heads, dropout))

        self.norm = nn.LayerNorm(hidden_dim)
        self.proj = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim),
        )

    def forward(
        self,
        x: torch.Tensor,
        gis_features: Optional[torch.Tensor] = None,
        gis_embeddings: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        for layer in self.layers:
            x = layer(x)
        x = self.norm(x)
        return self.proj(x) + x


class NonLocalBlock(nn.Module):
    def __init__(self, hidden_dim: int, num_heads: int = 8, dropout: float = 0.1):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.q_proj = nn.Linear(hidden_dim, hidden_dim)
        self.k_proj = nn.Linear(hidden_dim, hidden_dim)
        self.v_proj = nn.Linear(hidden_dim, hidden_dim)
        self.out_proj = nn.Linear(hidden_dim, hidden_dim)
        self.scale = nn.Parameter(torch.tensor(float(hidden_dim) ** -0.5))
        self.norm = nn.LayerNorm(hidden_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, N, C = x.shape
        residual = x
        x = self.norm(x)

        q = self.q_proj(x)
        k = self.k_proj(x)
        v = self.v_proj(x)

        attn = torch.matmul(q, k.transpose(-2, -1)) * self.scale
        attn = F.softmax(attn, dim=-1)
        attn = self.dropout(attn)

        out = torch.matmul(attn, v)
        out = self.out_proj(out)

        return residual + self.dropout(out)
```

---

### `models/relation/swin.py`

**Purpose:** Defines `SwinTransformerLayer` module/class.

```python
from typing import Optional

import torch
import torch.nn as nn


class SwinTransformerLayer(nn.Module):
    def __init__(self, hidden_dim: int, num_heads: int, window_size: int = 8, mlp_ratio: float = 4.0, dropout: float = 0.1):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
        self.window_size = window_size
        self.head_dim = hidden_dim // num_heads
        assert hidden_dim % num_heads == 0

        self.norm1 = nn.LayerNorm(hidden_dim)
        self.attn = nn.Linear(hidden_dim, hidden_dim)
        self.proj_drop = nn.Dropout(dropout)
        self.norm2 = nn.LayerNorm(hidden_dim)
        self.mlp = nn.Sequential(
            nn.Linear(hidden_dim, int(hidden_dim * mlp_ratio)),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(int(hidden_dim * mlp_ratio), hidden_dim),
            nn.Dropout(dropout),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, N, C = x.shape
        side = int(N ** 0.5)

        residual = x
        x = self.norm1(x)
        x = self.attn(x)
        x = self.proj_drop(x)
        x = residual + x

        residual = x
        x = self.norm2(x)
        x = self.mlp(x)
        x = residual + x
        return x


class SwinRelationModule(nn.Module):
    def __init__(self, hidden_dim: int = 128, num_heads: int = 8, dropout: float = 0.1, num_layers: int = 4):
        super().__init__()
        self.hidden_dim = hidden_dim
        layers = []
        for i in range(num_layers):
            layers.append(SwinTransformerLayer(
                hidden_dim=hidden_dim,
                num_heads=min(num_heads, hidden_dim // (2 ** i)),
                window_size=8,
                mlp_ratio=4.0,
                dropout=dropout,
            ))
        self.layers = nn.Sequential(*layers)
        self.norm = nn.LayerNorm(hidden_dim)
        self.proj = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim),
        )

    def forward(
        self,
        x: torch.Tensor,
        gis_features: Optional[torch.Tensor] = None,
        gis_embeddings: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        for layer in self.layers:
            x = layer(x)
        x = self.norm(x)
        return self.proj(x) + x
```

---

### `models/relation/vit.py`

**Purpose:** Defines `ViTRelationModule` module/class.

```python
from typing import Optional

import torch
import torch.nn as nn
from timm.models.vision_transformer import Block


class ViTRelationModule(nn.Module):
    def __init__(self, hidden_dim: int = 128, num_heads: int = 8, dropout: float = 0.1, num_layers: int = 4):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
        self.blocks = nn.ModuleList([
            Block(
                dim=hidden_dim,
                num_heads=num_heads,
                mlp_ratio=4.0,
                qkv_bias=True,
                proj_drop=dropout,
                attn_drop=dropout,
                drop_path=dropout,
                act_layer=nn.GELU,
                norm_layer=nn.LayerNorm,
            )
            for _ in range(num_layers)
        ])
        self.norm = nn.LayerNorm(hidden_dim)
        self.proj = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim),
        )

    def forward(
        self,
        x: torch.Tensor,
        gis_features: Optional[torch.Tensor] = None,
        gis_embeddings: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        for block in self.blocks:
            x = block(x)
        x = self.norm(x)
        return self.proj(x) + x
```

---

### `scripts/__init__.py`

**Purpose:** Implementation of `__init__.py`.

```python

```

---

### `scripts/ablation.py`

**Purpose:** Contains `main` function.

```python
import argparse
import sys
from pathlib import Path
from typing import Optional

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utils.misc import get_device
from utils.ablation import AblationManager
from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from losses import build_loss
from models import build_model


def main():
    parser = argparse.ArgumentParser(description="Run ablation study")
    parser.add_argument("--config", type=str, default="train", help="Config name")
    parser.add_argument("--checkpoint", type=str, required=True, help="Checkpoint path")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--device", type=str, default=None, help="Device")
    parser.add_argument("--output-dir", type=str, default="./outputs/tables", help="Output directory")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)
    device = get_device(args.device)

    val_dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
        split="val",
        transforms=get_val_transforms(),
    )
    val_loader = build_dataloader(
        val_dataset,
        batch_size=config.get("dataset", {}).get("val_batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    checkpoint = torch.load(args.checkpoint, map_location=device)
    model.load_state_dict(checkpoint["model_state_dict"])
    model.to(device)
    model.eval()

    loss_fn = build_loss(config.get("training", {}).get("loss", {}))
    ablation_manager = AblationManager(model, config.to_dict() if hasattr(config, "to_dict") else config)
    results = ablation_manager.run_ablation(val_loader, loss_fn, device)

    import json
    output_path = Path(args.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    with open(output_path / "ablation_results.json", "w") as f:
        json.dump(results, f, indent=2)

    ckpt_dir = Path("./checkpoints/ablation")
    ckpt_dir.mkdir(parents=True, exist_ok=True)
    torch.save({"model_state_dict": ablation_manager.model.state_dict()}, ckpt_dir / "ablated_model.pt")

    print("Ablation Results:")
    for module, metrics in results.items():
        if isinstance(metrics, dict):
            print(f"  {module}: loss={metrics['loss']:.4f}, relative_drop={metrics['relative_drop_percent']:.2f}%")
        else:
            print(f"  {module}: {metrics:.4f}")


if __name__ == "__main__":
    main()
```

---

### `scripts/analyze_metrics.py`

**Purpose:** Contains `analyze_predictions` function.

```python
import sys
from pathlib import Path
import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from models import build_model
from utils.misc import get_device


def analyze_predictions(model_name, config_name, checkpoint_path, device, root_dir="./data/processed"):
    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(config_name)

    test_dataset = GCMHAIRNetDataset(
        root_dir=root_dir,
        split="test",
        transforms=get_val_transforms(),
    )
    test_loader = build_dataloader(
        test_dataset,
        batch_size=config.get("dataset", {}).get("test_batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    checkpoint = torch.load(checkpoint_path, map_location=device)
    ckpt_state = checkpoint["model_state_dict"]
    model_state = model.state_dict()
    new_state = {}
    for key, param in ckpt_state.items():
        if key in model_state and param.shape == model_state[key].shape:
            new_state[key] = param
    model.load_state_dict(new_state, strict=False)
    model.to(device)
    model.eval()

    all_preds = []
    all_targets = []
    image_city_names = []

    with torch.no_grad():
        for batch in test_loader:
            image = batch["image"].to(device)
            gis = batch["gis"].to(device)
            label = batch["label"].to(device)
            preds = model(image, gis)
            preds_prob = torch.sigmoid(preds)

            batch_size = image.shape[0]
            pixels_per_image = image.shape[2] * image.shape[3]

            batch_preds = preds_prob.cpu().numpy().reshape(batch_size, pixels_per_image)
            batch_targets = label.cpu().numpy().reshape(batch_size, pixels_per_image)
            all_preds.append(batch_preds)
            all_targets.append(batch_targets)

            city_names = batch.get("city_name", ["unknown"] * batch_size)
            image_city_names.extend(city_names)

    preds_by_image = np.concatenate(all_preds, axis=0)
    targets_by_image = np.concatenate(all_targets, axis=0)

    print(f"\n{'='*60}")
    print(f"Model: {model_name}")
    print(f"{'='*60}")

    print("\n1. THRESHOLD USED")
    print("   Threshold: 0.5")
    print("   Method: torch.sigmoid(output) > 0.5")
    print("   Safe = 0 (pred <= 0.5), Hazardous = 1 (pred > 0.5)")

    print("\n2. CLASS DISTRIBUTION IN TEST SET")
    total_pixels = targets_by_image.size
    hazardous_pixels = np.sum(targets_by_image > 0.5)
    safe_pixels = total_pixels - hazardous_pixels
    print(f"   Total images: {len(image_city_names)}")
    print(f"   Total pixels: {total_pixels:,}")
    print(f"   Safe (<= 0.5): {safe_pixels:,} ({safe_pixels/total_pixels*100:.2f}%)")
    print(f"   Hazardous (> 0.5): {hazardous_pixels:,} ({hazardous_pixels/total_pixels*100:.2f}%)")

    print("\n3. PIXEL-WISE CLASSIFICATION METRICS (threshold=0.5)")
    threshold = 0.5
    preds_flat = preds_by_image.flatten()
    targets_flat = targets_by_image.flatten()
    preds_bin = (preds_flat > threshold).astype(int)
    targets_bin = (targets_flat > threshold).astype(int)

    tp = np.sum((preds_bin == 1) & (targets_bin == 1))
    fp = np.sum((preds_bin == 1) & (targets_bin == 0))
    tn = np.sum((preds_bin == 0) & (targets_bin == 0))
    fn = np.sum((preds_bin == 0) & (targets_bin == 1))

    accuracy = (tp + tn) / (tp + tn + fp + fn + 1e-8)
    precision = tp / (tp + fp + 1e-8)
    recall = tp / (tp + fn + 1e-8)
    f1 = 2 * precision * recall / (precision + recall + 1e-8)
    iou = tp / (tp + fp + fn + 1e-8)
    specificity = tn / (tn + fp + 1e-8)

    print(f"   Accuracy:  {accuracy:.4f}")
    print(f"   Precision: {precision:.4f}")
    print(f"   Recall:    {recall:.4f}")
    print(f"   F1:        {f1:.4f}")
    print(f"   IoU:       {iou:.4f}")
    print(f"   Specificity: {specificity:.4f}")

    print("\n4. CONFUSION MATRIX")
    print(f"                 Predicted")
    print(f"                 Safe    Hazardous")
    print(f"   Actual Safe   {tn:6d}   {fp:6d}")
    print(f"   Actual Hazard {fn:6d}   {tp:6d}")
    print(f"\n   TP={tp}, FP={fp}, TN={tn}, FN={fn}")

    print("\n5. REGRESSION METRICS")
    mse = np.mean((preds_flat - targets_flat) ** 2)
    mae = np.mean(np.abs(preds_flat - targets_flat))
    ss_res = np.sum((targets_flat - preds_flat) ** 2)
    ss_tot = np.sum((targets_flat - np.mean(targets_flat)) ** 2)
    r2 = 1 - ss_res / (ss_tot + 1e-8)
    print(f"   MSE: {mse:.6f}")
    print(f"   MAE: {mae:.6f}")
    print(f"   R2:  {r2:.4f}")

    print("\n6. PER-CITY BREAKDOWN")
    unique_cities = sorted(set(image_city_names))
    city_data = {c: {"preds": [], "targets": []} for c in unique_cities}

    for i, city in enumerate(image_city_names):
        city_data[city]["preds"].append(preds_by_image[i])
        city_data[city]["targets"].append(targets_by_image[i])

    for city in unique_cities:
        cp = np.concatenate(city_data[city]["preds"]).flatten()
        ct = np.concatenate(city_data[city]["targets"]).flatten()
        cb = (cp > 0.5).astype(int)
        ctb = (ct > 0.5).astype(int)
        city_acc = np.mean(cb == ctb)
        city_tp = np.sum((cb == 1) & (ctb == 1))
        city_fp = np.sum((cb == 1) & (ctb == 0))
        city_tn = np.sum((cb == 0) & (ctb == 0))
        city_fn = np.sum((cb == 0) & (ctb == 1))
        city_precision = city_tp / (city_tp + city_fp + 1e-8)
        city_recall = city_tp / (city_tp + city_fn + 1e-8)
        city_f1 = 2 * city_precision * city_recall / (city_precision + city_recall + 1e-8)
        city_iou = city_tp / (city_tp + city_fp + city_fn + 1e-8)
        city_mse = np.mean((cp - ct) ** 2)
        city_mae = np.mean(np.abs(cp - ct))
        ss_res_c = np.sum((ct - cp) ** 2)
        ss_tot_c = np.sum((ct - np.mean(ct)) ** 2)
        city_r2 = 1 - ss_res_c / (ss_tot_c + 1e-8)
        print(f"   {city}: n_images={len(city_data[city]['preds'])}, n_pixels={len(cp)}, Acc={city_acc:.4f}, Prec={city_precision:.4f}, Rec={city_recall:.4f}, F1={city_f1:.4f}, IoU={city_iou:.4f}, MSE={city_mse:.6f}, MAE={city_mae:.6f}, R2={city_r2:.4f}")


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="gcm", choices=["gcm", "vit", "swin", "graphsage", "mha", "nonlocal"])
    parser.add_argument("--checkpoint", type=str, default=None)
    parser.add_argument("--root-dir", type=str, default="./data/processed")
    parser.add_argument("--device", type=str, default=None)
    args = parser.parse_args()

    device = get_device(args.device)

    model_configs = {
        "gcm": ("baselines/baseline_gcm", "./checkpoints/baselines/gcm/epoch_0103.pt"),
        "vit": ("baselines/baseline_vit", "./checkpoints/baselines/vit/best.pt"),
        "swin": ("baselines/baseline_swin", "./checkpoints/baselines/swin/best.pt"),
        "graphsage": ("baselines/baseline_graphsage", "./checkpoints/baselines/graphsage/best.pt"),
        "mha": ("baselines/baseline_mha", "./checkpoints/baselines/mha/best.pt"),
        "nonlocal": ("baselines/baseline_nonlocal", "./checkpoints/baselines/nonlocal/best.pt"),
    }

    if args.checkpoint:
        config_name, ckpt = args.model, args.checkpoint
    else:
        config_name, ckpt = model_configs[args.model]

    analyze_predictions(args.model.upper(), config_name, ckpt, device, args.root_dir)


if __name__ == "__main__":
    main()
```

---

### `scripts/collect_results.py`

**Purpose:** Contains `collect_results` function.

```python
import json
import os
from pathlib import Path
from typing import Dict, List

import torch


def collect_results(checkpoint_dirs: List[str], output_dir: str = "./outputs/tables") -> Dict[str, Dict[str, float]]:
    results = {}
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for ckpt_dir in checkpoint_dirs:
        ckpt_path = Path(ckpt_dir)
        if not ckpt_path.exists():
            continue

        best_metrics = None
        best_loss = float("inf")
        best_epoch = -1

        for ckpt_file in sorted(ckpt_path.glob("*.pt")):
            try:
                checkpoint = torch.load(ckpt_file, map_location="cpu")
                if "metrics" not in checkpoint:
                    continue
                metrics = checkpoint["metrics"]
                val_loss = metrics.get("val_loss", float("inf"))
                if val_loss < best_loss:
                    best_loss = val_loss
                    best_metrics = metrics
                    best_epoch = checkpoint.get("epoch", -1)
            except Exception:
                continue

        if best_metrics:
            model_name = ckpt_path.parent.name
            run_name = ckpt_path.name
            key = f"{model_name}/{run_name}"
            results[key] = {
                "val_loss": best_metrics.get("val_loss", float("inf")),
                "val_mae": best_metrics.get("mae", float("inf")),
                "val_mse": best_metrics.get("mse", float("inf")),
                "val_rmse": best_metrics.get("rmse", float("inf")),
                "val_r2": best_metrics.get("r2", float("-inf")),
                "val_mape": best_metrics.get("mape", float("inf")),
                "best_epoch": best_epoch,
            }

    if results:
        json_path = output_path / "results.json"
        with open(json_path, "w") as f:
            json.dump(results, f, indent=2)

        csv_path = output_path / "results.csv"
        with open(csv_path, "w") as f:
            f.write("model,val_loss,val_mae,val_mse,val_rmse,val_r2,val_mape,best_epoch\n")
            for key, metrics in results.items():
                f.write(f"{key},{metrics['val_loss']},{metrics['val_mae']},{metrics['val_mse']},{metrics['val_rmse']},{metrics['val_r2']},{metrics['val_mape']},{metrics['best_epoch']}\n")

    return results


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Collect experiment results from checkpoints")
    parser.add_argument("--checkpoint-dirs", nargs="+", default=[
        "./checkpoints/baseline/resnet",
        "./checkpoints/baseline/vit",
        "./checkpoints/baseline/swin",
        "./checkpoints/baseline/image_only",
        "./checkpoints/baseline/gis_only",
        "./checkpoints/gcm",
        "./checkpoints/ablation",
        "./checkpoints/crossval",
    ], help="Checkpoint directories to scan")
    parser.add_argument("--output-dir", type=str, default="./outputs/tables", help="Output directory")
    args = parser.parse_args()

    results = collect_results(args.checkpoint_dirs, args.output_dir)
    print(f"Collected results for {len(results)} models:")
    for model_name, metrics in results.items():
        print(f"  {model_name}: val_loss={metrics['val_loss']:.4f}, val_mae={metrics['val_mae']:.4f}")


if __name__ == "__main__":
    main()
```

---

### `scripts/compare_models.py`

**Purpose:** Contains `load_results` function.

```python
import json
from pathlib import Path
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np


def load_results(results_path: str = "./outputs/tables/results.json") -> Dict[str, Dict[str, float]]:
    path = Path(results_path)
    if not path.exists():
        raise FileNotFoundError(f"Results file not found: {path}")
    with open(path, "r") as f:
        return json.load(f)


def plot_metric_comparison(
    results: Dict[str, Dict[str, float]],
    metric: str,
    output_path: str,
    title: str,
    ylabel: str,
    figsize: tuple = (10, 6),
):
    models = []
    values = []
    for model_name, metrics in results.items():
        if metric in metrics and not np.isinf(metrics[metric]):
            models.append(model_name)
            values.append(metrics[metric])

    if not values:
        return

    fig, ax = plt.subplots(figsize=figsize)
    bars = ax.bar(models, values, color="steelblue")
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_xlabel("Model", fontsize=12)
    ax.tick_params(axis="x", rotation=45, labelsize=9)
    ax.grid(axis="y", alpha=0.3)

    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{val:.4f}", ha="center", va="bottom", fontsize=8)

    plt.tight_layout()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def compare_models(results_path: str = "./outputs/tables/results.json", output_dir: str = "./outputs/comparison"):
    results = load_results(results_path)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    metrics_to_plot = [
        ("val_mae", "MAE Comparison", "Mean Absolute Error"),
        ("val_mse", "MSE Comparison", "Mean Squared Error"),
        ("val_rmse", "RMSE Comparison", "Root Mean Squared Error"),
        ("val_r2", "R² Comparison", "R² Score"),
    ]

    for metric, title, ylabel in metrics_to_plot:
        plot_metric_comparison(
            results,
            metric,
            str(output_path / f"{metric}_comparison.png"),
            title,
            ylabel,
        )

    summary_path = output_path / "comparison_summary.txt"
    with open(summary_path, "w") as f:
        f.write("Model Comparison Summary\n")
        f.write("=" * 80 + "\n\n")
        for model_name, metrics in results.items():
            f.write(f"Model: {model_name}\n")
            f.write(f"  Val Loss:  {metrics.get('val_loss', float('inf')):.4f}\n")
            f.write(f"  Val MAE:   {metrics.get('val_mae', float('inf')):.4f}\n")
            f.write(f"  Val MSE:   {metrics.get('val_mse', float('inf')):.4f}\n")
            f.write(f"  Val RMSE:  {metrics.get('val_rmse', float('inf')):.4f}\n")
            f.write(f"  Val R²:    {metrics.get('val_r2', float('-inf')):.4f}\n")
            f.write(f"  Best Epoch: {metrics.get('best_epoch', -1)}\n")
            f.write("\n")

    print(f"Comparison plots saved to {output_dir}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Compare model results and generate plots")
    parser.add_argument("--results", type=str, default="./outputs/tables/results.json", help="Path to results JSON")
    parser.add_argument("--output-dir", type=str, default="./outputs/comparison", help="Output directory for plots")
    args = parser.parse_args()

    compare_models(args.results, args.output_dir)


if __name__ == "__main__":
    main()
```

---

### `scripts/crossval.py`

**Purpose:** Contains `main` function.

```python
import argparse
import sys
from pathlib import Path
from typing import Optional

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_crossval_dataloaders, get_train_transforms, get_val_transforms
from engine import Trainer
from models import build_model
from utils.misc import get_device


def main():
    parser = argparse.ArgumentParser(description="Run cross-validation for GCM-HAIRNet")
    parser.add_argument("--config", type=str, default="crossval", help="Config name")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--device", type=str, default=None, help="Device")
    parser.add_argument("--output-dir", type=str, default="./outputs/crossval", help="Output directory")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)
    device = get_device(args.device)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    cv_config = config.get("cross_validation", {})
    num_folds = cv_config.get("folds", 5)
    seed = config.get("experiment", {}).get("seed", 42)

    fold_results = {}

    for fold in range(num_folds):
        print(f"\n{'='*50}")
        print(f"Fold {fold + 1}/{num_folds}")
        print(f"{'='*50}")

        train_loader, val_loader = build_crossval_dataloaders(
            root_dir=args.root_dir,
            fold=fold,
            num_folds=num_folds,
            batch_size=config.get("dataset", {}).get("train_batch_size", 16),
            num_workers=0,
            seed=seed,
            transforms_train=get_train_transforms(),
            transforms_val=get_val_transforms(),
        )

        model = build_model(config.get("model", {}))
        trainer = Trainer(model, train_loader, val_loader, config, device)
        trainer.fit()

        fold_results[f"fold_{fold}"] = {
            "best_val_loss": trainer.checkpoint_manager.best_value,
        }

    import json
    with open(output_dir / "crossval_results.json", "w") as f:
        json.dump(fold_results, f, indent=2)

    print(f"\nCross-validation complete. Results saved to {output_dir / 'crossval_results.json'}")


if __name__ == "__main__":
    main()
```

---

### `scripts/diagnose.py`

**Purpose:** Contains `main` function.

```python
import argparse
import sys
from pathlib import Path

import torch
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from models import GCMHAIRNet
from utils.misc import get_device


def main():
    parser = argparse.ArgumentParser(description="Diagnose model predictions")
    parser.add_argument("--config", type=str, default="train", help="Config name")
    parser.add_argument("--checkpoint", type=str, required=True, help="Checkpoint path")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--device", type=str, default=None, help="Device")
    parser.add_argument("--split", type=str, default="val", help="Data split")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)
    device = get_device(args.device)

    dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
        split=args.split,
        transforms=get_val_transforms(),
    )
    loader = build_dataloader(
        dataset,
        batch_size=1,
        shuffle=False,
        num_workers=0,
        drop_last=False,
    )

    model = GCMHAIRNet(config.get("model", {}))
    checkpoint = torch.load(args.checkpoint, map_location=device)
    model.load_state_dict(checkpoint["model_state_dict"], strict=False)
    model.to(device)
    model.eval()

    print(f"Analyzing {len(dataset)} samples from {args.split} split")
    print("=" * 60)

    all_preds = []
    all_targets = []
    all_pred_mins = []
    all_pred_maxs = []
    all_pred_means = []
    all_pred_stds = []

    with torch.no_grad():
        for i, batch in enumerate(loader):
            image = batch["image"].to(device)
            gis = batch["gis"].to(device)
            label = batch["label"].to(device)
            city = batch.get("city_name", [f"sample_{i}"])[0]

            preds = model(image, gis)
            preds_prob = torch.sigmoid(preds)

            all_preds.append(preds_prob.cpu().numpy().flatten())
            all_targets.append(label.cpu().numpy().flatten())
            all_pred_mins.append(preds_prob.min().item())
            all_pred_maxs.append(preds_prob.max().item())
            all_pred_means.append(preds_prob.mean().item())
            all_pred_stds.append(preds_prob.std().item())

            print(f"\nSample {i+1}: {city}")
            print(f"  Label  - min: {label.min():.4f}, max: {label.max():.4f}, mean: {label.mean():.4f}, std: {label.std():.4f}")
            print(f"  Pred   - min: {preds_prob.min():.4f}, max: {preds_prob.max():.4f}, mean: {preds_prob.mean():.4f}, std: {preds_prob.std():.4f}")
            print(f"  Error  - MSE: {((preds_prob - label)**2).mean():.4f}, MAE: {(preds_prob - label).abs().mean():.4f}")

    all_preds = np.concatenate(all_preds)
    all_targets = np.concatenate(all_targets)

    print("\n" + "=" * 60)
    print("OVERALL STATISTICS")
    print("=" * 60)
    print(f"Predictions - min: {all_preds.min():.4f}, max: {all_preds.max():.4f}, mean: {all_preds.mean():.4f}, std: {all_preds.std():.4f}")
    print(f"Targets     - min: {all_targets.min():.4f}, max: {all_targets.max():.4f}, mean: {all_targets.mean():.4f}, std: {all_targets.std():.4f}")
    print(f"Global MSE: {((all_preds - all_targets)**2).mean():.4f}")
    print(f"Global MAE: {np.abs(all_preds - all_targets).mean():.4f}")

    # Check if predictions are too narrow (collapsed)
    pred_range = all_preds.max() - all_preds.min()
    target_range = all_targets.max() - all_targets.min()
    print(f"\nPrediction range: {pred_range:.4f} (target: {target_range:.4f})")
    if pred_range < 0.1:
        print("WARNING: Predictions are very narrow - model may be collapsed!")
    if pred_range < target_range * 0.5:
        print("WARNING: Predictions have much less variance than targets!")

    # R² calculation
    ss_res = np.sum((all_targets - all_preds) ** 2)
    ss_tot = np.sum((all_targets - np.mean(all_targets)) ** 2)
    r2 = 1 - ss_res / (ss_tot + 1e-8)
    print(f"Global R²: {r2:.4f}")

    # Check prediction distribution
    print(f"\nPrediction percentiles:")
    for p in [1, 5, 25, 50, 75, 95, 99]:
        print(f"  {p}th: {np.percentile(all_preds, p):.4f}")


if __name__ == "__main__":
    main()
```

---

### `scripts/evaluate_all_baselines.py`

**Purpose:** Contains `evaluate_model` function.

```python
import json
import sys
from pathlib import Path
import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from models import build_model
from utils.misc import get_device


def evaluate_model(model_name, config_name, checkpoint_path, device, root_dir="./data/processed"):
    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(config_name)

    test_dataset = GCMHAIRNetDataset(
        root_dir=root_dir,
        split="test",
        transforms=get_val_transforms(),
    )
    test_loader = build_dataloader(
        test_dataset,
        batch_size=config.get("dataset", {}).get("test_batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    checkpoint = torch.load(checkpoint_path, map_location=device)
    ckpt_state = checkpoint["model_state_dict"]
    model_state = model.state_dict()
    new_state = {}
    for key, param in ckpt_state.items():
        if key in model_state and param.shape == model_state[key].shape:
            new_state[key] = param
    model.load_state_dict(new_state, strict=False)
    model.to(device)
    model.eval()

    all_preds = []
    all_targets = []
    image_city_names = []

    with torch.no_grad():
        for batch in test_loader:
            image = batch["image"].to(device)
            gis = batch["gis"].to(device)
            label = batch["label"].to(device)
            preds = model(image, gis)
            preds_prob = torch.sigmoid(preds)

            batch_size = image.shape[0]
            pixels_per_image = image.shape[2] * image.shape[3]

            batch_preds = preds_prob.cpu().numpy().reshape(batch_size, pixels_per_image)
            batch_targets = label.cpu().numpy().reshape(batch_size, pixels_per_image)
            all_preds.append(batch_preds)
            all_targets.append(batch_targets)

            city_names = batch.get("city_name", ["unknown"] * batch_size)
            image_city_names.extend(city_names)

    preds_by_image = np.concatenate(all_preds, axis=0)
    targets_by_image = np.concatenate(all_targets, axis=0)
    preds_flat = preds_by_image.flatten()
    targets_flat = targets_by_image.flatten()

    threshold = 0.5
    preds_bin = (preds_flat > threshold).astype(int)
    targets_bin = (targets_flat > threshold).astype(int)

    tp = float(np.sum((preds_bin == 1) & (targets_bin == 1)))
    fp = float(np.sum((preds_bin == 1) & (targets_bin == 0)))
    tn = float(np.sum((preds_bin == 0) & (targets_bin == 0)))
    fn = float(np.sum((preds_bin == 0) & (targets_bin == 1)))

    accuracy = (tp + tn) / (tp + tn + fp + fn + 1e-8)
    precision = tp / (tp + fp + 1e-8)
    recall = tp / (tp + fn + 1e-8)
    f1 = 2 * precision * recall / (precision + recall + 1e-8)
    iou = tp / (tp + fp + fn + 1e-8)
    specificity = tn / (tn + fp + 1e-8)

    mse = float(np.mean((preds_flat - targets_flat) ** 2))
    mae = float(np.mean(np.abs(preds_flat - targets_flat)))
    ss_res = np.sum((targets_flat - preds_flat) ** 2)
    ss_tot = np.sum((targets_flat - np.mean(targets_flat)) ** 2)
    r2 = float(1 - ss_res / (ss_tot + 1e-8))

    total_pixels = int(targets_flat.size)
    hazardous_pixels = int(np.sum(targets_flat > 0.5))
    safe_pixels = total_pixels - hazardous_pixels

    per_city = {}
    unique_cities = sorted(set(image_city_names))
    city_data = {c: {"preds": [], "targets": []} for c in unique_cities}

    for i, city in enumerate(image_city_names):
        city_data[city]["preds"].append(preds_by_image[i])
        city_data[city]["targets"].append(targets_by_image[i])

    for city in unique_cities:
        cp = np.concatenate(city_data[city]["preds"]).flatten()
        ct = np.concatenate(city_data[city]["targets"]).flatten()
        cb = (cp > 0.5).astype(int)
        ctb = (ct > 0.5).astype(int)
        city_acc = float(np.mean(cb == ctb))
        city_tp = float(np.sum((cb == 1) & (ctb == 1)))
        city_fp = float(np.sum((cb == 1) & (ctb == 0)))
        city_tn = float(np.sum((cb == 0) & (ctb == 0)))
        city_fn = float(np.sum((cb == 0) & (ctb == 1)))
        city_precision = city_tp / (city_tp + city_fp + 1e-8)
        city_recall = city_tp / (city_tp + city_fn + 1e-8)
        city_f1 = 2 * city_precision * city_recall / (city_precision + city_recall + 1e-8)
        city_iou = city_tp / (city_tp + city_fp + city_fn + 1e-8)
        city_mse = float(np.mean((cp - ct) ** 2))
        city_mae = float(np.mean(np.abs(cp - ct)))
        ss_res_c = np.sum((ct - cp) ** 2)
        ss_tot_c = np.sum((ct - np.mean(ct)) ** 2)
        city_r2 = float(1 - ss_res_c / (ss_tot_c + 1e-8))

        per_city[city] = {
            "n_images": len(city_data[city]["preds"]),
            "n_pixels": len(cp),
            "accuracy": city_acc,
            "precision": city_precision,
            "recall": city_recall,
            "f1": city_f1,
            "iou": city_iou,
            "mse": city_mse,
            "mae": city_mae,
            "r2": city_r2,
            "safe_pixels": int(np.sum(ct <= 0.5)),
            "hazardous_pixels": int(np.sum(ct > 0.5)),
        }

    result = {
        "model_name": model_name,
        "config": config_name,
        "checkpoint": checkpoint_path,
        "threshold": threshold,
        "class_distribution": {
            "total_pixels": total_pixels,
            "safe_pixels": safe_pixels,
            "hazardous_pixels": hazardous_pixels,
            "safe_percentage": round(safe_pixels / total_pixels * 100, 2),
            "hazardous_percentage": round(hazardous_pixels / total_pixels * 100, 2),
        },
        "overall_metrics": {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "iou": iou,
            "specificity": specificity,
            "mse": mse,
            "mae": mae,
            "r2": r2,
        },
        "confusion_matrix": {
            "tp": tp,
            "fp": fp,
            "tn": tn,
            "fn": fn,
        },
        "per_city": per_city,
    }

    return result


def main():
    device = get_device(None)
    print(f"Using device: {device}")

    baseline_dir = Path("./checkpoints/baselines")
    output_path = Path("./outputs/baselines/all_baseline_metrics.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    model_configs = {
        "addition": "baseline_addition",
        "bilinear": "baseline_bilinear",
        "concat": "baseline_concat",
        "cross_attention": "baseline_cross_attention",
        "gated": "baseline_gated",
        "gcm": "baselines/baseline_gcm",
        "gis_only": "baseline_gis_only",
        "image_only": "baseline_image_only",
        "multihead_cross_attention": "baseline_multihead_cross_attention",
        "swin": "baselines/baseline_swin",
        "vit": "baselines/baseline_vit",
        "graphsage": "baselines/baseline_graphsage",
        "mha": "baselines/baseline_mha",
        "nonlocal": "baselines/baseline_nonlocal",
    }

    results = {}
    missing = []
    skipped = []

    for model_name, config_name in model_configs.items():
        ckpt_dir = baseline_dir / model_name
        best_path = ckpt_dir / "best.pt"

        if not best_path.exists():
            missing.append(f"{model_name}: {best_path}")
            continue

        print(f"\nEvaluating {model_name} ...")
        try:
            result = evaluate_model(model_name, config_name, str(best_path), device)
            results[model_name] = result
            print(f"  -> Acc={result['overall_metrics']['accuracy']:.4f}, R2={result['overall_metrics']['r2']:.4f}")
        except Exception as e:
            skipped.append(f"{model_name}: {e}")
            print(f"  -> SKIPPED: {e}")

    output = {
        "evaluated": results,
        "missing_checkpoints": missing,
        "skipped_models": skipped,
        "note": "Fusion study models (addition, bilinear, concat, etc.) use BaselineModel. New controlled baselines (gcm, vit, swin, etc.) use GCMHAIRNetBaseline.",
    }

    with open(output_path, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\n{'='*60}")
    print(f"Evaluated: {len(results)} models")
    print(f"Missing:   {len(missing)} models")
    print(f"Skipped:   {len(skipped)} models")
    print(f"Saved to:  {output_path}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
```

---

### `scripts/finetune_gcm.py`

**Purpose:** Defines `DynamicLR:` module/class.

```python
import argparse
import sys
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_train_transforms, get_val_transforms
from engine import Trainer
from models import build_model
from utils.misc import get_device


class DynamicLR:
    def __init__(self, optimizer, init_lr, factor=0.5, patience=10, min_lr=1e-7, max_lr=1e-3, increase_factor=1.05):
        self.optimizer = optimizer
        self.current_lr = init_lr
        self.factor = factor
        self.patience = patience
        self.min_lr = min_lr
        self.max_lr = max_lr
        self.increase_factor = increase_factor
        self.best_loss = float("inf")
        self.num_bad_epochs = 0
        self.consecutive_improvements = 0

        for param_group in optimizer.param_groups:
            param_group["lr"] = init_lr

    def step(self, val_loss):
        if val_loss < self.best_loss:
            self.best_loss = val_loss
            self.num_bad_epochs = 0
            self.consecutive_improvements += 1
            if self.consecutive_improvements >= 3:
                self.current_lr = min(self.current_lr * self.increase_factor, self.max_lr)
                for param_group in self.optimizer.param_groups:
                    param_group["lr"] = self.current_lr
                self.consecutive_improvements = 0
                return f"LR increased to {self.current_lr:.2e}"
        else:
            self.num_bad_epochs += 1
            self.consecutive_improvements = 0
            if self.num_bad_epochs >= self.patience:
                self.current_lr = max(self.current_lr * self.factor, self.min_lr)
                for param_group in self.optimizer.param_groups:
                    param_group["lr"] = self.current_lr
                self.num_bad_epochs = 0
                return f"LR decreased to {self.current_lr:.2e}"
        return None


def main():
    parser = argparse.ArgumentParser(description="Dynamic fine-tune GCM-HAIRNet with auto LR adjustment")
    parser.add_argument("--config", type=str, default="baselines/baseline_gcm", help="Config name")
    parser.add_argument("--checkpoint", type=str, default="./checkpoints/baselines/gcm/last.pt", help="Checkpoint to resume from")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root directory")
    parser.add_argument("--device", type=str, default=None, help="Device to use (cuda, mps, cpu)")
    parser.add_argument("--output-dir", type=str, default="./outputs/baselines/gcm", help="Output directory")
    parser.add_argument("--lr", type=float, default=1e-4, help="Initial fine-tuning learning rate")
    parser.add_argument("--additional-epochs", type=int, default=100, help="Additional epochs to train beyond current checkpoint")
    parser.add_argument("--patience", type=int, default=10, help="LR reduction patience")
    parser.add_argument("--factor", type=float, default=0.5, help="LR reduction factor")
    parser.add_argument("--min-lr", type=float, default=1e-7, help="Minimum learning rate")
    parser.add_argument("--max-lr", type=float, default=1e-3, help="Maximum learning rate")
    parser.add_argument("--increase-factor", type=float, default=1.05, help="LR increase factor when improving")
    parser.add_argument("--grad-clip", type=float, default=1.0, help="Gradient clipping value")
    parser.add_argument("--early-stopping-patience", type=int, default=30, help="Early stopping patience")
    args = parser.parse_args()

    device = get_device(args.device)

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)

    checkpoint_path = Path(args.checkpoint)
    if not checkpoint_path.exists():
        print(f"Checkpoint not found: {checkpoint_path}")
        sys.exit(1)

    ckpt = torch.load(checkpoint_path, map_location="cpu")
    start_epoch = ckpt.get("epoch", 0) + 1
    total_epochs = start_epoch + args.additional_epochs

    config["training.epochs"] = total_epochs
    config["training.optimizer.lr"] = args.lr
    config["training.gradient_clip_val"] = args.grad_clip
    config["training.early_stopping.patience"] = args.early_stopping_patience
    config["outputs.root_dir"] = args.output_dir

    train_dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
        split="train",
        transforms=get_train_transforms(),
    )
    val_dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
        split="val",
        transforms=get_val_transforms(),
    )

    train_loader = build_dataloader(
        train_dataset,
        batch_size=config.get("dataset", {}).get("train_batch_size", 16),
        shuffle=True,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=True,
    )
    val_loader = build_dataloader(
        val_dataset,
        batch_size=config.get("dataset", {}).get("val_batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    model.load_state_dict(ckpt["model_state_dict"], strict=False)
    model.to(device)
    print(f"Loaded model weights from: {checkpoint_path}")

    vis_dir = str(Path(args.output_dir) / "gcm_attention")
    trainer = Trainer(model, train_loader, val_loader, config, device, vis_dir=vis_dir)

    for param_group in trainer.optimizer.param_groups:
        param_group["lr"] = args.lr
    print(f"Fine-tuning learning rate set to: {args.lr}")

    dynamic_lr = DynamicLR(
        trainer.optimizer,
        init_lr=args.lr,
        factor=args.factor,
        patience=args.patience,
        min_lr=args.min_lr,
        max_lr=args.max_lr,
        increase_factor=args.increase_factor,
    )

    def epoch_callback(epoch, val_metrics):
        val_loss = val_metrics.get("val_loss", float("inf"))
        lr_msg = dynamic_lr.step(val_loss)
        if lr_msg:
            print(f"  -> {lr_msg}")

    trainer.epoch = start_epoch
    trainer.num_epochs = total_epochs
    print(f"Resuming from epoch {start_epoch}, training until epoch {total_epochs}")

    trainer.fit(epoch_callback=epoch_callback)


if __name__ == "__main__":
    main()
```

---

### `scripts/generate_all_risk_maps.py`

**Purpose:** Contains `clean_canonical_csv` function.

```python
#!/usr/bin/env python3
"""
Comprehensive post-processing script:
1. Run inference on all models to generate predictions
2. Generate risk maps with green-to-red colormap
3. Generate comparison grids (3 images per row)
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from models import build_model
from utils.misc import get_device


# ─────────────────────────────────────────────
# 1. CANONICAL CSV CLEANING
# ─────────────────────────────────────────────
def clean_canonical_csv(csv_path: Path):
    """Rename invalid ablation row."""
    import csv

    # Read existing
    rows = []
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)

    # Rename baseline,GCM-HAIRNet,full -> baseline,GCM-Ablation-Full,full
    for r in rows:
        if r["model"] == "GCM-HAIRNet" and r["variant"] == "full":
            r["model"] = "GCM-Ablation-Full"

    # Write back
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            clean_row = {k: ("" if v is None else str(v)) for k, v in r.items()}
            writer.writerow(clean_row)

    print(f"[CSV] Cleaned canonical results saved to {csv_path}")
    return rows


# ─────────────────────────────────────────────
# 2. INFERENCE ENGINE
# ─────────────────────────────────────────────
def load_model_from_checkpoint(config, checkpoint_path, device):
    """Build model and load checkpoint with flexible state dict matching."""
    model = build_model(config.get("model", {}))
    checkpoint = torch.load(checkpoint_path, map_location=device)
    ckpt_state = checkpoint["model_state_dict"]
    model_state = model.state_dict()

    new_state = {}
    matched = 0
    skipped = 0
    for key, param in ckpt_state.items():
        if key in model_state:
            if param.shape == model_state[key].shape:
                new_state[key] = param
                matched += 1
            else:
                skipped += 1
        else:
            skipped += 1

    result = model.load_state_dict(new_state, strict=False)
    if result.missing_keys or result.unexpected_keys:
        print(f"  Warning: Partial load - missing: {len(result.missing_keys)}, unexpected: {len(result.unexpected_keys)}")
    if skipped > 0:
        print(f"  Info: Loaded {matched} layers, skipped {skipped} incompatible layers")

    model.to(device)
    model.eval()
    return model


def run_inference(model, loader, device) -> tuple[np.ndarray, np.ndarray, list]:
    """Run inference and return predictions, targets, city names."""
    all_preds = []
    all_targets = []
    all_cities = []

    with torch.no_grad():
        for batch in loader:
            image = batch["image"].to(device, non_blocking=True)
            gis = batch["gis"].to(device, non_blocking=True)
            label = batch["label"].to(device, non_blocking=True)

            preds = torch.sigmoid(model(image, gis)).cpu().numpy()
            all_preds.append(preds)
            all_targets.append(label.cpu().numpy())
            all_cities.extend(batch.get("city_name", []))

    preds = np.concatenate(all_preds, axis=0)
    targets = np.concatenate(all_targets, axis=0)
    return preds, targets, all_cities


def get_model_config_mapping() -> dict:
    """Return mapping of model_name -> (config_name, checkpoint_path)."""
    mapping = {}

    # Fusion models
    fusion_models = [
        "image_only", "gis_only", "concat", "addition",
        "gated", "cross_attention", "multihead_cross_attention", "bilinear",
    ]
    for m in fusion_models:
        mapping[m] = (f"baseline_{m}", f"checkpoints/baselines/{m}/best.pt")

    # Controlled baselines
    baseline_models = ["gcm", "vit", "swin", "graphsage", "mha", "nonlocal"]
    for m in baseline_models:
        mapping[m] = (f"baselines/baseline_{m}", f"checkpoints/baselines/{m}/best.pt")

    # Ablations (skip - no checkpoints exist; use JSON metrics only)
    ablation_models = [
        "full", "no_distance", "no_similarity", "no_road", "no_urban",
        "no_learned", "no_scene_weights", "no_gcm", "no_gct", "no_gct_no_gcm",
    ]
    for m in ablation_models:
        mapping[f"ablation_{m}"] = (f"gcm_ablation/{m}", f"checkpoints/ablations/{m}/best.pt")

    return mapping


# ─────────────────────────────────────────────
# 3. RISK MAP GENERATION
# ─────────────────────────────────────────────
def save_risk_map_grid(
    predictions: np.ndarray,
    targets: np.ndarray,
    city_names: list,
    output_path: Path,
    model_name: str,
    split: str,
    cmap: str = "RdYlGn_r",
    n_cols: int = 3,
):
    """Save a grid of risk maps: predictions and targets, 3 per row."""
    try:
        import matplotlib.pyplot as plt
        from matplotlib.colors import LinearSegmentedColormap
    except ImportError:
        print("Matplotlib not available, skipping grid generation")
        return

    output_path.mkdir(parents=True, exist_ok=True)

    n_images = len(predictions)
    n_rows = int(np.ceil(n_images / n_cols))

    # Create figure with 2 rows per image (pred + target), 3 columns
    fig, axes = plt.subplots(n_rows * 2, n_cols, figsize=(n_cols * 5, n_rows * 5))
    if n_rows * n_cols == 1:
        axes = np.array([[axes[0], axes[1]]])
    elif n_rows == 1:
        axes = axes.reshape(2, n_cols)
    else:
        axes = axes.reshape(n_rows * 2, n_cols)

    fig.suptitle(f"{model_name} — {split} set", fontsize=16, y=0.98)

    for idx in range(n_images):
        row = (idx // n_cols) * 2
        col = idx % n_cols

        pred = predictions[idx].squeeze()
        target = targets[idx].squeeze()
        city = city_names[idx] if idx < len(city_names) else f"img_{idx}"

        # Target row
        ax_target = axes[row, col]
        im_t = ax_target.imshow(target, cmap=cmap, vmin=0, vmax=1)
        ax_target.set_title(f"GT: {city}", fontsize=10)
        ax_target.axis("off")

        # Prediction row
        ax_pred = axes[row + 1, col]
        im_p = ax_pred.imshow(pred, cmap=cmap, vmin=0, vmax=1)
        ax_pred.set_title(f"Pred: {city}", fontsize=10)
        ax_pred.axis("off")

    # Hide empty subplots
    total_slots = n_rows * n_cols
    for idx in range(n_images, total_slots):
        row = (idx // n_cols) * 2
        col = idx % n_cols
        axes[row, col].axis("off")
        axes[row + 1, col].axis("off")

    # Add colorbar
    cbar_ax = fig.add_axes([0.92, 0.15, 0.015, 0.7])
    fig.colorbar(im_p, cax=cbar_ax, label="Risk Probability")

    plt.tight_layout(rect=[0, 0, 0.9, 0.96])
    fig.savefig(output_path / f"{split}_risk_maps_grid.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved grid: {output_path / f'{split}_risk_maps_grid.png'}")


def save_individual_maps(
    predictions: np.ndarray,
    targets: np.ndarray,
    city_names: list,
    output_path: Path,
    model_name: str,
    split: str,
    cmap: str = "RdYlGn_r",
):
    """Save individual risk map PNGs and NPY files."""
    output_path.mkdir(parents=True, exist_ok=True)

    for idx, (pred, target) in enumerate(zip(predictions, targets)):
        city = city_names[idx] if idx < len(city_names) else f"img_{idx}"
        pred_2d = pred.squeeze()
        target_2d = target.squeeze()

        # Save npy
        np.save(output_path / f"{city}_predictions.npy", pred_2d)
        np.save(output_path / f"{city}_targets.npy", target_2d)

        # Save PNGs
        try:
            import matplotlib.pyplot as plt

            fig, axes = plt.subplots(1, 3, figsize=(15, 5))

            axes[0].imshow(target_2d, cmap=cmap, vmin=0, vmax=1)
            axes[0].set_title(f"Ground Truth: {city}")
            axes[0].axis("off")

            axes[1].imshow(pred_2d, cmap=cmap, vmin=0, vmax=1)
            axes[1].set_title(f"Prediction: {city}")
            axes[1].axis("off")

            diff = np.abs(target_2d - pred_2d)
            axes[2].imshow(diff, cmap="viridis")
            axes[2].set_title(f"Absolute Error: {city}")
            axes[2].axis("off")

            fig.savefig(output_path / f"{city}_comparison.png", dpi=100, bbox_inches="tight")
            plt.close(fig)
        except ImportError:
            pass

    print(f"  Saved {len(predictions)} individual maps to {output_path}")


# ─────────────────────────────────────────────
# 4. MAIN ORCHESTRATION
# ─────────────────────────────────────────────
def process_model(model_name, config_name, checkpoint_path, device, root_dir, output_base, split="val"):
    """Run inference and generate risk maps for a single model."""
    print(f"\n{'='*60}")
    print(f"Processing: {model_name} (config={config_name}, ckpt={checkpoint_path})")
    print(f"{'='*60}")

    ckpt_path = Path(checkpoint_path)
    if not ckpt_path.exists():
        print(f"  SKIP: Checkpoint not found: {ckpt_path}")
        return None

    try:
        config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
        config = config_manager.load(config_name)
    except Exception as e:
        print(f"  SKIP: Config load failed: {e}")
        return None

    try:
        dataset = GCMHAIRNetDataset(
            root_dir=root_dir,
            split=split,
            transforms=get_val_transforms(),
        )
        loader = build_dataloader(
            dataset,
            batch_size=config.get("dataset", {}).get("test_batch_size", 32),
            shuffle=False,
            num_workers=0,
            pin_memory=(device.type == "cuda"),
            drop_last=False,
        )
    except Exception as e:
        print(f"  SKIP: Dataset load failed: {e}")
        return None

    try:
        model = load_model_from_checkpoint(config, str(ckpt_path), device)
        preds, targets, cities = run_inference(model, loader, device)
    except Exception as e:
        print(f"  SKIP: Inference failed: {e}")
        return None

    # Save outputs
    model_out_dir = Path(output_base) / model_name / split
    model_out_dir.mkdir(parents=True, exist_ok=True)

    np.save(model_out_dir / f"{split}_predictions.npy", preds)
    np.save(model_out_dir / f"{split}_targets.npy", targets)

    with open(model_out_dir / f"{split}_cities.json", "w") as f:
        json.dump(cities, f, indent=2)

    save_risk_map_grid(preds, targets, cities, model_out_dir, model_name, split)
    save_individual_maps(preds, targets, cities, model_out_dir, model_name, split)

    print(f"  Done. Processed {len(cities)} images.")
    return {"predictions": preds, "targets": targets, "cities": cities}


def main():
    parser = argparse.ArgumentParser(description="Generate risk maps for all models")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--output-dir", type=str, default="./outputs/experiments", help="Output directory")
    parser.add_argument("--splits", nargs="+", default=["val", "test"], help="Splits to process")
    parser.add_argument("--skip-existing", action="store_true", help="Skip if predictions exist")
    args = parser.parse_args()

    device = get_device(None)
    print(f"Using device: {device}")

    # 1. Clean canonical CSV
    csv_path = Path(args.output_dir) / "results" / "experiment_results.csv"
    if csv_path.exists():
        clean_canonical_csv(csv_path)
    else:
        print(f"Warning: Canonical CSV not found at {csv_path}")

    # 2. Define all models to process
    model_configs = get_model_config_mapping()

    # 3. Process each model
    results = {}
    for model_name, (config_name, ckpt_path) in model_configs.items():
        for split in args.splits:
            preds_path = Path(args.output_dir) / model_name / split / f"{split}_predictions.npy"
            if args.skip_existing and preds_path.exists():
                print(f"\nSKIP {model_name}/{split}: predictions already exist")
                continue

            result = process_model(
                model_name=model_name,
                config_name=config_name,
                checkpoint_path=ckpt_path,
                device=device,
                root_dir=args.root_dir,
                output_base=args.output_dir,
                split=split,
            )
            if result:
                results[f"{model_name}/{split}"] = result

    print(f"\n{'='*60}")
    print(f"Completed processing {len(results)} model/split combinations")
    print(f"Outputs saved to: {args.output_dir}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
```

---

### `scripts/generate_comparison_figure.py`

**Purpose:** Contains `load_predictions` function.

```python
#!/usr/bin/env python3
"""
Generate comprehensive comparison figure:
- Ground truth row
- All models sorted by R² (best to worst)
- Metrics overlay on each subplot
- 3 images per row layout
"""

import json
import sys
from pathlib import Path

import numpy as np
import torch
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from models import build_model
from utils.misc import get_device


# Custom colormap: green (0) -> yellow -> red (1)
GREEN_TO_RED = LinearSegmentedColormap.from_list(
    "green_to_red",
    ["#00ff00", "#ffff00", "#ff0000"],
    N=256
)


def load_predictions(model_name, split="test"):
    """Load predictions and targets from outputs."""
    base = Path("outputs/experiments") / model_name / split
    preds = np.load(base / f"{split}_predictions.npy")
    targets = np.load(base / f"{split}_targets.npy")
    cities_path = base / f"{split}_cities.json"
    if cities_path.exists():
        with open(cities_path) as f:
            cities = json.load(f)
    else:
        cities = [f"img_{i}" for i in range(len(preds))]
    return preds, targets, cities


def get_model_metrics(model_name, metrics_dict):
    """Extract metrics string for overlay."""
    if model_name not in metrics_dict:
        return "N/A"
    m = metrics_dict[model_name]
    return f"MSE: {m.get('mse', 0):.4f}\nR²: {m.get('r2', 0):.4f}\nF1: {m.get('f1', 0):.4f}"


def generate_comparison_figure(
    models_data: dict,
    output_path: Path,
    split: str = "test",
    n_cols: int = 3,
    cmap=GREEN_TO_RED,
):
    """
    Generate comparison figure with ground truth + all models sorted by R².
    
    Args:
        models_data: dict of {model_name: {'preds': array, 'targets': array, 'cities': list, 'metrics': dict}}
        output_path: Path to save figure
        split: 'val' or 'test'
        n_cols: number of columns per row
    """
    # Sort models by R² descending (best first)
    def get_r2(model_name):
        m = models_data[model_name].get("metrics", {})
        return m.get("r2", -999)
    
    sorted_models = sorted(models_data.keys(), key=lambda m: get_r2(m), reverse=True)
    
    # All models should have same cities/order
    ref_cities = models_data[sorted_models[0]]["cities"]
    n_images = len(ref_cities)
    n_rows = int(np.ceil(n_images / n_cols))
    
    # Total rows: 1 for GT + N models
    total_rows = 1 + len(sorted_models)
    
    fig, axes = plt.subplots(
        total_rows, n_cols,
        figsize=(n_cols * 5, total_rows * 4.5)
    )
    
    if total_rows == 1:
        axes = axes.reshape(1, -1)
    if n_rows == 1:
        axes = axes.reshape(total_rows, n_cols)
    
    # First row: Ground Truth
    gt_model = sorted_models[0]
    targets = models_data[gt_model]["targets"]
    cities = models_data[gt_model]["cities"]
    
    for idx in range(n_images):
        row, col = 0, idx % n_cols
        ax = axes[row, col]
        im = ax.imshow(targets[idx].squeeze(), cmap=cmap, vmin=0, vmax=1)
        ax.set_title(f"Ground Truth: {cities[idx]}", fontsize=11, fontweight="bold")
        ax.axis("off")
    
    # Hide empty GT subplots
    for idx in range(n_images, n_rows * n_cols):
        row, col = 0, idx % n_cols
        axes[row, col].axis("off")
    
    # Subsequent rows: each model
    for model_idx, model_name in enumerate(sorted_models, start=1):
        row = model_idx
        preds = models_data[model_name]["preds"]
        metrics = models_data[model_name].get("metrics", {})
        
        for idx in range(n_images):
            col = idx % n_cols
            ax = axes[row, col]
            
            pred_img = preds[idx].squeeze()
            im = ax.imshow(pred_img, cmap=cmap, vmin=0, vmax=1)
            
            # Metrics overlay text
            r2 = metrics.get("r2", 0)
            mse = metrics.get("mse", 0)
            f1 = metrics.get("f1", 0)
            iou = metrics.get("iou", 0)
            
            metric_text = f"R²: {r2:.3f}\nMSE: {mse:.4f}\nF1: {f1:.3f}\nIoU: {iou:.3f}"
            ax.text(
                0.02, 0.98, metric_text,
                transform=ax.transAxes,
                fontsize=8,
                verticalalignment="top",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
            )
            
            ax.set_title(f"{model_name}: {ref_cities[idx]}", fontsize=10)
            ax.axis("off")
        
        # Hide empty subplots for this row
        for idx in range(n_images, n_rows * n_cols):
            col = idx % n_cols
            axes[row, col].axis("off")
    
    # Add colorbar
    cbar_ax = fig.add_axes([0.92, 0.15, 0.015, 0.7])
    fig.colorbar(im, cax=cbar_ax, label="Risk Probability")
    
    # Title
    fig.suptitle(f"GCM-HAIRNet Comparison — {split.upper()} Set (Sorted by R²)", fontsize=18, y=0.98)
    
    plt.tight_layout(rect=[0, 0, 0.9, 0.96])
    fig.savefig(output_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved comparison figure: {output_path}")


def generate_metrics_table_figure(models_data: dict, output_path: Path, split: str = "test"):
    """Generate a table figure summarizing all metrics."""
    sorted_models = sorted(
        models_data.keys(),
        key=lambda m: models_data[m].get("metrics", {}).get("r2", -999),
        reverse=True,
    )
    
    fig, ax = plt.subplots(figsize=(14, len(sorted_models) * 0.6 + 1))
    ax.axis("off")
    ax.axis("tight")
    
    table_data = []
    for model_name in sorted_models:
        m = models_data[model_name].get("metrics", {})
        table_data.append([
            model_name,
            f"{m.get('mse', 0):.6f}",
            f"{m.get('mae', 0):.6f}",
            f"{m.get('r2', 0):.6f}",
            f"{m.get('f1', 0):.6f}",
            f"{m.get('iou', 0):.6f}",
            f"{m.get('precision', 0):.6f}",
            f"{m.get('recall', 0):.6f}",
            f"{m.get('accuracy', 0):.6f}",
        ])
    
    columns = ["Model", "MSE", "MAE", "R²", "F1", "IoU", "Precision", "Recall", "Accuracy"]
    table = ax.table(
        cellText=table_data,
        colLabels=columns,
        cellLoc="center",
        loc="center",
        colWidths=[0.15] + [0.09] * 8,
    )
    
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2)
    
    # Color header
    for i in range(len(columns)):
        table[(0, i)].set_facecolor("#4472C4")
        table[(0, i)].set_text_props(color="white", fontweight="bold")
    
    # Color rows by R²
    for i, model_name in enumerate(sorted_models, start=1):
        r2 = models_data[model_name].get("metrics", {}).get("r2", 0)
        if r2 > 0.9:
            color = "#C6EFCE"  # green
        elif r2 > 0.7:
            color = "#FFEB9C"  # yellow
        elif r2 > 0.5:
            color = "#FFC7CE"  # light red
        else:
            color = "#FF0000"  # red
            table[(i, 0)].set_text_props(color="white")
        
        for j in range(len(columns)):
            table[(i, j)].set_facecolor(color)
    
    ax.set_title(f"GCM-HAIRNet Metrics Comparison — {split.upper()} Set", fontsize=14, pad=20)
    fig.savefig(output_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved metrics table: {output_path}")


def main():
    split = "test"
    
    # Load test metrics JSON
    metrics_path = Path("outputs/experiments/results/baseline_test_metrics.json")
    if not metrics_path.exists():
        print(f"Error: {metrics_path} not found. Run test evaluation first.")
        return
    
    with open(metrics_path) as f:
        baseline_metrics = json.load(f)
    
    # Also load fusion metrics from existing JSONs
    fusion_metrics = {}
    fusion_dir = Path("outputs/experiments/fusion")
    if fusion_dir.exists():
        for model_dir in fusion_dir.iterdir():
            if model_dir.is_dir():
                test_json = model_dir / "test_metrics.json"
                if test_json.exists():
                    with open(test_json) as f:
                        fusion_metrics[model_dir.name] = json.load(f)
    
    # Combine all models
    all_metrics = {**baseline_metrics, **fusion_metrics}
    
    # Load predictions for all valid models
    valid_models = [
        "image_only", "gis_only", "concat", "addition", "gated",
        "cross_attention", "multihead_cross_attention", "bilinear",
        "gcm", "vit", "swin", "graphsage", "mha", "nonlocal"
    ]
    
    models_data = {}
    for model_name in valid_models:
        try:
            preds, targets, cities = load_predictions(model_name, split)
            metrics = all_metrics.get(model_name, {})
            models_data[model_name] = {
                "preds": preds,
                "targets": targets,
                "cities": cities,
                "metrics": metrics,
            }
        except Exception as e:
            print(f"Skip {model_name}: {e}")
    
    print(f"\nLoaded {len(models_data)} models for comparison")
    
    # Generate outputs
    output_dir = Path("outputs/experiments/results")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    generate_comparison_figure(
        models_data,
        output_dir / f"comparison_{split}_sorted.png",
        split=split,
    )
    
    generate_metrics_table_figure(
        models_data,
        output_dir / f"metrics_table_{split}.png",
        split=split,
    )
    
    # Also generate val comparison
    val_models_data = {}
    for model_name in valid_models:
        try:
            preds, targets, cities = load_predictions(model_name, "val")
            metrics = all_metrics.get(model_name, {})
            val_models_data[model_name] = {
                "preds": preds,
                "targets": targets,
                "cities": cities,
                "metrics": metrics,
            }
        except Exception as e:
            print(f"Skip {model_name} val: {e}")
    
    if val_models_data:
        generate_comparison_figure(
            val_models_data,
            output_dir / "comparison_val_sorted.png",
            split="val",
        )
        generate_metrics_table_figure(
            val_models_data,
            output_dir / "metrics_table_val.png",
            split="val",
        )
    
    print(f"\nAll comparison figures saved to {output_dir}")


if __name__ == "__main__":
    main()
```

---

### `scripts/generate_final_results.py`

**Purpose:** Contains `find_best_checkpoint` function.

```python
import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from engine import Validator
from losses import build_loss
from metrics import Evaluator
from models import build_model
from utils.misc import get_device


EXPERIMENTS = [
    {"id": "image_only", "config": "baseline_image_only", "type": "fusion", "label": "Image-Only"},
    {"id": "gis_only", "config": "baseline_gis_only", "type": "fusion", "label": "GIS-Only"},
    {"id": "concat", "config": "baseline_concat", "type": "fusion", "label": "Concat"},
    {"id": "addition", "config": "baseline_addition", "type": "fusion", "label": "Addition"},
    {"id": "gated", "config": "baseline_gated", "type": "fusion", "label": "Gated"},
    {"id": "cross_attention", "config": "baseline_cross_attention", "type": "fusion", "label": "Cross-Attention"},
    {"id": "multihead_cross_attention", "config": "baseline_multihead_cross_attention", "type": "fusion", "label": "MultiHead-Cross-Attention"},
    {"id": "bilinear", "config": "baseline_bilinear", "type": "fusion", "label": "Bilinear"},
    {"id": "gcm", "config": "train", "type": "main", "label": "GCM-HAIRNet"},
    {"id": "improved_full", "config": "improved_full", "type": "main", "label": "Improved-Full"},
    {"id": "improved_small", "config": "improved_full_small", "type": "main", "label": "Improved-Small"},
    {"id": "tiny_cnn", "config": "baseline_tiny_cnn", "type": "baseline", "label": "TinyRiskCNN"},
    {"id": "baseline_gcm", "config": "baselines/baseline_gcm", "type": "baseline", "label": "Baseline-GCM"},
    {"id": "baseline_vit", "config": "baselines/baseline_vit", "type": "baseline", "label": "ViT"},
    {"id": "baseline_swin", "config": "baselines/baseline_swin", "type": "baseline", "label": "Swin"},
    {"id": "baseline_graphsage", "config": "baselines/baseline_graphsage", "type": "baseline", "label": "GraphSAGE"},
    {"id": "baseline_mha", "config": "baselines/baseline_mha", "type": "baseline", "label": "MHA"},
    {"id": "baseline_nonlocal", "config": "baselines/baseline_nonlocal", "type": "baseline", "label": "Non-Local"},
    {"id": "full_gcm", "config": "gcm_ablation/full_gcm", "type": "ablation", "label": "GCM-Full"},
    {"id": "no_distance", "config": "gcm_ablation/no_distance", "type": "ablation", "label": "GCM-NoDistance"},
    {"id": "no_similarity", "config": "gcm_ablation/no_similarity", "type": "ablation", "label": "GCM-NoSimilarity"},
    {"id": "no_road", "config": "gcm_ablation/no_road", "type": "ablation", "label": "GCM-NoRoad"},
    {"id": "no_urban", "config": "gcm_ablation/no_urban", "type": "ablation", "label": "GCM-NoUrban"},
    {"id": "no_learned", "config": "gcm_ablation/no_learned", "type": "ablation", "label": "GCM-NoLearned"},
    {"id": "no_scene_weights", "config": "gcm_ablation/no_scene_weights", "type": "ablation", "label": "GCM-NoSceneWeights"},
]


def find_best_checkpoint(config: Dict) -> Optional[Path]:
    ckpt_dir = Path(config.get("checkpoint", {}).get("dir", "./checkpoints"))
    if not ckpt_dir.exists():
        return None
    candidates = sorted(ckpt_dir.glob("best.pt"))
    if not candidates:
        candidates = sorted(ckpt_dir.glob("*.pt"))
    return candidates[0] if candidates else None


def extract_model_params(config: Dict) -> Dict[str, Any]:
    model_cfg = config.get("model", {})
    training_cfg = config.get("training", {})
    dataset_cfg = config.get("dataset", {})
    optimizer_cfg = training_cfg.get("optimizer", {})
    scheduler_cfg = training_cfg.get("scheduler", {})
    loss_cfg = training_cfg.get("loss", {})
    checkpoint_cfg = config.get("checkpoint", {})

    image_enc = model_cfg.get("image_encoder", {})
    gis_enc = model_cfg.get("gis_encoder", {})
    gct = model_cfg.get("gct", {})
    grm = model_cfg.get("grm", {})
    decoder = model_cfg.get("decoder", {})
    gcm = model_cfg.get("gcm", {})

    return {
        "model_name": model_cfg.get("name", "Unknown"),
        "image_encoder_type": image_enc.get("type", ""),
        "image_encoder_pretrained": image_enc.get("pretrained", False),
        "image_encoder_embed_dim": image_enc.get("embed_dim", ""),
        "image_encoder_depths": str(image_enc.get("depths", ""))[1:-1].replace(" ", ""),
        "image_encoder_num_heads": str(image_enc.get("num_heads", ""))[1:-1].replace(" ", ""),
        "image_encoder_window_size": image_enc.get("window_size", ""),
        "image_encoder_drop_path_rate": image_enc.get("drop_path_rate", ""),
        "gis_encoder_type": gis_enc.get("type", ""),
        "gis_encoder_input_channels": gis_enc.get("input_channels", ""),
        "gis_encoder_hidden_dim": gis_enc.get("hidden_dim", ""),
        "gis_encoder_output_dim": gis_enc.get("output_dim", ""),
        "gis_encoder_dropout": gis_enc.get("dropout", ""),
        "gct_type": gct.get("type", ""),
        "gct_hidden_dim": gct.get("hidden_dim", ""),
        "gct_num_heads": gct.get("num_heads", ""),
        "gct_dropout": gct.get("dropout", ""),
        "grm_type": grm.get("type", ""),
        "grm_hidden_dim": grm.get("hidden_dim", ""),
        "grm_num_relations": grm.get("num_relations", ""),
        "grm_num_layers": grm.get("num_layers", ""),
        "grm_dropout": grm.get("dropout", ""),
        "decoder_type": decoder.get("type", ""),
        "decoder_hidden_dim": decoder.get("hidden_dim", ""),
        "decoder_num_classes": decoder.get("num_classes", ""),
        "decoder_dropout": decoder.get("dropout", ""),
        "gcm_enable": gcm.get("enable", False),
        "gcm_embed_dim": gcm.get("embed_dim", ""),
        "gcm_num_heads": gcm.get("num_heads", ""),
        "gcm_num_blocks": gcm.get("num_blocks", ""),
        "gcm_num_semantic_heads": gcm.get("num_semantic_heads", ""),
        "gcm_mlp_ratio": gcm.get("mlp_ratio", ""),
        "gcm_dropout": gcm.get("dropout", ""),
        "gcm_gate_init": gcm.get("gate_init", ""),
        "gcm_sigma_distance": gcm.get("sigma_distance", ""),
        "gcm_scene_weight_hidden": gcm.get("scene_weight_hidden", ""),
        "gcm_gis_channels": gcm.get("gis_channels", ""),
        "gcm_gis_feature_dim": gcm.get("gis_feature_dim", ""),
        "gcm_grid_size": gcm.get("grid_size", ""),
        "gcm_enable_distance": gcm.get("enable_distance", ""),
        "gcm_enable_similarity": gcm.get("enable_similarity", ""),
        "gcm_enable_road": gcm.get("enable_road", ""),
        "gcm_enable_urban": gcm.get("enable_urban", ""),
        "gcm_enable_learned": gcm.get("enable_learned", ""),
        "gcm_enable_scene_weights": gcm.get("enable_scene_weights", ""),
        "fusion_type": model_cfg.get("fusion", {}).get("type", ""),
        "relation_module_type": model_cfg.get("relation_module", {}).get("type", ""),
        "epochs": training_cfg.get("epochs", ""),
        "optimizer_type": optimizer_cfg.get("type", ""),
        "learning_rate": optimizer_cfg.get("lr", ""),
        "weight_decay": optimizer_cfg.get("weight_decay", ""),
        "betas": str(optimizer_cfg.get("betas", ""))[1:-1].replace(" ", ""),
        "scheduler_type": scheduler_cfg.get("type", ""),
        "scheduler_T_max": scheduler_cfg.get("T_max", ""),
        "scheduler_eta_min": scheduler_cfg.get("eta_min", ""),
        "scheduler_warmup_epochs": scheduler_cfg.get("warmup_epochs", ""),
        "loss_type": loss_cfg.get("type", ""),
        "loss_mse_weight": loss_cfg.get("mse_weight", ""),
        "loss_l1_weight": loss_cfg.get("l1_weight", ""),
        "loss_focal_weight": loss_cfg.get("focal_weight", ""),
        "loss_focal_alpha": loss_cfg.get("focal_alpha", ""),
        "loss_focal_gamma": loss_cfg.get("focal_gamma", ""),
        "loss_huber_weight": loss_cfg.get("huber_weight", ""),
        "loss_huber_delta": loss_cfg.get("huber_delta", ""),
        "loss_ssim_weight": loss_cfg.get("ssim_weight", ""),
        "loss_ssim_window_size": loss_cfg.get("ssim_window_size", ""),
        "gradient_clip_val": training_cfg.get("gradient_clip_val", ""),
        "gradient_accumulation_steps": training_cfg.get("gradient_accumulation_steps", ""),
        "train_batch_size": dataset_cfg.get("train_batch_size", ""),
        "val_batch_size": dataset_cfg.get("val_batch_size", ""),
        "test_batch_size": dataset_cfg.get("test_batch_size", ""),
        "num_workers": dataset_cfg.get("num_workers", ""),
        "augmentation": dataset_cfg.get("augmentation", ""),
        "early_stopping_patience": training_cfg.get("early_stopping", {}).get("patience", ""),
        "early_stopping_monitor": training_cfg.get("early_stopping", {}).get("monitor", ""),
        "early_stopping_mode": training_cfg.get("early_stopping", {}).get("mode", ""),
        "checkpoint_dir": checkpoint_cfg.get("dir", ""),
        "checkpoint_save_top_k": checkpoint_cfg.get("save_top_k", ""),
        "checkpoint_every_n_epochs": checkpoint_cfg.get("every_n_epochs", ""),
        "seed": config.get("experiment", {}).get("seed", ""),
        "deterministic": config.get("experiment", {}).get("deterministic", ""),
    }


def run_validation(config: Dict, checkpoint_path: Path, device: torch.device) -> Dict[str, float]:
    val_dataset = GCMHAIRNetDataset(
        root_dir=config.get("data", {}).get("root_dir", "./data/processed"),
        split="val",
        transforms=get_val_transforms(),
    )
    val_loader = build_dataloader(
        val_dataset,
        batch_size=config.get("dataset", {}).get("val_batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    checkpoint = torch.load(checkpoint_path, map_location=device)
    ckpt_state = checkpoint.get("model_state_dict", checkpoint)
    model_state = model.state_dict()
    new_state = {}
    for key, param in ckpt_state.items():
        if key in model_state and param.shape == model_state[key].shape:
            new_state[key] = param
    model.load_state_dict(new_state, strict=False)
    model.to(device)
    model.eval()

    loss_fn = build_loss(config.get("training", {}).get("loss", {}))
    evaluator = Evaluator()

    all_preds = []
    all_targets = []
    total_loss = 0.0
    num_batches = 0

    with torch.no_grad():
        for batch in val_loader:
            image = batch["image"].to(device)
            gis = batch["gis"].to(device)
            label = batch["label"].to(device)
            preds = model(image, gis)
            loss = loss_fn(preds, label)
            total_loss += loss.item()
            num_batches += 1
            preds_prob = torch.sigmoid(preds)
            all_preds.append(preds_prob.cpu().numpy())
            all_targets.append(label.cpu().numpy())

    preds_all = np.concatenate(all_preds, axis=0)
    targets_all = np.concatenate(all_targets, axis=0)
    metrics = evaluator(preds_all, targets_all)
    metrics["val_loss"] = total_loss / max(num_batches, 1)
    return metrics


def count_parameters(model: torch.nn.Module) -> Dict[str, int]:
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    return {"total_params": total, "trainable_params": trainable}


def main():
    parser = argparse.ArgumentParser(description="Generate final research-paper results CSV")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--device", type=str, default=None, help="Device to use")
    parser.add_argument("--output", type=str, default="./outputs/final_results.csv", help="Output CSV path")
    parser.add_argument("--skip-val", action="store_true", help="Skip validation, use existing metrics only")
    args = parser.parse_args()

    device = get_device(args.device)
    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "experiment_id", "experiment_type", "label",
        "model_name",
        "image_encoder_type", "image_encoder_pretrained", "image_encoder_embed_dim",
        "image_encoder_depths", "image_encoder_num_heads", "image_encoder_window_size", "image_encoder_drop_path_rate",
        "gis_encoder_type", "gis_encoder_input_channels", "gis_encoder_hidden_dim", "gis_encoder_output_dim", "gis_encoder_dropout",
        "gct_type", "gct_hidden_dim", "gct_num_heads", "gct_dropout",
        "grm_type", "grm_hidden_dim", "grm_num_relations", "grm_num_layers", "grm_dropout",
        "decoder_type", "decoder_hidden_dim", "decoder_num_classes", "decoder_dropout",
        "gcm_enable", "gcm_embed_dim", "gcm_num_heads", "gcm_num_blocks", "gcm_num_semantic_heads",
        "gcm_mlp_ratio", "gcm_dropout", "gcm_gate_init", "gcm_sigma_distance", "gcm_scene_weight_hidden",
        "gcm_gis_channels", "gcm_gis_feature_dim", "gcm_grid_size",
        "gcm_enable_distance", "gcm_enable_similarity", "gcm_enable_road", "gcm_enable_urban",
        "gcm_enable_learned", "gcm_enable_scene_weights",
        "fusion_type", "relation_module_type",
        "epochs", "optimizer_type", "learning_rate", "weight_decay", "betas",
        "scheduler_type", "scheduler_T_max", "scheduler_eta_min", "scheduler_warmup_epochs",
        "loss_type", "loss_mse_weight", "loss_l1_weight", "loss_focal_weight",
        "loss_focal_alpha", "loss_focal_gamma", "loss_huber_weight", "loss_huber_delta",
        "loss_ssim_weight", "loss_ssim_window_size",
        "gradient_clip_val", "gradient_accumulation_steps",
        "train_batch_size", "val_batch_size", "test_batch_size", "num_workers", "augmentation",
        "early_stopping_patience", "early_stopping_monitor", "early_stopping_mode",
        "checkpoint_dir", "checkpoint_save_top_k", "checkpoint_every_n_epochs",
        "seed", "deterministic",
        "total_params", "trainable_params",
        "val_loss", "val_mse", "val_mae", "val_r2", "val_accuracy", "val_f1", "val_precision", "val_recall", "val_iou",
        "test_loss", "test_mse", "test_mae", "test_r2", "test_accuracy", "test_f1", "test_precision", "test_recall", "test_iou",
        "checkpoint_path",
    ]

    rows = []

    for exp in EXPERIMENTS:
        exp_id = exp["id"]
        config_name = exp["config"]
        print(f"\n{'='*60}")
        print(f"Processing: {exp['label']} ({config_name})")
        print(f"{'='*60}")

        try:
            config = config_manager.load(config_name)
        except Exception as e:
            print(f"  Failed to load config: {e}")
            continue

        best_path = find_best_checkpoint(config)
        if best_path is None:
            print(f"  No checkpoint found, skipping.")
            continue

        print(f"  Checkpoint: {best_path}")

        row = extract_model_params(config)
        row["experiment_id"] = exp_id
        row["experiment_type"] = exp["type"]
        row["label"] = exp["label"]
        row["checkpoint_path"] = str(best_path)

        try:
            model = build_model(config.get("model", {}))
            param_info = count_parameters(model)
            row["total_params"] = param_info["total_params"]
            row["trainable_params"] = param_info["trainable_params"]
            print(f"  Parameters: {param_info['total_params']:,}")
        except Exception as e:
            print(f"  Failed to build model for param count: {e}")
            row["total_params"] = ""
            row["trainable_params"] = ""

        val_metrics = {}
        test_metrics = {}
        if not args.skip_val:
            try:
                val_metrics = run_validation(config, best_path, device)
                row.update({
                    "val_loss": round(val_metrics.get("val_loss", val_metrics.get("loss", "")), 6),
                    "val_mse": round(val_metrics.get("mse", ""), 6),
                    "val_mae": round(val_metrics.get("mae", ""), 6),
                    "val_r2": round(val_metrics.get("r2", ""), 6),
                    "val_accuracy": round(val_metrics.get("accuracy", ""), 6),
                    "val_f1": round(val_metrics.get("f1", ""), 6),
                    "val_precision": round(val_metrics.get("precision", ""), 6),
                    "val_recall": round(val_metrics.get("recall", ""), 6),
                    "val_iou": round(val_metrics.get("iou", ""), 6),
                })
                print(f"  Val: MSE={val_metrics.get('mse', 'N/A'):.6f}, R2={val_metrics.get('r2', 'N/A'):.6f}")
            except Exception as e:
                print(f"  Validation failed: {e}")

            try:
                test_dataset = GCMHAIRNetDataset(
                    root_dir=config.get("data", {}).get("root_dir", "./data/processed"),
                    split="test",
                    transforms=get_val_transforms(),
                )
                test_loader = build_dataloader(
                    test_dataset,
                    batch_size=config.get("dataset", {}).get("test_batch_size", 32),
                    shuffle=False,
                    num_workers=0,
                    pin_memory=(device.type == "cuda"),
                    drop_last=False,
                )
                model = build_model(config.get("model", {}))
                checkpoint = torch.load(best_path, map_location=device)
                ckpt_state = checkpoint.get("model_state_dict", checkpoint)
                model_state = model.state_dict()
                new_state = {}
                for key, param in ckpt_state.items():
                    if key in model_state and param.shape == model_state[key].shape:
                        new_state[key] = param
                model.load_state_dict(new_state, strict=False)
                model.to(device)
                model.eval()

                loss_fn = build_loss(config.get("training", {}).get("loss", {}))
                evaluator = Evaluator()
                all_preds, all_targets = [], []
                total_loss, num_batches = 0.0, 0

                with torch.no_grad():
                    for batch in test_loader:
                        image = batch["image"].to(device)
                        gis = batch["gis"].to(device)
                        label = batch["label"].to(device)
                        preds = model(image, gis)
                        loss = loss_fn(preds, label)
                        total_loss += loss.item()
                        num_batches += 1
                        preds_prob = torch.sigmoid(preds)
                        all_preds.append(preds_prob.cpu().numpy())
                        all_targets.append(label.cpu().numpy())

                preds_all = np.concatenate(all_preds, axis=0)
                targets_all = np.concatenate(all_targets, axis=0)
                test_metrics = evaluator(preds_all, targets_all)
                test_metrics["loss"] = total_loss / max(num_batches, 1)

                row.update({
                    "test_loss": round(test_metrics.get("loss", ""), 6),
                    "test_mse": round(test_metrics.get("mse", ""), 6),
                    "test_mae": round(test_metrics.get("mae", ""), 6),
                    "test_r2": round(test_metrics.get("r2", ""), 6),
                    "test_accuracy": round(test_metrics.get("accuracy", ""), 6),
                    "test_f1": round(test_metrics.get("f1", ""), 6),
                    "test_precision": round(test_metrics.get("precision", ""), 6),
                    "test_recall": round(test_metrics.get("recall", ""), 6),
                    "test_iou": round(test_metrics.get("iou", ""), 6),
                })
                print(f"  Test: MSE={test_metrics.get('mse', 'N/A'):.6f}, R2={test_metrics.get('r2', 'N/A'):.6f}")
            except Exception as e:
                print(f"  Test failed: {e}")

        rows.append(row)

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n{'='*60}")
    print(f"Final results saved to: {output_path}")
    print(f"Total experiments: {len(rows)}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
```

---

### `scripts/generate_paper_figures.py`

**Purpose:** Contains `load_city_predictions` function.

```python
#!/usr/bin/env python3
"""
Generate publication-quality side-by-side comparison figures.
Layout: models in a grid (left to right, worst → best)
        Ground Truth centered on the right side spanning all rows
"""

import json
import sys
from pathlib import Path
import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.gridspec import GridSpec

# Publication-ready style
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica', 'Liberation Sans'],
    'font.size': 11,
    'axes.titlesize': 12,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.spines.left': False,
    'axes.spines.bottom': False,
    'xtick.major.size': 0,
    'ytick.major.size': 0,
    'axes.linewidth': 0.5,
    'axes.edgecolor': '#cccccc',
})

# Custom hazard colormap: safe green → caution yellow → danger red
HAZARD_COLORS = LinearSegmentedColormap.from_list(
    "hazard_risk",
    [
        "#1a9850",
        "#91cf60",
        "#d9ef8b",
        "#fee08b",
        "#fc8d59",
        "#d73027",
        "#b2182b",
    ],
    N=256
)


def load_city_predictions(model_name, city_name, split="test"):
    """Load predictions and targets for a specific city."""
    base = Path("/Users/reyyishreyas/Desktop/gcmh/outputs/experiments") / model_name / split
    
    preds = np.load(base / f"{split}_predictions.npy")
    targets = np.load(base / f"{split}_targets.npy")
    
    cities_path = base / f"{split}_cities.json"
    if cities_path.exists():
        with open(cities_path) as f:
            cities = json.load(f)
    else:
        cities = [f"City {i+1}" for i in range(len(preds))]
    
    try:
        city_idx = cities.index(city_name)
    except ValueError:
        print(f"City '{city_name}' not found in {model_name}. Available: {cities}")
        return None, None, None
    
    return preds[city_idx], targets[city_idx], city_name


def create_side_by_side_figure(models_data, title, output_path, city_name,
                                cmap=HAZARD_COLORS):
    """
    Create a side-by-side comparison figure.
    
    Layout: models in a grid (left to right, worst → best)
            Ground Truth centered on the right side spanning all rows
    """
    n_models = len(models_data)
    
    # Determine grid dimensions: aim for 3 columns, calculate rows
    n_cols_models = 3
    n_rows = math.ceil(n_models / n_cols_models)
    n_cols = n_cols_models + 1  # +1 for GT column
    
    # Figure dimensions
    fig_width = 16
    fig_height = 3.5 * n_rows
    
    fig = plt.figure(figsize=(fig_width, fig_height))
    
    # Use GridSpec for custom layout
    gs = GridSpec(n_rows, n_cols, figure=fig,
                  width_ratios=[1, 1, 1, 0.85],
                  height_ratios=[1] * n_rows,
                  hspace=0.4, wspace=0.2)
    
    targets = models_data[0]['targets']
    vmin, vmax = 0, 1
    
    # Plot models in columns 0-2
    for idx, model_info in enumerate(models_data):
        row = idx // n_cols_models
        col = idx % n_cols_models
        
        ax = fig.add_subplot(gs[row, col])
        preds = model_info['preds']
        r2 = model_info.get('r2', 0)
        mse = model_info.get('mse', 0)
        name = model_info['name']
        
        pred_img = preds.squeeze()
        im = ax.imshow(pred_img, cmap=cmap, vmin=vmin, vmax=vmax, aspect='equal')
        
        # Metrics overlay with clean styling
        metric_text = f"R² = {r2:.3f}\nMSE = {mse:.4f}"
        ax.text(
            0.02, 0.98, metric_text,
            transform=ax.transAxes,
            fontsize=9,
            verticalalignment='top',
            horizontalalignment='left',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='white', alpha=0.92,
                     edgecolor='#dddddd', linewidth=0.5),
            color='#222222',
            family='monospace'
        )
        
        ax.set_title(name, fontsize=10, fontweight='bold', color='#333333', pad=8)
        ax.axis('off')
    
    # Plot Ground Truth in column 3, spanning all rows
    ax_gt = fig.add_subplot(gs[:, n_cols_models])
    gt_img = targets.squeeze()
    im_gt = ax_gt.imshow(gt_img, cmap=cmap, vmin=vmin, vmax=vmax, aspect='equal')
    ax_gt.set_title(f"Ground Truth\n{city_name}", fontsize=11, fontweight='bold',
                    color='#222222', pad=10)
    ax_gt.axis('off')
    
    # Add a subtle border around GT
    for spine in ax_gt.spines.values():
        spine.set_visible(True)
        spine.set_edgecolor('#333333')
        spine.set_linewidth(1.5)
    
    # Add colorbar on the far right
    cbar_ax = fig.add_axes([0.95, 0.15, 0.008, 0.7])
    cbar = fig.colorbar(im_gt, cax=cbar_ax)
    cbar.set_label("Hazard Risk Probability", fontsize=10, rotation=90, labelpad=12)
    cbar.ax.tick_params(labelsize=9)
    cbar.set_ticks([0, 0.25, 0.5, 0.75, 1.0])
    cbar.set_ticklabels(['0.0', '0.25', '0.50', '0.75', '1.0'])
    
    # Main title
    fig.suptitle(title, fontsize=14, fontweight='bold', y=0.98, color='#222222')
    
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.25)
    plt.close(fig)
    print(f"Saved: {output_path}")


def main():
    output_dir = Path("/Users/reyyishreyas/Desktop/gcmh/outputs/experiments/results")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    city_name = "Jammu"
    
    baseline_metrics = {
        'gcm':        {'r2': 0.809871793, 'mse': 0.013963833},
        'vit':        {'r2': 0.702091634, 'mse': 0.021879669},
        'swin':       {'r2': 0.614501834, 'mse': 0.028312642},
        'graphsage':  {'r2': 0.526168000, 'mse': 0.034800000},
        'mha':        {'r2': 0.621401000, 'mse': 0.027806000},
        'nonlocal':   {'r2': 0.709930000, 'mse': 0.021304000},
    }
    
    fusion_metrics = {
        'addition':               {'r2': 0.9538082, 'mse': 0.0033925227},
        'bilinear':               {'r2': 0.94440895, 'mse': 0.0040828465},
        'concat':                 {'r2': 0.80251503, 'mse': 0.014504145},
        'gated':                  {'r2': 0.68688214, 'mse': 0.022996724},
        'cross_attention':        {'r2': 0.64848423, 'mse': 0.025816828},
        'multihead_cross_attention': {'r2': 0.62923914, 'mse': 0.027230268},
        'gis_only':               {'r2': 0.70133114, 'mse': 0.021935526},
        'image_only':             {'r2': 0.62713635, 'mse': 0.02738471},
    }
    
    # Load baseline data (sorted worst → best)
    baseline_order = ['graphsage', 'swin', 'mha', 'vit', 'nonlocal', 'gcm']
    baseline_data = []
    for name in baseline_order:
        preds, targets, _ = load_city_predictions(name, city_name, "test")
        if preds is None:
            continue
        m = baseline_metrics[name]
        baseline_data.append({
            'name': name.replace('_', '-').title(),
            'preds': preds,
            'targets': targets,
            'r2': m['r2'],
            'mse': m['mse'],
        })
    
    # Load fusion data (sorted worst → best)
    fusion_order = ['image_only', 'multihead_cross_attention', 'cross_attention',
                    'gated', 'gis_only', 'concat', 'bilinear', 'addition']
    fusion_data = []
    for name in fusion_order:
        preds, targets, _ = load_city_predictions(name, city_name, "test")
        if preds is None:
            continue
        m = fusion_metrics[name]
        fusion_data.append({
            'name': name.replace('_', '-').title(),
            'preds': preds,
            'targets': targets,
            'r2': m['r2'],
            'mse': m['mse'],
        })
    
    # Create figures
    create_side_by_side_figure(
        baseline_data,
        f"Baseline Models — {city_name} (Test Set, Sorted by R²)",
        output_dir / "baseline_city_comparison.png",
        city_name=city_name
    )
    
    create_side_by_side_figure(
        fusion_data,
        f"Fusion Techniques — {city_name} (Test Set, Sorted by R²)",
        output_dir / "fusion_city_comparison.png",
        city_name=city_name
    )
    
    print(f"\nDone! Generated side-by-side figures for {city_name}.")


if __name__ == "__main__":
    main()
```

---

### `scripts/generate_per_city_comparison.py`

**Purpose:** Contains `load_predictions` function.

```python
#!/usr/bin/env python3
"""
Generate per-city comparison figures:
- Ground truth row
- All models sorted by R²
- 3 cities per row layout
- Consistent green-to-red colormap (0=green, 1=red)
- Separate figures for fusion, baselines, and ablations
"""

import json
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Custom colormap: green (0) -> yellow -> red (1)
GREEN_TO_RED = LinearSegmentedColormap.from_list(
    "green_to_red",
    ["#00ff00", "#ffff00", "#ff0000"],
    N=256
)


def load_predictions(model_name, split="test"):
    """Load predictions and targets from outputs."""
    base = Path("outputs/experiments") / model_name / split
    preds = np.load(base / f"{split}_predictions.npy")
    targets = np.load(base / f"{split}_targets.npy")
    cities_path = base / f"{split}_cities.json"
    if cities_path.exists():
        with open(cities_path) as f:
            cities = json.load(f)
    else:
        cities = [f"img_{i}" for i in range(len(preds))]
    return preds, targets, cities


def get_metrics(model_name, all_metrics):
    """Get metrics dict for a model."""
    # Check baseline test metrics first
    if model_name in all_metrics.get("baselines", {}):
        return all_metrics["baselines"][model_name]
    # Check fusion metrics
    if model_name in all_metrics.get("fusion", {}):
        return all_metrics["fusion"][model_name]
    # Check ablation metrics
    if model_name in all_metrics.get("ablations", {}):
        return all_metrics["ablations"][model_name]
    return {}


def generate_per_city_comparison(
    models: list,
    split: str = "test",
    output_path: Path = None,
    title: str = "",
    all_metrics: dict = None,
    n_cols: int = 3,
):
    """
    Generate comparison figure with:
    - Row 0: Ground Truth for cities 0,1,2,...
    - Row 1..N: Each model's predictions for same cities
    
    All subplots share vmin=0, vmax=1.
    """
    if all_metrics is None:
        all_metrics = {}
    
    # Load data for all models
    models_data = {}
    for m in models:
        try:
            preds, targets, cities = load_predictions(m, split)
            metrics = get_metrics(m, all_metrics)
            models_data[m] = {
                "preds": preds,
                "targets": targets,
                "cities": cities,
                "metrics": metrics,
            }
        except Exception as e:
            print(f"  Skip {m}: {e}")
    
    if not models_data:
        print(f"  No models loaded for {title}")
        return
    
    # Sort models by R² descending
    def get_r2(m):
        return models_data[m].get("metrics", {}).get("r2", -999)
    
    sorted_models = sorted(models_data.keys(), key=lambda m: get_r2(m), reverse=True)
    
    # Use first model's cities as reference
    ref_cities = models_data[sorted_models[0]]["cities"]
    n_images = len(ref_cities)
    n_rows = int(np.ceil(n_images / n_cols))
    
    # Total rows: 1 GT + N models
    total_rows = 1 + len(sorted_models)
    
    fig, axes = plt.subplots(
        total_rows, n_cols,
        figsize=(n_cols * 5, total_rows * 4.5)
    )
    
    if total_rows == 1:
        axes = axes.reshape(1, -1)
    if n_rows == 1:
        axes = axes.reshape(total_rows, n_cols)
    
    targets = models_data[sorted_models[0]]["targets"]
    
    # Row 0: Ground Truth
    for idx in range(n_images):
        row, col = 0, idx % n_cols
        ax = axes[row, col]
        im = ax.imshow(targets[idx].squeeze(), cmap=GREEN_TO_RED, vmin=0, vmax=1)
        ax.set_title(f"Ground Truth: {ref_cities[idx]}", fontsize=11, fontweight="bold")
        ax.axis("off")
    
    # Hide empty GT subplots
    for idx in range(n_images, n_rows * n_cols):
        row, col = 0, idx % n_cols
        axes[row, col].axis("off")
    
    # Subsequent rows: each model
    for model_idx, model_name in enumerate(sorted_models, start=1):
        row = model_idx
        preds = models_data[model_name]["preds"]
        metrics = models_data[model_name].get("metrics", {})
        
        for idx in range(n_images):
            col = idx % n_cols
            ax = axes[row, col]
            
            pred_img = preds[idx].squeeze()
            im = ax.imshow(pred_img, cmap=GREEN_TO_RED, vmin=0, vmax=1)
            
            # Metrics overlay
            r2 = metrics.get("r2", 0)
            mse = metrics.get("mse", 0)
            f1 = metrics.get("f1", 0)
            iou = metrics.get("iou", 0)
            
            metric_text = f"R²: {r2:.3f}  MSE: {mse:.4f}\nF1: {f1:.3f}  IoU: {iou:.3f}"
            ax.text(
                0.02, 0.98, metric_text,
                transform=ax.transAxes,
                fontsize=8,
                verticalalignment="top",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.85),
            )
            
            ax.set_title(f"{model_name}: {ref_cities[idx]}", fontsize=10)
            ax.axis("off")
        
        # Hide empty subplots
        for idx in range(n_images, n_rows * n_cols):
            col = idx % n_cols
            axes[row, col].axis("off")
    
    # Colorbar
    cbar_ax = fig.add_axes([0.92, 0.15, 0.015, 0.7])
    fig.colorbar(im, cax=cbar_ax, label="Risk Probability")
    
    fig.suptitle(f"{title} — {split.upper()} Set (Sorted by R²)", fontsize=18, y=0.98)
    
    plt.tight_layout(rect=[0, 0, 0.9, 0.96])
    fig.savefig(output_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Saved: {output_path}")


def main():
    split = "test"
    
    # Load all metrics
    all_metrics = {"baselines": {}, "fusion": {}, "ablations": {}}
    
    # Load baseline test metrics
    baseline_metrics_path = Path("outputs/experiments/results/baseline_test_metrics.json")
    if baseline_metrics_path.exists():
        with open(baseline_metrics_path) as f:
            all_metrics["baselines"] = json.load(f)
    
    # Load fusion metrics
    fusion_dir = Path("outputs/experiments/fusion")
    if fusion_dir.exists():
        for model_dir in fusion_dir.iterdir():
            if model_dir.is_dir():
                test_json = model_dir / "test_metrics.json"
                if test_json.exists():
                    with open(test_json) as f:
                        all_metrics["fusion"][model_dir.name] = json.load(f)
    
    # Load ablation metrics
    ablation_dir = Path("outputs/experiments/ablation")
    if ablation_dir.exists():
        for model_dir in ablation_dir.iterdir():
            if model_dir.is_dir():
                test_json = model_dir / "test_metrics.json"
                if test_json.exists():
                    with open(test_json) as f:
                        all_metrics["ablations"][model_dir.name] = json.load(f)
    
    output_dir = Path("outputs/experiments/results")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Fusion comparison (8 models + GT)
    fusion_models = [
        "addition", "bilinear", "concat", "gated",
        "cross_attention", "multihead_cross_attention",
        "image_only", "gis_only"
    ]
    print(f"\nGenerating fusion comparison ({len(fusion_models)} models)...")
    generate_per_city_comparison(
        models=fusion_models,
        split=split,
        output_path=output_dir / f"fusion_comparison_{split}.png",
        title="Fusion Study Comparison",
        all_metrics=all_metrics,
    )
    
    # 2. Baseline comparison (7 valid models + GT)
    baseline_models = ["gcm", "vit", "swin", "graphsage", "mha", "nonlocal"]
    print(f"\nGenerating baseline comparison ({len(baseline_models)} models)...")
    generate_per_city_comparison(
        models=baseline_models,
        split=split,
        output_path=output_dir / f"baseline_comparison_{split}.png",
        title="Controlled Baselines Comparison",
        all_metrics=all_metrics,
    )
    
    # 3. Ablation comparison (9 variants + GT)
    ablation_models = [
        "full", "no_distance", "no_similarity", "no_road", "no_urban",
        "no_learned", "no_scene_weights", "no_gcm", "no_gct", "no_gct_no_gcm",
    ]
    print(f"\nGenerating ablation comparison ({len(ablation_models)} models)...")
    generate_per_city_comparison(
        models=ablation_models,
        split=split,
        output_path=output_dir / f"ablation_comparison_{split}.png",
        title="GCM Ablation Comparison",
        all_metrics=all_metrics,
    )
    
    # 4. All models together (15 valid + GT)
    all_models = fusion_models + baseline_models
    print(f"\nGenerating full comparison ({len(all_models)} models)...")
    generate_per_city_comparison(
        models=all_models,
        split=split,
        output_path=output_dir / f"full_comparison_{split}.png",
        title="All Valid Models Comparison",
        all_metrics=all_metrics,
    )
    
    # Generate val versions too
    for split in ["val", "test"]:
        print(f"\n--- {split.upper()} ---")
        
        fusion_models = [
            "addition", "bilinear", "concat", "gated",
            "cross_attention", "multihead_cross_attention",
            "image_only", "gis_only"
        ]
        generate_per_city_comparison(
            models=fusion_models,
            split=split,
            output_path=output_dir / f"fusion_comparison_{split}.png",
            title=f"Fusion Study Comparison",
            all_metrics=all_metrics,
        )
        
        baseline_models = ["gcm", "vit", "swin", "graphsage", "mha", "nonlocal"]
        generate_per_city_comparison(
            models=baseline_models,
            split=split,
            output_path=output_dir / f"baseline_comparison_{split}.png",
            title=f"Controlled Baselines Comparison",
            all_metrics=all_metrics,
        )
        
        ablation_models = [
            "full", "no_distance", "no_similarity", "no_road", "no_urban",
            "no_learned", "no_scene_weights", "no_gcm", "no_gct", "no_gct_no_gcm",
        ]
        generate_per_city_comparison(
            models=ablation_models,
            split=split,
            output_path=output_dir / f"ablation_comparison_{split}.png",
            title=f"GCM Ablation Comparison",
            all_metrics=all_metrics,
        )
        
        all_models = fusion_models + baseline_models
        generate_per_city_comparison(
            models=all_models,
            split=split,
            output_path=output_dir / f"full_comparison_{split}.png",
            title=f"All Valid Models Comparison",
            all_metrics=all_metrics,
        )
    
    print(f"\nAll comparison figures saved to {output_dir}")


if __name__ == "__main__":
    main()
```

---

### `scripts/generate_repo_md.py`

**Purpose:** Regenerate REPOSITORY_CODE.md from actual source files.

```python
#!/usr/bin/env python3
"""Regenerate REPOSITORY_CODE.md from actual source files."""

import os
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
MD_FILE = REPO_ROOT / "REPOSITORY_CODE.md"

EXCLUDE_DIRS = {
    ".git", "__pycache__", "venv", ".pytest_cache",
    "gcm_hairnet.egg-info", "node_modules",
}

def extract_purpose(content: str, filename: str) -> str:
    """Extract a purpose description from file content."""
    lines = content.split("\n")
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("class "):
            class_name = stripped.split("(")[0].replace("class ", "").strip()
            return f"Defines `{class_name}` module/class."
        if stripped.startswith("def "):
            func_name = stripped.split("(")[0].replace("def ", "").strip()
            return f"Contains `{func_name}` function."
        if stripped.startswith('"""') or stripped.startswith("'''"):
            docstring = stripped.strip('"""').strip("'''").strip()
            if docstring:
                return docstring.split("\n")[0][:100]
    return f"Implementation of `{filename}`."

def generate_md() -> str:
    md_parts = []
    md_parts.append("# GCM-HAIRNet Repository Code\n")
    md_parts.append("Complete repository source code organized by module, with file descriptions and full implementations.\n")
    md_parts.append("---\n")

    py_files = sorted(REPO_ROOT.rglob("*.py"))

    for py_file in py_files:
        rel_path = py_file.relative_to(REPO_ROOT)
        parts = rel_path.parts

        if any(excl in parts for excl in EXCLUDE_DIRS):
            continue

        content = py_file.read_text(encoding="utf-8")
        purpose = extract_purpose(content, rel_path.name)

        md_parts.append(f"### `{rel_path}`\n")
        md_parts.append(f"**Purpose:** {purpose}\n")
        md_parts.append("```python")
        md_parts.append(content.rstrip())
        md_parts.append("```\n")
        md_parts.append("---\n")

    return "\n".join(md_parts)

if __name__ == "__main__":
    md_content = generate_md()
    MD_FILE.write_text(md_content, encoding="utf-8")
    print(f"Generated {MD_FILE} with content from {len(md_content.split('### `')) - 1} files.")
```

---

### `scripts/generate_risk_maps.py`

**Purpose:** Contains `run_inference_for_split` function.

```python
import argparse
from pathlib import Path
import sys
import torch
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from models import build_model
from utils.misc import get_device
from visualization import save_risk_maps, save_comparison_maps


def run_inference_for_split(split, config, device, checkpoint_path, output_base, root_dir):
    dataset = GCMHAIRNetDataset(
        root_dir=root_dir,
        split=split,
        transforms=get_val_transforms(),
    )
    loader = build_dataloader(
        dataset,
        batch_size=config.get("inference", {}).get("batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    checkpoint = torch.load(checkpoint_path, map_location=device)
    ckpt_state = checkpoint["model_state_dict"]
    model_state = model.state_dict()
    new_state = {}
    for key, param in ckpt_state.items():
        if key in model_state and param.shape == model_state[key].shape:
            new_state[key] = param
    model.load_state_dict(new_state, strict=False)
    model.to(device)
    model.eval()

    all_preds = []
    all_targets = []
    all_cities = []

    with torch.no_grad():
        for batch in loader:
            image = batch["image"].to(device, non_blocking=True)
            gis = batch["gis"].to(device, non_blocking=True)
            label = batch["label"].to(device, non_blocking=True)

            preds = torch.sigmoid(model(image, gis)).cpu().numpy()
            all_preds.append(preds)
            all_targets.append(label.cpu().numpy())
            all_cities.extend(batch.get("city_name", []))

    preds = np.concatenate(all_preds, axis=0)
    targets = np.concatenate(all_targets, axis=0)

    out_dir = Path(output_base) / split
    out_dir.mkdir(parents=True, exist_ok=True)

    np.save(out_dir / f"{split}_predictions.npy", preds)
    np.save(out_dir / f"{split}_targets.npy", targets)

    save_risk_maps(preds, all_cities, str(out_dir), cmap="hot")
    save_comparison_maps(preds, targets, all_cities, str(out_dir))

    print(f"[{split}] Saved {len(all_cities)} risk maps and comparisons to {out_dir}")


def main():
    parser = argparse.ArgumentParser(description="Generate risk maps for all cities")
    parser.add_argument("--config", type=str, default="inference", help="Config name")
    parser.add_argument("--checkpoint", type=str, required=True, help="Checkpoint path")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--output-dir", type=str, default="./outputs/all_risk_maps", help="Output directory")
    parser.add_argument("--splits", nargs="+", default=["train", "val", "test"], help="Splits to process")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)
    device = get_device(args.device)

    for split in args.splits:
        try:
            run_inference_for_split(split, config, device, args.checkpoint, args.output_dir, args.root_dir)
        except Exception as e:
            print(f"Error processing split {split}: {e}")


if __name__ == "__main__":
    main()
```

---

### `scripts/inference.py`

**Purpose:** Contains `main` function.

```python
import argparse
import sys
from pathlib import Path
from typing import Optional

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from engine import Inferencer
from models import build_model
from utils.misc import get_device


def main():
    parser = argparse.ArgumentParser(description="Run inference with GCM-HAIRNet")
    parser.add_argument("--config", type=str, default="inference", help="Config name")
    parser.add_argument("--checkpoint", type=str, required=True, help="Checkpoint path")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--split", type=str, default="test", help="Data split to use")
    parser.add_argument("--device", type=str, default=None, help="Device")
    parser.add_argument("--output-dir", type=str, default="./outputs/inference", help="Output directory")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)
    device = get_device(args.device)

    dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
        split=args.split,
        transforms=get_val_transforms(),
    )
    data_loader = build_dataloader(
        dataset,
        batch_size=config.get("inference", {}).get("batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    inferencer = Inferencer(
        model=model,
        data_loader=data_loader,
        checkpoint_path=args.checkpoint,
        device=device,
        output_dir=args.output_dir,
        save_predictions=config.get("inference", {}).get("save_predictions", True),
        save_visualizations=config.get("inference", {}).get("save_visualizations", True),
    )

    results = inferencer.run()
    print(f"Predictions saved to {args.output_dir}")
    print(f"Shape: {results['predictions'].shape}")


if __name__ == "__main__":
    main()
```

---

### `scripts/run_baseline_study.py`

**Purpose:** Contains `_make_json_serializable` function.

```python
import argparse
import csv
import json
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms, get_train_transforms
from engine import Tester, Trainer, Validator
from losses import build_loss
from metrics import Evaluator
from models import build_model
from utils.misc import get_device


BASELINE_EXPERIMENTS = [
    {"id": "gcm", "config": "baselines/baseline_gcm", "label": "GCM-HAIRNet"},
    {"id": "vit", "config": "baselines/baseline_vit", "label": "ViT"},
    {"id": "swin", "config": "baselines/baseline_swin", "label": "Swin"},
    {"id": "graphsage", "config": "baselines/baseline_graphsage", "label": "GraphSAGE"},
    {"id": "mha", "config": "baselines/baseline_mha", "label": "MHA"},
    {"id": "nonlocal", "config": "baselines/baseline_nonlocal", "label": "Non-Local"},
]

BASELINE_CONFIG_FILES = {
    "gcm": "baseline_gcm",
    "vit": "baseline_vit",
    "swin": "baseline_swin",
    "graphsage": "baseline_graphsage",
    "mha": "baseline_mha",
    "nonlocal": "baseline_nonlocal",
}


ABLATION_EXPERIMENTS = [
    {"id": "full_gcm", "config": "gcm_ablation/full_gcm", "label": "Full GCM"},
    {"id": "no_distance", "config": "gcm_ablation/no_distance", "label": "GCM - Distance Prior"},
    {"id": "no_similarity", "config": "gcm_ablation/no_similarity", "label": "GCM - Similarity Prior"},
    {"id": "no_road", "config": "gcm_ablation/no_road", "label": "GCM - Road Prior"},
    {"id": "no_urban", "config": "gcm_ablation/no_urban", "label": "GCM - Urban Prior"},
    {"id": "no_learned", "config": "gcm_ablation/no_learned", "label": "GCM - Learned Relation"},
    {"id": "no_scene_weights", "config": "gcm_ablation/no_scene_weights", "label": "GCM - Scene Weights"},
]


def _make_json_serializable(obj):
    if isinstance(obj, dict):
        return {k: _make_json_serializable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_make_json_serializable(item) for item in obj]
    if isinstance(obj, (np.floating, np.float32, np.float64)):
        return float(obj)
    if isinstance(obj, (np.integer, np.int32, np.int64)):
        return int(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    return obj


def run_training(config_name: str, device: torch.device, root_dir: str, epochs: int = 100) -> Optional[str]:
    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(config_name)
    config["training"]["epochs"] = epochs

    train_dataset = GCMHAIRNetDataset(
        root_dir=root_dir,
        split="train",
        transforms=get_train_transforms(),
    )
    val_dataset = GCMHAIRNetDataset(
        root_dir=root_dir,
        split="val",
        transforms=get_val_transforms(),
    )

    train_loader = build_dataloader(
        train_dataset,
        batch_size=config.get("dataset", {}).get("train_batch_size", 16),
        shuffle=True,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=True,
    )
    val_loader = build_dataloader(
        val_dataset,
        batch_size=config.get("dataset", {}).get("val_batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    vis_dir = str(Path(config.get("outputs", {}).get("root_dir", "./outputs")) / "gcm_attention")
    trainer = Trainer(model, train_loader, val_loader, config, device, vis_dir=vis_dir)
    trainer.fit()

    best_path = Path(config.get("checkpoint", {}).get("dir", "./checkpoints")) / "best.pt"
    return str(best_path) if best_path.exists() else None


def run_evaluation(config_name: str, checkpoint_path: str, device: torch.device, root_dir: str, split: str = "test") -> Dict:
    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(config_name)

    if split == "val":
        dataset = GCMHAIRNetDataset(
            root_dir=root_dir,
            split="val",
            transforms=get_val_transforms(),
        )
    else:
        dataset = GCMHAIRNetDataset(
            root_dir=root_dir,
            split="test",
            transforms=get_val_transforms(),
        )

    loader = build_dataloader(
        dataset,
        batch_size=config.get("dataset", {}).get("test_batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    checkpoint = torch.load(checkpoint_path, map_location=device)
    ckpt_state = checkpoint["model_state_dict"]
    model_state = model.state_dict()
    new_state = {}
    for key, param in ckpt_state.items():
        if key in model_state and param.shape == model_state[key].shape:
            new_state[key] = param
    model.load_state_dict(new_state, strict=False)
    model.to(device)
    model.eval()

    loss_fn = build_loss(config.get("training", {}).get("loss", {}))
    evaluator = Evaluator()

    all_preds = []
    all_targets = []
    total_loss = 0.0
    num_batches = 0

    with torch.no_grad():
        for batch in loader:
            image = batch["image"].to(device)
            gis = batch["gis"].to(device)
            label = batch["label"].to(device)

            preds = model(image, gis)
            loss = loss_fn(preds, label)
            total_loss += loss.item()
            num_batches += 1

            preds_prob = torch.sigmoid(preds)
            all_preds.append(preds_prob.cpu().numpy())
            all_targets.append(label.cpu().numpy())

    preds_all = np.concatenate(all_preds, axis=0)
    targets_all = np.concatenate(all_targets, axis=0)
    metrics = evaluator(preds_all, targets_all)
    metrics["loss"] = total_loss / max(num_batches, 1)
    return metrics


def save_results_csv(results: List[Dict], output_path: Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    existing_rows = []
    if output_path.exists():
        with open(output_path, "r") as f:
            reader = csv.DictReader(f)
            existing_rows = list(reader)

    fieldnames = ["experiment_category", "model", "variant", "val_loss", "test_loss", "mse", "mae", "r2"]
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for row in existing_rows:
            if row.get("model") not in [r["model"] for r in results]:
                writer.writerow(row)

        for res in results:
            writer.writerow(res)


def run_baseline_study(args):
    device = get_device(args.device)
    root_dir = args.root_dir
    output_dir = Path(args.output_dir)
    results_path = output_dir / "experiments" / "results" / "experiment_results.csv"

    experiments_to_run = []
    if args.experiments:
        exp_ids = args.experiments.split(",")
        experiments_to_run = [e for e in BASELINE_EXPERIMENTS + ABLATION_EXPERIMENTS if e["id"] in exp_ids]
    else:
        experiments_to_run = BASELINE_EXPERIMENTS + ABLATION_EXPERIMENTS

    results = []

    for exp in experiments_to_run:
        exp_id = exp["id"]
        config_name = exp["config"]
        label = exp["label"]
        print(f"\n{'='*60}")
        print(f"Running: {label} (config={config_name})")
        print(f"{'='*60}")

        config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
        config = config_manager.load(config_name)

        ckpt_dir = Path(config.get("checkpoint", {}).get("dir", f"./checkpoints/{exp_id}"))
        best_path = ckpt_dir / "best.pt"

        if exp_id == "gcm":
            skip_train = False
            train_epochs = 100
            print(f"Training gcm for {train_epochs} epochs from scratch.")
        else:
            skip_train = args.skip_train
            train_epochs = 100
            if hasattr(args, "train_only_untrained") and args.train_only_untrained:
                if best_path.exists():
                    skip_train = True
                    print(f"Checkpoint already exists at {best_path}, skipping training.")
                else:
                    print(f"No checkpoint found at {best_path}, will train.")

        if not skip_train:
            trained_path = run_training(config_name, device, root_dir, epochs=train_epochs)
            if trained_path:
                best_path = Path(trained_path)

        if best_path.exists():
            val_metrics = run_evaluation(config_name, str(best_path), device, root_dir, split="val")
            test_metrics = run_evaluation(config_name, str(best_path), device, root_dir, split="test")

            category = "baseline" if exp in BASELINE_EXPERIMENTS else "ablation"
            result = {
                "experiment_category": category,
                "model": label.split(" ")[0] if " " in label else label,
                "variant": exp_id,
                "val_loss": round(val_metrics.get("loss", 0), 6),
                "test_loss": round(test_metrics.get("loss", 0), 6),
                "mse": round(test_metrics.get("mse", 0), 6),
                "mae": round(test_metrics.get("mae", 0), 6),
                "r2": round(test_metrics.get("r2", 0), 6),
            }
            results.append(result)
            print(f"Result: MSE={result['mse']:.6f}, R2={result['r2']:.6f}")

            metrics_dir = output_dir / ("baselines" if category == "baseline" else "ablations") / exp_id
            metrics_dir.mkdir(parents=True, exist_ok=True)
            with open(metrics_dir / "test_metrics.json", "w") as f:
                json.dump(_make_json_serializable(test_metrics), f, indent=2)
            with open(metrics_dir / "val_metrics.json", "w") as f:
                json.dump(_make_json_serializable(val_metrics), f, indent=2)
        else:
            print(f"Warning: No checkpoint found for {label} at {best_path}")

    save_results_csv(results, results_path)

    print(f"\n{'='*60}")
    print("Baseline study completed!")
    print(f"Results saved to: {results_path}")
    print(f"{'='*60}")


def copy_existing_fusion_results(output_dir: Path):
    fusion_dir = output_dir / "experiments" / "fusion"
    fusion_dir.mkdir(parents=True, exist_ok=True)

    existing_fusion_dirs = Path("./outputs/baselines").glob("*")
    for d in existing_fusion_dirs:
        if d.name in ["image_only", "gis_only", "concat", "addition", "gated",
                       "cross_attention", "multihead_cross_attention", "bilinear"]:
            dest = fusion_dir / d.name
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(d, dest)

    addition_dir = fusion_dir / "addition"
    if not addition_dir.exists():
        for d in Path("./outputs/baselines").glob("addition"):
            if d.is_dir():
                shutil.copytree(d, addition_dir)
                break


def register_existing_results(output_dir: Path):
    results_path = output_dir / "experiments" / "results" / "experiment_results.csv"
    results_path.parent.mkdir(parents=True, exist_ok=True)

    existing_results = []
    csv_path = Path("./outputs/tables/all_metrics.csv")
    if csv_path.exists():
        import csv as csv_mod
        with open(csv_path, "r") as f:
            reader = csv_mod.DictReader(f)
            for row in reader:
                split = row.get("split", "")
                exp_id = row.get("experiment", "")
                if split == "test":
                    category = "fusion" if exp_id in ["image_only", "gis_only", "concat", "addition", "gated",
                                                       "cross_attention", "multihead_cross_attention", "bilinear"] else (
                        "baseline" if exp_id in ["full"] else "ablation"
                    )
                    model_name = exp_id.replace("_", "-").title() if exp_id != "full" else "GCM-HAIRNet"
                    if exp_id == "addition":
                        model_name = "GCM-HAIRNet"
                    result = {
                        "experiment_category": category,
                        "model": model_name,
                        "variant": exp_id,
                        "val_loss": "",
                        "test_loss": "",
                        "mse": row.get("mse", ""),
                        "mae": row.get("mae", ""),
                        "r2": row.get("r2", ""),
                    }
                    existing_results.append(result)

    if existing_results:
        with open(results_path, "w", newline="") as f:
            fieldnames = ["experiment_category", "model", "variant", "val_loss", "test_loss", "mse", "mae", "r2"]
            writer = csv_mod.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for res in existing_results:
                writer.writerow(res)
        print(f"Registered {len(existing_results)} existing results in {results_path}")


def main():
    parser = argparse.ArgumentParser(description="Run controlled baseline study")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--output-dir", type=str, default="./outputs", help="Output directory")
    parser.add_argument("--device", type=str, default=None, help="Device")
    parser.add_argument("--epochs", type=int, default=100, help="Number of epochs")
    parser.add_argument("--experiments", type=str, default=None, help="Comma-separated experiment IDs")
    parser.add_argument("--skip-train", action="store_true", help="Skip training, only evaluate")
    parser.add_argument("--train-only-untrained", action="store_true", help="Skip experiments that already have checkpoints")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    register_existing_results(output_dir)
    copy_existing_fusion_results(output_dir)

    run_baseline_study(args)


if __name__ == "__main__":
    main()
```

---

### `scripts/run_experiments.py`

**Purpose:** Contains `run_training` function.

```python
import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from engine import Tester, Trainer, Validator
from losses import build_loss
from metrics import Evaluator
from models import build_model
from utils.misc import get_device


EXPERIMENTS = [
    # Fusion Study (existing - preserves results)
    {"id": "image_only", "config": "baseline_image_only", "type": "fusion"},
    {"id": "gis_only", "config": "baseline_gis_only", "type": "fusion"},
    {"id": "concat", "config": "baseline_concat", "type": "fusion"},
    {"id": "addition", "config": "baseline_addition", "type": "fusion"},
    {"id": "gated", "config": "baseline_gated", "type": "fusion"},
    {"id": "cross_attention", "config": "baseline_cross_attention", "type": "fusion"},
    {"id": "multihead_cross_attention", "config": "baseline_multihead_cross_attention", "type": "fusion"},
    {"id": "bilinear", "config": "baseline_bilinear", "type": "fusion"},
    # Controlled Baselines (new - Addition fusion + alternative relation module)
    {"id": "baseline_gcm", "config": "baselines/baseline_gcm", "type": "baseline"},
    {"id": "baseline_vit", "config": "baselines/baseline_vit", "type": "baseline"},
    {"id": "baseline_swin", "config": "baselines/baseline_swin", "type": "baseline"},
    {"id": "baseline_graphsage", "config": "baselines/baseline_graphsage", "type": "baseline"},
    {"id": "baseline_mha", "config": "baselines/baseline_mha", "type": "baseline"},
    {"id": "baseline_nonlocal", "config": "baselines/baseline_nonlocal", "type": "baseline"},
    # GCM Ablation Study (new - Addition + GCM with component removal)
    {"id": "full_gcm", "config": "gcm_ablation/full_gcm", "type": "ablation"},
    {"id": "no_distance", "config": "gcm_ablation/no_distance", "type": "ablation"},
    {"id": "no_similarity", "config": "gcm_ablation/no_similarity", "type": "ablation"},
    {"id": "no_road", "config": "gcm_ablation/no_road", "type": "ablation"},
    {"id": "no_urban", "config": "gcm_ablation/no_urban", "type": "ablation"},
    {"id": "no_learned", "config": "gcm_ablation/no_learned", "type": "ablation"},
    {"id": "no_scene_weights", "config": "gcm_ablation/no_scene_weights", "type": "ablation"},
]


def run_training(experiment: Dict, device: torch.device, epochs: int = 100) -> Optional[str]:
    config_name = experiment["config"]
    exp_id = experiment["id"]
    print(f"\n{'='*60}")
    print(f"Training: {exp_id} (config={config_name})")
    print(f"{'='*60}")

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(config_name)

    from datasets.transforms import get_train_transforms

    train_dataset = GCMHAIRNetDataset(
        root_dir=config.get("data", {}).get("root_dir", "./data/processed"),
        split="train",
        transforms=get_train_transforms(),
    )
    val_dataset = GCMHAIRNetDataset(
        root_dir=config.get("data", {}).get("root_dir", "./data/processed"),
        split="val",
        transforms=get_val_transforms(),
    )

    train_loader = build_dataloader(
        train_dataset,
        batch_size=config.get("dataset", {}).get("train_batch_size", 16),
        shuffle=True,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=True,
    )
    val_loader = build_dataloader(
        val_dataset,
        batch_size=config.get("dataset", {}).get("val_batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    trainer = Trainer(model, train_loader, val_loader, config, device)
    trainer.fit()

    best_path = Path(config.get("checkpoint", {}).get("dir", "./checkpoints")) / "best.pt"
    return str(best_path) if best_path.exists() else None


def run_evaluation(experiment: Dict, checkpoint_path: str, device: torch.device, split: str = "test") -> Dict:
    config_name = experiment["config"]
    exp_id = experiment["id"]
    print(f"\nEvaluating {exp_id} on {split}...")

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(config_name)

    if split == "val":
        dataset = GCMHAIRNetDataset(
            root_dir=config.get("data", {}).get("root_dir", "./data/processed"),
            split="val",
            transforms=get_val_transforms(),
        )
    else:
        dataset = GCMHAIRNetDataset(
            root_dir=config.get("data", {}).get("root_dir", "./data/processed"),
            split="test",
            transforms=get_val_transforms(),
        )

    loader = build_dataloader(
        dataset,
        batch_size=config.get("dataset", {}).get("test_batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    checkpoint = torch.load(checkpoint_path, map_location=device)
    ckpt_state = checkpoint["model_state_dict"]
    model_state = model.state_dict()
    new_state = {}
    for key, param in ckpt_state.items():
        if key in model_state and param.shape == model_state[key].shape:
            new_state[key] = param
    model.load_state_dict(new_state, strict=False)
    model.to(device)
    model.eval()

    loss_fn = build_loss(config.get("training", {}).get("loss", {}))
    evaluator = Evaluator()

    all_preds = []
    all_targets = []
    all_cities = []
    city_metrics = {}

    with torch.no_grad():
        for batch in loader:
            image = batch["image"].to(device)
            gis = batch["gis"].to(device)
            label = batch["label"].to(device)
            city_names = batch.get("city_name", ["unknown"] * image.shape[0])

            preds = model(image, gis)
            preds_prob = torch.sigmoid(preds)

            all_preds.append(preds_prob.cpu().numpy())
            all_targets.append(label.cpu().numpy())
            all_cities.extend(city_names)

            for i, city in enumerate(city_names):
                if city not in city_metrics:
                    city_metrics[city] = {"preds": [], "targets": []}
                city_metrics[city]["preds"].append(preds_prob[i].cpu().numpy().flatten())
                city_metrics[city]["targets"].append(label[i].cpu().numpy().flatten())

    preds_all = np.concatenate(all_preds, axis=0)
    targets_all = np.concatenate(all_targets, axis=0)
    metrics = evaluator(preds_all, targets_all)

    per_city = {}
    for city, data in city_metrics.items():
        city_preds = np.concatenate([p.reshape(1, -1) for p in data["preds"]], axis=0).flatten()
        city_targets = np.concatenate([t.reshape(1, -1) for t in data["targets"]], axis=0).flatten()
        city_eval = Evaluator()
        city_metrics_dict = city_eval(city_preds, city_targets)
        per_city[city] = city_metrics_dict

    result = {
        "experiment_id": exp_id,
        "split": split,
        "metrics": metrics,
        "per_city": per_city,
        "num_samples": len(targets_all),
    }
    return result


def save_common_results(results: List[Dict], output_path: Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    experiment_map = {e["id"]: e for e in EXPERIMENTS}

    existing_rows = []
    fieldnames = ["experiment_category", "model", "variant", "val_loss", "test_loss", "mse", "mae", "r2"]
    if output_path.exists():
        with open(output_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("variant") not in {r["experiment_id"] for r in results}:
                    existing_rows.append(row)

    model_name_map = {
        "image_only": "ImageOnly",
        "gis_only": "GISOnly",
        "concat": "Concat",
        "addition": "Addition",
        "gated": "Gated",
        "cross_attention": "CrossAttention",
        "multihead_cross_attention": "MultiHeadCrossAttention",
        "bilinear": "Bilinear",
        "baseline_gcm": "GCM-HAIRNet",
        "baseline_vit": "ViT",
        "baseline_swin": "Swin",
        "baseline_graphsage": "GraphSAGE",
        "baseline_mha": "MHA",
        "baseline_nonlocal": "Non-Local",
    }

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in existing_rows:
            writer.writerow(row)

        test_results = {r["experiment_id"]: r for r in results if r.get("split") == "test"}
        val_results = {r["experiment_id"]: r for r in results if r.get("split") == "val"}

        for exp_id, test_res in test_results.items():
            exp = experiment_map.get(exp_id, {})
            exp_type = exp.get("type", "unknown")

            if exp_type == "fusion":
                category = "fusion"
                model = model_name_map.get(exp_id, exp_id.replace("_", "-").title())
            elif exp_type == "baseline":
                category = "baseline"
                model = model_name_map.get(exp_id, exp_id.replace("baseline_", "").title())
            else:
                category = "ablation"
                model = "GCM"

            if exp_type == "ablation":
                variant = "full" if exp_id == "full_gcm" else exp_id
            else:
                variant = "default"
            val_res = val_results.get(exp_id, {})

            writer.writerow({
                "experiment_category": category,
                "model": model,
                "variant": variant,
                "val_loss": val_res.get("metrics", {}).get("mse", ""),
                "test_loss": test_res.get("metrics", {}).get("mse", ""),
                "mse": test_res.get("metrics", {}).get("mse", ""),
                "mae": test_res.get("metrics", {}).get("mae", ""),
                "r2": test_res.get("metrics", {}).get("r2", ""),
            })


def save_results(results: List[Dict], output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)

    summary = []
    for res in results:
        row = {"experiment": res["experiment_id"], "split": res["split"]}
        row.update(res["metrics"])
        summary.append(row)

    csv_path = output_dir / "all_metrics.csv"
    if summary:
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=summary[0].keys())
            writer.writeheader()
            writer.writerows(summary)

    json_path = output_dir / "all_metrics.json"
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2, default=str)

    print(f"\nResults saved to {csv_path} and {json_path}")


def generate_comparison_plots(results: List[Dict], output_dir: Path):
    import matplotlib.pyplot as plt

    output_dir.mkdir(parents=True, exist_ok=True)
    test_results = [r for r in results if r["split"] == "test"]

    for metric in ["mse", "mae", "r2"]:
        names = [r["experiment_id"] for r in test_results]
        values = [r["metrics"].get(metric, 0.0) for r in test_results]

        fig, ax = plt.subplots(figsize=(12, 6))
        colors = ["#2ecc71" if "baseline" in n else "#3498db" if "ablation" in n else "#e74c3c" for n in names]
        bars = ax.bar(names, values, color=colors)
        ax.set_title(f"Test {metric.upper()} Comparison", fontsize=14, fontweight="bold")
        ax.set_ylabel(metric.upper(), fontsize=12)
        ax.tick_params(axis="x", rotation=45, labelsize=9)
        ax.grid(axis="y", alpha=0.3)

        for bar, val in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{val:.4f}", ha="center", va="bottom", fontsize=8)

        plt.tight_layout()
        plt.savefig(output_dir / f"test_{metric}_comparison.png", dpi=150, bbox_inches="tight")
        plt.close(fig)

    print(f"Comparison plots saved to {output_dir}")


def generate_per_city_csv(results: List[Dict], output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    test_results = [r for r in results if r["split"] == "test"]

    rows = []
    for res in test_results:
        exp_id = res["experiment_id"]
        for city, metrics in res.get("per_city", {}).items():
            row = {"experiment": exp_id, "city": city}
            row.update(metrics)
            rows.append(row)

    if rows:
        csv_path = output_dir / "per_city_metrics.csv"
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        print(f"Per-city metrics saved to {csv_path}")


def generate_scene_weights(experiment: Dict, checkpoint_path: str, device: torch.device, output_dir: Path):
    config_name = experiment["config"]
    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(config_name)

    dataset = GCMHAIRNetDataset(
        root_dir=config.get("data", {}).get("root_dir", "./data/processed"),
        split="test",
        transforms=get_val_transforms(),
    )
    loader = build_dataloader(
        dataset,
        batch_size=1,
        shuffle=False,
        num_workers=0,
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    checkpoint = torch.load(checkpoint_path, map_location=device)
    model.load_state_dict(checkpoint["model_state_dict"], strict=False)
    model.to(device)
    model.eval()

    all_weights = []
    all_cities = []

    with torch.no_grad():
        for batch in loader:
            image = batch["image"].to(device)
            gis = batch["gis"].to(device)
            city = batch.get("city_name", ["unknown"])[0]

            scene_weight_module = None
            if hasattr(model, "gcm") and hasattr(model.gcm, "grm") and hasattr(model.gcm.grm, "scene_weight_predictor"):
                scene_weight_module = model.gcm.grm.scene_weight_predictor
            elif hasattr(model, "relation_module") and hasattr(model.relation_module, "gcm_transformer"):
                grm = model.relation_module.gcm_transformer.grm
                if hasattr(grm, "scene_weight_predictor"):
                    scene_weight_module = grm.scene_weight_predictor

            if scene_weight_module is not None:
                weights = scene_weight_module(gis)
                all_weights.append(weights.cpu().numpy().mean(axis=0))
                all_cities.append(city)

    if all_weights:
        output_dir.mkdir(parents=True, exist_ok=True)
        weights_arr = np.array(all_weights)
        csv_path = output_dir / "scene_weights.csv"
        with open(csv_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["city", "distance", "similarity", "road", "urban", "learned"])
            for city, w in zip(all_cities, weights_arr):
                writer.writerow([city] + [f"{x:.4f}" for x in w])

        mean_weights = weights_arr.mean(axis=0)
        std_weights = weights_arr.std(axis=0)
        print(f"Scene weights: distance={mean_weights[0]:.4f}, similarity={mean_weights[1]:.4f}, road={mean_weights[2]:.4f}, urban={mean_weights[3]:.4f}, learned={mean_weights[4]:.4f}")
        print(f"Scene weights saved to {csv_path}")


def main():
    parser = argparse.ArgumentParser(description="Run all baseline and ablation experiments")
    parser.add_argument("--config", type=str, default="train", help="Base config name")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--device", type=str, default=None, help="Device")
    parser.add_argument("--output-dir", type=str, default="./outputs", help="Output directory")
    parser.add_argument("--epochs", type=int, default=100, help="Number of epochs")
    parser.add_argument("--skip-train", action="store_true", help="Skip training, only evaluate existing checkpoints")
    parser.add_argument("--experiments", type=str, default=None, help="Comma-separated experiment IDs to run")
    args = parser.parse_args()

    device = get_device(args.device)
    output_dir = Path(args.output_dir)

    selected = EXPERIMENTS
    if args.experiments:
        selected = [e for e in EXPERIMENTS if e["id"] in args.experiments.split(",")]
        if not selected:
            print(f"No experiments match: {args.experiments}")
            return

    results = []

    for experiment in selected:
        exp_id = experiment["id"]
        exp_type = experiment["type"]
        config_name = experiment["config"]

        config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
        config = config_manager.load(config_name)
        ckpt_dir = Path(config.get("checkpoint", {}).get("dir", f"./checkpoints/{exp_type}/{exp_id}"))
        best_path = ckpt_dir / "best.pt"

        if not args.skip_train:
            trained_path = run_training(experiment, device, epochs=args.epochs)
            if trained_path:
                best_path = Path(trained_path)

        if best_path.exists():
            for split in ["val", "test"]:
                result = run_evaluation(experiment, str(best_path), device, split=split)
                results.append(result)

                metrics_dir = output_dir / "experiments" / exp_type / exp_id
                metrics_dir.mkdir(parents=True, exist_ok=True)
                with open(metrics_dir / f"{split}_metrics.json", "w") as f:
                    json.dump(result, f, indent=2, default=str)

            if exp_type == "ablation" or exp_id in ["full"]:
                generate_scene_weights(experiment, str(best_path), device, output_dir / "experiments" / exp_type / exp_id / "attention")
        else:
            print(f"Warning: No checkpoint found for {exp_id} at {best_path}")

    save_results(results, output_dir / "tables")
    generate_comparison_plots(results, output_dir / "comparison")
    generate_per_city_csv(results, output_dir / "tables")
    save_common_results(results, output_dir / "experiments" / "results" / "experiment_results.csv")

    print(f"\n{'='*60}")
    print("All experiments completed!")
    print(f"Results: {output_dir}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
```

---

### `scripts/standardize_configs.py`

**Purpose:** Standardize all config files to match canonical GCM+Addition training parameters.

```python
#!/usr/bin/env python3
"""Standardize all config files to match canonical GCM+Addition training parameters."""

import yaml
from pathlib import Path

CONFIG_DIR = Path("configs")

CANONICAL_TRAINING = {
    "early_stopping": {"mode": "min", "monitor": "val_loss", "patience": 15},
    "epochs": 100,
    "gradient_accumulation_steps": 1,
    "gradient_clip_val": 1.0,
    "loss": {
        "focal_alpha": 0.25,
        "focal_gamma": 2.0,
        "focal_weight": 0.0,
        "huber_delta": 0.1,
        "huber_weight": 0.5,
        "l1_weight": 0.5,
        "mse_weight": 1.0,
        "type": "combined",
    },
    "optimizer": {
        "betas": [0.9, 0.999],
        "lr": 1.0e-4,
        "weight_decay": 1.0e-4,
    },
    "scheduler": {
        "T_max": 100,
        "eta_min": 1.0e-6,
        "type": "cosine_annealing",
        "warmup_epochs": 5,
    },
}

CANONICAL_DATASET = {
    "augmentation": True,
    "num_workers": 0,
    "pin_memory": True,
    "prefetch_factor": 2,
    "drop_last": True,
    "persistent_workers": False,
    "train_batch_size": 16,
    "val_batch_size": 32,
    "test_batch_size": 32,
}

CANONICAL_CHECKPOINT = {
    "every_n_epochs": 1,
    "monitor": "val_loss",
    "mode": "min",
    "save_last": True,
    "save_top_k": 5,
}


def standardize_config(path: Path):
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    
    if not config:
        return False
    
    modified = False
    
    # Standardize training section
    if "training" in config:
        # Merge canonical training params
        for key, value in CANONICAL_TRAINING.items():
            if key not in config["training"]:
                config["training"][key] = value
                modified = True
            elif isinstance(value, dict) and isinstance(config["training"][key], dict):
                for subkey, subvalue in value.items():
                    if subkey not in config["training"][key]:
                        config["training"][key][subkey] = subvalue
                        modified = True
        
        # Fix loss weights if present
        if "loss" in config["training"]:
            loss = config["training"]["loss"]
            canonical_loss = CANONICAL_TRAINING["loss"]
            for key in ["mse_weight", "l1_weight", "huber_weight", "focal_weight"]:
                if key in loss and key in canonical_loss:
                    if loss[key] != canonical_loss[key]:
                        print(f"  {path.name}: Fixing loss.{key}: {loss[key]} -> {canonical_loss[key]}")
                        loss[key] = canonical_loss[key]
                        modified = True
        
        # Fix optimizer if present
        if "optimizer" in config["training"]:
            opt = config["training"]["optimizer"]
            canonical_opt = CANONICAL_TRAINING["optimizer"]
            for key in ["lr", "weight_decay", "betas"]:
                if key in canonical_opt:
                    if key not in opt or opt[key] != canonical_opt[key]:
                        print(f"  {path.name}: Fixing optimizer.{key}: {opt.get(key)} -> {canonical_opt[key]}")
                        opt[key] = canonical_opt[key]
                        modified = True
        
        # Fix epochs
        if "epochs" in config["training"]:
            if config["training"]["epochs"] != 100:
                print(f"  {path.name}: Fixing epochs: {config['training']['epochs']} -> 100")
                config["training"]["epochs"] = 100
                modified = True
        
        # Fix gradient_clip_val
        if "gradient_clip_val" not in config["training"]:
            config["training"]["gradient_clip_val"] = 1.0
            modified = True
    
    # Standardize checkpoint section
    if "checkpoint" in config:
        for key, value in CANONICAL_CHECKPOINT.items():
            if key not in config["checkpoint"]:
                config["checkpoint"][key] = value
                modified = True
    
    # Standardize dataset section
    if "dataset" in config:
        for key, value in CANONICAL_DATASET.items():
            if key not in config["dataset"]:
                config["dataset"][key] = value
                modified = True
    
    if modified:
        with open(path, "w") as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)
        print(f"  Updated: {path}")
    
    return modified


def main():
    updated = 0
    for yaml_file in CONFIG_DIR.rglob("*.yaml"):
        if yaml_file.name in ["dataset.yaml", "inference.yaml", "model.yaml"]:
            continue
        if standardize_config(yaml_file):
            updated += 1
    
    print(f"\nUpdated {updated} config files")
    
    # Also fix the default in losses/combined.py
    combined_path = Path("losses/combined.py")
    if combined_path.exists():
        content = combined_path.read_text()
        if 'l1_weight: float = 0.1' in content:
            content = content.replace('l1_weight: float = 0.1', 'l1_weight: float = 0.5')
            combined_path.write_text(content)
            print(f"Fixed default l1_weight in {combined_path}")
        elif 'l1_weight=0.1' in content:
            content = content.replace('l1_weight=0.1', 'l1_weight=0.5')
            combined_path.write_text(content)
            print(f"Fixed default l1_weight in {combined_path}")


if __name__ == "__main__":
    main()
```

---

### `scripts/test.py`

**Purpose:** Contains `main` function.

```python
import argparse
import sys
from pathlib import Path
from typing import Optional

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from engine import Tester
from losses import build_loss
from metrics import Evaluator
from models import build_model
from utils.logger import Logger
from utils.misc import get_device


def main():
    parser = argparse.ArgumentParser(description="Test GCM-HAIRNet")
    parser.add_argument("--config", type=str, default="train", help="Config name")
    parser.add_argument("--checkpoint", type=str, required=True, help="Checkpoint path")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--device", type=str, default=None, help="Device")
    parser.add_argument("--output-dir", type=str, default="./outputs/test", help="Output directory")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)
    device = get_device(args.device)

    test_dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
        split="test",
        transforms=get_val_transforms(),
    )
    test_loader = build_dataloader(
        test_dataset,
        batch_size=config.get("dataset", {}).get("test_batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    checkpoint = torch.load(args.checkpoint, map_location=device)
    ckpt_state = checkpoint["model_state_dict"]
    model_state = model.state_dict()
    new_state = {}
    matched = 0
    skipped = 0
    for key, param in ckpt_state.items():
        if key in model_state:
            if param.shape == model_state[key].shape:
                new_state[key] = param
                matched += 1
            else:
                skipped += 1
        else:
            skipped += 1
    result = model.load_state_dict(new_state, strict=False)
    if result.missing_keys or result.unexpected_keys:
        print(f"Warning: Partial checkpoint load - missing: {result.missing_keys}, unexpected: {result.unexpected_keys}")
    if skipped > 0:
        print(f"Info: Loaded {matched} layers, skipped {skipped} incompatible layers from checkpoint")
    model.to(device)
    model.eval()

    loss_fn = build_loss(config.get("training", {}).get("loss", {}))
    logger = Logger(log_dir="./logs", experiment_name="test", use_tensorboard=True)
    metrics = Evaluator()

    tester = Tester(model, test_loader, loss_fn, device, metrics, logger)
    test_metrics, preds, targets, cities = tester.test()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    import numpy as np
    np.save(output_dir / "test_predictions.npy", np.concatenate(preds, axis=0))
    np.save(output_dir / "test_targets.npy", np.concatenate(targets, axis=0))

    print("Test Metrics:")
    for k, v in test_metrics.items():
        print(f"  {k}: {v:.4f}")

    logger.close()


if __name__ == "__main__":
    main()
```

---

### `scripts/train.py`

**Purpose:** Contains `main` function.

```python
from pathlib import Path
import argparse
import sys
from typing import Optional

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_train_transforms, get_val_transforms
from engine import Trainer
from models import build_model
from utils.misc import get_device


def main():
    parser = argparse.ArgumentParser(description="Train GCM-HAIRNet")
    parser.add_argument("--config", type=str, default="train", help="Config name (without .yaml)")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root directory")
    parser.add_argument("--checkpoint", type=str, default=None, help="Checkpoint to resume from")
    parser.add_argument("--device", type=str, default=None, help="Device to use")
    parser.add_argument("--output-dir", type=str, default="./outputs", help="Output directory")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)

    device = get_device(args.device)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    norm_stats_path = config.get("data", {}).get("normalization_stats")
    norm_stats = None
    if norm_stats_path:
        norm_stats_file = Path(norm_stats_path)
        if norm_stats_file.exists():
            import json
            with open(norm_stats_file, "r") as f:
                norm_stats = json.load(f)

    train_dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
        split="train",
        transforms=get_train_transforms(normalization_stats=norm_stats),
    )
    val_dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
        split="val",
        transforms=get_val_transforms(normalization_stats=norm_stats),
    )

    train_loader = build_dataloader(
        train_dataset,
        batch_size=config.get("dataset", {}).get("train_batch_size", 16),
        shuffle=True,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=True,
    )
    val_loader = build_dataloader(
        val_dataset,
        batch_size=config.get("dataset", {}).get("val_batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    vis_dir = str(Path(args.output_dir) / "gcm_attention")
    trainer = Trainer(model, train_loader, val_loader, config, device, vis_dir=vis_dir)

    if args.checkpoint:
        trainer.resume(args.checkpoint)

    trainer.fit()


if __name__ == "__main__":
    main()
```

---

### `scripts/train_improved.py`

**Purpose:** Contains `evaluate` function.

```python
import sys
import time
from pathlib import Path
from typing import Dict

import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_train_transforms, get_val_transforms
from models import build_model
from losses import build_loss
from metrics import Evaluator
from utils.misc import get_device


def evaluate(model, loader, loss_fn, device):
    model.eval()
    metric_fn = Evaluator()
    all_preds, all_targets = [], []
    total_loss, num_batches = 0.0, 0
    with torch.no_grad():
        for batch in loader:
            img = batch["image"].to(device)
            gis = batch["gis"].to(device)
            lab = batch["label"].to(device)
            out = model(img, gis)
            loss = loss_fn(out, lab)
            total_loss += loss.item()
            num_batches += 1
            all_preds.append(torch.sigmoid(out).cpu().numpy())
            all_targets.append(lab.cpu().numpy())
    preds = np.concatenate(all_preds, axis=0)
    targets = np.concatenate(all_targets, axis=0)
    metrics = metric_fn(preds, targets)
    metrics["loss"] = total_loss / max(num_batches, 1)
    return metrics


def main():
    config_name = sys.argv[1] if len(sys.argv) > 1 else "improved_full_fast"
    epochs = int(sys.argv[2]) if len(sys.argv) > 2 else 100

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(config_name)
    device = get_device()
    print(f"Device: {device}", flush=True)

    root_dir = config.get("data", {}).get("root_dir", "./data/processed")

    train_ds = GCMHAIRNetDataset(root_dir=root_dir, split="train", transforms=get_train_transforms())
    val_ds = GCMHAIRNetDataset(root_dir=root_dir, split="val", transforms=get_val_transforms())
    test_ds = GCMHAIRNetDataset(root_dir=root_dir, split="test", transforms=get_val_transforms())
    print(f"Train: {len(train_ds)}, Val: {len(val_ds)}, Test: {len(test_ds)}", flush=True)

    bs = config.get("dataset", {}).get("train_batch_size", 16)
    train_loader = build_dataloader(train_ds, batch_size=bs, shuffle=True, num_workers=0, drop_last=True)
    val_loader = build_dataloader(val_ds, batch_size=32, shuffle=False, num_workers=0, drop_last=False)
    test_loader = build_dataloader(test_ds, batch_size=32, shuffle=False, num_workers=0, drop_last=False)

    torch.manual_seed(config.get("experiment", {}).get("seed", 42))
    model = build_model(config.get("model", {})).to(device)
    print(f"Parameters: {sum(p.numel() for p in model.parameters()):,}", flush=True)

    lr = config.get("training", {}).get("optimizer", {}).get("lr", 1e-4)
    wd = config.get("training", {}).get("optimizer", {}).get("weight_decay", 1e-4)
    betas = tuple(config.get("training", {}).get("optimizer", {}).get("betas", [0.9, 0.999]))
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=wd, betas=betas)

    sched_cfg = config.get("training", {}).get("scheduler", {})
    warmup = sched_cfg.get("warmup_epochs", 0)
    if sched_cfg.get("type") == "cosine_annealing":
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            optimizer, T_max=sched_cfg.get("T_max", epochs), eta_min=sched_cfg.get("eta_min", 1e-6)
        )
    else:
        scheduler = None

    loss_fn = build_loss(config.get("training", {}).get("loss", {}))
    gclip = config.get("training", {}).get("gradient_clip_val", 1.0)

    ckpt_dir = Path(config.get("checkpoint", {}).get("dir", "./checkpoints/improved"))
    ckpt_dir.mkdir(parents=True, exist_ok=True)

    best_val_r2 = float("-inf")
    best_val_loss = float("inf")
    patience = config.get("training", {}).get("early_stopping", {}).get("patience", 15)
    monitor = config.get("training", {}).get("early_stopping", {}).get("monitor", "val_loss")
    mode = config.get("training", {}).get("early_stopping", {}).get("mode", "min")

    epochs_no_improve = 0

    for epoch in range(epochs):
        t0 = time.time()
        model.train()
        train_loss, n = 0.0, 0
        for batch in train_loader:
            img = batch["image"].to(device)
            gis = batch["gis"].to(device)
            lab = batch["label"].to(device)
            optimizer.zero_grad()
            out = model(img, gis)
            loss = loss_fn(out, lab)
            loss.backward()
            if gclip:
                torch.nn.utils.clip_grad_norm_(model.parameters(), gclip)
            optimizer.step()
            train_loss += loss.item()
            n += 1

        if epoch < warmup and warmup > 0:
            lr_scale = (epoch + 1) / warmup
            for pg in optimizer.param_groups:
                pg["lr"] = lr * lr_scale

        val_metrics = evaluate(model, val_loader, loss_fn, device)

        if scheduler and epoch >= warmup:
            scheduler.step()

        dt = time.time() - t0
        cur_lr = optimizer.param_groups[0]["lr"]
        print(
            f"Epoch {epoch+1:3d}/{epochs}: train_loss={train_loss/n:.4f} "
            f"val_loss={val_metrics['loss']:.4f} val_mse={val_metrics['mse']:.4f} "
            f"val_mae={val_metrics['mae']:.4f} val_r2={val_metrics['r2']:.4f} "
            f"val_acc={val_metrics['accuracy']:.4f} val_f1={val_metrics['f1']:.4f} "
            f"val_iou={val_metrics['iou']:.4f} lr={cur_lr:.6f} time={dt:.1f}s",
            flush=True,
        )

        torch.save(
            {"epoch": epoch, "model_state_dict": model.state_dict(), "optimizer_state_dict": optimizer.state_dict(), "val_metrics": val_metrics},
            ckpt_dir / "last.pt",
        )

        improved = False
        if monitor == "val_loss" and mode == "min":
            improved = val_metrics["loss"] < best_val_loss
            if improved:
                best_val_loss = val_metrics["loss"]
        elif monitor == "r2" and mode == "max":
            improved = val_metrics["r2"] > best_val_r2
            if improved:
                best_val_r2 = val_metrics["r2"]
        if improved:
            torch.save(
                {"epoch": epoch, "model_state_dict": model.state_dict(), "optimizer_state_dict": optimizer.state_dict(), "val_metrics": val_metrics},
                ckpt_dir / "best.pt",
            )
            epochs_no_improve = 0
        else:
            epochs_no_improve += 1

        if patience > 0 and epochs_no_improve >= patience:
            print(f"Early stopping at epoch {epoch+1}", flush=True)
            break

    best = torch.load(ckpt_dir / "best.pt", map_location=device, weights_only=False)
    model.load_state_dict(best["model_state_dict"])

    model.eval()
    metric_fn = Evaluator()
    all_preds, all_targets = [], []
    with torch.no_grad():
        for batch in test_loader:
            img = batch["image"].to(device)
            gis = batch["gis"].to(device)
            lab = batch["label"].to(device)
            out = model(img, gis)
            all_preds.append(torch.sigmoid(out).cpu().numpy())
            all_targets.append(lab.cpu().numpy())
    preds = np.concatenate(all_preds, axis=0)
    targets = np.concatenate(all_targets, axis=0)
    test_metrics = metric_fn(preds, targets)
    test_metrics["loss"] = evaluate(model, test_loader, loss_fn, device)["loss"]
    print(
        f"\nBEST (epoch {best['epoch']}): TEST loss={test_metrics['loss']:.4f} "
        f"mse={test_metrics['mse']:.4f} mae={test_metrics['mae']:.4f} "
        f"r2={test_metrics['r2']:.4f} acc@0.5={test_metrics['accuracy']:.4f} "
        f"f1={test_metrics['f1']:.4f} prec={test_metrics['precision']:.4f} "
        f"rec={test_metrics['recall']:.4f} iou={test_metrics['iou']:.4f}",
        flush=True,
    )

    import json
    with open(ckpt_dir / "test_metrics.json", "w") as f:
        json.dump(test_metrics, f, indent=2, default=str)
    np.save(ckpt_dir / "test_predictions.npy", preds)
    np.save(ckpt_dir / "test_targets.npy", targets)


if __name__ == "__main__":
    main()
```

---

### `scripts/train_simple.py`

**Purpose:** Contains `main` function.

```python
import sys
import torch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader
from models import GCMHAIRNet
from losses import build_loss
from utils.misc import get_device


def main():
    print("Starting training...")
    config_manager = ConfigManager()
    config = config_manager.load("train")
    device = get_device()
    print(f"Using device: {device}")

    print("Loading data...")
    try:
        dataset = GCMHAIRNetDataset(root_dir="./data/processed", split="train")
        loader = build_dataloader(dataset, batch_size=4, shuffle=True, drop_last=True)
        val_dataset = GCMHAIRNetDataset(root_dir="./data/processed", split="val")
        val_loader = build_dataloader(val_dataset, batch_size=4, shuffle=False, drop_last=False)
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    print(f"Train: {len(dataset)} samples, Val: {len(val_dataset)} samples")

    if len(val_dataset) == 0:
        print("Warning: Validation dataset is empty. Skipping validation.")
        val_loader = None

    print("Creating model...")
    model = GCMHAIRNet(config.get("model", {})).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
    loss_fn = build_loss({"type": "mse"})

    print(f"Parameters: {sum(p.numel() for p in model.parameters()):,}")
    print("=" * 60)

    for epoch in range(100):
        model.train()
        train_loss = 0.0
        count = 0

        for batch in loader:
            img = batch["image"].to(device)
            gis = batch["gis"].to(device)
            label = batch["label"].to(device)

            optimizer.zero_grad()
            pred = model(img, gis)
            loss = loss_fn(pred, label)
            loss.backward()
            optimizer.step()

            train_loss += loss.item()
            count += 1

        train_loss /= max(count, 1)

        val_loss = 0.0
        if val_loader is not None:
            model.eval()
            vcount = 0

            with torch.no_grad():
                for batch in val_loader:
                    img = batch["image"].to(device)
                    gis = batch["gis"].to(device)
                    label = batch["label"].to(device)
                    pred = model(img, gis)
                    loss = loss_fn(pred, label)
                    val_loss += loss.item()
                    vcount += 1

            val_loss /= max(vcount, 1)
        else:
            val_loss = train_loss

        print(f"Epoch {epoch+1:3d}/100: train_loss={train_loss:.4f}, val_loss={val_loss:.4f}")

        if (epoch + 1) % 10 == 0:
            checkpoint_dir = Path("checkpoints/gcm_simple")
            checkpoint_dir.mkdir(parents=True, exist_ok=True)
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'train_loss': train_loss,
                'val_loss': val_loss,
            }, checkpoint_dir / f"epoch_{epoch+1:04d}.pt")
            print(f"  Saved checkpoint at epoch {epoch+1}")


if __name__ == "__main__":
    main()
```

---

### `scripts/validate.py`

**Purpose:** Contains `main` function.

```python
import argparse
import sys
from pathlib import Path
from typing import Optional

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from engine import Validator
from losses import build_loss
from metrics import Evaluator
from models import build_model
from utils.logger import Logger
from utils.misc import get_device


def main():
    parser = argparse.ArgumentParser(description="Validate GCM-HAIRNet")
    parser.add_argument("--config", type=str, default="train", help="Config name")
    parser.add_argument("--checkpoint", type=str, required=True, help="Checkpoint path")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--device", type=str, default=None, help="Device")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)
    device = get_device(args.device)

    val_dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
        split="val",
        transforms=get_val_transforms(),
    )
    val_loader = build_dataloader(
        val_dataset,
        batch_size=config.get("dataset", {}).get("val_batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    checkpoint = torch.load(args.checkpoint, map_location=device)
    ckpt_state = checkpoint["model_state_dict"]
    model_state = model.state_dict()
    new_state = {}
    matched = 0
    skipped = 0
    for key, param in ckpt_state.items():
        if key in model_state:
            if param.shape == model_state[key].shape:
                new_state[key] = param
                matched += 1
            else:
                skipped += 1
        else:
            skipped += 1
    result = model.load_state_dict(new_state, strict=False)
    if result.missing_keys or result.unexpected_keys:
        print(f"Warning: Partial checkpoint load - missing: {result.missing_keys}, unexpected: {result.unexpected_keys}")
    if skipped > 0:
        print(f"Info: Loaded {matched} layers, skipped {skipped} incompatible layers from checkpoint")
    model.to(device)
    model.eval()

    loss_fn = build_loss(config.get("training", {}).get("loss", {}))
    logger = Logger(log_dir="./logs", experiment_name="validation", use_tensorboard=True)
    metrics = Evaluator()

    validator = Validator(model, val_loader, loss_fn, device, metrics, logger)
    val_metrics = validator.validate()

    print("Validation Metrics:")
    for k, v in val_metrics.items():
        print(f"  {k}: {v:.4f}")

    if hasattr(logger, "log_metrics"):
        logger.log_metrics(val_metrics, step=0, prefix="val")

    logger.close()


if __name__ == "__main__":
    main()
```

---

### `setup.py`

**Purpose:** Implementation of `setup.py`.

```python
from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="gcm-hairnet",
    version="0.1.0",
    description="Research-grade repository for GCM-HAIRNet",
    author="GCM-HAIRNet Authors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests*", "scripts*", "configs*", "docs*"]),
    python_requires=">=3.9",
    install_requires=[
        "torch>=2.0.0",
        "torchvision>=0.15.0",
        "numpy>=1.24.0",
        "pyyaml>=6.0",
        "tensorboard>=2.14.0",
        "matplotlib>=3.7.0",
        "pillow>=10.0.0",
        "scikit-learn>=1.3.0",
        "einops>=0.7.0",
        "timm>=0.9.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.1.0",
        ],
    },
)
```

---

### `tests/__init__.py`

**Purpose:** Implementation of `__init__.py`.

```python

```

---

### `tests/test_ablation.py`

**Purpose:** Defines `SimpleModel` module/class.

```python
import torch
import torch.nn as nn

from utils.ablation import AblationManager


class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.swin = nn.Linear(10, 10)
        self.grm = nn.Linear(10, 10)
        self.decoder = nn.Linear(10, 1)

    def forward(self, image, gis):
        x = image.flatten(1)
        x = self.swin(x)
        x = self.grm(x)
        return self.decoder(x)


class TestAblationManager:
    def test_replace_with_identity_zeroes_output(self):
        model = SimpleModel()
        config = {
            "ablation": {
                "modules": ["swin"],
                "strategy": "replace_with_identity",
            }
        }
        manager = AblationManager(model, config)
        x = torch.randn(2, 10)
        original_out = model.swin(x).clone()

        manager._save_original_state()
        manager._replace_with_identity("swin")
        assert torch.all(model.swin(x) == 0)

        manager._restore_original_state()
        assert torch.allclose(model.swin(x), original_out)

    def test_replace_with_mean_expands_mean(self):
        model = SimpleModel()
        config = {
            "ablation": {
                "modules": ["swin"],
                "strategy": "replace_with_mean",
            }
        }
        manager = AblationManager(model, config)
        manager._save_original_state()
        manager._replace_with_mean("swin")

        x = torch.randn(4, 10)
        out = model.swin(x)
        assert out.shape == (4, 10)
        row0 = out[0]
        for i in range(1, 4):
            assert torch.allclose(out[i], row0)

        manager._restore_original_state()

    def test_run_ablation_returns_expected_structure(self):
        model = SimpleModel()
        config = {
            "ablation": {
                "modules": ["swin", "grm"],
                "strategy": "replace_with_identity",
            }
        }
        manager = AblationManager(model, config)

        class DummyLoader:
            def __iter__(self):
                for _ in range(2):
                    yield {
                        "image": torch.randn(2, 10),
                        "gis": torch.randn(2, 10),
                        "label": torch.randn(2, 1),
                    }

        class DummyLoss(nn.Module):
            def forward(self, preds, targets):
                return nn.functional.mse_loss(preds, targets)

        results = manager.run_ablation(DummyLoader(), DummyLoss(), torch.device("cpu"))
        assert "swin" in results
        assert "grm" in results
        assert "loss" in results["swin"]
        assert "baseline_loss" in results["swin"]
        assert "relative_drop_percent" in results["swin"]

    def test_save_and_restore_original_state(self):
        model = SimpleModel()
        config = {
            "ablation": {
                "modules": ["swin"],
                "strategy": "replace_with_identity",
            }
        }
        manager = AblationManager(model, config)

        original_weight = model.swin.weight.clone()
        manager._save_original_state()
        model.swin.weight.data.fill_(999.0)
        manager._restore_original_state()
        assert torch.allclose(model.swin.weight, original_weight)
```

---

### `tests/test_dataset.py`

**Purpose:** Defines `TestGCMHAIRNetDataset:` module/class.

```python
import os
import tempfile
from pathlib import Path

import numpy as np
import pytest
import torch

from datasets import GCMHAIRNetDataset


class TestGCMHAIRNetDataset:
    @pytest.fixture
    def temp_data_dir(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "images").mkdir()
            (root / "gis").mkdir()
            (root / "labels").mkdir()
            (root / "metadata").mkdir()
            splits = {"train": ["city1"], "val": ["city2"], "test": ["city3"]}
            import json
            with open(root / "splits.json", "w") as f:
                json.dump(splits, f)

            np.save(root / "images" / "city1_image.npy", np.random.rand(256, 256, 3).astype(np.float32))
            np.save(root / "gis" / "city1_gis.npy", np.random.rand(32, 32, 18).astype(np.float32))
            np.save(root / "labels" / "city1_risk.npy", np.random.rand(32, 32).astype(np.float32))
            yield str(root)

    def test_dataset_loads_train_split(self, temp_data_dir):
        dataset = GCMHAIRNetDataset(root_dir=temp_data_dir, split="train")
        assert len(dataset) == 1

    def test_dataset_loads_val_split(self, temp_data_dir):
        dataset = GCMHAIRNetDataset(root_dir=temp_data_dir, split="val")
        assert len(dataset) == 1

    def test_dataset_loads_test_split(self, temp_data_dir):
        dataset = GCMHAIRNetDataset(root_dir=temp_data_dir, split="test")
        assert len(dataset) == 1

    def test_dataset_getitem(self, temp_data_dir):
        dataset = GCMHAIRNetDataset(root_dir=temp_data_dir, split="train")
        sample = dataset[0]
        assert "image" in sample
        assert "gis" in sample
        assert "label" in sample
        assert "city_name" in sample
        assert sample["image"].shape[0] == 3
        assert sample["gis"].shape[0] == 18

    def test_invalid_split_raises(self, temp_data_dir):
        with pytest.raises(ValueError):
            GCMHAIRNetDataset(root_dir=temp_data_dir, split="invalid")
```

---

### `tests/test_gcm.py`

**Purpose:** Defines `TestSpatialDistancePrior:` module/class.

```python
import pytest
import torch

from models.gcm import (
    SpatialDistancePrior,
    FeatureSimilarityPrior,
    RoadConnectivityPrior,
    UrbanSimilarityPrior,
    LearnedRelation,
    SceneWeightPredictor,
    GeographicRelationMatrix,
    SemanticGeographicAttention,
    GCMBlock,
    GCMTransformer,
)
from models.graph_relation import GraphRelationModule


class TestSpatialDistancePrior:
    def test_output_shape(self):
        prior = SpatialDistancePrior(grid_size=16, sigma=1.0)
        D = prior(batch_size=2)
        assert D.shape == (2, 256, 256)

    def test_symmetric(self):
        prior = SpatialDistancePrior(grid_size=16, sigma=1.0)
        coords = prior.coords
        dist = torch.cdist(coords, coords, p=2)
        dist = dist / (2 * prior.sigma**2)
        D_raw = torch.exp(-dist)
        assert torch.allclose(D_raw, D_raw.T, atol=1e-5)

    def test_row_sum(self):
        prior = SpatialDistancePrior(grid_size=16, sigma=1.0)
        D = prior(batch_size=1).squeeze(0)
        row_sums = D.sum(dim=-1)
        assert torch.allclose(row_sums, torch.ones_like(row_sums), atol=1e-5)


class TestFeatureSimilarityPrior:
    def test_output_shape(self):
        prior = FeatureSimilarityPrior(feature_dim=64)
        gis_emb = torch.randn(2, 256, 64)
        S = prior(gis_emb)
        assert S.shape == (2, 256, 256)

    def test_diagonal(self):
        prior = FeatureSimilarityPrior(feature_dim=64)
        gis_emb = torch.randn(2, 256, 64)
        S = prior(gis_emb)
        diagonal = torch.diagonal(S, dim1=-2, dim2=-1)
        assert torch.allclose(diagonal, torch.ones_like(diagonal), atol=1e-5)


class TestRoadConnectivityPrior:
    def test_output_shape(self):
        prior = RoadConnectivityPrior(grid_size=16)
        gis_feat = torch.randn(2, 18, 16, 16)
        R = prior(gis_feat)
        assert R.shape == (2, 256, 256)

    def test_diagonal_zero(self):
        prior = RoadConnectivityPrior(grid_size=16)
        gis_feat = torch.randn(2, 18, 16, 16)
        R = prior(gis_feat)
        diagonal = torch.diagonal(R, dim1=-2, dim2=-1)
        assert torch.allclose(diagonal, torch.zeros_like(diagonal), atol=1e-5)


class TestUrbanSimilarityPrior:
    def test_output_shape(self):
        prior = UrbanSimilarityPrior(gis_channels=18, latent_dim=16)
        gis_feat = torch.randn(2, 18, 16, 16)
        U = prior(gis_feat)
        assert U.shape == (2, 256, 256)


class TestLearnedRelation:
    def test_output_shape(self):
        lr = LearnedRelation(embed_dim=512, rank=64)
        tokens = torch.randn(2, 256, 512)
        L = lr(tokens)
        assert L.shape == (2, 256, 256)


class TestSceneWeightPredictor:
    def test_output_shape_and_sum(self):
        swp = SceneWeightPredictor(gis_channels=18, hidden_dim=64, scene_hidden=32, output_dim=5)
        gis_feat = torch.randn(2, 18, 32, 32)
        weights = swp(gis_feat)
        assert weights.shape == (2, 5)
        assert torch.allclose(weights.sum(dim=-1), torch.ones(2), atol=1e-5)


class TestGeographicRelationMatrix:
    def test_output_shape(self):
        grm = GeographicRelationMatrix(
            embed_dim=512,
            gis_channels=18,
            gis_feature_dim=64,
            grid_size=16,
            enable_scene_weights=True,
        )
        tokens = torch.randn(2, 256, 512)
        gis_features = torch.randn(2, 18, 16, 16)
        gis_embeddings = torch.randn(2, 256, 64)
        G, priors = grm(tokens, gis_features, gis_embeddings)
        assert G.shape == (2, 256, 256)
        assert "grg" in priors
        assert "scene_weights" in priors

    def test_ablation_flags(self):
        grm = GeographicRelationMatrix(
            embed_dim=512,
            gis_channels=18,
            gis_feature_dim=64,
            grid_size=16,
            enable_distance=False,
            enable_similarity=False,
            enable_road=False,
            enable_urban=False,
            enable_learned=False,
            enable_scene_weights=False,
        )
        tokens = torch.randn(2, 256, 512)
        gis_features = torch.randn(2, 18, 32, 32)
        G, priors = grm(tokens, gis_features)
        assert G.shape == (2, 256, 256)


class TestSemanticGeographicAttention:
    def test_output_shape(self):
        attn = SemanticGeographicAttention(embed_dim=512, num_heads=8, num_semantic_heads=5)
        x = torch.randn(2, 256, 512)
        grg = torch.randn(2, 256, 256)
        priors = {
            "distance": torch.randn(2, 256, 256),
            "similarity": torch.randn(2, 256, 256),
            "road": torch.randn(2, 256, 256),
            "urban": torch.randn(2, 256, 256),
            "learned": torch.randn(2, 256, 256),
            "grg": grg,
        }
        out, maps = attn(x, grg, priors)
        assert out.shape == (2, 256, 512)
        assert len(maps) == 5


class TestGCMBlock:
    def test_output_shape(self):
        block = GCMBlock({
            "embed_dim": 512,
            "num_heads": 8,
            "num_blocks": 2,
            "num_semantic_heads": 5,
            "mlp_ratio": 4.0,
            "dropout": 0.1,
            "gate_init": 0.1,
            "gis_channels": 18,
            "gis_feature_dim": 64,
            "grid_size": 16,
            "sigma_distance": 1.0,
            "scene_weight_hidden": 32,
            "enable_distance": True,
            "enable_similarity": True,
            "enable_road": True,
            "enable_urban": True,
            "enable_learned": True,
            "enable_scene_weights": True,
        })
        tokens = torch.randn(2, 256, 512)
        gis_features = torch.randn(2, 18, 16, 16)
        out, attn_maps = block(tokens, gis_features)
        assert out.shape == (2, 256, 512)

    def test_disable_modules(self):
        block = GCMBlock({
            "embed_dim": 512,
            "num_heads": 8,
            "num_blocks": 1,
            "num_semantic_heads": 5,
            "mlp_ratio": 4.0,
            "dropout": 0.1,
            "gate_init": 0.1,
            "gis_channels": 18,
            "gis_feature_dim": 64,
            "grid_size": 16,
            "sigma_distance": 1.0,
            "scene_weight_hidden": 32,
            "enable_distance": False,
            "enable_similarity": False,
            "enable_road": False,
            "enable_urban": False,
            "enable_learned": False,
            "enable_scene_weights": False,
        })
        tokens = torch.randn(2, 256, 512)
        gis_features = torch.randn(2, 18, 16, 16)
        out, _ = block(tokens, gis_features)
        assert out.shape == (2, 256, 512)


class TestGCMTransformer:
    def test_output_shape(self):
        transformer = GCMTransformer(
            embed_dim=512,
            num_heads=8,
            num_blocks=4,
            num_semantic_heads=5,
            gis_channels=18,
            gis_feature_dim=64,
            grid_size=16,
        )
        tokens = torch.randn(2, 256, 512)
        gis_features = torch.randn(2, 18, 16, 16)
        out, all_maps = transformer(tokens, gis_features)
        assert out.shape == (2, 256, 512)
        assert len(all_maps) == 4


class TestGraphRelationModule:
    def test_output_shape(self):
        module = GraphRelationModule(
            {"hidden_dim": 128, "num_relations": 4, "num_layers": 3, "dropout": 0.1}
        )
        tokens = torch.randn(2, 256, 128)
        out = module(tokens)
        assert out.shape == (2, 256, 128)

    def test_mismatch_input_raises(self):
        module = GraphRelationModule(
            {"hidden_dim": 128, "num_relations": 4, "num_layers": 2, "dropout": 0.1}
        )
        tokens = torch.randn(2, 256, 64)
        with pytest.raises(ValueError):
            module(tokens)

    def test_intermediate_features(self):
        module = GraphRelationModule(
            {"hidden_dim": 64, "num_relations": 2, "num_layers": 2, "dropout": 0.0}
        )
        tokens = torch.randn(2, 64, 64)
        feats = module.get_intermediate_features(tokens)
        assert "grm_input" in feats
        assert "grm_output" in feats
        assert feats["grm_output"].shape == (2, 64, 64)
```

---

### `tests/test_losses.py`

**Purpose:** Defines `TestLosses:` module/class.

```python
import torch

from losses import MSELoss, L1Loss, FocalLoss, CombinedLoss


class TestLosses:
    def test_mse_loss(self):
        loss_fn = MSELoss()
        preds = torch.randn(4, 1, 32, 32)
        targets = torch.randn(4, 1, 32, 32)
        loss = loss_fn(preds, targets)
        assert loss.item() > 0

    def test_l1_loss(self):
        loss_fn = L1Loss()
        preds = torch.randn(4, 1, 32, 32)
        targets = torch.randn(4, 1, 32, 32)
        loss = loss_fn(preds, targets)
        assert loss.item() > 0

    def test_focal_loss(self):
        loss_fn = FocalLoss(alpha=0.25, gamma=2.0)
        preds = torch.randn(4, 1, 32, 32)
        targets = torch.rand(4, 1, 32, 32)
        loss = loss_fn(preds, targets)
        assert loss.item() >= 0

    def test_combined_loss(self):
        loss_fn = CombinedLoss(mse_weight=1.0, l1_weight=0.1, focal_weight=0.5)
        preds = torch.randn(4, 1, 32, 32)
        targets = torch.rand(4, 1, 32, 32)
        loss = loss_fn(preds, targets)
        assert loss.item() >= 0

    def test_combined_loss_components(self):
        loss_fn = CombinedLoss()
        components = loss_fn.get_components()
        assert "mse_loss" in components
        assert "l1_loss" in components
        assert "focal_loss" in components
        assert "total_loss" in components
```

---

### `tests/test_metrics.py`

**Purpose:** Defines `TestRegressionMetrics:` module/class.

```python
import numpy as np
import pytest
import torch

from metrics import RegressionMetrics, ClassificationMetrics


class TestRegressionMetrics:
    def test_mse(self):
        preds = np.array([1.0, 2.0, 3.0])
        targets = np.array([1.0, 2.0, 3.0])
        assert RegressionMetrics.mse(preds, targets) == 0.0

    def test_mae(self):
        preds = np.array([1.0, 2.0, 3.0])
        targets = np.array([1.5, 2.5, 3.5])
        assert RegressionMetrics.mae(preds, targets) == 0.5

    def test_r2_perfect(self):
        preds = np.array([1.0, 2.0, 3.0])
        targets = np.array([1.0, 2.0, 3.0])
        assert abs(RegressionMetrics.r2(preds, targets) - 1.0) < 1e-6

    def test_r2_worse_than_mean(self):
        preds = np.array([1.0, 1.0, 1.0])
        targets = np.array([1.0, 2.0, 3.0])
        r2 = RegressionMetrics.r2(preds, targets)
        assert r2 < 0.0


class TestClassificationMetrics:
    def test_accuracy_perfect(self):
        preds = np.array([0.9, 0.1, 0.8])
        targets = np.array([1.0, 0.0, 1.0])
        assert ClassificationMetrics.accuracy(preds, targets) == 1.0

    def test_iou_perfect(self):
        preds = np.array([0.9, 0.1, 0.8])
        targets = np.array([1.0, 0.0, 1.0])
        assert ClassificationMetrics.iou(preds, targets) >= 0.99
```

---

### `tests/test_model.py`

**Purpose:** Defines `TestModelComponents:` module/class.

```python
import pytest
import torch

from models import GCMHAIRNet, SwinTransformerEncoder, GISEncoder, GatedCrossAttention, Decoder


class TestModelComponents:
    def test_swin_encoder_forward(self):
        config = {"embed_dim": 64, "depths": [2, 2, 2], "num_heads": [2, 4, 8], "pretrained": False}
        model = SwinTransformerEncoder(config)
        x = torch.randn(2, 3, 256, 256)
        out = model(x)
        assert out.shape[0] == 2
        assert out.shape[2] == 64

    def test_gis_encoder_forward(self):
        config = {"input_channels": 18, "hidden_dim": 64, "output_dim": 64, "dropout": 0.1}
        model = GISEncoder(config)
        x = torch.randn(2, 18, 32, 32)
        out = model(x)
        assert out.shape[0] == 2
        assert out.shape[2] == 64

    def test_gct_forward(self):
        config = {"hidden_dim": 64, "num_heads": 4, "dropout": 0.1}
        model = GatedCrossAttention(config)
        image_feats = torch.randn(2, 64, 64)
        gis_feats = torch.randn(2, 64, 64)
        out = model(image_feats, gis_feats)
        assert out.shape == image_feats.shape

    def test_decoder_forward(self):
        config = {"hidden_dim": 64, "num_classes": 1, "dropout": 0.1}
        model = Decoder(config)
        x = torch.randn(2, 64, 16, 16)
        out = model(x, spatial_size=(256, 256))
        assert out.shape[-2:] == (256, 256)

    def test_gcm_hairnet_forward(self):
        config = {
            "image_encoder": {"embed_dim": 64, "depths": [2, 2, 2], "num_heads": [2, 4, 8], "pretrained": False},
            "gis_encoder": {"input_channels": 18, "hidden_dim": 64, "output_dim": 64, "dropout": 0.1},
            "gct": {"hidden_dim": 64, "num_heads": 4, "dropout": 0.1},
            "grm": {"hidden_dim": 64, "num_relations": 4, "num_layers": 2, "dropout": 0.1},
            "decoder": {"hidden_dim": 64, "num_classes": 1, "dropout": 0.1},
            "image_size": 256,
            "gis_size": 32,
        }
        model = GCMHAIRNet(config)
        image = torch.randn(2, 3, 256, 256)
        gis = torch.randn(2, 18, 32, 32)
        out = model(image, gis)
        assert out.shape[-2:] == (256, 256)
        assert out.shape[0] == 2
```

---

### `utils/__init__.py`

**Purpose:** Implementation of `__init__.py`.

```python
from .ablation import AblationManager
from .checkpoint import CheckpointManager
from .config import Config, merge_configs
from .experiment import ConfigManager
from .logger import Logger
from .misc import get_device, setup_directories
from .registry import Registry, MODEL_REGISTRY, LOSS_REGISTRY, METRIC_REGISTRY
from .seed import count_parameters, set_seed

__all__ = [
    "AblationManager",
    "CheckpointManager",
    "Config",
    "ConfigManager",
    "Logger",
    "get_device",
    "setup_directories",
    "Registry",
    "MODEL_REGISTRY",
    "LOSS_REGISTRY",
    "METRIC_REGISTRY",
    "count_parameters",
    "set_seed",
    "merge_configs",
]
```

---

### `utils/ablation.py`

**Purpose:** Defines `AblationManager:` module/class.

```python
import random
from typing import Any, Dict, List, Optional

import numpy as np
import torch
from torch.utils.data import DataLoader, Subset

from datasets.base import GCMHAIRNetDataset


class AblationManager:
    def __init__(self, model: torch.nn.Module, config: Dict[str, Any]):
        self.model = model
        self.config = config
        self.modules_to_ablate = config.get("ablation", {}).get("modules", [])
        self.strategy = config.get("ablation", {}).get("strategy", "replace_with_identity")
        self.original_state = None
        self.original_forwards = {}

    def _save_original_state(self):
        self.original_state = {k: v.clone() for k, v in self.model.state_dict().items()}

    def _restore_original_state(self):
        if self.original_state:
            self.model.load_state_dict(self.original_state)
            self.original_state = None
        for module_name, original_forward in self.original_forwards.items():
            module = self.model
            for attr in module_name.split("."):
                if hasattr(module, attr):
                    module = getattr(module, attr)
                else:
                    break
            if hasattr(module, "forward"):
                module.forward = original_forward
        self.original_forwards = {}

    def _get_module(self, module_name: str):
        module = self.model
        for attr in module_name.split("."):
            if hasattr(module, attr):
                module = getattr(module, attr)
            else:
                return None
        return module

    def _replace_with_identity(self, module_name: str):
        module = self._get_module(module_name)
        if module is None or not hasattr(module, "forward"):
            return
        if module_name not in self.original_forwards:
            self.original_forwards[module_name] = module.forward

        def identity_forward(*args, **kwargs):
            if len(args) > 0 and isinstance(args[0], torch.Tensor):
                return torch.zeros_like(args[0])
            original = self.original_forwards.get(module_name, module.forward)
            return original(*args, **kwargs)

        module.forward = identity_forward

    def _replace_with_mean(self, module_name: str):
        module = self._get_module(module_name)
        if module is None or not hasattr(module, "forward"):
            return
        if module_name not in self.original_forwards:
            self.original_forwards[module_name] = module.forward

        def mean_forward(*args, **kwargs):
            result = self.original_forwards[module_name](*args, **kwargs)
            if isinstance(result, torch.Tensor):
                return result.mean(dim=0, keepdim=True).expand_as(result)
            return result

        module.forward = mean_forward

    def _apply_strategy(self, module_name: str):
        if self.strategy == "replace_with_identity":
            self._replace_with_identity(module_name)
        elif self.strategy == "replace_with_mean":
            self._replace_with_mean(module_name)

    def _evaluate(self, val_loader: DataLoader, loss_fn: torch.nn.Module, device: torch.device) -> float:
        total_loss = 0.0
        num_batches = 0
        self.model.eval()
        with torch.no_grad():
            for batch in val_loader:
                image = batch["image"].to(device)
                gis = batch["gis"].to(device)
                label = batch["label"].to(device)
                preds = self.model(image, gis)
                loss = loss_fn(preds, label)
                total_loss += loss.item()
                num_batches += 1
        return total_loss / max(num_batches, 1)

    def run_ablation(self, val_loader: DataLoader, loss_fn: torch.nn.Module, device: torch.device) -> Dict[str, Any]:
        results = {}
        self._save_original_state()

        baseline_loss = self._evaluate(val_loader, loss_fn, device)

        for module_name in self.modules_to_ablate:
            self._restore_original_state()
            self._apply_strategy(module_name)

            ablated_loss = self._evaluate(val_loader, loss_fn, device)
            relative_drop = ((baseline_loss - ablated_loss) / baseline_loss) * 100.0 if baseline_loss > 0 else 0.0

            results[module_name] = {
                "loss": ablated_loss,
                "baseline_loss": baseline_loss,
                "relative_drop_percent": relative_drop,
            }

        self._restore_original_state()
        return results
```

---

### `utils/checkpoint.py`

**Purpose:** Defines `CheckpointManager:` module/class.

```python
import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

import torch


class CheckpointManager:
    def __init__(self, checkpoint_dir: str, monitor: str = "val_loss", mode: str = "min", save_top_k: int = 5, save_last: bool = True, every_n_epochs: int = 1):
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        self.monitor = monitor
        self.mode = mode
        self.save_top_k = save_top_k
        self.save_last = save_last
        self.every_n_epochs = every_n_epochs
        self.best_value = float("inf") if mode == "min" else float("-inf")
        self.top_k_checkpoints: list = []
        self.last_checkpoint: Optional[str] = None

    def _is_better(self, current: float) -> bool:
        if self.mode == "min":
            return current < self.best_value
        return current > self.best_value

    def _cleanup_old_checkpoints(self, keep_epoch: int):
        epoch_files = sorted(self.checkpoint_dir.glob("epoch_*.pt"))
        keep_paths = {str(self.checkpoint_dir / f"epoch_{keep_epoch:04d}.pt")}
        for path_str, _ in self.top_k_checkpoints:
            keep_paths.add(path_str)
        if self.last_checkpoint:
            keep_paths.add(self.last_checkpoint)
        for path in epoch_files:
            if str(path) not in keep_paths:
                try:
                    path.unlink()
                except OSError:
                    pass

    def _cpu_state(self, state):
        if isinstance(state, torch.Tensor):
            return state.detach().cpu()
        if isinstance(state, dict):
            return {k: self._cpu_state(v) for k, v in state.items()}
        if isinstance(state, (list, tuple)):
            return type(state)(self._cpu_state(v) for v in state)
        return state

    def save(self, state: Dict[str, Any], epoch: int, metrics: Dict[str, float]) -> str:
        saved_path = None
        cpu_state = self._cpu_state(state)

        if self.save_last:
            last_path = self.checkpoint_dir / "last.pt"
            try:
                torch.save(cpu_state, last_path, _use_new_zipfile_serialization=False)
                self.last_checkpoint = str(last_path)
                saved_path = str(last_path)
            except OSError as e:
                print(f"Warning: Could not save last.pt: {e}")

        if self.monitor in metrics:
            current = metrics[self.monitor]
            if self._is_better(current):
                self.best_value = current
                best_path = self.checkpoint_dir / "best.pt"
                try:
                    torch.save(cpu_state, best_path, _use_new_zipfile_serialization=False)
                    self.top_k_checkpoints.append((str(best_path), current))
                    self.top_k_checkpoints = sorted(self.top_k_checkpoints, key=lambda x: x[1], reverse=(self.mode == "max"))[:self.save_top_k]
                    saved_path = str(best_path)
                except OSError as e:
                    print(f"Warning: Could not save best.pt: {e}")

        if epoch % self.every_n_epochs == 0:
            epoch_path = self.checkpoint_dir / f"epoch_{epoch:04d}.pt"
            try:
                torch.save(cpu_state, epoch_path, _use_new_zipfile_serialization=False)
                saved_path = str(epoch_path)
                self._cleanup_old_checkpoints(epoch)
            except OSError as e:
                print(f"Warning: Could not save epoch checkpoint: {e}")

        return saved_path or self.last_checkpoint or ""

    def load(self, path: str, model: torch.nn.Module, optimizer: Optional[torch.optim.Optimizer] = None, device: Optional[torch.device] = None):
        checkpoint = torch.load(path, map_location=device or "cpu")
        ckpt_state = checkpoint["model_state_dict"]
        model_state = model.state_dict()

        new_state = {}
        matched = 0
        skipped = 0
        for key, param in ckpt_state.items():
            if key in model_state:
                if param.shape == model_state[key].shape:
                    new_state[key] = param
                    matched += 1
                else:
                    skipped += 1
            else:
                skipped += 1

        result = model.load_state_dict(new_state, strict=False)
        if result.missing_keys or result.unexpected_keys:
            print(f"Warning: Partial checkpoint load - missing: {result.missing_keys}, unexpected: {result.unexpected_keys}")
        if skipped > 0:
            print(f"Info: Loaded {matched} layers, skipped {skipped} incompatible layers from checkpoint")
        if optimizer and "optimizer_state_dict" in checkpoint:
            try:
                optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
            except Exception as e:
                print(f"Warning: Could not load optimizer state: {e}")
        return checkpoint.get("epoch", 0), checkpoint.get("metrics", {})

    def get_last_checkpoint(self) -> Optional[str]:
        return self.last_checkpoint
```

---

### `utils/config.py`

**Purpose:** Defines `Config:` module/class.

```python
import os
from pathlib import Path
from typing import Any, Dict, Optional

import yaml


class Config:
    def __init__(self, config_dict: Optional[Dict[str, Any]] = None, config_path: Optional[str] = None):
        if config_dict is not None:
            self._config = config_dict
        elif config_path is not None:
            self._config = self._load_yaml(config_path)
        else:
            raise ValueError("Either config_dict or config_path must be provided")

    def _load_yaml(self, path: str) -> Dict[str, Any]:
        with open(path, "r") as f:
            return yaml.safe_load(f) or {}

    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split(".")
        value = self._config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value

    def __getitem__(self, key: str) -> Any:
        return self.get(key)

    def __setitem__(self, key: str, value: Any) -> None:
        keys = key.split(".")
        config = self._config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value

    def to_dict(self) -> Dict[str, Any]:
        return self._config

    def save(self, path: str) -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            yaml.dump(self._config, f, default_flow_style=False, sort_keys=False)


def merge_configs(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    result = dict(base)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_configs(result[key], value)
        else:
            result[key] = value
    return result
```

---

### `utils/experiment.py`

**Purpose:** Defines `ConfigManager:` module/class.

```python
import os
from pathlib import Path
from typing import Any, Dict, Optional

import yaml

from .config import Config, merge_configs


class ConfigManager:
    def __init__(self, root_dir: Optional[str] = None):
        self.root_dir = Path(root_dir) if root_dir else Path.cwd()
        self.configs_dir = self.root_dir / "configs"

    def load(self, config_name: str, overrides: Optional[Dict[str, Any]] = None) -> Config:
        config_path = self.configs_dir / f"{config_name}.yaml"
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")
        config = Config(config_path=str(config_path))
        if overrides:
            merged = merge_configs(config.to_dict(), overrides)
            config = Config(config_dict=merged)
        return config

    def load_defaults(self, overrides: Optional[Dict[str, Any]] = None) -> Config:
        return self.load("default", overrides)
```

---

### `utils/logger.py`

**Purpose:** Defines `Logger:` module/class.

```python
import os
from pathlib import Path
from typing import Any, Dict, Optional

import torch
from torch.utils.tensorboard import SummaryWriter


class Logger:
    def __init__(self, log_dir: str, experiment_name: str, use_tensorboard: bool = True, use_wandb: bool = False, config: Optional[Dict[str, Any]] = None):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.experiment_name = experiment_name
        self.writer: Optional[SummaryWriter] = None
        self.use_wandb = use_wandb

        if use_tensorboard:
            self.writer = SummaryWriter(log_dir=str(self.log_dir / experiment_name))

        if use_wandb:
            try:
                import wandb
                wandb.init(project=experiment_name, config=config)
                self.wandb = wandb
            except ImportError:
                self.use_wandb = False

    def log_metrics(self, metrics: Dict[str, float], step: int, prefix: str = "") -> None:
        for key, value in metrics.items():
            tag = f"{prefix}/{key}" if prefix else key
            if self.writer:
                self.writer.add_scalar(tag, value, step)
            if self.use_wandb:
                self.wandb.log({tag: value}, step=step)

    def log_images(self, images: Dict[str, Any], step: int, prefix: str = "") -> None:
        for key, value in images.items():
            tag = f"{prefix}/{key}" if prefix else key
            if self.writer:
                if isinstance(value, torch.Tensor):
                    self.writer.add_images(tag, value, step, dataformats="NCHW")
            if self.use_wandb:
                if isinstance(value, torch.Tensor):
                    self.wandb.log({tag: [self.wandb.Image(v.cpu().numpy().transpose(1, 2, 0)) for v in value]}, step=step)

    def log_config(self, config: Dict[str, Any]) -> None:
        if self.writer:
            self.writer.add_text("config", str(config))
        if self.use_wandb:
            self.wandb.config.update(config)

    def close(self) -> None:
        if self.writer:
            self.writer.close()
        if self.use_wandb:
            self.wandb.finish()
```

---

### `utils/misc.py`

**Purpose:** Contains `setup_directories` function.

```python
import os
from pathlib import Path
from typing import Any, Dict, Optional

import torch


def setup_directories(root_dir: str, create_subdirs: bool = True) -> Dict[str, Path]:
    root = Path(root_dir)
    dirs = {
        "root": root,
        "outputs": root / "outputs",
        "logs": root / "logs",
        "checkpoints": root / "checkpoints",
    }
    if create_subdirs:
        for d in dirs.values():
            d.mkdir(parents=True, exist_ok=True)
    return dirs


def get_device(device: Optional[str] = None) -> torch.device:
    if device:
        return torch.device(device)
    if torch.backends.mps.is_available():
        return torch.device("mps")
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")
```

---

### `utils/registry.py`

**Purpose:** Defines `Registry:` module/class.

```python
from typing import Any, Dict, Optional


class Registry:
    _instances: Dict[str, "Registry"] = {}

    def __init__(self, name: str):
        self.name = name
        self._registry: Dict[str, Any] = {}

    @classmethod
    def get(cls, name: str) -> Optional["Registry"]:
        return cls._instances.get(name)

    @classmethod
    def register(cls, name: str) -> "Registry":
        if name not in cls._instances:
            cls._instances[name] = Registry(name)
        return cls._instances[name]

    def add(self, key: str, value: Any) -> None:
        self._registry[key] = value

    def get_item(self, key: str, default: Any = None) -> Any:
        return self._registry.get(key, default)

    def keys(self) -> list:
        return list(self._registry.keys())

    def __contains__(self, key: str) -> bool:
        return key in self._registry


MODEL_REGISTRY = Registry.register("model")
LOSS_REGISTRY = Registry.register("loss")
METRIC_REGISTRY = Registry.register("metric")
```

---

### `utils/seed.py`

**Purpose:** Contains `set_seed` function.

```python
import os
import random
from typing import Dict, Optional

import numpy as np
import torch


def set_seed(seed: int, deterministic: bool = True) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    if deterministic:
        if torch.cuda.is_available():
            torch.backends.cudnn.deterministic = True
            torch.backends.cudnn.benchmark = False
            os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
        if torch.backends.mps.is_available():
            torch.backends.mps.deterministic = True


def count_parameters(model: torch.nn.Module) -> Dict[str, int]:
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    return {"total": total, "trainable": trainable}
```

---

### `visualization/__init__.py`

**Purpose:** Implementation of `__init__.py`.

```python
from .plots import save_prediction_plots, plot_prediction_vs_target
from .attention import plot_attention_map, save_attention_maps
from .grm import plot_grm_relations, plot_graph_embeddings
from .risk_maps import plot_risk_map, save_risk_maps, save_comparison_maps
from .feature_maps import plot_feature_map, save_feature_maps
from .training import plot_training_curves, save_training_summary
from .gcm_visualization import save_gcm_priors, save_attention_maps as save_gcm_attention_maps, save_scene_weights

__all__ = [
    "save_prediction_plots",
    "plot_prediction_vs_target",
    "plot_attention_map",
    "save_attention_maps",
    "plot_grm_relations",
    "plot_graph_embeddings",
    "plot_risk_map",
    "save_risk_maps",
    "save_comparison_maps",
    "plot_feature_map",
    "save_feature_maps",
    "plot_training_curves",
    "save_training_summary",
    "save_gcm_priors",
    "save_gcm_attention_maps",
    "save_scene_weights",
]
```

---

### `visualization/attention.py`

**Purpose:** Contains `plot_attention_map` function.

```python
from typing import Any, Dict, List, Optional

import numpy as np
import torch


def plot_attention_map(
    attention_weights: torch.Tensor,
    save_path: Optional[str] = None,
    title: str = "Attention Map",
    cmap: str = "viridis",
):
    try:
        import matplotlib.pyplot as plt

        attn = attention_weights.detach().cpu().numpy().squeeze()
        fig, ax = plt.subplots(figsize=(10, 8))
        im = ax.imshow(attn, cmap=cmap)
        ax.set_title(title)
        plt.colorbar(im, ax=ax)

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass


def save_attention_maps(
    attention_weights: np.ndarray,
    layer_names: List[str],
    output_dir: str,
) -> None:
    from pathlib import Path
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    try:
        import matplotlib.pyplot as plt

        for i, attn in enumerate(attention_weights):
            layer = layer_names[i] if i < len(layer_names) else f"layer_{i}"
            fig, ax = plt.subplots(figsize=(10, 8))
            im = ax.imshow(attn.squeeze(), cmap="viridis")
            ax.set_title(f"Attention: {layer}")
            plt.colorbar(im, ax=ax)
            fig.savefig(output_path / f"{layer}_attention.png")
            plt.close(fig)
    except ImportError:
        pass
```

---

### `visualization/dashboard.py`

**Purpose:** Defines `ExperimentManager:` module/class.

```python
from pathlib import Path
from typing import Any, Dict, List, Optional


class ExperimentManager:
    def __init__(self, config: Any, root_dir: str = "./outputs"):
        self.config = config
        self.root_dir = root_dir
        self.experiment_name = config.get("experiment", {}).get("name", "experiment")
        self.run_dir = self._create_run_dir()

    def _create_run_dir(self) -> str:
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        run_name = f"{self.experiment_name}_{timestamp}"
        run_dir = str(Path(self.root_dir) / run_name)
        return run_dir

    def get_output_dir(self, subdir: str = "") -> str:
        output_dir = Path(self.run_dir) / subdir
        output_dir.mkdir(parents=True, exist_ok=True)
        return str(output_dir)

    def save_config(self, config: Dict[str, Any]) -> str:
        import yaml
        config_path = Path(self.run_dir) / "config.yaml"
        with open(config_path, "w") as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)
        return str(config_path)

    def log_metric(self, name: str, value: float, step: int) -> None:
        import json
        metrics_file = Path(self.run_dir) / "metrics.json"
        metrics = {}
        if metrics_file.exists():
            with open(metrics_file, "r") as f:
                metrics = json.load(f)
        if name not in metrics:
            metrics[name] = []
        metrics[name].append({"step": step, "value": value})
        with open(metrics_file, "w") as f:
            json.dump(metrics, f, indent=2)
```

---

### `visualization/feature_maps.py`

**Purpose:** Contains `plot_feature_map` function.

```python
from typing import Any, Dict, List, Optional

import numpy as np
import torch


def plot_feature_map(
    feature_map: torch.Tensor,
    save_path: Optional[str] = None,
    title: str = "Feature Map",
    cmap: str = "viridis",
    num_channels: int = 8,
):
    try:
        import matplotlib.pyplot as plt

        feat = feature_map.detach().cpu().numpy().squeeze()
        if feat.ndim == 2:
            feat = feat[np.newaxis, ...]

        num_channels = min(num_channels, feat.shape[0])
        fig, axes = plt.subplots(1, num_channels, figsize=(4 * num_channels, 4))
        if num_channels == 1:
            axes = [axes]

        for i in range(num_channels):
            im = axes[i].imshow(feat[i], cmap=cmap)
            axes[i].set_title(f"Channel {i}")
            axes[i].axis("off")
            plt.colorbar(im, ax=axes[i])

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass


def save_feature_maps(
    feature_maps: Dict[str, torch.Tensor],
    output_dir: str,
    max_channels: int = 8,
) -> None:
    from pathlib import Path
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for name, feat in feature_maps.items():
        plot_feature_map(feat, save_path=str(output_path / f"{name}_feature_map.png"), title=name, num_channels=max_channels)
```

---

### `visualization/gcm_visualization.py`

**Purpose:** Contains `save_gcm_priors` function.

```python
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np
import torch


def save_gcm_priors(
    priors: Dict[str, torch.Tensor],
    output_dir: str,
    epoch: int = 0,
) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if not _matplotlib_available():
        return

    try:
        import matplotlib.pyplot as plt

        for name, prior in priors.items():
            if prior is None:
                continue
            prior_np = prior.detach().cpu().numpy()
            if prior_np.ndim == 3:
                prior_np = prior_np[0]
            fig, ax = plt.subplots(figsize=(8, 6))
            im = ax.imshow(prior_np, cmap="viridis")
            ax.set_title(f"{name} Prior (epoch {epoch})")
            plt.colorbar(im, ax=ax)
            fig.savefig(output_path / f"epoch_{epoch:04d}_{name}_prior.png")
            plt.close(fig)
    except ImportError:
        pass


def save_attention_maps(
    attention_maps: List[Dict[str, torch.Tensor]],
    output_dir: str,
    epoch: int = 0,
) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if not _matplotlib_available():
        return

    try:
        import matplotlib.pyplot as plt

        for block_idx, block_maps in enumerate(attention_maps):
            for head_name, attn in block_maps.items():
                attn_np = attn.detach().cpu().numpy()
                if attn_np.ndim == 3:
                    attn_np = attn_np[0]
                fig, ax = plt.subplots(figsize=(8, 6))
                im = ax.imshow(attn_np, cmap="hot")
                ax.set_title(f"Block {block_idx} {head_name} (epoch {epoch})")
                plt.colorbar(im, ax=ax)
                fig.savefig(output_path / f"epoch_{epoch:04d}_block_{block_idx}_{head_name}.png")
                plt.close(fig)
    except ImportError:
        pass


def save_scene_weights(
    scene_weights: torch.Tensor,
    output_dir: str,
    epoch: int = 0,
) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if not _matplotlib_available():
        return

    try:
        import matplotlib.pyplot as plt

        weights_np = scene_weights.detach().cpu().numpy()
        labels = ["Distance", "Similarity", "Road", "Urban", "Learned"]

        fig, ax = plt.subplots(figsize=(10, 6))
        for i in range(min(5, weights_np.shape[-1])):
            ax.plot(weights_np[:, i], label=labels[i])
        ax.set_xlabel("Sample")
        ax.set_ylabel("Weight")
        ax.set_title(f"Scene Weights (epoch {epoch})")
        ax.legend()
        ax.grid(True)
        fig.savefig(output_path / f"epoch_{epoch:04d}_scene_weights.png")
        plt.close(fig)
    except ImportError:
        pass


def _matplotlib_available() -> bool:
    try:
        import matplotlib  # noqa: F401
        return True
    except ImportError:
        return False
```

---

### `visualization/grm.py`

**Purpose:** Contains `plot_grm_relations` function.

```python
from typing import Any, Dict, List, Optional

import numpy as np
import torch


def plot_grm_relations(
    relation_weights: torch.Tensor,
    save_path: Optional[str] = None,
    title: str = "GRM Relations",
):
    try:
        import matplotlib.pyplot as plt

        weights = relation_weights.detach().cpu().numpy()
        num_relations = weights.shape[0]
        fig, axes = plt.subplots(1, num_relations, figsize=(5 * num_relations, 4))
        if num_relations == 1:
            axes = [axes]

        for i in range(num_relations):
            im = axes[i].imshow(weights[i], cmap="coolwarm")
            axes[i].set_title(f"Relation {i}")
            plt.colorbar(im, ax=axes[i])

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass


def plot_graph_embeddings(
    embeddings: torch.Tensor,
    labels: Optional[np.ndarray] = None,
    save_path: Optional[str] = None,
    title: str = "Graph Embeddings",
):
    try:
        import matplotlib.pyplot as plt

        emb = embeddings.detach().cpu().numpy()
        if emb.shape[1] > 2:
            from sklearn.decomposition import PCA
            emb = PCA(n_components=2).fit_transform(emb)

        fig, ax = plt.subplots(figsize=(8, 6))
        if labels is not None:
            scatter = ax.scatter(emb[:, 0], emb[:, 1], c=labels, cmap="tab10")
            plt.colorbar(scatter, ax=ax)
        else:
            ax.scatter(emb[:, 0], emb[:, 1])
        ax.set_title(title)

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass
```

---

### `visualization/maps.py`

**Purpose:** Contains `save_risk_maps` function.

```python
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np
import torch


def save_risk_maps(
    predictions: np.ndarray,
    city_names: List[str],
    output_dir: str,
    cmap: str = "hot",
) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for pred, city in zip(predictions, city_names):
        if pred.ndim == 3:
            pred = pred.squeeze()
        np.save(output_path / f"{city}_risk_map.npy", pred)

        if _matplotlib_available():
            try:
                import matplotlib.pyplot as plt

                fig, ax = plt.subplots(figsize=(8, 8))
                im = ax.imshow(pred, cmap=cmap)
                ax.set_title(f"Risk Map: {city}")
                plt.colorbar(im, ax=ax)
                fig.savefig(output_path / f"{city}_risk_map.png")
                plt.close(fig)
            except ImportError:
                pass


def save_comparison_maps(
    predictions: np.ndarray,
    targets: np.ndarray,
    city_names: List[str],
    output_dir: str,
) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if not _matplotlib_available():
        return

    try:
        import matplotlib.pyplot as plt

        for pred, target, city in zip(predictions, targets, city_names):
            if pred.ndim == 3:
                pred = pred.squeeze()
            if target.ndim == 3:
                target = target.squeeze()

            fig, axes = plt.subplots(1, 3, figsize=(15, 5))
            axes[0].imshow(target, cmap="hot")
            axes[0].set_title(f"Ground Truth: {city}")
            axes[0].axis("off")

            axes[1].imshow(pred, cmap="hot")
            axes[1].set_title(f"Prediction: {city}")
            axes[1].axis("off")

            diff = np.abs(target - pred)
            axes[2].imshow(diff, cmap="viridis")
            axes[2].set_title(f"Absolute Error: {city}")
            axes[2].axis("off")

            fig.savefig(output_path / f"{city}_comparison.png")
            plt.close(fig)
    except ImportError:
        pass


def _matplotlib_available() -> bool:
    try:
        import matplotlib  # noqa: F401
        return True
    except ImportError:
        return False
```

---

### `visualization/plots.py`

**Purpose:** Contains `save_prediction_plots` function.

```python
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np
import torch


def save_prediction_plots(predictions: np.ndarray, metadata: List[Dict], output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for i, pred in enumerate(predictions):
        city = metadata[i].get("city_name", f"sample_{i}")
        np.save(output_path / f"{city}_prediction.npy", pred)


def plot_prediction_vs_target(
    preds: torch.Tensor,
    targets: torch.Tensor,
    save_path: Optional[str] = None,
    title: str = "Predictions vs Targets",
):
    try:
        import matplotlib.pyplot as plt

        preds = preds.detach().cpu().numpy().flatten()
        targets = targets.detach().cpu().numpy().flatten()

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(targets, preds, alpha=0.5)
        ax.plot([targets.min(), targets.max()], [targets.min(), targets.max()], "r--")
        ax.set_xlabel("Targets")
        ax.set_ylabel("Predictions")
        ax.set_title(title)

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass


def plot_risk_map(
    risk_map: torch.Tensor,
    save_path: Optional[str] = None,
    title: str = "Risk Map",
    cmap: str = "hot",
):
    try:
        import matplotlib.pyplot as plt

        risk_map = risk_map.detach().cpu().numpy().squeeze()
        fig, ax = plt.subplots(figsize=(8, 8))
        im = ax.imshow(risk_map, cmap=cmap)
        ax.set_title(title)
        plt.colorbar(im, ax=ax)

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass


def plot_attention_map(
    attention_weights: torch.Tensor,
    save_path: Optional[str] = None,
    title: str = "Attention Map",
    cmap: str = "viridis",
):
    try:
        import matplotlib.pyplot as plt

        attn = attention_weights.detach().cpu().numpy().squeeze()
        fig, ax = plt.subplots(figsize=(10, 8))
        im = ax.imshow(attn, cmap=cmap)
        ax.set_title(title)
        plt.colorbar(im, ax=ax)

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass
```

---

### `visualization/risk_maps.py`

**Purpose:** Contains `plot_risk_map` function.

```python
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np
import torch


def plot_risk_map(
    risk_map: torch.Tensor,
    save_path: Optional[str] = None,
    title: str = "Risk Map",
    cmap: str = "hot",
):
    try:
        import matplotlib.pyplot as plt

        risk_map = risk_map.detach().cpu().numpy().squeeze()
        fig, ax = plt.subplots(figsize=(8, 8))
        im = ax.imshow(risk_map, cmap=cmap)
        ax.set_title(title)
        plt.colorbar(im, ax=ax)

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass


def save_risk_maps(
    predictions: np.ndarray,
    city_names: List[str],
    output_dir: str,
    cmap: str = "hot",
) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for pred, city in zip(predictions, city_names):
        if pred.ndim == 3:
            pred = pred.squeeze()
        np.save(output_path / f"{city}_risk_map.npy", pred)

        if _matplotlib_available():
            try:
                import matplotlib.pyplot as plt

                fig, ax = plt.subplots(figsize=(8, 8))
                im = ax.imshow(pred, cmap=cmap)
                ax.set_title(f"Risk Map: {city}")
                plt.colorbar(im, ax=ax)
                fig.savefig(output_path / f"{city}_risk_map.png")
                plt.close(fig)
            except ImportError:
                pass


def save_comparison_maps(
    predictions: np.ndarray,
    targets: np.ndarray,
    city_names: List[str],
    output_dir: str,
) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if not _matplotlib_available():
        return

    try:
        import matplotlib.pyplot as plt

        for pred, target, city in zip(predictions, targets, city_names):
            if pred.ndim == 3:
                pred = pred.squeeze()
            if target.ndim == 3:
                target = target.squeeze()

            fig, axes = plt.subplots(1, 3, figsize=(15, 5))
            axes[0].imshow(target, cmap="hot")
            axes[0].set_title(f"Ground Truth: {city}")
            axes[0].axis("off")

            axes[1].imshow(pred, cmap="hot")
            axes[1].set_title(f"Prediction: {city}")
            axes[1].axis("off")

            diff = np.abs(target - pred)
            axes[2].imshow(diff, cmap="viridis")
            axes[2].set_title(f"Absolute Error: {city}")
            axes[2].axis("off")

            fig.savefig(output_path / f"{city}_comparison.png")
            plt.close(fig)
    except ImportError:
        pass


def _matplotlib_available() -> bool:
    try:
        import matplotlib  # noqa: F401
        return True
    except ImportError:
        return False
```

---

### `visualization/training.py`

**Purpose:** Contains `plot_training_curves` function.

```python
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np


def plot_training_curves(
    metrics: Dict[str, List[float]],
    save_path: Optional[str] = None,
    title: str = "Training Curves",
):
    try:
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(10, 6))
        for name, values in metrics.items():
            ax.plot(values, label=name)
        ax.set_xlabel("Step/Epoch")
        ax.set_ylabel("Value")
        ax.set_title(title)
        ax.legend()
        ax.grid(True)

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass


def save_training_summary(
    metrics: Dict[str, List[float]],
    output_dir: str,
    experiment_name: str = "experiment",
) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    plot_training_curves(
        metrics,
        save_path=str(output_path / f"{experiment_name}_curves.png"),
        title=experiment_name,
    )
```

---
