from typing import Dict

import torch
import torch.nn as nn

from ..base import BaseModel


class Decoder(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.hidden_dim = config.get("hidden_dim", 128)
        self.num_classes = config.get("num_classes", 1)
        self.dropout = config.get("dropout", 0.1)
        self._build_decoder()

    def _build_decoder(self):
        self.up1 = nn.Sequential(
            nn.ConvTranspose2d(self.hidden_dim, self.hidden_dim // 2, kernel_size=2, stride=2),
            nn.ReLU(),
            nn.Dropout2d(self.dropout),
        )
        self.up2 = nn.Sequential(
            nn.ConvTranspose2d(self.hidden_dim // 2, self.hidden_dim // 4, kernel_size=2, stride=2),
            nn.ReLU(),
            nn.Dropout2d(self.dropout),
        )
        self.up3 = nn.Sequential(
            nn.ConvTranspose2d(self.hidden_dim // 4, self.hidden_dim // 8, kernel_size=2, stride=2),
            nn.ReLU(),
            nn.Dropout2d(self.dropout),
        )
        self.final = nn.Sequential(
            nn.Conv2d(self.hidden_dim // 8, self.num_classes, kernel_size=1),
        )

    def forward(self, feats: torch.Tensor, spatial_size: tuple) -> torch.Tensor:
        if feats.shape[1] != self.hidden_dim:
            raise ValueError(
                f"Decoder expected input with {self.hidden_dim} channels, "
                f"but got tensor with {feats.shape[1]} channels. "
                f"Ensure encoder/GCM output channels match decoder hidden_dim."
            )
        x = feats
        x = self.up1(x)
        x = self.up2(x)
        x = self.up3(x)
        x = nn.functional.interpolate(x, size=spatial_size, mode="bilinear", align_corners=False)
        x = self.final(x)
        return x

    def get_intermediate_features(self, feats: torch.Tensor, spatial_size: tuple) -> Dict[str, torch.Tensor]:
        if feats.shape[1] != self.hidden_dim:
            raise ValueError(
                f"Decoder expected input with {self.hidden_dim} channels, "
                f"but got tensor with {feats.shape[1]} channels."
            )
        features = {}
        x = feats
        for i, layer in enumerate([self.up1, self.up2, self.up3]):
            x = layer(x)
            features[f"decoder_up_{i}"] = x
        x = nn.functional.interpolate(x, size=spatial_size, mode="bilinear", align_corners=False)
        features["decoder_output"] = self.final(x)
        return features
