# Recruitment AI vendor assurance | Executive risk committee and funding decision

**Project 55 strengthens AI governance, not a new sourcing / candidate-screening project.**

## Executive decision record
**Decision:** HOLD automated screening and live Claude/ATS integration pending independent evidence.

**Reason:** The toy screener exhibits nine unjustified routing flips in 16 synthetic pairs; a corrected toy scorer with zero flips is not job-valid, representative or legally reviewed. The 17 Claude-compatible folders are design-only; the source-code catalogue checks written constraints, not actual model behaviour.

## Procurement and model risk requirements
| Evidence required before consideration | Vendor / delivery owner | Independent challenge |
|---|---|---|
| Intended purpose and excluded use cases; identity of responsible controller/processor | AI Product Owner and vendor | CHRO/CAIO |
| Role-related selection validation, sampling design, feature provenance and known limits | Assessment specialist and supplier | Independent qualified assessor |
| Jurisdictional privacy, transparency, data retention and permitted candidate data handling | Legal / Data Protection | Privacy & Compliance |
| Bias/impact analysis where lawful, accessible alternate route, appeal and adverse decision review | Responsible AI / TA | Assessment / Legal |
| Technical architecture: hosting, data flow, secrets, model/version logs, PII and prompt-injection safeguards | IT Security / Vendor | Security Assurance |
| Task accuracy, citation fidelity, hallucination, prompt injection, reviewer override and robustness checks | AI Eval team | Independent QA / HR SMEs |
| Cost: licences, implementation, monitoring, human review, training, support, exit and retraining | Finance / Procurement | CHRO + CAIO |
| Incident escalation, rollback, vendor exit, audit/export rights, country transfers and subprocessor changes | IT Ops / Procurement | Risk Committee |

## Risk appetite and launch gates
- **Immediate HARD HOLD:** automated rejection/selection, covert sensitive-trait inference, candidate PII in unapproved LLMs, unverifiable legal/licence claims or missing human appeals.
- **Proposed pilot-only support:** non-sensitive drafting, workflow completeness checks and reviewer-guided summaries *after* source tracing, security and local policy review.
- **Production consideration:** requires signed business case, legally valid basis, controlled data, independent real-world evidence, role-specific validity, safe human appeal, monitoring/kill-switch and vendor obligations. None are in this repo.

## Model monitoring service-level objectives (definitions only)
- Unsupported assertion / source mismatch rate by task.
- Human override/rework rate, stratified by workflow and lawful sample criteria.
- Candidate communication error/complaint response time.
- Policy/knowledge-source freshness and relevance drift.
- Security incidents and privileged tool-action denial.
- Retrieval quality, opt-out accessibility and appeals closure.
- Expense-to-verified-benefit variance, including paid human review time.

Record denominators, true sample size, thresholds, monitoring windows, false-negative risks, reviewers and incident severity. Do not claim thresholds were met without observed evidence.

## Three-lines assurance model
1. **First line:** TA operations and AI product team own tasks, data quality, runbooks and human reviews.
2. **Second line:** legal/privacy, cyber, responsible AI and HR governance independently challenge data/tech/design choices.
3. **Third line:** Internal audit evaluates controls, evidence integrity and reporting independently where applicable.

## RACI and incident response
- CHRO approves recruiting operating outcomes; CAIO owns AI lifecycle controls; Finance approves economics; Legal/Privacy validates lawful basis; IT owns technical security; hiring managers and assessors own candidate decisions; Audit assures controls.
- If a real model shows unreliable source use, privacy leakage, unfair adverse impact, automated high-stakes action or untraceable output: stop affected feature, preserve secure incident evidence, use human manual fallback, assess/report obligations with Legal, remediate, independently retest, then require formal restart decision.

**Current status:** policy/control proposals, not actual legal compliance, model vendor due diligence, third-party audit or ISO/IEC 42001 certification. Existing [reproducible synthetic HOLD gate](END_TO_END_ASSURANCE_AND_HUMAN_GATE.md) remains decisive.
