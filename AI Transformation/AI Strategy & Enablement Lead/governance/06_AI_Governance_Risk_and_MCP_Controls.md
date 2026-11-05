# Responsible AI, information security, MCP and controls

## Governance design
Reference standards and frameworks for assessment: NIST AI RMF, ISO/IEC 42001 and relevant privacy/security requirements **subject to legal validation** for specific jurisdictions and regulated entities. Referencing a standard does **not** imply organizational certification.

## Illustrative risk register
| Risk | Consequence | Required safeguard | Decision owner |
|---|---|---|---|
| Sensitive KYC/KYB data sent to public model | confidentiality/regulatory breach | DLP, approved endpoints, contracts, minimization, retention review | privacy + security |
| Prompt injection through uploaded docs / retrieved sources | tool misuse or untrusted instruction execution | treat documents as data, allowlist tools, structured outputs, privilege separation | engineering |
| Incorrect OCR/LLM field extraction | misidentification / operational rework | confidence, page evidence, field validation, analyst sign-off | product + compliance |
| Automated adverse customer decision | unfairness and legal exposure | prohibit autonomous approve/reject; human ownership | compliance |
| Hallucinated RFP statement | contractual / reputational risk | citations to approved knowledge, legal review | commercial |
| Model/vendor drift | degraded quality | version pinning, shadow tests, rollback and periodic re-evaluation | platform owner |
| Bias by jurisdiction/document type | unequal service quality | cohort-level evaluations and escalation paths | risk + product |
| Unlogged access or data sharing | audit failure | signed evidence trail and access logging | security |

## MCP / tool calling policy
- Default deny; registry of permitted tools and **least privilege** per role.
- Distinguish **read**, **draft**, and **write/commit** actions.
- Never allow free-form tool installation or unrestricted file/network access in production workflows.
- Validate inputs against schemas, constrain egress, bind service identity, implement timeouts and rate limits.
- Require explicit human confirmation for any external communication, record mutation, permission change or regulatory disposition.
- Log tool name, effective privileges, requesting user, correlation ID, arguments with secrets redacted, result status and model/prompt versions.
- Test exfiltration, forged system instructions, malicious PDFs, chain-of-tool privilege escalation and replay attacks.

## Incident path
Detect -> isolate feature/credential -> preserve protected evidence -> assess customer impact -> notify required internal and external parties under applicable rules -> rollback -> root-cause analysis -> revalidate before relaunch.

## Required pre-launch artifacts
DPIA/privacy assessment where applicable, data-flow diagram, threat model, test report, third-party assessment, human oversight protocol, model card/system card, change controls, audit specification and incident runbook.
