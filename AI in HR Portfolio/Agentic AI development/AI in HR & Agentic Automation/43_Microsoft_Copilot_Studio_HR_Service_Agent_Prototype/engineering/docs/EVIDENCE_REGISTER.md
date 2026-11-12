# Evidence register — executed vs not executed

Date: 30 October 2026. Industry reference: UAE professional services. All underlying HR policy examples are **original synthetic text**, not genuine company HR policy or UAE labour-law guidance.

## Executed local evidence
- Input: `data/policies.json`; five invented approved records (policy date/owner/version metadata).
- Data ETL: `python run_lab.py ingest`; produces accepted/quarantined counts, SHA-256 source record lineage and SQLite entries.
- Python runtime: SQLite SQL tables, deterministic decisions, source/version citations, vector lookups, human queue and minimal audit records.
- `python -m unittest discover -s tests -v` — offline logic tests. Raw console output is not a cryptographic attestation.
- `python run_lab.py eval` — calls the **real local Python function** once per `data/evaluation_cases.json` prompt. Actual responses and source hashes are in [`../evidence/2026-10-30_python_local_evaluation.json`](../evidence/2026-10-30_python_local_evaluation.json). The test case list is authored by the same project team, not independent adjudicators.
- The prior Project 43 JavaScript prototype and 28-case evidence remain separately in the root (`agent.js`, `evidence/2026-10-29_test_run.json`). Do not combine scores from different engines/datasets without describing which was run.

## What the current local results mean
They establish that a deterministic Python program executed, stored and retrieved synthetic policy data, followed specified routing on these authored prompts, produced source metadata and recorded queue requests. They do **NOT** establish that a generative agent answered correctly or that a SaaS product, Azure, Databricks, n8n, Copilot Studio or a production RAG retrieval system worked.

## External evidence required before claiming deployment
| Product | Need to retain | Status |
|---|---|---|
| Azure Foundry agent | Actual project/agent ID (redacted public), versions, SDK invocation response ID, model, region, trace/cost, cleanup | Not tested |
| OpenAI + LangChain | Actual response text, prompt, context, citations, model/embedding versions, safety review and token bill | Not tested |
| n8n | Imported workflow, connected API execution ID, webhook request/response, incident handling | Not tested |
| Databricks/PySpark | Job run, Spark/Delta output, quality exceptions and reconciliation | Not tested |
| Fabric | Pipeline run IDs, workspace, lakehouse data model and security review | Not tested |
| CI/GitHub Actions | Successful hosted run URL and artifact | Must confirm after commit |
| Human approval | Real authorised human approval record in an enterprise identity system | Not tested |
| Security/compliance | Pen test, RBAC/DLP, privacy impact, legal review, red-team | Not done |

## Current release decision
**HOLD** — an educational portfolio project, not a live service. The test-suite pass rate on narrow, developer-authored scenarios cannot establish production readiness. Independent holdout, multi-turn, adversarial, access, privacy, failure/retry, cost and non-functional tests are outstanding.
