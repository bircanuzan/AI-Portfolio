# Enterprise Voice Agent Configuration Audit — Illustrative template

| Dimension | Reviewer questions | Failure example | Remediation recommendation |
| --- | --- | --- | --- |
| Intent and scope | Are goals explicit and business-approved? | Agent invents out-of-scope answer | Constrain supported intents |
| Knowledge quality | Is source ownership and freshness recorded? | Stale fee information | Source links, expiry and review owner |
| Prompt and persona | Are tone, consent, disclosure and escalation clear? | Incorrect promise or impersonation | Rework system instructions |
| Tools and permissions | Are tool contracts, allowlists and failure modes set? | Sensitive CRM access from untrusted text | Minimum permissions, server-side checks |
| Agent testing | Are next-reply, tool-call, simulation regressions maintained? | Single happy path only | Add edge cases and repeat trials |
| Language | Is each language approved by competent reviewers? | Wrong terminology in Arabic | Native-language test pool |
| Reliability | What happens during timeouts, network errors and interruptions? | Silent failure | Timed retry plus human fallback |
| Analytics | Are success/failure/unknown and cost definitions stable? | Unknown calls excluded | Segment and report denominators |
| Privacy | Are consent, retention and personal data rules enforced? | Sensitive call logs exported | Security, legal and lifecycle review |
| Accessibility | Can callers repeat, slow down, switch or request human support? | Inaccessible long monologues | Flexible dialogue and immediate handoff |

**Score proposal:** 0 missing, 1 partial, 2 demonstrated in controlled test. A high total never substitutes for mandatory privacy, human handoff and security approval. No real system was audited.

Source concepts: https://elevenlabs.io/docs/eleven-agents/customization/agent-testing and https://elevenlabs.io/docs/eleven-agents/customization/agent-analysis
