# Oracle Fusion Cloud HCM — Solution Architecture & Engineering

**HumanEvoX independent HCM solution-design case | Fictional UAE multi-entity employer | November 2026**

## The challenge
Define how an approved worker change in Oracle Fusion Cloud HCM is validated, transformed and passed to an HR service consumer with minimal exposure of personal data, auditability, retries, and named business ownership. The focus is on HCM-specific **integration architecture and engineering handoff**, not payroll calculations or Core HR configuration.

## Practical vendor-specific file preparation
- [Oracle HCM Data Loader Job.dat preparation and preflight](04_HDL_Job_Data_Preflight.md): fictional `Job.dat`, local parser and unit tests. No Oracle tenant or import attempted.

## Architecture and work samples
- [Oracle HCM interface choices and solution architecture](01_Architecture_and_Interface_Selection.md): conceptual HCM REST, HCM Data Loader, HCM Extracts, Atom feeds and optional OIC.
- [Contract, mapping and solution-engineering runbook](02_Integration_Contract_and_Engineering.md): canonical event mapping, data quality and replay specification.
- [Security, UAT, go-live and hypercare](03_Assurance_UAT_and_Hypercare.md): approval, least privilege and operational acceptance.
- [Shared runnable cross-platform adapter and tests](../../HRIS%20%26%20HCM%20Systems/04_HRIS_HCM_Integration_Solution_Engineering_Lab/README.md): synthetic Python checks for Oracle/SAP-shaped inputs.

## Vendor-specific decision points
For Oracle Fusion HCM, [Oracle Workers REST documentation](https://docs.oracle.com/en/cloud/saas/human-resources/farws/api-workers.html) advises using **HCM Data Loader for bulk load**, **HCM Extracts for bulk export**, and **Atom feeds for change detection**, not polling Workers REST for changes. Supported resources and privileges must be verified against the licensed release and tenant.

## Distinction from existing GitHub work
- [Oracle Solution Architecture](../Oracle%20Solution%20Architecture/) already models Oracle HCM-to-ERP/Finance solution architecture for six subsidiaries.
- [Oracle Fusion HCM](../13_Oracle_Fusion_HCM/) already covers functional programme governance, UAT and release readiness.
- **This project** supplies the HCM interface-method decision, engineer-ready handoff, data contract and operational controls.

**Evidence boundary:** No Oracle HCM tenant, credentials, OIC environment, actual data-load execution, production integration, vendor certification or customer assignment is claimed. All examples are independent fictional designs.
