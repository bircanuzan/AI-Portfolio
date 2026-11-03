# Recruiter-facing demo, reproducibility and truthful claims

## 5-minute hands-on walkthrough
1. Open the [engineering README](../README.md) and the G42 role mapping. Explain why the use case is HR services: your previous work includes human capability, assessment, process governance and digital transformation.
2. `python run_lab.py ingest` — demonstrate validated approved synthetic records, source hashes and no rejected rows; optionally modify a copy of the JSON to an expired/unapproved policy to show quarantine.
3. `python run_lab.py ask --query "What is the annual leave policy?"` — show cited version ID and exact synthetic content retrieved from SQLite.
4. `python run_lab.py ask --query "What is Sam's salary?"` and `python run_lab.py queue` — show it creates a **local** human-review ticket, never a data leak or external HR action.
5. `python run_lab.py eval --evidence evidence/new_local_run.json` — open the actual JSON with prompt, expected answer class, returned answer, citation and source code hash. Run `python -m unittest discover -s tests -v`.
6. Open the `integrations` folders to show the separate *unexecuted* OpenAI/LangChain, Microsoft Foundry, n8n and Databricks paths. Explain what Azure and MLOps evidence is still missing.

## Answer to the important interview question
**“Which AI agent did you actually test, what did it respond, and how did you capture the evidence?”**

“I executed an HR Service Agent **local Python decision/retrieval prototype** — not an LLM or Azure-hosted agent — against a set of approved synthetic policies. It returned an identified, versioned sample policy answer for a general leave-policy question and created an internal human review queue entry for sensitive salary requests. I recorded every actual prompt, model-engine label, response, source reference and test comparison into JSON, with source/test file hashes and separate repeatable unit tests. I prepared Azure Foundry and LangChain integrations but have not run them in a cloud tenant. The enterprise release decision is HOLD pending independent LLM, access, governance and integration tests.”

## CV-safe claim
> Developed and tested a local Python/SQLite HR policy assistant prototype with validated synthetic-data ingestion, source-referenced retrieval, REST interface, case escalation and reproducible evaluation; prepared implementation adapters for OpenAI/LangChain, Azure AI Foundry, n8n and Databricks, pending cloud validation.

## Do not say
- “Built and deployed a G42-grade autonomous AI agent.”
- “Configured Azure Foundry, Databricks and n8n” without real credentials and actual executions.
- “Achieved 100% AI accuracy.” The local test is deterministic and authored internally.
- “Implemented UAE-law-compliant HR decisions.” This is invented policy text, not legal or HRIS certification.

## Evidence images/video
Capture only **real** screen recordings of your own local CLI/API and subsequently verified Microsoft or n8n dashboards. No screenshots, video recording, external SaaS session or production outcome is represented as completed in this commit.
