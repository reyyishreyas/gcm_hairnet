from typing import Dict, List, Optional, Tuple

import torch
import torch.nn as nn

from .base import BaseModel
from .encoders.swin import SwinTransformerEncoder
from .encoders.gis_encoder import GISEncoder
from .fusion.gct import GatedCrossAttention
from .graph_relation import GraphRelationModule
from .decoder.risk_decoder import Decoder


class GCMHAIRNet(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.image_encoder = SwinTransformerEncoder(config.get("image_encoder", {}))
        self.gis_encoder = GISEncoder(config.get("gis_encoder", {}))
        gct_config = dict(config.get("gct", {}))
        gct_config.setdefault("gis_input_dim", self.gis_encoder.output_dim)
        self.gct = GatedCrossAttention(gct_config)
        self.graph_relation_module = GraphRelationModule(config.get("grm", {}))
        self.decoder = Decoder(config.get("decoder", {}))
        self.image_size = config.get("image_size", 256)
        self.gis_size = config.get("gis_size", 32)

        gcm_config = config.get("gcm", {})
        self.gcm_config = gcm_config
        self.use_gcm = gcm_config.get("enable", True)
        if self.use_gcm:
            from models.gcm.gcm_block import GCMBlock

            self.gcm = GCMBlock(gcm_config)
            self.gcm_proj = nn.Conv2d(
                self.image_encoder.embed_dim + self.gis_encoder.input_channels,
                gcm_config.get("embed_dim", 512),
                kernel_size=1,
            )
            self.decoder_proj = nn.Conv2d(
                gcm_config.get("embed_dim", 512),
                self.decoder.hidden_dim,
                kernel_size=1,
            )

    @property
    def swin(self):
        return self.image_encoder

    @property
    def grm(self):
        return self.graph_relation_module

    def forward(self, image: torch.Tensor, gis: torch.Tensor) -> torch.Tensor:
        image_feats = self.image_encoder(image)
        gis_feats = self.gis_encoder(gis)
        fused_feats = self.gct(image_feats, gis_feats)

        B, N, C = fused_feats.shape
        H = W = int(N ** 0.5)
        spatial_feats = fused_feats.transpose(1, 2).reshape(B, C, H, W)

        if self.use_gcm:
            upsampled_gis = nn.functional.interpolate(
                gis, size=(H, W), mode="bilinear", align_corners=False
            )
            concat_feats = torch.cat([spatial_feats, upsampled_gis], dim=1)
            projected = self.gcm_proj(concat_feats)
            projected = nn.functional.layer_norm(projected, projected.shape[1:])
            B, C, H, W = projected.shape
            tokens = projected.flatten(2).transpose(1, 2)
            gis_for_priors = nn.functional.interpolate(
                gis, size=(H, W), mode="bilinear", align_corners=False
            )
            gis_embeddings = None
            if hasattr(self.gis_encoder, "encoder"):
                with torch.no_grad():
                    gis_embeddings = self.gis_encoder(gis_for_priors)
            tokens, _ = self.gcm(tokens, gis_for_priors, gis_embeddings)
            spatial_feats = tokens.transpose(1, 2).reshape(B, C, H, W)
            spatial_feats = self.decoder_proj(spatial_feats)

        B, C, H, W = spatial_feats.shape
        tokens = spatial_feats.flatten(2).transpose(1, 2)
        refined_tokens = self.graph_relation_module(tokens)
        spatial_feats = refined_tokens.transpose(1, 2).reshape(B, C, H, W)

        output = self.decoder(spatial_feats, spatial_size=(256, 256))
        return output

    def get_intermediate_features(self, image: torch.Tensor, gis: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = {}
        features["image_encoder"] = self.image_encoder.get_intermediate_features(image)
        features["gis_encoder"] = self.gis_encoder.get_intermediate_features(gis)
        image_feats = features["image_encoder"]["final"]
        gis_feats = features["gis_encoder"]["final"]
        features["gct"] = self.gct.get_intermediate_features(image_feats, gis_feats)

        B, N, C = features["gct"]["gct_output"].shape
        H = W = int(N ** 0.5)
        spatial_feats = features["gct"]["gct_output"].transpose(1, 2).reshape(B, C, H, W)

        if self.use_gcm:
            upsampled_gis = nn.functional.interpolate(
                gis, size=(H, W), mode="bilinear", align_corners=False
            )
            concat_feats = torch.cat([spatial_feats, upsampled_gis], dim=1)
            projected = self.gcm_proj(concat_feats)
            projected = nn.functional.layer_norm(projected, projected.shape[1:])
            B, C, H, W = projected.shape
            tokens = projected.flatten(2).transpose(1, 2)
            features["gcm_input"] = tokens
            gis_for_priors = nn.functional.interpolate(
                gis, size=(H, W), mode="bilinear", align_corners=False
            )
            gis_embeddings = None
            if hasattr(self.gis_encoder, "encoder"):
                with torch.no_grad():
                    gis_embeddings = self.gis_encoder(gis_for_priors)
            gcm_out, gcm_attn_maps = self.gcm(tokens, gis_for_priors, gis_embeddings)
            features["gcm_output"] = gcm_out
            features["gcm_attention"] = gcm_attn_maps
            spatial_feats = gcm_out.transpose(1, 2).reshape(B, C, H, W)
            spatial_feats = self.decoder_proj(spatial_feats)

        features["graph_relation_input"] = spatial_feats.flatten(2).transpose(1, 2)
        refined_tokens = self.graph_relation_module(features["graph_relation_input"])
        features["graph_relation_output"] = refined_tokens
        B, C, H, W = spatial_feats.shape
        spatial_feats = refined_tokens.transpose(1, 2).reshape(B, C, H, W)

        features["decoder_input"] = spatial_feats
        features["decoder"] = self.decoder.get_intermediate_features(spatial_feats, (256, 256))
        return features
