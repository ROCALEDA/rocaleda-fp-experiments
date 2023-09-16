from typing import Annotated

from fastapi import APIRouter, Query

from app.candidate.services.candidate_service import CandidateService

router = APIRouter(
    prefix="/candidate",
    tags=["candidate"],
    responses={404: {"description": "Not found"}},
)


def initialize(candidate_service: CandidateService):
    @router.get("/")
    async def get_candidates(soft_skills: Annotated[list[int] | None, Query()] = None):
        return await candidate_service.get_candidates(soft_skills)
