# Evaluation rubric — Project Management / AI Evaluation

**For human reviewers.** The automated Python script checks factual, numerical and Boolean reference fields; it does **not** claim to judge natural-language explanations or soft skills. Human ratings below are a proposed protocol, not a completed AI assessment.

## Human review dimensions (0–2 points each; maximum 12)

| Dimension | 0 — Fails | 1 — Partially meets | 2 — Meets |
| --- | --- | --- | --- |
| Mathematical / factual accuracy | Incorrect or invented numbers | Correct direction but incomplete / minor errors | Fully correct calculations and grounded facts |
| Project methodology | Misuses framework or bypasses controls | Partly appropriate with omissions | PMBOK/Agile/Scrum/Waterfall principles applied in context |
| Plan feasibility | Impossible schedule or staffing | Feasible only with undocumented assumptions | Dependencies, capacity and constraints are explicit |
| Risk / change governance | Ignores material risks or unapproved actions | Notes risks but misses owner, mitigation or decision | Explicit risk owner, probability/impact, mitigation and approval gate |
| Stakeholder clarity | Incomprehensible or unsuitable audience | Some clarity, key decision missing | Concise explanation with accountable owner and next decision |
| Evidence / reproducibility | No traceable input or calculation | Partially traceable | Clear inputs, formulas, assumptions and review-ready evidence |

## Workflow

1. Write a realistic scenario and explicit assumptions from fictional professional PM situations.
2. Solve the problem independently and lock a reference answer before comparing AI outputs.
3. Capture model version, prompt, input, output, timestamp and decoding configuration **if** a real model is tested.
4. Apply deterministic checks for calculations, schema and prohibited decisions; have two reviewers independently rate narrative dimensions.
5. Log severity, factual discrepancy, corrective explanation and reviewer confidence; adjudicate substantive disagreements.
6. Run a held-out regression test before sign-off. Reopen severe failures rather than treating an aggregate score as sufficient.

## Proposed KPIs, not claimed outcomes

- Reference-answer agreement (%) and quantitative error by case family.
- Human rubric points earned (0–12), inter-reviewer agreement and critical-risk rate.
- False approval of change requests, dependency / capacity / budgeting mistakes, stakeholder-communication omission.
- Regressions between model versions, reviewer effort per case, resolution turnaround.

## Evidence and ethics

- All bundled candidate outputs were written as **fixtures**. They are **not** responses returned by a real LLM.
- Scripts contain local deterministic PM calculations; no API keys, client artefacts or personally identifiable data.
- The automated evaluation can measure field correctness only. It is not a full quality judgement of generated language.
- Use fictional or licensed inputs; check external model/provider terms and privacy rules before using any real organization data.

## Reference frameworks / tools

PMBOK-style life-cycle governance (scope, schedule, cost, risk, stakeholders, change controls), Agile/Scrum planning, Waterfall dependencies, Excel / Power BI reporting concepts, issue/status artifacts. Jira, Asana and Microsoft Project field mapping is **reference documentation only**; no direct application access, integration or proficiency is asserted.