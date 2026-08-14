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
