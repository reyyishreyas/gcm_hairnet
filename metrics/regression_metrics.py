import numpy as np
from typing import Dict, List


class RegressionMetrics:
    @staticmethod
    def mse(preds: np.ndarray, targets: np.ndarray) -> float:
        return float(np.mean((preds - targets) ** 2))

    @staticmethod
    def mae(preds: np.ndarray, targets: np.ndarray) -> float:
        return float(np.mean(np.abs(preds - targets)))

    @staticmethod
    def rmse(preds: np.ndarray, targets: np.ndarray) -> float:
        return float(np.sqrt(np.mean((preds - targets) ** 2)))

    @staticmethod
    def r2(preds: np.ndarray, targets: np.ndarray) -> float:
        ss_res = np.sum((targets - preds) ** 2)
        ss_tot = np.sum((targets - np.mean(targets)) ** 2)
        return float(1 - ss_res / (ss_tot + 1e-8))

    @staticmethod
    def mape(preds: np.ndarray, targets: np.ndarray) -> float:
        return float(np.mean(np.abs((targets - preds) / (targets + 1e-8))) * 100)

    @staticmethod
    def accuracy(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        preds_bin = (preds > threshold).astype(int)
        targets_bin = (targets > threshold).astype(int)
        return float(np.mean(preds_bin == targets_bin))

    @staticmethod
    def precision(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        preds_bin = (preds > threshold).astype(int)
        targets_bin = (targets > threshold).astype(int)
        tp = np.sum((preds_bin == 1) & (targets_bin == 1))
        fp = np.sum((preds_bin == 1) & (targets_bin == 0))
        return float(tp / (tp + fp + 1e-8))

    @staticmethod
    def recall(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        preds_bin = (preds > threshold).astype(int)
        targets_bin = (targets > threshold).astype(int)
        tp = np.sum((preds_bin == 1) & (targets_bin == 1))
        fn = np.sum((preds_bin == 0) & (targets_bin == 1))
        return float(tp / (tp + fn + 1e-8))

    @staticmethod
    def f1(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        precision = RegressionMetrics.precision(preds, targets, threshold)
        recall = RegressionMetrics.recall(preds, targets, threshold)
        return float(2 * precision * recall / (precision + recall + 1e-8))

    @staticmethod
    def iou(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        preds_bin = (preds > threshold).astype(int)
        targets_bin = (targets > threshold).astype(int)
        intersection = np.sum((preds_bin == 1) & (targets_bin == 1))
        union = np.sum((preds_bin == 1) | (targets_bin == 1))
        return float(intersection / (union + 1e-8))

    def __call__(self, preds, targets):
        """Make class callable"""
        return {
            "mse": self.mse(preds, targets),
            "mae": self.mae(preds, targets),
            "rmse": self.rmse(preds, targets),
            "r2": self.r2(preds, targets),
            "mape": self.mape(preds, targets),
            "accuracy": self.accuracy(preds, targets),
            "f1": self.f1(preds, targets),
            "precision": self.precision(preds, targets),
            "recall": self.recall(preds, targets),
            "iou": self.iou(preds, targets),
        }
