from sqlalchemy.orm import Session
from typing import Optional
from ..models.project_category import ProjectCategory
from pydantic import BaseModel, Field

class ProjectCategoryCreate(BaseModel):
    name: str = Field(..., max_length=50)
    description: Optional[str] = Field(None, max_length=500)

class ProjectCategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = Field(None, max_length=500)
    is_active: Optional[bool] = None

def create_project_category(db: Session, category: ProjectCategoryCreate):
    db_category = ProjectCategory(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_project_categories(db: Session, skip: int = 0, limit: int = 100, include_inactive: bool = False) -> tuple:
    query = db.query(ProjectCategory)
    if not include_inactive:
        query = query.filter(ProjectCategory.is_active == True)
    categories = query.order_by(ProjectCategory.id).offset(skip).limit(limit).all()
    total = query.count()
    return categories, total

def get_project_category_by_id(db: Session, category_id: int):
    return db.query(ProjectCategory).filter(ProjectCategory.id == category_id).first()

def update_project_category(db: Session, category_id: int, category_update: ProjectCategoryUpdate):
    db_category = get_project_category_by_id(db, category_id)
    if not db_category:
        return None
    for key, value in category_update.dict(exclude_unset=True).items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category

def toggle_project_category_status(db: Session, category_id: int):
    db_category = get_project_category_by_id(db, category_id)
    if not db_category:
        return None
    db_category.is_active = not db_category.is_active
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_project_category(db: Session, category_id: int):
    db_category = get_project_category_by_id(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False