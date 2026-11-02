# AI Impact Assessment & Use-Case Intake (Illustrative)

**Use case ID:** UC-HR-001  
**Intended purpose:** Answer fictional internal HR policy questions with a linked and current source.  
**Intended users:** Internal HR staff only; no autonomous employment decisions.  
**Excluded:** Giving legal advice; candidate selection; payroll disbursement; government filing; autonomous action.  
**AI system:** Mock responder driven by hand-authored fixture (no live LLM).  
**Accountable owner:** Fictional HR Policy Owner.

| Dimension | Assessment question | Example treatment |
|---|---|---|
| People affected | Could employees act on an inaccurate answer? | Display limits; escalation to policy owner |
| Source provenance | Is the source legally and operationally authoritative? | Legal SME confirmation for real laws |
| Accuracy | Are answers supported by applicable and effective policy? | Version-and-answer test suite |
| Explainability | Can a reviewer see the relevant clause and version? | Exact evidence/source ID requirement |
| Fairness | Are different groups disproportionately disadvantaged? | Not evaluated in this toy dataset; require representative data and lawful audit plan |
| Privacy | Can employee or candidate data enter prompts/logs? | Minimise, redact, restrict access and retention |
| Security | Can prompt injection redirect the assistant or agent? | Untrusted content isolation and least privilege |
| Change | What triggers reassessment? | Policy, model, prompt, retrieval index, agent tool, jurisdiction and workflow changes |
| Third parties | Is the model/vendor's claim verified? | Vendor documentation, independent tests, documented exceptions |
| Human oversight | Who can halt or release the system? | Governance owner + independent reviewer + risk forum |

## Risk appetite / scoring (illustrative)
Likelihood and impact are independently rated 1–5; **risk score = likelihood × impact**. The sample register uses these categories only as teaching aids. Risk appetite and thresholds must be authorised for a live deployment.

## Decision gates
**Intake** -> **Risk review** -> **Test design** -> **TEVV evidence** -> **Independent review** -> **Approval/HOLD** -> **Monitoring** -> **Retest after a material change**.

## Legal-source change workflow (future integration)
1. Obtain authorised change notice from official legislation channel or curated legal source.
2. Validate authenticity, jurisdiction, effective date, interpretation and completeness; preserve the publication URL and source hash.
3. Match affected AI systems and retrieval sources in the dependency inventory.
4. Generate and review test cases; run TEVV with both new and regression scenarios.
5. HOLD affected release paths if source or test evidence is incomplete; obtain approvals.
6. Publish approved content version with audit trail, then monitor and periodically retest.

**Important:** Email notifications, prompt instructions or a scraped web page alone are not an authoritative legal determination. The repository neither connects to MOHRE nor simulates a real UAE law change.
