# HR AI & Automation Operations Lead - Mobility

**Project 26 — Independent portfolio case study aligned to Remote's EOR Operations / Mobility role.**

## What this project does
Design and test an **employee-mobility case-intake and HR automation operating model**. A fictional global EOR receives visa/work authorization cases and HR service requests; the system must route them, verify who can act, respect sensitive data, create safe human approval checkpoints and produce audit-ready metrics. The project is **not a live immigration decision, HRIS integration or payroll deployment**.

## What to open
1. [01 — EOR mobility discovery, As-Is/To-Be and business requirements](01_EOR_Mobility_Discovery_and_Process_Redesign.md) — full employee lifecycle, process bottlenecks, intake rules and goals.
2. [02 — HRIS, case, payroll integration and n8n blueprint](02_Low_Code_AI_Automation_and_Integration_Architecture.md) — architecture, maker/checker pattern, APIs/webhooks, retry and event queues.
3. [03 — Privacy, mobility compliance and observability](03_Global_Employment_Privacy_RBAC_Auditability.md) — sensitive data lifecycle, access controls, decision boundaries and trace model.
4. [04 — Analytics, SQL KPIs and value measurement](04_HR_Ops_Analytics_SQL_and_Impact.md) — scorecard, source definitions, governance and SQL.
5. [05 — DRI delivery and phased rollout](05_DRI_Rollout_RACI_Change_Enablement.md) — scout-to-scale roadmap, owners, handover and adoption.
6. [06 — Product backlog, user stories and UAT](06_Requirements_Edge_Cases_and_UAT.md).
7. [Runnable Python maker/checker workflow](src/mobility_workflow.py), [synthetic scenario evaluation](src/evaluate.py), [scenarios](data/scenarios.json) and [unit tests](tests/test_mobility.py).
8. [Operational KPIs from synthetic records](src/kpi_dashboard.py), [sample data](data/synthetic_case_operations.csv) and [SQL report](sql/operations_metrics.sql).
9. [Illustrative n8n sandbox starter](integrations/n8n_sandbox_workflow.json) — deliberately has NO private connectors, HRIS credentials, customer data or external side effects.

## Run
Python 3.10+, no packages, secrets or accounts needed:

~~~bash
python src/mobility_workflow.py
python src/evaluate.py
python src/kpi_dashboard.py
python -m unittest discover -s tests -v
~~~

## Match to Remote's requirements
EOR Mobility, global employment, HR Operations, HR shared services, process optimization, AI automation, n8n-style orchestration, Python, APIs and webhooks, maker/checker agents, approval gates, role-based access, retries/fallbacks, traceability, regulatory/privacy controls, SQL, Tableau/Sigma-ready KPIs, stakeholder leadership and the independent DRI operating model.

## Limitations
All input data and organisations are fictional. "Agents" in the runnable demonstration are **deterministic processing stages**, not trained LLMs; human review is always required for immigration/work authorization decisions and any consequential employment/payroll change. No real automation, SaaS integration, legal judgement, production performance or verified benefits result is claimed.

Role description: https://www.linkedin.com/jobs/view/4474617054/
