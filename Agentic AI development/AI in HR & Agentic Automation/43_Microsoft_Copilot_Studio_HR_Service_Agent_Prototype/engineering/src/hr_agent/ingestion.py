"""Validated, idempotent sample-policy ETL. Record-level quarantine, hashes, vector index."""
import hashlib
import json
from datetime import date
from pathlib import Path
from .retrieval import hashed_vector

REQUIRED = ("policy_id","title","body","keywords","version","owner","effective_from","effective_to","approved")

def ingest(db, source_path):
    payload = json.loads(Path(source_path).read_text(encoding="utf8"))
    if not isinstance(payload,list): raise ValueError("Expected a list of policy records")
    seen=set();accepted=[];quarantined=[]
    for idx,p in enumerate(payload):
        pid = str(p.get("policy_id","(missing)")) if isinstance(p,dict) else "(not_object)"
        try:
            if not isinstance(p,dict): raise ValueError("not an object")
            missing=[f for f in REQUIRED if f not in p]
            if missing: raise ValueError("missing: "+",".join(missing))
            if pid in seen: raise ValueError("duplicate policy_id")
            seen.add(pid)
            if not pid.startswith("HR-POL-"): raise ValueError("unexpected policy id")
            if not p["approved"] is True: raise ValueError("not approved")
            start=date.fromisoformat(p["effective_from"]);end=date.fromisoformat(p["effective_to"])
            if end<start: raise ValueError("invalid dates")
            if not start <= date.today() <= end: raise ValueError("expired or not yet effective")
            if len(str(p["body"]))<60: raise ValueError("policy body too short")
            if not isinstance(p["keywords"],list) or not p["keywords"]: raise ValueError("keywords required")
            fingerprint=hashlib.sha256(json.dumps(p,sort_keys=True).encode()).hexdigest()
            vector = hashed_vector(" ".join([p["title"],p["body"]," ".join(p["keywords"])]))
            db.execute("""INSERT INTO policies(policy_id,title,body,keywords,version,owner,effective_from,effective_to,approved,sha256)
             VALUES(?,?,?,?,?,?,?,?,?,?) ON CONFLICT(policy_id) DO UPDATE SET
             title=excluded.title,body=excluded.body,keywords=excluded.keywords,version=excluded.version,
             owner=excluded.owner,effective_from=excluded.effective_from,effective_to=excluded.effective_to,
             approved=excluded.approved,sha256=excluded.sha256,updated_at=CURRENT_TIMESTAMP""",
             (pid,p["title"],p["body"],json.dumps(p["keywords"]),p["version"],p["owner"],p["effective_from"],p["effective_to"],1,fingerprint))
            db.execute("INSERT INTO vectors(policy_id,model,vector_json) VALUES(?,?,?) ON CONFLICT(policy_id,model) DO UPDATE SET vector_json=excluded.vector_json",
                       (pid,"sha256-lexical-v1",json.dumps(vector)))
            accepted.append(pid)
        except (ValueError,TypeError,KeyError) as exc:
            quarantined.append({"row":idx+1,"policy_id":pid,"reason":str(exc)})
    db.commit()
    return {"records_received":len(payload),"accepted":len(accepted),"accepted_ids":accepted,"quarantined":quarantined,"data_quality_rate":round(len(accepted)/len(payload),4) if payload else 0}
