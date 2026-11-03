"""Authenticated read-only FastAPI sample. Not an enterprise identity boundary."""
import time
from fastapi import FastAPI,Header,HTTPException
from pydantic import BaseModel,ConfigDict,Field
from typing import Literal
from .engine import load_data,execute
from .security import Authorizer,Unauthorized,Forbidden
from .audit import AuditLedger
from .llm import summarize,ProviderUnavailable
from .planner import orchestrate,PlanError

class Job(BaseModel):
    model_config=ConfigDict(extra="forbid")
    capability:Literal["talent_acquisition","employer_brand","human_capital_operations",
                       "talent_management","total_rewards","workforce_intelligence","executive_brief"]
    entity:Literal["CORP","INV","INF","ALL"]
    llm_summary:bool=False

class GoalJob(BaseModel):
    model_config=ConfigDict(extra="forbid")
    goal:str=Field(min_length=3,max_length=300)
    entity:Literal["CORP","INV","INF","ALL"]
    use_model_planner:bool=False

def create_app(auth=None,audit=None,data=None):
    app=FastAPI(title="Human Capital Intelligence Agent — synthetic prototype",
                version="0.1.0",docs_url=None,redoc_url=None,openapi_url=None)
    authorizer=auth if auth is not None else Authorizer()
    dataset=data if data is not None else load_data()

    @app.get("/health")
    def health():
        return {"status":"prototype","synthetic":True,"production_deployed":False}

    @app.post("/v1/agent/run")
    def run(job:Job,authorization:str|None=Header(default=None)):
        started=time.perf_counter()
        try:
            actor=authorizer.authorize(authorization,job.capability,job.entity)
        except Unauthorized:
            raise HTTPException(status_code=401,detail="Authentication required")
        except Forbidden:
            raise HTTPException(status_code=403,detail="Insufficient permissions")
        if audit is None:
            raise HTTPException(status_code=503,detail="No audit control configured")
        try:
            answer=execute(dataset,job.capability,job.entity)
            if job.llm_summary:
                try:
                    answer["narrative"]=summarize(answer)
                except ProviderUnavailable:
                    answer["narrative"]={"mode":"unavailable","instruction":"Manual review of metrics required"}
            else:
                answer["narrative"]={"mode":"not_requested"}
            event=audit.append(actor,job.entity,job.capability,"SUCCESS",
                               (time.perf_counter()-started)*1000)
        except Exception:
            raise HTTPException(status_code=503,detail="Agent processing or audit failed")
        answer.update(event_id=event,agent_version="0.1.0",deployment_status="LOCAL_PROTOTYPE")
        return answer

    @app.post("/v1/agent/orchestrate")
    def orchestrate_request(job:GoalJob,authorization:str|None=Header(default=None)):
        started=time.perf_counter()
        try:
            # Only a scoped people_leader may execute a cross-domain plan.
            actor=authorizer.authorize(authorization,"executive_brief",job.entity)
        except Unauthorized:
            raise HTTPException(status_code=401,detail="Authentication required")
        except Forbidden:
            raise HTTPException(status_code=403,detail="Insufficient permissions")
        if audit is None:
            raise HTTPException(status_code=503,detail="No audit control configured")
        try:
            outcome=orchestrate(dataset,job.goal,job.entity,job.use_model_planner)
        except PlanError:
            raise HTTPException(status_code=422,detail="Unsupported, unsafe or unavailable tool plan")
        try:
            event=audit.append(actor,job.entity,"bounded_orchestrator","SUCCESS",
                               (time.perf_counter()-started)*1000)
        except Exception:
            raise HTTPException(status_code=503,detail="Audit unavailable")
        outcome.update(event_id=event,agent_version="0.1.0",deployment_status="LOCAL_PROTOTYPE")
        return outcome

    @app.get("/v1/audit/verify")
    def verify(authorization:str|None=Header(default=None)):
        try:
            actor=authorizer.authorize(authorization,"executive_brief","ALL")
        except (Unauthorized,Forbidden):
            raise HTTPException(status_code=403,detail="Executive audit access required")
        if actor.role!="people_leader" or audit is None:
            raise HTTPException(status_code=403,detail="Executive audit access required")
        return audit.verify()
    return app

try:
    app=create_app(audit=AuditLedger())
except ValueError:
    app=create_app()
