"""SQLite data model: curated policies, vector index, audit and human review queue."""
import sqlite3
from pathlib import Path

SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS policies (
 policy_id TEXT PRIMARY KEY, title TEXT NOT NULL, body TEXT NOT NULL,
 keywords TEXT NOT NULL, version TEXT NOT NULL, owner TEXT NOT NULL,
 effective_from TEXT NOT NULL, effective_to TEXT NOT NULL,
 approved INTEGER NOT NULL CHECK (approved IN (0, 1)), sha256 TEXT NOT NULL,
 updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS vectors (
 policy_id TEXT NOT NULL REFERENCES policies(policy_id) ON DELETE CASCADE,
 model TEXT NOT NULL, vector_json TEXT NOT NULL,
 PRIMARY KEY (policy_id, model)
);
CREATE TABLE IF NOT EXISTS review_queue (
 case_id TEXT PRIMARY KEY, category TEXT NOT NULL, status TEXT NOT NULL,
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
 reviewed_at TEXT, reviewed_by TEXT, decision_note TEXT,
 CHECK (status IN ('PENDING', 'APPROVED', 'REJECTED', 'CLOSED'))
);
CREATE TABLE IF NOT EXISTS audit_events (
 event_id TEXT PRIMARY KEY, decision TEXT NOT NULL, route_reason TEXT NOT NULL,
 source_ids TEXT NOT NULL, action_taken TEXT NOT NULL,
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS policy_links (
 from_id TEXT REFERENCES policies(policy_id), to_id TEXT REFERENCES policies(policy_id),
 relation TEXT NOT NULL, PRIMARY KEY (from_id, to_id, relation)
);
"""

def connect(path):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(str(p), timeout=10)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys=ON")
    db.executescript(SCHEMA)
    return db
