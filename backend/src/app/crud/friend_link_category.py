from sqlalchemy.orm import Session
from typing import Optional
from ..models.friend_link_category import FriendLinkCategory
from pydantic import BaseModel, Field

class FriendLinkCategoryCreate(BaseModel):
    name: str = Field(..., max_length=50)
    description: Optional[str] = Field(None, max_length=500)

class FriendLinkCategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = Field(None, max_length=500)
    is_active: Optional[bool] = None

def create_friend_link_category(db: Session, category: FriendLinkCategoryCreate):
    db_category = FriendLinkCategory(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_friend_link_categories(db: Session, skip: int = 0, limit: int = 100, include_inactive: bool = False) -> tuple:
    query = db.query(FriendLinkCategory)
    if not include_inactive:
        query = query.filter(FriendLinkCategory.is_active == True)
    categories = query.order_by(FriendLinkCategory.id).offset(skip).limit(limit).all()
    total = query.count()
    return categories, total

def get_friend_link_category_by_id(db: Session, category_id: int):
    return db.query(FriendLinkCategory).filter(FriendLinkCategory.id == category_id).first()

def update_friend_link_category(db: Session, category_id: int, category_update: FriendLinkCategoryUpdate):
    db_category = get_friend_link_category_by_id(db, category_id)
    if not db_category:
        return None
    for key, value in category_update.dict(exclude_unset=True).items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category

def toggle_friend_link_category_status(db: Session, category_id: int):
    db_category = get_friend_link_category_by_id(db, category_id)
    if not db_category:
        return None
    db_category.is_active = not db_category.is_active
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_friend_link_category(db: Session, category_id: int):
    db_category = get_friend_link_category_by_id(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False