from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np
import torch


def save_risk_maps(
    predictions: np.ndarray,
    city_names: List[str],
    output_dir: str,
    cmap: str = "hot",
) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for pred, city in zip(predictions, city_names):
        if pred.ndim == 3:
            pred = pred.squeeze()
        np.save(output_path / f"{city}_risk_map.npy", pred)

        if _matplotlib_available():
            try:
                import matplotlib.pyplot as plt

                fig, ax = plt.subplots(figsize=(8, 8))
                im = ax.imshow(pred, cmap=cmap)
                ax.set_title(f"Risk Map: {city}")
                plt.colorbar(im, ax=ax)
                fig.savefig(output_path / f"{city}_risk_map.png")
                plt.close(fig)
            except ImportError:
                pass


def save_comparison_maps(
    predictions: np.ndarray,
    targets: np.ndarray,
    city_names: List[str],
    output_dir: str,
) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if not _matplotlib_available():
        return

    try:
        import matplotlib.pyplot as plt

        for pred, target, city in zip(predictions, targets, city_names):
            if pred.ndim == 3:
                pred = pred.squeeze()
            if target.ndim == 3:
                target = target.squeeze()

            fig, axes = plt.subplots(1, 3, figsize=(15, 5))
            axes[0].imshow(target, cmap="hot")
            axes[0].set_title(f"Ground Truth: {city}")
            axes[0].axis("off")

            axes[1].imshow(pred, cmap="hot")
            axes[1].set_title(f"Prediction: {city}")
            axes[1].axis("off")

            diff = np.abs(target - pred)
            axes[2].imshow(diff, cmap="viridis")
            axes[2].set_title(f"Absolute Error: {city}")
            axes[2].axis("off")

            fig.savefig(output_path / f"{city}_comparison.png")
            plt.close(fig)
    except ImportError:
        pass


def _matplotlib_available() -> bool:
    try:
        import matplotlib  # noqa: F401
        return True
    except ImportError:
        return False
