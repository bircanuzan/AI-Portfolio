"""Enable LANGSMITH_TRACING=true and set LANGSMITH_API_KEY to upload traces."""
from langsmith import traceable

@traceable(name="demo-approval-policy", run_type="chain")
def evaluate(amount: float, human_approved: bool) -> dict:
    """Business rule only: makes no call to a model."""
    status = ("needs_human_approval" if amount > 1000 and not human_approved
              else "approved")
    return {"amount": amount, "status": status}

if __name__ == "__main__":
    print(evaluate(1250, False))
    print(evaluate(800, False))
    assert evaluate(1250, False)["status"] == "needs_human_approval"
