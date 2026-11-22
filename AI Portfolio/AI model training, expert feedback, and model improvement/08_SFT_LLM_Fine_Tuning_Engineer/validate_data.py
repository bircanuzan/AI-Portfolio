"""Standard-library QA for synthetic SFT data. No model download required."""
from __future__ import annotations

import json
from pathlib import Path

LABELS = {"billing", "technical", "unknown"}
SPLITS = ("train", "validation", "test")


def read_rows(path: Path) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8") as source:
        for line_number, line in enumerate(source, start=1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSON") from exc
            if not isinstance(row, dict) or set(row) != {"id", "message", "intent"}:
                raise ValueError(f"{path}:{line_number}: expected id, message, intent only")
            if not all(isinstance(row[k], str) and row[k].strip() for k in row):
                raise ValueError(f"{path}:{line_number}: fields must be non-empty strings")
            if row["intent"] not in LABELS:
                raise ValueError(f"{path}:{line_number}: unexpected intent {row['intent']!r}")
            rows.append(row)
    if not rows:
        raise ValueError(f"{path}: empty split")
    return rows


def audit(directory: Path) -> dict[str, int]:
    ids: set[str] = set()
    messages: set[str] = set()
    counts = {}
    for split in SPLITS:
        rows = read_rows(directory / f"{split}.jsonl")
        for row in rows:
            identifier = row["id"]
            norm = " ".join(row["message"].casefold().split())
            if identifier in ids:
                raise ValueError(f"duplicate row ID: {identifier}")
            if norm in messages:
                raise ValueError(f"exact normalized message leaked across rows: {norm}")
            ids.add(identifier)
            messages.add(norm)
        counts[split] = len(rows)
    return counts


if __name__ == "__main__":
    print("Synthetic data audit:", audit(Path(__file__).parent / "data"))
