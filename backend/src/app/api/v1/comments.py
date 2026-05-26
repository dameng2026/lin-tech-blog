from fastapi import APIRouter, Depends, Query, Request, HTTPException
from sqlalchemy.orm import Session
from typing import Optional, List
from ..dependencies import get_current_admin, get_current_admin_optional
from ...crud.comment import (
    create_comment, delete_comment, toggle_comment_like,
    update_guestbook, delete_guestbook,
    get_comments_by_article, get_comments_by_project, get_all_comments,
    get_guestbook_messages, create_guestbook_message
)
from ...crud.user import get_user_by_id
from ...models.comment import Comment, Guestbook
from ...schemas.comment import CommentCreate, CommentResponse as CommentSchema
from ...schemas.guestbook import GuestbookResponse
from ...core.database import get_db
from ...services.content_filter import check_content, get_client_ip, check_rate_limit
from pydantic import BaseModel
from .auth import wrap_response

router = APIRouter(prefix="/comments", tags=["comments"])

class CommentListResponse(BaseModel):
    comments: List[CommentSchema]
    total: int
    page: int
    size: int

    class Config:
        from_attributes = True

def _build_comment_response(comment: Comment, db: Session, depth: int = 0) -> CommentSchema:
    if depth > 10:
        return CommentSchema(
            id=comment.id, article_id=comment.article_id, project_id=comment.project_id,
            user_id=comment.user_id, username='', content='[递归深度超限]',
            parent_id=comment.parent_id, like_count=0, replies=[], created_at=comment.created_at,
            is_approved=comment.is_approved
        )
    if comment.user_id:
        user = get_user_by_id(db, comment.user_id)
        username = user.username if user else "Unknown"
        avatar = user.avatar if user else None
    else:
        username = comment.guest_name or "游客"
        avatar = None

    content_type = 'article' if comment.article_id else ('project' if comment.project_id else None)
    content_id = comment.article_id or comment.project_id
    content_title = ''

    if comment.article_id:
        from ...models.article import Article
        article = db.query(Article).filter(Article.id == comment.article_id).first()
        content_title = article.title if article else ''
    elif comment.project_id:
        from ...models.project import Project
        project = db.query(Project).filter(Project.id == comment.project_id).first()
        content_title = project.name if project else ''

    replies_data = []
    approved_replies = db.query(Comment).filter(
        Comment.parent_id == comment.id,
        Comment.is_approved == True
    ).all()
    for reply in approved_replies:
        replies_data.append(_build_comment_response(reply, db, depth + 1))

    return CommentSchema(
        id=comment.id,
        article_id=comment.article_id,
        project_id=comment.project_id,
        user_id=comment.user_id,
        username=username,
        avatar=avatar,
        guest_name=comment.guest_name,
        content=comment.content,
        parent_id=comment.parent_id,
        reply_to_id=comment.reply_to_id,
        reply_to_name=comment.reply_to_name,
        like_count=comment.like_count,
        replies=replies_data,
        created_at=comment.created_at,
        is_approved=comment.is_approved,
        content_type=content_type,
        content_id=content_id,
        content_title=content_title
    )

@router.get("/")
def list_all_comments(
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
    content: Optional[str] = None,
    article_id: Optional[int] = None,
    project_id: Optional[int] = None,
    status: Optional[str] = None,
    type: Optional[str] = None,
    db: Session = Depends(get_db)
):
    from ...models.article import Article
    from ...models.project import Project

    comments, total = get_all_comments(db, page, size, content, article_id, project_id, status, type)

    article_cache: dict[int, str] = {}
    project_cache: dict[int, str] = {}

    result = []
    for comment in comments:
        if comment.user_id:
            user = get_user_by_id(db, comment.user_id)
            username = user.username if user else "Unknown"
            avatar = user.avatar if user else None
        else:
            username = comment.guest_name or "游客"
            avatar = None

        content_type = 'article' if comment.article_id else ('project' if comment.project_id else None)
        content_id = comment.article_id or comment.project_id
        content_title = ''

        if comment.article_id:
            if comment.article_id in article_cache:
                content_title = article_cache[comment.article_id]
            else:
                article = db.query(Article).filter(Article.id == comment.article_id).first()
                content_title = article.title if article else ''
                article_cache[comment.article_id] = content_title
        elif comment.project_id:
            if comment.project_id in project_cache:
                content_title = project_cache[comment.project_id]
            else:
                project = db.query(Project).filter(Project.id == comment.project_id).first()
                content_title = project.name if project else ''
                project_cache[comment.project_id] = content_title

        result.append(CommentSchema(
            id=comment.id,
            article_id=comment.article_id,
            project_id=comment.project_id,
            user_id=comment.user_id,
            username=username,
            avatar=avatar,
            guest_name=comment.guest_name,
            content=comment.content,
            parent_id=comment.parent_id,
            like_count=comment.like_count,
            is_approved=comment.is_approved,
            created_at=comment.created_at,
            replies=[],
            content_type=content_type,
            content_id=content_id,
            content_title=content_title
        ).model_dump())

    return wrap_response(data={
        "comments": result,
        "total": total,
        "page": page,
        "size": size
    })

@router.get("/article/{article_id}")
def get_article_comments(
    article_id: int,
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=50),
    sort: str = Query("newest", regex="^(newest|hottest)$"),
    db: Session = Depends(get_db)
):
    parent_comments, total = get_comments_by_article(db, article_id, page, size, sort)
    result = [_build_comment_response(c, db).model_dump() for c in parent_comments]

    return wrap_response(data={
        "comments": result,
        "total": total,
        "page": page,
        "size": size
    })

@router.post("/article/{article_id}")
def create_new_comment(
    article_id: int,
    comment_data: CommentCreate,
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_optional)
):
    user_id = current_user.id if current_user else None
    ip_address = get_client_ip(request)
    guest_name = comment_data.guest_name

    passed, message = check_content(comment_data.content, db)
    if not passed:
        raise HTTPException(status_code=422, detail=message)

    rate_passed, rate_message = check_rate_limit(ip_address)
    if not rate_passed:
        raise HTTPException(status_code=429, detail=rate_message)

    if not user_id and not guest_name:
        raise HTTPException(status_code=422, detail="请提供评论者名称")

    comment = create_comment(db, article_id, None, user_id, comment_data, ip_address)

    if user_id:
        user = get_user_by_id(db, user_id)
        username = user.username if user else "Unknown"
        avatar = user.avatar if user else None
    else:
        username = guest_name or "游客"
        avatar = None

    return wrap_response(data=CommentSchema(
        id=comment.id,
        article_id=comment.article_id,
        user_id=comment.user_id,
        username=username,
        avatar=avatar,
        guest_name=comment.guest_name,
        content=comment.content,
        parent_id=comment.parent_id,
        like_count=comment.like_count,
        replies=[],
        created_at=comment.created_at,
        is_approved=comment.is_approved
    ).model_dump())

@router.get("/project/{project_id}")
def get_project_comments(
    project_id: int,
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=50),
    sort: str = Query("newest", regex="^(newest|hottest)$"),
    db: Session = Depends(get_db)
):
    parent_comments, total = get_comments_by_project(db, project_id, page, size, sort)
    result = [_build_comment_response(c, db).model_dump() for c in parent_comments]

    return wrap_response(data={
        "comments": result,
        "total": total,
        "page": page,
        "size": size
    })

@router.post("/project/{project_id}")
def create_project_comment(
    project_id: int,
    comment_data: CommentCreate,
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_optional)
):
    user_id = current_user.id if current_user else None
    ip_address = get_client_ip(request)
    guest_name = comment_data.guest_name

    passed, message = check_content(comment_data.content, db)
    if not passed:
        raise HTTPException(status_code=422, detail=message)

    rate_passed, rate_message = check_rate_limit(ip_address)
    if not rate_passed:
        raise HTTPException(status_code=429, detail=rate_message)

    if not user_id and not guest_name:
        raise HTTPException(status_code=422, detail="请提供评论者名称")

    comment = create_comment(db, None, project_id, user_id, comment_data, ip_address)

    if user_id:
        user = get_user_by_id(db, user_id)
        username = user.username if user else "Unknown"
        avatar = user.avatar if user else None
    else:
        username = guest_name or "游客"
        avatar = None

    return wrap_response(data=CommentSchema(
        id=comment.id,
        article_id=comment.article_id,
        project_id=comment.project_id,
        user_id=comment.user_id,
        username=username,
        avatar=avatar,
        guest_name=comment.guest_name,
        content=comment.content,
        parent_id=comment.parent_id,
        like_count=comment.like_count,
        replies=[],
        created_at=comment.created_at,
        is_approved=comment.is_approved
    ).model_dump())

@router.get("/guestbook")
def get_all_guestbooks(db: Session = Depends(get_db)):
    from ...crud.comment import get_guestbooks
    guestbooks = get_guestbooks(db)
    result = []
    for guestbook in guestbooks:
        user = get_user_by_id(db, guestbook.user_id)
        result.append(GuestbookResponse(
            id=guestbook.id,
            user_id=guestbook.user_id,
            username=user.username if user else "Unknown",
            avatar=user.avatar if user else None,
            content=guestbook.content,
            is_top=guestbook.is_top,
            reply=guestbook.reply,
            created_at=guestbook.created_at
        ).model_dump())
    return wrap_response(data=result)

@router.get("/guestbook/messages")
def get_guestbook_message_list(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=50),
    sort: str = Query("newest", regex="^(newest|hottest)$"),
    db: Session = Depends(get_db)
):
    parent_comments, total = get_guestbook_messages(db, page, size, sort)
    result = []
    for c in parent_comments:
        comment_data = _build_comment_response(c, db).model_dump()
        comment_data['ip_address'] = c.ip_address
        comment_data['guest_email'] = c.guest_email
        result.append(comment_data)
    return wrap_response(data={"comments": result, "total": total, "page": page, "size": size})

@router.post("/guestbook/messages")
def create_guestbook_comment(
    comment_data: CommentCreate,
    request: Request,
    db: Session = Depends(get_db)
):
    ip_address = get_client_ip(request)

    passed, message = check_content(comment_data.content, db)
    if not passed:
        raise HTTPException(status_code=422, detail=message)

    rate_passed, rate_message = check_rate_limit(ip_address)
    if not rate_passed:
        raise HTTPException(status_code=429, detail=rate_message)

    if not comment_data.guest_name:
        raise HTTPException(status_code=422, detail="请输入留言者名称")

    comment = create_guestbook_message(db, comment_data, ip_address)
    username = comment.guest_name or "游客"

    return wrap_response(data=CommentSchema(
        id=comment.id,
        user_id=comment.user_id,
        username=username,
        guest_name=comment.guest_name,
        content=comment.content,
        parent_id=comment.parent_id,
        reply_to_id=comment.reply_to_id,
        reply_to_name=comment.reply_to_name,
        like_count=comment.like_count,
        replies=[],
        created_at=comment.created_at,
        is_approved=comment.is_approved
    ).model_dump())

@router.put("/guestbook/{guestbook_id}", dependencies=[Depends(get_current_admin)])
def update_existing_guestbook(
    guestbook_id: int,
    reply: Optional[str] = None,
    is_top: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    guestbook = update_guestbook(db, guestbook_id, reply, is_top)
    user = get_user_by_id(db, guestbook.user_id)
    return wrap_response(data=GuestbookResponse(
        id=guestbook.id,
        user_id=guestbook.user_id,
        username=user.username if user else "Unknown",
        avatar=user.avatar if user else None,
        content=guestbook.content,
        is_top=guestbook.is_top,
        reply=guestbook.reply,
        created_at=guestbook.created_at
    ).model_dump())

@router.delete("/guestbook/{guestbook_id}", dependencies=[Depends(get_current_admin)])
def delete_existing_guestbook(guestbook_id: int, db: Session = Depends(get_db)):
    delete_guestbook(db, guestbook_id)
    return wrap_response(data={"message": "Guestbook entry deleted successfully"})

@router.get("/{comment_id}")
def get_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    result = _build_comment_response(comment, db)
    return wrap_response(data=result.model_dump())

@router.put("/{comment_id}/approve", dependencies=[Depends(get_current_admin)])
def approve_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    comment.is_approved = not comment.is_approved
    db.commit()
    db.refresh(comment)

    if comment.user_id:
        user = get_user_by_id(db, comment.user_id)
        username = user.username if user else "Unknown"
        avatar = user.avatar if user else None
    else:
        username = comment.guest_name or "游客"
        avatar = None

    return wrap_response(data=CommentSchema(
        id=comment.id,
        article_id=comment.article_id,
        user_id=comment.user_id,
        username=username,
        avatar=avatar,
        guest_name=comment.guest_name,
        content=comment.content,
        parent_id=comment.parent_id,
        like_count=comment.like_count,
        is_approved=comment.is_approved,
        created_at=comment.created_at,
        replies=[]
    ).model_dump())

@router.delete("/{comment_id}", dependencies=[Depends(get_current_admin)])
def delete_existing_comment(comment_id: int, db: Session = Depends(get_db)):
    delete_comment(db, comment_id)
    return wrap_response(data={"message": "Comment deleted successfully"})

@router.post("/{comment_id}/like")
def like_comment(
    comment_id: int,
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_optional)
):
    from ...models.site_settings import SiteSettings
    settings = db.query(SiteSettings).first()
    login_enabled = bool(settings.login_enabled) if settings else True

    if login_enabled and not current_user:
        raise HTTPException(status_code=401, detail="请先登录")

    if current_user:
        liked = toggle_comment_like(db, current_user.id, comment_id)
    else:
        from ...models.comment import CommentLike
        ip_address = get_client_ip(request)
        existing_like = db.query(CommentLike).filter(
            CommentLike.comment_id == comment_id,
            CommentLike.user_id == None
        ).first()
        if existing_like:
            raise HTTPException(status_code=400, detail="您已经点过赞了")

        comment = db.query(Comment).filter(Comment.id == comment_id).first()
        if not comment:
            raise HTTPException(status_code=404, detail="评论不存在")

        guest_like = CommentLike(user_id=None, comment_id=comment_id)
        db.add(guest_like)
        comment.like_count = (comment.like_count or 0) + 1
        db.commit()
        db.refresh(comment)
        liked = True

    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    return wrap_response(data={"liked": liked, "like_count": comment.like_count if comment else 0})