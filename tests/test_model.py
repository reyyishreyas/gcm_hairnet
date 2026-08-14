import pytest
import torch

from models import GCMHAIRNet, SwinTransformerEncoder, GISEncoder, GatedCrossAttention, Decoder


class TestModelComponents:
    def test_swin_encoder_forward(self):
        config = {"embed_dim": 64, "depths": [2, 2, 2], "num_heads": [2, 4, 8], "pretrained": False}
        model = SwinTransformerEncoder(config)
        x = torch.randn(2, 3, 256, 256)
        out = model(x)
        assert out.shape[0] == 2
        assert out.shape[2] == 64

    def test_gis_encoder_forward(self):
        config = {"input_channels": 18, "hidden_dim": 64, "output_dim": 64, "dropout": 0.1}
        model = GISEncoder(config)
        x = torch.randn(2, 18, 32, 32)
        out = model(x)
        assert out.shape[0] == 2
        assert out.shape[2] == 64

    def test_gct_forward(self):
        config = {"hidden_dim": 64, "num_heads": 4, "dropout": 0.1}
        model = GatedCrossAttention(config)
        image_feats = torch.randn(2, 64, 64)
        gis_feats = torch.randn(2, 64, 64)
        out = model(image_feats, gis_feats)
        assert out.shape == image_feats.shape

    def test_decoder_forward(self):
        config = {"hidden_dim": 64, "num_classes": 1, "dropout": 0.1}
        model = Decoder(config)
        x = torch.randn(2, 64, 16, 16)
        out = model(x, spatial_size=(256, 256))
        assert out.shape[-2:] == (256, 256)

    def test_gcm_hairnet_forward(self):
        config = {
            "image_encoder": {"embed_dim": 64, "depths": [2, 2, 2], "num_heads": [2, 4, 8], "pretrained": False},
            "gis_encoder": {"input_channels": 18, "hidden_dim": 64, "output_dim": 64, "dropout": 0.1},
            "gct": {"hidden_dim": 64, "num_heads": 4, "dropout": 0.1},
            "grm": {"hidden_dim": 64, "num_relations": 4, "num_layers": 2, "dropout": 0.1},
            "decoder": {"hidden_dim": 64, "num_classes": 1, "dropout": 0.1},
            "image_size": 256,
            "gis_size": 32,
        }
        model = GCMHAIRNet(config)
        image = torch.randn(2, 3, 256, 256)
        gis = torch.randn(2, 18, 32, 32)
        out = model(image, gis)
        assert out.shape[-2:] == (256, 256)
        assert out.shape[0] == 2
