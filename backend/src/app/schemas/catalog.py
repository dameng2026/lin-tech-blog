"""
目录生成相关的Schema定义
"""
from pydantic import BaseModel, Field
from typing import Optional

class CatalogGenerateRequest(BaseModel):
    content: str = Field(..., description="文章内容")
    use_ai: Optional[bool] = Field(True, description="是否使用AI生成")
