import numpy as np
from typing import Dict, List


class ClassificationMetrics:
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
        precision = ClassificationMetrics.precision(preds, targets, threshold)
        recall = ClassificationMetrics.recall(preds, targets, threshold)
        return float(2 * precision * recall / (precision + recall + 1e-8))

    @staticmethod
    def iou(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        preds_bin = (preds > threshold).astype(int)
        targets_bin = (targets > threshold).astype(int)
        intersection = np.sum((preds_bin == 1) & (targets_bin == 1))
        union = np.sum((preds_bin == 1) | (targets_bin == 1))
        return float(intersection / (union + 1e-8))

    @staticmethod
    def specificity(preds: np.ndarray, targets: np.ndarray, threshold: float = 0.5) -> float:
        preds_bin = (preds > threshold).astype(int)
        targets_bin = (targets > threshold).astype(int)
        tn = np.sum((preds_bin == 0) & (targets_bin == 0))
        fp = np.sum((preds_bin == 1) & (targets_bin == 0))
        return float(tn / (tn + fp + 1e-8))

    def __call__(self, preds, targets) -> Dict[str, float]:
        return {
            "accuracy": self.accuracy(preds, targets),
            "precision": self.precision(preds, targets),
            "recall": self.recall(preds, targets),
            "f1": self.f1(preds, targets),
            "iou": self.iou(preds, targets),
            "specificity": self.specificity(preds, targets),
        }
