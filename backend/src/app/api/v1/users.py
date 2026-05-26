from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import datetime
from ..dependencies import get_current_admin
from ...crud.user import get_user_by_id, update_user, delete_user
from ...models.user import User
from ...schemas.user import UserResponse, UserUpdate
from ...core.database import get_db
from .auth import wrap_response
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])

class UserListResponse(BaseModel):
    users: List[UserResponse]
    total: int
    page: int
    size: int

class AdminUserUpdate(BaseModel):
    nickname: Optional[str] = None
    avatar: Optional[str] = None
    bio: Optional[str] = None
    city: Optional[str] = None
    social_links: Optional[str] = None
    is_active: Optional[bool] = None
    role: Optional[str] = None

@router.get("/")
def list_users(
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
    userName: Optional[str] = None,
    userEmail: Optional[str] = None,
    status: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(User)
    
    if userName:
        query = query.filter(User.username.like(f"%{userName}%"))
    if userEmail:
        query = query.filter(User.email.like(f"%{userEmail}%"))
    if status:
        is_active = status == "active"
        query = query.filter(User.is_active == is_active)
    
    total = query.count()
    users = query.order_by(User.created_at.desc()).offset((page - 1) * size).limit(size).all()
    
    return wrap_response(data={
        "users": [UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            nickname=user.nickname,
            avatar=user.avatar,
            bio=user.bio,
            city=user.city,
            social_links=user.social_links,
            role=user.role,
            is_active=user.is_active,
            created_at=user.created_at
        ).model_dump() for user in users],
        "total": total,
        "page": page,
        "size": size
    })

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    return wrap_response(data=UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        nickname=user.nickname,
        avatar=user.avatar,
        bio=user.bio,
        city=user.city,
        social_links=user.social_links,
        role=user.role,
        is_active=user.is_active,
        created_at=user.created_at
    ).model_dump())

@router.put("/{user_id}", dependencies=[Depends(get_current_admin)])
def update_existing_user(
    user_id: int,
    user_update: AdminUserUpdate,
    db: Session = Depends(get_db)
):
    db_user = get_user_by_id(db, user_id)
    
    update_data = user_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    
    db.commit()
    db.refresh(db_user)
    
    return wrap_response(data=UserResponse(
        id=db_user.id,
        username=db_user.username,
        email=db_user.email,
        nickname=db_user.nickname,
        avatar=db_user.avatar,
        bio=db_user.bio,
        city=db_user.city,
        social_links=db_user.social_links,
        role=db_user.role,
        is_active=db_user.is_active,
        created_at=db_user.created_at
    ).model_dump())

@router.delete("/{user_id}", dependencies=[Depends(get_current_admin)])
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    delete_user(db, user_id)
    return wrap_response(data={"message": "User deleted successfully"})

@router.post("/{user_id}/reset-password", dependencies=[Depends(get_current_admin)])
def reset_user_password(user_id: int, db: Session = Depends(get_db)):
    from ...security.password import get_password_hash
    user = get_user_by_id(db, user_id)
    new_password_hash = get_password_hash("123456")
    user.password_hash = new_password_hash
    db.commit()
    return wrap_response(data={"message": "Password reset successfully", "new_password": "123456"})

@router.post("/{user_id}/toggle-status", dependencies=[Depends(get_current_admin)])
def toggle_user_status(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    user.is_active = not user.is_active
    db.commit()
    return wrap_response(data={"message": "Status toggled successfully", "is_active": user.is_active})
