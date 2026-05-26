from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.taxonomy import Category, Tag
from pydantic import BaseModel, Field

class CategoryCreate(BaseModel):
    name: str = Field(..., max_length=50)
    description: Optional[str] = Field(None, max_length=500)

class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = Field(None, max_length=500)
    is_active: Optional[bool] = None

class TagCreate(BaseModel):
    name: str
    slug: str

class TagUpdate(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    is_active: Optional[bool] = None

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session, skip: int = 0, limit: int = 100, include_inactive: bool = False) -> tuple:
    query = db.query(Category)
    if not include_inactive:
        query = query.filter(Category.is_active == True)
    categories = query.order_by(Category.id).offset(skip).limit(limit).all()
    total = query.count()
    return categories, total

def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def update_category(db: Session, category_id: int, category_update: CategoryUpdate):
    db_category = get_category_by_id(db, category_id)
    if not db_category:
        return None
    for key, value in category_update.dict(exclude_unset=True).items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category

def toggle_category_status(db: Session, category_id: int):
    db_category = get_category_by_id(db, category_id)
    if not db_category:
        return None
    db_category.is_active = not db_category.is_active
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = get_category_by_id(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False

def create_tag(db: Session, tag: TagCreate):
    db_tag = Tag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def get_tags(db: Session, skip: int = 0, limit: int = 100) -> tuple:
    tags = db.query(Tag).order_by(Tag.name).offset(skip).limit(limit).all()
    total = db.query(Tag).count()
    return tags, total

def get_tag_by_id(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()

def get_tag_by_slug(db: Session, slug: str):
    return db.query(Tag).filter(Tag.slug == slug).first()

def update_tag(db: Session, tag_id: int, tag_update: TagUpdate):
    db_tag = get_tag_by_id(db, tag_id)
    if not db_tag:
        return None
    for key, value in tag_update.dict(exclude_unset=True).items():
        setattr(db_tag, key, value)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def delete_tag(db: Session, tag_id: int):
    db_tag = get_tag_by_id(db, tag_id)
    if db_tag:
        db.delete(db_tag)
        db.commit()
        return True
    return False
