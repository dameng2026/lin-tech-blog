from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from ..dependencies import get_current_admin
from .auth import wrap_response
from ...crud.friend_link import (
    create_friend_link, get_friend_link_by_id, get_friend_links, update_friend_link, delete_friend_link, get_category_stats
)
from ...schemas.friend_link import FriendLinkCreate, FriendLinkUpdate, FriendLinkResponse
from ...core.database import get_db

router = APIRouter(prefix="/friend-links", tags=["friend_links"])

@router.get("/")
def list_friend_links(
    status: Optional[str] = Query("approved"),
    category: Optional[str] = None,
    page: int = Query(1, ge=1),
    size: int = Query(12, ge=1, le=50),
    db: Session = Depends(get_db)
):
    friend_links, total = get_friend_links(db, status=status, category=category, page=page, size=size)
    return wrap_response(data={
        "friend_links": [FriendLinkResponse.model_validate(fl).model_dump() for fl in friend_links],
        "total": total,
        "page": page,
        "size": size
    })

@router.get("/stats")
def get_friend_link_stats(
    status: Optional[str] = Query("approved"),
    db: Session = Depends(get_db)
):
    stats = get_category_stats(db, status)
    return wrap_response(data=stats)

@router.get("/admin", dependencies=[Depends(get_current_admin)])
def list_all_friend_links(
    status: Optional[str] = None,
    category: Optional[str] = None,
    name: Optional[str] = None,
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    friend_links, total = get_friend_links(db, status, category, name, page, size)
    return wrap_response(data={
        "records": [FriendLinkResponse.model_validate(fl).model_dump() for fl in friend_links],
        "total": total,
        "current": page,
        "size": size
    })

@router.post("/apply")
def apply_friend_link(friend_link_create: FriendLinkCreate, db: Session = Depends(get_db)):
    friend_link = create_friend_link(db, friend_link_create)
    return wrap_response(data={"message": "Friend link application submitted", "id": friend_link.id})

@router.get("/categories")
def get_friend_link_categories(db: Session = Depends(get_db)):
    from ...models.friend_link_category import FriendLinkCategory
    categories = db.query(FriendLinkCategory.name).filter(FriendLinkCategory.is_active == True).all()
    return wrap_response(data={"categories": [c[0] for c in categories if c[0]]})

@router.put("/{friend_link_id}/approve", dependencies=[Depends(get_current_admin)])
def approve_friend_link(friend_link_id: int, db: Session = Depends(get_db)):
    friend_link = update_friend_link(db, friend_link_id, FriendLinkUpdate(status="approved"))
    return wrap_response(data=FriendLinkResponse.model_validate(friend_link).model_dump())

@router.put("/{friend_link_id}/reject", dependencies=[Depends(get_current_admin)])
def reject_friend_link(friend_link_id: int, db: Session = Depends(get_db)):
    friend_link = update_friend_link(db, friend_link_id, FriendLinkUpdate(status="rejected"))
    return wrap_response(data=FriendLinkResponse.model_validate(friend_link).model_dump())

@router.put("/{friend_link_id}/pause", dependencies=[Depends(get_current_admin)])
def pause_friend_link(friend_link_id: int, db: Session = Depends(get_db)):
    friend_link = update_friend_link(db, friend_link_id, FriendLinkUpdate(status="paused"))
    return wrap_response(data=FriendLinkResponse.model_validate(friend_link).model_dump())

@router.put("/{friend_link_id}/resume", dependencies=[Depends(get_current_admin)])
def resume_friend_link(friend_link_id: int, db: Session = Depends(get_db)):
    friend_link = update_friend_link(db, friend_link_id, FriendLinkUpdate(status="approved"))
    return wrap_response(data=FriendLinkResponse.model_validate(friend_link).model_dump())

@router.put("/{friend_link_id}", dependencies=[Depends(get_current_admin)])
def update_friend_link_status(
    friend_link_id: int,
    friend_link_update: FriendLinkUpdate,
    db: Session = Depends(get_db)
):
    friend_link = update_friend_link(db, friend_link_id, friend_link_update)
    return wrap_response(data=FriendLinkResponse.model_validate(friend_link).model_dump())

@router.delete("/{friend_link_id}", dependencies=[Depends(get_current_admin)])
def delete_existing_friend_link(friend_link_id: int, db: Session = Depends(get_db)):
    delete_friend_link(db, friend_link_id)
    return wrap_response(data={"message": "Friend link deleted successfully"})
