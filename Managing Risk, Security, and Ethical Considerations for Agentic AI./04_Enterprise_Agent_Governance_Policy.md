# 04 — Enterprise Policy for Agentic AI (Draft)

**Applies to:** AI agents that invoke tools or act on organizational data and systems.  
**Organization:** [ ] · **Version:** 0.1 · **Status:** NOT APPROVED · **Approver:** [ ]

## 1. Registration and delegated authority

Every agent must have a registered name, human sponsor, defined purpose, data and tools list, permitted action types, maximum autonomy level, expiration and an emergency stop owner. No privilege may be granted solely by a natural-language prompt.

## 2. Data and identity

Tools must enforce least-privilege access using a service identity or delegated identity appropriate to context. Never share secrets in prompts. Apply tenant/user separation, retention limits, logging redaction, approval for sensitive transfers and appropriate UAE legal review.

## 3. Tool and workflow authority

- Default unknown tools or actions: **DENY**.
- Separate read, draft, send, update, export, delete, payment and admin permissions.
- Do not allow an agent to approve its own actions or elevate its own privileges.
- Check purpose, user authority, destination, data classification and policy before each consequential tool call.
- Material external communications, HRIS/ATS changes, compensation updates and personally consequential actions require documented human approval.
- No production self-modification or sub-agent privilege inheritance without separate governance approval.

## 4. Ethical obligations

Design and evaluate for fairness, transparency, accuracy, security and accountable human outcomes. Use business-relevant criteria in candidate assessment; allow documented corrections, appeals and overrides.

## 5. Validation and monitoring

Before release: impact assessment, threat model, injection testing, tool permission checks, privacy review, human workflow demonstration and sign-off. After release: track anomalies, tool denials, incident trends, data events, latency, cost and drift. Reapprove changes to models, prompts, connectors, memory, autonomy or data scope.

## 6. Incident controls

On suspected critical compromise: suspend high-risk tool tokens, disable agent routes, preserve privacy-protected event metadata, notify security/owner/legal, investigate exposure, document remediation and retest before restoration. No autonomous restoration after critical hold.

## 7. Go / Hold / Reject decision

**HOLD** for missing legal applicability review, missing human owner, possible uncontrolled PII transfer, unauditable high-impact action, unresolved critical exploit or absent emergency stop. **GO** only after evidence-based approval.

## 8. Approval and exception form

- Agent and version: [ ]
- Tools and privileges authorized: [ ]
- Data classes and regions: [ ]
- Residual risks: [ ]
- Test/evidence links: [ ]
- Human approval policy: [ ]
- Monitoring and stop owner: [ ]
- Security/legal/business sign-off: [ ]
- Review/expiry date: [ ]

This is a sample policy for educational design; it is not adopted or legally vetted.