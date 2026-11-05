"""Tiny REST service for a closed-loop engineering lab; bind to loopback only."""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from .storage import connect
from .agent import Agent, review_case

class Handler(BaseHTTPRequestHandler):
    db_path = "lab.sqlite3"
    def _send(self, code, data):
        body=json.dumps(data,ensure_ascii=False).encode()
        self.send_response(code);self.send_header("Content-Type","application/json; charset=utf-8")
        self.send_header("Cache-Control","no-store")
        self.send_header("Content-Length",str(len(body)));self.end_headers();self.wfile.write(body)
    def do_GET(self):
        if self.path=="/healthz": self._send(200,{"status":"ok","deployment":"local_only","model_connected":False})
        else: self._send(404,{"error":"not_found"})
    def do_POST(self):
        if self.path not in ("/ask","/review"):
            return self._send(404,{"error":"not_found"})
        n=self.headers.get("Content-Length")
        if not n or not n.isdigit() or int(n)>8192:
            return self._send(413,{"error":"invalid_body_size"})
        try:
            payload=json.loads(self.rfile.read(int(n)))
            if not isinstance(payload,dict): raise ValueError("object expected")
            with connect(self.db_path) as db:
                if self.path=="/ask":
                    res=Agent(db).ask(payload.get("query"),payload.get("mode","local"))
                else:
                    token=os.getenv("HR_AGENT_REVIEW_TOKEN","")
                    if len(token)<16 or self.headers.get("X-Review-Token")!=token:
                        return self._send(403,{"error":"review_credentials_required"})
                    res=review_case(db,payload["case_id"],payload["reviewer"],payload["decision"],payload["note"])
            self._send(200,res)
        except (KeyError,ValueError,TypeError,json.JSONDecodeError) as exc:
            self._send(400,{"error":"invalid_request","detail":str(exc)})
        except Exception:
            self._send(500,{"error":"internal_error"})

def serve(db_path,host="127.0.0.1",port=8000):
    if host!="127.0.0.1": raise ValueError("This lab server must bind to loopback. Use authenticated production gateway for remote access.")
    handler=type("BoundLabHandler",(Handler,),{"db_path":str(db_path)})
    server=ThreadingHTTPServer((host,port),handler)
    print(f"LOCAL ONLY http://{host}:{port} ; no external cloud integration",flush=True)
    try: server.serve_forever()
    finally: server.server_close()
