"""Offline service adapter with mock case records. NOT production authorization."""
import hashlib
import hmac
import json
ALLOWED={"policy_question","letter_request"}
class IntegrationError(ValueError): pass
class MockAdapter:
    def __init__(self):
        self.records={}
        self.counter=0
    def submit(self,payload,key):
        if not isinstance(payload,dict) or payload.get("confirmed") is not True:
            raise IntegrationError("explicit confirmation required")
        if payload.get("category") not in ALLOWED:
            raise IntegrationError("disallowed category")
        summary=payload.get("safe_summary")
        if not isinstance(summary,str) or not 1<=len(summary.strip())<=200:
            raise IntegrationError("invalid summary")
        if not isinstance(key,str) or not 8<=len(key)<=100:
            raise IntegrationError("invalid idempotency key")
        safe={"category":payload["category"],"safe_summary":summary.strip(),"confirmed":True}
        digest=hashlib.sha256(json.dumps(safe,sort_keys=True).encode()).hexdigest()
        if key in self.records:
            old_digest,old_result=self.records[key]
            if digest!=old_digest: raise IntegrationError("idempotency conflict")
            return dict(old_result)
        self.counter+=1
        result={"case_id":f"TKT-{self.counter:04d}","status":"created"}
        self.records[key]=(digest,result)
        return dict(result)
def signature(body,secret):
    return "sha256="+hmac.new(secret,body,hashlib.sha256).hexdigest()
def valid_webhook(body,header,secret):
    return isinstance(body,bytes) and isinstance(secret,bytes) and isinstance(header,str) and hmac.compare_digest(signature(body,secret),header)
if __name__=="__main__":
    adapter=MockAdapter()
    print(adapter.submit({"category":"policy_question","safe_summary":"Please clarify policy","confirmed":True},"synthetic-key-01"))
