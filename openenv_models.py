from pydantic import BaseModel
from typing import List, Dict, Any

# Observations
class EmailTriageObs(BaseModel):
    emails: List[Dict[str, Any]]  # id, sender, subject, body_snippet, label
    state_id: int

class DataCleaningObs(BaseModel):
    table: List[Dict[str, Any]]   # rows as dict
    schema: Dict[str, str]        # col -> type
    state_id: int

class SchedulingObs(BaseModel):
    participants: List[str]
    calendars: Dict[str, List[Dict[str, str]]]  # participant -> busy slots
    state_id: int

# Action
class Action(BaseModel):
    task: str       # "email", "data", "schedule"
    cmd: str        # "classify", "drop_missing", "propose_meeting", etc.
    args: Dict[str, Any]

# Reward
class Reward(BaseModel):
    value: float
    score: float   # 0.0 - 1.0 normalized grader score