# Technical Program Management — Enterprise Fintech Integration Delivery

**Project 40 | Bircan Uzan | Portfolio demonstration using fictional data**

## Overview
This original technical-program-management case models two simultaneous enterprise integrations for a hypothetical financial-risk SaaS provider. It demonstrates balancing rigorous enterprise project governance with engineering delivery agility, as relevant to the [Sardine Technical Program Manager opportunity](https://jobs.ashbyhq.com/sardine/6e1a4fea-9953-4c1a-9ef7-ea60168a0c3f).

**Disclosure:** Atlas Bank, Beacon FinTech, dates, milestones, figures, risks and technical details are fictional. This is a learning/portfolio deliverable, **not client work, a Sardine implementation, access to Sardine's proprietary systems, or a claim of hands-on production fintech integrations**.

## Illustrative brief
- **Atlas Bank:** Event-schema mapping for a hypothetical risk event feed, sandbox integration, security approval, UAT and controlled cutover.
- **Beacon FinTech:** Webhook delivery, replay/idempotency, alert routing, sandbox testing, UAT and controlled cutover.
- **Reporting date:** 29 October 2026. Atlas mapping approval has slipped. Beacon is blocked by a high-severity duplicated-event defect.
- **TPM objective:** Maintain integrated plans, one accountable owner per decision, rapid risk escalation, disciplined scope control, customer confidence and evidence-based launch gates.

## Documents and practical deliverables

| Capability | Artifact |
| --- | --- |
| Delivery roadmap, milestones and PMO controls | [Program charter](docs/01_program_charter.md), [milestone register](data/milestones.csv) |
| Technical dependencies, APIs, security, observability | [Conceptual architecture](docs/02_technical_blueprint.md) |
| Cross-functional leadership and RACI | [Governance & RACI](docs/03_governance_raci.md) |
| Client-facing reporting and escalation | [Communications plan](docs/04_client_communication.md), [executive status](docs/07_executive_status.md) |
| Feature request triage and change control | [Change management](docs/05_feature_change_control.md), [feature register](data/feature_requests.csv) |
| Delivery risks, issues and dependencies | [RAID register](data/raid_register.csv) |
| UAT, go/no-go, cutover and hypercare | [Testing and release governance](docs/06_uat_cutover.md) |
| Data-driven decisions, cross-program capacity | [Capacity plan](data/capacity_plan.csv), [Python reporting tool](src/project_health.py) |
| Tested executable logic | [Unit tests](tests/test_project_health.py) |

## Sample management insight (fictional)
As of **2026-10-29**: 13 milestones are tracked; 6 are complete, 4 of those on time (66.7%); 2 incomplete milestones are past due; 1 open P1 issue blocks Beacon; illustrative team demand exceeds named capacity by 24 hours/week. Atlas is **Amber**, Beacon **Red**. Neither hypothetical client receives go-live approval until evidence and signed release gates are satisfied.

## Run the dashboard
From this folder (Python 3, standard library only):

```bash
python3 src/project_health.py --as-of 2026-10-29
python3 src/project_health.py --as-of 2026-10-29 --output program_health.json
python3 -m unittest discover -s tests -v
```

The CLI reads CSV registers, calculates milestone adherence, open overdue work, P1 blockers, blocked features, capacity gaps and an explainable per-client Red/Amber/Green status. Its metrics are derived from simulated input and should **not** be represented as client results.

## Tools, technologies and methods
- **Governance:** Integrated program plan, RACI, RAID, work breakdown structure, baseline/change control, critical-path monitoring, executive scorecard, SLA-style escalation.
- **Delivery:** SDLC coordination, Agile sprints with enterprise PMO, Product/Engineering prioritization, dependency sequencing, UAT and cutover controls.
- **Technical fluency (conceptual):** REST, event/webhook contracts, authentication, idempotency, retries, data minimization, event correlation, auditability and operational telemetry.
- **Analytics:** CSV, Python, metrics QA, portfolio capacity and red-amber-green logic.
- **Ethics:** No synthetic examples are presented as live fraud-prevention accuracy, SOC certification, regulatory validation or proprietary architecture.

## CV alignment
The tailored CV for this vacancy documents enterprise governance, cross-functional delivery, requirements gathering, cloud applications experience at Oracle and payment-system exposure at sector_organization. This project shows how those **transferable** capabilities could be used in a technical financial-risk integration setting.

[Project collection](../README.md) · [Back to portfolio index](../../README.md) · [HumanEvoX](https://humanevox.com)
