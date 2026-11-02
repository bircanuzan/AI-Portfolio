"""Create fictional records only; safe to run more than once."""
from pathlib import Path
import os
import sqlite3
from humanevox.documents import extract_document
from humanevox.engine import analyze
from humanevox.storage import add_role, add_candidate, connect, initialize, rows, save_assessment

DB_PATH = os.environ.get("HUMANEVOX_DB", str(Path.home() / ".humanevox_recruitment_os" / "workspace.sqlite3"))
if __name__ == "__main__":
    with connect(DB_PATH) as db:
        initialize(db)
        role_title = "AI-enabled Talent Intelligence Consultant (synthetic demo)"
        old = rows(db, "SELECT id FROM roles WHERE title=?", (role_title,))
        rid = old[0]["id"] if old else add_role(db, role_title, "Recruitment", "recruitment, stakeholder management, excel", "python, power bi, workday")
        path = Path(__file__).parent / "sample_data" / "synthetic_cv.txt"
        evaluation = analyze(extract_document(path.name, path.read_bytes()), "recruitment, stakeholder management, excel", "python, power bi, workday")
        found = rows(db, "SELECT id FROM candidates WHERE role_id=? AND email=?", (rid, "aisha@example.test"))
        if found:
            print("Synthetic candidate already exists; leaving all data unchanged.")
        else:
            cid = add_candidate(db, rid, "Aisha Example (SYNTHETIC)", "aisha@example.test", "synthetic seed", path.name, evaluation, True)
            save_assessment(db, cid, "Stakeholder engagement (synthetic demonstration)", 3,
                            "Fictional role-play example only; not a verified person or assessment", "Demo Reviewer")
            print(f"Created synthetic demo role #{rid}, candidate #{cid}")
