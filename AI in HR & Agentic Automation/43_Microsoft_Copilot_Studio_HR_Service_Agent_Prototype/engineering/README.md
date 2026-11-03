# Project 43 engineering implementation — G42 / Inception42 Data Engineer skill map

**HR Service Agent | Python · SQL · local RAG/vector retrieval · REST API · governance · optional OpenAI/LangChain, Microsoft Foundry, n8n and Databricks**

**Status (30 Oct 2026):** The offline engineering build and unit tests were executed with **synthetic UAE professional-services HR policies**. External OpenAI, Microsoft Foundry, n8n and Databricks workflows are **coded/integrated as optional adapters or prepared import artifacts but have not been provisioned, invoked or verified against live services**. This is *not* a production AI agent, client engagement, certified governance system or evidence of years of data engineering employment. AI-assisted source authoring is acknowledged.

**Role reference:** [Inception42 / G42 — Data Engineer, 9 Oct 2026](https://jobs.g42.ai/Inception42/job/Abu-Dhabi-Data-Engineer-Abu/733373322/). It requests scalable ETL/ELT, Python, SQL/PySpark, agents on Azure Agent Foundry/OpenAI/LangChain/n8n, RAG/embeddings/vector and knowledge graphs, REST APIs, Databricks/Fabric and CI/CD/MLOps. This portfolio illustrates *selected concepts*; it does not satisfy production experience or all listed requirements.

## Reproduce the executed offline system (Python 3.10+, standard library only)

From `engineering/`:

```bash
python run_lab.py ingest
python run_lab.py ask --query "What is the annual leave policy?"
python run_lab.py ask --query "What is Sam's salary?"
python run_lab.py eval --evidence evidence/my_run.json
python -m unittest discover -s tests -v
python run_lab.py serve
```

Local REST test from another terminal:

```bash
curl -s http://127.0.0.1:8000/healthz
curl -s -X POST http://127.0.0.1:8000/ask -H 'Content-Type: application/json' -d '{"query":"What is the annual leave policy?"}'
```

The API only binds to **127.0.0.1** and is **not ready for public access**. `/review` requires `HR_AGENT_REVIEW_TOKEN` (16+ chars) and is a local queue-record update only; no actual HR approval, email or document issue occurs.

## What is actually implemented

| Layer | Implementation | Evidence |
|---|---|---|
| ETL/ELT | Validates source records; quarantines invalid/unapproved/expired inputs; idempotent UPSERT and SHA-256 lineage | `src/hr_agent/ingestion.py`, `tests/test_local.py` |
| SQL model | SQLite tables for policies, versioned vectors, simple graph links, human review queue and minimal audit events | `src/hr_agent/storage.py` |
| Local RAG | Approved source retrieval, version/hash citation and abstention; 256-d hashed lexical vectors stored in SQLite | `src/hr_agent/retrieval.py`, `agent.py` |
| Knowledge graph | Explicit policy-to-policy SQL edges (not Neo4j or enterprise graph engine) | `src/hr_agent/graph.py`, `data/graph_edges.json` |
| API | `/healthz`, `/ask`, reviewer-gated `/review` on loopback | `src/hr_agent/api.py` |
| Human approval | Local queue with immutable `case_id`, PENDING → APPROVED/REJECTED/CLOSED, no downstream employment action | `src/hr_agent/agent.py` |
| Evaluation | Golden prompts, actual returned answer/decision/source, source/test hashes, summary, failure criteria | `run_lab.py`, `data/evaluation_cases.json`, `evidence/` |
| CI/CD | GitHub Actions offline test pipeline, artifact upload and Python container recipe | `.github/workflows/project43-engineering.yml`, `ops/Dockerfile` |

**Terminology:** The local runner is a **deterministic, retrieval-based conversational program**. Its hashed vectors are **lexical features**, not neural semantic embeddings, and SQLite is a **small local vector index**, not an enterprise vector database. The architecture is RAG-like but does not use an LLM until an optional external path is configured and genuinely executed. This distinction must remain explicit in applications/interviews.

## Optional real-model / cloud integration paths — NOT executed here

| Technology requested in G42 vacancy | Integration artifact | What it would take to verify |
|---|---|---|
| OpenAI + LangChain | `integrations/openai_langchain.py` implements `ChatOpenAI`, prompt chain, optional `OpenAIEmbeddings` and local-vector storage | API key, paid API usage, first real output/transcript, independent grading |
| Azure AI Foundry / Foundry Agent Service | `integrations/azure/foundry_agent.py` provisions/invokes a versioned hosted agent using `AIProjectClient` and Entra auth | Real Azure subscription, Foundry project, deployment, RBAC, verified successful run and logs |
| n8n workflow | `integrations/n8n/hr_agent_intake_workflow.json` import candidate: webhook → local REST API → JSON response | Running local n8n (same host), import, executed workflow and run-history capture |
| Azure Databricks / PySpark | `integrations/databricks/pyspark_policy_etl.py` Spark validation and Delta writing | Databricks/Spark cluster or compatible local install, dataset paths, actual job run |
| Microsoft Fabric | `docs/CLOUD_DEPLOYMENT.md` lakehouse mapping and implementation gates | Fabric workspace and successful pipeline/job evidence |
| Copilot Studio / Power Automate | Root folder's Copilot Studio and approval-flow guides | Actual tenant, agent transcript, flow run ID, human approval, permissions review |

**Avoid cost surprises:** no cloud/API call is made by `run_lab.py`. Optional integrations require explicit credentials and intentional commands. Do not commit secrets or actual personal/medical/employee records.

## Demonstrated results vs remaining gaps

See [`evidence/2026-10-30_python_local_evaluation.json`](evidence/2026-10-30_python_local_evaluation.json) for actual Python execution records and [`docs/EVIDENCE_REGISTER.md`](docs/EVIDENCE_REGISTER.md) for scope limitations. Passing developer-authored test prompts **does not** establish AI correctness, robustness, compliance or enterprise readiness. **Go-live recommendation: HOLD.**

## Read next

- [G42 requirement-by-requirement skill mapping](docs/G42_SKILL_MATRIX.md)
- [Architecture, data flow and technical decisions](docs/ARCHITECTURE.md)
- [Evidence register, test protocol and limitations](docs/EVIDENCE_REGISTER.md)
- [Security and agent governance (NIST AI RMF conceptual alignment)](docs/GOVERNANCE_SECURITY.md)
- [Azure / Databricks / Fabric integration runbook](docs/CLOUD_DEPLOYMENT.md)
- [Demonstration script and employment-safe wording](docs/DEMO_AND_INTERVIEW.md)

© 2026 Bircan Uzan / HumanEvoX. Original synthetic educational demonstration, AI-assisted authoring.
