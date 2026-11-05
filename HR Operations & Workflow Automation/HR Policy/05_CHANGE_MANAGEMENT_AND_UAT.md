# 05 | Change Management, HR Briefings, HRIS and Payroll UAT

## Change design
**Population:** synthetic Aurora Aviation Group; six illustrative markets, mixed flight/ground/corporate functions. **Change:** new approved global policy core plus country-controlled contract and handbook addenda. **Launch principle:** no market go-live without local counsel's evidenced approval and applicable employee representation/consultation steps.

### Impact assessment
| Audience | Change impact | Sponsor / enablement |
|---|---|---|
| Country HRBPs and ER | Determine applicable version, handle requests, grievances and exceptions | Country HR lead; scenario-based workshops |
| Managers and operations | Consistent eligibility decisions; rostering/fatigue/safety checks | Ops leadership; manager decision trees |
| Employees | Clear rights, where to seek support and what changed | Country comms; accessible translations and FAQs |
| Payroll and Reward | Variations in hours, allowances, leave and adjustments | Payroll lead; country parallel testing |
| HRIS and IT | Effective-dated policies, role-based access, request workflow | HRIS lead; UAT and rollback |
| Legal and Data Privacy | Local-law interpretation, consultations, retention and privacy | Country counsel; documented sign-off |
| Leadership / Finance | Exception risk, implementation budget and measured outcomes | CHRO sponsor; monthly scorecard |

### Rollout sequence (illustrative, not executed)
1. Inventory all active versions and contracts, map countries/entities and document owners.
2. Obtain counsel-validated country requirements and any employee-consultation evidence.
3. Finalize redlines, contract links, translations and financial/safety impact.
4. Complete approval gates, HRIS/payroll configuration and parallel UAT.
5. Run controlled pilot **only in fully approved jurisdictions**, with support desk and escalation channels.
6. Publish with version/effective-date locks; archive retired templates; record employee notifications.
7. Review at 2, 6 and 12 weeks, including worker feedback and exceptions.
8. Escalate defects and roll back per counsel-authorized plan; never roll back mandatory entitlements.

### UAT script library
| Test ID | Scenario | Expected result | Gate owner |
|---|---|---|---|
| UAT-01 | Employee in market A requests policy | Only country-eligible effective version displayed | HRIS + Country HR |
| UAT-02 | Unapproved market policy selected | Block publication/use | HR Policy |
| UAT-03 | Future-dated policy before effective date | Existing approved policy remains active | HRIS |
| UAT-04 | Change from one legal entity to another | Correct country/entity terms, manual review triggered | HRIS + Legal |
| UAT-05 | Contract clause revised | Approved template version and redline traceable | Legal |
| UAT-06 | Change affects working hours | Payroll and rostering rules independently validated | Payroll + Operations |
| UAT-07 | Manager lacks delegation | Decision blocked and rerouted | HRBP / Governance |
| UAT-08 | Employee notification failed | Launch dashboard flags unnotified records | HR Operations |
| UAT-09 | Exception attempts to waive statutory rights | Escalation; no automated override | Legal |
| UAT-10 | Language variant or translation expired | Prevent release pending approved translation | HR Policy |
| UAT-11 | Duplicate employee request | No duplicate payroll/workflow action | HRIS |
| UAT-12 | Automated AI draft proposed as final advice | Human/legal review gate blocks publication | Legal / Privacy |

**Evidence per UAT:** test data ID (synthetic), expected/actual, result, defect severity, retest date, approver, release ticket. A proposed test case is not equivalent to a passed UAT.

### HR briefing agenda (45 minutes)
5m: Why the policy is changing and what's not changing.  
10m: Local legal rights and employee category scope (counsel-presented).  
10m: Decision workflow and escalation/appeals.  
10m: HRIS demonstration, payroll impact and document control.  
5m: Difficult scenarios, ethics and privacy.  
5m: Knowledge check and support contacts.

### Communications controls
- Segment by employing entity, location, role and language.
- Send concise employee summary, approved full policy, effective date, change comparison, FAQ, contact and appeal details.
- Accessibility and translation are reviewed locally; don't assume acknowledgment equals legal consent.
- Track manager briefing attendance, read receipt where appropriate, and direct employee feedback channels.

### Risk register
| Risk | Early signal | Mitigation | Owner |
|---|---|---|---|
| Statutory conflict | Counsel finds unresolved entitlement | STOP release, amend country addendum | Legal |
| Payroll under/overpayment | Reconciliation defects | Parallel run; targeted corrections | Payroll |
| Wrong policy served | Country/entity mapping errors | Access rules and effective-date UAT | HRIS |
| Manager inconsistency | Appeal/exception spikes | Decision tree, coaching and audit | HRBP |
| Employee distrust | Negative pulse, low clarity | Transparent redlines, dialogue | HR Comms |
| AI hallucination | Uncited provision in draft | Source validation and human review | HR Policy |
