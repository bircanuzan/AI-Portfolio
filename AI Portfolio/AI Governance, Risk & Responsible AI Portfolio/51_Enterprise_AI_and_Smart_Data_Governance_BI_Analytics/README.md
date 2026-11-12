# Project 51 — Enterprise AI & Smart Data | Governance, BI & Analytics

**Role alignment:** Senior Manager AI & Smart Data (Transguard Workforce Solutions / unnamed Abu Dhabi client, October 2026)  
**Project type:** AI-assisted, independently reproducible **portfolio demonstration + enterprise solution-design documents**, using fictional insurance data.  
**Business case:** Improve visibility into motor-insurance claim triage and define controlled AI/data/BI delivery for a hypothetical UAE insurer.

> **Evidence boundary:** This is not an implementation for Transguard, its client, any insurer, or Azure. No company data, live premiums/claims, production integrations, trained enterprise LLM, completed vendor certification, or financial returns are claimed. Python model performance on synthetic labels is only evidence that the local code runs; it is NOT evidence of genuine insurance model accuracy or business impact.

## Three linked workstreams

| Workstream | Status | Deliverables |
|---|---|---|
| [01 — Insurance claims analytics demonstration](01_Insurance_Claims_Analytics_Demonstration/) | **Runnable local demo**; synthetic data, actual execution evidence in /evidence | Deterministic data generator, data-quality gate, logistic regression baseline, held-out evaluation, human-routing output, Python tests, SQL & Power BI examples |
| [02 — Azure data platform and data fabric/mesh](02_Azure_Data_Platform_and_Data_Architecture/) | **Proposed reference design only**; not deployed | Azure Data Factory / Data Lake / Databricks / Synapse / Azure ML architecture, data contracts, master data, governance, real-time integration, responsible model lifecycle |
| [03 — AI/BI CoE, governance and investment case](03_AI_BI_Governance_CoE_and_Business_Case/) | **Proposed operating model and hypothetical value scenario** | AI/BI roadmap, CoE charter, business KPIs and ROI, insurance vendor assessment, Responsible AI policy, monitoring and RACI |

## Management problem, choices and safeguards

1. **Business problem:** manual claim-review work queues lack consistent triage visibility; leadership needs usable BI without creating unfair automated insurance decisions.
2. **Baseline:** define manual review volumes, queue delays, data-quality exceptions, customer complaints and employee effort; in this case baseline values are **hypotheses to measure**, not captured operational facts.
3. **Approach:** first improve data ownership and dashboard definitions; pilot human-reviewed routing suggestions on synthetic data; only consider real-world pilot after privacy, data provenance, security, independent validation and regulatory review.
4. **Human ownership:** the demonstration recommends a *review queue*, never approves/denies a claim, changes a premium, or makes a fraud accusation.
5. **Deployment gates:** documented data contracts; PII classification; model risk review; evidence of non-discrimination; monitoring; fallback; human override; procurement/DPIA; UAT; sign-off by insurer compliance, IT security and business owner.

## Technology coverage — precise evidence

**Actually demonstrated locally:** Python 3, pandas, scikit-learn logistic regression, stratified train/holdout split, ROC-AUC/precision/recall/Brier, CSV/JSON outputs, schema checks, Python unittest. See the execution record.

**Designs or illustrative examples only:** SQL/Power BI DAX, Azure Data Factory, ADLS Gen2, Azure Databricks, Azure Synapse, Azure SQL, Azure Machine Learning, Azure AI services, Microsoft Purview, Event Hubs, data mesh/fabric, MLOps, master-data management, CI/CD, vendor integration, production security.

**Not demonstrated here:** TensorFlow, PyTorch, XGBoost, LightGBM, Java/R, Docker/Kubernetes/Kubeflow, live LLM/NLP/NER/OCR, cloud training, operational real-time ETL, or insurer-specific regulatory approval. These are hiring-JD requirements but not credentials established by this project.

## How to reproduce the local demonstration

From the Project 51 folder:

1. Install dependencies: python -m pip install -r requirements.txt
2. Run: python 01_Insurance_Claims_Analytics_Demonstration/src/demo.py --output-dir local_run
3. Test: python -m unittest discover -s 01_Insurance_Claims_Analytics_Demonstration/tests -v
4. Compare local_run/summary.json with evidence/ (different package versions can change numeric results).

Outputs include a synthetic dataset, quality report, model evaluation, and a sample review queue. No personal data or actual insurance information is used.

## What I would do next in a real organization

| Stage | Leadership deliverable | Acceptance gate |
|---|---|---|
| 0–30 days | discovery, current-state data flow, risk/control mapping, KPI dictionary, stakeholders | approved use case, data access basis, accountable owners |
| 31–60 days | source contracts, data-quality checks, governed BI prototype, model baseline and challenger design | QA, validation, risk and security review |
| 61–90 days | time-bound human-reviewed pilot proposal, UAT, operating model, monitoring & financial assumptions | signed pilot decision; otherwise stop/rework |

**Authorship disclosure:** These artifacts were developed as an AI-assisted portfolio demonstration for Bircan Uzan and require independent employer/client validation before real-world use.
