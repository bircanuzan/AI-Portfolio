# HumanEvoX Responsible Agentic AI policy — demonstration draft v0.1
**Owner:** HumanEvoX (proposed); **approval:** pending; **status:** not an adopted operational company policy.

## Policy position
Use AI to assist humans, not replace accountable hiring, legal or people decisions. Scope: synthetic recruitment-policy answers and candidate communications. AI output is not legal advice and must cite an approved source when conveying a rule. Personal candidate data must never be pasted into a public demo repository.

### Allowed, restricted and prohibited
- **Synthetic-only demos:** read verified policy snippets, generate **draft** communications; `ALLOW_DEMO_ONLY` means no tool is invoked.
- **Requires a human approval record in any real deployment:** sending applicant messages, changing ATS status, record deletion, exports.
- **Never allow autonomous consequential HR decisions:** candidate scoring/ranking/rejection, inference of protected traits, sensitive-data judgments.
- **Reject** prompt injection, unauthorized tools, missing lawful basis, or unreviewed transfers.

## Human–agent accountability (illustrative RACI)
| Activity | HR decision owner | AI governance lead | Privacy/legal | Technical owner | Independent reviewer |
|---|---|---|---|---|---|
| Define use case and human decision | A/R | C | C | C | I |
| Risk assessment / intended use | C | A/R | C | C | I |
| Privacy basis / transfer decision | C | C | A/R | C | I |
| Implement tool permissions | C | A | C | R | C |
| Release acceptance | A | R | A for legal/privacy | R | C |
| Test quality / bias / adversarial cases | C | A | C | R | R |
| Investigate incident | C | A | C | R | I |
A=Accountable; R=Responsible; C=Consulted; I=Informed. For a real organization avoid split A authority on a single decision; formalize approvals per decision type.

## Original demo control catalogue
| ID | Control intention | Verification artifact |
|---|---|---|
| C-01 | Untrusted instructions cannot override approved policy/tools | Injection tests with detected/blocked examples |
| C-02 | Tool allowlist + least privilege | Access and tool inventory; denied-call logs |
| C-03 | Documented lawful-basis review before candidate processing | Processing record reviewed by legal/privacy owner |
| C-04 | Prior cross-border transfer risk and safeguards review | Supplier, jurisdiction and safeguards assessment |
| C-05 | Never execute autonomous candidate data export | Export approval ticket and execution separation |
| C-06 | Human gate for state-changing actions | Identity-bound, time-stamped approval + outcome |
| C-07 | Substantive human assessment for candidate ranking/selection | Review notes; fairness/quality evidence |
| C-08 | Versioned, approved authoritative policy sources | Source index; last reviewed date |
| C-09 | Additional review for sensitive data | Minimization, protective controls and counsel sign-off |
| C-10 | Reason-coded decisions, immutable evidence in production | Trace and retention policy; internal audit sample |

### Incident and exception procedure
1. Stop external action and preserve minimum necessary evidence safely.
2. Contain access/token permissions; notify designated incident owner.
3. Classify potential privacy, discrimination, security, integrity or supplier incident.
4. Refer legal/regulatory notification thresholds to qualified counsel for the *applicable* regime; do not invent reporting periods.
5. Log severity, owner, harm, root cause, containment, corrective action, target, validation and decision to restore.
6. Retest failed controls and obtain sponsor sign-off; issue a versioned update.

### Change control
A change in model, provider, prompt, tool, data category, purpose, jurisdiction, law or policy source triggers re-assessment; keep old baselines and traceable retests. Real deployment requires independent technical penetration/security and privacy reviews.
