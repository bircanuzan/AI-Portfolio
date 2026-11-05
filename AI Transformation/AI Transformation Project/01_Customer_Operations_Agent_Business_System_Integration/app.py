"""Offline business workflow: actual CSV/SQLite/EML integration, never sends mail."""
import csv, json, os, sqlite3, pathlib
from email.message import EmailMessage
from datetime import datetime, timezone
from urllib.request import Request, urlopen

HERE=pathlib.Path(__file__).resolve().parent
SAMPLE=HERE/"cases.csv"

def db_open(path):
    db=sqlite3.connect(str(path))
    db.row_factory=sqlite3.Row
    db.executescript("""
      CREATE TABLE IF NOT EXISTS cases(
        case_id TEXT PRIMARY KEY, alias TEXT, email TEXT, policy_status TEXT,
        required_docs TEXT, received_docs TEXT, status TEXT DEFAULT 'NEW');
      CREATE TABLE IF NOT EXISTS audit(
        id INTEGER PRIMARY KEY, case_id TEXT, event TEXT, at TEXT, detail TEXT);
    """)
    return db

def seed(db,filename=SAMPLE):
    with open(filename,encoding="utf-8",newline="") as file:
        rows=list(csv.DictReader(file))
    for r in rows:
        if not r["case_id"].startswith("SYN") or not r["email"].endswith("@example.invalid"):
            raise ValueError("Only explicitly synthetic records allowed")
        db.execute("INSERT OR IGNORE INTO cases(case_id,alias,email,policy_status,required_docs,received_docs) VALUES(?,?,?,?,?,?)",
           tuple(r[k] for k in ("case_id","alias","email","policy_status","required_docs","received_docs")))
    db.commit()
    return len(rows)

def get_case(db,case_id):
    r=db.execute("SELECT * FROM cases WHERE case_id=?",(case_id,)).fetchone()
    if r is None: raise KeyError("Case not found")
    return dict(r)

def record(db,case_id,event,detail):
    db.execute("INSERT INTO audit(case_id,event,at,detail) VALUES(?,?,?,?)",
      (case_id,event,datetime.now(timezone.utc).isoformat(),json.dumps(detail)))

def llm_draft_opt_in(missing):
    """Optional provider integration: NOT run in CI, never send identifiable customer data."""
    key=os.environ.get("OPENAI_API_KEY")
    if not key: raise ValueError("No key. Tested offline mode is recommended.")
    req=Request("https://api.openai.com/v1/responses",
      data=json.dumps({
        "model":os.environ.get("OPENAI_MODEL","gpt-4.1-mini"),
        "instructions":"Draft a concise document-request email; do not assume insurance coverage. Human must review.",
        "input":"Missing document types: "+", ".join(missing), "max_output_tokens":120,
      }).encode(),
      headers={"Authorization":"Bearer "+key,"Content-Type":"application/json"},method="POST")
    with urlopen(req,timeout=15) as resp: value=json.load(resp)
    content=" ".join(v.get("text","") for x in value.get("output",[]) for v in x.get("content",[]) if v.get("type")=="output_text")
    if not content: raise ValueError("No LLM text")
    return content

def run_case(db,case_id,outbox,llm=False):
    case=get_case(db,case_id)
    needed=set(filter(None,(s.strip() for s in case["required_docs"].split("|"))))
    have=set(filter(None,(s.strip() for s in case["received_docs"].split("|"))))
    missing=sorted(needed-have)
    status="HUMAN_ESCALATION" if case["policy_status"]!="active" else (
       "PENDING_REVIEW" if missing else "MANUAL_COMPLETENESS_CHECK")
    filename=None
    if status=="PENDING_REVIEW":
        body=llm_draft_opt_in(missing) if llm else (
           "Hello,\n\nFor case "+case_id+", please provide: "+", ".join(missing)+
           ".\n\nThis is a draft awaiting human approval.\n\nCustomer Operations")
        message=EmailMessage()
        message["To"]=case["email"]
        message["From"]="no-send@demo.invalid"
        message["Subject"]="Requested documents: "+case_id
        message.set_content(body)
        outbox=pathlib.Path(outbox)
        outbox.mkdir(parents=True,exist_ok=True)
        filename=case_id+".eml"
        (outbox/filename).write_bytes(message.as_bytes()) # No SMTP or send API exists
    db.execute("UPDATE cases SET status=? WHERE case_id=?",(status,case_id))
    record(db,case_id,status,{"missing":missing,"llm_requested":bool(llm)})
    db.commit()
    return {"case_id":case_id,"status":status,"missing":missing,"email_draft":filename,
            "email_sent":False,"llm_executed":bool(llm and filename)}

def human_review(db,case_id,actor,decision):
    if not actor or decision not in ("approve","reject"):
        raise ValueError("Named reviewer and approve/reject decision required")
    case=get_case(db,case_id)
    if case["status"]!="PENDING_REVIEW":
        raise ValueError("Only draft review is available")
    status="APPROVED_DRAFT_FOR_MANUAL_USE" if decision=="approve" else "REJECTED_DRAFT"
    db.execute("UPDATE cases SET status=? WHERE case_id=?",(status,case_id))
    record(db,case_id,status,{"reviewer":actor})
    db.commit()
    return {"case_id":case_id,"status":status,"email_sent":False}

def audit_count(db,case_id):
    return db.execute("SELECT count(*) FROM audit WHERE case_id=?",(case_id,)).fetchone()[0]
