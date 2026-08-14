import numpy as np
from typing import Optional


class RMSEMetric:
    def __init__(self):
        self._sum = 0.0
        self._count = 0

    def reset(self) -> None:
        self._sum = 0.0
        self._count = 0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        self._sum += np.sqrt(np.mean((preds - targets) ** 2))
        self._count += 1

    def compute(self) -> float:
        return self._sum / max(self._count, 1)

    @staticmethod
    def compute_static(preds: np.ndarray, targets: np.ndarray) -> float:
        return float(np.sqrt(np.mean((preds - targets) ** 2)))
