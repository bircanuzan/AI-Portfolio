"""Deterministic synthetic-data ingestion and quality gate. No external dependencies."""
import argparse
import csv
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path

FIELDS = ["event_id", "account_id", "occurred_at", "event_type", "units"]
ALLOWED_TYPES = {"query", "review", "approve"}


def assess(source):
    """Return accepted rows, quarantined row reasons, and basic provenance."""
    source = Path(source)
    accepted, quarantine, seen = [], [], set()
    with source.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDS:
            raise ValueError("Input column contract mismatch")
        for line, row in enumerate(reader, start=2):
            try:
                event_id = (row["event_id"] or "").strip()
                account_id = (row["account_id"] or "").strip()
                if not re.fullmatch(r"[A-Za-z0-9_-]+", event_id):
                    raise ValueError("invalid_event_id")
                if not re.fullmatch(r"[A-Za-z0-9_-]+", account_id):
                    raise ValueError("invalid_account_id")
                if event_id in seen:
                    raise ValueError("duplicate_event_id")
                timestamp = datetime.fromisoformat((row["occurred_at"] or "").replace("Z", "+00:00"))
                if timestamp.tzinfo is None:
                    raise ValueError("timezone_required")
                event_type = (row["event_type"] or "").strip()
                if event_type not in ALLOWED_TYPES:
                    raise ValueError("invalid_event_type")
                units = int(row["units"])
                if units < 0:
                    raise ValueError("negative_units")
                accepted.append({
                    "event_id": event_id, "account_id": account_id,
                    "occurred_at": timestamp.isoformat(), "event_type": event_type,
                    "units": units
                })
                seen.add(event_id)
            except (ValueError, TypeError, KeyError, OverflowError) as error:
                quarantine.append({"line": line, "reason": str(error)})
    total = len(accepted) + len(quarantine)
    quality = {
        "input_file": source.name,
        "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "processed_rows": total, "accepted_rows": len(accepted),
        "quarantined_rows": len(quarantine),
        "acceptance_rate": round(len(accepted) / total, 4) if total else 1.0,
        "schema": FIELDS, "source_type": "synthetic_demo"
    }
    return accepted, quarantine, quality


def run(source, output):
    accepted, quarantine, quality = assess(source)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    with (output / "clean_events.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(accepted)
    (output / "quarantine.json").write_text(
        json.dumps(quarantine, indent=2), encoding="utf-8")
    (output / "quality_report.json").write_text(
        json.dumps(quality, indent=2), encoding="utf-8")
    return quality


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.input, args.output), indent=2))
