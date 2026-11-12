"""Offline, deterministic *text* routing demo for a proposed voice AI service.

Not an ElevenLabs agent, speech model or API integration. Never processes real customer data.
"""
import re

FAQ = {
    "hours": "For current service hours, please consult the official service website.",
    "pricing": "Pricing can change. Please consult the approved pricing page.",
    "how_to_apply": "Please follow the application instructions on the official website.",
}
UNTRUSTED = re.compile(
    r"(ignore (all )?(previous|system) instructions|reveal .*secret|print .*token|bypass .*policy)",
    re.IGNORECASE,
)
PRIVATE = re.compile(
    r"(my account|my salary|my application status|my case|passport|national id|credit card|otp|one.time pass)",
    re.IGNORECASE,
)

def route(message):
    """Classify only general, non-personal requests; otherwise hand off."""
    if not isinstance(message, str):
        raise TypeError("Message must be text")
    q = message.strip().lower()
    if not q:
        return {"intent": "clarify", "response": "What can I help you with?", "escalate": False}
    if UNTRUSTED.search(q):
        return {"intent": "security", "response": "I cannot follow that request. I can connect you with a person.", "escalate": True}
    if PRIVATE.search(q):
        return {"intent": "sensitive", "response": "For account-specific information, I will direct you to an authorised team member.", "escalate": True}
    if any(token in q for token in ("human", "person", "agent", "operator", "representative")):
        return {"intent": "handoff", "response": "I can arrange a handoff to the support team.", "escalate": True}
    if any(token in q for token in ("opening hours", "open today", "working hours", "business hours")):
        return {"intent": "hours", "response": FAQ["hours"], "escalate": False}
    if any(token in q for token in ("price", "pricing", "cost", "fee")):
        return {"intent": "pricing", "response": FAQ["pricing"], "escalate": False}
    if any(token in q for token in ("how do i apply", "application instructions", "how to submit")):
        return {"intent": "how_to_apply", "response": FAQ["how_to_apply"], "escalate": False}
    return {"intent": "unknown", "response": "I do not have an approved answer. I can transfer you to a team member.", "escalate": True}

if __name__ == "__main__":
    samples = ["What are your opening hours?", "What are the fees?", "What is my application status?"]
    for sample in samples:
        print("USER:", sample)
        print("DEMO:", route(sample))
