# Role-calibrated Conversational Blueprint — fictional AI Integration Engineer

**Purpose:** teach development of an explainable, job-relevant interview **workflow**. This is a fictional role; no real client, hiring panel or applicant.

## 1. Role analysis

Business need: build and support reliable AI-assisted HR workflows, API integrations and privacy-preserving human approval controls.

| Competency | Weight | Evidence to explore | Standard question |
| --- | ---: | --- | --- |
| API integration and reliability | 35% | Authentication, idempotency, exception recovery, monitoring | Describe a production-like integration you personally designed. How were auth, failures, retries and observability handled? |
| AI governance and security | 25% | Personal data minimization, authorization, misuse, human review | Explain a case where you prevented an unsafe AI/automation action. What controls did you implement? |
| Debugging and evaluation | 25% | Reproduction, hypotheses, tests, remediation, regression evidence | Describe an integration/AI error you investigated. How did you determine and verify the root cause? |
| Stakeholder judgment | 15% | Decision trade-offs, STAR, communication and measurable outcome | Tell me about a time you challenged a stakeholder's automation request. What did you do and what happened? |

All role weights are hypothetical and have **not** been statistically validated.

## 2. Structured conversation flow

**Intake -> consent -> neutral instructions -> four core questions in fixed order -> limited, preapproved clarification probes -> end-of-session review -> transcript evidence -> assessor calibration -> human-approved report.**

A response without detail may trigger the same neutral probe for any candidate; low verbosity or language fluency must not be used as a proxy for capability. Candidates may ask for clarification or request an accommodation.

## 3. STAR / behavioral event evidence

- **S**ituation: what happened and why did it matter?
- **T**ask: what responsibility did the interviewee actually own?
- **A**ction: what specific choices, tools and interactions did they execute?
- **R**esult: what happened and how was it measured?
- **R**eflection (optional): what would they adapt next time?

Reviewer distinguishes **first-hand concrete evidence** from generalized claims. Do not invent a stronger response; a missing excerpt is **insufficient evidence** and requires follow-up, not necessarily a low capability level.

## 4. Five-level BARS process

- **Level 1:** No credible evidence of job-relevant action or clear unsafe approach.
- **Level 2:** Basic vocabulary or partial example, with key gaps in ownership/controls.
- **Level 3:** Complete, credible example of relevant action, method and outcome.
- **Level 4:** Clear trade-offs, testing, risk management and measured outcomes.
- **Level 5:** Repeatable systems impact with independently verified results and transferable lessons.

These are generic explanatory anchors. Production use requires **competency-specific anchors** developed and reviewed by qualified SMEs, calibration and validation.

## 5. Talent Insights Report schema

```json
{
  "role_blueprint_version": "demo-1",
  "session_status": "human_reviewed_synthetic",
  "human_reviewer": "fictional-rater-001",
  "competencies": [
    {
      "name": "API integration and reliability",
      "rating_source": "trained human",
      "rating_1_to_5": 3,
      "answer_quote": "I added idempotency keys and tested retry behavior",
      "rationale": "Evidence of explicit design and error-control decisions",
      "coverage": "partial"
    }
  ],
  "decision": "Human reviewer only; no automated hiring decision"
}
```

The report must include precise source spans, coverage and uncertainty; redaction of unrelated personal details; audit metadata; reviewer overrides; any needed accessibility accommodations (stored separately with minimum necessary access); and feedback/appeal routing.

## 6. Feature differentiation and use cases

**Publicly described category:** job-calibrated AI interviews, behavioral/technical competency reports, hiring at scale, leadership intake, high-potential identification, succession planning, consent, audits and ATS/HRIS output.

**Independent possible extensions:** adaptive but equivalent question selection; engineer-specific system-design exercises; internal mobility skill portability; learning recommendations after human review; recruiter/assessor calibration dashboard; multilingual fairness checks; trace-level LLM evaluation; enterprise human approval service.

## 7. Product metrics

Evidence coverage; unsupported-quote rate; consistent interview question coverage; assessor agreement; auditability; fairness/accessibility review; candidate completion and opt-out; time-to-review; false claims; latency; cost per completed assessment; talent decision quality **only** if measured through a justified and validated study. No invented time-saving or accuracy claims.
