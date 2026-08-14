import torch
import torch.nn as nn
import torch.nn.functional as F


class SceneWeightPredictor(nn.Module):
    def __init__(self, gis_channels: int = 18, hidden_dim: int = 64, scene_hidden: int = 32, output_dim: int = 5):
        super().__init__()
        self.scene_encoder = nn.Sequential(
            nn.Conv2d(gis_channels, hidden_dim, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(hidden_dim, hidden_dim // 2, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
            nn.Linear(hidden_dim // 2, scene_hidden),
            nn.ReLU(),
            nn.Linear(scene_hidden, output_dim),
        )

    def forward(self, gis_features: torch.Tensor) -> torch.Tensor:
        logits = self.scene_encoder(gis_features)
        weights = F.softmax(logits, dim=-1)
        return weights
