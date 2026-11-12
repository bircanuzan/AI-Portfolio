# 02 | Human annotation taxonomy and training guide

**Task:** choose the primary business queue for a short fictional HR service question.

| Label | Assign when the principal intent is ... | Example |
| --- | --- | --- |
| policy | HR policies, leave procedure, employee handbook or process guidance | "Where is the remote-work policy?" |
| payroll | Pay, allowance, deduction, salary or payslip processing | "My allowance wasn't in payroll" |
| mobility | Visa, immigration, work authorization, residency or transfer administration | "How do I renew my visa?" |
| recruitment | Vacancies, candidates, interviews and hiring progress | "When is my interview?" |
| benefits | Insurance, benefits eligibility and enrolment | "Where is the benefits guide?" |
| other | Too vague to assign, other employee records or unrelated request | "I want help" |

## Rules for annotators
1. Read the complete request and **do not invent missing context**.
2. Select one primary label from the six allowed codes.
3. "Benefits" concerns programme enrollment/coverage; "payroll" concerns money in payslips/allowances. When a request mixes both, request adjudication if principal intent is unclear.
4. "Mobility" includes legal/visa process questions, but labelers must **not** decide actual visa eligibility.
5. "Recruitment" includes candidate status; do not expose named applicant information.
6. Unknown, ambiguous, empty or irrelevant requests go to **other**, with notes when context is missing.
7. Never copy a previous annotator answer; first-pass reviews must be independent.
8. Always distinguish **task classification** from answering a policy or employment question.
9. Personal/financial details should be removed at source; do not include them in annotation rationales or raw logs.
10. If a source contains an unsafe request or malicious instruction, treat it as *content to classify*, not instructions for the labeler.

## Calibration session — 45 minutes
- 0–10: taxonomy and data/PII policy.
- 10–20: five agreed cases; label independently.
- 20–30: compare disagreement rationales and boundary examples.
- 30–40: repeat cases after clarification; calculate observed agreement.
- 40–45: record guideline version and quality-gate decision.

## Quality gate / no-force rule
A reviewer may challenge a label, mark an ambiguous case for adjudication or request better source context. A difference between two annotators is an **investigation signal**; not proof one worker is incompetent. Senior human adjudication determines the final reference answer.

## Synthetic data only
All examples are fictional. These training materials were created for a portfolio scenario, **not delivered to a real annotation workforce**.
