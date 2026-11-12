"""Deterministic fictional UAE motor-insurance claim review-routing demonstration.

Synthetic labels are generated from the same features the model sees; scores therefore
do not establish clinical/financial/insurance validity, fairness, or production readiness.
"""
from __future__ import annotations

import argparse
import json
import math
import random
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss, confusion_matrix, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

SEED = 20261030
ALLOWED_COLUMNS = {
    "claim_id", "claim_amount_aed", "policy_tenure_months", "prior_claim_count",
    "missing_doc_count", "anomaly_indicator", "submission_channel", "manual_review_required",
}
NUMERIC_FEATURES = [
    "claim_amount_aed", "policy_tenure_months", "prior_claim_count",
    "missing_doc_count", "anomaly_indicator",
]
CATEGORICAL_FEATURES = ["submission_channel"]
FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES
CHANNELS = ("app", "broker", "branch")
THRESHOLD = 0.40


def sigmoid(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-max(-30.0, min(30.0, value))))


def make_synthetic_claims(n: int = 480, seed: int = SEED) -> pd.DataFrame:
    """No source claims or personal information: all values are invented."""
    if n < 100:
        raise ValueError("At least 100 invented rows are required for this demo.")
    rng = random.Random(seed)
    rows = []
    for idx in range(1, n + 1):
        amount = round(rng.uniform(750.0, 50000.0), 2)
        tenure = rng.randint(1, 120)
        prior = rng.choices((0, 1, 2, 3), weights=(60, 25, 12, 3))[0]
        missing = rng.choices((0, 1, 2), weights=(74, 20, 6))[0]
        anomaly = 1 if rng.random() < 0.14 else 0
        channel = rng.choice(CHANNELS)
        # Artificial formula; NOT a learned insurance business rule.
        log_odds = (-2.4 + 0.00003 * amount - 0.005 * tenure
                    + 0.43 * prior + 0.82 * missing + 0.90 * anomaly
                    + (0.18 if channel == "broker" else 0.0))
        label = int(rng.random() < sigmoid(log_odds))
        rows.append({
            "claim_id": f"SIM-{idx:05d}",
            "claim_amount_aed": amount,
            "policy_tenure_months": tenure,
            "prior_claim_count": prior,
            "missing_doc_count": missing,
            "anomaly_indicator": anomaly,
            "submission_channel": channel,
            "manual_review_required": label,
        })
    return pd.DataFrame(rows)


def validate_data(df: pd.DataFrame) -> dict:
    unexpected = sorted(set(df.columns) - ALLOWED_COLUMNS)
    missing_columns = sorted(ALLOWED_COLUMNS - set(df.columns))
    errors = []
    if unexpected:
        errors.append(f"Unexpected columns (blocked): {unexpected}")
    if missing_columns:
        errors.append(f"Required columns missing: {missing_columns}")
    if not missing_columns:
        if df[list(ALLOWED_COLUMNS)].isnull().any().any():
            errors.append("Null values in required fields")
        if df["claim_id"].duplicated().any():
            errors.append("Duplicate claim_id")
        if (df["claim_amount_aed"] < 0).any():
            errors.append("Negative amount")
        if (df["policy_tenure_months"] < 0).any():
            errors.append("Negative policy tenure")
        if (df[["prior_claim_count", "missing_doc_count"]].lt(0).any().any()):
            errors.append("Negative count")
        if not df["submission_channel"].isin(CHANNELS).all():
            errors.append("Unexpected submission channel")
        for col in ("anomaly_indicator", "manual_review_required"):
            if not df[col].isin((0, 1)).all():
                errors.append(f"Invalid binary field {col}")
        if not df["claim_id"].astype(str).str.match(r"^SIM-[0-9]{5}$").all():
            errors.append("Unexpected claim identifier")
    return {"row_count": int(len(df)), "status": "pass" if not errors else "fail",
            "missing_columns": missing_columns, "unexpected_columns": unexpected,
            "errors": errors, "note": "Synthetic-only structural checks; not live data validation."}


def model_pipeline() -> Pipeline:
    numeric = Pipeline([("impute", SimpleImputer(strategy="median")),
                        ("scale", StandardScaler())])
    transform = ColumnTransformer([
        ("numeric", numeric, NUMERIC_FEATURES),
        ("channel", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
    ])
    return Pipeline([("transform", transform),
                     ("classifier", LogisticRegression(max_iter=2000, random_state=SEED))])


def run(output_dir: Path, n: int = 480) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    df = make_synthetic_claims(n)
    quality = validate_data(df)
    (output_dir / "data_quality.json").write_text(
        json.dumps(quality, indent=2) + "\n", encoding="utf-8"
    )
    if quality["status"] != "pass":
        raise ValueError(f"Data quality failure: {quality['errors']}")
    df.to_csv(output_dir / "synthetic_claims.csv", index=False)
    train, test = train_test_split(df, test_size=0.30, random_state=SEED,
                                   stratify=df["manual_review_required"])
    model = model_pipeline()
    model.fit(train[FEATURES], train["manual_review_required"])
    scores = model.predict_proba(test[FEATURES])[:, 1]
    assigned = (scores >= THRESHOLD).astype(int)
    truth = test["manual_review_required"].to_numpy()
    tn, fp, fn, tp = confusion_matrix(truth, assigned, labels=[0, 1]).ravel()
    # Submission channel is operational segmentation, NOT a protected-group fairness audit.
    segment_counts = {str(k): int(v) for k, v in test["submission_channel"].value_counts().sort_index().items()}
    summary = {
        "project_type": "Local synthetic demonstration; NOT insurance production",
        "seed": SEED,
        "records": int(n), "train_rows": int(len(train)), "holdout_rows": int(len(test)),
        "artificial_target_prevalence": round(float(df["manual_review_required"].mean()), 4),
        "threshold": THRESHOLD,
        "holdout_roc_auc": round(float(roc_auc_score(truth, scores)), 4),
        "holdout_precision_at_threshold": round(float(precision_score(truth, assigned, zero_division=0)), 4),
        "holdout_recall_at_threshold": round(float(recall_score(truth, assigned, zero_division=0)), 4),
        "holdout_brier_score": round(float(brier_score_loss(truth, scores)), 4),
        "confusion_matrix": {"true_negative": int(tn), "false_positive": int(fp),
                             "false_negative": int(fn), "true_positive": int(tp)},
        "holdout_channel_counts": segment_counts,
        "software": {"python": __import__("sys").version.split()[0],
                     "numpy": np.__version__, "pandas": pd.__version__,
                     "scikit_learn": sklearn.__version__},
        "limitations": [
            "All records and labels are artificially generated; accuracy is not externally valid.",
            "This is not proof of fairness or UAE regulatory compliance.",
            "No cloud/production deployment, LLM, insurance client, or automated adverse decision.",
            "Model does not establish ROI; holdout data are synthetic.",
        ],
    }
    (output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    sample = test[["claim_id", "submission_channel", "manual_review_required"]].copy()
    sample["review_score"] = scores.round(4)
    sample["suggested_route"] = np.where(assigned == 1, "human_review", "standard_queue")
    sample.sort_values("claim_id").head(25).to_csv(
        output_dir / "review_queue_sample.csv", index=False
    )
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="local_run")
    parser.add_argument("--rows", type=int, default=480)
    args = parser.parse_args()
    print(json.dumps(run(Path(args.output_dir), n=args.rows), indent=2))
