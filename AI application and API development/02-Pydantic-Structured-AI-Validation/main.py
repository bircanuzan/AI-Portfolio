"""Pydantic v2 input governance for a synthetic model response."""
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, ValidationError

class AIReview(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    task_id: str = Field(min_length=3)
    risk_level: Literal["low", "medium", "high"]
    evidence: list[str] = Field(min_length=1)
    requires_human_review: bool

SAMPLE_OK = {
    "task_id": "DEMO-01",
    "risk_level": "high",
    "evidence": ["Example source paragraph"],
    "requires_human_review": True,
}
SAMPLE_BAD = {**SAMPLE_OK, "risk_level": "critical"}

if __name__ == "__main__":
    result = AIReview.model_validate(SAMPLE_OK)
    print(result.model_dump_json(indent=2))
    try:
        AIReview.model_validate(SAMPLE_BAD)
    except ValidationError as err:
        print("Rejected invalid model payload:", err.errors()[0]["type"])
    else:
        raise AssertionError("Invalid risk level was not rejected")
