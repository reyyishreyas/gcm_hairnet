from typing import Dict

import torch
import torch.nn as nn

from ..base import BaseModel
from ..encoders.swin import SwinTransformerEncoder
from ..encoders.gis_encoder import GISEncoder
from ..graph_relation import GraphRelationModule
from ..decoder.risk_decoder import Decoder


class ImageOnlyModel(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.image_encoder = SwinTransformerEncoder(config.get("image_encoder", {}))
        self.grm = GraphRelationModule(config.get("grm", {}))
        self.decoder = Decoder(config.get("decoder", {}))
        self.proj = nn.Linear(self.image_encoder.embed_dim, self.decoder.hidden_dim)

    def forward(self, image: torch.Tensor, gis: torch.Tensor) -> torch.Tensor:
        feats = self.image_encoder(image)
        B, N, C = feats.shape
        H = W = int(N ** 0.5)
        spatial = self.proj(feats).transpose(1, 2).reshape(B, self.decoder.hidden_dim, H, W)
        tokens = spatial.flatten(2).transpose(1, 2)
        refined = self.grm(tokens)
        spatial = refined.transpose(1, 2).reshape(B, self.decoder.hidden_dim, H, W)
        return self.decoder(spatial, spatial_size=(256, 256))

    def get_intermediate_features(self, image: torch.Tensor, gis: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = {}
        features["image_encoder"] = self.image_encoder.get_intermediate_features(image)
        feats = features["image_encoder"]["final"]
        B, N, C = feats.shape
        H = W = int(N ** 0.5)
        spatial = self.proj(feats).transpose(1, 2).reshape(B, self.decoder.hidden_dim, H, W)
        features["decoder_input"] = spatial
        features["decoder"] = self.decoder.get_intermediate_features(spatial, (256, 256))
        return features


class GISOnlyModel(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.gis_encoder = GISEncoder(config.get("gis_encoder", {}))
        self.grm = GraphRelationModule(config.get("grm", {}))
        self.decoder = Decoder(config.get("decoder", {}))
        self.proj = nn.Linear(self.gis_encoder.output_dim, self.decoder.hidden_dim)

    def forward(self, image: torch.Tensor, gis: torch.Tensor) -> torch.Tensor:
        feats = self.gis_encoder(gis)
        B, N, C = feats.shape
        H = W = int(N ** 0.5)
        spatial = self.proj(feats).transpose(1, 2).reshape(B, self.decoder.hidden_dim, H, W)
        tokens = spatial.flatten(2).transpose(1, 2)
        refined = self.grm(tokens)
        spatial = refined.transpose(1, 2).reshape(B, self.decoder.hidden_dim, H, W)
        return self.decoder(spatial, spatial_size=(256, 256))

    def get_intermediate_features(self, image: torch.Tensor, gis: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = {}
        features["gis_encoder"] = self.gis_encoder.get_intermediate_features(gis)
        feats = features["gis_encoder"]["final"]
        B, N, C = feats.shape
        H = W = int(N ** 0.5)
        spatial = self.proj(feats).transpose(1, 2).reshape(B, self.decoder.hidden_dim, H, W)
        features["decoder_input"] = spatial
        features["decoder"] = self.decoder.get_intermediate_features(spatial, (256, 256))
        return features
