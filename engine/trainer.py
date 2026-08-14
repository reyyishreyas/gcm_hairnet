import numpy as np
from typing import Any, Dict, Optional

import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from datasets.collate import collate_fn
from losses.combined import build_loss
from metrics.regression_metrics import RegressionMetrics
from utils.checkpoint import CheckpointManager
from utils.logger import Logger
from utils.seed import count_parameters, set_seed
from .engine import Engine


class Trainer:
    def __init__(
        self,
        model: nn.Module,
        train_loader: DataLoader,
        val_loader: DataLoader,
        config: Any,
        device: torch.device,
        vis_dir: Optional[str] = None,
    ):
        self.model = model
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.config = config
        self.device = device
        self.epoch = 0
        self.global_step = 0
        self.vis_dir = vis_dir

        self._setup_training()

    def _setup_training(self):
        set_seed(self.config.get("experiment", {}).get("seed", 42))

        self.optimizer = torch.optim.AdamW(
            self.model.parameters(),
            lr=self.config.get("training", {}).get("optimizer", {}).get("lr", 1e-4),
            weight_decay=self.config.get("training", {}).get("optimizer", {}).get("weight_decay", 1e-4),
            betas=tuple(self.config.get("training", {}).get("optimizer", {}).get("betas", [0.9, 0.999])),
        )

        scheduler_config = self.config.get("training", {}).get("scheduler", {})
        self.warmup_epochs = scheduler_config.get("warmup_epochs", 0)
        self.base_lr = self.config.get("training", {}).get("optimizer", {}).get("lr", 1e-4)
        if scheduler_config.get("type") == "cosine_annealing":
            self.scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
                self.optimizer,
                T_max=scheduler_config.get("T_max", 100),
                eta_min=scheduler_config.get("eta_min", 1e-6),
            )
        else:
            self.scheduler = None

        self.loss_fn = build_loss(self.config.get("training", {}).get("loss", {}))

        checkpoint_config = self.config.get("checkpoint", {})
        self.checkpoint_manager = CheckpointManager(
            checkpoint_dir=checkpoint_config.get("dir", "./checkpoints"),
            monitor=checkpoint_config.get("monitor", "val_loss"),
            mode=checkpoint_config.get("mode", "min"),
            save_top_k=checkpoint_config.get("save_top_k", 5),
            save_last=checkpoint_config.get("save_last", True),
            every_n_epochs=checkpoint_config.get("every_n_epochs", 1),
        )

        logger_config = self.config.get("logger", {})
        self.logger = Logger(
            log_dir=logger_config.get("log_dir", "./logs"),
            experiment_name=self.config.get("experiment", {}).get("name", "gcm_hairnet"),
            use_tensorboard=True,
            config=self.config.to_dict() if hasattr(self.config, "to_dict") else dict(self.config),
        )

        self.metric_fn = RegressionMetrics()
        self.num_epochs = self.config.get("training", {}).get("epochs", 100)

    def train_epoch(self) -> Dict[str, float]:
        self.model.train()
        total_loss = 0.0
        num_batches = 0

        for batch in self.train_loader:
            metrics = self.engine.train_step(batch)
            total_loss += metrics["loss"]
            num_batches += 1

            if self.global_step % self.config.get("logger", {}).get("log_every_n_steps", 50) == 0:
                self.logger.log_metrics({"train_loss_step": metrics["loss"]}, self.global_step, prefix="train")

        avg_loss = total_loss / max(num_batches, 1)
        self.logger.log_metrics({"train_loss_epoch": avg_loss}, self.epoch, prefix="train")
        return {"train_loss": avg_loss}

    @torch.no_grad()
    def validate_epoch(self) -> Dict[str, float]:
        self.model.eval()
        total_loss = 0.0
        num_batches = 0
        all_preds = []
        all_targets = []

        for batch in self.val_loader:
            result = self.engine.validation_step(batch)
            total_loss += result["val_loss"]
            num_batches += 1
            all_preds.append(result["preds"].numpy())
            all_targets.append(result["targets"].numpy())

        avg_loss = total_loss / max(num_batches, 1)

        if all_preds:
            preds = np.concatenate(all_preds, axis=0)
            targets = np.concatenate(all_targets, axis=0)
            metrics = self.metric_fn(preds, targets)
            metrics["val_loss"] = avg_loss
            self.logger.log_metrics(metrics, self.epoch, prefix="val")
            if self.vis_dir and hasattr(self.model, "use_gcm") and self.model.use_gcm:
                try:
                    from visualization import save_gcm_priors, save_gcm_attention_maps, save_scene_weights
                    sample_batch = next(iter(self.val_loader))
                    sample_image = sample_batch["image"].to(self.device)
                    sample_gis = sample_batch["gis"].to(self.device)
                    with torch.no_grad():
                        inter = self.model.get_intermediate_features(sample_image, sample_gis)
                    if "gcm_attention" in inter:
                        save_gcm_attention_maps(inter["gcm_attention"], self.vis_dir, self.epoch)
                    if hasattr(self.model.gcm.grm, "scene_weight_predictor"):
                        scene_weights = self.model.gcm.grm.scene_weight_predictor(sample_gis)
                        save_scene_weights(scene_weights, self.vis_dir, self.epoch)
                except Exception:
                    pass
            return metrics

        self.logger.log_metrics({"val_loss": avg_loss}, self.epoch, prefix="val")
        return {"val_loss": avg_loss}

    def fit(self, epoch_callback=None):
        self.model.to(self.device)
        self.engine = Engine(
            model=self.model,
            optimizer=self.optimizer,
            scheduler=self.scheduler,
            loss_fn=self.loss_fn,
            device=self.device,
            gradient_clip_val=self.config.get("training", {}).get("gradient_clip_val"),
            gradient_accumulation_steps=self.config.get("training", {}).get("gradient_accumulation_steps", 1),
        )

        param_info = count_parameters(self.model)
        print(f"Total parameters: {param_info['total']:,}")
        print(f"Trainable parameters: {param_info['trainable']:,}")

        early_stopping_config = self.config.get("training", {}).get("early_stopping", {})
        patience = early_stopping_config.get("patience", 0)
        monitor = early_stopping_config.get("monitor", "val_loss")
        mode = early_stopping_config.get("mode", "min")
        best_value = float("inf") if mode == "min" else float("-inf")
        epochs_no_improve = 0

        for epoch in range(self.epoch, self.num_epochs):
            self.epoch = epoch

            if self.scheduler:
                if epoch < self.warmup_epochs:
                    lr_scale = (epoch + 1) / self.warmup_epochs
                    for param_group in self.optimizer.param_groups:
                        param_group["lr"] = self.base_lr * lr_scale

            train_metrics = self.train_epoch()
            val_metrics = self.validate_epoch()

            val_loss = val_metrics.get("val_loss", float("inf"))
            print(f"Epoch {epoch:03d} | Train Loss: {train_metrics['train_loss']:.4f} | Val Loss: {val_loss:.4f}")

            if epoch_callback is not None:
                epoch_callback(epoch, val_metrics)

            checkpoint_state = {
                "epoch": epoch,
                "model_state_dict": self.model.state_dict(),
                "optimizer_state_dict": self.optimizer.state_dict(),
                "metrics": val_metrics,
            }
            self.checkpoint_manager.save(checkpoint_state, epoch, val_metrics)

            current_value = val_metrics.get(monitor, val_metrics.get("val_loss", float("inf")))
            if mode == "min":
                improved = current_value < best_value
            else:
                improved = current_value > best_value

            if improved:
                best_value = current_value
                epochs_no_improve = 0
            else:
                epochs_no_improve += 1

            if patience > 0 and epochs_no_improve >= patience:
                print(f"Early stopping triggered at epoch {epoch}. Best {monitor}: {best_value:.4f}")
                break

            if self.scheduler and epoch >= self.warmup_epochs:
                self.scheduler.step()

        self.logger.close()

    def resume(self, checkpoint_path: Optional[str] = None):
        path = checkpoint_path or self.checkpoint_manager.get_last_checkpoint()
        if path:
            start_epoch, metrics = self.checkpoint_manager.load(path, self.model, self.optimizer, self.device)
            self.epoch = start_epoch
            print(f"Resumed from epoch {start_epoch}")
