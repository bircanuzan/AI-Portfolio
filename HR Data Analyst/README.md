# HR Data Analyst
## Workforce MIS, Headcount Forecasting, Manpower Budget & Emiratisation Reporting Controls

**Author:** Bircan Uzan | HumanEvoX Talent Consultancy  
**Portfolio classification:** Independent, fictional UAE banking-sector HR data-analyst case study (November 2026).  
**Purpose:** Demonstrate a rigorous monthly workforce reporting and reconciliation workflow aligned to a published HR Data Analyst role.

> **Evidence boundary:** Not work delivered for Abu Dhabi Islamic Bank (ADIB), another bank, CBUAE or a government authority. All people records, budgets, division labels, staffing targets and outputs are fictional. There is no access to internal HRMS/finance systems, personal HR data, production dashboards, or confidential regulatory filings. Example Emiratisation targets are arbitrary teaching assumptions **not** legal or bank-specific requirements.

### Executive business question
How can HR produce reliable monthly headcount and cost MIS across divisions, forecast changes, support an annual manpower budget, and explain national workforce target variances without mixing up employees, FTE, funded positions, recruitment requests or expected exits?

### Workflow
1. **Cutoff & intake:** take a month-end, effective-dated HRMS employee snapshot, approved-position register and requisition list, with an explicit cutoff and immutable source references.
2. **Validate:** assert unique employee and position identifiers; check dates, division values, status codes, mandatory fields, cost/FTE ranges and join cardinality; quarantine exceptions.
3. **Reconcile:** distinguish active employees (persons), actual full-time equivalent (FTE), approved/funded position capacity, vacant funded FTE, pending requests and forecast hires.
4. **Partner with Finance:** compare authorized annualized people-cost budget to annualized active employee cost; build a traceable budget bridge and isolate unapproved requests.
5. **Emiratisation metrics:** calculate Emirati FTE share and illustrative division target gaps; route definitions and applicability to HR/Legal/Compliance for sign-off. Never infer legal compliance from this demonstration.
6. **Publish MIS:** produce division-level and group totals, definitions, reconciliations, data quality exceptions, management commentary and a versioned reporting pack; require dual approval before any regulator-facing release.
7. **Improve HRMS:** log defects, IT/data-owner remediation tickets and regression tests; freeze reviewed data snapshots.

### Repository artefacts
- [DATA_DICTIONARY.md](DATA_DICTIONARY.md) — records, dimensions, calculations, definitions, lineage and controls.
- [REPORTING_CONTROL_MATRIX.md](REPORTING_CONTROL_MATRIX.md) — RACI, monthly close steps, Finance, ITD and compliance approval controls.
- [EXCEL_POWERBI_SQL_SPEC.md](EXCEL_POWERBI_SQL_SPEC.md) — Excel formulas, DAX-style measures, SQL, sample MIS and exception patterns.
- [analysis.py](analysis.py) — offline Python standard-library calculations over de-identified fictional CSV inputs.
- [tests/test_analysis.py](tests/test_analysis.py) — validation and calculation regression tests.
- [data/employee_snapshot.csv](data/employee_snapshot.csv), [data/funded_positions.csv](data/funded_positions.csv), [data/requisitions.csv](data/requisitions.csv) — artificial inputs.
- [30_60_90_DAY_PLAN.md](30_60_90_DAY_PLAN.md) — implementation roadmap and reporting evidence gates.

### Run locally
```bash
python "HR Data Analyst/analysis.py"
python -m unittest discover -s "HR Data Analyst/tests" -p "test_*.py" -v
```
Python 3.10+, standard library only. Output is a JSON management summary, not a production regulatory submission.

### Decision definitions
| Metric | Formula / rule | Control |
|---|---|---|
| Actual HC | Count of distinct active worker IDs at cutoff | One employee once; documented inclusion policy |
| Actual FTE | Sum of active workers' contractual FTE | FTE can differ from headcount |
| Funded FTE | Approved budgeted position capacity | Exclude unapproved requisitions |
| Vacancy FTE | MAX(funded FTE - actual FTE, 0) | Review negative/overstaffed conditions separately |
| Cost variance AED | Annualized actual active cost - authorized annual budget | Reconcile with Finance accrual/payroll policy |
| Emirati share | Emirati active FTE / all active FTE | Illustrative only; legal denominators may differ |
| Target gap | CEILING(target% × denominator FTE - Emirati FTE) | Illustrative planning metric, not regulatory certification |
| Forecast FTE | Current FTE + funded/approved expected hires - forecast exits | Scenario, never booked actual |

### Responsible handling
Use fictional data only. Real implementation must use least-privilege HR/Finance access, encryption, restricted distribution, cell-level suppression where appropriate, retention controls, approved data classifications, audit trails and Legal/Compliance review of UAE and CBUAE-specific obligations.

**Related independent portfolio:** [HR Strategy & Planning](../HR%20Strategy%20%26%20Planning/README.md) | [People Analytics & HR Data](../People%20Analytics%20%26%20HR%20Data/) | [Executive Talent Dashboard](../Executive%20Talent%20Dashboard%20in%20Power%20BI%20and%20Board%20Presentation/)
