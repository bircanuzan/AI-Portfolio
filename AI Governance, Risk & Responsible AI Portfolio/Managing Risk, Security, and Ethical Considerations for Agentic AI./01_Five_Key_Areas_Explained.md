# 01 — Five Key Areas: Meaning, Examples and Controls

> As Agentic AI becomes more capable, it may operate across multiple systems, access information, and take actions on behalf of the organization. That means organizations need to define clear boundaries before giving an agent any authority.

The five headings below are **original working summaries of the topic** and should not be mistaken for verbatim slide text.

## 1. Authority, permissions and human oversight

**Meaning:** An agent is not an employee with general discretion. Organizations must define who authorized the agent, which tasks it may complete, what systems it can access, where it must stop, and who can intervene.

**Illustrative example:** A recruitment agent may read approved job requirements and generate an interview invitation **draft**, but it must not send the invitation, reject a candidate, alter a salary record, create an offer or change an ATS status without explicit permitted human authorization.

**Key controls:** agent identity; tool allow-list; separate read/write permissions; per-action authorization checks; delegation expiry; transaction caps; manager approval for high-impact steps; manual stop and credential revocation.

**Evidence:** signed agent charter, permission configuration, approval log, denied-action traces.

## 2. Cybersecurity and secure system integration

**Meaning:** An agent's autonomy expands the attack surface. It can process untrusted email, webpages or documents while holding access to tools and internal systems. A prompt injection, compromised connector, insecure memory or malicious API result could redirect the agent.

**Illustrative example:** A supplier PDF contains hidden instructions asking the agent to export confidential applicant profiles. The system must treat document content as data, never as a source of new authority.

**Key controls:** least-privilege connectors; secrets vault; independent policy engine; sandboxed execution; validation of all inputs and tool outputs; network allow-list; authenticated inter-agent messages; request throttles; separated production/test environments.

**Evidence:** threat model, security architecture, denied exfiltration test, connector review and security event log.

## 3. Privacy, data protection and confidentiality

**Meaning:** Agents may cross organizational boundaries, access sensitive information and retain memory or logs. Information must be processed only for justified, authorized purposes, with access and retention restricted.

**Illustrative example:** A policy support agent must not reveal another employee's compensation or medical information simply because a user asks. The agent's tool access must enforce the user's permissions.

**Key controls:** role-based authorization; data classification; field-level filters; data minimization; PII redaction in logs; retention/deletion rules; data protection assessment; vendor and cross-border transfer review; separation of users and sessions.

**Evidence:** data flow and classification map, access-control tests, retention policy, approved vendor terms, legal review of UAE PDPL applicability.

## 4. Fairness, ethics, transparency and accountability

**Meaning:** AI can produce plausible but wrong outputs and embed unfair distinctions. When agents act on those outputs, consequences may scale rapidly. People need clarity about AI involvement and a responsible human decision-maker.

**Illustrative example:** An agent recommends rejecting a candidate for a career gap, although the approved competency criteria do not justify it. The human recruiter must be able to challenge the recommendation and correct the process.

**Key controls:** job-relevant evaluation criteria; fairness tests using legally authorized data; explanation and correction mechanisms; documented agent limitations; human-owned consequential decisions; evidence of review and appeal.

**Evidence:** evaluation protocol, human override record, fairness remediation plan, disclosure and incident logs.

## 5. Continuous monitoring, risk response and compliance

**Meaning:** Risk evolves with model updates, changed tools, altered data, multi-agent delegation and external threats. One-time predeployment testing is insufficient.

**Illustrative example:** After an agent's email tool gains write access, it begins attempting messages without required human approval. Monitoring should detect the attempted action, block execution, trigger a hold and prompt investigation.

**Key controls:** action tracing; versioned models/prompts/tools; anomaly and cost alerts; max tool-chain depth; automatic safe halt; incident owner and escalation tree; periodic control review; regression and adversarial tests.

**Evidence:** deployment approval, structured logs with redaction, monitoring specification, incident rehearsal, release notes and corrective-action register.

## Risk-tiered approvals (illustrative)

| Proposed tier | Example | Suggested default |
|---|---|---|
| Read-only | Search approved internal knowledge | Controlled read access; audit |
| Low-impact reversible | Create a draft or draft calendar event | Human-visible preview; rate limit |
| High-impact or external communication | Send candidate email or update ATS | Named human approval and recorded action |
| Sensitive or irreversible | Candidate rejection, salary edit, data export, payment | Default DENY unless specifically and independently authorized |

These are **proposed enterprise controls**, not an official UAE statutory tier classification.