from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class CommentCreate(BaseModel):
    content: str
    parent_id: Optional[int] = None
    reply_to_id: Optional[int] = None
    reply_to_name: Optional[str] = None
    guest_name: Optional[str] = None
    guest_email: Optional[str] = None

class CommentResponse(BaseModel):
    id: int
    article_id: Optional[int] = None
    project_id: Optional[int] = None
    user_id: Optional[int] = None
    username: str
    avatar: Optional[str] = None
    guest_name: Optional[str] = None
    content: str
    parent_id: Optional[int] = None
    reply_to_id: Optional[int] = None
    reply_to_name: Optional[str] = None
    like_count: int
    replies: Optional[List['CommentResponse']] = []
    created_at: datetime
    is_approved: bool = True
    content_type: Optional[str] = None
    content_id: Optional[int] = None
    content_title: Optional[str] = None

    class Config:
        from_attributes = True

class GuestbookCreate(BaseModel):
    content: str

class GuestbookResponse(BaseModel):
    id: int
    user_id: int
    username: str
    avatar: Optional[str] = None
    content: str
    is_top: bool
    reply: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True