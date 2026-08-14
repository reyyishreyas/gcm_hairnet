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
