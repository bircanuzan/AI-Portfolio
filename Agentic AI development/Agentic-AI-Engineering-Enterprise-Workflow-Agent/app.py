"""Local FastAPI gateway; protect with an external auth layer BEFORE any real deployment."""
import os
import secrets
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field
from agent import run, resolve

app = FastAPI(title="HumanEvoX Enterprise Workflow Agent (local prototype)")


class Query(BaseModel):
    question: str = Field(min_length=1, max_length=4000)


class Decision(BaseModel):
    decision: str


@app.get("/health")
def health():
    return {"status": "ok", "environment": "local_prototype"}


@app.post("/run")
def run_agent(body: Query):
    return run(body.question)


@app.post("/approve/{request_id}")
def approve(request_id: str, body: Decision, x_approver_token: str | None = Header(default=None)):
    expected = os.environ.get("APPROVER_TOKEN", "")
    if not expected or not x_approver_token or not secrets.compare_digest(expected, x_approver_token):
        raise HTTPException(status_code=403, detail="Approver credential required")
    if not resolve(request_id, body.decision):
        raise HTTPException(status_code=409, detail="Invalid decision or request not pending")
    return {"request_id": request_id, "decision": body.decision,
            "effect": "LOCAL_DATABASE_ONLY_NO_ENTERPRISE_ACTION"}
