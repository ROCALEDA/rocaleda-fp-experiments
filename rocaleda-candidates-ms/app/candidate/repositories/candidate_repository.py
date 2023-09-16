from typing import List

from app.database import models, database


class CandidateRepository:
    async def get_candidates_by_filter(self, soft_skill_ids: List[int]):
        with database.create_session() as db:
            candidate_ids = (
                db.query(models.SoftSkillsSet.candidate_id)
                .filter(models.SoftSkillsSet.soft_skill_id.in_(soft_skill_ids))
                .distinct()
                .all()
            )

            unique_candidate_ids = {id for id, in candidate_ids}

            candidates = (
                db.query(models.Candidate)
                .filter(models.Candidate.id.in_(unique_candidate_ids))
                .all()
            )
            return candidates

    async def get_candidates(self):
        with database.create_session() as db:
            candidates = db.query(models.Candidate).all()
            return candidates
