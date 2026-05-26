from sqlalchemy.orm import Session
from sqlalchemy import desc
from ..models.profile import Profile, Skill, Experience, Education, ResumeKey
from ..schemas.profile import SkillCreate, ExperienceCreate, EducationCreate
from ..security.password import get_password_hash, verify_password
from fastapi import HTTPException, status

def get_or_create_profile(db: Session, user_id: int) -> Profile:
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()
    if not profile:
        profile = Profile(user_id=user_id)
        db.add(profile)
        db.commit()
        db.refresh(profile)
    return profile

def update_profile(db: Session, user_id: int, bio: str = None, social_links: dict = None) -> Profile:
    profile = get_or_create_profile(db, user_id)
    if bio is not None:
        profile.bio = bio
    if social_links is not None:
        profile.social_links = social_links
    db.commit()
    db.refresh(profile)
    return profile

def create_skill(db: Session, profile_id: int, skill_create: SkillCreate) -> Skill:
    skill = Skill(
        profile_id=profile_id,
        name=skill_create.name,
        proficiency=skill_create.proficiency,
        category=skill_create.category
    )
    db.add(skill)
    db.commit()
    db.refresh(skill)
    return skill

def get_skills(db: Session, profile_id: int) -> list:
    return db.query(Skill).filter(Skill.profile_id == profile_id).all()

def update_skill(db: Session, skill_id: int, skill_create: SkillCreate) -> Skill:
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Skill not found")
    skill.name = skill_create.name
    skill.proficiency = skill_create.proficiency
    skill.category = skill_create.category
    db.commit()
    db.refresh(skill)
    return skill

def delete_skill(db: Session, skill_id: int) -> None:
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Skill not found")
    db.delete(skill)
    db.commit()

def create_experience(db: Session, profile_id: int, experience_create: ExperienceCreate) -> Experience:
    experience = Experience(
        profile_id=profile_id,
        title=experience_create.title,
        company=experience_create.company,
        start_date=experience_create.start_date,
        end_date=experience_create.end_date,
        description=experience_create.description,
        tags=experience_create.tags or [],
        order=experience_create.order
    )
    db.add(experience)
    db.commit()
    db.refresh(experience)
    return experience

def get_experiences(db: Session, profile_id: int) -> list:
    return db.query(Experience).filter(Experience.profile_id == profile_id).order_by(Experience.order).all()

def update_experience(db: Session, experience_id: int, experience_create: ExperienceCreate) -> Experience:
    experience = db.query(Experience).filter(Experience.id == experience_id).first()
    if not experience:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found")
    experience.title = experience_create.title
    experience.company = experience_create.company
    experience.start_date = experience_create.start_date
    experience.end_date = experience_create.end_date
    experience.description = experience_create.description
    experience.tags = experience_create.tags or []
    experience.order = experience_create.order
    db.commit()
    db.refresh(experience)
    return experience

def delete_experience(db: Session, experience_id: int) -> None:
    experience = db.query(Experience).filter(Experience.id == experience_id).first()
    if not experience:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found")
    db.delete(experience)
    db.commit()

def create_education(db: Session, profile_id: int, education_create: EducationCreate) -> Education:
    education = Education(
        profile_id=profile_id,
        degree=education_create.degree,
        school=education_create.school,
        major=education_create.major,
        start_date=education_create.start_date,
        end_date=education_create.end_date,
        order=education_create.order
    )
    db.add(education)
    db.commit()
    db.refresh(education)
    return education

def get_education(db: Session, profile_id: int) -> list:
    return db.query(Education).filter(Education.profile_id == profile_id).order_by(Education.order).all()

def update_education(db: Session, education_id: int, education_create: EducationCreate) -> Education:
    education = db.query(Education).filter(Education.id == education_id).first()
    if not education:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Education not found")
    education.degree = education_create.degree
    education.school = education_create.school
    education.major = education_create.major
    education.start_date = education_create.start_date
    education.end_date = education_create.end_date
    education.order = education_create.order
    db.commit()
    db.refresh(education)
    return education

def delete_education(db: Session, education_id: int) -> None:
    education = db.query(Education).filter(Education.id == education_id).first()
    if not education:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Education not found")
    db.delete(education)
    db.commit()

def set_resume_key(db: Session, user_id: int, key: str) -> None:
    resume_key = db.query(ResumeKey).filter(ResumeKey.user_id == user_id).first()
    if resume_key:
        resume_key.key_hash = get_password_hash(key)
    else:
        resume_key = ResumeKey(user_id=user_id, key_hash=get_password_hash(key))
        db.add(resume_key)
    db.commit()

def verify_resume_key(db: Session, user_id: int, key: str) -> bool:
    resume_key = db.query(ResumeKey).filter(ResumeKey.user_id == user_id).first()
    if not resume_key:
        return False
    return verify_password(key, resume_key.key_hash)