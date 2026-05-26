from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from typing import Optional, Tuple, List
from ..models.friend_link import FriendLink
from ..schemas.friend_link import FriendLinkCreate, FriendLinkUpdate

def create_friend_link(db: Session, friend_link_create: FriendLinkCreate) -> FriendLink:
    friend_link = FriendLink(
        name=friend_link_create.name,
        url=friend_link_create.url,
        logo=friend_link_create.logo,
        description=friend_link_create.description,
        category=friend_link_create.category,
        status="pending"
    )
    db.add(friend_link)
    db.commit()
    db.refresh(friend_link)
    return friend_link

def get_friend_link_by_id(db: Session, friend_link_id: int) -> FriendLink:
    friend_link = db.query(FriendLink).filter(FriendLink.id == friend_link_id).first()
    if not friend_link:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Friend link not found")
    return friend_link

def get_friend_links(
    db: Session,
    status: Optional[str] = None,
    category: Optional[str] = None,
    name: Optional[str] = None,
    page: int = 1,
    size: int = 12
) -> Tuple[List[FriendLink], int]:
    query = db.query(FriendLink)
    if status:
        query = query.filter(FriendLink.status == status)
    if category:
        query = query.filter(FriendLink.category == category)
    if name:
        query = query.filter(FriendLink.name.ilike(f"%{name}%"))
    total = query.count()
    friend_links = query.order_by(desc(FriendLink.created_at)).offset((page - 1) * size).limit(size).all()
    return friend_links, total

def get_category_stats(db: Session, status: Optional[str] = "approved") -> dict:
    query = db.query(FriendLink.category, func.count(FriendLink.id))
    if status:
        query = query.filter(FriendLink.status == status)
    results = query.group_by(FriendLink.category).all()
    stats = {}
    total = 0
    for category, count in results:
        stats[category] = count
        total += count
    stats["全部友链"] = total
    return stats

def update_friend_link(db: Session, friend_link_id: int, friend_link_update: FriendLinkUpdate) -> FriendLink:
    friend_link = get_friend_link_by_id(db, friend_link_id)
    if friend_link_update.name is not None:
        friend_link.name = friend_link_update.name
    if friend_link_update.url is not None:
        friend_link.url = friend_link_update.url
    if friend_link_update.logo is not None:
        friend_link.logo = friend_link_update.logo
    if friend_link_update.description is not None:
        friend_link.description = friend_link_update.description
    if friend_link_update.category is not None:
        friend_link.category = friend_link_update.category
    if friend_link_update.status is not None:
        friend_link.status = friend_link_update.status
    db.commit()
    db.refresh(friend_link)
    return friend_link

def delete_friend_link(db: Session, friend_link_id: int) -> None:
    friend_link = get_friend_link_by_id(db, friend_link_id)
    db.delete(friend_link)
    db.commit()
