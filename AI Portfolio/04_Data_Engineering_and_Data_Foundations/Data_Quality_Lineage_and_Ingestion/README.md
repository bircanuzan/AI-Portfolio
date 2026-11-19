# Data Quality, Lineage & Controlled Ingestion

**New independent demonstration | locally runnable | Python standard library only**

## Business problem
Downstream AI analytics becomes unreliable when event records are duplicated, incomplete, inconsistent or untraceable. This fictional, vendor-neutral lab demonstrates a governed data ingestion boundary for operational events.

## Implemented components
1. CSV input contract with exact schema, explicit timezone, permitted event types and nonnegative units.
2. Repeatable deduplication by event identifier, rejection reasons and clean/quarantine separation.
3. SHA-256 input-file fingerprint for a basic lineage record; ingestion row counts, rejection rate and validation summary.
4. Synthetic fixture, Python CLI and unit tests for accepted input, duplicates, invalid schema and invalid values.

## Run (from this project directory)
```bash
python src/pipeline.py --input data/synthetic_events.csv --output output
python -m unittest discover -s tests -v
```
Generated `output/` includes `clean_events.csv`, `quarantine.json` and `quality_report.json`.

## Production roadmap (NOT implemented)
A real deployment would add orchestration (e.g. Azure Data Factory), immutable landing zones, IAM, secrets management, event streaming, catalog/lineage systems, schema versioning, PII detection, incident alerts, checksums for each transform and agreed data stewardship. These are design recommendations, not claims of cloud usage.

**Evidence limit:** Local deterministic prototype, synthetic events only. No live enterprise sources, real personal data, Azure deployment, performance SLA or data-quality improvement is claimed.
