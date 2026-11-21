# 06 — Cross-Functional Use Cases (Fictional)

These are **generic business requirements and product discovery examples**, not implementations at Modon, ADNEC or any client. They illustrate the public job brief's combination of AI tooling, customer platforms and subsidiaries.

## UC-01 Internal knowledge and business assistance
**Need:** Employees locate approved policy/process guidance.  
**Candidate capability:** Claude or enterprise assistant, with retrieval from authorised internal sources; Microsoft Copilot/Foundry as alternative architecture considerations.  
**Boundary:** Role-based permissions, provenance, no confidential prompt use without approved contractual controls, human check for high-stakes output.  
**Metrics:** Adoption, correct-source citation rate, resolution time and escalation rate.  
**Acceptance:** Evaluated on a synthetic question set; sensitive requests refused/escalated.

## UC-02 Learning and communications video production
**Need:** Business teams produce short approved training/internal update videos.  
**Candidate capability:** Synthesia.  
**Boundary:** Speaker/voice likeness consent, legal/brand approval, accessibility, no impersonation, no personal-data leakage.  
**Metrics:** Training completion, content reuse, publication approval defects and time to prepare.  
**Acceptance:** Editor and approver sign off each released asset.

## UC-03 Contact centre and service communications
**Need:** Customer teams improve voice/SMS workflows and support response.  
**Candidate capability:** Telnyx with approved enterprise orchestration and human handoff.  
**Boundary:** Consent, recording notices, privacy, telecom requirements, rate/cost limits, no handling of OTPs outside specifically approved flows.  
**Metrics:** Service level, successful handoffs, incident rate and cost per resolved interaction.  
**Acceptance:** PII handling and opt-out paths tested before release.

## UC-04 Brand and design ideation
**Need:** Creative teams generate concept mockups for review.  
**Candidate capability:** Midjourney.  
**Boundary:** IP/trademark checks, rights, confidentiality and human editorial approval.  
**Metrics:** Time to shortlist concepts, rejection/approval rates and brand compliance.  
**Acceptance:** No creative output published automatically.

## UC-05 Resident / customer super-app assistant
**Need:** Customers find facilities, service information and support routes.  
**Design choice:** A governed assistant integrated through approved APIs, with live service information coming only from permissioned systems.  
**Boundary:** No fabricated availability/prices; prohibit autonomous transactions without user confirmation; privacy and audit trail.  
**Metrics:** Grounded answer rate, successful deflection, human escalation rate and CSAT.  
**Acceptance:** Integration, security, hallucination and handoff tests.

## UC-06 Loyalty and engagement services
**Need:** Explain points and offers or provide relevant help across loyalty touchpoints.  
**Design choice:** AI as a bounded presentation/assistant layer over a verified loyalty service of record.  
**Boundary:** No unilateral alteration of balances or terms; user consent, fairness, explainability and human approval for exceptions.  
**Metrics:** Accuracy, task completion, complaint rate and containment of non-authorised changes.

## Cross-product guardrails
One intake and portfolio registration process; business-unit product owners; vendor assurance; logs proportionate to purpose; approved prompts/data; tested fallback; reliable cost attribution; transparent opt-out; human support; and formal change control.
