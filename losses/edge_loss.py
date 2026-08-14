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
