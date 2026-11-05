# Solution alignment: SAP People Intelligence, Business Data Cloud, Datasphere, SAC and Report Stories

## Intended business-side architecture
Source of authorized HR data: SAP SuccessFactors and relevant licensed/approved third-party business data.
SAP Business Data Cloud: governed data products and relevant People Intelligence package capabilities, subject to entitlement and configuration.
SAP Datasphere: technical team's integration, semantic modeling and governed access layer.
SAP Analytics Cloud: story visualisation, exploration and planning aligned with approved metric definitions.
Stakeholders: HR Analytics, SuccessFactors architect, SAP Datasphere modeler, SAP Analytics Cloud consultant, security/privacy, finance and programme sponsor.

## SAP People Intelligence preconditions (technical team's checklist)
1. Confirm product entitlement and associated licensing.
2. Provision/configure Business Data Cloud in SAP for Me.
3. Verify active and configured Datasphere and SAP Analytics Cloud tenants.
4. Form the supported SuccessFactors + BDC + Datasphere + SAC landscape.
5. Install relevant insights and activate data packages.
6. Define consumer roles and maintain accurate data access control (DAC) permissions.
7. Validate source reconciliation, applicable data quality and business semantic definitions.
8. Establish approved story publishing/access rules and audit/rollback owners.

## Role-specific handoff
**Strategy consultant owns:** executive priorities, decisions, KPI glossary, expected benefits, business acceptance, adoption and future phase roadmap.
**SAP technical consultants own:** source connectors, permissions, data models, DAC, configuration, BDC entitlement, SAP Analytics Cloud story publication, reliability and support.
**HR data owners own:** source field validity, policy interpretation, employee identity/privacy and final business acceptance.

## Report Stories distinction
SuccessFactors People Analytics Story Reports are an operational reporting approach built on SAC capabilities; People Intelligence within BDC is a distinct product offering. Do not presume they are interchangeable, identical or configured in the same way. Assess current client landscape with the SAP specialists.

## UAT
Trace a KPI from authorised SuccessFactors fields to approved metric definition, reconciled sample, aggregation, role-restricted story, manager interpretation and human action. Negative tests: missing employee dimension, late exit, conflicting effective date, restricted compensation attribute, small team suppression, wrong period.

Official SAP references:
https://help.sap.com/docs/people-intelligence/people-intelligence/prerequisites-for-using-people-intelligence
https://help.sap.com/docs/business-data-cloud/viewing-intelligent-applications/people-intelligence-package-insights
https://help.sap.com/docs/portfolio-category/data-cloud

All diagrams/hand-offs are proposed only.
