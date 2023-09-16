from typing import List
from pydantic import BaseModel


class SoftSkillRead(BaseModel):
    id: int
    name: str
    description: str
    system_score: int

    class Config:
        orm_mode = True


class CandidateRead(BaseModel):
    id: int
    name: str
    document_type: str
    document_number: str
    cv_path: str
    soft_skills: List[SoftSkillRead] = []

    class Config:
        orm_mode = True
