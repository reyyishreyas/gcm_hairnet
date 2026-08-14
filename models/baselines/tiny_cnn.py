from typing import Dict

import torch
import torch.nn as nn

from ..base import BaseModel


class TinyRiskCNN(BaseModel):
    """Minimal CNN baseline for tiny datasets. Works well with heavy augmentation."""
    def __init__(self, config: Dict):
        super().__init__(config)
        input_channels = config.get("input_channels", 18)
        hidden_dim = config.get("hidden_dim", 32)
        dropout = config.get("dropout", 0.3)

        self.encoder = nn.Sequential(
            nn.Conv2d(3, hidden_dim, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Dropout2d(dropout),
            nn.Conv2d(hidden_dim, hidden_dim * 2, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Dropout2d(dropout),
            nn.Conv2d(hidden_dim * 2, hidden_dim * 2, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Dropout2d(dropout),
        )

        self.gis_encoder = nn.Sequential(
            nn.Conv2d(input_channels, hidden_dim, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Dropout2d(dropout),
            nn.Conv2d(hidden_dim, hidden_dim * 2, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Dropout2d(dropout),
        )

        self.fusion = nn.Sequential(
            nn.Conv2d(hidden_dim * 4, hidden_dim * 2, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Dropout2d(dropout),
            nn.Conv2d(hidden_dim * 2, hidden_dim, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Dropout2d(dropout),
            nn.Conv2d(hidden_dim, 1, kernel_size=1),
        )

    def forward(self, image: torch.Tensor, gis: torch.Tensor) -> torch.Tensor:
        img_feats = self.encoder(image)
        gis_feats = self.gis_encoder(gis)

        if gis_feats.shape[-2:] != img_feats.shape[-2:]:
            gis_feats = nn.functional.interpolate(gis_feats, size=img_feats.shape[-2:], mode="bilinear", align_corners=False)

        concat = torch.cat([img_feats, gis_feats], dim=1)
        out = self.fusion(concat)
        return out

    def get_intermediate_features(self, image: torch.Tensor, gis: torch.Tensor) -> Dict[str, torch.Tensor]:
        img_feats = self.encoder(image)
        gis_feats = self.gis_encoder(gis)
        if gis_feats.shape[-2:] != img_feats.shape[-2:]:
            gis_feats = nn.functional.interpolate(gis_feats, size=img_feats.shape[-2:], mode="bilinear", align_corners=False)
        concat = torch.cat([img_feats, gis_feats], dim=1)
        out = self.fusion(concat)
        return {"encoder": img_feats, "gis_encoder": gis_feats, "final": out}
