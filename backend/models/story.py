from sqlalchemy import column, Integer, String, DateTime, ForeignKey, Boolean , JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from backend.db.database import Base
class Story(Base):
    __tablename__ = "stories"
    id = column(Integer, primary_key=True, index=True)
    title = column(String, index=True)
    session_id = column(String, index=True)
    ceated_at = column(DateTime(timezone=True), server_default=func.now())
    nodes = relationship("StoryNode", back_populates="story")

class StoryNode(Base):
    __tablename__ = "story_nodes"
    id = column(Integer, primary_key=True, index=True)
    story_id = column(Integer, ForeignKey("stories.id"),index=True)
    content = column(String)
    is_root = column(Boolean, default=False)
    is_ending = column(Boolean, default=False)
    is_winning_ending = column(Boolean, default=False)
    options = column(JSON, default=list)
    story = relationship("Story", back_populates="nodes")