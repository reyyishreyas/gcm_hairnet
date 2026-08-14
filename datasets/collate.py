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
