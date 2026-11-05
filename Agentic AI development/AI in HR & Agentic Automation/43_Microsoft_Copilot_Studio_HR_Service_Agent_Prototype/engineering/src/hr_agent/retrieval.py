"""Small local vector index. Default vectors are hashed lexical features, NOT ML embeddings."""
import hashlib
import json
import math
import re

STOP = {"the", "a", "an", "to", "is", "are", "at", "our", "for", "how", "do", "i", "can", "what", "which", "of", "and", "my", "please", "tell", "me", "about", "have", "on", "in", "does"}
DIM = 256

def tokens(text):
    return [x for x in re.findall(r"[a-z0-9]+", text.lower()) if len(x)>1 and x not in STOP]

def hashed_vector(text):
    vec = [0.0] * DIM
    for word in tokens(text):
        slot = int(hashlib.sha256(word.encode()).hexdigest()[:8], 16) % DIM
        vec[slot] += 1.0
    norm = math.sqrt(sum(x*x for x in vec)) or 1.0
    return [x/norm for x in vec]

def cosine(a, b):
    if len(a) != len(b):
        raise ValueError("Embedding dimensions mismatch; refuse mixed model scores")
    return sum(x*y for x,y in zip(a,b))

def retrieve(db, query, policy_id=None, min_score=0.14, model="sha256-lexical-v1", query_vector=None):
    """Enforce approved/current source; return only one matching policy or None."""
    rows = db.execute("""SELECT p.*,v.vector_json FROM policies p
      JOIN vectors v ON p.policy_id=v.policy_id AND v.model=?
      WHERE p.approved=1 AND date('now') BETWEEN p.effective_from AND p.effective_to
      AND (? IS NULL OR p.policy_id=?)""",(model,policy_id,policy_id)).fetchall()
    qv = query_vector if query_vector is not None else hashed_vector(query)
    ranked=[]
    for r in rows:
        score = cosine(qv, json.loads(r["vector_json"]))
        ranked.append((score, dict(r)))
    ranked.sort(key=lambda item:(-item[0],item[1]["policy_id"]))
    if not ranked or ranked[0][0] < min_score: return None
    score, p = ranked[0]
    p.pop("vector_json", None)
    return {"source":p,"retrieval_score":round(score,4),"vector_model":model}
