from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from ..dependencies import get_current_admin
from .auth import wrap_response
from ...crud.friend_link_category import (
    create_friend_link_category, get_friend_link_categories, get_friend_link_category_by_id,
    update_friend_link_category, delete_friend_link_category, toggle_friend_link_category_status
)
from ...schemas.friend_link_category import (
    FriendLinkCategoryCreate, FriendLinkCategoryUpdate, FriendLinkCategoryResponse
)
from ...core.database import get_db

router = APIRouter(prefix="/friend-link-categories", tags=["friend-link-categories"])

@router.get("/")
def list_friend_link_categories(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1),
    include_inactive: bool = Query(False, description="是否包含已暂停的分类"),
    db: Session = Depends(get_db)
):
    categories, _ = get_friend_link_categories(db, skip, limit, include_inactive)
    return wrap_response(data=categories)

@router.post("/", dependencies=[Depends(get_current_admin)])
def create_new_friend_link_category(category: FriendLinkCategoryCreate, db: Session = Depends(get_db)):
    return wrap_response(data=create_friend_link_category(db, category))

@router.put("/{category_id}", dependencies=[Depends(get_current_admin)])
def update_existing_friend_link_category(category_id: int, category_update: FriendLinkCategoryUpdate, db: Session = Depends(get_db)):
    category = update_friend_link_category(db, category_id, category_update)
    if not category:
        return {"code": 404, "msg": "友链分类不存在", "data": None}
    return wrap_response(data=category)

@router.patch("/{category_id}/toggle-status", dependencies=[Depends(get_current_admin)])
def toggle_friend_link_category(category_id: int, db: Session = Depends(get_db)):
    category = toggle_friend_link_category_status(db, category_id)
    if not category:
        return {"code": 404, "msg": "友链分类不存在", "data": None}
    status_text = "已启用" if category.is_active else "已暂停"
    return wrap_response(data={"id": category.id, "is_active": category.is_active}, msg=status_text)

@router.delete("/{category_id}", dependencies=[Depends(get_current_admin)])
def delete_existing_friend_link_category(category_id: int, db: Session = Depends(get_db)):
    category = get_friend_link_category_by_id(db, category_id)
    if not category:
        return {"code": 404, "msg": "友链分类不存在", "data": None}
    delete_friend_link_category(db, category_id)
    return wrap_response(data={"id": category_id}, msg="删除成功")