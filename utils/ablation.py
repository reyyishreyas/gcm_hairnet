import random
from typing import Any, Dict, List, Optional

import numpy as np
import torch
from torch.utils.data import DataLoader, Subset

from datasets.base import GCMHAIRNetDataset


class AblationManager:
    def __init__(self, model: torch.nn.Module, config: Dict[str, Any]):
        self.model = model
        self.config = config
        self.modules_to_ablate = config.get("ablation", {}).get("modules", [])
        self.strategy = config.get("ablation", {}).get("strategy", "replace_with_identity")
        self.original_state = None
        self.original_forwards = {}

    def _save_original_state(self):
        self.original_state = {k: v.clone() for k, v in self.model.state_dict().items()}

    def _restore_original_state(self):
        if self.original_state:
            self.model.load_state_dict(self.original_state)
            self.original_state = None
        for module_name, original_forward in self.original_forwards.items():
            module = self.model
            for attr in module_name.split("."):
                if hasattr(module, attr):
                    module = getattr(module, attr)
                else:
                    break
            if hasattr(module, "forward"):
                module.forward = original_forward
        self.original_forwards = {}

    def _get_module(self, module_name: str):
        module = self.model
        for attr in module_name.split("."):
            if hasattr(module, attr):
                module = getattr(module, attr)
            else:
                return None
        return module

    def _replace_with_identity(self, module_name: str):
        module = self._get_module(module_name)
        if module is None or not hasattr(module, "forward"):
            return
        if module_name not in self.original_forwards:
            self.original_forwards[module_name] = module.forward

        def identity_forward(*args, **kwargs):
            if len(args) > 0 and isinstance(args[0], torch.Tensor):
                return torch.zeros_like(args[0])
            original = self.original_forwards.get(module_name, module.forward)
            return original(*args, **kwargs)

        module.forward = identity_forward

    def _replace_with_mean(self, module_name: str):
        module = self._get_module(module_name)
        if module is None or not hasattr(module, "forward"):
            return
        if module_name not in self.original_forwards:
            self.original_forwards[module_name] = module.forward

        def mean_forward(*args, **kwargs):
            result = self.original_forwards[module_name](*args, **kwargs)
            if isinstance(result, torch.Tensor):
                return result.mean(dim=0, keepdim=True).expand_as(result)
            return result

        module.forward = mean_forward

    def _apply_strategy(self, module_name: str):
        if self.strategy == "replace_with_identity":
            self._replace_with_identity(module_name)
        elif self.strategy == "replace_with_mean":
            self._replace_with_mean(module_name)

    def _evaluate(self, val_loader: DataLoader, loss_fn: torch.nn.Module, device: torch.device) -> float:
        total_loss = 0.0
        num_batches = 0
        self.model.eval()
        with torch.no_grad():
            for batch in val_loader:
                image = batch["image"].to(device)
                gis = batch["gis"].to(device)
                label = batch["label"].to(device)
                preds = self.model(image, gis)
                loss = loss_fn(preds, label)
                total_loss += loss.item()
                num_batches += 1
        return total_loss / max(num_batches, 1)

    def run_ablation(self, val_loader: DataLoader, loss_fn: torch.nn.Module, device: torch.device) -> Dict[str, Any]:
        results = {}
        self._save_original_state()

        baseline_loss = self._evaluate(val_loader, loss_fn, device)

        for module_name in self.modules_to_ablate:
            self._restore_original_state()
            self._apply_strategy(module_name)

            ablated_loss = self._evaluate(val_loader, loss_fn, device)
            relative_drop = ((baseline_loss - ablated_loss) / baseline_loss) * 100.0 if baseline_loss > 0 else 0.0

            results[module_name] = {
                "loss": ablated_loss,
                "baseline_loss": baseline_loss,
                "relative_drop_percent": relative_drop,
            }

        self._restore_original_state()
        return results
