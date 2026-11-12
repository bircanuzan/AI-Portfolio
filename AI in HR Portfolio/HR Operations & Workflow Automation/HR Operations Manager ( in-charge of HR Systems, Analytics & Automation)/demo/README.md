# Synthetic HRMS-to-payroll control tower

Runs with Python 3.10+ standard library only and does not call any external system. Test fixtures contain fictional staff IDs and illustrative AED pay amounts, not confidential or real employee details.

```bash
python demo/hr_ops_control_tower.py
python -m unittest discover -s demo -p 'test_*.py' -v
```

**Implemented rules:** duplicate payroll rows, unknown employee, missing bank reference, unapproved batch, mismatch of net proposed amount vs HRMS basic+allowance+variable-deduction, exited-employee hold, EOS expert review and WPS applicability check. Outputs `demo/output/exception_register.csv` and `demo/output/summary.json`; these are local artifacts. No salary transfer, legal EOS calculations or AI-powered employment decisions.

**What is not implemented:** statutory wage deductions, contract/leave nuance, WPS bank file generation, salaries in kind, approval APIs, payroll vendor adapters, actual Power BI environment, independent UAE legal analysis. A clean demo result is not approval to pay.