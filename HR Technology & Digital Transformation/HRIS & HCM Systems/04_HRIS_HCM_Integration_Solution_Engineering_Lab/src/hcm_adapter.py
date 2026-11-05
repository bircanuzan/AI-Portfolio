"""Offline synthetic Oracle/SAP-shaped event normalization: NOT vendor integrations."""
from __future__ import annotations
import json
from datetime import date
from pathlib import Path
from typing import Any

BASE = Path(__file__).resolve().parents[1]
ALLOWED_ENTITIES = {"UAE_DEMO_01", "UAE_DEMO_02"}
ACTIONS = {"HIRE", "TRANSFER", "EXIT"}
FIELD_MAP = {
    "ORACLE_FUSION_HCM": {
        "worker_key": "person_number", "event_type": "action",
        "effective_date": "effective_date", "legal_entity": "legal_entity"
    },
    "SAP_SUCCESSFACTORS_EC": {
        "worker_key": "person_id_external", "event_type": "event",
        "effective_date": "effective_start_date", "legal_entity": "company"
    }
}

def normalize(batch: list[dict[str, Any]]) -> dict[str, Any]:
    """Validate simulated records. Accept means offline checks passed, not release."""
    accepted: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    seen: set[tuple[str, str, int]] = set()
    for position, row in enumerate(batch, 1):
        reasons: list[str] = []
        if not isinstance(row, dict):
            rejected.append({"row": position, "reasons": ["INVALID_RECORD_TYPE"]})
            continue
        source = row.get("source")
        if not isinstance(source, str) or source not in FIELD_MAP:
            rejected.append({"row": position, "reasons": ["UNKNOWN_SOURCE"]})
            continue
        version = row.get("version")
        event_id = row.get("event_id")
        if not isinstance(event_id, str) or not event_id.strip():
            reasons.append("MISSING_EVENT_ID")
        if type(version) is not int or version <= 0:
            reasons.append("INVALID_VERSION")
        if reasons:
            rejected.append({"row": position, "reasons": reasons})
            continue
        key = (source, event_id, version)
        if key in seen:
            reasons.append("REPLAY_DETECTED")
        seen.add(key)
        data = {out: row.get(inp) for out, inp in FIELD_MAP[source].items()}
        worker = data["worker_key"]
        if not isinstance(worker, str) or not worker.startswith("SYN-") or len(worker) > 40:
            reasons.append("INVALID_SYNTHETIC_WORKER_KEY")
        if not isinstance(data["event_type"], str) or data["event_type"] not in ACTIONS:
            reasons.append("UNSUPPORTED_EVENT")
        if not isinstance(data["legal_entity"], str) or data["legal_entity"] not in ALLOWED_ENTITIES:
            reasons.append("UNKNOWN_LEGAL_ENTITY")
        try:
            d = date.fromisoformat(data["effective_date"])
        except (ValueError, TypeError):
            reasons.append("INVALID_EFFECTIVE_DATE")
        else:
            if not isinstance(data["effective_date"], str) or d.isoformat() != data["effective_date"]:
                reasons.append("INVALID_EFFECTIVE_DATE")
        if row.get("approved") is not True:
            reasons.append("MISSING_HUMAN_APPROVAL")
        if reasons:
            rejected.append({"row": position, "event_id": event_id, "reasons": reasons})
            continue
        accepted.append({
            "source_system": source, "event_id": event_id,
            "worker_key": worker, "event_type": data["event_type"],
            "effective_date": data["effective_date"],
            "legal_entity": data["legal_entity"], "version": version,
            "human_approval_required": True, "status": "AWAITING_FINAL_HUMAN_SIGNOFF"
        })
    return {
        "received": len(batch), "accepted": len(accepted),
        "rejected": len(rejected), "accepted_events": accepted,
        "exceptions": rejected,
        "release_state": "HOLD_FOR_REVIEW"
    }

def main() -> None:
    rows = json.loads((BASE / "data" / "synthetic_events.json").read_text(encoding="utf-8"))
    print(json.dumps(normalize(rows), indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
