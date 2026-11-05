from sqlalchemy import column, Integer, String, DateTime, ForeignKey, Boolean , JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from backend.db.database import Base
class Story(Base):
    pass