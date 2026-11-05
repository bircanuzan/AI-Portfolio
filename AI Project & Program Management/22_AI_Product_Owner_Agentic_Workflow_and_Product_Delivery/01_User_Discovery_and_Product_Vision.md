# 01 — Discovery, framing and product vision

## Users (fictional; validation required)
- Employee: "I need a trusted answer or a fast route to a real adviser."
- HR case officer: "I need a complete, authorized escalation with clear evidence and fewer duplicates."
- HR operations lead: "I need to monitor answer quality, deflection, exceptions and support burden."
- IT/security: "I need access controls, traceability, safe tool calls and clear incident ownership."

## Discovery research plan (not interviews already conducted)
10 semi-structured interviews, 3 shadowing sessions, anonymized top ticket categories, data landscape review, click-path mapping and baseline time-to-answer from case logs. Consent/privacy approval before reviewing any sensitive case data.

## As-is service blueprint
Employee sends email -> generic HR inbox -> manual category -> policy lookup / HRIS search -> ambiguous owner -> back-and-forth -> resolution -> manual status. Failure states: wrong recipient, unanswered personal query, stale policy, missing approvals.

## To-be experience
Employee asks -> intent classification and context boundary -> tool/knowledge retrieval ONLY when approved -> cite authoritative policy OR handoff -> show uncertainty and source -> audit-safe case summary -> human close and feedback. User can always ask for human help.

## MVP hypothesis
An assistive service could reduce repetitive low-risk guidance while increasing clarity, not autonomously decide leave rights, eligibility or salary. Outcome measures: grounded answer % and safe handoff %, first contact resolution, time to first useful response, % corrections and cost per resolved request.

## Product decision
Choose deterministic FAQ routing first for high-risk HR domain, then evaluate human-reviewed RAG in controlled environment. This illustrates the owner's judgement about when **not** to use an autonomous AI agent.
