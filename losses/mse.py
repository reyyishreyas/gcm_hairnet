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
