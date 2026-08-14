import os
from pathlib import Path
from typing import Any, Dict, Optional

import torch
from torch.utils.tensorboard import SummaryWriter


class Logger:
    def __init__(self, log_dir: str, experiment_name: str, use_tensorboard: bool = True, use_wandb: bool = False, config: Optional[Dict[str, Any]] = None):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.experiment_name = experiment_name
        self.writer: Optional[SummaryWriter] = None
        self.use_wandb = use_wandb

        if use_tensorboard:
            self.writer = SummaryWriter(log_dir=str(self.log_dir / experiment_name))

        if use_wandb:
            try:
                import wandb
                wandb.init(project=experiment_name, config=config)
                self.wandb = wandb
            except ImportError:
                self.use_wandb = False

    def log_metrics(self, metrics: Dict[str, float], step: int, prefix: str = "") -> None:
        for key, value in metrics.items():
            tag = f"{prefix}/{key}" if prefix else key
            if self.writer:
                self.writer.add_scalar(tag, value, step)
            if self.use_wandb:
                self.wandb.log({tag: value}, step=step)

    def log_images(self, images: Dict[str, Any], step: int, prefix: str = "") -> None:
        for key, value in images.items():
            tag = f"{prefix}/{key}" if prefix else key
            if self.writer:
                if isinstance(value, torch.Tensor):
                    self.writer.add_images(tag, value, step, dataformats="NCHW")
            if self.use_wandb:
                if isinstance(value, torch.Tensor):
                    self.wandb.log({tag: [self.wandb.Image(v.cpu().numpy().transpose(1, 2, 0)) for v in value]}, step=step)

    def log_config(self, config: Dict[str, Any]) -> None:
        if self.writer:
            self.writer.add_text("config", str(config))
        if self.use_wandb:
            self.wandb.config.update(config)

    def close(self) -> None:
        if self.writer:
            self.writer.close()
        if self.use_wandb:
            self.wandb.finish()
