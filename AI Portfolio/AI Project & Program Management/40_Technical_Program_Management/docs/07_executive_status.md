# 07 — Executive Status Report

**Illustrative reporting date: 29 October 2026**. All figures and clients below are fictional; see the reproducible CSV and Python calculations.

| Client | RAG | Material issue | Required action |
| --- | --- | --- | --- |
| Atlas Bank | **Amber** | Mapping acceptance planned for 23 October is unsigned | Client Product Owner to sign by 30 October or approve new sequence |
| Beacon FinTech | **Red** | Duplicate webhook events are a P1 blocker; 28 October sandbox acceptance missed | Engineering fix, replay test evidence, client technical signoff |

## Illustrative program performance
- 13 tracked milestones, 6 completed, of which 4 on time (**66.7%**).
- 2 incomplete milestones past the planned dates (Atlas A04 and Beacon B04).
- 1 open P1 issue (Beacon I01).
- 1 blocked feature request (Beacon BE-F01).
- 24 hours of illustrative weekly staffing shortage (Atlas PM 4, Atlas Engineering 8, Beacon QA 12).
- Neither client passes its launch gates today.

## Management decisions
1. Atlas Product Owner confirms mapping acceptance or invokes controlled re-baselining.
2. Beacon Engineering lead demonstrates replay/idempotency repair to client technical owner.
3. Program sponsor agrees a capacity or sequencing resolution before committing dates.

## RAG policy
**Red:** any open P1 issue or two or more late, open milestones per client.  
**Amber:** at least one overdue open milestone, high-priority open risk or capacity gap, absent Red.  
**Green:** no identified Red/Amber signals; does **not** itself mean approved for production.

This scoring policy is designed for this example only and is not a Sardine standard.

Generate the report from `python3 src/project_health.py --as-of 2026-10-29`.
