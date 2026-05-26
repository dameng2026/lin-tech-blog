from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SiteSettingsBase(BaseModel):
    site_name: Optional[str] = None
    site_title: Optional[str] = None
    keywords: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None
    banner_text: Optional[str] = None
    icp_number: Optional[str] = None
    github_url: Optional[str] = None
    qq_qrcode: Optional[str] = None
    wechat_qrcode: Optional[str] = None
    admin_avatar: Optional[str] = None
    email: Optional[str] = None
    author_name: Optional[str] = None
    bio: Optional[str] = None
    bio_motto: Optional[str] = None
    bio_motto_items: Optional[str] = None
    bio_interests: Optional[str] = None
    experience: Optional[str] = None
    location: Optional[str] = None
    wechat: Optional[str] = None
    qq: Optional[str] = None
    phone: Optional[str] = None
    favicon: Optional[str] = None
    login_enabled: Optional[int] = None

class SiteSettingsUpdate(SiteSettingsBase):
    site_start_date: Optional[datetime] = None

class SiteSettingsResponse(SiteSettingsBase):
    id: int
    site_start_date: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class UploadedFileResponse(BaseModel):
    id: int
    filename: str
    original_name: str
    file_path: str
    file_type: Optional[str] = None
    file_size: Optional[int] = None
    created_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
