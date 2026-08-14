from typing import Any, Dict, List, Optional

import numpy as np
import torch


def plot_feature_map(
    feature_map: torch.Tensor,
    save_path: Optional[str] = None,
    title: str = "Feature Map",
    cmap: str = "viridis",
    num_channels: int = 8,
):
    try:
        import matplotlib.pyplot as plt

        feat = feature_map.detach().cpu().numpy().squeeze()
        if feat.ndim == 2:
            feat = feat[np.newaxis, ...]

        num_channels = min(num_channels, feat.shape[0])
        fig, axes = plt.subplots(1, num_channels, figsize=(4 * num_channels, 4))
        if num_channels == 1:
            axes = [axes]

        for i in range(num_channels):
            im = axes[i].imshow(feat[i], cmap=cmap)
            axes[i].set_title(f"Channel {i}")
            axes[i].axis("off")
            plt.colorbar(im, ax=axes[i])

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass


def save_feature_maps(
    feature_maps: Dict[str, torch.Tensor],
    output_dir: str,
    max_channels: int = 8,
) -> None:
    from pathlib import Path
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for name, feat in feature_maps.items():
        plot_feature_map(feat, save_path=str(output_path / f"{name}_feature_map.png"), title=name, num_channels=max_channels)
