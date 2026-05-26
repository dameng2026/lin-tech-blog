"""
AI模型配置相关的Schema定义
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class AIModelConfigCreate(BaseModel):
    name: str = Field(..., description="配置名称")
    model_type: str = Field(..., description="模型类型")
    api_key: Optional[str] = Field(None, description="API密钥")
    api_url: str = Field(..., description="API服务URL")
    timeout: Optional[int] = Field(30, description="请求超时时间（秒）")
    max_tokens: Optional[int] = Field(2048, description="最大token数")
    temperature: Optional[float] = Field(0.7, description="温度参数")
    enabled: Optional[bool] = Field(True, description="是否启用")
    description: Optional[str] = Field(None, description="配置描述")

class AIModelConfigUpdate(BaseModel):
    name: Optional[str] = Field(None, description="配置名称")
    model_type: Optional[str] = Field(None, description="模型类型")
    api_key: Optional[str] = Field(None, description="API密钥")
    api_url: Optional[str] = Field(None, description="API服务URL")
    timeout: Optional[int] = Field(None, description="请求超时时间（秒）")
    max_tokens: Optional[int] = Field(None, description="最大token数")
    temperature: Optional[float] = Field(None, description="温度参数")
    enabled: Optional[bool] = Field(None, description="是否启用")
    description: Optional[str] = Field(None, description="配置描述")

class AIModelConfigResponse(BaseModel):
    id: int
    name: str
    model_type: str
    api_key: Optional[str] = Field(None, description="API密钥")
    api_url: str
    timeout: int
    max_tokens: int
    temperature: float
    enabled: bool
    description: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
