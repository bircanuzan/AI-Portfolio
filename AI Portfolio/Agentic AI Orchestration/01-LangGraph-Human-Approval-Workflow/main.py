"""LangGraph with explicit human-approval gate; no model or API credentials required."""
from typing import TypedDict
from langgraph.graph import END, START, StateGraph

class State(TypedDict):
    amount: float
    approved_by_human: bool
    risk: str
    decision: str

def classify(state: State) -> dict:
    return {"risk": "high" if state["amount"] > 1000 else "low"}

def route(state: State) -> str:
    return "review" if state["risk"] == "high" else "auto_approve"

def review(state: State) -> dict:
    return {"decision": "approved" if state["approved_by_human"] else "blocked_pending_approval"}

def auto_approve(state: State) -> dict:
    return {"decision": "approved_under_threshold"}

builder = StateGraph(State)
builder.add_node("classify", classify)
builder.add_node("review", review)
builder.add_node("auto_approve", auto_approve)
builder.add_edge(START, "classify")
builder.add_conditional_edges("classify", route, {"review": "review", "auto_approve": "auto_approve"})
builder.add_edge("review", END)
builder.add_edge("auto_approve", END)
app = builder.compile()

if __name__ == "__main__":
    for amount, approved in [(250.0, False), (1500.0, False), (1500.0, True)]:
        result = app.invoke({"amount": amount, "approved_by_human": approved,
                             "risk": "", "decision": ""})
        print(result)
        if amount > 1000 and not approved:
            assert result["decision"] == "blocked_pending_approval"
