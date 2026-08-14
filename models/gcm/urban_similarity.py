import torch
import torch.nn as nn
import torch.nn.functional as F


class UrbanSimilarityPrior(nn.Module):
    def __init__(self, gis_channels: int = 18, hidden_dim: int = 64, latent_dim: int = 16, eps: float = 1e-8):
        super().__init__()
        self.urban_encoder = nn.Sequential(
            nn.Conv2d(gis_channels, hidden_dim, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(hidden_dim, hidden_dim // 2, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(hidden_dim // 2, latent_dim, kernel_size=3, padding=1),
        )
        self.latent_dim = latent_dim
        self.eps = eps

    def forward(self, gis_features: torch.Tensor) -> torch.Tensor:
        B, C, H, W = gis_features.shape
        latent = self.urban_encoder(gis_features)
        latent = F.normalize(latent, dim=1, eps=self.eps)
        latent = latent.view(B, self.latent_dim, H * W).transpose(1, 2)
        U = torch.bmm(latent, latent.transpose(1, 2))
        row_max = U.max(dim=-1, keepdim=True)[0]
        row_min = U.min(dim=-1, keepdim=True)[0]
        U = (U - row_min) / (row_max - row_min + self.eps)
        return U
