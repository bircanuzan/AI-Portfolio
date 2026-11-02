# Dubai Holding JD-to-Portfolio Traceability

| Role requirement | Artefact | Implemented vs designed |
|---|---|---|
| ServiceNow SPM Demand, Project, Funding and Cost | SPM data dictionary; demand/project/cost CSVs | **SPM-aligned simulation only** |
| Portfolio intake / qualification / categorisation | demand pipeline; intake and weighted scoring | CSV-driven |
| Portfolio structures and single source of truth | shared canonical sample datasets; Python report | Demonstrated with CSV; no ServiceNow instance |
| Demand-to-Project/Product conversion | conversion IDs + product mapping | Sample records |
| Prioritisation, approvals and dispositions | RACI, forum calendar, approvals/dispositions | Documented + QA flags |
| Delivery governance, milestones, RAID | project milestones and RAID data; board report | Synthetic |
| Compliance, audit-ready BRD, UAT, security | BRD/UAT pack, approval matrix, exceptions | Documents only; no live approvals |
| Portfolio cost, funding and quality reviews | funding/cost sheet; QA cost gap | Python rule-based checks |
| Benefits tracking and business case continuity | benefits register + benefits design | Forecast vs actual carefully separated |
| Project closure, acceptance, EOL | product transition, closure/EOL policy | Defined only |
| AI CoE, PMO, Product Mgmt interface | stakeholder/RACI, intake and reporting | Operating model design |
| AI/ML lifecycle and Responsible AI | impact and release-readiness checkpoints | Controls designed |
| VP-ready pipeline, health and maturity reporting | generated Markdown dashboard | Runnable CSV-based demo |

## What was actually built
Synthetic portfolio data, written operating model, 6-stage delivery plan, structured demand and finance registers, evidence/RAID/benefits registers, a deterministic Python audit/report script and unit tests. No ServiceNow SPM certification, live product access, configuration or employer-client implementation.

## Responsible CV phrasing
Use: **“ServiceNow SPM-aligned AI portfolio governance project — functional workflow design and simulated reporting (GitHub portfolio).”**
Do not claim: **“hands-on ServiceNow SPM administrator,” “implemented SPM modules,”** or **“ServiceNow certified.”**

## Project execution scorecard
Demonstration findings are **synthetic**; portfolio data quality exceptions and finance gaps are intentionally seeded to show judgement and issue escalation.
