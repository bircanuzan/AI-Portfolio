"""Transparent workforce capacity scenarios. Synthetic data; not an employment decision engine."""
import csv
import json
import math
from pathlib import Path

INPUT = Path(__file__).resolve().parents[1] / "data" / "synthetic_workload.csv"
FRACTIONS = ("productive_fraction", "eligible_case_share", "assistance_success_rate")

def model(row):
    r = {k: (float(v) if k != "team" else v) for k, v in row.items()}
    for key in FRACTIONS:
        if not 0 <= r[key] <= 1:
            raise ValueError(f"{key} must be between 0 and 1")
    for key in ("monthly_cases", "minutes_per_case", "current_fte", "paid_hours_per_fte", "human_review_minutes_per_eligible_case"):
        if r[key] < 0:
            raise ValueError(f"{key} cannot be negative")
    if r["productive_fraction"] == 0 or r["paid_hours_per_fte"] == 0:
        raise ValueError("Capacity assumptions must be positive")
    if r["variability_buffer"] < 1:
        raise ValueError("variability_buffer must be >=1")
    volume = r["monthly_cases"]
    base_hours = volume * r["minutes_per_case"] / 60
    # Unsuccessful AI attempts still require original work. Review applies to ALL eligible attempts.
    assist_h = volume * (
        r["minutes_per_case"] * (1 - r["eligible_case_share"] * r["assistance_success_rate"])
        + r["eligible_case_share"] * r["human_review_minutes_per_eligible_case"]
    ) / 60
    one_fte_capacity = r["paid_hours_per_fte"] * r["productive_fraction"]
    modelled_fte = math.ceil((assist_h * r["variability_buffer"]) / one_fte_capacity)
    return {
        "team": row["team"],
        "baseline_hours": round(base_hours, 1),
        "assisted_human_hours": round(assist_h, 1),
        "protected_available_hours": round(one_fte_capacity * r["current_fte"], 1),
        "modelled_fte_with_buffer": modelled_fte,
        "current_fte": int(r["current_fte"]),
        "modelled_fte_gap": modelled_fte - int(r["current_fte"]),
        "decision": "HUMAN_VALIDATION_REQUIRED",
    }

def load(path=INPUT):
    with open(path, encoding="utf-8", newline="") as handle:
        return [model(row) for row in csv.DictReader(handle)]

if __name__ == "__main__":
    print(json.dumps({"evidence": "SYNTHETIC SCENARIOS ONLY", "results": load()}, indent=2))
