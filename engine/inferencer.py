from pathlib import Path
from typing import Any, Dict, Optional

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from utils.misc import get_device
from visualization import save_prediction_plots


class Inferencer:
    def __init__(
        self,
        model: nn.Module,
        data_loader: DataLoader,
        checkpoint_path: Optional[str] = None,
        device: Optional[torch.device] = None,
        output_dir: str = "./outputs/inference",
        save_predictions: bool = True,
        save_visualizations: bool = True,
    ):
        self.model = model
        self.data_loader = data_loader
        self.device = device or get_device()
        self.output_dir = Path(output_dir)
        self.save_predictions = save_predictions
        self.save_visualizations = save_visualizations
        self.output_dir.mkdir(parents=True, exist_ok=True)

        if checkpoint_path:
            self._load_checkpoint(checkpoint_path)

        self.model.to(self.device)
        self.model.eval()

    def _load_checkpoint(self, path: str):
        checkpoint = torch.load(path, map_location=self.device)
        ckpt_state = checkpoint["model_state_dict"]
        model_state = self.model.state_dict()
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
        result = self.model.load_state_dict(new_state, strict=False)
        if result.missing_keys or result.unexpected_keys:
            print(f"Warning: Partial checkpoint load - missing: {result.missing_keys}, unexpected: {result.unexpected_keys}")
        if skipped > 0:
            print(f"Info: Loaded {matched} layers, skipped {skipped} incompatible layers from checkpoint")

    @torch.no_grad()
    def run(self) -> Dict[str, Any]:
        all_preds = []
        all_metadata = []

        for batch in self.data_loader:
            image = batch["image"].to(self.device, non_blocking=True)
            gis = batch["gis"].to(self.device, non_blocking=True)

            preds = self.model(image, gis)
            all_preds.append(torch.sigmoid(preds).cpu().numpy())
            all_metadata.extend(batch.get("metadata", []))

        predictions = np.concatenate(all_preds, axis=0)

        if self.save_predictions:
            np.save(self.output_dir / "predictions.npy", predictions)

        if self.save_visualizations and all_metadata:
            save_prediction_plots(predictions, all_metadata, str(self.output_dir))

        return {"predictions": predictions}
