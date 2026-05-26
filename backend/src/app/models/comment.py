from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Index
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..core.database import Base

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    guest_name = Column(String(100), nullable=True)
    guest_email = Column(String(255), nullable=True)
    ip_address = Column(String(45), nullable=True)
    content = Column(Text, nullable=False)
    parent_id = Column(Integer, ForeignKey("comments.id"))
    reply_to_id = Column(Integer, nullable=True)
    reply_to_name = Column(String(100), nullable=True)
    like_count = Column(Integer, default=0)
    is_approved = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    article = relationship("Article", back_populates="comments")
    project = relationship("Project", back_populates="comments")
    replies = relationship("Comment", back_populates="parent", remote_side=[id])
    parent = relationship("Comment", back_populates="replies")
    likes = relationship("CommentLike", back_populates="comment", cascade="all, delete-orphan")
    
    # 确保每个评论要么有 article_id 要么有 project_id
    __table_args__ = (
        Index("idx_article_created", "article_id", "created_at"),
        Index("idx_article_likes", "article_id", "like_count"),
        Index("idx_project_created", "project_id", "created_at"),
        Index("idx_project_likes", "project_id", "like_count"),
        Index("idx_ip_created", "ip_address", "created_at"),
    )

class CommentLike(Base):
    __tablename__ = "comment_likes"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    comment_id = Column(Integer, ForeignKey("comments.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    comment = relationship("Comment", back_populates="likes")

class Guestbook(Base):
    __tablename__ = "guestbook"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text, nullable=False)
    is_top = Column(Boolean, default=False)
    reply = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())