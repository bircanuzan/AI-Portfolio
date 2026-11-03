# Microsoft Copilot Studio — HR Service Agent & G42-Aligned AI/Data Engineering Lab

**Project 43 | HumanEvoX | 30 October 2026**

> **Current evidence status:** Working **local** JavaScript and Python/SQLite HR-policy prototypes, reproducible evaluation harness, local REST service and authored operational governance. OpenAI/LangChain, Microsoft Foundry (Azure Agent Foundry), n8n, PySpark/Databricks, Microsoft Fabric and Copilot Studio remain **optional integration code or implementation designs, not tested cloud deployments**. No enterprise customer, production AI model, paid API invocation, Azure resource, actual employee data, real human approval, or employment outcome is claimed.

## NEW — G42-aligned Python and data-engineering implementation

**[Open the engineering project — Python, SQL, RAG, REST, OpenAI/LangChain, Azure Foundry, n8n, PySpark, CI/CD](engineering/README.md)**

This second phase is mapped directly to the official [Inception42 / G42 Data Engineer vacancy dated 9 October 2026](https://jobs.g42.ai/Inception42/job/Abu-Dhabi-Data-Engineer-Abu/733373322/). Its goal is to translate an HR service and agent-governance problem into a more technical demonstration: source-quality ETL, SQLite storage, small local vector index, versioned citations, decision routing, human queue, REST API, unit tests and real executed evaluation records.

**What can be rerun today:**

```bash
cd engineering
python run_lab.py ingest
python run_lab.py ask --query "What is the annual leave policy?"
python run_lab.py eval
python -m unittest discover -s tests -v
```

- [Architecture and full pipeline](engineering/docs/ARCHITECTURE.md)
- [G42 requirement-by-requirement skill mapping](engineering/docs/G42_SKILL_MATRIX.md)
- [Actual recorded Python evaluation results](engineering/evidence/2026-10-30_python_local_evaluation.json)
- [Executed local HTTP smoke evidence](engineering/evidence/local_http_smoke.json)
- [Cloud integrations and limits](engineering/docs/CLOUD_DEPLOYMENT.md)
- [Risk controls and governance](engineering/docs/GOVERNANCE_SECURITY.md)
- [Interview demonstration](engineering/docs/DEMO_AND_INTERVIEW.md)

**Crucial distinction:** The implemented Python/SQL engine is **deterministic lexical retrieval with a rule-based policy decision router**. It is not a generative LLM agent, not production-grade semantic RAG and not Azure-hosted. Full OpenAI/LangChain and Azure Foundry adapters exist but have **not been executed** without a real account and credentials. See the [evidence register](engineering/docs/EVIDENCE_REGISTER.md).

## Phase 1 — original local JavaScript HR policy assistant (retained)

- [Working local JavaScript policy router](agent.js) and [browser interface](index.html)
- [28-case original JavaScript evaluation](evidence/2026-10-29_test_run.json), including 2 failures
- [Legacy JavaScript assessment findings](evidence/REVIEW_FINDINGS.md)
- [Copilot Studio tenant build guide — not yet completed](COPILOT_STUDIO_BUILD_GUIDE.md)
- [Power Automate human approval flow specification — not yet executed](POWER_AUTOMATE_FLOW_SPEC.md)
- [Security limitations](SECURITY_ASSURANCE.md)

## Evidence maturity and career positioning

The first local prototype demonstrated intent and policy routing. The new Python phase adds structured ETL/SQL, reproducible evaluation, API and optional cloud integration code. **Do not combine the two test populations as if they were one agent.** Do not claim that a test fixture score represents live AI accuracy, compliance, a Microsoft deployment or several years of engineering experience.

**Accurate description:** “I developed two runnable local HR-service prototypes, including a Python/SQLite versioned-policy retrieval system with an API, offline evaluation and human-review queue. I prepared cloud adapters for OpenAI/LangChain, Azure Foundry, n8n and Databricks and am progressing toward real hosted agent validation.”

Original UAE professional-services *sector* example with synthetic policies — **not a reference to a real client**. AI-assisted authoring was used; all deployment and skill claims are scoped to evidence. © 2026 Bircan Uzan.
