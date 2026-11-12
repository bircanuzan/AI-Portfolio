# Project 21 — Senior AI Business Analyst | Retail Process Re-engineering & AI Automation

**Inspire Selection senior retail AI business analyst JD — original fictional retail transformation case study.** Simulated discovery and measurable business case, not a deployed retail system, certified Lean Six Sigma qualification or claimed four years of retail operations leadership.

## Fictional client
A 60-store UAE retailer faces inventory discrepancies, promotion-price mismatches between ecommerce and POS, slow returns and manual finance reconciliation.

## Complete role-aligned deliverables
1. [BPMN 2.0 process design](01_BPMN_SIPOC_Value_Stream.md), including readable BPMN XML in [process model](bpmn/retail_returns_as_is.bpmn).
2. [As-is discovery and performance baseline](02_Retail_Baseline_and_Lean_Diagnosis.md) across merchandising, supply chain, inventory, pricing, promotions, POS, fulfilment, returns, CRM and finance.
3. [To-be redesign and automation architecture](03_To_Be_AI_Automation_and_Requirements.md), user stories, functional/non-functional requirements, acceptance.
4. [ROI, prioritization, KPIs and executive governance](04_ROI_KPIs_Steering_Committee.md), including Lean/Six Sigma, VSM, SIPOC, RACI and measured-outcome plan.
5. [KPI and ROI Python calculator](src/retail_roi.py) and [unit tests](tests/test_retail_roi.py). Figures are **invented baseline assumptions** and not observed client performance.

### Actual business challenge
1. Retail pricing updates create ERP-to-POS and ecommerce inconsistency.
2. Customers return an item but CRM, stock and finance remain out of sync.
3. Head office overorders because on-hand inventory does not match scanned inventory.
4. Proposed orchestration validates transaction changes, waits for defined controls, and only then updates downstream systems; predictive AI is reserved for judgement cases with human approval.

### Leadership and controls
Executive sponsor: COO; operational owner: Retail Operations; process leads: Head of Merchandising, Supply Chain, Store Operations and Finance; technology leads: Enterprise Apps, POS, Security and Integration. Discovery, weekly workshops, steering committee, rollout approval, benefits owner, defects and risk register included.

### Practical integrity
This is a **consulting simulation**. It shows what artifacts a Senior AI Business Analyst creates; it does **not** substitute for verified retail domain experience, production automation deployments or CBAP / Six Sigma credentials.

Role link: https://ae.linkedin.com/jobs/view/senior-ai-business-analyst-at-inspire-selection-recruitment-agency-4480668874

## Expanded retail business analysis demonstration
- [Ten core retail domains and end-to-end system handoffs](05_Retail_Operating_Model_and_10_Process_Areas.md)
- [Ten UAT scenarios and failure/exception paths](06_End_to_End_Workflow_Test_Cases.md)
- [Runnable offline retail refund rule demonstration](src/return_decision.py) with [unit tests](tests/test_return_decision.py)

The additional Python demo is deterministic and synthetic, **not a retail-system deployment or proof of prior retail engineering employment**.
