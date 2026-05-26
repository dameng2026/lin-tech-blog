from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
from ..models.site_settings import SiteSettings, UploadedFile
from pydantic import BaseModel
from typing import List

class SiteSettingsUpdate(BaseModel):
    site_name: Optional[str] = None
    site_title: Optional[str] = None
    keywords: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None
    banner_text: Optional[str] = None
    icp_number: Optional[str] = None
    site_start_date: Optional[datetime] = None
    github_url: Optional[str] = None
    qq_qrcode: Optional[str] = None
    wechat_qrcode: Optional[str] = None
    email: Optional[str] = None
    author_name: Optional[str] = None
    bio: Optional[str] = None
    experience: Optional[str] = None
    admin_avatar: Optional[str] = None
    location: Optional[str] = None
    wechat: Optional[str] = None
    qq: Optional[str] = None
    phone: Optional[str] = None
    favicon: Optional[str] = None
    login_enabled: Optional[int] = None

def get_site_settings(db: Session):
    settings = db.query(SiteSettings).first()
    if not settings:
        settings = SiteSettings()
        db.add(settings)
        db.commit()
        db.refresh(settings)
    return settings

def update_site_settings(db: Session, settings_update: SiteSettingsUpdate):
    settings = get_site_settings(db)
    for key, value in settings_update.dict(exclude_unset=True).items():
        setattr(settings, key, value)
    db.commit()
    db.refresh(settings)
    return settings

def create_uploaded_file(db: Session, filename: str, original_name: str, file_path: str, file_type: str, file_size: int):
    uploaded_file = UploadedFile(
        filename=filename,
        original_name=original_name,
        file_path=file_path,
        file_type=file_type,
        file_size=file_size
    )
    db.add(uploaded_file)
    db.commit()
    db.refresh(uploaded_file)
    return uploaded_file

def get_uploaded_files(db: Session, skip: int = 0, limit: int = 100) -> tuple:
    files = db.query(UploadedFile).order_by(UploadedFile.created_at.desc()).offset(skip).limit(limit).all()
    total = db.query(UploadedFile).count()
    return files, total

def delete_uploaded_file(db: Session, file_id: int) -> Optional[UploadedFile]:
    file = db.query(UploadedFile).filter(UploadedFile.id == file_id).first()
    if file:
        db.delete(file)
        db.commit()
        return file
    return None
