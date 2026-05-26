from sqlalchemy import Column, Integer, String, Text, DateTime, JSON, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    cover = Column(String(255))
    tags = Column(JSON)
    github_url = Column(String(255))
    demo_url = Column(String(255))
    summary = Column(Text)
    tech_stack = Column(JSON)
    status = Column(String(20), default="active")
    view_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    description = Column(Text)
    project_type = Column(String(50))
    start_date = Column(DateTime(timezone=True))
    end_date = Column(DateTime(timezone=True))
    last_update = Column(DateTime(timezone=True))
    open_source_license = Column(String(100))
    database_type = Column(String(50))
    deployment_platform = Column(String(255))
    docs_url = Column(String(255))
    content = Column(Text)
    catalog = Column(JSON)
    
    is_paid = Column(Boolean, default=False)
    is_featured = Column(Boolean, default=False)
    repost_url = Column(String(255))
    category_id = Column(Integer)
    display_status = Column(String(20), default="active")
    publish_time = Column(DateTime(timezone=True), server_default=func.now())
    like_count = Column(Integer, default=0)
    
    comments = relationship("Comment", back_populates="project")