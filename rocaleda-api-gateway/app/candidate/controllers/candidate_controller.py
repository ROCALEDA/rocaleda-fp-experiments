from fastapi import APIRouter

from app.candidate.services.candidate_service import CandidateService

router = APIRouter(
    prefix="/candidate",
    tags=["candidate"],
    responses={404: {"description": "Not found"}},
)


def initialize(candidate_service: CandidateService):
    @router.get("/")
    async def get_candidates():
        return await candidate_service.get_candidates()
