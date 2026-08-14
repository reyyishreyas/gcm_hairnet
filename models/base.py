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
