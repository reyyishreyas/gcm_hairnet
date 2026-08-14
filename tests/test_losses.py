import torch

from losses import MSELoss, L1Loss, FocalLoss, CombinedLoss


class TestLosses:
    def test_mse_loss(self):
        loss_fn = MSELoss()
        preds = torch.randn(4, 1, 32, 32)
        targets = torch.randn(4, 1, 32, 32)
        loss = loss_fn(preds, targets)
        assert loss.item() > 0

    def test_l1_loss(self):
        loss_fn = L1Loss()
        preds = torch.randn(4, 1, 32, 32)
        targets = torch.randn(4, 1, 32, 32)
        loss = loss_fn(preds, targets)
        assert loss.item() > 0

    def test_focal_loss(self):
        loss_fn = FocalLoss(alpha=0.25, gamma=2.0)
        preds = torch.randn(4, 1, 32, 32)
        targets = torch.rand(4, 1, 32, 32)
        loss = loss_fn(preds, targets)
        assert loss.item() >= 0

    def test_combined_loss(self):
        loss_fn = CombinedLoss(mse_weight=1.0, l1_weight=0.1, focal_weight=0.5)
        preds = torch.randn(4, 1, 32, 32)
        targets = torch.rand(4, 1, 32, 32)
        loss = loss_fn(preds, targets)
        assert loss.item() >= 0

    def test_combined_loss_components(self):
        loss_fn = CombinedLoss()
        components = loss_fn.get_components()
        assert "mse_loss" in components
        assert "l1_loss" in components
        assert "focal_loss" in components
        assert "total_loss" in components
