# 06 — AI adoption KPIs, benefits realisation and steering report

**Purpose:** distinguish rollout activity from actual employee adoption and verified business results. All sample figures are synthetic.

## KPI dictionary
| Metric | Calculation | Minimum data source | Caveat |
|---|---|---|---|
| Eligible activation rate | Unique approved users who performed >=1 permitted workflow / eligible users | SSO + workflow telemetry | Do not count test/unauthorised use |
| Weekly sustained use | Users with >=1 qualifying workflow this week / active eligible cohort | Permission/usage logs | Exclude passive logins |
| Scenario completion rate | Successfully completed, reviewed workflows / attempted workflows | Work logs + reviewer QA | Define a consistent work unit |
| Answer quality pass rate | Human-validated correct outputs / sampled outputs | Blind review rubric | Stratify by use case / language |
| Escalation rate | Escalated cases / completed workflows | Helpdesk / incident log | Higher rate can signal *better* reporting |
| Time impact | Baseline median minutes minus validated post-pilot median | Matched workflow time study | Cannot imply saved salary or headcount |
| Confidence / usefulness | Role-specific pulse survey result | Anonymous survey | Sampling bias, avoid forced response |

## Illustrative dashboard data
See [data/synthetic_adoption_metrics.csv](data/synthetic_adoption_metrics.csv). Fictional weeks, targets and values only; not Zayed University statistics.

Example week 4, policy assistant:
- Eligible users: 100
- Activated users: 38 -> activation = 38%
- Completed workflows: 140
- Human-reviewed samples: 30, of which 25 correct -> sampled quality = 83.3%
- Escalations: 12 -> escalation rate = 8.6%

The sample size is too small to declare the assistant safe, fair or cost-saving. A scale decision additionally requires approvals and regression tests.

## Benefits management
1. Agree baseline process and per-task definition before pilot.
2. Separate **time avoided** from **productive capacity released**.
3. Require quality/control compliance; no value claimed for unsafe outputs.
4. Confirm benefits with finance and business owner, including incremental costs and support effort.
5. Report confidence intervals or uncertainty; never turn an assumed time saving into reported cash savings.

## Example executive steering report (fictional)
**RAG:** Amber — staff policy pilot operating in controlled evaluation, while expanded rollout remains unapproved.

- **Progress:** charter agreed and two pilot work packages documented (hypothetical).
- **Adoption:** 38/100 approved staff activated in sample week 4 (synthetic).
- **Quality:** 25/30 human-reviewed responses correct; increase test coverage required.
- **Risk:** incorrect policy answer scenario requires retrieval freshness control.
- **Decision sought:** authorise extra evaluation and keep broader deployment on hold.

### Suggested steering questions
Are we solving the right user problem? Are outputs reliable? Is the data handled safely? Is a human still accountable? Do the benefits outweigh licensing, support and control cost?

**No live KPI telemetry or realised results are claimed.**
