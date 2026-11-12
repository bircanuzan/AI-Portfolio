# Workforce data contract & trusted metrics

**Project 11 owns the data foundation.** Do not copy the scoring, data checks or denominator into dashboard code; the dashboard reads only the **explicitly embedded synthetic summary**.

## Source
The original `synthetic_hr_data.csv` contains 500 fictional employee records. The `exit_12m` and `internal_move_12m` columns are synthetic binary flags with no event dates. They **are not** monthly exits, historical employee-level prediction labels, or verified employer metrics.

## Enforced checks
- Exact required column names; every row must supply a synthetic unique employee ID, nonempty department and location.
- `exit_12m` and `internal_move_12m` strictly `0` or `1`.
- Valid 1–5 performance and skill rating, nonnegative tenure and learning hours.
- Reject missing values, duplicates and invalid numeric types; stop rather than quietly impute.
- Minimum department reporting n=10; do not expose small cohorts or raw rows to scorecard.
- Derived aggregates reconcile to total source records.
- Output includes synthetic provenance, metric label and limitations.

## Canonical metric dictionary
| Field | Exact definition | Caveat |
|---|---|---|
| workforce_record_count | Number of unique fictional employee rows | Not current payroll headcount |
| exit_flagged_count | Number with `exit_12m=1` | Not monthly departures |
| exit_flag_share_pct | 100 × flagged / source rows | Not a validated real-world turnover rate |
| internal_move_flag_share_pct | 100 × internal-move flag / source rows | Not a rate of approved internal transfers |
| average_learning_hours | Mean invented learning-hour field | No period alignment or verified LMS data |
| department_metrics | Same rate within source department, reported only for n≥10 | Suppression does not guarantee privacy in a real release |

**Excluded:** `time_to_fill_days` average is present in original prototype but is a fictional employee-row field, not a requisition-grain verified time-to-fill measure; it is not promoted to the CHRO release contract.

## Reproduce
```bash
python src/trusted_workforce_metrics.py --out evidence/trusted_workforce_metrics.json
python -m unittest discover -s tests -v
```
Uses Python standard library and existing original CSV; no new data sources or packages.

[See connected workflow](../WORKFORCE_INTELLIGENCE_PIPELINE.md). No production data quality or access-control certification is claimed.
