# UAT, Cutover, Hypercare and AI Governance Plan
**Status:** Design-only independent case. No executed Oracle tenant testing, AI service deployment or measured real-user outcomes claimed.

## UAT scenario register (examples)
| Test ID | Scenario | Expected result | Priority | Test evidence |
|---|---|---|---|---|
| UAT-01 | Create employee with all mandatory Core HR fields | Valid record; correct legal employer, org, job and effective date | P1 | Field validation, transaction and audit IDs |
| UAT-02 | Attempt duplicate national/employee identifier | Block or send to managed data-quality exception | P1 | Duplicate validation log |
| UAT-03 | Manager requests employee data change | Correct route and approval; no bypass for own request | P1 | Workflow and approved RACI evidence |
| UAT-04 | Unauthorized user attempts compensation data access | Denied; security event captured | P1 | Role/access test and audit evidence |
| UAT-05 | Approved employee change feeds payroll/Finance | Correct effective-dated fields and reconciliation totals | P1 | Source/extract/consumer reconciliation |
| UAT-06 | Invalid outbound interface record | Quarantined, flagged, retried safely after correction | P2 | Error queue, alert and reconciliation |
| UAT-07 | OTBI workforce count vs governed HR data extract | >=99.5% reconciliation; mismatch documented and resolved | P1 | Signed source-to-report check |
| UAT-08 | Analytics Publisher month-end report | Approved schema, distribution, access and timestamp | P2 | Scheduled distribution acceptance |
| UAT-09 | HR letter request via workflow | Valid case, human approval, audit history and SLA timer | P2 | Case workflow and history |
| UAT-10 | OCR document confidence below threshold | Human queue; no auto-change to employee record | P1 | Model confidence and case state |
| UAT-11 | AI assistant asked for sensitive/unauthorized data | Refusal / handoff, no PII disclosure, event logged | P1 | Red-team test cases and trace |
| UAT-12 | Rehearsed release rollback | Restored stable state with no lost approved transaction | P1 | Runbook and signed rehearsal |

**Exit criteria:** 100% critical paths passed; >=98% overall eligible tests passed; zero unresolved P1/P2; all data and access issues signed off; HR, IT, Payroll and InfoSec approvals captured where relevant.

## 30-day hypercare operating model
- **Days 0–7:** Daily HR/IT/vendor triage, incident bridge contact list, reconciliation checks after major HR transactions, release rollback watch.
- **Days 8–14:** Incident trend and root-cause review, SOP/FAQ amendments, adoption analysis by employee segment, queue and SLA review.
- **Days 15–30:** Optimise knowledge and approvals, retest regressions, complete BAU ownership, confirm KPI baseline quality with Finance and HR sponsors.
- **Exit:** No critical systemic defect, documented ownership, support knowledge transferred, exception queues aging within agreed limits and service metrics signed.

## Access and data controls
- Least-privilege, role-to-person matrix and segregation-of-duties policy.
- Joiner/mover/leaver identity review; high-risk role recertification quarterly.
- Effective-dated person and employment record validation with master-data ownership.
- Data contracts for Oracle extracts/REST integrations; retry, idempotency and error quarantine patterns evaluated by technical specialists.
- Immutable change history, restricted audit retention and approved privacy/compliance treatment.

## AI / OCR / chatbot safety and evaluation
1. **Use case intake:** Assess employee impact, data protection, regulatory scope, explainability needs and whether simpler rules can solve it.
2. **OCR pilot:** Predefined field-level ground truth; aim >=97% extraction accuracy on approved test corpus; flag low confidence and inconsistent identity fields for human review.
3. **HR FAQ retrieval assistant:** Restrict to approved/current policy sources; require policy citation and effective date; evaluate >=90% supported accuracy on an agreed test set; test abstention and stale-policy behavior separately.
4. **HR case classification:** Test macro-F1, incorrect routing and privacy leakage before use; never let the model approve payroll, entitlement or disciplinary outcomes.
5. **Human escalation:** 100% low-confidence/sensitive items handled by authorised HR agent; capture override reason and SLA impact.
6. **Controls:** Prompt-injection and access tests, restricted PII, vendor data agreements, event trace and documented incident shutoff.
7. **Monitoring:** Weekly error and override checks; monthly drift review; quarterly security and policy refresh.

## Benefits assurance checklist
- Confirm actual baseline volumes and timings with representative logs.
- Compare like-for-like cases before and after pilot, excluding scope changes.
- Calculate handling-time savings and reallocatable capacity, not presumed headcount reduction.
- Finance certifies any actual spend avoidance/cash value; otherwise report gross capacity value only.
- Avoid double-counting OCR, chatbot and workflow time saved on the same case.

**Financial scenario:** 480 monthly cases; 25-to-12-minute reduction; 104h/month; 1,248h/year; AED120/h; AED149,760 gross annual capacity value; AED89,000 first-year costs; AED60,760 hypothetical net value; 68.3% hypothetical ROI. None are claimed as actual.
