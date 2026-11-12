import pathlib,tempfile,unittest,json,threading
from urllib.request import Request,urlopen
from urllib.error import HTTPError
from app import db_open,seed,get_case,run_case,human_review,audit_count
from server import create_server,DEMO_TOKEN

class LabTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        p=pathlib.Path(self.tmp.name)
        self.dbfile=p/"cases.sqlite";self.outbox=p/"outbox"
        with db_open(self.dbfile) as db:self.assertEqual(seed(db),3)
    def test_sqlite_and_csv_integration(self):
        with db_open(self.dbfile) as db:
            self.assertEqual(get_case(db,"SYN1001")["status"],"NEW")
            self.assertEqual(db.execute("select count(*) from cases").fetchone()[0],3)
    def test_missing_document_email_draft_and_audit(self):
        with db_open(self.dbfile) as db:
            result=run_case(db,"SYN1001",self.outbox)
            self.assertEqual(result["missing"],["Address Proof"])
            self.assertEqual(result["status"],"PENDING_REVIEW")
            self.assertEqual(audit_count(db,"SYN1001"),1)
            self.assertFalse(result["email_sent"])
            self.assertFalse(result["llm_executed"])
        self.assertIn(b"Address Proof",(self.outbox/"SYN1001.eml").read_bytes())
    def test_expired_policy_escalates(self):
        with db_open(self.dbfile) as db:
            result=run_case(db,"SYN1003",self.outbox)
            self.assertEqual(result["status"],"HUMAN_ESCALATION")
            self.assertIsNone(result["email_draft"])
    def test_completed_doc_check(self):
        with db_open(self.dbfile) as db:
            result=run_case(db,"SYN1002",self.outbox)
            self.assertEqual(result["status"],"MANUAL_COMPLETENESS_CHECK")
            self.assertEqual(result["missing"],[])
    def test_human_approval_required_without_send(self):
        with db_open(self.dbfile) as db:
            run_case(db,"SYN1001",self.outbox)
            with self.assertRaises(ValueError):human_review(db,"SYN1001",None,"approve")
            result=human_review(db,"SYN1001","Human Reviewer","approve")
            self.assertEqual(result["status"],"APPROVED_DRAFT_FOR_MANUAL_USE")
            self.assertFalse(result["email_sent"])
            self.assertEqual(audit_count(db,"SYN1001"),2)
    def test_http_request_auth_integration(self):
        server=create_server(self.dbfile,self.outbox)
        thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
        root="http://127.0.0.1:"+str(server.server_port)
        def http(route,payload=None,auth=True):
            body=json.dumps(payload).encode() if payload else None
            headers={"Content-Type":"application/json"}
            if auth: headers["X-Demo-Token"]=DEMO_TOKEN
            with urlopen(Request(root+route,data=body,headers=headers,
                      method="POST" if body else "GET"),timeout=3) as resp:return json.load(resp)
        try:
            with self.assertRaises(HTTPError) as err:http("/case/SYN1001",auth=False)
            self.assertEqual(err.exception.code,401)
            self.assertEqual(http("/case/SYN1001")["status"],"NEW")
            status=http("/triage",{"case_id":"SYN1001"})
            self.assertEqual(status["status"],"PENDING_REVIEW")
            review=http("/review",{"case_id":"SYN1001","actor":"Reviewer","decision":"approve"})
            self.assertEqual(review["status"],"APPROVED_DRAFT_FOR_MANUAL_USE")
            self.assertTrue((self.outbox/"SYN1001.eml").exists())
        finally:
            server.shutdown();server.server_close();thread.join(timeout=2)
if __name__=="__main__":unittest.main()
