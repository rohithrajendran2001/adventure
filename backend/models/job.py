from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db.database import Base

class StoryJob(Base):
    __tablename__ = "story_jobs"
    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, nullable=True)
    job_id = Column(String, index=True, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    theme = Column(String, nullable=True)
    status = Column(String, nullable=True)
    error = Column(String, nullable=True)
    completed_at = Column("completed_job", DateTime(timezone=True), nullable=True)
    session_id = Column(String, index=True, nullable=True)
    