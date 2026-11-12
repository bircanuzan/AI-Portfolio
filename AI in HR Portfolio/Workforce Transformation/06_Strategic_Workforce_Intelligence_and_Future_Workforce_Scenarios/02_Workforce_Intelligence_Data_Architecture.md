# Workforce intelligence platform and evidence design

## Conceptual enterprise architecture
1. **Business systems of record:** Workday, SAP SuccessFactors, Oracle Fusion HCM or a legacy HRIS *where licensed and approved*; staffing, learning and organization structures must be reconciled.
2. **Market data:** official MOHRE Labour Market Observatory / reputable market publications **via lawful, approved processes**, with documented definitions, currency, update date and usage rights. No current official dataset is included.
3. **Service demand:** privacy-minimized aggregate volumes from ticketing, customer service and finance systems.
4. **Data engineering:** role/skill IDs, effective dates, source-to-target mapping, data-quality checks, privacy-preserving aggregation and history/versioning.
5. **Semantic and analytics layer:** documented metric dictionary, scenario assumptions, Power BI/Tableau/Oracle Analytics conceptual dashboard.
6. **Decision support:** human-reviewed options, risk register, sensitivity, skills action and benefit ownership.

## KPI / data dictionary
| Metric | Definition | Owner | Guardrail |
|---|---|---|---|
| FTE demand | modeled human hours / modeled effective hours/FTE | Workforce planning | Never use alone for hiring |
| Supply FTE | workforce records after reconciliation | HRIS/Finance | Respect effective dates and contingent categories |
| Skill coverage | aggregate current proficiency relative to required threshold | Talent development | No automated selection or adverse employee decisions |
| AI-assisted share | proportion of eligible tasks *actually* aided successfully | Process owner | Needs real test evidence; synthetic here |
| Human review load | minutes reviewing automated work and errors | Operations | Never assume zero |
| Workforce quality | resolved cases meeting validated standard | Service owner | Detect disparate impact and customer harm |
| Forecast confidence | source reliability + range of scenario assumptions | Data owner | Must show unknowns |
| Labour market trend | source, geography, period, population and definition | Research lead | Do not merge incompatible datasets |

## Source trust and reconciliation checks
- Worker master must use a stable surrogate ID; secure PII is never put in public GitHub.
- Validate country, entity, currency, legal employment type, time zones, role taxonomy, occupation code and effective date.
- Deduplicate and reconcile HRIS headcount with payroll/Finance; flag actual vs planned vacancies separately.
- Record source permission, freshness, missingness, owner, transformations and assumptions.
- Split aggregate skills data from individually identifiable performance/assessment records.

## Scenario-to-decision API concept (not implemented)
Input: approved aggregate function ID, scenario ID, base demand, expected review minutes, capability evidence version. Output: baseline hours, modeled assisted hours, uncertainty, gap, data quality status, risks and *human decision required*. No action endpoint for hire/fire/pay decisions.

## Product options and caveats
**Product research references:** Oracle Fusion Cloud HCM, OCI Dedicated Region, Oracle Grow/Dynamic Skills, Workday, SAP SuccessFactors, Visier and Power BI. Vendor-specific features, APIs, licensing, data residency and security architecture must be validated directly before design commitments. No platform is connected in this demonstration.