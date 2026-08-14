from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np
import torch


def save_prediction_plots(predictions: np.ndarray, metadata: List[Dict], output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for i, pred in enumerate(predictions):
        city = metadata[i].get("city_name", f"sample_{i}")
        np.save(output_path / f"{city}_prediction.npy", pred)


def plot_prediction_vs_target(
    preds: torch.Tensor,
    targets: torch.Tensor,
    save_path: Optional[str] = None,
    title: str = "Predictions vs Targets",
):
    try:
        import matplotlib.pyplot as plt

        preds = preds.detach().cpu().numpy().flatten()
        targets = targets.detach().cpu().numpy().flatten()

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(targets, preds, alpha=0.5)
        ax.plot([targets.min(), targets.max()], [targets.min(), targets.max()], "r--")
        ax.set_xlabel("Targets")
        ax.set_ylabel("Predictions")
        ax.set_title(title)

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass


def plot_risk_map(
    risk_map: torch.Tensor,
    save_path: Optional[str] = None,
    title: str = "Risk Map",
    cmap: str = "hot",
):
    try:
        import matplotlib.pyplot as plt

        risk_map = risk_map.detach().cpu().numpy().squeeze()
        fig, ax = plt.subplots(figsize=(8, 8))
        im = ax.imshow(risk_map, cmap=cmap)
        ax.set_title(title)
        plt.colorbar(im, ax=ax)

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass


def plot_attention_map(
    attention_weights: torch.Tensor,
    save_path: Optional[str] = None,
    title: str = "Attention Map",
    cmap: str = "viridis",
):
    try:
        import matplotlib.pyplot as plt

        attn = attention_weights.detach().cpu().numpy().squeeze()
        fig, ax = plt.subplots(figsize=(10, 8))
        im = ax.imshow(attn, cmap=cmap)
        ax.set_title(title)
        plt.colorbar(im, ax=ax)

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass
