"""Functional + regression + API/integration tests for the local synthetic API."""
from __future__ import annotations
import json
from pathlib import Path
import sys
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from http.server import ThreadingHTTPServer

sys.path.insert(0,str(Path(__file__).resolve().parent))
from service import Handler, CaseStore

class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.local_handler=type("IsolatedHandler",(Handler,),{"store":CaseStore()})
        cls.server=ThreadingHTTPServer(("127.0.0.1",0),cls.local_handler)
        cls.thread=threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base=f"http://127.0.0.1:{cls.server.server_address[1]}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)

    def request(self,path,method="GET",body=None,key=None,malformed=False):
        data = None if body is None else (
            b"this is not json" if malformed else json.dumps(body).encode("utf-8"))
        headers={"Content-Type":"application/json"}
        if key is not None:
            headers["Idempotency-Key"]=key
        request=Request(self.base+path,data=data,headers=headers,method=method)
        try:
            with urlopen(request, timeout=5) as r:
                return r.status,json.load(r)
        except HTTPError as e:
            return e.code,json.loads(e.read().decode("utf-8"))

    def payload(self):
        return {"category":"policy_question","safe_summary":"Synthetic HR clarification","confirmed":True}

    def test_01_health(self):
        status,body=self.request("/health")
        self.assertEqual((status,body["status"]),(200,"ok"))

    def test_02_create_and_get(self):
        status,body=self.request("/cases","POST",self.payload(),"unique-0002")
        self.assertEqual(status,201)
        self.assertTrue(body["case_id"].startswith("TKT-"))
        get_status, case=self.request("/cases/"+body["case_id"])
        self.assertEqual(get_status,200)
        self.assertEqual(case["case_id"],body["case_id"])

    def test_03_unconfirmed_rejected(self):
        status,_=self.request("/cases","POST",{**self.payload(),"confirmed":False},"unique-0003")
        self.assertEqual(status,400)

    def test_04_category_allowlist(self):
        status,_=self.request("/cases","POST",{**self.payload(),"category":"payroll_write"},"unique-0004")
        self.assertEqual(status,400)

    def test_05_idempotent_retry(self):
        first,r1=self.request("/cases","POST",self.payload(),"unique-0005")
        second,r2=self.request("/cases","POST",self.payload(),"unique-0005")
        self.assertEqual((first,second),(201,200))
        self.assertEqual(r1,r2)

    def test_06_conflicting_replay(self):
        self.request("/cases","POST",self.payload(),"unique-0006")
        status,_=self.request("/cases","POST",{**self.payload(),"safe_summary":"Changed"},"unique-0006")
        self.assertEqual(status,409)

    def test_07_missing(self):
        status,_=self.request("/cases/TKT-MISSING")
        self.assertEqual(status,404)

    def test_08_malformed_json(self):
        status,_=self.request("/cases","POST",self.payload(),"unique-0008",malformed=True)
        self.assertEqual(status,400)

if __name__=="__main__":unittest.main()
