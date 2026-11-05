# 02 | Employee Exit and September Payroll — original benchmark work sample

**Synthetic demonstration from the earlier OpenTrain application. Not a client deployment. Assumed company policy, not UAE legal advice.**

## Task objective
Can an AI assistant reconcile several HR records, apply written company policy, calculate the approved payroll input and identify uncertainty **without inventing facts**?

## Instructions given to an AI model
> You are reviewing an employee exit for September. Using **only** the synthetic records A–E below, calculate the determinable approved monthly gross payroll input for September under the provided policy. Identify discrepancies and approval items requiring human review. Explain the calculation, cite the source documents and do not assume statutory end-of-service benefits or local legal rules.

## Synthetic source documents — all five

**A — Payroll Policy, Clause 4**

Monthly base pay is AED 18,000. Where employment ends mid-month, the base salary is prorated by calendar days worked divided by 30 (the company method for September). Only approved monthly allowances are paid.

**B — Signed Employment Contract**

Employee ID: P-104. Final day of employment: 20 September. Base monthly salary: AED 18,000. Monthly transport allowance: AED 1,500, payable only if approved in the monthly allowances register.

**C — September Payroll Change Log**

Employee P-104 shown with full base salary AED 18,000 and full transport allowance AED 1,500. Status: **Draft — final payroll batch not approved**.

**D — HR Exit Approval**

Line manager confirms final day: 20 September. HR ticket references P-104 and notes the exit recorded in HRIS.

**E — Allowance Approval Register**

P-104 transport allowance record marked **Pending**. No sign-off timestamp or approver recorded.

## Gold-standard answer

1. Under Policy A, Contract B and Exit Approval D, determinable base input: **AED 18,000 × 20/30 = AED 12,000**.
2. Allowance: AED 1,500 is **not yet approved** under Policy A and Register E; exclude from determinable approved input and route for approval. Do not claim it has been rejected.
3. Draft record C overstates **base salary** by **AED 6,000** (AED 18,000 − AED 12,000). The draft AED 1,500 transport item is an unresolved exception, not an automatic entitlement.
4. The determinable approved gross input under **this fictional policy** is **AED 12,000**, pending separate review of the allowance. Statutory benefits and other deductions are explicitly out of scope.

## Original objective grading rubric — ten points

| Criterion | Points | Correct evidence |
| --- | ---: | --- |
| Uses final working date from B and D and prorating rule in A | 2 | 20 September, divisor 30 |
| Correct base salary calculation | 2 | AED 12,000 |
| Flags transport allowance pending approval | 2 | Must not include AED 1,500 in approved input |
| Detects draft excess base | 2 | AED 6,000 vs C |
| References all five source documents | 1 | A, B, C, D, E |
| Avoids unsupported statutory or external assumptions | 1 | Statutory benefits/deductions not calculated |
| **Total** | **10** | |

## Error analysis — why a model might fail
- **Blind copy of the draft:** says AED 19,500 is payable, overlooking policy and draft status.
- **Wrong proration:** uses 20/31, calendar days excluding the final day, or an undocumented rule.
- **Allowance hallucination:** includes AED 1,500 even though it is still pending approval.
- **Statutory speculation:** invents UAE end-of-service or deduction amounts not supported by documents.
- **Missing provenance:** gives a correct number but no source citations.
- **Conflicting evidence:** if B and D disagree on the exit day, stop and escalate unless a clear source precedence is provided.

## Judge notes
A 10/10 answer must include all rubric elements; it need not match exact prose. An answer that calculates the right number but includes the unapproved allowance **does not pass the allowance criterion**. Scoring should be independently reviewed where annotations require interpretation.

### Accuracy and ethical caveat
The problem **does not** calculate genuine employee legal entitlements, and the fictional /30 policy is only a benchmarking assumption. No HRIS configuration, payroll processing or law-compliance claim is made.
