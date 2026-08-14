from typing import Optional

import numpy as np
from scipy.stats import pearsonr


class PearsonMetric:
    @staticmethod
    def compute(preds: np.ndarray, targets: np.ndarray) -> float:
        preds_flat = preds.flatten()
        targets_flat = targets.flatten()
        if len(preds_flat) < 2:
            return 0.0
        corr, _ = pearsonr(preds_flat, targets_flat)
        return float(corr) if not np.isnan(corr) else 0.0
