from typing import Optional

import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.csgraph import laplacian


class MoranMetric:
    @staticmethod
    def compute(preds: np.ndarray, targets: np.ndarray) -> float:
        try:
            x = targets.flatten()
            n = len(x)
            if n < 4:
                return 0.0
            
            mean = np.mean(x)
            x_centered = x - mean
            variance = np.var(x)
            if variance < 1e-8:
                return 0.0
            
            spatial_lag = np.zeros(n)
            grid_size = int(np.sqrt(n))
            for i in range(n):
                row, col = i // grid_size, i % grid_size
                neighbors = []
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < grid_size and 0 <= nc < grid_size:
                        neighbors.append(nr * grid_size + nc)
                if neighbors:
                    spatial_lag[i] = np.mean([x_centered[j] for j in neighbors])
            
            moran = np.sum(x_centered * spatial_lag) / (np.sum(x_centered ** 2) / n)
            return float(np.clip(moran, -1.0, 1.0))
        except Exception:
            return 0.0
