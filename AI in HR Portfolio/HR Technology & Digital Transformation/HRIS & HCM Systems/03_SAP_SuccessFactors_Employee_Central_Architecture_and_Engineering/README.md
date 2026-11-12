# SAP SuccessFactors Employee Central — Solution Architecture & Engineering

**HumanEvoX independent solution design | Fictional cross-border enterprise | SAP Employee Central emphasis**

## Challenge
Design a defensible Employee Central data-replication interface for workforce changes, appropriate for separate HR service and downstream applications. Preserve event history, controlled replication, least-privilege permissions, effective-dated semantics, and incident resolution.

## Work samples
1. [SAP Employee Central interface architecture and API selection](01_EC_Architecture_and_API_Selection.md)
2. [Data replication, mapping and exception controls](02_Replication_Data_Mapping_and_Controls.md)
3. [Role-based permissions, tests and operational delivery](03_Security_UAT_and_Release.md)
4. [Synthetic cross-platform integration adapter](../04_HRIS_HCM_Integration_Solution_Engineering_Lab/README.md)

## Key platform distinction
SAP's official integration comparison distinguishes **OData APIs**, suitable for Employee Central entity access and suitable write scenarios, from the **CompoundEmployee SOAP API**, primarily intended for employee master-data replication, including full, delta and snapshot modes. These two interfaces are not interchangeable.

- [SAP: When are Employee Central OData APIs used?](https://help.sap.com/docs/successfactors-platform/sap-successfactors-api-reference-guide-odata-v2/when-are-employee-central-odata-apis-used)
- [SAP: CompoundEmployee API overview](https://help.sap.com/docs/successfactors-employee-central/employee-central-compound-employee-api/introduction-to-compoundemployee-api)
- [SAP: API permissions](https://help.sap.com/docs/successfactors-employee-central/employee-central-compound-employee-api/granting-permissions-for-full-access-to-compoundemployee-api)

## Difference from existing projects
[Project 23 SAP People Intelligence / Business Data Cloud](../../../People%20Analytics%20%26%20HR%20Data/23_Strategy_Consultant_SAP_People_Intelligence_Business_Data_Cloud_AI_Driven_People_Analytics/) focuses on strategic people analytics. This case focuses on **Employee Central transaction and master-data integration architecture**, not People Intelligence dashboards.

**Evidence boundary:** No SuccessFactors tenant, SAP Integration Suite account, Cloud Integration flow, real replication, paid licence or SAP certification is claimed.
