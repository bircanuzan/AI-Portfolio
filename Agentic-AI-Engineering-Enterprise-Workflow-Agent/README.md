# Agentic AI Engineering — Enterprise Workflow Agent

**HumanEvoX engineering laboratory | Python + FastAPI + n8n | Project status: runnable engineering starter, NOT a production deployment**

## Business problem
A typical enterprise service team spends time locating policies, checking case status, routing exceptions and requesting manager approval. This project implements a bounded agent around these tasks with **retrieval grounded in local documents**, a **real HTTP client integration point** to a case-status API, and **separate human authorization** before any state-changing action.

**Case:** HR employee-service request handling; the architecture can be adapted to IT helpdesk, vendor onboarding or customer operations. All included documents, case identifiers and workflows are synthetic.

## What is implemented in source
- Python document ingestion/retrieval for versioned Markdown policies, with source references.
- Optional OpenAI-compatible LLM answer generation (requires a user-provided API key; no model output is fabricated). Without the key, the service responds with an explicitly labeled evidence-only preview rather than pretending an LLM was used.
- Allowlisted HTTPS case lookup using a separate external API; disabled by default until configured. Timeout and errors produce escalation instead of invented status.
- Creation of a **pending** ticket request in SQLite; a separate authenticated approver endpoint must explicitly authorize it. No external business system receives the action.
- FastAPI endpoints, structured event evidence, pytest cases, n8n webhook orchestration starter.
- Recorded evaluation and pilot templates clearly distinguishing intended tests from executed runs.

## Architecture
[View the system diagram and control boundaries](architecture/ARCHITECTURE.md)

## Start locally

~~~bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env              # manually configure environment variables
python -m pytest -q
uvicorn app:app --reload --port 8000
~~~

Environment variables must be loaded by your shell or deployment platform; this starter does not automatically read .env. For a model-backed answer, set LLM_API_KEY in your environment. For authorized approvals, set APPROVER_TOKEN to a long random secret. The demo does not include user login/authentication for the /run endpoint; **run locally only**, not on public internet.

~~~bash
curl -s http://127.0.0.1:8000/health
curl -s -H 'Content-Type: application/json' -d '{"question":"What is the leave approval process?"}' http://127.0.0.1:8000/run
curl -s -H 'Content-Type: application/json' -d '{"question":"submit a leave exception"}' http://127.0.0.1:8000/run
~~~

The second request creates a pending request only; it does not approve it. An authorized human sends POST /approve/{request_id} with header X-Approver-Token and body {"decision":"approve"}. This changes only a local SQLite demo record.

## Optional live integrations

1. **Case-status API:** set CASE_API_BASE=https://your-verified-service.example/api and CASE_API_TOKEN. The host is configured by the operator, never accepted from user prompts. A request mentioning CASE-123 can retrieve a case status from GET /cases/CASE-123. Use mock/synthetic cases until an authorization and data-protection agreement exists.
2. **LLM:** set LLM_API_KEY; optionally LLM_MODEL (default gpt-4o-mini) and LLM_BASE_URL (default https://api.openai.com/v1/chat/completions). A provider other than OpenAI must expose the compatible chat-completions schema. No model calls occur in offline tests.
3. **n8n:** import n8n/enterprise-agent-workflow.json into your own n8n instance, change http://host.docker.internal:8000/run for your development environment, and test webhook invocation. **This workflow is supplied as an importable starter; an executed n8n run is not yet evidenced.**

## Honest status and acceptance

| Item | Present in repository | What is NOT claimed |
|---|---|---|
| Python service and endpoint code | Yes | Cloud hosting or enterprise sign-off |
| Document retrieval and source citations | Yes | Validated accuracy on real policies |
| Case API integration adapter | Yes | Connected enterprise API |
| LLM adapter | Yes | Successful live LLM run before key is supplied |
| Human approval boundary | Yes | Corporate identity integration |
| Unit-test scripts | Yes | Passed CI until results are published |
| n8n import workflow | Yes | A recorded production workflow execution |
| Pilot & commercial materials | Yes | Paying client or signed pilot |

## Evaluation and evidence workflow
See [evaluation plan](evaluation/EVALUATION_PLAN.md), [evidence capture](evidence/README.md), [demo script](demo/RECORDING_SCRIPT.md) and [pilot pack](pilot/PILOT_PACK.md). Commit real transcript IDs, redacted traces, date, model/version, scenario rubric, unexpected failures and signed pilot milestones **after** execution. Never use personal employee records in a public repository.

## Career presentation
See [CAREER_EVIDENCE.md](CAREER_EVIDENCE.md). A GitHub project is a personal lab; a verified client project may be described as self-employed consulting only once it actually occurred.

**Author/project context:** HumanEvoX | https://humanevox.com | https://github.com/bircanuzan/AI-in-HR-Portfolio
