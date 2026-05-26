"""
AI模型配置的CRUD操作
"""
from sqlalchemy.orm import Session
from typing import Optional, List
from ..models.ai_config import AIModelConfig
from ..schemas.ai_config import AIModelConfigCreate, AIModelConfigUpdate
from fastapi import HTTPException, status

def create_ai_config(db: Session, config_create: AIModelConfigCreate) -> AIModelConfig:
    config = AIModelConfig(
        name=config_create.name,
        model_type=config_create.model_type,
        api_key=config_create.api_key,
        api_url=config_create.api_url,
        timeout=config_create.timeout,
        max_tokens=config_create.max_tokens,
        temperature=config_create.temperature,
        enabled=config_create.enabled,
        description=config_create.description
    )
    db.add(config)
    db.commit()
    db.refresh(config)
    return config

def get_ai_config(db: Session, config_id: int) -> AIModelConfig:
    return db.query(AIModelConfig).filter(AIModelConfig.id == config_id).first()

def get_ai_config_by_name(db: Session, name: str) -> AIModelConfig:
    return db.query(AIModelConfig).filter(AIModelConfig.name == name).first()

def get_all_ai_configs(db: Session) -> List[AIModelConfig]:
    return db.query(AIModelConfig).all()

def get_enabled_ai_configs(db: Session) -> List[AIModelConfig]:
    return db.query(AIModelConfig).filter(AIModelConfig.enabled == True).all()

def update_ai_config(db: Session, config_id: int, config_update: AIModelConfigUpdate) -> AIModelConfig:
    config = get_ai_config(db, config_id)
    if not config:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AI配置不存在")
    
    if config_update.name is not None:
        config.name = config_update.name
    if config_update.model_type is not None:
        config.model_type = config_update.model_type
    if config_update.api_key is not None:
        config.api_key = config_update.api_key
    if config_update.api_url is not None:
        config.api_url = config_update.api_url
    if config_update.timeout is not None:
        config.timeout = config_update.timeout
    if config_update.max_tokens is not None:
        config.max_tokens = config_update.max_tokens
    if config_update.temperature is not None:
        config.temperature = config_update.temperature
    if config_update.enabled is not None:
        config.enabled = config_update.enabled
    if config_update.description is not None:
        config.description = config_update.description
    
    db.commit()
    db.refresh(config)
    return config

def delete_ai_config(db: Session, config_id: int) -> None:
    config = get_ai_config(db, config_id)
    if not config:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AI配置不存在")
    db.delete(config)
    db.commit()

def get_default_config(db: Session) -> Optional[AIModelConfig]:
    """获取默认启用的配置"""
    return db.query(AIModelConfig).filter(AIModelConfig.enabled == True).first()
