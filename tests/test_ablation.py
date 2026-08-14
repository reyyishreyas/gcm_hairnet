import torch
import torch.nn as nn

from utils.ablation import AblationManager


class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.swin = nn.Linear(10, 10)
        self.grm = nn.Linear(10, 10)
        self.decoder = nn.Linear(10, 1)

    def forward(self, image, gis):
        x = image.flatten(1)
        x = self.swin(x)
        x = self.grm(x)
        return self.decoder(x)


class TestAblationManager:
    def test_replace_with_identity_zeroes_output(self):
        model = SimpleModel()
        config = {
            "ablation": {
                "modules": ["swin"],
                "strategy": "replace_with_identity",
            }
        }
        manager = AblationManager(model, config)
        x = torch.randn(2, 10)
        original_out = model.swin(x).clone()

        manager._save_original_state()
        manager._replace_with_identity("swin")
        assert torch.all(model.swin(x) == 0)

        manager._restore_original_state()
        assert torch.allclose(model.swin(x), original_out)

    def test_replace_with_mean_expands_mean(self):
        model = SimpleModel()
        config = {
            "ablation": {
                "modules": ["swin"],
                "strategy": "replace_with_mean",
            }
        }
        manager = AblationManager(model, config)
        manager._save_original_state()
        manager._replace_with_mean("swin")

        x = torch.randn(4, 10)
        out = model.swin(x)
        assert out.shape == (4, 10)
        row0 = out[0]
        for i in range(1, 4):
            assert torch.allclose(out[i], row0)

        manager._restore_original_state()

    def test_run_ablation_returns_expected_structure(self):
        model = SimpleModel()
        config = {
            "ablation": {
                "modules": ["swin", "grm"],
                "strategy": "replace_with_identity",
            }
        }
        manager = AblationManager(model, config)

        class DummyLoader:
            def __iter__(self):
                for _ in range(2):
                    yield {
                        "image": torch.randn(2, 10),
                        "gis": torch.randn(2, 10),
                        "label": torch.randn(2, 1),
                    }

        class DummyLoss(nn.Module):
            def forward(self, preds, targets):
                return nn.functional.mse_loss(preds, targets)

        results = manager.run_ablation(DummyLoader(), DummyLoss(), torch.device("cpu"))
        assert "swin" in results
        assert "grm" in results
        assert "loss" in results["swin"]
        assert "baseline_loss" in results["swin"]
        assert "relative_drop_percent" in results["swin"]

    def test_save_and_restore_original_state(self):
        model = SimpleModel()
        config = {
            "ablation": {
                "modules": ["swin"],
                "strategy": "replace_with_identity",
            }
        }
        manager = AblationManager(model, config)

        original_weight = model.swin.weight.clone()
        manager._save_original_state()
        model.swin.weight.data.fill_(999.0)
        manager._restore_original_state()
        assert torch.allclose(model.swin.weight, original_weight)
