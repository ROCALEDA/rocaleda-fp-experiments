from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    document_type = Column(String(20), nullable=False)
    document_number = Column(String(20), nullable=False)
    cv_path = Column(String(200), nullable=False)

    soft_skills_set = relationship("SoftSkillsSet", back_populates="candidate")


class SoftSkill(Base):
    __tablename__ = "soft_skills"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)

    soft_skills_set = relationship("SoftSkillsSet", back_populates="soft_skill")


class SoftSkillsSet(Base):
    __tablename__ = "soft_skills_set"

    candidate_id = Column(Integer, ForeignKey("candidates.id"), primary_key=True)
    soft_skill_id = Column(Integer, ForeignKey("soft_skills.id"), primary_key=True)
    system_score = Column(Integer, nullable=False, default=0)

    candidate = relationship("Candidate", back_populates="soft_skills_set")
    soft_skill = relationship("SoftSkill", back_populates="soft_skills_set")
