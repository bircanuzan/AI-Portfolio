"""HR request decision orchestrator: retrieve -> decide -> queue -> minimal audit.
No HRIS integration, real employee records, actual human notification or email actions.
"""
import json
import re
import uuid
from .retrieval import retrieve

CATEGORY_RULES = [
    ("HR-POL-001",r"working hours|office hours|core hours|collaboration time|work schedule"),
    ("HR-POL-002",r"annual leave|leave policy|request leave|vacation policy|holiday policy"),
    ("HR-POL-003",r"onboard|new joiner|induction checklist|joining checklist"),
    ("HR-POL-004",r"hybrid|remote work|work from home|telework"),
    ("HR-POL-005",r"office location|office address|where is the office|visitor instructions"),
]
BLOCKED = r"salary|payroll|bank account|bonus|emirates id|passport|medical|health record|visa|immigration|disciplin|terminat|another person|other employee|private|personal record|leave balance|remaining leave|my (leave|holiday|vacation) (quota|entitlement)|quota|eligib|entitl|contract|change my|edit my|hiring decision|candidate ranking|employee scoring"
ATTACK = r"ignore (all|previous)|override (system|rules)|bypass|system prompt|developer message|admin token|secret key|exfiltrat|jailbreak|all employee data|remove safeguards"
FRESHNESS = r"outdated|expired|changed yesterday|missing source|policy changed|new rule|no citation|uncertain policy"
LETTER = r"employment (confirmation |verification )?letter|letter of employment|experience letter|proof of employment|employment confirmation"

class Agent:
    def __init__(self, db): self.db=db

    def ask(self, query, mode="local"):
        if mode!="local": raise ValueError("Use optional integrations separately; local API never silently invokes a billable model")
        if not isinstance(query,str) or not query.strip() or len(query)>2500:
            return self._record("HUMAN_ESCALATION","invalid_or_empty_input","Please ask an HR colleague for help.",None,None)
        q=query.lower().strip()
        if re.search(ATTACK,q): return self._record("HUMAN_ESCALATION","adversarial_instruction","An authorised human must review this request. No protected records were accessed.",None,None)
        if re.search(BLOCKED,q): return self._record("HUMAN_ESCALATION","restricted_or_personal_hr_action","An authorised HR specialist must assess this request; I cannot access employee records or make employment decisions.",None,None)
        if re.search(FRESHNESS,q): return self._record("HUMAN_ESCALATION","uncertain_policy_freshness","The currently approved policy source cannot be verified for this request; ask the HR policy owner.",None,None)
        if re.search(LETTER,q):
            return self._record("APPROVAL_REQUIRED","employment_letter_draft","A human must confirm identity, review the details and separately approve any document. No document was created or sent.",None,"LETTER_DRAFT")
        category = next((pid for pid,rx in CATEGORY_RULES if re.search(rx,q)),None)
        if not category: return self._record("HUMAN_ESCALATION","unknown_intent","I cannot identify an approved answer; the request requires human review.",None,None)
        hit=retrieve(self.db,query+" "+category,policy_id=category,min_score=0.03)
        if hit is None: return self._record("HUMAN_ESCALATION","unavailable_or_unapproved_source","No current approved source was retrieved, so I will not guess.",None,None)
        p=hit["source"]
        return self._record("ANSWER","approved_policy_retrieval",p["body"]+f" [Synthetic source: {p['policy_id']} v{p['version']} — NOT company/UAE legal advice]",p, None, hit["retrieval_score"])

    def _record(self,decision,reason,answer,p,queue_category,score=None):
        event_id=str(uuid.uuid4()); case_id=None
        if decision in ("HUMAN_ESCALATION","APPROVAL_REQUIRED"):
            case_id=str(uuid.uuid4())
            self.db.execute("INSERT INTO review_queue(case_id,category,status) VALUES(?,?,?)",(case_id,queue_category or reason,"PENDING"))
        sources=[{"id":p["policy_id"],"version":p["version"],"sha256":p["sha256"]}] if p else []
        self.db.execute("INSERT INTO audit_events(event_id,decision,route_reason,source_ids,action_taken) VALUES(?,?,?,?,?)",
                        (event_id,decision,reason,json.dumps([x["id"] for x in sources]),"LOCAL_QUEUE_RECORD" if case_id else "NONE"))
        self.db.commit()
        return {"agent":"HR Service Agent Engineering Lab v1", "engine":"deterministic-python-rag-router", "decision":decision,
                "reason":reason,"answer":answer,"sources":sources,"retrieval_score":score,"event_id":event_id,
                "human_queue_case_id":case_id,"external_action_performed":False,
                "human_approval_executed":False,"limitations":"Synthetic policy library; no LLM, Microsoft, n8n, HRIS or real employee access in local mode"}

def review_case(db, case_id, reviewer, decision, note):
    if decision not in ("APPROVED","REJECTED","CLOSED"): raise ValueError("Invalid reviewer decision")
    if not reviewer or not note: raise ValueError("Reviewer identity and note required")
    row=db.execute("SELECT status FROM review_queue WHERE case_id=?",(case_id,)).fetchone()
    if row is None: raise KeyError("Unknown case")
    if row["status"]!="PENDING": raise ValueError("Case already reviewed; no repeat approval")
    db.execute("UPDATE review_queue SET status=?,reviewed_by=?,decision_note=?,reviewed_at=CURRENT_TIMESTAMP WHERE case_id=?",
               (decision,reviewer,note,case_id));db.commit()
    return {"case_id":case_id,"status":decision,"reviewed_by":reviewer,"message":"Local queue review only; no employment letter sent, no external workflow invoked"}
