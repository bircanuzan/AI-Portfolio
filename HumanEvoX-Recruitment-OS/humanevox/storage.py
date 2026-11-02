"""Single-user local SQLite pilot. No network or hosted multi-tenant guarantees."""
from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


@contextmanager
def connect(path: str):
    if path != ":memory:":
        Path(path).expanduser().parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys=ON")
    try:
        yield db
        db.commit()
    except BaseException:
        db.rollback()
        raise
    finally:
        db.close()


def initialize(db):
    db.executescript("""
        CREATE TABLE IF NOT EXISTS roles (
            id INTEGER PRIMARY KEY, title TEXT NOT NULL, department TEXT NOT NULL DEFAULT '',
            required TEXT NOT NULL, preferred TEXT NOT NULL DEFAULT '', created_at TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY, role_id INTEGER NOT NULL REFERENCES roles(id) ON DELETE CASCADE,
            full_name TEXT NOT NULL, email TEXT NOT NULL COLLATE NOCASE, source TEXT NOT NULL DEFAULT '',
            filename TEXT NOT NULL DEFAULT '', evidence TEXT NOT NULL, coverage INTEGER NOT NULL DEFAULT 0,
            stage TEXT NOT NULL DEFAULT 'New', consent INTEGER NOT NULL DEFAULT 0,
            recruiter_notes TEXT NOT NULL DEFAULT '', created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
            UNIQUE (role_id, email));
        CREATE TABLE IF NOT EXISTS assessments (
            id INTEGER PRIMARY KEY, candidate_id INTEGER NOT NULL REFERENCES candidates(id) ON DELETE CASCADE,
            competency TEXT NOT NULL, score INTEGER NOT NULL CHECK(score BETWEEN 0 AND 4),
            evidence TEXT NOT NULL, assessor TEXT NOT NULL, created_at TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY, candidate_id INTEGER NOT NULL REFERENCES candidates(id) ON DELETE CASCADE,
            title TEXT NOT NULL, due_at TEXT NOT NULL, completed INTEGER NOT NULL DEFAULT 0);
        CREATE TABLE IF NOT EXISTS activity (
            id INTEGER PRIMARY KEY, entity TEXT NOT NULL, entity_id INTEGER NOT NULL,
            action TEXT NOT NULL, detail TEXT NOT NULL, created_at TEXT NOT NULL);
    """)


def audit(db, entity: str, entity_id: int, action: str, detail: str):
    db.execute("INSERT INTO activity(entity,entity_id,action,detail,created_at) VALUES(?,?,?,?,?)",
               (entity, entity_id, action, detail[:350], now()))


def add_role(db, title: str, department: str, required: str, preferred: str) -> int:
    if not title.strip() or not required.strip():
        raise ValueError("Role title and essential criteria are required")
    cur = db.execute("INSERT INTO roles(title,department,required,preferred,created_at) VALUES(?,?,?,?,?)",
                     (title.strip(), department.strip(), required.strip(), preferred.strip(), now()))
    audit(db, "role", cur.lastrowid, "created", f"Role: {title[:100]}")
    return cur.lastrowid


def add_candidate(db, role_id: int, full_name: str, email: str, source: str,
                  filename: str, evaluation: dict, consent: bool) -> int:
    if not consent:
        raise ValueError("Documented lawful basis/permission is required before saving a candidate")
    if not full_name.strip() or "@" not in email or not email.rsplit("@", 1)[-1].count("."):
        raise ValueError("Valid name and email required")
    cur = db.execute("""INSERT INTO candidates
        (role_id,full_name,email,source,filename,evidence,coverage,consent,created_at,updated_at)
        VALUES(?,?,?,?,?,?,?,?,?,?)""",
        (role_id, full_name.strip(), email.strip().lower(), source.strip(), filename,
         json.dumps(evaluation, ensure_ascii=False), evaluation["summary"]["coverage_percent"],
         int(consent), now(), now()))
    audit(db, "candidate", cur.lastrowid, "added", "Document parsed; recruiter review required")
    return cur.lastrowid


def update_candidate(db, candidate_id: int, stage: str, notes: str):
    from .templates import STAGES
    if stage not in STAGES:
        raise ValueError("Invalid pipeline stage")
    old = db.execute("SELECT stage FROM candidates WHERE id=?", (candidate_id,)).fetchone()
    if old is None:
        raise ValueError("Candidate not found")
    db.execute("UPDATE candidates SET stage=?, recruiter_notes=?, updated_at=? WHERE id=?",
               (stage, notes.strip()[:2500], now(), candidate_id))
    audit(db, "candidate", candidate_id, "updated", f"Stage: {old['stage']} -> {stage}; notes edited")


def save_assessment(db, candidate_id: int, competency: str, score: int, evidence: str, assessor: str):
    if not competency.strip() or not evidence.strip() or not assessor.strip():
        raise ValueError("Competency, factual evidence and assessor are required")
    if not isinstance(score, int) or score not in range(5):
        raise ValueError("Score must be 0–4")
    db.execute("""INSERT INTO assessments(candidate_id,competency,score,evidence,assessor,created_at)
               VALUES(?,?,?,?,?,?)""", (candidate_id, competency.strip(), score, evidence.strip(), assessor.strip(), now()))
    audit(db, "candidate", candidate_id, "assessed", f"Human-rated competency: {competency[:80]}")


def add_task(db, candidate_id: int, title: str, due_at: str):
    if not title.strip():
        raise ValueError("Task name required")
    cur = db.execute("INSERT INTO tasks(candidate_id,title,due_at) VALUES(?,?,?)",
                     (candidate_id, title.strip()[:200], due_at))
    audit(db, "candidate", candidate_id, "task added", title[:100])
    return cur.lastrowid


def complete_task(db, task_id: int):
    row = db.execute("SELECT candidate_id FROM tasks WHERE id=?", (task_id,)).fetchone()
    if row is None:
        raise ValueError("Task not found")
    db.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))
    audit(db, "candidate", row["candidate_id"], "task completed", f"Task #{task_id}")


def delete_candidate(db, candidate_id: int):
    """Erase candidate record, related assessments and tasks; keep anonymized deletion event."""
    db.execute("DELETE FROM candidates WHERE id=?", (candidate_id,))
    db.execute("DELETE FROM activity WHERE entity='candidate' AND entity_id=?", (candidate_id,))
    audit(db, "system", 0, "candidate deleted", "Personal candidate record erased from active database")


def rows(db, sql: str, params: tuple = ()) -> list[dict]:
    return [dict(row) for row in db.execute(sql, params).fetchall()]


def csv_bytes(rows_: list[dict]) -> bytes:
    import csv
    from io import StringIO
    if not rows_:
        return b""
    buf = StringIO()
    writer = csv.DictWriter(buf, fieldnames=list(rows_[0]))
    writer.writeheader()
    # Protect against spreadsheet-formula injection in exports.
    for row in rows_:
        writer.writerow({k: "'" + v if isinstance(v, str) and v.lstrip().startswith(("=", "+", "-", "@")) else v
                         for k, v in row.items()})
    return buf.getvalue().encode("utf-8-sig")
