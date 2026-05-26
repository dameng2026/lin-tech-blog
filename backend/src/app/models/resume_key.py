from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from ..core.database import Base

class ResumeKey(Base):
    __tablename__ = "resume_download_keys"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    key_value = Column(String(32), nullable=False, unique=True)
    is_active = Column(Boolean, default=True)
    use_count = Column(Integer, default=0)
    expire_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, server_default=func.now())