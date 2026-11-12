"""Localhost-only HTTP API. Static test secret is NOT a production authentication design."""
import json
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlsplit
from app import db_open,get_case,run_case,human_review

DEMO_TOKEN="offline-example-key"

def create_server(dbfile,outbox):
    class Handler(BaseHTTPRequestHandler):
        def reply(self,code,payload):
            data=json.dumps(payload).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type","application/json")
            self.send_header("Content-Length",str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        def allowed(self):
            if self.headers.get("X-Demo-Token")!=DEMO_TOKEN:
                self.reply(401,{"error":"Unauthorized test request"})
                return False
            return True
        def do_GET(self):
            if not self.allowed():return
            path=urlsplit(self.path).path
            if not path.startswith("/case/"):return self.reply(404,{"error":"Unknown route"})
            try:
                with db_open(dbfile) as db:
                    case=get_case(db,path.split("/")[-1])
                return self.reply(200,{"case_id":case["case_id"],"status":case["status"]})
            except KeyError:return self.reply(404,{"error":"Unknown case"})
        def do_POST(self):
            if not self.allowed():return
            path=urlsplit(self.path).path
            if path not in ("/triage","/review"):return self.reply(404,{"error":"Unknown route"})
            try:
                n=int(self.headers.get("Content-Length","0"))
                if not 0<n<=2048:raise ValueError("Request size invalid")
                payload=json.loads(self.rfile.read(n))
                if not isinstance(payload,dict) or not isinstance(payload.get("case_id"),str):
                    raise ValueError("case_id required")
                with db_open(dbfile) as db:
                    if path=="/triage": output=run_case(db,payload["case_id"],outbox,llm=False)
                    else:output=human_review(db,payload["case_id"],payload.get("actor"),payload.get("decision"))
                return self.reply(200,output)
            except (ValueError,KeyError,TypeError) as e:
                return self.reply(400,{"error":str(e)})
        def log_message(self,*args):pass
    return ThreadingHTTPServer(("127.0.0.1",0),Handler)
