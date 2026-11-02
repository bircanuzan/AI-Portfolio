"""Synthetic learning KPI example for the independent programme portfolio.
Uses Python standard library only. This code has NOT been connected to any LMS.
"""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path

FIELDS = {"learner_id", "region", "role", "assigned", "completed",
          "assessment_score", "critical_error", "manager_observed"}

def parse_binary(raw: str, key: str) -> int:
    if raw not in {"0", "1"}:
        raise ValueError(f"{key} must be 0 or 1")
    return int(raw)

def summarize(rows: list[dict[str, str]], threshold: int = 20) -> dict:
    if not 0 <= threshold <= 25:
        raise ValueError("threshold must be between 0 and 25")
    if not rows:
        raise ValueError("Cannot summarize empty dataset")
    unique_ids: set[str] = set()
    enrolled = completed = assessed = passed = critical = observed = 0
    for index, row in enumerate(rows, start=2):
        missing = FIELDS - set(row)
        if missing:
            raise ValueError(f"row {index} missing fields {sorted(missing)}")
        uid = (row["learner_id"] or "").strip()
        if not uid or uid in unique_ids:
            raise ValueError(f"row {index} blank or duplicate learner_id")
        unique_ids.add(uid)
        a = parse_binary((row["assigned"] or "").strip(), "assigned")
        c = parse_binary((row["completed"] or "").strip(), "completed")
        m = parse_binary((row["manager_observed"] or "").strip(), "manager_observed")
        if c and not a:
            raise ValueError(f"row {index} completed without assignment")
        if m and not a:
            raise ValueError(f"row {index} observed without assignment")
        score_text = (row["assessment_score"] or "").strip()
        err_text = (row["critical_error"] or "").strip()
        if score_text and not c:
            raise ValueError(f"row {index} assessed without completion")
        if (bool(score_text) != bool(err_text)):
            raise ValueError(f"row {index} score and critical_error must be paired")
        if c and not score_text:
            raise ValueError(f"row {index} completion missing assessment score")
        enrolled += a
        completed += c
        observed += m
        if score_text:
            try:
                score = int(score_text)
            except ValueError as exc:
                raise ValueError(f"row {index} score must be an integer") from exc
            if not 0 <= score <= 25:
                raise ValueError(f"row {index} score outside 0..25")
            has_error = parse_binary(err_text, "critical_error")
            assessed += 1
            critical += has_error
            passed += int(score >= threshold and not has_error)
    if not enrolled:
        raise ValueError("No assigned learners")
    return {
        "disclaimer": "ALL RECORDS SYNTHETIC. NOT REAL TRAINING OUTCOMES.",
        "assigned": enrolled,
        "completed": completed,
        "completion_pct": round(completed / enrolled * 100, 1),
        "assessed": assessed,
        "passed": passed,
        "pass_pct_of_assessed": round(passed / assessed * 100, 1) if assessed else None,
        "critical_errors": critical,
        "manager_observed": observed,
        "manager_observation_pct": round(observed / enrolled * 100, 1),
        "proposed_targets": {"completion_pct": 85, "pass_pct_of_assessed": 80,
                             "manager_observation_pct": 75},
    }

def read_csv(path: str | Path) -> list[dict[str, str]]:
    with Path(path).open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", help="CSV of synthetic learners")
    parser.add_argument("--threshold", type=int, default=20)
    args = parser.parse_args()
    print(json.dumps(summarize(read_csv(args.csv_file), args.threshold),
                     indent=2, sort_keys=True))
