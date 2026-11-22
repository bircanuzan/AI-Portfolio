# Prompt Assessment
**Bircan Uzan | HumanEvoX Consultancy**

Independent, synthetic portfolio exercise demonstrating complex prompt design, model-output evaluation and rubric development. This pack was created for the portfolio; it contains no employer assessment, client records or live model-run results.

## Business problem and requirement
A business needs a reliable month-end receivables review. A model must connect invoice eligibility, reporting dates, matched payments and disputes before producing a usable file. A fluent explanation alone is insufficient: calculations, source references and exception handling must agree.

## What I demonstrate
- Translate an operational workflow into a demanding, reproducible prompt.
- Define the reporting cutoff, output schema and evidence hierarchy.
- Separate missing evidence, disputed balances and confirmed collectible balances.
- Design observable, weighted grading criteria with reference answers.
- Document failure modes and refine instructions without leaking answer totals.
- Review structured outputs and route material uncertainty to a human.

## Included deliverables
- A synthetic four-invoice task and expected-answer reference below.
- A refined prompt ready for a manual model trial.
- [Eight-criterion scoring rubric](rubric.csv).
- Failure-analysis protocol, run log schema and governance controls.

## Synthetic source data
All amounts are AED. Reporting cutoff: **2026-11-20, inclusive**. An invoice enters the report if its issue date is on or before cutoff. Payments count only when matched to an invoice and received on or before cutoff.

| Invoice | Issue date | Due date | Amount | Matched payment | Payment date | Status |
|---|---|---|---:|---:|---|---|
| P101 | 2026-11-01 | 2026-11-10 | 1,200 | 1,200 | 2026-11-09 | Accepted |
| P102 | 2026-11-05 | 2026-11-10 | 800 | 300 | 2026-11-15 | Accepted |
| P103 | 2026-11-10 | 2026-11-18 | 650 | 0 | None | Disputed; acceptance not established |
| P104 | 2026-11-21 | 2026-11-30 | 450 | 0 | None | Future issue date |

Dispute rule: retain the open balance in total receivables but classify it as disputed, not confirmed collectible. Age is max(0, cutoff minus due date) in whole calendar days. A dispute does not erase the invoice or resolve liability.

## Methodology and workflow
1. Map required decisions and source fields.
2. Start with the baseline prompt: “Review these invoices and tell me what to collect.”
3. Identify ambiguity in eligibility, cutoffs, disputed amounts, payment matching and deliverable format.
4. Replace it with the explicit prompt below.
5. Save each actual model response without altering it, then grade against the CSV.
6. Link every failure to a source row, criterion and output location.
7. Record proposed prompt changes and re-run with the model/version held constant where possible.

No baseline or refined model trial has been run in this pack. The baseline is an illustrative starting instruction, not an observed failed attempt.

## Refined assessment prompt
> Using only the four source records and rules in this README, prepare an invoice-level receivables CSV and a management review note as of 20 November 2026.
>
> Return fields: invoice_id, included_at_cutoff, invoice_amount_aed, matched_cash_at_cutoff_aed, open_balance_aed, overdue_days, classification, evidence_note.
>
> Include all four rows for traceability, but exclude future-issued invoices from reporting totals and label them excluded_future. Classify eligible rows as settled, confirmed_collectible or disputed. Do not infer acceptance, write off a disputed balance, invent payment evidence, or treat a future invoice as currently receivable.
>
> Report eligible invoiced value, matched cash, open receivables, confirmed collectible balance and disputed balance. Explain the reconciliation and name the unresolved decision requiring human review. Preserve the source data. If file creation is supported, save receivables_review.csv; otherwise provide valid CSV in a code block and clearly state that no file was saved.

## Reference answer and checks
| Output | Expected |
|---|---:|
| Eligible invoiced value | AED 2,650 |
| Matched cash | AED 1,500 |
| Open receivables | AED 1,150 |
| Confirmed collectible | AED 500 |
| Disputed | AED 650 |
| Future invoice excluded from totals | AED 450 |

P101: settled, open 0, overdue_days 10 under the stated calendar-age definition; this is age relative to due date, not a claim of payment delinquency.
P102: confirmed_collectible, open 500, overdue_days 10.
P103: disputed, open 650, overdue_days 2.
P104: excluded_future, not in report totals; overdue_days 0.

Reconciliation: 2,650 - 1,500 = 1,150 = 500 + 650.
Human action: confirm acceptance/dispute resolution for P103 before classifying it as confirmed collectible.

## Failure cases to assess
- Includes P104 in current totals: temporal eligibility failure.
- Reports 1,150 as confirmed collectible: dispute classification failure.
- Writes off P103: unsupported commercial decision.
- Uses 800 as P102 open balance: ignores matched payment.
- Claims a file was saved while only returning text: deliverable-integrity failure.
- Describes a dispute but still includes it in confirmed collection: rationale/calculation inconsistency.

## Scoring and review
Each CSV criterion is binary: award its weight only when all its conditions are evidenced. Total possible score: 100. Record an explanation and source/output location for every score. Any invented settlement, acceptance or file-save claim triggers human review regardless of total. Suggested review threshold: 85/100 with no critical flag; this is a project policy, not validated against hiring outcomes.

Run log fields: run_id, date, prompt_version, model/version, output_filename, criterion_id, score, evidence_location, failure_category, reviewer_note, second_review_status. Keep reference answers separate from the prompt during a trial.

## Tools and technology
**Used in this pack:** Markdown, CSV, manually derived reference calculations, structured evaluation criteria and source-to-output traceability.
**Suitable execution tools:** a spreadsheet editor for totals and CSV inspection; an LLM interface for a separately logged trial; an optional screen recorder where consent and task rules permit.
No API integration, automated grader, Python execution or live model benchmarking is claimed.

## Results, limitations and next steps
Delivered one task, four fictional invoice records, eight weighted criteria, a reference reconciliation and a failure-review protocol. Reference totals reconcile arithmetically. This is a ready-to-use assessment pack, not measured model accuracy or a paid client delivery. Next: run blinded trials, retain generated files, independently calibrate scores and report disagreement before claiming comparative improvement.

Do not record real candidate/client screens or upload confidential documents. Review any consequential financial action manually; this exercise authorizes no collection action.
