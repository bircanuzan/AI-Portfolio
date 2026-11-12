# Financial AI Evaluation Rubric and Decision Rules

| Criterion | Weight | Typical evidence |
|---|---:|---|
| computational correctness | 30% | Reproduced calculation, formula, units and correct denominator |
| source fidelity | 25% | Matches approved documents and report periods |
| analytical reasoning | 20% | Sound assumptions, traceable steps, justified conclusions |
| instruction adherence | 10% | Requested format, entity and timeframe |
| uncertainty / risk handling | 15% | No invented regulation, evidence or unjustified confidence |

Each category scored by a human reviewer: 0 unacceptable, 1 major error, 2 partial, 3 acceptable minor issue, 4 meets criteria. A critical formula or source mismatch is a fail regardless of the total rating.

## Case-specific checks
**Banking:** recognize posting date vs value date, transaction reference and partial receipt.
**Accounting:** assets = liabilities + equity; margin is net income / revenue; do not substitute EBITDA.
**Insurance:** do not invent coverage terms; distinguish premium, claim, deductible, excess and limit.
**Risk:** separate descriptive statistics from forward-looking conclusions; date and jurisdiction matters.
**Spreadsheet testing:** hidden/unrounded values, formula dependencies, data type conversion, mismatched IDs and external receipts require explicit reconciliation.

## Reviewer output
case_id | model_answer_excerpt | incorrect_claim | documentary_evidence | corrected_formula | severity | recommended_feedback | reviewer | date | final_disposition

## Quality gates
1. Document and numerical reference data must be validated independently.
2. Do not accept claims about legislation, pricing, insurance cover or investment returns without authoritative sources.
3. Human adjudication for financial, legal or customer-data consequences.
4. Store data provenance and test results; do not leak real account or customer information.
