#!/usr/bin/env python3
"""Synthetic process baseline vs pilot scorecard (Python standard library).

Illustration ONLY: not actual client, Stake, or employment performance data.
"""
import csv
import json
import sys
from pathlib import Path


def build_scorecard(path: str) -> dict:
    with Path(path).open(newline="", encoding="utf-8") as fh:
        records = list(csv.DictReader(fh))
    if not records:
        raise ValueError("Input CSV is empty")
    minutes_before = minutes_after = errors_before = errors_after = total_volume = 0.0
    for record in records:
        volume = float(record["monthly_volume"])
        manual = float(record["baseline_minutes_per_case"])
        pilot = float(record["pilot_minutes_per_case"])
        er_b = float(record["baseline_exception_rate"])
        er_a = float(record["pilot_exception_rate"])
        if volume < 0 or min(manual, pilot) < 0 or not (0 <= er_b <= 1 and 0 <= er_a <= 1):
            raise ValueError("Negative volume/time or exception rate outside [0, 1]")
        total_volume += volume
        minutes_before += volume * manual
        minutes_after += volume * pilot
        errors_before += volume * er_b
        errors_after += volume * er_a
    if minutes_before <= 0 or errors_before <= 0:
        raise ValueError("Baseline minutes and exceptions must be positive")
    return {
        "data_provenance": "SYNTHETIC ILLUSTRATIVE - NOT CLIENT RESULTS",
        "monthly_event_volume": total_volume,
        "staff_hours_before": round(minutes_before / 60, 2),
        "staff_hours_after": round(minutes_after / 60, 2),
        "staff_hours_difference": round((minutes_before - minutes_after) / 60, 2),
        "processing_time_reduction_pct": round(100 * (minutes_before - minutes_after) / minutes_before, 2),
        "expected_exception_events_before": round(errors_before, 2),
        "expected_exception_events_after": round(errors_after, 2),
        "expected_exception_event_reduction_pct": round(100 * (errors_before-errors_after) / errors_before, 2),
        "gross_labour_equivalent_usd_at_hypothetical_35_per_hr": round((minutes_before-minutes_after)/60*35, 2),
        "note": "Gross illustrative equivalent only: excludes implementation, support, licences and actual cash realisation",
    }


if __name__ == "__main__":
    data = sys.argv[1] if len(sys.argv)>1 else str(Path(__file__).parent.parent / "data" / "synthetic_before_after.csv")
    print(json.dumps(build_scorecard(data), indent=2))
