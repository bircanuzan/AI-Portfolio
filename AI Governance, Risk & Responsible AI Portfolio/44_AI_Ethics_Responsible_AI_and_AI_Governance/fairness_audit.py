#!/usr/bin/env python3
"""Analyse 20 invented output labels; no ML model is trained or queried.

This demonstrates transparent audit metrics and limits. It is NOT fairness
certification and has no universal legal compliance threshold.
"""
import argparse
import csv
from collections import defaultdict
from pathlib import Path


def read_rows(path):
    with Path(path).open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    if not rows:
        raise ValueError("Synthetic fairness input is empty")
    required = {"candidate_id", "synthetic_group", "job_qualified", "model_selected"}
    for row in rows:
        if not required.issubset(row):
            raise ValueError("Missing required input columns")
        if row["job_qualified"] not in ("0", "1") or row["model_selected"] not in ("0", "1"):
            raise ValueError("Labels must be 0 or 1")
    return rows


def audit_rows(rows):
    grouped = defaultdict(list)
    for row in rows:
        grouped[row["synthetic_group"]].append(row)
    metrics = {}
    for group, sample in sorted(grouped.items()):
        n = len(sample)
        selected = sum(int(r["model_selected"]) for r in sample)
        qualified = sum(int(r["job_qualified"]) for r in sample)
        true_selected = sum(
            int(r["job_qualified"]) * int(r["model_selected"]) for r in sample
        )
        false_rejected = qualified - true_selected
        metrics[group] = {
            "n": n,
            "selected": selected,
            "qualified": qualified,
            "false_rejected_qualified": false_rejected,
            "selection_rate": selected / n,
            "true_positive_rate": true_selected / qualified if qualified else None,
        }
    return metrics


def main():
    parser = argparse.ArgumentParser(description="Original synthetic fairness metrics lab")
    parser.add_argument("csv_path")
    args = parser.parse_args()
    metrics = audit_rows(read_rows(args.csv_path))
    for group, v in metrics.items():
        tpr = "N/A" if v["true_positive_rate"] is None else f'{v["true_positive_rate"]:.3f}'
        print(f'Group {group} | N={v["n"]} | selected={v["selected"]} | qualified={v["qualified"]} | selection_rate={v["selection_rate"]:.3f} | TPR={tpr}')
    if len(metrics) == 2:
        a, b = metrics.values()
        print("Absolute selection-rate gap: {:.3f}".format(abs(a["selection_rate"]-b["selection_rate"])))
        if a["true_positive_rate"] is not None and b["true_positive_rate"] is not None:
            print("Absolute qualified-selection (TPR) gap: {:.3f}".format(abs(a["true_positive_rate"]-b["true_positive_rate"])))
    print("Illustrative subgroup analysis only; use with lawful data, uncertainty intervals, root-cause review and human oversight.")


if __name__ == "__main__":
    main()
