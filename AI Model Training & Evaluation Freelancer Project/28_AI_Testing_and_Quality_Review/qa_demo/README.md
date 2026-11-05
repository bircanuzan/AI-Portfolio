# Runnable QA Lab — Local Mock HTTP API

**Purpose:** transition from document-only AI answer reviews to practical manual/API/integration/regression QA, based on software_group QA Engineer JD.

Python 3.10+; no third-party packages for the API and its tests. Local-only loopback service; no user accounts or employer data.

## Run (from repository root)
`python -m unittest discover -s 28_AI_Testing_and_Quality_Review/qa_demo -p 'test_api.py' -v`

To run a local API manually:
`python 28_AI_Testing_and_Quality_Review/qa_demo/service.py`
Default address `127.0.0.1:8765`. Stop with Ctrl+C.

Postman collection: `postman_collection.json` using local baseUrl `http://127.0.0.1:8765`. The examples use synthetic IDs and no tokens.

Optional Playwright UI smoke (not part of required CI): `python -m pip install playwright`, `python -m playwright install chromium`, then `python 28_AI_Testing_and_Quality_Review/qa_demo/playwright_smoke_optional.py`. It tests an **inline synthetic UI only**, not a web app, to demonstrate locators and validations.

## Test objectives
Create valid case; reject unconfirmed/disallowed categories, invalid JSON; check idempotent retry; retrieve case; inspect status codes and JSON schemas. Tests launch server on an automatically assigned localhost port and shut it down after tests.

## Limitations
Demo has no production OAuth, durable database, multi-user tenancy, LLM, external network or UI integration. It is not security audited. Track defects with the parent [traceability plan](../04_software_group_QA_Engineer_JD_Skills_Test_Plan_and_Defects.md).

## Next enhancements
Add pytest reports/JUnit artifacts, publish CI run link, Playwright tests against a sandbox browser application, contract testing, authenticated API, simulated rate limiting, mobile test harness and load/security testing (k6, JMeter) after building a safe sandbox. Never claim unrun tests.
