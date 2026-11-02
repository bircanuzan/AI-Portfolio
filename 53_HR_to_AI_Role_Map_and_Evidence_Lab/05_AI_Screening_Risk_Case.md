# Case 2 — AI recruitment screening risk and control assessment

**Hypothetical challenge:** a UAE employer wants to use an AI shortlist assistant without disadvantaging qualified applicants through format errors, irrelevant proxies or unexplained automatic rejection.

**Scope:** 12 [fictional scenarios](data/screening_risk_cases.csv), e.g. career breaks, résumé parsing, name/nationality proxies, accessibility, invalid requirements, model-generated CV misstatements, role-criteria version control and appeal routes.

**Method:** risk register -> severity / existing status -> control owner -> remedial test -> independent review -> release approval. Severity is **illustrative qualitative prioritisation**, not calculated likelihood or proven discrimination.

**Suggested controls:** document essential requirements; strip or limit unjustified proxy features; approved accessible alternatives; role-relevant evidence; human review for rejection; auditable reason codes and appeals; vendor transparency; periodic drift checks; versioned criterion changes.

**Executable check:** [screening_risk_audit.py](scripts/screening_risk_audit.py) counts unresolved HIGH/CRITICAL cases and issues a proposed **HOLD** gate. This is a register validator **not an ATS audit or fairness-metric test**.

~~~bash
python scripts/screening_risk_audit.py
~~~

**Next evidence needed for real deployment:** tested vendor configurations, lawful collection/retention basis, representative and sufficiently sized consented assessment samples, group-level validation where lawful and appropriate, adverse-impact analysis with expert review, employer approval and documented remediation.

**Intended business output:** a decision-ready issue log and responsible AI control design. No actual applicant was screened, rejected, assessed, or compared.
