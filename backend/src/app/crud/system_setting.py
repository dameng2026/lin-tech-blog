"""
系统设置的CRUD操作
"""
from sqlalchemy.orm import Session
from typing import Optional, Dict
from ..models.system_setting import SystemSetting
from ..core.exceptions import NotFoundException

def get_setting(db: Session, key: str) -> Optional[SystemSetting]:
    return db.query(SystemSetting).filter(SystemSetting.key == key).first()

def get_setting_value(db: Session, key: str, default=None):
    """获取设置值，如果不存在返回默认值"""
    setting = get_setting(db, key)
    if setting is None:
        return default
    
    # 根据类型转换值
    if setting.setting_type == "boolean":
        return setting.value.lower() == "true"
    elif setting.setting_type == "int":
        return int(setting.value)
    elif setting.setting_type == "float":
        return float(setting.value)
    return setting.value

def set_setting(db: Session, key: str, value, description: str = "", setting_type: str = "string") -> SystemSetting:
    """设置配置项"""
    setting = get_setting(db, key)
    
    # 转换值为字符串存储
    if isinstance(value, bool):
        value_str = "true" if value else "false"
        setting_type = "boolean"
    elif isinstance(value, int):
        value_str = str(value)
        setting_type = "int"
    elif isinstance(value, float):
        value_str = str(value)
        setting_type = "float"
    else:
        value_str = str(value)
    
    if setting:
        setting.value = value_str
        setting.setting_type = setting_type
        if description:
            setting.description = description
    else:
        setting = SystemSetting(
            key=key,
            value=value_str,
            description=description,
            setting_type=setting_type
        )
        db.add(setting)
    
    db.commit()
    db.refresh(setting)
    return setting

def delete_setting(db: Session, key: str) -> None:
    """删除配置项"""
    setting = get_setting(db, key)
    if not setting:
        raise NotFoundException("Setting not found")
    db.delete(setting)
    db.commit()

def get_all_settings(db: Session) -> Dict[str, any]:
    """获取所有配置项"""
    settings = db.query(SystemSetting).all()
    result = {}
    for setting in settings:
        result[setting.key] = get_setting_value(db, setting.key)
    return result

def init_default_settings(db: Session) -> None:
    """初始化默认设置"""
    default_settings = [
        {
            "key": "ai_model_enabled",
            "value": False,
            "description": "AI模型功能开关",
            "setting_type": "boolean"
        },
        {
            "key": "ai_model_default_config",
            "value": "",
            "description": "默认AI模型配置ID",
            "setting_type": "string"
        },
        {
            "key": "catalog_auto_generate",
            "value": False,
            "description": "是否自动生成章节目录",
            "setting_type": "boolean"
        },
        {
            "key": "prohibited_words",
            "value": "",
            "description": "违禁词列表，多个词用逗号或换行分隔",
            "setting_type": "string"
        },
    ]
    
    for setting in default_settings:
        if not get_setting(db, setting["key"]):
            set_setting(
                db,
                setting["key"],
                setting["value"],
                setting["description"],
                setting["setting_type"]
            )
