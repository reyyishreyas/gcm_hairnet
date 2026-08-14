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
