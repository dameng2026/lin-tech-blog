"""
系统设置模型
用于存储系统级别的配置项，如功能开关等
"""
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.sql import func
from ..core.database import Base

class SystemSetting(Base):
    __tablename__ = "system_settings"
    
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(100), nullable=False, unique=True)
    value = Column(Text)
    description = Column(String(500))
    setting_type = Column(String(20), default="string")  # string, boolean, int, float
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<SystemSetting {self.key}={self.value}>"

# 预定义的系统设置键
SETTING_KEYS = {
    "AI_MODEL_ENABLED": "ai_model_enabled",
    "AI_MODEL_DEFAULT_CONFIG": "ai_model_default_config",
    "CATALOG_AUTO_GENERATE": "catalog_auto_generate",
}
