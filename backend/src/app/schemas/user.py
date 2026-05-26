from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, Dict

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: Optional[str] = None
    userName: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    code: Optional[str] = None

class UserUpdate(BaseModel):
    nickname: Optional[str] = None
    avatar: Optional[str] = None
    bio: Optional[str] = None
    city: Optional[str] = None
    social_links: Optional[Dict] = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    nickname: Optional[str]
    avatar: Optional[str]
    bio: Optional[str]
    city: Optional[str]
    social_links: Optional[Dict]
    role: str
    created_at: datetime

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: UserResponse

class VerifyCodeRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    email: EmailStr
    code: str
    new_password: str

class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str