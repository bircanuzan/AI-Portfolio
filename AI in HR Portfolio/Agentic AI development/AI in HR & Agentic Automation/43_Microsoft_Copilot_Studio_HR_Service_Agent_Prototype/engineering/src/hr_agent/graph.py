"""Simple SQL relationship graph — transparent local proof, not a graph-database product."""
import json
from pathlib import Path

def load_edges(db,path):
    edges=json.loads(Path(path).read_text(encoding="utf-8"))
    count=0
    for edge in edges:
        if not all(k in edge for k in ("from","to","relation")):raise ValueError("Invalid edge")
        if not db.execute("SELECT 1 FROM policies WHERE policy_id=?",(edge["from"],)).fetchone():raise ValueError("Unknown source node")
        if not db.execute("SELECT 1 FROM policies WHERE policy_id=?",(edge["to"],)).fetchone():raise ValueError("Unknown destination node")
        db.execute("INSERT OR IGNORE INTO policy_links(from_id,to_id,relation) VALUES(?,?,?)",
                  (edge["from"],edge["to"],edge["relation"]))
        count+=1
    db.commit();return {"relationships_loaded":count}

def related(db,policy_id):
    return [dict(x) for x in db.execute("""SELECT from_id,to_id,relation FROM policy_links
     WHERE from_id=? OR to_id=? ORDER BY from_id,to_id""",(policy_id,policy_id)).fetchall()]
