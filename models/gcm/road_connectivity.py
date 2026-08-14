from pathlib import Path
from typing import Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F


class RoadConnectivityPrior(nn.Module):
    def __init__(self, grid_size: int = 16, eps: float = 1e-8, precomputed_path: Optional[str] = None):
        super().__init__()
        self.grid_size = grid_size
        self.num_tokens = grid_size * grid_size
        self.eps = eps
        self.precomputed_path = precomputed_path
        self.register_buffer("precomputed_R", torch.zeros(1, grid_size * grid_size, grid_size * grid_size))

        if precomputed_path and Path(precomputed_path).exists():
            self.load_precomputed(precomputed_path)

    def load_precomputed(self, path: str):
        state = torch.load(path, map_location="cpu")
        if "road_connectivity" in state:
            R = state["road_connectivity"]
        else:
            R = state
        if R.ndim == 2:
            R = R.unsqueeze(0)
        self.register_buffer("precomputed_R", R)

    def _density_fallback(self, gis_features: torch.Tensor) -> torch.Tensor:
        road_density = gis_features[:, 2, :, :]
        B, H, W = road_density.shape
        N = H * W
        road_density = road_density.view(B, N)
        road_sim = torch.bmm(road_density.unsqueeze(-1), road_density.unsqueeze(-1).transpose(1, 2))
        diagonal = torch.diagonal(road_sim, dim1=-2, dim2=-1)
        max_vals = diagonal.max(dim=-1, keepdim=True)[0].unsqueeze(-1)
        R = road_sim / (max_vals + self.eps)
        identity = torch.eye(N, device=gis_features.device).unsqueeze(0)
        R = R * (1 - identity)
        R = R / (R.sum(dim=-1, keepdim=True) + self.eps)
        return R

    def forward(self, gis_features: torch.Tensor) -> torch.Tensor:
        if self.precomputed_R.sum() > 0:
            R = self.precomputed_R.to(gis_features.device)
            if R.shape[1] != gis_features.shape[2] * gis_features.shape[3]:
                return self._density_fallback(gis_features)
            return R.expand(gis_features.shape[0], -1, -1)
        return self._density_fallback(gis_features)
