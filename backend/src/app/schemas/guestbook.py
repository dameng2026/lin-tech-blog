from pydantic import BaseModel
from typing import Optional

class GuestbookCreate(BaseModel):
    content: str

class GuestbookResponse(BaseModel):
    id: int
    user_id: int
    username: str
    avatar: Optional[str]
    content: str
    is_top: bool
    reply: Optional[str]
    created_at: Optional[str]
    ip_address: Optional[str] = None
    guest_email: Optional[str] = None
    
    class Config:
        from_attributes = True
