from typing import Any, Dict, List, Optional

import numpy as np
import torch


def plot_grm_relations(
    relation_weights: torch.Tensor,
    save_path: Optional[str] = None,
    title: str = "GRM Relations",
):
    try:
        import matplotlib.pyplot as plt

        weights = relation_weights.detach().cpu().numpy()
        num_relations = weights.shape[0]
        fig, axes = plt.subplots(1, num_relations, figsize=(5 * num_relations, 4))
        if num_relations == 1:
            axes = [axes]

        for i in range(num_relations):
            im = axes[i].imshow(weights[i], cmap="coolwarm")
            axes[i].set_title(f"Relation {i}")
            plt.colorbar(im, ax=axes[i])

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass


def plot_graph_embeddings(
    embeddings: torch.Tensor,
    labels: Optional[np.ndarray] = None,
    save_path: Optional[str] = None,
    title: str = "Graph Embeddings",
):
    try:
        import matplotlib.pyplot as plt

        emb = embeddings.detach().cpu().numpy()
        if emb.shape[1] > 2:
            from sklearn.decomposition import PCA
            emb = PCA(n_components=2).fit_transform(emb)

        fig, ax = plt.subplots(figsize=(8, 6))
        if labels is not None:
            scatter = ax.scatter(emb[:, 0], emb[:, 1], c=labels, cmap="tab10")
            plt.colorbar(scatter, ax=ax)
        else:
            ax.scatter(emb[:, 0], emb[:, 1])
        ax.set_title(title)

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass
