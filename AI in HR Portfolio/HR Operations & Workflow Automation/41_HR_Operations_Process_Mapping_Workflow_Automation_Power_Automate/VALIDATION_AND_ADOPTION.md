# Validation, value measurement and adoption

## Acceptance scenarios — planned, not executed
All tests below have status **Not run — live Power Automate environment required**. Expected results are acceptance criteria, not reported outcomes.

| Scenario | Expected behaviour |
|---|---|
| Complete standard request; approval granted | One record and approval; status becomes Ready for preparation |
| Approval rejected | Rejection recorded; employee informed; no preparation task |
| Required detail missing | Clarification requested; no approval sent |
| Unknown or unavailable approver | Exception assigned to HR owner; no requester-chosen substitute |
| Duplicate intake event | One request and one active approval |
| Approval times out | Exception surfaced; no automatic approval |
| Outlook or SharePoint action fails | Failure visible; owner alerted; no false completion |
| Scheduled reminder runs twice | No duplicate approval; reminder frequency controlled |
| HR tries to close before approval | Closure blocked or flagged for correction |
| Approved letter checked and delivered | Completion timestamp and evidence recorded once |
| Unauthorised user tries to read request | Actual access blocked, including direct item access |
| Flow owner unavailable | Backup owner can inspect and recover a failed run |

Test the flow checker findings, manually trigger representative submissions and inspect each action's inputs and outputs in run history. Retest affected scenarios after changes. A successful technical run does not by itself prove that approval policy or access controls are correct.

## Monitoring and measures

| Measure | Definition | Intended source |
|---|---|---|
| End-to-end turnaround | Completed timestamp minus received timestamp; report median and p90 | Request register |
| Approval waiting time | Decision timestamp minus approval-created timestamp | Approval record |
| HR handling time | Active staff minutes per request, excluding waiting | Timed observations |
| Exception rate | Requests entering Exception / requests received in cohort | Status history |
| On-time completion | Requests delivered by due date / requests due in period | Register and business calendar |
| Flow failure rate | Failed runs / total runs for the same flow and period | Power Automate run history |
| Adoption | Eligible requests through the new route / all eligible requests | Register plus legacy intake log |

The flow owner checks failures daily in the pilot. HR reviews backlog and overdue cases weekly. Separate technical failures from approval rejection and employee-request cancellation.

## Illustrative capacity model
**Assumptions only:** 100 requests/month; current active HR effort 15 minutes/request; future effort 7 minutes/request. The future estimate retains manual verification, preparation and delivery.

- Baseline: 100 × 15 / 60 = **25 hours/month**.
- Proposed: 100 × 7 / 60 = **11.7 hours/month**.
- Gross capacity released: 100 × (15 − 7) / 60 = **13.3 hours/month**, or **53.3%** of active handling effort.
- If support and monitoring take 2 hours/month, net recurring capacity released would be **11.3 hours/month** before initial setup and training.

These are hypothetical capacity estimates, not payroll cost savings, measured results or an end-to-end turnaround reduction. With a 20-hour illustrative setup/training effort, simple capacity payback would be approximately 1.8 months at the stated volume and net benefit. No licence or cash ROI claim is made.

## Practical adoption plan
**Week 1:** HR validates the map, service scope, approver ownership and baseline observation approach. Check tenant prerequisites.

**Week 2:** configure in a test environment with fictional data; review Copilot suggestions where available; execute acceptance scenarios and collect evidence.

**Week 3:** after HR sign-off, pilot with a small consenting business team. Give employees a short submission guide and HR a status/exception walkthrough. Keep a documented manual fallback.

**Week 4:** review handling effort, failures, overdue work and feedback against the baseline. Fix recurring problems before expanding.

Pilot exit requires all critical scenarios passed, access verified, backup ownership demonstrated and HR process-owner approval. If failures risk lost requests or incorrect release, pause new automated intake, reconcile the register and use the agreed manual route.

## Evidence status at publication
Documentation and illustrative arithmetic have been reviewed. No tenant was configured, no live UAT was run, and no employee data was used. The next evidence milestone is a tenant-built flow with sanitised run history and actual pilot observations.


© 2026 Bircan Uzan — All Rights Reserved.
