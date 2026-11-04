# Customer Operations Agent + Business-System Integration

**Independent portfolio project; fictional UAE insurance-style operations example.** Demonstrates automated task decomposition and routing across real local business-system components.

## What actually works
- CSV of synthetic cases is imported into **SQLite**.
- Python workflow reads a case, calculates which documentation is missing, routes an expired policy for human escalation, writes an audit event and constructs an unsent **RFC 822 email draft (.eml)**.
- An authenticated **localhost HTTP/JSON API** supports retrieving case status, triggering the workflow and recording a named human approval/rejection.
- Both a CLI demo and automated tests perform the real integration end-to-end.
- An **optional** external AI drafting adapter uses an explicit environment variable for OpenAI Responses API, but is **not run in tests**. The tested offline mode is deterministic automation, not a production LLM agent.

## Files
- [app.py](app.py) — core business workflow, CSV/SQLite, review and EML draft.
- [server.py](server.py) — localhost API service.
- [demo.py](demo.py) — executes integration; prints real local results.
- [test_lab.py](test_lab.py) — unit and API integration tests.
- [cases.csv](cases.csv) — synthetic business cases.
- [APPLICATION_EVIDENCE.md](APPLICATION_EVIDENCE.md) — evidence-based responses to all three hiring questions.
- [PRODUCTION_BLUEPRINT.md](PRODUCTION_BLUEPRINT.md) — future CRM/email/LLM architecture and governance.
- [CI](../../.github/workflows/ai-transformation-project-tests.yml) — tests and demo run on GitHub Actions.

## Run
Python 3.11 or later, standard library only. From this project directory:
    python -m unittest -v test_lab
    python demo.py

## Operating workflow
CSV > SQLite case store > rules/exception checks > EML draft (not sent) > human approval queue > audit events.
Client uses localhost HTTP API to create/retrieve case events. Real customers and external systems are never contacted.

**Skills:** Python, SQL/SQLite, data contracts, CSV, HTTP/JSON APIs, multi-step workflow orchestration, state management, integration tests, human-in-the-loop approvals, compliance exceptions, email draft generation, audit events, basic prompt design and AI integration architecture.

**Evidence honesty:** No deployment, no actual productivity or cost results, no validated insurance product advice, no full agentic LLM in the executed offline demonstration.
