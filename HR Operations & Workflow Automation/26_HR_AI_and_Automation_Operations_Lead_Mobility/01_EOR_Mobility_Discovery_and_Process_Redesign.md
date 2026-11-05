# 01 — EOR Mobility discovery and process redesign

## Customer scenario
A fictional global Employer of Record supports international team members across 12 jurisdictions. Visa renewal reminders and employee document questions arrive by email, case platform and partner handoffs. HR coordinators repeatedly copy case fields between a CRM/case system, HRIS, mobility vendor and payroll calendar.

**This is a designed scenario, not an actual Remote customer engagement.**

## As-Is: current-state observations to verify with real owners
1. Employee submits mobility request or asks about work authorization.
2. HR coordinator scans free-text email and attaches sensitive documents manually.
3. Mobility team asks for missing information and manually checks policy references.
4. Case status is updated separately in HRIS, case platform and vendor tracker.
5. Escalations go to legal/immigration specialist without standard evidence chain.
6. Payroll start-date changes are sometimes relayed by spreadsheet instead of approved integration.

Potential problems: duplicate work, uncertain permission boundaries, inconsistent updates, delayed renewal reminders, poor employee visibility, overcollection of sensitive documents and unclear decision accountability.

## SIPOC
| Supplier | Input | Process | Output | Customer |
| --- | --- | --- | --- | --- |
| Employee / customer HR | Approved request reason, consent, case reference | Identity/access gate, scope classification | Case ID and acknowledgement | Employee |
| HRIS / case platform | Authorized role, employment status, case metadata | Approved case lookup | Verified minimal metadata | Mobility agent |
| Mobility specialist / counsel | Jurisdiction-specific permitted policy and approvals | Specialist review | Signed status determination | HR Operations |
| Payroll operations | Approved effective date, employee key | Controlled change event | Reconciled pay calendar update | Finance and employee |

## To-Be
Case submitted -> minimal field and access checks -> **maker proposes a route only** -> **checker enforces permissions, evidence, and required review** -> explicit specialist queue OR safe FAQ response -> human decision -> permitted case update -> optional approved payroll notification -> reconciliation and metric event.

**Legal work authorization and visa eligibility are specialist decisions, never automatic LLM decisions.**

## Requirements
- Trace each state transition using a privacy-safe correlation ID and timestamp.
- Customer and employee can understand the case state without visibility into confidential fields.
- Global policy knowledge must carry jurisdiction, source, effective date and owner.
- HRIS, case, document vault and payroll remain systems of record in their own domains.
- No automatic termination, payroll activation or immigration eligibility decision.
- Audit trail records *decision metadata*, not full passport/ID or unredacted documents.

## Discovery interview prompts
Who is the DRI? What is the current case volume and average cycle time? Where is evidence stored? Which jurisdictions require additional authorized specialist review? Which workflow step requires consent? What are actual API throttles and tool permissions? How many exceptions go to counsel? How is payroll notified of a signed decision? What cannot be stored in the analytics warehouse?

## Metrics to baseline, not assume
Median and p95 case cycle time, first-response SLA, case reopen %, missing-document request %, duplicate work %, automation coverage, review transfer success, data/privacy incidents, employee satisfaction and actual avoidable operating cost.
