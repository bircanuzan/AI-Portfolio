"""Project 11: auditable synthetic HR data quality & aggregate scorecard contract."""
import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"synthetic_hr_data.csv"
REQUIRED={
 "employee_id","department","location","level","tenure_years","performance_rating",
 "learning_hours","primary_skill","skill_level","internal_move_12m","exit_12m",
 "hire_source","time_to_fill_days"
}
MIN_GROUP=10

def audit(rows):
    if not rows:
        raise ValueError("Empty source")
    ids=set()
    for i,row in enumerate(rows,1):
        if set(row) != REQUIRED or any(row.get(c) is None or not str(row[c]).strip() for c in REQUIRED):
            raise ValueError(f"Row {i}: missing/extra/blank field")
        if row["employee_id"] in ids:
            raise ValueError(f"Row {i}: duplicate employee id")
        ids.add(row["employee_id"])
        if row["exit_12m"] not in ("0","1") or row["internal_move_12m"] not in ("0","1"):
            raise ValueError(f"Row {i}: bad binary flag")
        for name in ("skill_level","performance_rating"):
            try:
                val=float(row[name])
            except ValueError as exc:
                raise ValueError(f"Row {i}: bad {name}") from exc
            if not val.is_integer() or not 1 <= val <= 5:
                raise ValueError(f"Row {i}: {name} outside 1-5")
        for name in ("tenure_years","learning_hours","time_to_fill_days"):
            try:
                val=float(row[name])
            except ValueError as exc:
                raise ValueError(f"Row {i}: bad {name}") from exc
            if not (0 <= val < 100000):
                raise ValueError(f"Row {i}: invalid {name}")
    return len(ids)

def metrics(rows):
    count=audit(rows)
    dept=defaultdict(list)
    for row in rows:
        dept[row["department"]].append(row)
    exit_total=sum(r["exit_12m"]=="1" for r in rows)
    move_total=sum(r["internal_move_12m"]=="1" for r in rows)
    groups=[]
    for name,subset in sorted(dept.items()):
        if len(subset)<MIN_GROUP:continue
        n_exit=sum(r["exit_12m"]=="1" for r in subset)
        groups.append({"department":name,"records":len(subset),
                       "exit_flagged_count":n_exit,
                       "exit_flag_share_pct":round(100*n_exit/len(subset),1)})
    return {
      "provenance":{"classification":"SYNTHETIC","source_file":"11_Data_Analytics_for_AI_in_HR/synthetic_hr_data.csv",
         "source_rows":count,"source_grain":"one fictional employee row",
         "window":"synthetic exit_12m and move_12m flags; exact event dates unavailable",
         "schema_version":"1.0","minimum_group_size":MIN_GROUP},
      "kpis":{"workforce_record_count":count,"exit_flagged_count":exit_total,
         "exit_flag_share_pct":round(100*exit_total/count,1),
         "internal_move_flag_share_pct":round(100*move_total/count,1),
         "average_learning_hours":round(sum(float(r["learning_hours"]) for r in rows)/count,1)},
      "department_metrics":groups,
      "interpretation":"Synthetic snapshot metrics only. Exit-flag share is NOT a validated organization turnover rate or employee-level risk prediction. No cross-dataset joining with Project 54."
    }

def read_source(path):
    with Path(path).open(encoding="utf-8-sig",newline="") as f:
        reader=csv.DictReader(f)
        if set(reader.fieldnames or [])!=REQUIRED:
            raise ValueError("Schema mismatch")
        return list(reader)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv",default=str(SOURCE))
    parser.add_argument("--out",default="")
    a=parser.parse_args()
    result=metrics(read_source(a.csv))
    blob=json.dumps(result,indent=2,ensure_ascii=False)+"\n"
    if a.out:Path(a.out).write_text(blob,encoding="utf-8")
    print(blob,end="")

if __name__=="__main__":main()
