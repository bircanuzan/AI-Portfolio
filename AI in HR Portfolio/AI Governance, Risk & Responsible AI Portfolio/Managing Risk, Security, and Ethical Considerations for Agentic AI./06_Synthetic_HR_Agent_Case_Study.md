# 06 — Fictional UAE HR Service Agent: Secure Human–AI Workflow

**Fictional demonstration design. No live agent test or deployment is claimed.**

## Business problem

HR employees spend substantial time locating policies and preparing interview communications. A hypothetical UAE company proposes an HR support agent connected to an approved HR knowledge base, a restricted ATS view, and a draft-only email function.

## System and permitted authority

| Component | Allowed | Disallowed by default |
|---|---|---|
| HR knowledge base | Retrieve approved policy and cite source | Read confidential employee case folders |
| ATS | Read approved role criteria | Reject candidate or update status |
| Email | Draft communications for review | Send without human approval |
| HRIS and payroll | No access | Read employee medical/payroll data |
| Agent memory | Temporary scoped context | Retain candidate personal data beyond approved policy |
| Human reviewer | Accept, amend or reject agent advice | Delegate final hiring decision to agent |

## Illustrative end-to-end process

1. HR user requests a draft interview invitation.
2. Backend verifies user authorization and loads approved job details.
3. Agent drafts message without exposing unnecessary personal data.
4. Human reviewer checks proposed details and wording.
5. A separate authorized send action may be approved by the human.
6. Event log links agent version, relevant draft, approval and delivery ID, with appropriate redaction.
7. HR owner monitors exceptions and can disable the agent immediately.

## Risks and proposed controls

- **Prompt injection in candidate CV:** untrusted text is not executable instruction; outbound tools gated.
- **Unauthorized ATS status update:** no update permission on service account.
- **Sensitive data leakage:** document classification and field-level retrieval.
- **Misleading policy answer:** source-linked retrieval and escalation on uncertainty.
- **Biased candidate recommendation:** no autonomous evaluation/rejection; job-relevant criteria; authorized fairness testing if that feature is later introduced.
- **Unbounded tool chain:** step, budget, time and retry caps.

## Proposed success criteria (NOT measured)

- 100% of high-impact actions require actual valid human approval.
- 0 successful unauthorized exfiltration or privilege escalation attempts in defined adversarial tests.
- A test-ready, traceable audit path for each material agent action.
- Documented approved-answer accuracy threshold established before testing.
- Emergency stop blocks tool invocation in a controlled drill.

These are **targets/proposed gates**, not results. Real data requires lawful authorization and independent ethical/legal assessment.

## What would constitute genuine evidence later?

Actual tool-call traces (including denials), complete test prompts, saved model responses, system version, redacted logs, signed human approvals, independent ratings and a reproducible test script.