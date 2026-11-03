# Organizational Effectiveness | Group Executive Decision & Control System

**HumanEvoX independent portfolio case** — a complete, *fictional* diversified-group operating model for the responsibilities of an Executive Director – Organisation Effectiveness. The supplied Dubai Holding role description is a **requirements benchmark**, not an employer engagement, proprietary framework or claim of work performed at Dubai Holding.

## Executive mandate
Make the connection between Group strategy, legal entity structure, organization design, work allocation, jobs/grades, approved positions, people cost, hiring controls, HR data and governance decisions demonstrable and auditable.

**Case context:** fictional Cedar Gulf Group: Group Corporate, Investment Portfolio and Infrastructure Portfolio. Baseline uses 9 authorized position records, 6 synthetic incumbents and 3 vacancies; yearly cost assumptions, scoring thresholds and approval routing are explicitly fictional and configurable. No employee/candidate data or enterprise APIs are used.

## A single integrated project with ten differentiated workstreams

| Workstream | Decision / evidence |
|---|---|
| [01 — People Strategy & Governance](01_People_Strategy_and_Governance/README.md) | Group People Strategy cascade, scorecards, committee rights, department budget and cross-vertical commitments |
| [02 — Organisation Design & Transformation](02_Organisation_Design_and_Restructuring/README.md) | Design principles, activity analysis, service catalogues, spans/layers, current–future options, restructure costs and change control |
| [03 — Job Architecture & Evaluation](03_Job_Architecture_and_Evaluation/README.md) | Job families, role profiles, skills, an illustrative point-factor evaluation, grade parity and JD governance |
| [04 — Strategic Workforce Planning](04_Workforce_Planning_and_People_Cost/README.md) | Approved-position ledger, headcount and workforce mix scenarios, loaded people cost, Finance alignment |
| [05 — Hiring & Contingent Workforce Controls](05_Hiring_and_Contingent_Governance/README.md) | Hiring freeze, unbudgeted/rehire exceptions, TA vacancy review, vendor diligence and formal decision trails |
| [06 — People Data & Analytics](06_People_Data_and_Analytics/README.md) | Monthly HRIS/payroll/org chart reconciliation, data ownership, audit thresholds and Group reporting |
| [07 — AI Workforce Impact](07_AI_and_Automation_Workforce_Impact/README.md) | Task-level exposure, quality-reviewed capacity scenarios, human agency/consultation, non-automated decisions |
| [08 — New Entity & Geography](08_New_Entity_and_International_Expansion/README.md) | Entity-launch model: establishment dependencies, job architecture, reward, compliance, policies and hiring |
| [09 — ExCo & Human Capital Committee](09_Executive_Advisory_and_Governance/README.md) | Decision memo, escalation matrix, scenario options, risk register and first-90-days mandate |
| [10 — OE Function & Capability](10_OE_Team_Operating_Model/README.md) | OE team structure, capacity, specialist skill standards, operating cadence and performance evidence |

## Runnable evidence
- [Fictional data](data/synthetic_group_case.json) — group entities, posts, incumbents, payroll, hiring requests, vendors, activities and deliverables.
- [Offline Python control engine](src/oe_control_engine.py) — deterministic validation, grade calibration, people costs, HRIS–payroll differences, vacancy and request recommendations, AI exposure and strategy scorecard.
- [Unit tests](tests/test_oe_control_engine.py) — safety and consistency checks; run locally to obtain actual execution evidence.
- [Decision outputs and reproducibility](EVIDENCE_AND_REPRODUCIBILITY.md) — limitations, sample outcomes and next evidence gates.
- [Role requirement → evidence map](REQUIREMENTS_TRACEABILITY.md) — explicit executive accountability coverage.

Run from the repository root:

    python "Organizational Effectiveness/src/oe_control_engine.py"
    python -m unittest discover -s "Organizational Effectiveness/tests" -v

The engine **never approves hires, changes grades, restructures, processes salaries or takes action in an HR system**. It creates transparent recommendations / exception flags for designated people. Real Mercer IPE / Aon methodologies require licensing/training and cannot be represented as used here.

## Positioning and non-duplication
This is **Group-level decision governance** rather than the diagnostic/learning focus of [Organizational Development](../Organizational%20Development/), the Human–AI workforce architecture in [Workforce Transformation](../Workforce%20Transformation/), general dashboards in [People Analytics & HR Data](../People%20Analytics%20%26%20HR%20Data/), or the cross-platform implementation in [HR Technology & Digital Transformation](../HR%20Technology%20%26%20Digital%20Transformation/).

**Status:** independent authored design + runnable, reproducible local code and tests. No Dubai Holding relationship, real client implementation, actual job evaluation license, SAP/Oracle/Workday connection, Power BI deployment, approved organisational change, claimed benefit or financial saving.
