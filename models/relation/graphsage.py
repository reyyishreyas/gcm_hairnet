from typing import Optional

import torch
import torch.nn as nn
import torch.nn.functional as F


class GraphSAGELayer(nn.Module):
    def __init__(self, in_dim: int, out_dim: int, dropout: float = 0.1):
        super().__init__()
        self.linear = nn.Linear(in_dim, out_dim)
        self.agg_linear = nn.Linear(in_dim * 2, out_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor, adj: torch.Tensor) -> torch.Tensor:
        B, N, C = x.shape
        neighbor_agg = torch.bmm(adj, x)
        combined = torch.cat([x, neighbor_agg], dim=-1)
        out = self.agg_linear(combined)
        out = self.dropout(F.relu(out))
        return out


class GraphSAGERelationModule(nn.Module):
    def __init__(self, hidden_dim: int = 128, dropout: float = 0.1, num_layers: int = 3):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.layers = nn.ModuleList()
        for _ in range(num_layers):
            self.layers.append(GraphSAGELayer(hidden_dim, hidden_dim, dropout))
        self.norm = nn.LayerNorm(hidden_dim)
        self.proj = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim),
        )

    @staticmethod
    def _compute_adjacency(x: torch.Tensor) -> torch.Tensor:
        B, N, C = x.shape
        x_norm = F.normalize(x, dim=-1)
        adj = torch.bmm(x_norm, x_norm.transpose(1, 2))
        adj = F.relu(adj)
        adj = adj + torch.eye(N, device=x.device).unsqueeze(0)
        row_sum = adj.sum(dim=-1, keepdim=True).clamp(min=1.0)
        adj = adj / row_sum
        return adj

    def forward(
        self,
        x: torch.Tensor,
        gis_features: Optional[torch.Tensor] = None,
        gis_embeddings: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        adj = self._compute_adjacency(x)
        for layer in self.layers:
            x = layer(x, adj)
        x = self.norm(x)
        return self.proj(x) + x
