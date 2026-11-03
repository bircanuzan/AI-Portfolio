# HRMS ownership: lifecycle architecture & implementation design

## 1. Scope / architecture
```text
Recruitment / ATS -> approved offer -> employee master in HRMS
   -> joiner checks -> onboarding tasks -> access provisioning
   -> employee changes (role, pay, manager, entity, benefits)
   -> monthly payroll cut-off -> dual HR/Finance approval -> bank/WPS process IF applicable
   -> performance/learning/employee service -> offboarding/EOS specialist review
   -> controlled retention, reporting and deletion per policy
                               |
                         Power BI semantic model
                    (approved, minimised, reconciled data)
```
**System of record:** nominated HRMS for employee master, effective dates and approved job/pay changes. Payroll processor remains accounting/payments authority. No fictional vendor integration is claimed.

## 2. Data ownership matrix
| Data element | Accountable owner | Control | Key failure |
|---|---|---|---|
| Employee ID / legal entity / status | HR Operations | Unique ID, documented effective dates | Duplicate or wrong-entity payroll |
| Contract, grade, basic pay & allowances | HR + authorised compensation reviewer | Maker-checker and versioned change request | Unapproved salary change |
| Bank payment details | HR/Payroll with employee-verification procedure | Masked access, independent verification | Fraud / misdirected pay |
| Time and attendance / unpaid absence | Line manager + HR | Signed cut-off, reconciliation | Under/overpayment |
| Payroll input and output | Payroll/Finance | Four-eyes signoff and batch reconciliation | Duplicate/late transfer |
| EOS inputs | HR/Payroll + legal specialist | Service-date and scheme applicability verification | Inaccurate entitlement |
| BI access and transformations | IT/BI + HR data owner | Access logs, certified dataset, refresh controls | Unauthorised disclosure |
| Service desk and employee requests | HR Shared Services | SLA ownership, role-based routing | Unresolved cases |

## 3. Mandatory change-event payload
`employee_id, legal_entity, event_type, effective_date, previous_value, new_value, supporting_reference, requestor, approver, approved_at, source_system, correlation_id`.

No bulk updates without a preview, sample validation, reversible plan and controlled approval. Keep direct identifiers out of analytics where aggregated values suffice.

## 4. HRMS product owner backlog
P0: employee master duplicates, employee status, finance signoff, payroll cut-off, bank verification, EOS handoff.  
P1: HR service request tracking, onboarding and offboarding automation, integration monitoring, data reconciliation.  
P2: predictive insight, employee self-service knowledge, skills analytics—only after data and consent/access bases are resolved.

**Deliverables:** AS-IS process inventory, target process maps, BRD/user stories, integration field mapping, RACI, data dictionary, access matrix, UAT pack, support/runbook, BI refresh ownership.

## 5. Example user stories
- As Payroll Approver, I can see every variance above AED 0.01 and its approval evidence before releasing a batch.
- As HR Operations Lead, I can trace who changed a pay field, why, and when it became effective.
- As HR Analyst, I can report employee-service SLA by entity without exposing bank details.
- As an employee, I can submit an HR inquiry and view status without seeing another employee's information.

**Acceptance gate:** signed field mapping, reconciled sample of all critical fields, no critical UAT defects, dual HR/Finance approvals and legal applicability sign-off.