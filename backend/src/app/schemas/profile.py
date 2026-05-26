from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict

class SkillCreate(BaseModel):
    name: str
    proficiency: int
    category: Optional[str] = None

class SkillResponse(BaseModel):
    id: int
    name: str
    proficiency: int
    category: Optional[str]

    class Config:
        from_attributes = True

class ExperienceCreate(BaseModel):
    title: str
    company: Optional[str] = None
    start_date: str
    end_date: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[list] = None
    order: Optional[int] = 0

class ExperienceResponse(BaseModel):
    id: int
    title: str
    company: Optional[str]
    start_date: str
    end_date: Optional[str]
    description: Optional[str]
    tags: Optional[list] = None
    order: int

    class Config:
        from_attributes = True

class EducationCreate(BaseModel):
    degree: str
    school: str
    major: Optional[str] = None
    start_date: str
    end_date: Optional[str] = None
    order: Optional[int] = 0

class EducationResponse(BaseModel):
    id: int
    degree: str
    school: str
    major: Optional[str]
    start_date: str
    end_date: Optional[str]
    order: int

    class Config:
        from_attributes = True

class ProfileResponse(BaseModel):
    bio: Optional[str]
    social_links: Optional[Dict]
    skills: List[SkillResponse]
    experiences: List[ExperienceResponse]
    education: List[EducationResponse]

class ResumeDownloadRequest(BaseModel):
    key: str