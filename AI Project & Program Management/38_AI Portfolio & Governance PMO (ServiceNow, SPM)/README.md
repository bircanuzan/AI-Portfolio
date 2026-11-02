# AI Portfolio & Governance PMO (ServiceNow, SPM)

**Project 38 | Dubai Holding role-aligned, fictional enterprise AI portfolio case | Bircan Uzan | 29 October 2026**

> **Scope truth:** This is an original **ServiceNow Strategic Portfolio Management (SPM)-aligned simulation** using synthetic CSV records and standard-library Python. It is **not** a configured ServiceNow instance, live integration, product certification, client engagement or evidence of production ServiceNow SPM administration. The example SPM field mappings and stage gates require validation against the actual licensed ServiceNow release, modules, ACLs and local configuration.

## Business problem
An enterprise AI Centre of Excellence (CoE) has incoming use cases, pilots and live AI-enabled products. Portfolio Governance needs **one reportable source of truth** for pipeline, funding, demand-to-project/product conversion, stage-gate approvals, delivery RAID, model/data dependencies, audit evidence, closure and realised benefits.

## Portfolio case
Six synthetic AI demand submissions across HR, customer support, finance and operations enter an SPM-style pipeline. They are classified and scored, screened for missing business cases and impact evidence, presented to a governance forum and either approved, deferred or rejected. Approved demands are linked to projects or a product transition. Cost and funding are monitored alongside delivery controls and benefit hypotheses.

## Deliverables / navigation
1. [End-to-end charter, target operating model and delivery plan](docs/PROJECT_CHARTER_AND_DELIVERY.md)
2. [ServiceNow SPM process-to-record mapping and workflows](docs/SPM_PROCESS_AND_DATA_DICTIONARY.md)
3. [Demand intake, scoring, approval gates, CoE governance and RACI](docs/GOVERNANCE_AND_DECISION_RIGHTS.md)
4. [BRD, UAT, security and audit evidence sample](docs/BRD_UAT_SECURITY_PACK.md)
5. [Benefits realization, financial controls and end-of-life lifecycle](docs/BENEFITS_AND_EOF_POLICY.md)
6. [Role/JD traceability, technical competencies and honest scope](docs/JD_TRACEABILITY_AND_LIMITATIONS.md)
7. [Synthetic source data](data/), [Python QA & pipeline report](src/portfolio_quality.py), [automated tests](tests/test_portfolio.py), [sample portfolio board pack](reports/PORTFOLIO_HEALTH_REPORT.md)

## Run the working demonstration
```bash
python "AI Project & Program Management/38_AI Portfolio & Governance PMO (ServiceNow, SPM)/src/portfolio_quality.py"
python -m unittest discover -s "AI Project & Program Management/38_AI Portfolio & Governance PMO (ServiceNow, SPM)/tests" -v
```
The evaluator reads CSVs from the project directory regardless of working directory; it creates/updates `reports/PORTFOLIO_HEALTH_REPORT.md`. It checks current pipeline counts, minimum field completeness, approved funding against cost forecasts, missing approvals and open high-severity RAID. It **does not connect to ServiceNow**.

## Design conventions
- Demand -> screening -> qualification -> prioritisation -> funding/approval -> project/product conversion -> delivery gates -> close -> benefits review -> decommission.
- The **SPM single source of truth** is a proposed *target operating principle*. In this sample, CSV files are the canonical simulated data source.
- Funding and cost are **different records**: budget/allocation approval ≠ forecast, actual or benefit achieved.
- All stage-gate approvals must reference decision-maker, date and evidence.
- Pilot-to-product transitions require ownership, operational support, data/model dependencies, security, UAT and value realisation checkpoints.
- AI oversight includes responsible AI, legal/security/privacy reviews, and accountable product owner sign-off.

## Tech, AI and methodology used
**Used:** Python 3 (csv, pathlib, unittest), synthetic CSV data, deterministic validation and Markdown board report. **Conceptual functional mapping:** ServiceNow SPM Demand, Project, Funding, Cost, Portfolio Management and benefits reporting; RACI, RAID, BRD/UAT, governance forums. **AI:** no LLM called; AI use cases are illustrative portfolio records. **Methods:** enterprise PMO/portfolio governance, stage gates, business case scrutiny, prioritisation scoring, financial governance, product lifecycle, responsible AI controls, continuous data-quality review.

## Illustrative outputs
The sample dataset deliberately includes a missing approval, stale milestone and funding shortfall. These are not errors in a real organisation; they are test cases for raising the governance issues a Portfolio Manager should identify.

## References
- Dubai Holding role description (LinkedIn employer post): https://ae.linkedin.com/jobs/view/ai-portfolio-governance-manager-at-dubai-holding-4472128390
- ServiceNow official project and portfolio funding: https://www.servicenow.com/docs/r/it-business-management/project-management/c_ProjectAndPortfolioFunding.html
- ServiceNow CIS-SPM scope and exam blueprint: https://learning.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0011561

*Independent portfolio demonstration — not affiliated with Dubai Holding or ServiceNow.*
