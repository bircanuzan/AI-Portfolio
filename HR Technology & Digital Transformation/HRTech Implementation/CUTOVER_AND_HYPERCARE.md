# Cutover, rollback, support and hypercare

## Go/no-go review
- Scope delivered with traceable signoff and approved change list
- Staff role access validated (least privilege)
- Case history transfer reconciled or explicitly not migrated
- Privacy and accessibility critical findings closed
- Service owners accept case-routing and escalation processes
- Support channels, ownership, vendor response and incident SLA agreed
- Recovery point and rollback time rehearsed with evidence

## Cutover runbook (proposed)
T-7 days: freeze policy catalogue, notify user cohorts and confirm owners.
T-3 days: backup nonproduction templates and obtain configuration checksum.
T-1 day: business owner checks; no pending critical UAT defects.
T0: IT deploys approved configuration, tests login and sample synthetic cases, records release ID.
T+1 day: HR verifies service routing, restricted-note visibility, confirmation messages and support.
T+7 days: service owner reviews incidents, workarounds, employee feedback and rollback decisions.

## Rollback triggers
Unauthorised access, privacy leakage, lost/duplicated cases, failed identity controls, unresolved high-severity defect or critical service disruption. Decision owner = named IT Incident Commander plus HR Product Owner.

## Hypercare metrics
Queue age, unassigned cases, SLA breaches, support tickets by category, first-contact resolution, login failures and failed permission checks. Publish only verified operational measures and protect employee confidentiality.

## 30-day handover
Runbook, knowledge articles, named owners, vendor support terms, change/release calendar, access review cadence, outstanding defects and post-implementation evaluation.

This is **documentation of an intended delivery approach**, not a claimed cutover or live deployment.
