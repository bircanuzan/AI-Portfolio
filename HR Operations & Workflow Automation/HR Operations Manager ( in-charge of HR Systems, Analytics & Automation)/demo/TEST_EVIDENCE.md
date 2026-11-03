# Local synthetic test evidence — 3 November 2026

**Evidence type:** offline Python 3 standard-library execution against synthetic four-employee HRMS and four-row payroll fixtures; local reproduction of the GitHub source and fixtures. Not a company HRMS, payroll system or regulatory certification.

Command:
```bash
python -m unittest discover -s demo -p 'test_*.py' -v
python demo/hr_ops_control_tower.py
```

Result after duplicate-master blocking fix: **6 tests passed**.

Tests covered: (1) expected pay/review exceptions, (2) clean case still requiring human approval, (3) duplicate payroll row detection, (4) duplicate employee master blocking, (5) unknown employee, (6) malformed amount input.

Synthetic fixture report:
- 4 employee-master rows and 4 payroll rows
- 6 control flags: amount variance (1), approval pending (1), exited employee (1), EOS review pending (1), missing payment reference (1), WPS applicability review (1)
- Recommended release gate: `HOLD_FOR_REVIEW`

The script does **not** calculate EOS entitlements or perform payments. A result with zero flags is `HUMAN_REVIEW_REQUIRED`, not a payment release. See the test module to reproduce.