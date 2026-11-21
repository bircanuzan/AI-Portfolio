# Requirements, Automation Backlog and UAT

## Prioritisation logic
Rate each proposed improvement 1–5 for volume, recurring risk and time-saving potential, and 1–5 for implementation complexity. Use a transparent score such as `(volume + risk + benefit) / effort`. Human review remains required for consequential payments or approvals even when an opportunity scores highly.

| Priority | Problem | Proposed change | Business owner | Acceptance evidence |
|---|---|---|---|---|
| P1 | Duplicate invoice intake | Validate invoice keys, flag duplicates | Operations | No duplicate moves to approval |
| P1 | AR matches require manual cross-check | Rules-based exact matches and exception queue | Finance | Unmatched and partial amounts routed to review |
| P1 | Conflicting customer IDs | Source-of-truth reconciliation checks | Systems Operations | No silent merge or overwritten master record |
| P2 | Late exception detection | Scheduled threshold dashboard and alert | Operations Excellence | Owner notified before SLA deadline |
| P2 | Manual KPI collation | Controlled reporting refresh and audit log | Operations Excellence | Traceable calculation and review sign-off |

## UAT scenarios
| ID | Test input | Expected control / result |
|---|---|---|
| UAT-01 | Matching invoice amount and remittance reference | Straight-through match; full trace |
| UAT-02 | Duplicate invoice number / different amount | Block auto-processing; create duplicate exception |
| UAT-03 | Partial payment | Record partial status, do not mark settled |
| UAT-04 | High-value approval outside limit | Require named authorised human reviewer |
| UAT-05 | Different customer IDs in CRM vs admin | Flag conflict, preserve both original records |
| UAT-06 | Missing invoice / beneficiary reference | No automatic posting; queue for investigation |
| UAT-07 | Service outage / timeout | Retry idempotently and avoid duplicate transaction |
| UAT-08 | Unauthorised role attempts override | Deny change, audit, alert process owner |
| UAT-09 | AI suggests a financial action with weak evidence | Show explanation, restrict to advisory, request human sign-off |
| UAT-10 | Dashboard refresh contains stale source data | Label stale, suppress decision-ready status |

## Release and change governance
- **Definition of ready:** problem statement, baseline, process map, owner, acceptance criteria, privacy/data controls and risk score.
- **Definition of done:** UAT pass, rollback route, release approval, updated SOP, assigned owner/backup, monitoring alert and evidence archive.
- **Pilot:** 2-week controlled scope; compare case mix and volumes; record time per case, exception count, rework and manual overrides.
- **Handover:** process owner receives change log, SOP and training notes; post-implementation review reports accepted/rejected hypotheses.

This is a demonstration design, not a claim that these integrations are live.
