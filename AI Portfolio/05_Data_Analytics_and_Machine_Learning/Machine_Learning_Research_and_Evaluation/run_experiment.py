"""Synthetic ML baseline comparison and subgroup evaluation.

Run: python run_experiment.py
Dependencies: numpy pandas scikit-learn
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, brier_score_loss, confusion_matrix, f1_score,
    precision_score, recall_score, roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

SEED = 42


def evaluate(y_true, pred, score):
    return {
        "accuracy": float(accuracy_score(y_true, pred)),
        "precision": float(precision_score(y_true, pred, zero_division=0)),
        "recall": float(recall_score(y_true, pred, zero_division=0)),
        "f1": float(f1_score(y_true, pred, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_true, score)),
        "brier": float(brier_score_loss(y_true, score)),
    }


def subgroup_diagnostics(y_true, pred, groups):
    output = {}
    for group in sorted(np.unique(groups)):
        mask = groups == group
        tn, fp, fn, tp = confusion_matrix(y_true[mask], pred[mask], labels=[0, 1]).ravel()
        output[str(group)] = {
            "support": int(mask.sum()),
            "true_positive_rate": float(tp / (tp + fn)) if tp + fn else None,
            "false_positive_rate": float(fp / (fp + tn)) if fp + tn else None,
        }
    return output


def main():
    x, y = make_classification(
        n_samples=1500, n_features=12, n_informative=7, n_redundant=2,
        weights=[0.75, 0.25], flip_y=0.04, random_state=SEED
    )
    # Synthetic audit cohort based on a feature threshold, NOT real demographics.
    cohort = np.where(x[:, 0] > np.median(x[:, 0]), "cohort_a", "cohort_b")
    indices = np.arange(len(y))
    train_idx, test_idx = train_test_split(
        indices, test_size=0.25, random_state=SEED, stratify=y
    )
    x_train, x_test = x[train_idx], x[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]

    models = {
        "majority_baseline": DummyClassifier(strategy="prior"),
        "logistic_regression": make_pipeline(
            StandardScaler(), LogisticRegression(max_iter=2000, random_state=SEED)
        ),
    }
    results = {
        "dataset": "synthetic sklearn.make_classification",
        "seed": SEED,
        "train_rows": int(len(train_idx)),
        "test_rows": int(len(test_idx)),
        "models": {},
        "notes": [
            "Subgroups are synthetic diagnostics, not protected demographic categories.",
            "No production or external benchmark claims.",
        ],
    }
    for name, model in models.items():
        model.fit(x_train, y_train)
        pred = model.predict(x_test)
        score = model.predict_proba(x_test)[:, 1]
        results["models"][name] = {
            "metrics": evaluate(y_test, pred, score),
            "subgroups": subgroup_diagnostics(y_test, pred, cohort[test_idx]),
        }
    Path("metrics.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(pd.DataFrame({n: v["metrics"] for n, v in results["models"].items()}).round(3))
    print("Saved metrics.json")


if __name__ == "__main__":
    main()
