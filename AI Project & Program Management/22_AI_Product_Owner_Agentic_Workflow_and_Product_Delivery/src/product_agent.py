"""Offline agentic-workflow prototype. Rule-based; no LLM, HRIS or API calls."""
import re
POLICY={"hours":("General HR helpdesk hours are listed on the employee portal.","HR-FAQ-001"),
        "onboarding":("Onboarding steps are available in the approved new-joiner guide.","HR-FAQ-002")}
PRIVATE=re.compile(r"\b(my salary|my payroll|my bank|my visa|my employee id|passport|national id|payslip|otp)\b",re.I)
INJECTION=re.compile(r"ignore (all )?(previous|system) instructions|reveal .*secret|print .*token|bypass .*policy",re.I)
def answer(query, tools_available=True):
    if not isinstance(query,str):raise TypeError("Expected text")
    q=query.strip().lower()
    if not q:return {"status":"clarify","message":"Please ask a question.","source":None,"human":False}
    if INJECTION.search(q):return {"status":"blocked","message":"Unsafe instruction blocked; contact HR for assistance.","source":None,"human":True}
    if PRIVATE.search(q):return {"status":"sensitive","message":"Personal HR records require an authorized HR adviser.","source":None,"human":True}
    if any(w in q for w in ("human","representative","person","agent")):
        return {"status":"handoff","message":"A human HR adviser is required.","source":None,"human":True}
    if not tools_available:return {"status":"tool_failure","message":"Approved knowledge source unavailable; contact HR.","source":None,"human":True}
    key = "hours" if "hours" in q else ("onboarding" if ("onboard" in q or "new joiner" in q) else None)
    if key is None:return {"status":"unknown","message":"No approved answer; refer to an HR adviser.","source":None,"human":True}
    text,source=POLICY[key]
    return {"status":"answered","message":text,"source":source,"human":False}
if __name__=="__main__":
    for q in ("What are HR hours?","What is my salary?","How does onboarding work?"):
        print(q,answer(q))
