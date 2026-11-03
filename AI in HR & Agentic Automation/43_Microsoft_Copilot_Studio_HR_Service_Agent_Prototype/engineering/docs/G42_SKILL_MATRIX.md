# G42 Inception42 Data Engineer — skills-to-evidence matrix

**Verified official role:** https://jobs.g42.ai/Inception42/job/Abu-Dhabi-Data-Engineer-Abu/733373322/ (posted 9 October 2026). Mapping is a portfolio learning checklist, **not a claim of job readiness**.

| G42 responsibility / qualification | Evidence created in Project 43 | Evidence maturity / explicit gap |
|---|---|---|
| Develop/deploy AI agents: Azure Agent Foundry | `integrations/azure/foundry_agent.py`: credential-gated creation and invocation of hosted prompt agent | **Not invoked**; subscription, RBAC, real Azure agent execution, model traces and deployment missing |
| OpenAI + LangChain | `integrations/openai_langchain.py`: `ChatOpenAI` and prompt chain, safety-gated source input | **Coded, unexecuted**; real model evaluation + billing required |
| n8n orchestration | Importable workflow candidate connecting webhook to local `/ask` | JSON validated; no actual n8n environment, trigger or execution history |
| RAG + vector databases | Ingest → SQLite vector table → hashed-vector cosine retrieval → cited answer | **Executed** lexical retrieval; no production vector DB; neural embedding path coded, unexecuted |
| Knowledge graph | Versioned policy nodes and relation edges stored/queryable in SQL | **Executed small SQL graph**, not large-scale knowledge graph reasoning |
| Scalable ETL/ELT + data architectures | Python ETL, source hashes, quality/quarantine, SQLite schema; Spark Delta template | **Executed small local ETL**; Spark/Delta large-data scaling not tested |
| Python / SQL | Source files, SQLite DDL, SQL queries, local tests | **Executed**; not benchmarked for scale or concurrency |
| PySpark / Databricks | `integrations/databricks/pyspark_policy_etl.py` | **Example only**; no Databricks workspace, Spark cluster or Delta trace |
| Microsoft Fabric | Lakehouse/Warehouse architecture and validation plan | **Design only**; no Fabric tenant or pipeline |
| REST APIs | stdlib HTTP server `/ask`, `/healthz`, `/review` | **Locally executable**; not deployed behind OAuth/TLS/rate limits |
| Governance / compliance | Case queues, source-version gate, withheld HR decisions, risk/QA documentation | **Conceptual + local rules**; independent security/legal review missing |
| CI/CD, MLOps, containers | GitHub Actions YAML, Dockerfile, evaluation harness | Tests run locally; CI workflow and container not verified in hosted runner |
| Big data / Kafka / Kubernetes | Tradeoffs and production migration plan documented | **Not implemented**; do not list as hands-on experience |
| 3+ years engineering experience | No evidence from this lab | **Not satisfied by a portfolio** |

## Interview positioning
“I expanded a human–AI workforce governance case into a working **local** Python/SQL HR policy-service demonstration. I implemented source validation, lexical retrieval, REST routing, safety-focused human queueing and repeatable test evidence. I also prepared but have **not yet executed** adapters for OpenAI/LangChain, Microsoft Foundry, n8n and PySpark.”

**Never claim:** “I deployed an agent on Azure”, “I delivered production Databricks pipelines”, “I have three years of AI engineering”, or “I assessed a live agent” until supported by genuine external evidence.
