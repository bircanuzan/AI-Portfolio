import json
import sqlite3
import pytest
from humanevox.storage import (connect, initialize, add_role, add_candidate, update_candidate, save_assessment,
                                add_task, complete_task, delete_candidate, rows, csv_bytes)
from humanevox.engine import analyze


def test_end_to_end(tmp_path):
    path = str(tmp_path / "test.db")
    with connect(path) as db:
        initialize(db)
        rid = add_role(db, "AI Recruitment Consultant", "Talent", "recruitment,python", "workday")
        eval_ = analyze("Recruitment expert with Python", "recruitment,python", "workday")
        with pytest.raises(ValueError):
            add_candidate(db, rid, "Example", "example@example.test", "demo", "test.txt", eval_, False)
        cid = add_candidate(db, rid, "Example Candidate", "EXAMPLE@example.test", "synthetic", "test.txt", eval_, True)
        with pytest.raises(sqlite3.IntegrityError):
            add_candidate(db, rid, "Duplicate", "example@example.test", "demo", "test.txt", eval_, True)
    with connect(path) as db:
        update_candidate(db, cid, "Review", "Ask for demonstrable examples")
        save_assessment(db, cid, "Role-specific evidence", 3, "Demonstrated test project", "Human assessor")
        tid = add_task(db, cid, "Manual follow-up", "2026-11-05")
        complete_task(db, tid)
        assert rows(db, "SELECT stage FROM candidates WHERE id=?", (cid,))[0]["stage"] == "Review"
        assert len(rows(db, "SELECT * FROM assessments")) == 1
        assert rows(db, "SELECT completed FROM tasks WHERE id=?", (tid,))[0]["completed"] == 1
        delete_candidate(db, cid)
        assert not rows(db, "SELECT * FROM candidates")
        assert not rows(db, "SELECT * FROM assessments")
        assert not rows(db, "SELECT * FROM activity WHERE entity='candidate' AND entity_id=?", (cid,))


def test_formula_safe_csv():
    result = csv_bytes([{"name": "=HYPERLINK(\"bad\")", "source": "+SUM(1,1)"}]).decode("utf-8-sig")
    assert "'=HYPERLINK" in result
    assert "'+SUM" in result
