# Microsoft Copilot Studio — implementation checklist (NOT EXECUTED)

**Target:** Rebuild the local rule-based demonstration as a true generative `HR Service Agent` in Microsoft Copilot Studio. This guide is a step-by-step *plan*, not proof of a Microsoft tenant or deployment.

Official starting point: https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-gpt-quickstart

## 1. Access and workspace
1. Sign into https://copilotstudio.microsoft.com/ using an eligible **work/school Microsoft account** and an approved environment; use a trial where permitted. Check licence and DLP policies. **Trial permits create/test but not publishing**: https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing-subscriptions
2. Create agent called `HR Service Agent — Policy and Escalations LAB` and label its instructions clearly as **sandbox**. Save agent ID, environment ID, owner and current config version in a private configuration record; never commit secrets.
3. Turn on relevant conversation/testing diagnostics in the tenant subject to privacy controls and retention policies.

## 2. Source grounding
1. Add a **separate synthetic policy document library** (e.g. SharePoint or uploaded example documents) containing only the synthetic policies in [POLICY_KNOWLEDGE.md](POLICY_KNOWLEDGE.md); do not connect employee HR files or HRIS.
2. Enforce current version, effective dates and named policy ownership. Test responses for exact document citations and deliberate source removal/expiration. For no match or unsupported claim require a refusal/handoff. Disable ungrounded broad general-knowledge answers where available and suitable.
3. Restrict knowledge source permissions and check access on every channel. Never rely on prompt text as the security boundary.

## 3. Agent instructions (candidate copy; validate in your tenant)
> You are a limited-scope HR policy assistant for an invented UAE professional-services practice. Answer only general process FAQs with verifiable current citations to the approved synthetic policy library. Never invent personal entitlements, UAE law, immigration or visa guidance. Do not ask for or retrieve ID, medical, salary, payroll or employee records. For missing sources, ambiguous, sensitive, adversarial or employment-decision questions, state the limitation and request an authorised human review. You may draft a request for an employment letter but may not issue or send a letter, decide eligibility, approve anything or modify HR systems. Every answer must identify its policy source and version. No retrieval or connector permission should be broader than necessary.

## 4. Design topics / actions
- `General policy FAQ`: policy grounded answer with source.
- `HR request exception`: route restricted, ambiguous, freshness or unsupported prompts to a **human-owned** flow; use approved routing categories, not hidden personal data.
- `Employment letter request`: construct a draft request and invoke a **separate approval flow**; the agent has no send or HRIS-write permissions.
- `Feedback and correction`: human case owner records policy correction, appeal and test-set updates.

## 5. Test and publish gates
1. Enter all 28 prompts from [test_cases.json](test_cases.json) manually or through a tenant-supported testing method; save test date, agent version, knowledge version, tool permission snapshot, verbatim prompts/responses, citations, author and reviewer.
2. Record multi-turn variants, prompt injection, false policy citations, PII requests, user-identity scenarios, stale library policy and connector-failure conditions. Apply independent HR + technical adjudication. The offline JSON in this repo **does not count** as these results.
3. Build approval/exception flows from [POWER_AUTOMATE_FLOW_SPEC.md](POWER_AUTOMATE_FLOW_SPEC.md); execute real test approvals in the sandbox, capture timestamps and approver decisions.
4. Publish only if the tenant licence allows, security/legal approval is documented, tests pass and access rules are independently verified. A published demo website is *not* production evidence.

## Evidence still required
- Real Microsoft environment and agent ID (redacted when public)
- Screenshots of actual topic/knowledge setup and conversation tests, with date and sensitive values removed
- Exported session trace and version details
- Flow-run ID and approval evidence (masked)
- Independent test review, permissions report and final go/no-go

**Present state: NONE of these Microsoft-specific proof items has been generated.**
