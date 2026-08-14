import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

import torch


class CheckpointManager:
    def __init__(self, checkpoint_dir: str, monitor: str = "val_loss", mode: str = "min", save_top_k: int = 5, save_last: bool = True, every_n_epochs: int = 1):
        self.checkpoint_dir = Path(checkpoint_dir)
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        self.monitor = monitor
        self.mode = mode
        self.save_top_k = save_top_k
        self.save_last = save_last
        self.every_n_epochs = every_n_epochs
        self.best_value = float("inf") if mode == "min" else float("-inf")
        self.top_k_checkpoints: list = []
        self.last_checkpoint: Optional[str] = None

    def _is_better(self, current: float) -> bool:
        if self.mode == "min":
            return current < self.best_value
        return current > self.best_value

    def _cleanup_old_checkpoints(self, keep_epoch: int):
        epoch_files = sorted(self.checkpoint_dir.glob("epoch_*.pt"))
        keep_paths = {str(self.checkpoint_dir / f"epoch_{keep_epoch:04d}.pt")}
        for path_str, _ in self.top_k_checkpoints:
            keep_paths.add(path_str)
        if self.last_checkpoint:
            keep_paths.add(self.last_checkpoint)
        for path in epoch_files:
            if str(path) not in keep_paths:
                try:
                    path.unlink()
                except OSError:
                    pass

    def _cpu_state(self, state):
        if isinstance(state, torch.Tensor):
            return state.detach().cpu()
        if isinstance(state, dict):
            return {k: self._cpu_state(v) for k, v in state.items()}
        if isinstance(state, (list, tuple)):
            return type(state)(self._cpu_state(v) for v in state)
        return state

    def save(self, state: Dict[str, Any], epoch: int, metrics: Dict[str, float]) -> str:
        saved_path = None
        cpu_state = self._cpu_state(state)

        if self.save_last:
            last_path = self.checkpoint_dir / "last.pt"
            try:
                torch.save(cpu_state, last_path, _use_new_zipfile_serialization=False)
                self.last_checkpoint = str(last_path)
                saved_path = str(last_path)
            except OSError as e:
                print(f"Warning: Could not save last.pt: {e}")

        if self.monitor in metrics:
            current = metrics[self.monitor]
            if self._is_better(current):
                self.best_value = current
                best_path = self.checkpoint_dir / "best.pt"
                try:
                    torch.save(cpu_state, best_path, _use_new_zipfile_serialization=False)
                    self.top_k_checkpoints.append((str(best_path), current))
                    self.top_k_checkpoints = sorted(self.top_k_checkpoints, key=lambda x: x[1], reverse=(self.mode == "max"))[:self.save_top_k]
                    saved_path = str(best_path)
                except OSError as e:
                    print(f"Warning: Could not save best.pt: {e}")

        if epoch % self.every_n_epochs == 0:
            epoch_path = self.checkpoint_dir / f"epoch_{epoch:04d}.pt"
            try:
                torch.save(cpu_state, epoch_path, _use_new_zipfile_serialization=False)
                saved_path = str(epoch_path)
                self._cleanup_old_checkpoints(epoch)
            except OSError as e:
                print(f"Warning: Could not save epoch checkpoint: {e}")

        return saved_path or self.last_checkpoint or ""

    def load(self, path: str, model: torch.nn.Module, optimizer: Optional[torch.optim.Optimizer] = None, device: Optional[torch.device] = None):
        checkpoint = torch.load(path, map_location=device or "cpu")
        ckpt_state = checkpoint["model_state_dict"]
        model_state = model.state_dict()

        new_state = {}
        matched = 0
        skipped = 0
        for key, param in ckpt_state.items():
            if key in model_state:
                if param.shape == model_state[key].shape:
                    new_state[key] = param
                    matched += 1
                else:
                    skipped += 1
            else:
                skipped += 1

        result = model.load_state_dict(new_state, strict=False)
        if result.missing_keys or result.unexpected_keys:
            print(f"Warning: Partial checkpoint load - missing: {result.missing_keys}, unexpected: {result.unexpected_keys}")
        if skipped > 0:
            print(f"Info: Loaded {matched} layers, skipped {skipped} incompatible layers from checkpoint")
        if optimizer and "optimizer_state_dict" in checkpoint:
            try:
                optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
            except Exception as e:
                print(f"Warning: Could not load optimizer state: {e}")
        return checkpoint.get("epoch", 0), checkpoint.get("metrics", {})

    def get_last_checkpoint(self) -> Optional[str]:
        return self.last_checkpoint
