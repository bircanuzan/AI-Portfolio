"""End-to-end CSV -> SQLite -> HTTP API -> EML draft -> human approval proof."""
import json, pathlib, tempfile, threading
from urllib.request import Request,urlopen
from app import db_open,seed,audit_count
from server import create_server,DEMO_TOKEN

def http(url,payload=None):
    data=json.dumps(payload).encode() if payload else None
    req=Request(url,data=data,headers={"X-Demo-Token":DEMO_TOKEN,
                  "Content-Type":"application/json"},method="POST" if data else "GET")
    with urlopen(req,timeout=3) as result:return json.load(result)

def main():
    with tempfile.TemporaryDirectory(prefix="humanevox_system_integration_") as folder:
        dbfile=pathlib.Path(folder)/"cases.sqlite"
        outbox=pathlib.Path(folder)/"outbox"
        with db_open(dbfile) as db:count=seed(db)
        server=create_server(dbfile,outbox)
        worker=threading.Thread(target=server.serve_forever,daemon=True);worker.start()
        try:
            url="http://127.0.0.1:"+str(server.server_port)
            before=http(url+"/case/SYN1001")
            after=http(url+"/triage",{"case_id":"SYN1001"})
            reviewed=http(url+"/review",{"case_id":"SYN1001",
                                      "actor":"Test Human Reviewer","decision":"approve"})
            with db_open(dbfile) as db:events=audit_count(db,"SYN1001")
            assert (outbox/"SYN1001.eml").exists()
            assert reviewed["email_sent"] is False
            print(json.dumps({"imported_cases":count,"before":before,"triage":after,
                  "approval":reviewed,"audit_events":events,"actual_integrations":
                  ["CSV","SQLite","localhost HTTP JSON API","EML email draft"],
                  "external_llm_executed":False,"outbound_email_sent":False,
                  "production_deployed":False},indent=2))
        finally:
            server.shutdown();server.server_close();worker.join(timeout=2)
if __name__=="__main__":main()
