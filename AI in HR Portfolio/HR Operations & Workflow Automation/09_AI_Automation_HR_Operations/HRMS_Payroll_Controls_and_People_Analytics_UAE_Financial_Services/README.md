# HRMS, Payroll Controls & People Analytics — UAE Financial Services

**Independent HumanEvoX portfolio case | 2 November 2026 | HR Operations / Systems / Analytics / Automation**

> **Evidence classification:** synthetic HRMS records, an offline Python control-check prototype, passing local unit tests, business-side implementation and reporting designs. **Not** a client project, production HRMS or payroll integration, payroll certification, or legal verification of UAE statutory entitlements.

## Business problem

A hypothetical UAE-regulated financial-services employer has fragmented employee master data, manual approvals and limited payroll exception visibility. HR Operations needs a controlled handoff from HRMS to payroll, dashboards for leadership, consistent service delivery and opportunities to automate low-risk steps.

## What this project demonstrates

1. **HRMS ownership operating model:** employee lifecycle data owners, field standards, access controls, change logs, critical interfaces and HR-to-payroll handoff.
2. **Pre-payroll assurance:** a runnable offline script that flags duplicated employee IDs, missing payment references, mismatched gross pay, unapproved payments and exited employees requiring EOS expert review.
3. **Power BI-ready reporting:** KPI definitions, proposed data model and example DAX measures in [DASHBOARD_AND_UAT.md](DASHBOARD_AND_UAT.md).
4. **Digital employee experience:** self-service intake, case-tracking, SLA alerts, approval routing, human decisions and segregation of duties in [PROCESS_AND_CONTROLS.md](PROCESS_AND_CONTROLS.md).
5. **Responsible automation:** deterministic validation and human escalation rather than letting AI approve pay or interpret labour law.

## Methods / tools

- Current-state interviews, employee lifecycle SIPOC, AS-IS/TO-BE mapping, functional requirements and RACI.
- HRMS / ATS business-side workflows; Power BI, Excel / Power Query, Power Automate concept design, Python stdlib, CSV, unittest.
- Risk-control mapping, audit evidence, management sign-off, UAT, data-quality exception reporting and adoption metrics.
- Financial-services focus: least-privilege access, separation of duties, change traceability and controlled financial data.

## Reproduce the tested prototype

Requires Python 3.10+; no packages, API keys or network.

\`\`\`bash
cd HRMS_Payroll_Controls_and_People_Analytics_UAE_Financial_Services
python audit.py
python -m unittest -v test_audit.py
\`\`\`

**Local verification (2 November 2026):** 3 / 3 unit tests passed on seven deliberately flawed synthetic rows representing six employee IDs. Six control flags were produced: duplicated employee ID (2), gross variance (1), missing payment reference (1), payment without authorisation (1), EOS review outstanding (1). Reproduce the detailed output using audit.py; see [TEST_EVIDENCE.md](TEST_EVIDENCE.md).

This is a **pre-release exception flagger**, not a payroll engine. The script does not calculate payroll, WPS, tax, leave or UAE EOS entitlements. Every flagged condition requires the appropriate authorised HR, finance and/or legal reviewer. No real employee or salary information was used.

## Employer relevance

Aligned to HR Operations Manager responsibilities involving HRMS improvement, employee lifecycle process controls, payroll data integrity and EOS review routing, Power BI reporting, employee self-service, automation and regulated-environment governance. This portfolio demonstrates **solution thinking and runnable synthetic controls**, not past payroll-run leadership.

## Adjacent portfolio

- [Project 09 — broader HR Operations automation](../README.md)
- [Project 41 — HR workflow mapping and Power Automate approval design](../../41_HR_Operations_Process_Mapping_Workflow_Automation_Power_Automate/README.md)
- [Project 03 — people analytics](../../../People%20Analytics%20%26%20HR%20Data/03_People_Analytics_AI/README.md)

© 2026 Bircan Uzan — Independent educational demonstration.