"""Reproducible ML training, evaluation, leakage and shift audit on synthetic data."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, brier_score_loss, roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

SEED = 42
CAPACITY = 0.10
FEATURES = (
    "step_count",
    "queue_depth",
    "retrieval_confidence",
    "tool_error_rate",
    "estimated_latency_ms",
    "recent_handoffs",
)
LEAKY_FEATURE = "post_outcome_retry_count"
TARGET = "missed_sla"


def make_synthetic_data(rows: int = 3000, seed: int = SEED) -> pd.DataFrame:
    """Create ordered synthetic cases. Post-outcome field MUST NOT be used for prediction."""
    if rows < 300:
        raise ValueError("Use at least 300 rows for meaningful chronological slices.")
    rng = np.random.default_rng(seed)
    idx = np.arange(rows)
    shifted = idx >= int(rows * 0.85)
    step_count = rng.poisson(5 + 1.8 * shifted) + 1
    queue_depth = rng.poisson(4 + 3.0 * shifted)
    retrieval_confidence = rng.beta(6.0 - 2.0 * shifted, 3.0 + shifted)
    tool_error_rate = rng.beta(1.4 + 1.0 * shifted, 13.0 - 3.0 * shifted)
    estimated_latency_ms = np.clip(
        rng.normal(450 + 135 * shifted + 16 * step_count, 115), 40, 1800
    )
    recent_handoffs = rng.poisson(1.4 + 0.8 * shifted)

    log_odds = (
        -3.7
        + 0.17 * step_count
        + 0.065 * queue_depth
        + 2.1 * (1.0 - retrieval_confidence)
        + 4.7 * tool_error_rate
        + 0.0011 * (estimated_latency_ms - 450)
        + 0.22 * recent_handoffs
        + 0.6 * shifted
    )
    p = 1.0 / (1.0 + np.exp(-np.clip(log_odds, -20, 20)))
    missed_sla = rng.binomial(1, p)
    # This feature is known only AFTER the outcome; including it is target leakage.
    retries = rng.poisson(0.15 + 4.0 * missed_sla)

    frame = pd.DataFrame(
        {
            "event_time": pd.date_range("2024-01-01", periods=rows, freq="h"),
            "step_count": step_count,
            "queue_depth": queue_depth,
            "retrieval_confidence": retrieval_confidence,
            "tool_error_rate": tool_error_rate,
            "estimated_latency_ms": estimated_latency_ms,
            "recent_handoffs": recent_handoffs,
            LEAKY_FEATURE: retries,
            "shifted_period": shifted.astype(int),
            TARGET: missed_sla,
        }
    )
    return frame


def chronological_split(frame: pd.DataFrame):
    """Split chronologically; no random reshuffling or overlapping observations."""
    if not frame["event_time"].is_monotonic_increasing:
        raise ValueError("Input data must be sorted by event_time.")
    n = len(frame)
    first, second = int(n * 0.60), int(n * 0.80)
    return (
        frame.iloc[:first].copy(),
        frame.iloc[first:second].copy(),
        frame.iloc[second:].copy(),
    )


def valid_features(features) -> tuple[str, ...]:
    """Reject both explicit leakage and accidental undeclared feature inputs."""
    selected = tuple(features)
    if not selected:
        raise ValueError("At least one feature is required.")
    unknown = set(selected) - set(FEATURES)
    if unknown:
        raise ValueError(f"Non-predecision or unapproved features: {sorted(unknown)}")
    return selected


def new_model(name: str, seed: int = SEED):
    if name == "baseline":
        return DummyClassifier(strategy="prior")
    if name == "logistic":
        return make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
    if name == "gradient_boosting":
        return HistGradientBoostingClassifier(
            max_iter=120, max_leaf_nodes=15, l2_regularization=1.0,
            learning_rate=0.06, random_state=seed
        )
    raise ValueError(f"Unknown model: {name}")


def fit_model(name: str, train: pd.DataFrame, features=FEATURES, seed: int = SEED,
              labels=None, allow_leakage_demo: bool = False):
    selected = tuple(features) if allow_leakage_demo else valid_features(features)
    if allow_leakage_demo and set(selected) - (set(FEATURES) | {LEAKY_FEATURE}):
        raise ValueError("Unknown experiment features.")
    model = new_model(name, seed)
    y = train[TARGET].to_numpy() if labels is None else np.asarray(labels)
    model.fit(train.loc[:, list(selected)], y)
    return model


def evaluate(model, frame: pd.DataFrame, features=FEATURES,
             allow_leakage_demo: bool = False) -> dict:
    selected = tuple(features) if allow_leakage_demo else valid_features(features)
    if len(frame) == 0:
        return {"n": 0}
    score = model.predict_proba(frame.loc[:, list(selected)])[:, 1]
    y = frame[TARGET].to_numpy(dtype=int)
    k = max(1, int(np.ceil(len(frame) * CAPACITY)))
    # Stable sort creates deterministic ranking for constant-score baselines.
    highest = np.argsort(-score, kind="stable")[:k]
    positives = int(y.sum())
    metrics = {
        "n": len(frame),
        "positive_rate": float(np.mean(y)),
        "reviewed": int(k),
        "review_capacity_fraction": CAPACITY,
        "precision_at_capacity": float(np.mean(y[highest])),
        "recall_at_capacity": float(np.sum(y[highest]) / positives) if positives else None,
        "average_precision": float(average_precision_score(y, score)) if positives else None,
        "roc_auc": float(roc_auc_score(y, score)) if len(np.unique(y)) == 2 else None,
        "brier_score": float(brier_score_loss(y, score)),
    }
    return metrics


def corrupt_training_labels(labels, fraction: float, seed: int = SEED):
    """Ablation: flip a fixed portion of TRAIN labels, never validation/test labels."""
    if not 0 <= fraction <= 1:
        raise ValueError("fraction must be between zero and one")
    rng = np.random.default_rng(seed)
    corrupted = np.asarray(labels, dtype=int).copy()
    count = int(round(len(corrupted) * fraction))
    indices = rng.choice(len(corrupted), size=count, replace=False)
    corrupted[indices] = 1 - corrupted[indices]
    return corrupted


def selection_key(item: dict):
    """Select on validation only: maximize recall@10%, break ties using AP."""
    m = item["validation"]
    return (
        m["recall_at_capacity"] if m["recall_at_capacity"] is not None else -1.0,
        m["average_precision"] if m["average_precision"] is not None else -1.0,
    )


def run_experiment(rows: int = 3000, seed: int = SEED) -> dict:
    frame = make_synthetic_data(rows, seed)
    train, valid, test = chronological_split(frame)
    # All hyperparameters are fixed before inspecting the test holdout.
    candidates = {}
    trained = {}
    for name in ("baseline", "logistic", "gradient_boosting"):
        model = fit_model(name, train, seed=seed)
        trained[name] = model
        candidates[name] = {"validation": evaluate(model, valid)}
    chosen = max(candidates, key=lambda name: selection_key(candidates[name]))
    champion = trained[chosen]
    test_metrics = evaluate(champion, test)

    # Slices are evaluated without tuning a model or threshold to the test set.
    slices = {
        "pre_shift": evaluate(champion, test.loc[test["shifted_period"] == 0]),
        "shifted": evaluate(champion, test.loc[test["shifted_period"] == 1]),
    }

    # Controlled intervention: all else identical, but training labels corrupted.
    altered_y = corrupt_training_labels(train[TARGET].to_numpy(), fraction=0.10, seed=seed)
    noisy_model = fit_model(chosen, train, seed=seed, labels=altered_y)

    # Feature ablation uses the SAME model class and train/test partitions.
    ablated = tuple(f for f in FEATURES if f != "retrieval_confidence")
    ablation_model = fit_model(chosen, train, features=ablated, seed=seed)

    # Invalid by construction: outcome-derived feature contaminates training/eval.
    leaky_features = FEATURES + (LEAKY_FEATURE,)
    leaky_model = fit_model("logistic", train, features=leaky_features,
                            seed=seed, allow_leakage_demo=True)

    return {
        "experiment": "synthetic_workflow_sla_failure",
        "source": "synthetic_only_no_real_client_data",
        "seed": seed,
        "rows": rows,
        "prediction_time": "before_workflow_completion",
        "objective": "maximize recall among top-risk 10% under fixed human review capacity",
        "eligible_features": list(FEATURES),
        "forbidden_post_outcome_feature": LEAKY_FEATURE,
        "split": {
            "method": "chronological_60_20_20",
            "train": len(train), "validation": len(valid), "test": len(test),
            "train_end": str(train["event_time"].max()),
            "validation_start": str(valid["event_time"].min()),
            "validation_end": str(valid["event_time"].max()),
            "test_start": str(test["event_time"].min()),
        },
        "candidates_validation_only": candidates,
        "selected_on_validation": chosen,
        "locked_champion_test": test_metrics,
        "test_slices": slices,
        "stress_tests": {
            "label_noise_10pct_train_only": {
                "test": evaluate(noisy_model, test),
                "interpretation": "Holdout labels were never flipped; compare with champion."
            },
            "remove_retrieval_confidence_ablation": {
                "features": list(ablated), "test": evaluate(ablation_model, test),
                "interpretation": "Exploratory test-only comparison; do not use to select champion."
            },
            "intentional_target_leakage_INVALID": {
                "test": evaluate(leaky_model, test, leaky_features,
                                 allow_leakage_demo=True),
                "deployment_eligible": False,
                "reason": "post_outcome_retry_count is unavailable at prediction time."
            }
        },
        "review_outcome": {
            "production_approved": False,
            "reason": "Synthetic offline experiment; real data, live validation, monitoring, fairness and operational checks are required."
        }
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows", type=int, default=3000)
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--output-dir", default="artifacts")
    args = parser.parse_args()
    report = run_experiment(args.rows, args.seed)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    output = out_dir / "report.json"
    output.write_text(json.dumps(report, indent=2, allow_nan=False), encoding="utf-8")
    print(f"Wrote {output}. Champion: {report['selected_on_validation']}")
    print("Synthetic evaluation only. NOT production approved.")


if __name__ == "__main__":
    main()
