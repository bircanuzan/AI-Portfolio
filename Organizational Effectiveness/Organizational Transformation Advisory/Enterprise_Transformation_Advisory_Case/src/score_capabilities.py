#!/usr/bin/env python3
"""Transparent organization-level capability triage for a synthetic consulting case.

The tool never produces employee-level assessments or automated personnel decisions.
Stdlib only. Use --input to replace the bundled example with an authorized aggregate dataset.
"""
from __future__ import annotations
import argparse
import csv
import sys
from pathlib import Path

DEFAULT_INPUT = Path(__file__).resolve().parents[1] / "data" / "capability_gap_baseline.csv"
FIELDS = (
    "capability_id", "domain", "capability", "owner", "current", "target",
    "criticality", "impacted_roles", "sample_size", "evidence_confidence"
)
OUTPUT_FIELDS = list(FIELDS) + ["gap", "priority_score", "priority_band", "evidence_gate"]


def score_rows(rows):
    """Validate, score and sort capability-level records; raises ValueError on bad data."""
    results = []
    seen = set()
    for row in rows:
        ident = (row.get("capability_id") or "").strip()
        if not ident or ident in seen:
            raise ValueError(f"Missing or duplicate capability_id: {ident!r}")
        seen.add(ident)
        if any(name not in row or str(row[name]).strip() == "" for name in FIELDS):
            raise ValueError(f"{ident}: missing required field")
        try:
            current, target = float(row["current"]), float(row["target"])
            criticality = int(row["criticality"])
            impacted = int(row["impacted_roles"])
            sample_size = int(row["sample_size"])
        except (ValueError, TypeError) as exc:
            raise ValueError(f"{ident}: invalid numeric field") from exc
        # This also rules out NaN because its comparisons are false.
        if not (0 <= current <= 5 and 0 <= target <= 5 and 1 <= criticality <= 5
                and impacted >= 0 and sample_size >= 0):
            raise ValueError(f"{ident}: values outside valid bounds")
        confidence = str(row["evidence_confidence"]).strip().lower()
        if confidence not in ("high", "medium", "low"):
            raise ValueError(f"{ident}: invalid evidence confidence")
        gap = round(max(0.0, target - current), 2)
        score = round(gap * criticality, 2)
        band = "HIGH" if score >= 8 else ("MEDIUM" if score >= 4 else "LOW")
        gate = "REVALIDATE" if confidence == "low" or sample_size < 10 else "SCREENED"
        item = {name: str(row[name]).strip() for name in FIELDS}
        item.update(gap=f"{gap:.2f}", priority_score=f"{score:.2f}",
                    priority_band=band, evidence_gate=gate)
        results.append(item)
    return sorted(results, key=lambda r: (
        -float(r["priority_score"]), -int(r["impacted_roles"]), r["capability_id"]
    ))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT,
                        help="CSV of aggregate organization-level capability maturity")
    args = parser.parse_args(argv)
    with args.input.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or any(field not in reader.fieldnames for field in FIELDS):
            raise ValueError(f"Required columns: {', '.join(FIELDS)}")
        assessed = score_rows(list(reader))
    writer = csv.DictWriter(sys.stdout, fieldnames=OUTPUT_FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(assessed)


if __name__ == "__main__":
    main()
