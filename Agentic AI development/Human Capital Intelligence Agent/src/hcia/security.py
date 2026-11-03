"""Fail-closed development RBAC: enterprise deployment requires OIDC gateway."""
import json
import os
import secrets
from dataclasses import dataclass

PERMISSIONS={
 "recruitment_analyst":{"talent_acquisition","employer_brand"},
 "hc_operations":{"human_capital_operations"},
 "workforce_analyst":{"talent_management","workforce_intelligence"},
 "reward_analyst":{"total_rewards"},
 "people_leader":{"talent_acquisition","employer_brand","human_capital_operations",
                  "talent_management","total_rewards","workforce_intelligence","executive_brief"},
 "auditor":set()
}
@dataclass(frozen=True)
class Actor:
    actor_id:str
    role:str
    entities:tuple[str,...]
class Unauthorized(Exception):
    pass
class Forbidden(Exception):
    pass
class Authorizer:
    def __init__(self,tokens=None):
        tokens=json.loads(os.getenv("HCIA_TOKENS_JSON","{}")) if tokens is None else tokens
        if not isinstance(tokens,dict):
            raise ValueError("Invalid token map")
        self.entries={}
        for token,info in tokens.items():
            if (not isinstance(token,str) or len(token)<16 or not isinstance(info,dict)
                or info.get("role") not in PERMISSIONS or not info.get("entities")):
                raise ValueError("Invalid token map entry")
            self.entries[token]=Actor(info.get("actor_id","anonymous"),
                                     info["role"],tuple(info["entities"]))
    def authorize(self,header,capability,entity):
        if not header or not header.startswith("Bearer "):
            raise Unauthorized("No bearer token")
        requested=header[7:].strip()
        actor=next((a for token,a in self.entries.items()
                    if secrets.compare_digest(token,requested)),None)
        if actor is None:
            raise Unauthorized("Unknown token")
        if capability not in PERMISSIONS[actor.role] or entity not in actor.entities:
            raise Forbidden("Insufficient scope")
        return actor
