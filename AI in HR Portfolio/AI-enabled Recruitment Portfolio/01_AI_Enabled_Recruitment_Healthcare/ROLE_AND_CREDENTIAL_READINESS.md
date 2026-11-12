# Healthcare recruitment: jurisdiction, role and credential readiness controls

**This extends the original Project 01; original portfolio PDF is preserved.**

## Exclusive contribution
Project 01 owns **the business specification and assurance pathway for healthcare-role sourcing**. This is not a second candidate-screening system (Project 55) and not a recruiter capacity model (Project 07).

Each healthcare role brief must identify the hiring jurisdiction and location, business and clinical sponsor, validated task and skills profile, documented licensing authority *where applicable*, official source/version, relevant HR/clinical approvals and a safe route for missing evidence.

### Reproducible synthetic workbench
- [Invented UAE/KSA requisition briefs](data/synthetic_healthcare_role_briefs.json)
- [Source/approval completeness Python checker](src/role_readiness.py)
- [Local unit tests](tests/test_role_readiness.py)
- [Synthetic findings](evidence/role_readiness.json)

```bash
python src/role_readiness.py --out evidence/role_readiness.json
python -m unittest discover -s tests -v
```

**Stop rules:** Unsupported or outdated jurisdiction requirements cannot be filled in from assumptions; an unknown source or unsigned clinical approval keeps the role on **HOLD**. A report marked 'READY_FOR_FURTHER_HUMAN_VERIFICATION' still requires independent jurisdiction/licensing verification and **never authorizes recruitment or an individual's employment**.

Do not put real candidate records, licences, identity numbers, immigration details or patient data in this public repository. Healthcare authorities and licensing requirements require checking against actual up-to-date official sources before any real workflow.

[Linked recruitment operating model](../WORKFLOW_INTELLIGENCE_AND_RELEASE_MODEL.md)
