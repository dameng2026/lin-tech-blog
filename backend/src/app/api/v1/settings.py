"""
系统设置相关的API端点
"""
from fastapi import APIRouter, Depends, HTTPException, Query, Body
from sqlalchemy.orm import Session
from typing import Optional, Dict
from ..dependencies import get_current_admin
from .auth import wrap_response
from ...crud.system_setting import (
    get_setting_value, set_setting, get_all_settings, delete_setting, init_default_settings
)
from ...crud.site_settings import get_site_settings as crud_get_site_settings
from ...crud.site_settings import update_site_settings as crud_update_site_settings
from ...schemas.site_settings import SiteSettingsUpdate as SiteSettingsSchema
from ...core.database import get_db

router = APIRouter(prefix="/settings", tags=["settings"])

@router.get("/")
def get_settings(db: Session = Depends(get_db)):
    settings = get_all_settings(db)
    return wrap_response(data=settings)

@router.get("/site")
def get_site_settings(db: Session = Depends(get_db)):
    settings = crud_get_site_settings(db)
    return wrap_response(data=settings)

@router.put("/site", dependencies=[Depends(get_current_admin)])
def update_site_settings(
    settings_data: SiteSettingsSchema,
    db: Session = Depends(get_db)
):
    updated = crud_update_site_settings(db, settings_data)
    return wrap_response(data=updated, msg="站点设置更新成功")

@router.get("/{key}")
def get_setting(key: str, db: Session = Depends(get_db)):
    value = get_setting_value(db, key)
    return wrap_response(data={key: value})

@router.put("/{key}", dependencies=[Depends(get_current_admin)])
def update_setting(
    key: str,
    value: str = Query(..., description="设置值"),
    description: Optional[str] = Query(None, description="设置描述"),
    setting_type: Optional[str] = Query("string", description="设置类型: string, boolean, int, float"),
    db: Session = Depends(get_db)
):
    # 尝试转换值类型
    try:
        if setting_type == "boolean":
            value = value.lower() == "true"
        elif setting_type == "int":
            value = int(value)
        elif setting_type == "float":
            value = float(value)
    except ValueError:
        raise HTTPException(status_code=400, detail="值类型转换失败")
    
    set_setting(db, key, value, description, setting_type)
    return wrap_response(msg="设置更新成功")

@router.delete("/{key}", dependencies=[Depends(get_current_admin)])
def remove_setting(key: str, db: Session = Depends(get_db)):
    try:
        delete_setting(db, key)
        return wrap_response(msg="设置删除成功")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/init", dependencies=[Depends(get_current_admin)])
def init_settings(db: Session = Depends(get_db)):
    init_default_settings(db)
    return wrap_response(msg="默认设置初始化成功")

# AI模型开关专用接口
@router.get("/ai-model/enabled")
def get_ai_model_enabled(db: Session = Depends(get_db)):
    enabled = get_setting_value(db, "ai_model_enabled", False)
    return wrap_response(data={"enabled": enabled})

@router.put("/ai-model/enabled", dependencies=[Depends(get_current_admin)])
def set_ai_model_enabled(
    request_data: Dict[str, bool] = Body(...),
    db: Session = Depends(get_db)
):
    enabled = request_data.get("enabled", False)
    set_setting(db, "ai_model_enabled", enabled, "AI模型功能开关", "boolean")
    return wrap_response(msg="AI模型开关已更新", data={"enabled": enabled})
