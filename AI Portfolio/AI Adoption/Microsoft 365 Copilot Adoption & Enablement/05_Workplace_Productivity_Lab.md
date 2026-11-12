# Scenario lab — fictional UAE enterprise Copilot adoption
This is an **original scripted workshop simulation**; all inputs and expected outputs are invented. No Microsoft 365 Copilot inference or application deployment was executed for this portfolio case.

## Scenario 1 — Finance month-end variance note
**Synthetic input:** Department A budget AED 400,000, actual AED 425,000; Department B budget AED 250,000, actual AED 239,000; Department C budget AED 180,000, actual AED 195,000.

### Prompt template (for a licensed supported app or Chat, after permissions check)
"Based only on the sample budget and actual figures given below, create a brief variance commentary with amount and percentage for each department. Highlight which variances need management review. Do not invent causes; list additional information needed."

### Gold-standard arithmetic (manually verified)
- A: **+25,000 AED / +6.25%** over budget.
- B: **–11,000 AED / –4.40%** under budget.
- C: **+15,000 AED / +8.33%** over budget.
- Group: budget **830,000 AED**, actual **859,000 AED**, net **+29,000 AED / +3.49%** over budget.

**Facilitator asks:** "Which claims in the AI narrative are calculations, and which are proposed explanations not supported by facts? What should finance verify before sending to a VP?"

## Scenario 2 — HR onboarding draft
**Synthetic source:** New employee start = 16 November; IT setup deadline = 12 November; HR orientation = 17 November; employee ID documentation status = pending. All dates are purely fictional.

**Prompt:** "Draft a short new-starter email based ONLY on these details. Do not assert the employee's documents are complete or invent access credentials. List questions for HR."

**Success rubric:** factual accuracy (4), disclosure-minimization (2), actionable clarity (2), human signoff (2); total 10. Draft fails if it invents a visa/ID status.

## Scenario 3 — Executive decision memo
**Synthetic problem:** Board has three competing initiatives, unknown costs, unknown security readiness.

**Prompt:** "Turn these initiatives into a one-page decision brief with options, assumptions, dependencies, risks and five questions for the board. Clearly mark absent information as UNKNOWN. Do not recommend a purchase until finance/security approval."

**Success:** distinguishes known vs assumptions; gives decision-maker meaningful questions, not fabricated ROI.

## Scenario 4 — Teams meeting follow-up
**Synthetic input:** "Owner: Maya to review operations process by 20 November. Finance pending cost estimates. VP requests decision on 25 November. No agreement on vendor."

**Prompt:** "Create action log with owner, deadline, current decision status and unresolved risks. Never turn an unresolved action into an approved decision."

**Verification:** Owner present; no fabricated cost; status correctly pending; escalate missing evidence.

## General evaluation rubric (0–10)
- 0–4 factual correctness and source fidelity
- 0–2 completeness against explicit task
- 0–2 privacy / no fabricated assumptions / human oversight
- 0–2 usability and role relevance

**Critical-stop conditions:** personally identifiable data without authorization, incorrect financial calculations, fabricated policy obligations, unauthorized transactions, or material unsupported executive claims. Never claim this simulated scorecard measures actual Copilot model performance.
