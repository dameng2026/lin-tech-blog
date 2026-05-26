from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..core.database import Base

class Article(Base):
    __tablename__ = "articles"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    cover = Column(String(2000))
    summary = Column(Text)
    content = Column(Text, nullable=False)
    category = Column(String(50))
    tags = Column(JSON)
    tech_stack = Column(JSON)
    catalog = Column(JSON)
    read_time = Column(Integer)
    view_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)
    collect_count = Column(Integer, default=0)
    is_published = Column(Boolean, default=True)
    allow_comment = Column(Boolean, default=True)
    
    source_type = Column(String(20), default="original", nullable=False)
    repost_url = Column(String(2000))
    
    author_name = Column(String(100))
    author_avatar = Column(String(2000))
    author_bio = Column(Text)
    
    seo_title = Column(String(255))
    seo_keywords = Column(String(500))
    seo_description = Column(Text)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    comments = relationship("Comment", back_populates="article", cascade="all, delete-orphan")
    likes = relationship("ArticleLike", back_populates="article", cascade="all, delete-orphan")
    collects = relationship("ArticleCollect", back_populates="article", cascade="all, delete-orphan")

class ArticleLike(Base):
    __tablename__ = "article_likes"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    article_id = Column(Integer, ForeignKey("articles.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    article = relationship("Article", back_populates="likes")

class ArticleCollect(Base):
    __tablename__ = "article_collects"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    article_id = Column(Integer, ForeignKey("articles.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    article = relationship("Article", back_populates="collects")