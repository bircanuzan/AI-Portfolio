# HRIS & HCM Systems

**Four complementary projects:** one cross-platform HRIS/HCM business analysis project, two vendor-specific solution architecture and engineering projects, and one reproducible integration simulator.

## Projects

1. **[01 — Cross-Platform HRIS/HCM Requirements, Integration, UAT & Data Integrity](01_Cross_Platform_HRIS_HCM_Requirements_Integration_UAT_Data_Integrity/)** — business requirements, master data quality, migration preparation, governance and UAT.
2. **[02 — Oracle Fusion Cloud HCM Solution Architecture & Engineering](02_Oracle_Fusion_HCM_Solution_Architecture_and_Engineering/)** — Oracle REST/HDL/Extract/Atom method choices, HCM-specific event interface design, security and technical handoff.
3. **[03 — SAP SuccessFactors Employee Central Solution Architecture & Engineering](03_SAP_SuccessFactors_Employee_Central_Architecture_and_Engineering/)** — SAP EC OData vs CompoundEmployee SOAP selection, data replication, effective dating, RBP and release assurance.
4. **[04 — HRIS/HCM Integration Solution Engineering Lab](04_HRIS_HCM_Integration_Solution_Engineering_Lab/)** — offline standard-library Python adapter for synthetic Oracle-/SAP-shaped events, validation, replay checks and tests.

## How the four differ
Business requirements (01) -> Oracle architecture (02) or SAP architecture (03) -> vendor-neutral offline engineering verification (04). These are complementary perspectives, not repeated project material.

## Adjacent categories retained without moving or duplicating work
- [Oracle Fusion HCM](../Oracle%20Fusion%20HCM/) — existing functional HCM programme and UAT portfolio, retained.
- [Oracle Solution Architecture](../Oracle%20Solution%20Architecture/) — existing HCM-to-ERP/Finance architecture and Python controls, retained.
- [People Analytics & HR Data](../People%20Analytics%20%26%20HR%20Data/) — people reporting, BI and SAP People Intelligence strategy.
- [HR Technology & Digital Transformation](../HR%20Technology%20%26%20Digital%20Transformation/) — strategy, software selection, employee experience and HRTech delivery.
- [HR Operations & Workflow Automation](../HR%20Operations%20%26%20Workflow%20Automation/) — process controls, payroll checks and HR service workflows.

**Evidence integrity:** The Oracle and SAP artifacts are fictional architecture designs. The shared Python code uses **custom synthetic fields**, not real vendor messages or connected services. No production implementation, vendor certification, client outcome, payroll handling or real employee data is claimed.

[Full portfolio](../README.md)