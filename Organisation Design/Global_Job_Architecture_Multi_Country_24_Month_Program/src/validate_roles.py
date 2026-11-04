"""Synthetic job architecture data quality rules. Not automated job evaluation."""
import csv
import json
import sys

FAMILY_TO_SUBFAMILIES = {
    "Ground Operations": {"Station Operations", "Ramp Services", "Cargo Handling"},
    "Customer Experience": {"Passenger Services", "Service Quality"},
    "Commercial": {"Account Management", "Sales Operations", "Customer Solutions"},
    "Technology & Data": {"Enterprise Systems", "Data Analytics", "Cybersecurity"},
    "Corporate Services": {"HR", "Finance", "Procurement", "Risk"},
}
LEVELS = {"IC1", "IC2", "IC3", "IC4", "IC5", "M1", "M2", "M3", "M4"}
REQUIRED = {"position_id","market","business_unit","current_title","job_family",
            "job_subfamily","track_level","global_job_code","local_grade","role_profile_version"}

def validate(rows):
    findings = []
    seen = set()
    positions = {r.get("position_id") for r in rows}
    for index, row in enumerate(rows, 2):
        pid = row.get("position_id", "")
        for field in sorted(REQUIRED):
            if not str(row.get(field, "")).strip():
                findings.append({"row":index,"position_id":pid,"code":"missing_required","field":field})
        if pid in seen:
            findings.append({"row":index,"position_id":pid,"code":"duplicate_position"})
        seen.add(pid)
        family, sub = row.get("job_family"), row.get("job_subfamily")
        if family not in FAMILY_TO_SUBFAMILIES or sub not in FAMILY_TO_SUBFAMILIES.get(family,set()):
            findings.append({"row":index,"position_id":pid,"code":"invalid_family_subfamily"})
        if row.get("track_level") not in LEVELS:
            findings.append({"row":index,"position_id":pid,"code":"invalid_track_level"})
        manager = (row.get("manager_position_id") or "").strip()
        if manager and manager not in positions:
            findings.append({"row":index,"position_id":pid,"code":"missing_manager_position"})
        if manager and manager == pid:
            findings.append({"row":index,"position_id":pid,"code":"self_reporting"})
        if not row.get("review_status"):
            findings.append({"row":index,"position_id":pid,"code":"unreviewed_mapping"})
    # A clean row still requires independent role-content and reward approval.
    return findings

if __name__=="__main__":
    path = sys.argv[1] if len(sys.argv)>1 else "data/synthetic_role_inventory.csv"
    with open(path,newline="",encoding="utf-8") as handle:
        rows=list(csv.DictReader(handle))
    issues=validate(rows)
    print(json.dumps({"total_rows":len(rows),"quality_issues":issues,"note":"QA is not job evaluation or grade approval"},indent=2))
    sys.exit(1 if issues else 0)
