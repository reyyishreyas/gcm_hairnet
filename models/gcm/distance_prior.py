from typing import Optional, Tuple

import torch
import torch.nn as nn


class SpatialDistancePrior(nn.Module):
    def __init__(self, grid_size: int = 16, sigma: float = 1.0):
        super().__init__()
        self.grid_size = grid_size
        self.sigma = sigma
        self.num_tokens = grid_size * grid_size
        coords = self._generate_coords(grid_size)
        self.register_buffer("coords", coords)
        self.register_buffer("distance_matrix", self._compute_distance_matrix())

    def _generate_coords(self, grid_size: int) -> torch.Tensor:
        x = torch.arange(grid_size, dtype=torch.float32)
        y = torch.arange(grid_size, dtype=torch.float32)
        xx, yy = torch.meshgrid(x, y, indexing="ij")
        coords = torch.stack([xx.flatten(), yy.flatten()], dim=-1)
        return coords

    def _compute_distance_matrix(self) -> torch.Tensor:
        dist = torch.cdist(self.coords, self.coords, p=2)
        dist = dist / (2 * self.sigma**2)
        D = torch.exp(-dist)
        D = D / (D.sum(dim=-1, keepdim=True) + 1e-8)
        return D

    def forward(self, batch_size: int) -> torch.Tensor:
        return self.distance_matrix.unsqueeze(0).expand(batch_size, -1, -1)
