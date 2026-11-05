# Six Consulting Benchmark Specifications

Every task has a prompt and supporting fictional information in `data/benchmark_tasks.json`. A competent response makes assumptions explicit and does not fabricate unavailable sources or results.

## B01 — Steering committee narrative
**Task:** decide whether to fund a 90-day transformation discovery pilot. **Deliverable:** six slides: context/problem, evidence, options, economics, risks, ask/next gates.
**Checks:** explicit approve/defer/decline recommendation; stated pilot scope; owner; funding assumptions; measures; uncertainty; board-safe language.
**Defect injection:** slide 2 quotes one cost baseline and slide 5 quietly changes it.

## B02 — Market entry
**Task:** compare entering fictional Region East vs Region West using supplied table assumptions. **Deliverable:** market attractiveness matrix, 3 strategic options, recommendation and validation list.
**Checks:** use only supplied assumptions; segregate observations from estimates; weigh downside; alternatives; no fabricated citations.
**Defect injection:** an apparently precise market size lacks a sourced base year.

## B03 — Operating model
**Task:** redesign an end-to-end customer intake-to-resolution service process. **Deliverable:** as-is/to-be, roles/decision rights, RACI, exceptions and controls.
**Checks:** only one Accountable owner for each critical decision; approval gates; separation of automation and human sign-off.
**Defect injection:** two individuals are both accountable for exception approval.

## B04 — Business case with sensitivity
**Task:** evaluate a workflow productivity investment with an upfront cost and recurring cash flows; show three adoption scenarios and costs.
**Deliverable:** editable formula workbook with input cells; three-year cash-flow table; NPV; simple payback; sensitivity grid; assumption audit.
**Checks:** base math independently reproducible in `src/financial_model.py`; capex negative at t0; end-of-year discounting; payback based on undiscounted annual net; benefits respond to adoption and costs to cost multiplier.
**Defect injection:** an Excel formula applies undiscounted benefits to NPV; numerical model must reject this.

## B05 — Interview synthesis
**Task:** synthesize five fictional stakeholder interviews.
**Deliverable:** issue tree, theme counts, attributed paraphrases (not invented quotes), agreement/dissent, hypothesis backlog.
**Checks:** identify conflicting evidence, sample limitations and needs for data validation; never present synthetic voices as real.
**Defect injection:** four interviews mention handoffs but one interview rejects the assumed root cause.

## B06 — Implementation and change
**Task:** prepare first 90 days for a controlled redesign pilot.
**Deliverable:** milestones/dependencies, RACI, stakeholder map, adoption measures, RAID, communications and stop/go criteria.
**Checks:** each milestone has an owner and acceptance gate; measures have baselines and collection method; safeguards and escalation.
**Defect injection:** a benefit KPI is declared successful before baseline measurement.

## Review artifacts
Record task ID, output version, rubric scores, issue severity, evidence pointer, reviewer judgment, fix owner, corrected outcome and final approval.

