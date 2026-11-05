"""Deterministic mock agent: configuration demonstration, NOT an LLM."""
POLICIES = {
    "annual leave": ("HR-LEAVE-01", "Request annual leave in the employee portal for manager review."),
    "employment letter": ("HR-LETTER-02", "Request an employment confirmation letter from the HR service desk."),
}
PRIVATE = ("salary", "payroll", "colleague", "passport", "medical")
REVIEW = ("approve", "override", "exception", "ignore instructions")
def respond(query, confirmed=False):
    q = query.casefold().strip()
    if not q:
        return {"decision": "clarify", "message": "What would you like to know?"}
    if any(x in q for x in PRIVATE):
        return {"decision": "refuse", "message": "I cannot disclose personal records. Contact authorized HR."}
    if any(x in q for x in REVIEW):
        return {"decision": "escalate", "message": "Human HR review is required for approvals and exceptions."}
    for keyword,(source,answer) in POLICIES.items():
        if keyword in q:
            return {"decision": "answer", "message": answer, "source_policy": source}
    if confirmed:
        return {"decision": "draft", "message": "Synthetic ticket draft only; none has been submitted."}
    return {"decision": "escalate", "message": "I do not have an approved source; human HR review is needed."}
if __name__=="__main__":
    for q in ["annual leave process", "approve my leave", "my colleague's salary", "relocation exception"]:
        print(q, respond(q))
