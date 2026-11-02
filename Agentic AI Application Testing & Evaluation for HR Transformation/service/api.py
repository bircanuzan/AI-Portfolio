"""HumanEvoX HR policy pilot API. Synthetic data only; no HRIS writes.

Live AI inference requires a configured provider. Never silently label the
rule-based fallback as a genuine model call. The served answer remains sourced
from the approved synthetic policy while an LLM draft is separately evaluated.
"""
from __future__ import annotations
import asyncio
import logging
import os
import re
import secrets
import threading
import time
import uuid
from collections import defaultdict, deque
from pathlib import Path

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from agent import HRPolicyAgent

LOGGER = logging.getLogger("humanevox.hr_agent")
APP_ROOT = Path(__file__).resolve().parent
app = FastAPI(title="HumanEvoX HR Agent Pilot", docs_url=None, redoc_url=None, openapi_url=None)
POLICY_AGENT = HRPolicyAgent()
PROVIDERS = {"openai", "local"}
REQUESTS: dict[str, deque[float]] = defaultdict(deque)
LOCK = threading.Lock()
MAX_PER_MINUTE = 12
PII_PATTERN = re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}|\b(?:784[- ]?)?\d{4}[- ]?\d{4}[- ]?\d{3}[- ]?\d\b")

class ChatInput(BaseModel):
    question: str = Field(min_length=2, max_length=1000)

class ChatOutput(BaseModel):
    request_id: str
    outcome: str
    answer: str
    policy_ids: list[str]
    escalation_team: str | None
    provider: str
    model_called: bool
    draft_released: bool = False
    note: str

def active_provider() -> str:
    value = os.getenv("HUMANEVOX_MODEL_PROVIDER", "openai").strip().lower()
    return value if value in PROVIDERS else "invalid"

def model_configured(provider: str) -> bool:
    if provider == "openai":
        return bool(os.getenv("OPENAI_API_KEY"))
    if provider == "local":
        return bool(os.getenv("LOCAL_LLM_ENDPOINT"))
    return False

def require_auth(authorization: str | None) -> str:
    token = os.getenv("HUMANEVOX_APP_TOKEN", "")
    if len(token) < 24:
        raise HTTPException(503, "Private access has not been configured")
    supplied = authorization or ""
    if not supplied.startswith("Bearer ") or not secrets.compare_digest(supplied[7:], token):
        raise HTTPException(401, "Unauthorized", headers={"WWW-Authenticate": "Bearer"})
    return "private-pilot"

def apply_rate_limit(principal: str) -> None:
    now = time.monotonic()
    with LOCK:
        window = REQUESTS[principal]
        while window and now - window[0] > 60:
            window.popleft()
        if len(window) >= MAX_PER_MINUTE:
            raise HTTPException(429, "Pilot request limit reached; retry after one minute")
        window.append(now)

def is_restricted_identifier(text: str) -> bool:
    return bool(PII_PATTERN.search(text))

def infer(question: str, provider: str) -> dict:
    """Blocking model inference; called through a thread pool by async route."""
    if provider == "openai":
        from live_llm_agent import run_live
        item = run_live(question)
        return {"model_called": item.model_called, "model_outcome": item.outcome}
    if provider == "local":
        from local_open_weight_llm import call_real_llm, POLICIES
        outcome = POLICY_AGENT.run(question)
        if outcome.outcome != "DIRECT_ANSWER":
            return {"model_called": False, "model_outcome": outcome.outcome}
        policy = POLICIES[outcome.policy_ids[0]]
        draft, _ = call_real_llm(question, policy)
        return {"model_called": bool(draft), "model_outcome": outcome.outcome}
    raise RuntimeError("Unsupported model provider")

@app.middleware("http")
async def privacy_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'self'"
    return response

@app.get("/health")
def health():
    return {"status": "ok", "pilot": True, "synthetic_only": True,
            "model_provider": active_provider(),
            "model_configured": model_configured(active_provider())}

@app.get("/")
def index():
    return FileResponse(APP_ROOT / "static" / "index.html")

@app.get("/app.js")
def javascript():
    return FileResponse(APP_ROOT / "static" / "app.js", media_type="text/javascript")

@app.get("/style.css")
def css():
    return FileResponse(APP_ROOT / "static" / "style.css", media_type="text/css")

@app.post("/api/chat", response_model=ChatOutput)
async def chat(body: ChatInput, authorization: str | None = Header(default=None)):
    principal = require_auth(authorization)
    apply_rate_limit(principal)
    question = body.question.strip()
    if is_restricted_identifier(question):
        raise HTTPException(422, "Personal identifiers are not permitted in this synthetic pilot")
    provider = active_provider()
    if not model_configured(provider):
        raise HTTPException(503, "Real model provider is not configured; no inference was attempted")
    baseline = POLICY_AGENT.run(question)
    request_id = uuid.uuid4().hex
    if baseline.outcome != "DIRECT_ANSWER":
        called = False
    else:
        try:
            result = await asyncio.to_thread(infer, question, provider)
            called = result["model_called"]
            if not called:
                raise RuntimeError("Provider returned no real model completion")
        except Exception as exc:
            LOGGER.warning("model_inference_failed request_id=%s provider=%s error_type=%s",
                           request_id, provider, type(exc).__name__)
            raise HTTPException(502, "Live model inference failed; no AI-generated answer was served") from exc
    LOGGER.info("completed request_id=%s outcome=%s policy=%s model_called=%s",
                request_id, baseline.outcome, ",".join(baseline.policy_ids), called)
    return ChatOutput(request_id=request_id, outcome=baseline.outcome,
                      answer=baseline.answer, policy_ids=baseline.policy_ids,
                      escalation_team=baseline.escalation_team, provider=provider,
                      model_called=called,
                      note=("Model consulted, but only the approved policy source was served."
                            if called else "Handled by a deterministic safety or approval rule without an LLM call."))
