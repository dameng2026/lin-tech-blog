from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FriendLinkCreate(BaseModel):
    name: str
    url: str
    logo: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = "技术博客"

class FriendLinkUpdate(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    logo: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    status: Optional[str] = None

class FriendLinkResponse(BaseModel):
    id: int
    name: str
    url: str
    logo: Optional[str]
    description: Optional[str]
    category: str
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
