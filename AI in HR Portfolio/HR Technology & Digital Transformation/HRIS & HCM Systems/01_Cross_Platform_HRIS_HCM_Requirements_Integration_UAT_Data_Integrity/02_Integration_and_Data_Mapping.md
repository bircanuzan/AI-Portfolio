# HRIS/HCM integration mapping and reconciliation

## Proposed source-to-target interface
| Legacy HRMS field | Canonical HCM field | Type | Rule | Control owner |
|---|---|---|---|---|
| EMP_ID | employee_id | text | Unique within employing entity; preserve immutable key | HR Data Steward |
| ENTITY_CODE | legal_entity | code | Reference-approved employing entity | HR Operations |
| START_DT | effective_start | ISO date | Required, parseable and auditable | HR Operations |
| LINE_MGR | manager_employee_id | text | Manager must exist in active master or approved exception | HR Data Steward |
| PAY_APPROVED | pay_change_approved | boolean | Explicit HR/Finance authorisation | Payroll/Finance |
| STATUS | employment_status | enum | Valid state with dated history | HR Operations |
| GRADE | grade_code | code | Approved grade catalogue and effective date | Rewards |
| RECORD_UPDATED | source_updated_at | timestamp | Version reconciliation and change audit | IT/HRIS |

## Common cross-platform issues
- **Oracle Fusion Cloud HCM:** conceptual mapping to person, assignment, legislative context and effective dates; must validate actual data model in licensed configuration.
- **Workday:** conceptual worker/event changes and security domain alignment; actual integration schemas vary.
- **SAP SuccessFactors Employee Central:** conceptual effective-dated employee and employment events; validate entity and picklist mapping.
- **Downstream:** payroll handoff, time & attendance, reporting, identity/access provisioning, benefits, LMS.

## Interface design and control checkpoints
1. Source extract captured with version and cutoff timestamp.
2. Validate schema, referential integrity and entity mapping.
3. Stage and compare total rows, unique keys, active/exited counts and key control totals.
4. Reject duplicate keys, malformed dates, unsupported states and unapproved pay events.
5. Route exceptions to named human owners with severity and evidence.
6. Apply approved transformations; sign off HR/Payroll controls before release.
7. Only then allow approved vendor/IT-controlled interface to execute; monitor, log and reconcile responses.

Use a correlation key `entity + employee_id + effective_start + event_version` to prevent duplicate retry effects. Do not expose identity documents, bank numbers, personal medical details or confidential employee dossiers in analytics or source control.

## Excel reconciliation spec
Use **Power Query** data-type enforcement and anti-joins to find missing keys; Excel structured tables and pivot summaries to compare legal entity counts. Sample formulas:
- `=COUNTIFS([EmployeeID],[@EmployeeID],[LegalEntity],[@LegalEntity])` to flag master duplicates (table context must be adjusted).
- `=IF([@Approved]="Y","READY","REVIEW")` as an *input validation flag*, never a bank-payment instruction.

**Completion gate:** signed field mapping, zero unresolved critical record errors, HR/Payroll acceptance, vendor validation of schema and controlled cutover approval.