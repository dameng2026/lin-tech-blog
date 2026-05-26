from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from ..core.database import Base

class SiteSettings(Base):
    __tablename__ = "site_settings"
    
    id = Column(Integer, primary_key=True, index=True)
    site_name = Column(String(100), default="我的技术博客")
    site_title = Column(String(200))
    keywords = Column(Text)
    description = Column(Text)
    logo = Column(String(255))
    banner_text = Column(Text)
    icp_number = Column(String(100))
    site_start_date = Column(DateTime(timezone=True))
    github_url = Column(String(255))
    qq_qrcode = Column(String(255))
    wechat_qrcode = Column(String(255))
    admin_avatar = Column(String(500))
    email = Column(String(100))
    author_name = Column(String(100))
    bio = Column(Text)
    bio_motto = Column(Text)
    bio_motto_items = Column(Text)
    bio_interests = Column(Text)
    experience = Column(String(100))
    location = Column(String(200))
    wechat = Column(String(100))
    qq = Column(String(50))
    phone = Column(String(50))
    favicon = Column(String(500))
    login_enabled = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class UploadedFile(Base):
    __tablename__ = "uploaded_files"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    original_name = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    file_type = Column(String(20))
    file_size = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
