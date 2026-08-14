from typing import Dict

import timm
import torch
import torch.nn as nn

from ..base import BaseModel


class SwinTransformerEncoder(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.embed_dim = config.get("embed_dim", 128)
        self.pretrained = config.get("pretrained", False)
        self.model_name = config.get("type", "swinv2_tiny_window16_256")
        self.depths = config.get("depths", None)
        self.num_heads = config.get("num_heads", None)
        self.window_size = config.get("window_size", None)
        self.img_size = config.get("img_size", 256)

        available_models = {
            "swinv2_tiny": "swinv2_tiny_window16_256",
            "swinv2_small": "swinv2_small_window16_256",
            "swinv2_base": "swinv2_base_window16_256",
        }

        if self.depths is not None and self.num_heads is not None and self.window_size is not None:
            from timm.models.swin_transformer_v2 import SwinTransformerV2

            self.swin = SwinTransformerV2(
                img_size=self.img_size,
                patch_size=4,
                in_chans=3,
                num_classes=0,
                embed_dim=self.embed_dim,
                depths=self.depths,
                num_heads=self.num_heads,
                window_size=self.window_size,
                drop_path_rate=config.get("drop_path_rate", 0.2),
                strict_img_size=False,
            )
            self.feature_dim = self.swin.num_features
        else:
            timm_model_name = available_models.get(self.model_name, self.model_name)
            try:
                self.swin = timm.create_model(timm_model_name, pretrained=self.pretrained, num_classes=0)
                self.feature_dim = self.swin.num_features
            except Exception:
                self.swin = timm.create_model("swinv2_tiny_window16_256", pretrained=self.pretrained, num_classes=0)
                self.feature_dim = 768

        self.proj = nn.Linear(self.feature_dim, self.embed_dim) if self.feature_dim != self.embed_dim else nn.Identity()

    def forward(self, image: torch.Tensor) -> torch.Tensor:
        features = self.swin.forward_features(image)
        features = features.flatten(1, 2)
        return self.proj(features)

    def get_intermediate_features(self, image: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = self.forward(image)
        return {"final": features}
