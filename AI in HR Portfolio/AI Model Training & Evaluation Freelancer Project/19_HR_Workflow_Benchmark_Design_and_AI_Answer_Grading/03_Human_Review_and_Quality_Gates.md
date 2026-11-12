# 03 | Human Review, Quality Gates and Ambiguity Management

## Why a human reviewer remains necessary
The programmed evaluator only scores structured annotations in a synthetic test. It cannot read and fairly judge arbitrary free-text LLM answers, interpret employment law, or know if documents have been altered. A trained HR reviewer must confirm what the model actually asserted before marking each field.

## Three hard rejection gates
1. **Missing governing policy:** there is no authoritative prorating rule; label ungradeable and request the correct document.
2. **Unresolved last-day conflict:** signed contract says 20 September, approved HR exit says another day, with no documented precedence. Do not invent a tie-breaker.
3. **Outside statutory interpretation required:** if the question cannot be answered without unseen legislation or legal facts, reject or narrow the benchmark.

## Reviewer checklist
- Exact scope and included/excluded calculations documented.
- Sources A–E available and consistent; contract, policy, exit approval and allowance register are distinguishable.
- Date, divisor, salary and allowance approval status supported by named sources.
- Gold answer computed before grading any model output.
- Rubric is observable and sums to 10; no extra credit for eloquence.
- Uncertainty is recorded: unapproved does not mean denied, draft does not mean final.
- Error review distinguishes arithmetic mistakes, evidence mistakes, unsupported assumptions and omissions.
- Version changes logged whenever policy text, date or scoring weights change.

## Prose answer -> structured annotations (human procedure)
From an AI response, record:
- last_worked_day: integer stated or null
- proration_denominator: integer stated or null
- approved_base_aed: explicitly given amount or null
- pending_allowance_escalated: true only if the assistant says allowance is pending and requires approval, and is not included
- allowance_in_approved_input_aed: amount included as approved, normally 0
- draft_base_overstatement_aed: stated discrepancy vs draft or null
- cited_sources: distinct A/B/C/D/E codes actually referenced
- no_statutory_speculation: false if it invents entitlements or external facts.

If the model gives ambiguous figures, a reviewer resolves the annotation or escalates for a second reviewer — **do not fill in what the model probably meant**.

## Evaluation use
Calibrate annotators on at least one strong and one flawed response. Record disagreement by criterion, revise examples without changing the underlying source facts, and retest after any rubric change.

## Scope limitation
Synthetic, business-process-oriented quality benchmark only. Not official OpenTrain scoring, not real employee data, not employment-law guidance, not a live AI evaluation platform.
