from sqlalchemy import Column, Integer, String, DateTime, JSON, BigInteger, ForeignKey
from sqlalchemy.sql import func
from ..core.database import Base

class SiteStats(Base):
    __tablename__ = "site_stats"
    
    id = Column(Integer, primary_key=True, index=True)
    articles_count = Column(Integer, default=0)
    projects_count = Column(Integer, default=0)
    total_views = Column(BigInteger, default=0)
    total_likes = Column(BigInteger, default=0)
    total_comments = Column(Integer, default=0)
    total_collects = Column(Integer, default=0)
    github_stars = Column(Integer, default=0)
    github_followers = Column(Integer, default=0)
    site_start_date = Column(DateTime(timezone=True))
    cached_at = Column(DateTime(timezone=True), server_default=func.now())

class ArticleArchive(Base):
    __tablename__ = "article_archive"
    
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    article_count = Column(Integer, default=0)
    articles = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class ViewLog(Base):
    __tablename__ = "view_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey("articles.id"))
    ip_address = Column(String(50))
    user_agent = Column(String(255))
    view_time = Column(DateTime(timezone=True), server_default=func.now())