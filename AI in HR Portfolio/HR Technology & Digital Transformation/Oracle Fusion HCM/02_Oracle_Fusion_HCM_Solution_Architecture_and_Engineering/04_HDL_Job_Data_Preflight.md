# Oracle HCM Data Loader — Source-key Job.dat engineering lab

**Enhancement to the existing Oracle HCM Solution Architecture & Engineering project.**

This demonstrates specific Oracle integration-engineering preparation rather than repeating the vendor-neutral Python adapter in [HRIS & HCM Systems](../../HRIS%20%26%20HCM%20Systems/04_HRIS_HCM_Integration_Solution_Engineering_Lab/).

## Build sequence
1. Determine the scope: fictional job catalogue, not worker personal details or payroll.
2. Select **Job.dat**, use a documented `Job` discriminator and `METADATA` attributes, then `MERGE` job lines.
3. Identify each record with `SourceSystemOwner` plus `SourceSystemId` (source key).
4. Use the exact attribute definitions from **View Business Objects** for the tenant's Oracle release.
5. Confirm set code and `HRC_SOURCE_SYSTEM_OWNER` lookup in the actual target tenant.
6. ZIP the .dat at archive root, import to authorised nonproduction HDL environment, inspect actual import/load results and reconcile.
7. Submit only approved real execution evidence with redacted logs, results and business sign-off.

## Artifacts and checks
- [Illustrative Oracle-style Job.dat](hdl_job_preflight/Job.dat)
- [Offline format preflight validator](hdl_job_preflight/check_job_dat.py)
- [Unit tests](hdl_job_preflight/test_job_dat.py)

```bash
python hdl_job_preflight/check_job_dat.py
python -m unittest discover -s hdl_job_preflight -p "test_*.py" -v
```

The local parser verifies syntax, one METADATA definition, required synthetic keys, MERGE row widths, date shape and duplicate source keys. It **cannot** certify Oracle HDL object support, licences, access, import viability, vendor validations or application configuration.

**Source:** [Oracle METADATA instruction](https://docs.oracle.com/en/cloud/saas/human-resources/fahdl/the-metadata-instruction.html) and [Oracle HDL Job example](https://docs.oracle.com/en/cloud/saas/human-resources/fahdl/upload-data-using-hcm-data-loader.html?embed=1).

**Status:** Synthetic, not imported to Oracle.
