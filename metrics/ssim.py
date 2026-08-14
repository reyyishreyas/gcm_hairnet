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
