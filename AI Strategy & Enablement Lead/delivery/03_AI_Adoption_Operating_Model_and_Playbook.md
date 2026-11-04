# AI adoption operating model, culture and internal playbook

## Decision ownership (RACI-inspired)
- **CEO / steering group:** strategic sponsor, investment, strategic risk acceptance within legal boundaries.
- **AI Strategy & Enablement Lead:** portfolio, tool selection process, change management, learning, benefits tracking.
- **Head of Engineering / Lead Architect:** code policies, approved integrations, SDLC quality, production controls.
- **Product Owner:** feature outcomes, human decision boundaries, release acceptance.
- **Security / Privacy / Compliance:** access, data handling, regulatory and contractual approval.
- **People/L&D champions:** onboarding, skills assessment, feedback loops, champions network.
- **Task owner:** accountable for work product and verification; never transfer professional accountability to an AI tool.

## Adoption campaign
**Discover -> Design -> Pilot -> Enable -> Measure -> Improve**
- Segment personas: engineers, QA, product, customer success, sales/marketing, leadership.
- Define role-task proficiency rubric: beginner (safe prompting), practitioner (workflow verification), champion (experiment design), approver (risk, escalation and auditing).
- Provide 45-minute onboarding, task-specific job aids, office hours, and monthly AI Innovation Days.
- Integrate 3 exemplar workflows into normal systems; avoid treating attendance as adoption.
- Offer opt-out/alternative route for unsuitable data or inaccessible tools.

## Example AI Innovation Day
1. **15 min:** approved use cases and two real failure modes.
2. **25 min:** hands-on sandbox challenge: test-case drafting or RFP answer source-checking.
3. **20 min:** peer demo with factual review checklist.
4. **15 min:** score outcomes, controls, and lessons.
5. **15 min:** prioritize one owner-backed experiment for next sprint.

## Prompt / review pattern
```text
Role: Assist the authorized employee with [bounded task].
Approved context: [versioned, access-controlled source IDs].
Instruction: Produce a draft and cite source IDs for factual statements.
Never invent company policy, regulatory interpretations, source evidence,
verification outcomes or completion claims.
If input is missing/conflicting, state uncertainty and route to a human.
Output: structured draft, sources, assumptions, open questions.
```

## Communication / culture guardrails
- Celebrate **validated improvements** and documented failures equally.
- Track usage without punitive individual-surveillance rankings.
- Use privacy-preserving adoption aggregates and protected feedback channels.
- Publish playbook version, tool approval status and change log.

## Adoption reporting
Denominator = eligible technical staff with access during measurement window. Numerator = distinct eligible technical staff performing >=1 meaningful approved task with AI in a trailing 7-day period; optionally report >=3 meaningful tasks as sustained-use indicator. Report access gaps and team participation separately.
