# Organisation Design, Reward & Governance | Workforce Cost and Control Demonstrator

**Portfolio project — illustrative prototype using entirely synthetic employee data.** This is not a claim of an engagement with Dubai Holding or any other client.

A reproducible HR analytics and controls project aligned with workforce planning, manpower cost governance, reward benchmarking, monthly HRIS/payroll/Finance reconciliation, short-term incentive review, delegated authority, and Human Capital audit readiness.

## Business scenario
A fictional holding-company Human Capital function needs an evidence-based view of approved workforce budgets, salary and allowance costs, market-positioning outliers, monthly variances, and incentive approvals. Mismatches across HRIS, payroll and Finance must be identified **before** review or payment.

## Components
- `data/synthetic_workforce.csv` — 9 entirely fictional employees, department, employee category, job grade, pay components, budgets, market midpoint, incentive fields and maker/checker identities.
- `workforce_reward_controls.py` — Python standard-library script that performs reconciliation, analytical review and data-quality/approval checks.
- `docs/controls_and_audit_protocol.md` — suggested controls, cross-functional responsibilities, segregation of duties and evidence standards.

## Checks
| Code | Check |
|---|---|
| DATA-01 | Missing or duplicate employee identifiers |
| DATA-02 | Non-active employee requiring separate settlement review |
| RECON-01 | HRIS base pay compared with payroll base pay |
| RECON-02 | Payroll base + allowances compared with Finance booked total |
| COST-01 | Monthly payroll cash elements compared with approved budget |
| REWARD-01 | Salary compa-ratio against a **synthetic** market reference band |
| STI-01 | Arithmetic validation of an **illustrative** annual incentive |
| DOA-01 / DOA-02 | Incentive approved status and designated approver |
| SOD-01 | Separation of preparer and approver |

## Run the demonstrator
```bash
python3 workforce_reward_controls.py
```
Uses only Python's standard library and writes:
- `outputs/department_workforce_costs.csv` — department/category counts and monthly/annualized cost variance summaries.
- `outputs/control_exceptions.csv` — employee-level exceptions and review reasons.

The sample is deliberately seeded with discrepancies. Reviewers should resolve exceptions, correct source records, and obtain authorized approvals; the script never changes pay or initiates payments.

## Management decision use
**Human Capital:** see headcount/cost by department and employee category, review market salary positioning and review incentive approval status.

**Finance:** identify budget variances and differences against Finance records and document root-cause actions.

**Group Services / Payroll:** reconcile employee records, review incentive arithmetic and enforce maker-checker approvals before any pay-cycle handoff.

**Audit:** retain source versions, approval evidence, exceptions, owners, materiality and remediation closure records.

## Limitations and evidence integrity
- All records, salaries, rates, names and approvals are fabricated; no confidential information is used.
- Thresholds and incentive mechanics are illustrative assumptions, not an employer's policy.
- Annualized cost is simply monthly synthetic cash pay multiplied by 12; it is not a workforce forecast.
- **No** UAE statutory payroll, WPS, settlements, pensions, gratuity, labour law or tax rules are calculated. Those require current jurisdiction-specific policy review and authorised specialists.
- This demonstrates a method and technical capabilities, not historical hands-on production processing.

**Author:** Bircan Uzan | HumanEvoX Consultancy | [AI & HR Portfolio](https://github.com/bircanuzan/AI-in-HR-Portfolio)
