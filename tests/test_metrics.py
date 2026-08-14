import numpy as np
import pytest
import torch

from metrics import RegressionMetrics, ClassificationMetrics


class TestRegressionMetrics:
    def test_mse(self):
        preds = np.array([1.0, 2.0, 3.0])
        targets = np.array([1.0, 2.0, 3.0])
        assert RegressionMetrics.mse(preds, targets) == 0.0

    def test_mae(self):
        preds = np.array([1.0, 2.0, 3.0])
        targets = np.array([1.5, 2.5, 3.5])
        assert RegressionMetrics.mae(preds, targets) == 0.5

    def test_r2_perfect(self):
        preds = np.array([1.0, 2.0, 3.0])
        targets = np.array([1.0, 2.0, 3.0])
        assert abs(RegressionMetrics.r2(preds, targets) - 1.0) < 1e-6

    def test_r2_worse_than_mean(self):
        preds = np.array([1.0, 1.0, 1.0])
        targets = np.array([1.0, 2.0, 3.0])
        r2 = RegressionMetrics.r2(preds, targets)
        assert r2 < 0.0


class TestClassificationMetrics:
    def test_accuracy_perfect(self):
        preds = np.array([0.9, 0.1, 0.8])
        targets = np.array([1.0, 0.0, 1.0])
        assert ClassificationMetrics.accuracy(preds, targets) == 1.0

    def test_iou_perfect(self):
        preds = np.array([0.9, 0.1, 0.8])
        targets = np.array([1.0, 0.0, 1.0])
        assert ClassificationMetrics.iou(preds, targets) >= 0.99
