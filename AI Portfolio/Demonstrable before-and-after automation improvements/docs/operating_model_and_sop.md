# Operating Model, Process Register and SOP

## 1. Control principles
1. All processes have a named **owner**, **backup**, systems of record and review date.
2. Every automated recommendation or financial movement has a defined review boundary.
3. Approved configuration changes are recorded, tested in UAT, authorised by a business owner and documented before go-live.
4. Operational exceptions are surfaced promptly; no silent overwrite of conflicting source data.

## 2. Process register
See `data/synthetic_before_after.csv` for process-step owner, backup, system of record, volumes, exception rates and human review triggers. **The register is fictional.**

| Business object | Proposed system of record | Control |
|---|---|---|
| Receivables and settlements | AR ledger | Finance signs off on non-exact matches |
| Customer identity | Customer master / CRM | Duplicate or conflicting identities quarantined |
| Workflow status | Admin platform | Audit-trail entry for state changes |
| Approval status | Approval register | Segregation of duties; four-eyes control where required |
| Incidents | Incident log | Root-cause tracking and owner assignment |

## 3. Example SOP: unmatched receivable
1. Extract recorded invoice ID, payer ID, due amount and remittance reference.
2. Normalise non-sensitive identifiers for comparison; do not change source ledger values.
3. Match exact references and amount under an approved tolerance configuration.
4. If unmatched, duplicate, disputed or outside tolerance: create exception record; do not approve settlement.
5. Assign Finance Operations as first responder and Finance Controller as review/backup.
6. Record evidence, timestamp, proposed action, decision, escalation and resolution category.
7. Reconcile status back to the AR ledger after authorised human approval.
8. Review weekly exception trends and quarterly SOP effectiveness.

## 4. Root-cause review and automation decision
Capture event → reproduce failure → confirm root cause → classify people/process/system/data → rank volume × severity × fix effort → specify requirements → UAT → controlled release → 2-week pilot → measure against stable baseline.

## 5. Monitoring
Monitor median processing time, workload, exception frequency, first-pass match rate, stale records, error reversals, manual overrides, SLA breaches, and evidence completeness. Use a single-owner, timestamped scorecard with weekly operating review.

## 6. Governance and consent
Do not place real customer, employee, banking or account data into public GitHub. This example uses synthetic data only.
