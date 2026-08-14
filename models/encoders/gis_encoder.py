from typing import Dict

import torch
import torch.nn as nn

from ..base import BaseModel


class GISEncoder(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.input_channels = config.get("input_channels", 18)
        self.hidden_dim = config.get("hidden_dim", 128)
        self.output_dim = config.get("output_dim", 128)
        self.dropout = config.get("dropout", 0.1)
        self._build_encoder()

    def _build_encoder(self):
        self.encoder = nn.Sequential(
            nn.Conv2d(self.input_channels, self.hidden_dim, kernel_size=3, padding=1),
            nn.BatchNorm2d(self.hidden_dim),
            nn.ReLU(),
            nn.Conv2d(self.hidden_dim, self.hidden_dim, kernel_size=3, padding=1),
            nn.BatchNorm2d(self.hidden_dim),
            nn.ReLU(),
            nn.Conv2d(self.hidden_dim, self.output_dim, kernel_size=3, padding=1),
            nn.AdaptiveAvgPool2d((16, 16)),
        )
        self.out_norm = nn.LayerNorm(self.output_dim)

    def forward(self, gis: torch.Tensor) -> torch.Tensor:
        x = self.encoder(gis)
        x = x.flatten(2).transpose(1, 2)
        x = self.out_norm(x)
        return x

    def get_intermediate_features(self, gis: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = {}
        x = gis
        for i, layer in enumerate(self.encoder):
            x = layer(x)
            features[f"gis_enc_{i}"] = x
        x = x.flatten(2).transpose(1, 2)
        x = self.out_norm(x)
        features["final"] = x
        return features
