from sqlalchemy import column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from backend.db.database import Base

class StoryJob(Base):
    __tablename__ = "story_jobs"
    id = column(Integer, primary_key=True, index=True)
    story_id = column(Integer, nullable=True)
    job_id = column(String, index=True, unique=True)
    created_at = column(DateTime(timezone=True), server_default=func.now())
    theme = column(String, nullable=True)
    status = column(String, nullable=True)
    error = column(String, nullable=True)
    completed_job = column(DateTime(timezone=True), nullable=True)
    session_id = column(String, index=True, nullable=True)
    