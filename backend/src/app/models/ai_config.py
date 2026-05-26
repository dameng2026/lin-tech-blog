"""
AI模型配置模型
"""
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Float
from sqlalchemy.sql import func
from ..core.database import Base

class AIModelConfig(Base):
    __tablename__ = "ai_model_configs"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    model_type = Column(String(50), nullable=False)
    api_key = Column(String(255))
    api_url = Column(String(500), nullable=False)
    timeout = Column(Integer, default=30)
    max_tokens = Column(Integer, default=2048)
    temperature = Column(Float, default=0.7)
    enabled = Column(Boolean, default=True)
    description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
