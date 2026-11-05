# Oracle Fusion HCM | Functional workforce configuration workbench

**Extension of existing Project 13, not another project.**
**Fictional organisation, synthetic records; no live Oracle Fusion HCM tenant.**

## Business scenario
Two UAE legal employers need consistent worker structures across their business units, departments, jobs, grades, locations and positions. The purpose is to model actual Oracle HCM configuration dependencies, define role segregation and produce testable acceptance criteria.

## Configuration design in logical build order
| Order | Oracle HCM area | Proposed configuration decision | Owner & required evidence |
|---|---|---|---|
| 1 | Legal entities / legal employers | Confirm two fictitious legal employers and country context | HR + legal + Finance sign off |
| 2 | Business units / reference data sets | Associate each BU with its approved set | HRIS config owner, set assignment evidence |
| 3 | Departments and locations | Restrict which departments belong to a BU | HR operations, setup screenshot or approved export |
| 4 | Jobs and grades | Common or BU-specific job and grade catalogues | Talent & Reward owners |
| 5 | Positions | Valid job, grade, department, location, FTE, effective start | HR position owner and UAT |
| 6 | Change approvals | Maker and checker must be different, and authorised | Security & HR process owner |
| 7 | Date-effective lifecycle | Track transfers, corrections and exception ownership | HRIS data steward |

## Executable design model
- [Synthetic configuration fixture](configuration_lab/configuration_synthetic.json)
- [Python dependency / segregation validator](configuration_lab/validate_configuration.py)
- [Local unit tests](configuration_lab/test_configuration.py)
- [Nonproduction configuration acceptance plan](CONFIGURATION_ACCEPTANCE_AND_EVIDENCE.md)

From this project directory:

```bash
python configuration_lab/validate_configuration.py
python -m unittest discover -s configuration_lab -p "test_*.py" -v
```

This script validates **a fictional JSON representation** of the setup (legal employer, business unit, set access, position references, FTE, effective date and reviewer separation). It is not Oracle configuration code or a connection to a SaaS tenant.

## Next engineering step if a licensed tenant becomes available
1. Confirm enabled Oracle HCM modules, roles, release and enterprise-structure design with authorised technical owners.
2. Inspect setup tasks and configure scoped objects in **nonproduction**. Use the current Work Structures and Setup and Maintenance instructions.
3. Run negative and positive cases: invalid position BU, restricted reference set, retroactive transfer, missing legal employer and same-person approval.
4. Capture actual approved setup evidence, version, reviewer, execution timestamp and UAT results; only then update claims of hands-on experience.
5. Keep payroll calculation and privileged employment decisions under separate specialist controls.

## Oracle technical references
- [Workforce structures](https://docs.oracle.com/en/cloud/saas/human-resources/fawhr/overview-of-workforce-structures.html)
- [Common HCM features and enterprise structures](https://docs.oracle.com/en/cloud/saas/human-resources/faucf/overview-of-using-hcm-common-features.html)
- [Loading work structures and reference data sets](https://docs.oracle.com/en/cloud/saas/human-resources/fahbo/overview-of-loading-work-structures.html)

**Claim-safe:** "Designed and tested a synthetic Oracle HCM workforce configuration dependency model, with documented setup, governance and acceptance criteria." **Not supported:** "Configured Oracle Fusion HCM in a client tenant."
