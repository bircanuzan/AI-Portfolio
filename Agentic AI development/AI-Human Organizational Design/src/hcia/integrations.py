"""Read-only HTTPS adapter contract for enterprise aggregate metric snapshots.

Not connected to a real HRIS/ATS/payroll platform in this portfolio.
Operator configures allowlisted HTTPS host and nonpersonal aggregate endpoint.
"""
import json
import os
from urllib.parse import urlparse
from urllib.request import Request,urlopen

SOURCES={"hris":"HRIS","ats":"ATS","payroll":"PAYROLL",
         "talent":"TALENT","workforce":"WORKFORCE"}
class IntegrationError(Exception):
    pass

def validate_snapshot(record):
    required={"schema_version","source_system","entity_id","period","aggregates"}
    if not isinstance(record,dict) or not required.issubset(record):
        raise IntegrationError("Unsupported aggregate snapshot schema")
    if not isinstance(record["aggregates"],dict):
        raise IntegrationError("Aggregates must be structured")
    forbidden={"employee_id","name","email","phone","national_id","date_of_birth",
               "bank_account","individual_salary","candidate_id"}
    if forbidden.intersection({key.lower() for key in record["aggregates"]}):
        raise IntegrationError("Individual personal data is prohibited in this adapter")
    for value in record["aggregates"].values():
        if isinstance(value,(list,dict)):
            raise IntegrationError("Only scalar aggregate metrics are accepted in the baseline contract")
    return record

def read_aggregate_snapshot(source,opener=urlopen):
    if source not in SOURCES:
        raise IntegrationError("Non-allowlisted source")
    prefix="HCIA_"+SOURCES[source]
    base=os.environ.get(prefix+"_URL","")
    token=os.environ.get(prefix+"_TOKEN","")
    allowlist={v.strip().lower() for v in os.environ.get("HCIA_INTEGRATION_HOST_ALLOWLIST","").split(",") if v.strip()}
    parsed=urlparse(base)
    if not (parsed.scheme=="https" and parsed.hostname and parsed.hostname.lower() in allowlist
            and not parsed.username and not parsed.password and token):
        raise IntegrationError("Operator-managed HTTPS integration is not configured")
    # Path is entirely configuration-controlled; user queries never supply URLs.
    req=Request(base,headers={"Authorization":"Bearer "+token,"Accept":"application/json"},
                method="GET")
    try:
        with opener(req,timeout=8) as response:
            data=json.loads(response.read(100000))
    except Exception as e:
        raise IntegrationError("Source unavailable; human exception review required") from e
    return validate_snapshot(data)
