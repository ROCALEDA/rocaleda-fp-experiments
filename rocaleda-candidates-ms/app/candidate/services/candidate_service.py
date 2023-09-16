from app.candidate.repositories.candidate_repository import CandidateRepository


class CandidateService:
    def __init__(self, candidate_repository: CandidateRepository):
        self.candidate_repository = candidate_repository

    async def get_candidates(self, soft_skills: list[int] | None):
        if soft_skills is None:
            return await self.candidate_repository.get_candidates()

        return await self.candidate_repository.get_candidates_by_filter(soft_skills)
