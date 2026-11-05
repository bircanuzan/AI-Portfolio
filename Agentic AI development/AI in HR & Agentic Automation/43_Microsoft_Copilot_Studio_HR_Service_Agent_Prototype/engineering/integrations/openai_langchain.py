#!/usr/bin/env python3
"""OPTIONAL real OpenAI/LangChain path. NOT tested without a user's API credentials.
Never call an LLM for requests that fail a local safety gate. Output remains unverified
until independently scored; never treat prompted constraints as access control.
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from hr_agent.storage import connect
from hr_agent.ingestion import ingest
from hr_agent.agent import Agent
from hr_agent.retrieval import cosine, retrieve


def add_openai_vectors(db):
    if not os.getenv("OPENAI_API_KEY"): raise RuntimeError("OPENAI_API_KEY is required; no implicit network calls")
    from langchain_openai import OpenAIEmbeddings  # optional dependency
    embed=OpenAIEmbeddings(model="text-embedding-3-small")
    policies=db.execute("SELECT policy_id,title,body FROM policies WHERE approved=1").fetchall()
    vectors=embed.embed_documents([r["title"]+"\n"+r["body"] for r in policies])
    if len(vectors)!=len(policies): raise RuntimeError("Embedding count mismatch")
    for r,vec in zip(policies,vectors):
        db.execute("INSERT INTO vectors(policy_id,model,vector_json) VALUES(?,?,?) ON CONFLICT(policy_id,model) DO UPDATE SET vector_json=excluded.vector_json",
                   (r["policy_id"],"openai:text-embedding-3-small",json.dumps(vec)))
    db.commit()
    return {"embedded_documents":len(vectors),"model":"text-embedding-3-small","storage":"local SQLite JSON vectors, not enterprise vector DB"}


def openai_answer(db,query,model="gpt-4.1-mini",use_semantic=False):
    if not os.getenv("OPENAI_API_KEY"): raise RuntimeError("OPENAI_API_KEY required")
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    local=Agent(db).ask(query)
    if local["decision"]!="ANSWER":
        return {"provider":"NO_LLM_CALL","safety_gate":local,"generated_answer":None}
    source=local["sources"][0]
    if use_semantic:
        vec=OpenAIEmbeddings(model="text-embedding-3-small").embed_query(query)
        retrieved=retrieve(db,query,policy_id=source["id"],model="openai:text-embedding-3-small",query_vector=vec,min_score=0.1)
    else:
        retrieved=retrieve(db,query,policy_id=source["id"],min_score=0.03)
    if not retrieved: return {"provider":"NO_LLM_CALL","error":"No verified matching indexed source"}
    doc=retrieved["source"]
    prompt=ChatPromptTemplate.from_messages([
       ("system","You are a limited-scope HR policy assistant. Use ONLY this SYNTHETIC policy text. Do not present as UAE labour law or company rules. If evidence is missing say you cannot verify it; do not make employment decisions or request private data. Provide one short sourced answer. Source ID: {policy_id} v{version}. Policy: {policy_text}"),
       ("human","{question}")])
    chain=prompt | ChatOpenAI(model=model,temperature=0,max_retries=1,timeout=25) | StrOutputParser()
    answer=chain.invoke({"policy_id":doc["policy_id"],"version":doc["version"],"policy_text":doc["body"],"question":query})
    return {"provider":"OpenAI via LangChain","model":model,"policy_source":source,
            "generated_answer":answer,"independent_correctness_review":"NOT_PERFORMED",
            "timestamp_utc":datetime.now(timezone.utc).isoformat(),"safety_gate":local,
            "warning":"LLM output not automatically verified; independent factual and safety grading required"}

if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("action",choices=["embed","ask"])
    parser.add_argument("--query",default="What is our annual leave policy?")
    parser.add_argument("--model",default="gpt-4.1-mini");parser.add_argument("--semantic",action="store_true")
    parser.add_argument("--db",default=str(ROOT/"data"/"lab.sqlite3"));args=parser.parse_args()
    with connect(args.db) as db:
        if not db.execute("SELECT 1 FROM policies").fetchone():ingest(db,ROOT/"data"/"policies.json")
        result=add_openai_vectors(db) if args.action=="embed" else openai_answer(db,args.query,args.model,args.semantic)
    print(json.dumps(result,indent=2))
