# AI Risk Management and Testing, Evaluation, Verification and Validation (TEVV)

**Portfolio Project 37 | Enterprise Responsible AI Governance and AI Assurance | Fictional, reproducible case study**  
**Prepared by:** Bircan Uzan | **Reference date:** 29 October 2026

> **Integrity notice:** This is a simulated HR-policy assurance environment. No MOHRE legislative change, regulatory notice, vendor AI product, production agent, client deployment, or certification is claimed. Dates, policies, test answers and model behaviour are invented for training and demonstration. No live LLM or MOHRE feed is connected.

## Executive problem
HR and employment-compliance AI tools may receive an updated policy notice while continuing to provide answers based on an obsolete version. A news alert or prompt update alone does not prove all affected AI responses have been retested, evidence-backed and approved.

**The challenge:** make policy changes *testable events*, connect each AI answer to an authoritative version, route exceptions to human owners, and preserve an audit trail of release decisions.

## What is delivered
1. Enterprise AI use-case intake and AI impact assessment
2. Model/source inventory, source-version register and change-trigger design
3. AI risk taxonomy, control register and governance decision rights
4. Synthetic TEVV test suite with source freshness, evidence completeness, answer correctness and prompt-injection case
5. Python standard-library evaluation script and unit tests
6. Exception log, human approval gate, rollback/escalation design
7. Illustrative **Agentic Control Plane** (architecture and guardrails; **not** deployed)
8. Repeatable scorecard, precomputed dashboard and vendor assurance question set
9. UK government and NIST source mappings and limitations

## Business scenario (entirely fictional)
- A fictional HR policy changes from **10 working days** to **5 working days** advance notice.
- A mock policy-answering AI still cites the previous version in one test.
- Another simulated response gives the right answer without evidence.
- An intentionally unsafe prompt is refused.
- Each response is graded against a **fictional approved source**; failing critical tests causes a **HOLD** decision.

**This is not a statement about UAE employment law.** The controlled internal-policy simulation avoids inventing MOHRE laws or implying an official update.

## Try the evidence dashboard
Run from the repository root:
```bash
python "AI Governance, Risk & Responsible AI Portfolio/37_AI_Risk_Management_and_Testing_Evaluation_Verification_and_Validation/src/assurance_dashboard.py"
python -m unittest discover -s "AI Governance, Risk & Responsible AI Portfolio/37_AI_Risk_Management_and_Testing_Evaluation_Verification_and_Validation/tests" -v
```
The script generates `reports/dashboard.md` relative to the project folder. **No external dependencies, API keys, candidate data or LLM API calls required.** See the checked-in illustrative dashboard [here](reports/dashboard.md).

## Tech, AI used and methodology
| Area | Actual implementation |
|---|---|
| Programming | Python 3 standard library (`csv`, `pathlib`, `datetime`, `unittest`) |
| Data | Synthetic CSV policy sources, AI-response fixtures, tests, inventory, risk and controls |
| Evaluation | Deterministic rules for current-source version, supporting evidence and expected answer |
| Dashboard | Generated Markdown scorecard and gate recommendation |
| AI tool/model used | **None invoked**; simulated responses stand in for future model output |
| Future integration concept | Authorised official-source ingestion, notifications, model endpoint, RAG retriever, ticket workflow and approval system; all **design-only** |
| Method | NIST AI RMF 1.0: GOVERN, MAP, MEASURE, MANAGE; scenario-based TEVV; UK 2026 AI Risk Management Toolkit |
| Adjacent standards | ISO/IEC 42001 and ISO/IEC 23894 are contextual references, **not a conformity assessment** |

## Governance principles
- Do not promote a model based solely on a vendor's assertion of fairness, transparency or accuracy.
- Separate **test coverage** from claims of overall validity or legal compliance.
- Define risk appetite and thresholds per use case; escalate missing evidence and stale sources.
- Independently check source provenance; an email alert is a *trigger*, not proof of policy correctness.
- Require specialist legal, privacy and security review for any real deployment.
- Re-evaluate whenever a source, prompt, model, retrieval index, agent tool or usage context changes.

## Work samples
- [Project brief and role-aligned delivery plan](docs/PROJECT_BRIEF.md)
- [Impact assessment and operating governance](docs/AI_IMPACT_ASSESSMENT.md)
- [Agentic control plane](docs/AGENTIC_CONTROL_PLANE.md)
- [Vendor assurance and measurable claims](docs/VENDOR_ASSURANCE.md)
- [UK publications and NIST crosswalk](docs/FRAMEWORK_MAPPING_AND_UK_SUMMARIES.md)
- [Risk register](data/risk_register.csv), [controls](data/control_register.csv), [policy sources](data/source_versions.csv), [test cases](data/test_cases.csv), [exceptions](data/exception_log.csv), [model inventory](data/model_inventory.csv)

## Limits
A small handcrafted dataset is useful for demonstrating governance workflow, **not** for inferring production accuracy, demographic fairness, causal bias, security resilience or compliance. The dashboard is a control demonstration only. Vendor fairness verification requires appropriate, lawfully obtained cohort data, context-sensitive definitions and independent review.

## Primary references
- [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
- [NIST AI RMF Playbook / MEASURE](https://airc.nist.gov/airmf-resources/playbook/measure/)
- [NIST Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [UK Trusted Third-Party AI Assurance Roadmap, 3 Sept 2025](https://www.gov.uk/government/publications/trusted-third-party-ai-assurance-roadmap/trusted-third-party-ai-assurance-roadmap)
- [UK AI Risk Management Toolkit, 8 Sept 2026](https://www.gov.uk/government/publications/ai-risk-management-toolkit/ai-risk-management-toolkit-guidance)

*This portfolio is an original illustrative implementation influenced by the cited public frameworks; it is not endorsed by NIST, the UK government, MOHRE or any AI vendor.*
