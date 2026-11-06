"""Start with uvicorn main:app --reload; then open /docs."""
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Synthetic human-approval decision service")

class ReviewRequest(BaseModel):
    amount: float = Field(ge=0, description="Demo currency units")
    approved_by_human: bool = False

@app.get("/health")
def health() -> dict:
    return {"status": "ok"}

@app.post("/review")
def review(payload: ReviewRequest) -> dict:
    if payload.amount > 1000 and not payload.approved_by_human:
        return {"status": "blocked", "reason": "Human approval required"}
    return {"status": "approved", "reason": "Policy conditions satisfied"}
