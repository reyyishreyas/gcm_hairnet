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
