"""HMAC-chained SQLite audit demo. No prompts, PII or raw tokens logged."""
import hashlib
import hmac
import json
import os
import sqlite3
import time
import uuid
from pathlib import Path

class AuditLedger:
    def __init__(self,path=None,key=None):
        self.path=str(path or os.getenv("HCIA_AUDIT_DB","/tmp/hcia_audit.sqlite3"))
        self.key=key or os.getenv("HCIA_AUDIT_HMAC_KEY","")
        if len(self.key)<24:
            raise ValueError("Audit signing secret required")
        Path(self.path).parent.mkdir(parents=True,exist_ok=True)
        with sqlite3.connect(self.path) as db:
            db.execute("""CREATE TABLE IF NOT EXISTS event(
              seq INTEGER PRIMARY KEY AUTOINCREMENT,event_id TEXT UNIQUE,
              ts INTEGER,actor TEXT,role TEXT,entity TEXT,tool TEXT,status TEXT,
              latency_ms REAL,previous TEXT,mac TEXT)""")
    def sign(self,body):
        raw=json.dumps(body,sort_keys=True,separators=(",",":"))
        return hmac.new(self.key.encode(),raw.encode(),hashlib.sha256).hexdigest()
    def append(self,actor,entity,tool,status,elapsed):
        with sqlite3.connect(self.path,timeout=8) as db:
            db.execute("BEGIN IMMEDIATE")
            prev=db.execute("SELECT mac FROM event ORDER BY seq DESC LIMIT 1").fetchone()
            record={"event_id":uuid.uuid4().hex,"ts":time.time_ns(),
                    "actor":actor.actor_id,"role":actor.role,"entity":entity,
                    "tool":tool,"status":status,"latency_ms":round(elapsed,3),
                    "previous":prev[0] if prev else "GENESIS"}
            mac=self.sign(record)
            db.execute("""INSERT INTO event(event_id,ts,actor,role,entity,tool,status,
                          latency_ms,previous,mac) VALUES(?,?,?,?,?,?,?,?,?,?)""",
                       (*record.values(),mac))
            return record["event_id"]
    def verify(self):
        previous="GENESIS"; count=0
        with sqlite3.connect(self.path) as db:
            for row in db.execute("SELECT event_id,ts,actor,role,entity,tool,status,latency_ms,previous,mac FROM event ORDER BY seq"):
                body=dict(zip(("event_id","ts","actor","role","entity","tool","status","latency_ms","previous"),row[:-1]))
                if body["previous"]!=previous or not hmac.compare_digest(self.sign(body),row[-1]):
                    return {"valid":False,"checked":count}
                previous=row[-1];count+=1
        return {"valid":True,"checked":count}
