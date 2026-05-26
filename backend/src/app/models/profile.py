from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.sql import func
from ..core.database import Base

class Profile(Base):
    __tablename__ = "profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    bio = Column(Text)
    social_links = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Skill(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer)
    name = Column(String(50), nullable=False)
    proficiency = Column(Integer, default=0)
    category = Column(String(50))

class Experience(Base):
    __tablename__ = "experiences"
    
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer)
    title = Column(String(100), nullable=False)
    company = Column(String(100))
    start_date = Column(String(20))
    end_date = Column(String(20))
    description = Column(Text)
    tags = Column(JSON, default=list)
    order = Column(Integer, default=0)

class Education(Base):
    __tablename__ = "education"
    
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer)
    degree = Column(String(50))
    school = Column(String(100))
    major = Column(String(100))
    start_date = Column(String(20))
    end_date = Column(String(20))
    order = Column(Integer, default=0)

class ResumeKey(Base):
    __tablename__ = "resume_keys"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    key_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())