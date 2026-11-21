# Demonstrable before-and-after automation improvements

## Operations automation & KPI measurement case study

**Purpose:** Show how to assess a manual process, establish accountable owners, prioritise changes, validate releases, and compare baseline vs pilot results. The case is aligned to operations-excellence responsibilities in finance-adjacent environments, including receivables matching, approval routing, data consistency, exception management, dashboards, and human oversight.

> **EVIDENCE NOTICE:** All rows, process timings, exception rates and currency values in this repository are **synthetic illustrative data**, not actual performance results at Stake, TASC, HSBC, HumanEvoX, or any client. This is a working *demonstrator*, not evidence of delivered production ROI. Real customer data and outcomes require an approved baseline, instrumentation and stakeholder validation. Source career experience is described separately in the CV.

## Scenario
A multi-system operations team handles invoice intake, accounts receivable matching, payment approvals, CRM/admin synchronisation, incident investigation, and weekly reporting. Fragmented ownership and manual review increase cycle time and exceptions. We design an operations-owned process register, testable low-code change backlog, and exception-based human controls.

### Sample model results (synthetic monthly scenario)
| KPI | Baseline | Pilot | Change |
|---|---:|---:|---:|
| Processing effort | 167.2 staff-hours | 64.2 staff-hours | 61.6% lower |
| Expected exception events | 72.1 | 27.0 | 62.6% lower |
| Illustrative gross time capacity | — | 103.0 h/month freed | Before implementation, validation, and support costs |
| Gross equivalent at hypothetical USD 35/hour | — | USD 3605 / month | **Not** a realised saving or profit forecast |

*Important: Exceptions are modelled as events and are not automatically prevented payments. This example estimates potential process effort change; real adoption and compliance results must be validated.*

## Process and controls
- Register every core process with **primary owner, backup, system of record**, control boundaries and review cadence.
- Rank opportunities by **monthly volume, operational risk, repeatability, and estimated implementation effort**. Do not automate high-risk decisions without review.
- Write requirements and acceptance criteria, run UAT on standard, edge and adverse cases, and record sign-off by the process owner.
- Keep payment approval, disputed settlements, unusual values and data-conflict resolution under **human review**.
- Define **one source of truth** by entity: finance in AR ledger, identity in customer master, operational status in admin platform.
- Measure before/after with matched volumes, stable definitions, data quality checks and an agreed observation period.

## Files
- [Synthetic baseline and pilot data](data/synthetic_before_after.csv)
- [Operating model and SOP](docs/operating_model_and_sop.md)
- [Automation backlog and UAT scenarios](docs/requirements_uat_and_change.md)
- [Evidence collection template](docs/real_world_evidence_template.md)
- [Reproducible KPI calculator](analysis/calculate_kpis.py) (Python standard library only)

## How to reproduce
```bash
python analysis/calculate_kpis.py data/synthetic_before_after.csv
```

## Responsible portfolio use
This public case study demonstrates **method, analytical reasoning, operating controls, test design and measurement**. It is not a claim that every proposed automation has been deployed or that the scenario numbers are verified client outcomes. For actual employment examples, reference documented operating-process improvements and scale, and supply baseline-to-pilot metrics only when supported by process logs, timesheets and sign-off.
