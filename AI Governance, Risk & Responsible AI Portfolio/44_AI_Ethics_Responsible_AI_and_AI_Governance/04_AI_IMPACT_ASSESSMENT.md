# Completed example: AI-001 Candidate Shortlist Assistant — simulated impact assessment
**Assessment type:** original illustrative **AI Impact Assessment (AIA)**, not a legal certification. **Reviewer:** Fictional AI Governance Office. **Date:** 29 October 2026.

## Intended use and prohibited use
The assistant receives a job profile and applicant evidence, then produces **an evidence-linked shortlist recommendation for a trained recruiter**. Recruiter independently checks relevant qualifications and context; final progression decision is human. **Never** infer age, health, religion, pregnancy, gender identity, nationality suitability, disability or other irrelevant traits. Never auto-reject or send candidate messages.

## Stakeholders and harms
- **Candidates:** disparate selection outcomes, privacy intrusion, lack of correction/appeal, misrepresented career history.
- **Recruiters:** automation bias and time pressure, over-reliance on fabricated citations.
- **Employer:** unlawful bias, audit failure, data leakage and vendor risk.

## Example risk scoring (sample assumptions)
Scale likelihood L1–L5, severity S1–S5; initial risk = L×S; thresholds 1–5 low, 6–11 moderate, 12–25 high. **This is an internal example method, not an ISO-mandated formula.**

| Risk | Initial | Mitigations | Residual estimate | Evidence needed |
|---|---|---|---|---|
| Proxy discrimination via CV features | 4×5=20 High | Job-relevant features only; trained human review; subgroup analysis where lawful and statistically meaningful | 2×5=10 Moderate | Protocol, subgroup outcomes, calibration review, adverse findings |
| Fabricated certifications | 3×4=12 High | Source citation checks; recruiter verifies original proof | 2×4=8 Moderate | Gold-set factuality review |
| Unauthorized CV data exposure | 3×5=15 High | No training on input; encryption; retention and processor DPA; privileged-access test | 1×5=5 Low | DPIA, contract, access evidence |
| Automation bias | 4×4=16 High | Human sign-off; meaningful appeal and blind second-look; user training | 2×4=8 Moderate | Decision log and override samples |
| Prompt injection in applicant CV | 4×4=16 High | Treat CV as untrusted input; allowlisted tools and guardrails | 2×4=8 Moderate | Injection test logs and tool traces |

## Law and framework screening
- Processing of applicant personal data calls for a counsel-led check of **UAE Federal PDPL** applicability and legal basis. DIFC/ADGM regimes only where jurisdictionally relevant.
- EU GDPR or EU AI Act may apply when particular extraterritorial criteria are met; don't assume that all UAE applicants or systems automatically fall within them.
- ISO/IEC 42001 and NIST AI RMF provide governance guidance rather than proof of compliance.

## Required before launch
1. Named business owner and full inventory/model card, versioning and data flow.
2. Privacy counsel approval with lawful-basis and retention checks.
3. Vendor security and subprocessor assessments, regional transfer check.
4. Independently run job-relevance, factuality, adversarial injection, accessibility and fairness tests.
5. UAT for recruiter workflow and candidate correction process.
6. Documented override criteria, recruiter training and post-launch drift/complaints monitoring.
7. Signed high-tier **human review** and committee gate.

**Decision: HOLD.** No validated subgroup/factuality tests, privacy assessment, supplier assurance or real live-system evidence exist in this demonstrator. Any GO would be misleading. This case is intentionally conservative.
