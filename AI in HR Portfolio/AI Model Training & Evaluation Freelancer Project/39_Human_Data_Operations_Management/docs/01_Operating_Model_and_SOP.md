# 01 — End-to-End Operating Model and SOP
## Project charter and scope
**Business outcome:** produce consistent human-labeled examples for an AI routing model, subject to human approval. Deliverables are a traceable dataset, exceptions/adjudication register, weekly operations report and improvement proposals. Illustrative volume: 48 synthetic requests in six classes; this is not a production volume commitment.

## Workflow with control points
1. **Demand intake:** product owner specifies model task, classes, business cost of misrouting, target delivery, privacy risk and acceptance criteria. Ops lead signs scope; ML engineer confirms schema compatibility.
2. **Collection and source control:** collect only approved de-identified text; record source ID, collection date and processing permissions; reject off-scope records.
3. **Preprocessing:** normalize whitespace/encoding and language fields, detect missing source IDs/duplication/potential identifiers, preserve original immutable source.
4. **Annotation preparation:** version six-class taxonomy, publish positive/negative examples and precedence rules; train annotators against calibration batch.
5. **Allocation:** balance workload by reviewer capacity and risk; enforce independent reviewer A/B assignments. Log work times, batch, reviewer and task state.
6. **First-pass and QA:** assign two independent labels; validate field completeness and allowed classes. Privacy incidents routed immediately, not used as training data.
7. **Adjudication:** disagreements, low-confidence cases and flagged policy-sensitive decisions require a designated human SME; maintain rationale, final label, date and reviewer ID.
8. **Release:** execute automated schema/quality checks; require gates and signed ML/operations/privacy approvals. HOLD if any failed.
9. **Insights:** publish throughput, quality, queue aging, SLA risk, rework, disagreement types, productivity and trend commentary with numerator/denominator.
10. **Improve:** use Pareto of exception reasons, guideline revisions and targeted re-calibration. Deploy at most one experimental change per measurement window.

## Operational exception examples
| Trigger | Response | Owner |
|---|---|---|
| Incomplete source or duplicate ID | Quarantine item; reconcile before assignment | Data steward |
| Conflicting labels | Refer to adjudicator; keep original labels and decision rationale | QA lead |
| Possible personal identifier | Hold affected record; restricted privacy review | Privacy owner |
| Falling agreement/kappa | Stop release; calibrate; sample recurring confusion | Ops manager |
| SLA at risk | Rebalance capacity; notify request owner, prioritize high-risk items | Ops manager |
| Schema/version mismatch | Block downstream export; agree schema with ML engineer | ML engineer |

**Definition of done:** provenance linked, validation checks passed, high-risk exceptions closed, adjudication signed, release gate green, versioned export and management report issued.
