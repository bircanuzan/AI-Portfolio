# Power Automate — Human oversight flow specification (proposed, not executed)

## Flow A — high-risk exception case
Trigger: Copilot Studio topic/action emits `case_type=HR_ESCALATION` with **non-sensitive** category, request ID, policy ID and reason. Validate the sender and schema. Create a restricted-access HR queue item. Notify assigned HR reviewer in Teams (if tenant access allows). Require acknowledgment, decision and resolution note. Capture timestamps, approver identity, audit status and escalation SLA. Return only a neutral tracking acknowledgment to the agent. Fail closed if queue or notification fails.

## Flow B — draft employment-letter request
Trigger: `case_type=LETTER_DRAFT` only after employee identity is validated **outside the agent**. Store draft request in approved restricted list. Use a human approval step. Generate and send a document **only** through an independently authorised HR procedure after checking employee data, entitlements and final approver. The agent has **no HRIS write or document-sending permission**.

## Control and test matrix
| Test | Expected outcome |
|---|---|
| General policy question | No flow invoked; cited FAQ only |
| Sensitive salary request | Route to restricted HR queue; do not disclose |
| Employment-letter request | Human approval is mandatory; no issuance on draft |
| Approval rejected | No letter issued; safe failure response |
| SharePoint / Teams outage | No false completion; retain minimal failure trace |
| Invalid agent or user identity | Reject invocation and log security event |
| Duplicate requests | Idempotency key prevents duplicate cases |
| Flow permission audit | No broad access to unrelated HR records |

## Proof still to collect
Actual flow ID, designer configuration, connector permissions, run history, Teams approval transcript with synthetic data, test dates, and review sign-off. These files do **not** assert working Power Automate integration.
