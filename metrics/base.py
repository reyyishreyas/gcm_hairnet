import numpy as np
from typing import Dict, List, Optional


class BaseMetric:
    def __init__(self, name: str):
        self.name = name
        self.values = []

    def reset(self) -> None:
        self.values = []

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        raise NotImplementedError

    def compute(self) -> float:
        raise NotImplementedError

    def __call__(self, preds: np.ndarray, targets: np.ndarray) -> float:
        self.update(preds, targets)
        return self.compute()


class MSEMetric(BaseMetric):
    def __init__(self):
        super().__init__("mse")
        self._sum = 0.0
        self._count = 0

    def reset(self) -> None:
        self._sum = 0.0
        self._count = 0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        self._sum += np.mean((preds - targets) ** 2)
        self._count += 1

    def compute(self) -> float:
        return self._sum / max(self._count, 1)


class MAEMetric(BaseMetric):
    def __init__(self):
        super().__init__("mae")
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


class R2Metric(BaseMetric):
    def __init__(self):
        super().__init__("r2")
        self._preds = []
        self._targets = []

    def reset(self) -> None:
        self._preds = []
        self._targets = []

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        self._preds.append(preds.flatten())
        self._targets.append(targets.flatten())

    def compute(self) -> float:
        preds = np.concatenate(self._preds)
        targets = np.concatenate(self._targets)
        ss_res = np.sum((targets - preds) ** 2)
        ss_tot = np.sum((targets - np.mean(targets)) ** 2)
        return 1 - ss_res / (ss_tot + 1e-8)


class AccuracyMetric(BaseMetric):
    def __init__(self, threshold: float = 0.5):
        super().__init__("accuracy")
        self.threshold = threshold
        self._sum = 0.0
        self._count = 0

    def reset(self) -> None:
        self._sum = 0.0
        self._count = 0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        preds_bin = (preds > self.threshold).astype(int)
        targets_bin = (targets > self.threshold).astype(int)
        self._sum += np.mean(preds_bin == targets_bin)
        self._count += 1

    def compute(self) -> float:
        return self._sum / max(self._count, 1)


class F1Metric(BaseMetric):
    def __init__(self, threshold: float = 0.5):
        super().__init__("f1")
        self.threshold = threshold
        self._tp = 0.0
        self._fp = 0.0
        self._fn = 0.0

    def reset(self) -> None:
        self._tp = 0.0
        self._fp = 0.0
        self._fn = 0.0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        preds_bin = (preds > self.threshold).astype(int)
        targets_bin = (targets > self.threshold).astype(int)
        self._tp += np.sum((preds_bin == 1) & (targets_bin == 1))
        self._fp += np.sum((preds_bin == 1) & (targets_bin == 0))
        self._fn += np.sum((preds_bin == 0) & (targets_bin == 1))

    def compute(self) -> float:
        prec = self._tp / (self._tp + self._fp + 1e-8)
        rec = self._tp / (self._tp + self._fn + 1e-8)
        return 2 * prec * rec / (prec + rec + 1e-8)


class PrecisionMetric(BaseMetric):
    def __init__(self, threshold: float = 0.5):
        super().__init__("precision")
        self.threshold = threshold
        self._tp = 0.0
        self._fp = 0.0

    def reset(self) -> None:
        self._tp = 0.0
        self._fp = 0.0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        preds_bin = (preds > self.threshold).astype(int)
        targets_bin = (targets > self.threshold).astype(int)
        self._tp += np.sum((preds_bin == 1) & (targets_bin == 1))
        self._fp += np.sum((preds_bin == 1) & (targets_bin == 0))

    def compute(self) -> float:
        return self._tp / (self._tp + self._fp + 1e-8)


class RecallMetric(BaseMetric):
    def __init__(self, threshold: float = 0.5):
        super().__init__("recall")
        self.threshold = threshold
        self._tp = 0.0
        self._fn = 0.0

    def reset(self) -> None:
        self._tp = 0.0
        self._fn = 0.0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        preds_bin = (preds > self.threshold).astype(int)
        targets_bin = (targets > self.threshold).astype(int)
        self._tp += np.sum((preds_bin == 1) & (targets_bin == 1))
        self._fn += np.sum((preds_bin == 0) & (targets_bin == 1))

    def compute(self) -> float:
        return self._tp / (self._tp + self._fn + 1e-8)


class IoUMetric(BaseMetric):
    def __init__(self, threshold: float = 0.5):
        super().__init__("iou")
        self.threshold = threshold
        self._tp = 0.0
        self._union = 0.0

    def reset(self) -> None:
        self._tp = 0.0
        self._union = 0.0

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        preds_bin = (preds > self.threshold).astype(int)
        targets_bin = (targets > self.threshold).astype(int)
        self._tp += np.sum((preds_bin == 1) & (targets_bin == 1))
        self._union += np.sum((preds_bin == 1) | (targets_bin == 1))

    def compute(self) -> float:
        return self._tp / (self._union + 1e-8)


class Evaluator:
    def __init__(self, metrics: Optional[List[BaseMetric]] = None, threshold: float = 0.5):
        if metrics is not None:
            self.metrics = metrics
        else:
            self.metrics = [
                MSEMetric(),
                MAEMetric(),
                R2Metric(),
                AccuracyMetric(threshold),
                F1Metric(threshold),
                PrecisionMetric(threshold),
                RecallMetric(threshold),
                IoUMetric(threshold),
            ]

    def reset(self) -> None:
        for m in self.metrics:
            m.reset()

    def update(self, preds: np.ndarray, targets: np.ndarray) -> None:
        for m in self.metrics:
            m.update(preds, targets)

    def compute_all(self) -> Dict[str, float]:
        return {m.name: m.compute() for m in self.metrics}

    def __call__(self, preds: np.ndarray, targets: np.ndarray) -> Dict[str, float]:
        self.update(preds, targets)
        return self.compute_all()
