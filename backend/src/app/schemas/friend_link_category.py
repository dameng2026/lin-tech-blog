from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FriendLinkCategoryCreate(BaseModel):
    name: str
    description: Optional[str] = None

class FriendLinkCategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class FriendLinkCategoryResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True