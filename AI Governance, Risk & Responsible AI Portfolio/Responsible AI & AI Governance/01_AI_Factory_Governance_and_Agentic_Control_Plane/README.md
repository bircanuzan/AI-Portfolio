# AI Factory Governance and Agentic Control Plane — Risk-to-Release Assurance

**HumanEvoX independent work sample. Fictional UAE multi-sector organization, synthetic data.**

## Executive problem
A diversified enterprise proposes an HR policy assistant, a recruitment evaluation support agent and a financial-services case copilot. The CEO and Chief AI Officer need risk acceptance and decision rights, a traceable AI system inventory, independent impact/assurance gates and technical controls before agents may be entrusted with work.

## End-to-end deliverables
1. [Governance charter and RACI](docs/01_GOVERNANCE_AND_DECISION_RIGHTS.md): executive oversight, policy, risk ownership and lifecycle release gates.
2. [AI system inventory](data/ai_inventory.json): three fictional AI systems with named role owners, data scope, AI assurance and allowed tools.
3. [Risk register](data/risk_register.csv) and [impact/assurance assessment](docs/02_IMPACT_AND_ASSURANCE.md): fairness, safety, explainability, privacy, model quality, hallucination, leakage and human oversight.
4. [Runnable policy-as-code agent control plane](src/control_plane.py): synthetic tool authorization, release readiness, budgets, information source controls, human approvals, exfiltration blocks and prompt-injection indicator.
5. [Synthetic agent action scenarios](data/scenarios.json), [unit tests](tests/test_controls.py) and an offline hash-chained audit.
6. [Executive evidence-pack generator](src/board_report.py) plus [board decision and CAPAs](docs/04_BOARD_BRIEF_AND_CAPA.md).
7. [ISO, NIST and UAE data protection applicability crosswalk](docs/03_STANDARDS_AND_LEGAL_SCREEN.md).
8. [90-day AI Factory, sovereign AI and regulated-sector delivery proposal](docs/05_AI_FACTORY_ROADMAP.md).

## JD coverage
- AI governance operating models and policies; AI use-case intake, model inventory and oversight committees.
- AI risk and assurance; fairness, explainability, human oversight, safety and audit support.
- GenAI and agentic risks: hallucinations, prompt injection, data leakage and unauthorized delegated action.
- Agentic control plane translated into programmatic rules with negative/adversarial tests.
- ISO/IEC 42001, ISO/IEC 23894 and NIST AI RMF conceptual alignment.
- Sovereign AI and regulated sector due diligence, AI Factory governance and leadership brief.

## Run
Python 3.11+, standard library only, no credentials:

    python -m unittest discover -s "Responsible AI & AI Governance/01_AI_Factory_Governance_and_Agentic_Control_Plane/tests" -v
    python "Responsible AI & AI Governance/01_AI_Factory_Governance_and_Agentic_Control_Plane/src/board_report.py"

**Evidence integrity:** The program is a deterministic OFFLINE policy simulator, not a live agent, regulated model evaluation, deployed security control or ISO audit. Approval booleans are synthetic fixtures, not authenticated enterprise identities. No outside tool requests are executed. All independent audit, privacy and fairness activities are plans until actual evidence is obtained.

**CV-safe:** Developed an independent synthetic Responsible AI governance engagement with an AI inventory, risk-to-release committee design, runnable agentic control-plane policy gates, negative tests and reproducible executive evidence.
