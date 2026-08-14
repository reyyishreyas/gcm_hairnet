import numpy as np
from typing import Optional


class PSNRMetric:
    def __init__(self, max_val: float = 1.0):
        self.max_val = max_val

    def compute(self, preds: np.ndarray, targets: np.ndarray) -> float:
        mse = np.mean((preds - targets) ** 2)
        if mse == 0:
            return 100.0
        return 20 * np.log10(self.max_val / np.sqrt(mse))
