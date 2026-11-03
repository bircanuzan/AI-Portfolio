"""Offline synthetic Job.dat structure checker. NOT actual Oracle HDL import/validation."""
from datetime import datetime
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
REQ=("SourceSystemOwner","SourceSystemId","EffectiveStartDate","SetCode","JobCode","Name")
def check(text):
    errors=[];layout=None;keys=set();count=0
    for index,raw in enumerate(text.splitlines(),1):
        if not raw.strip():continue
        parts=raw.strip().split("|")
        if len(parts)<3:errors.append(f"L{index}:SHORT_LINE");continue
        command,object_type=parts[:2]
        if object_type!="Job":errors.append(f"L{index}:NOT_JOB");continue
        if command=="METADATA":
            if layout is not None:errors.append(f"L{index}:DUPLICATE_METADATA")
            else:
                layout=parts[2:]
                if not set(REQ).issubset(layout):errors.append(f"L{index}:MISSING_FIELDS")
                if len(layout)!=len(set(layout)):errors.append(f"L{index}:REPEAT_FIELD")
        elif command=="MERGE":
            if layout is None:errors.append(f"L{index}:METADATA_FIRST");continue
            if len(parts)-2!=len(layout):errors.append(f"L{index}:FIELD_COUNT");continue
            row=dict(zip(layout,parts[2:]))
            if any(not row.get(k) for k in REQ):errors.append(f"L{index}:BLANK_REQUIRED");continue
            try:datetime.strptime(row["EffectiveStartDate"],"%Y/%m/%d")
            except ValueError:errors.append(f"L{index}:INVALID_DATE")
            key=(row["SourceSystemOwner"],row["SourceSystemId"])
            if key in keys:errors.append(f"L{index}:DUPLICATE_SOURCE_KEY")
            keys.add(key);count+=1
        else:errors.append(f"L{index}:UNSUPPORTED_INSTRUCTION")
    if layout is None:errors.append("NO_METADATA")
    if not count:errors.append("NO_MERGE")
    return {"structure_pass":not errors,"checked":count,"errors":errors,"oracle_import_performed":False}
if __name__=="__main__":
    print(json.dumps(check((HERE/"Job.dat").read_text(encoding="utf-8")),indent=2))
