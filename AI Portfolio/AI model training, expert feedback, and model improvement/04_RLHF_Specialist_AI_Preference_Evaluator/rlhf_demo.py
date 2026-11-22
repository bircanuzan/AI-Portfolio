"""Toy RLHF workflow: preference dataset -> logistic reward -> KL-regularized action choice.

Educational standard-library demo only; no transformer reward model, PPO, model-weight
fine-tuning, external annotators, or live LLM evaluation is performed.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path

LABELS = {"billing", "technical", "unknown"}


def read_cases(path: Path) -> list[dict]:
    rows = [json.loads(s) for s in path.read_text(encoding="utf-8").splitlines() if s.strip()]
    seen_ids, seen_prompts = set(), set()
    if len(rows) < 2:
        raise ValueError("Need train and test preferences")
    for r in rows:
        if not {"id","split","prompt","expected_intent","chosen","rejected","rationale"} <= set(r):
            raise ValueError(f"Missing fields in {r}")
        if r["split"] not in {"train", "test"} or r["expected_intent"] not in LABELS:
            raise ValueError(f"Invalid split / expected label: {r['id']}")
        if r["id"] in seen_ids:
            raise ValueError(f"Duplicate identifier: {r['id']}")
        normalized = " ".join(r["prompt"].casefold().split())
        if normalized in seen_prompts:
            raise ValueError(f"Duplicate prompt: {r['id']}")
        if r["chosen"] == r["rejected"]:
            raise ValueError(f"Preference is not a comparison: {r['id']}")
        seen_ids.add(r["id"])
        seen_prompts.add(normalized)
    if not any(r["split"] == "train" for r in rows) or not any(r["split"] == "test" for r in rows):
        raise ValueError("Expected separate train and locked test splits")
    return rows


def features(response: str, expected_intent: str) -> tuple[float, float, float]:
    # Toy hand-engineered reward features, not an ML understanding of semantics.
    try:
        answer = json.loads(response)
    except (ValueError, TypeError):
        answer = None
    schema = isinstance(answer, dict) and set(answer) == {"intent"} and answer["intent"] in LABELS
    correct = bool(schema and answer["intent"] == expected_intent)
    unsafe_markers = ("send me your password", "share your password", "reveal your password")
    safe = not any(x in response.casefold() for x in unsafe_markers)
    return float(correct), float(schema), float(safe)


def sigmoid(x: float) -> float:
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    e = math.exp(x)
    return e / (1.0 + e)


def reward(weights: list[float], vector: tuple[float,float,float]) -> float:
    return sum(w * x for w, x in zip(weights, vector))


def fit_pairwise(train: list[dict], epochs: int = 400, lr: float = 0.12, l2: float = 0.01):
    weights = [0.0, 0.0, 0.0]
    pairs = []
    for r in train:
        good = features(r["chosen"], r["expected_intent"])
        bad = features(r["rejected"], r["expected_intent"])
        pairs.append(tuple(a - b for a, b in zip(good, bad)))
    if not any(any(x != 0.0 for x in pair) for pair in pairs):
        raise ValueError("No preference feature signal")
    for _ in range(epochs):
        gradient = [0.0, 0.0, 0.0]
        for diff in pairs:
            p = sigmoid(reward(weights, diff))
            for idx, x in enumerate(diff):
                gradient[idx] += (1.0 - p) * x / len(pairs)
        weights = [w + lr * (g - l2 * w) for w, g in zip(weights, gradient)]
    return weights


def preference_probability(weights: list[float], row: dict, temperature: float = 1.0) -> float:
    if temperature <= 0:
        raise ValueError("Temperature must be positive")
    chosen = features(row["chosen"], row["expected_intent"])
    rejected = features(row["rejected"], row["expected_intent"])
    return sigmoid((reward(weights, chosen) - reward(weights, rejected)) / temperature)


def evaluate(rows: list[dict], weights: list[float]) -> dict:
    outcomes = []
    for r in rows:
        p = preference_probability(weights, r)
        q = 1.0 - p
        # KL of 2-action preference-adjusted distribution from uniform reference (0.5,0.5)
        kl = p * math.log(2*p) + q * math.log(2*q)
        outcomes.append({"id": r["id"], "ranks_chosen_first": p > 0.5,
                         "reference_chosen_probability": 0.5,
                         "adjusted_chosen_probability": round(p, 4),
                         "kl_from_uniform_reference": round(kl, 4)})
    return {"pair_count": len(rows),
            "heldout_pairwise_ranking_accuracy": round(sum(x["ranks_chosen_first"] for x in outcomes)/len(outcomes), 4),
            "mean_adjusted_chosen_probability": round(sum(x["adjusted_chosen_probability"] for x in outcomes)/len(outcomes), 4),
            "mean_policy_kl_from_reference": round(sum(x["kl_from_uniform_reference"] for x in outcomes)/len(outcomes), 4),
            "cases": outcomes}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="outputs/evaluation.json")
    args = parser.parse_args()
    rows = read_cases(Path(__file__).with_name("cases.jsonl"))
    train = [r for r in rows if r["split"] == "train"]
    test = [r for r in rows if r["split"] == "test"]
    weights = fit_pairwise(train)
    report = {"evidence_level": "toy synthetic preference demo; not an LLM RLHF run",
              "method": "hand-engineered features, Bradley-Terry logistic preference fit, two-action KL-regularized reweighting",
              "train_pairs": len(train), "test_pairs": len(test),
              "learned_reward_feature_weights": dict(zip(("intent_correct", "strict_schema", "safe_marker"), [round(w, 4) for w in weights])),
              "holdout": evaluate(test, weights),
              "limitations": ["authored labels, no real annotators", "tiny dataset and engineered reward features", "not transformer/PPO/DPO", "simple unsafe marker, not a safety evaluator"]}
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
