"""
AI模型配置相关的API端点
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from ..dependencies import get_current_admin
from .auth import wrap_response
from ...crud.ai_config import (
    create_ai_config, get_ai_config, get_ai_config_by_name,
    get_all_ai_configs, get_enabled_ai_configs, update_ai_config,
    delete_ai_config, get_default_config
)
from ...schemas.ai_config import AIModelConfigCreate, AIModelConfigUpdate, AIModelConfigResponse
from ...core.database import get_db

router = APIRouter(prefix="/ai-config", tags=["ai-config"])

@router.get("/")
def list_ai_configs(
    enabled_only: bool = Query(False),
    db: Session = Depends(get_db)
):
    if enabled_only:
        configs = get_enabled_ai_configs(db)
    else:
        configs = get_all_ai_configs(db)
    
    return wrap_response(data=[
        AIModelConfigResponse.from_orm(config) for config in configs
    ])

@router.get("/default")
def get_default_ai_config(db: Session = Depends(get_db)):
    config = get_default_config(db)
    if not config:
        return wrap_response(data=None, msg="暂无启用的AI配置")
    
    return wrap_response(data=AIModelConfigResponse.from_orm(config))

@router.get("/{config_id}")
def get_ai_config_detail(config_id: int, db: Session = Depends(get_db)):
    config = get_ai_config(db, config_id)
    if not config:
        raise HTTPException(status_code=404, detail="AI配置不存在")
    
    return wrap_response(data=AIModelConfigResponse.from_orm(config))

@router.post("/", dependencies=[Depends(get_current_admin)])
def create_new_ai_config(config_create: AIModelConfigCreate, db: Session = Depends(get_db)):
    # 检查名称是否已存在
    existing = get_ai_config_by_name(db, config_create.name)
    if existing:
        raise HTTPException(status_code=400, detail="配置名称已存在")
    
    config = create_ai_config(db, config_create)
    return wrap_response(data=AIModelConfigResponse.from_orm(config), msg="配置创建成功")

@router.put("/{config_id}", dependencies=[Depends(get_current_admin)])
def update_existing_ai_config(
    config_id: int,
    config_update: AIModelConfigUpdate,
    db: Session = Depends(get_db)
):
    try:
        config = update_ai_config(db, config_id, config_update)
        return wrap_response(data=AIModelConfigResponse.from_orm(config), msg="配置更新成功")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{config_id}", dependencies=[Depends(get_current_admin)])
def delete_ai_config_by_id(config_id: int, db: Session = Depends(get_db)):
    try:
        delete_ai_config(db, config_id)
        return wrap_response(data=None, msg="配置删除成功")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
