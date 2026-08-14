import torch
import torch.nn as nn
import torch.nn.functional as F


class FeatureSimilarityPrior(nn.Module):
    def __init__(self, feature_dim: int = 64, eps: float = 1e-8):
        super().__init__()
        self.feature_dim = feature_dim
        self.eps = eps

    def forward(self, gis_embeddings: torch.Tensor) -> torch.Tensor:
        if gis_embeddings.dim() == 4:
            B, C, H, W = gis_embeddings.shape
            gis_embeddings = gis_embeddings.flatten(2).transpose(1, 2)
        gis_norm = F.normalize(gis_embeddings, dim=-1, eps=self.eps)
        S = torch.bmm(gis_norm, gis_norm.transpose(1, 2))
        row_max = S.max(dim=-1, keepdim=True)[0]
        row_min = S.min(dim=-1, keepdim=True)[0]
        denom = (row_max - row_min).clamp(min=self.eps)
        S = (S - row_min) / denom
        return S
