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



