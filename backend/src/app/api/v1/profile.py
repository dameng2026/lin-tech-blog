import os
import uuid
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Query, File, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_current_user, get_current_admin
from ..v1.auth import wrap_response
from ...crud.profile import (
    get_or_create_profile, update_profile, create_skill, get_skills, update_skill, delete_skill,
    create_experience, get_experiences, update_experience, delete_experience,
    create_education, get_education, update_education, delete_education,
    set_resume_key, verify_resume_key
)
from ...schemas.profile import (
    SkillCreate, SkillResponse, ExperienceCreate, ExperienceResponse,
    EducationCreate, EducationResponse, ProfileResponse, ResumeDownloadRequest
)
from ...schemas.user import UserResponse
from ...core.database import get_db
from ...core.config import settings
from ...models.resume import Resume

router = APIRouter(prefix="/profile", tags=["profile"])

@router.get("/")
def get_profile(db: Session = Depends(get_db)):
    profile = get_or_create_profile(db, 1)
    skills = get_skills(db, profile.id)
    experiences = get_experiences(db, profile.id)
    education = get_education(db, profile.id)

    return wrap_response(data={
        "bio": profile.bio,
        "social_links": profile.social_links,
        "skills": [SkillResponse.from_orm(s).model_dump() for s in skills],
        "experiences": [ExperienceResponse.from_orm(e).model_dump() for e in experiences],
        "education": [EducationResponse.from_orm(e).model_dump() for e in education]
    })

@router.put("/")
def update_profile_info(
    bio: str = Query(None),
    social_links: dict = None,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_admin)
):
    profile = update_profile(db, current_user.id, bio, social_links)
    return wrap_response(msg="Profile updated successfully")

@router.post("/skills", dependencies=[Depends(get_current_admin)])
def add_skill(
    skill_create: SkillCreate,
    db: Session = Depends(get_db)
):
    profile = get_or_create_profile(db, 1)
    skill = create_skill(db, profile.id, skill_create)
    return wrap_response(data=SkillResponse.from_orm(skill).model_dump())

@router.get("/skills")
def list_skills(db: Session = Depends(get_db)):
    profile = get_or_create_profile(db, 1)
    skills = get_skills(db, profile.id)
    return wrap_response(data=[SkillResponse.from_orm(s).model_dump() for s in skills])

@router.put("/skills/{skill_id}", dependencies=[Depends(get_current_admin)])
def update_skill_info(
    skill_id: int,
    skill_create: SkillCreate,
    db: Session = Depends(get_db)
):
    skill = update_skill(db, skill_id, skill_create)
    return wrap_response(data=SkillResponse.from_orm(skill).model_dump())

@router.delete("/skills/{skill_id}", dependencies=[Depends(get_current_admin)])
def remove_skill(skill_id: int, db: Session = Depends(get_db)):
    delete_skill(db, skill_id)
    return wrap_response(msg="Skill deleted successfully")

@router.post("/experiences", dependencies=[Depends(get_current_admin)])
def add_experience(
    experience_create: ExperienceCreate,
    db: Session = Depends(get_db)
):
    profile = get_or_create_profile(db, 1)
    experience = create_experience(db, profile.id, experience_create)
    return wrap_response(data=ExperienceResponse.from_orm(experience).model_dump())

@router.get("/experiences")
def list_experiences(db: Session = Depends(get_db)):
    profile = get_or_create_profile(db, 1)
    experiences = get_experiences(db, profile.id)
    return wrap_response(data=[ExperienceResponse.from_orm(e).model_dump() for e in experiences])

@router.put("/experiences/{experience_id}", dependencies=[Depends(get_current_admin)])
def update_experience_info(
    experience_id: int,
    experience_create: ExperienceCreate,
    db: Session = Depends(get_db)
):
    experience = update_experience(db, experience_id, experience_create)
    return wrap_response(data=ExperienceResponse.from_orm(experience).model_dump())

@router.delete("/experiences/{experience_id}", dependencies=[Depends(get_current_admin)])
def remove_experience(experience_id: int, db: Session = Depends(get_db)):
    delete_experience(db, experience_id)
    return wrap_response(msg="Experience deleted successfully")

@router.post("/education", dependencies=[Depends(get_current_admin)])
def add_education(
    education_create: EducationCreate,
    db: Session = Depends(get_db)
):
    profile = get_or_create_profile(db, 1)
    education = create_education(db, profile.id, education_create)
    return wrap_response(data=EducationResponse.from_orm(education).model_dump())

@router.get("/education")
def list_education(db: Session = Depends(get_db)):
    profile = get_or_create_profile(db, 1)
    education = get_education(db, profile.id)
    return wrap_response(data=[EducationResponse.from_orm(e).model_dump() for e in education])

@router.put("/education/{education_id}", dependencies=[Depends(get_current_admin)])
def update_education_info(
    education_id: int,
    education_create: EducationCreate,
    db: Session = Depends(get_db)
):
    education = update_education(db, education_id, education_create)
    return wrap_response(data=EducationResponse.from_orm(education).model_dump())

@router.delete("/education/{education_id}", dependencies=[Depends(get_current_admin)])
def remove_education(education_id: int, db: Session = Depends(get_db)):
    delete_education(db, education_id)
    return wrap_response(msg="Education deleted successfully")

@router.post("/resume/key", dependencies=[Depends(get_current_admin)])
def set_download_key(key: str, db: Session = Depends(get_db)):
    set_resume_key(db, 1, key)
    return wrap_response(msg="Resume key set successfully")

@router.post("/resume/download")
def download_resume(request: ResumeDownloadRequest, db: Session = Depends(get_db)):
    if not verify_resume_key(db, 1, request.key):
        raise HTTPException(status_code=401, detail="Invalid download key")

    return wrap_response(data={"message": "Resume download link generated"})


@router.post("/resume/upload")
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin)
):
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="只允许上传PDF文件")

    if file.size and file.size > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="文件大小不能超过10MB")

    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

    old_resume = db.query(Resume).first()
    if old_resume:
        old_path = os.path.join(settings.UPLOAD_DIR, old_resume.filename)
        if os.path.exists(old_path):
            os.remove(old_path)
        db.delete(old_resume)
        db.commit()

    filename = f"resume_{uuid.uuid4()}.pdf"
    file_path = os.path.join(settings.UPLOAD_DIR, filename)
    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)

    resume = Resume(
        filename=filename,
        original_name=file.filename,
        file_size=file.size or 0,
        is_active=True,
        created_at=datetime.now()
    )
    db.add(resume)
    db.commit()
    db.refresh(resume)

    return wrap_response(data={
        "id": resume.id,
        "filename": resume.filename,
        "original_name": resume.original_name,
        "file_size": resume.file_size,
        "is_active": resume.is_active,
        "created_at": resume.created_at.isoformat()
    }, msg="简历上传成功")


@router.get("/resume/info")
def get_resume_info(db: Session = Depends(get_db)):
    resume = db.query(Resume).first()
    if not resume:
        return wrap_response(data={"exists": False})
    return wrap_response(data={
        "exists": True,
        "id": resume.id,
        "filename": resume.filename,
        "original_name": resume.original_name,
        "file_size": resume.file_size,
        "is_active": resume.is_active,
        "created_at": resume.created_at.isoformat()
    })


@router.put("/resume/{resume_id}/toggle")
def toggle_resume_status(resume_id: int, db: Session = Depends(get_db)):
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="简历不存在")
    resume.is_active = not resume.is_active
    db.commit()
    return wrap_response(data={"is_active": resume.is_active}, msg="状态已更新")


@router.delete("/resume/{resume_id}")
def delete_resume(resume_id: int, db: Session = Depends(get_db)):
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="简历不存在")
    file_path = os.path.join(settings.UPLOAD_DIR, resume.filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    db.delete(resume)
    db.commit()
    return wrap_response(data={"message": "简历删除成功"})


@router.get("/resume/download")
def download_resume_pdf(db: Session = Depends(get_db)):
    resume = db.query(Resume).first()
    if not resume:
        raise HTTPException(status_code=404, detail="简历不存在")
    if not resume.is_active:
        raise HTTPException(status_code=403, detail="简历暂时不可下载，请联系管理员了解详情")

    file_path = os.path.join(settings.UPLOAD_DIR, resume.filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="简历文件不存在")

    return FileResponse(file_path, filename=resume.original_name, media_type="application/pdf")