# HRMS operating model & controls

**Case:** fictional UAE financial-services HR Operations team, six synthetic employees in the demonstrator; enterprise deployment design is conceptual.

## Current-state pain points
Multiple spreadsheets and HRMS exports, unclear record ownership, manual payroll reconciliation, inconsistent employee self-service, delayed EOS reviews and no single management view of HR service performance.

## Future-state workflow
1. **HRMS authoritative source:** HR Operations validates identifiers, employment status, dates, bank master data and compensation change approvals; restrict access by role.
2. **Pre-payroll interface:** scheduled export with row counts, schema/data checks, version and source timestamp; validate against HR approvals.
3. **Exception queue:** deterministic rules flag duplicate IDs, missing account references, unapproved disbursements, variance or EOS-review status. Never execute payments automatically.
4. **Human reconciliation:** HR payroll lead examines exceptions; Finance authorises approved payout control totals, with independent review.
5. **EOS governance:** trigger upon confirmed exit; route entitlements to qualified HR/legal/payroll specialist against current law and company policy; retain dated sign-offs.
6. **Management dashboard:** refresh reconciled aggregated views, SLA, data completeness and exception ageing. Restrict individual payroll details.
7. **Employee portal:** policy Q&A, requests and case status; escalate sensitive pay, grievance or legal matters to people.

## RACI (illustrative)
| Control | HR Operations | Payroll specialist | Finance controller | IT/HRIS | Legal |
| --- | --- | --- | --- | --- | --- |
| Employee master completeness | A/R | C | I | C | I |
| HRMS change logging and access | A | C | I | R | C |
| Pre-payroll reconciliation | C | R | A | C | I |
| UAE EOS interpretation | C | R | C | I | A |
| Release authorisation | I | R | A | I | I |
| Dashboard data access | A | C | C | R | I |

## Control evidence register
| Control ID | Risk | Rule / evidence | Owner | Escalation |
| --- | --- | --- | --- | --- |
| C01 | Duplicate pay instruction | Unique employee key + batch ID, reject duplicate, exception log | HRMS analyst | Payroll lead |
| C02 | Misrouted payment | Missing bank reference blocks batch; verification audit | Payroll | Finance |
| C03 | Unapproved pay | Approved amount must reconcile with proposed | Payroll | Finance |
| C04 | Unauthorised release | Approval status must be 'approved' | Finance | Controller |
| C05 | Incorrect EOS settlement | Exit requires specialist-reviewed EOS case | HR / Legal | Qualified reviewer |
| C06 | Personal data exposure | Least privilege, encryption, retention and logs | IT/security | DPO / HR |

## Automation boundaries
**Automate:** intake validation, task assignment, SLA reminders, aggregate KPI refresh, rules-based duplicate/approval checks.

**Human only:** salary approval, settlement calculation, statutory interpretation, sensitive employee decisions, final payroll release.

**AI-assisted but review required:** policy lookup, HR FAQ drafting, summarising anonymised employee service trends. No autonomous employment or payment decisions.

## Data quality and controls
Minimum data dictionary: Employee_ID, Employment_Status, Effective_Date, Salary_Approved, Payroll_Proposed, Bank_Reference, Approval_State, EOS_Case_State, Updated_By, Updated_At. Use hashed pseudonymous keys in analytical models; log changes; restrict raw payroll data.

**Not legal advice:** WPS / UAE labour law and EOS rules must be independently checked against official up-to-date sources and the employing entity's correct legal regime by accountable specialists.