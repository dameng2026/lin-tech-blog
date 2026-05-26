from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime
from typing import Optional, List

class ProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    cover: Optional[str] = None
    tags: Optional[List[str]] = []
    github_url: Optional[str] = None
    demo_url: Optional[str] = None
    summary: Optional[str] = None
    tech_stack: Optional[List[str]] = []
    status: Optional[str] = "active"
    
    description: Optional[str] = None
    project_type: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    open_source_license: Optional[str] = None
    database_type: Optional[str] = None
    deployment_platform: Optional[str] = None
    docs_url: Optional[str] = None
    content: Optional[str] = None
    catalog: Optional[List[dict]] = []
    
    is_paid: Optional[bool] = False
    is_featured: Optional[bool] = False
    repost_url: Optional[str] = None
    category_id: Optional[int] = None
    display_status: Optional[str] = None
    like_count: Optional[int] = None
    view_count: Optional[int] = None

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    cover: Optional[str] = None
    tags: Optional[List[str]] = None
    github_url: Optional[str] = None
    demo_url: Optional[str] = None
    summary: Optional[str] = None
    tech_stack: Optional[List[str]] = None
    status: Optional[str] = None
    
    description: Optional[str] = None
    project_type: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    open_source_license: Optional[str] = None
    database_type: Optional[str] = None
    deployment_platform: Optional[str] = None
    docs_url: Optional[str] = None
    content: Optional[str] = None
    catalog: Optional[List[dict]] = None
    
    is_paid: Optional[bool] = None
    is_featured: Optional[bool] = None
    repost_url: Optional[str] = None
    category_id: Optional[int] = None
    display_status: Optional[str] = None

class ProjectResponse(BaseModel):
    id: int
    name: str
    cover: Optional[str]
    tags: List[str]
    github_url: Optional[str]
    demo_url: Optional[str]
    summary: Optional[str]
    tech_stack: List[str]
    status: str
    view_count: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    description: Optional[str] = None
    project_type: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    open_source_license: Optional[str] = None
    database_type: Optional[str] = None
    deployment_platform: Optional[str] = None
    docs_url: Optional[str] = None
    content: Optional[str] = None
    catalog: Optional[List[dict]] = None
    
    is_paid: bool = False
    is_featured: bool = False
    repost_url: Optional[str] = None
    category_id: Optional[int] = None
    display_status: Optional[str] = None
    publish_time: Optional[datetime] = None
    like_count: int = 0

    class Config:
        from_attributes = True
    
    @classmethod
    def model_validate(cls, obj, **kwargs):
        result = super().model_validate(obj, **kwargs)
        if result.catalog is None:
            result.catalog = []
        if result.tags is None:
            result.tags = []
        if result.tech_stack is None:
            result.tech_stack = []
        return result