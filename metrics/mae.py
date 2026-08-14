import numpy as np
from typing import Optional


class MAEMetric:
    def __init__(self):
        self._sum = 0.0
        self._count = 0

    def reset(self) -> None:
        self._sum = 0.0
        self._count = 0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        self._sum += np.mean(np.abs(preds - targets))
        self._count += 1

    def compute(self) -> float:
        return self._sum / max(self._count, 1)

    @staticmethod
    def compute_static(preds: np.ndarray, targets: np.ndarray) -> float:
        return float(np.mean(np.abs(preds - targets)))
