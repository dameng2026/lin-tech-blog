from sqlalchemy.orm import Session, joinedload
from sqlalchemy import desc, asc
from typing import Optional, List, Tuple
from ..models.comment import Comment, CommentLike, Guestbook
from ..schemas.comment import CommentCreate, GuestbookCreate
from fastapi import HTTPException, status

def create_comment(
    db: Session,
    article_id: Optional[int],
    project_id: Optional[int],
    user_id: Optional[int],
    comment_create: CommentCreate,
    ip_address: Optional[str] = None
) -> Comment:
    comment = Comment(
        article_id=article_id,
        project_id=project_id,
        user_id=user_id,
        guest_name=comment_create.guest_name if not user_id else None,
        guest_email=comment_create.guest_email,
        ip_address=ip_address,
        content=comment_create.content,
        parent_id=comment_create.parent_id,
        reply_to_id=comment_create.reply_to_id,
        reply_to_name=comment_create.reply_to_name
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def get_comment_by_id(db: Session, comment_id: int) -> Optional[Comment]:
    return db.query(Comment).filter(Comment.id == comment_id).first()

def get_comments_by_article(
    db: Session,
    article_id: int,
    page: int = 1,
    size: int = 10,
    sort: str = "newest"
) -> Tuple[List[Comment], int]:
    query = db.query(Comment).filter(
        Comment.article_id == article_id,
        Comment.is_approved == True,
        Comment.parent_id == None
    )

    total = query.count()

    if sort == "hottest":
        query = query.order_by(desc(Comment.like_count), desc(Comment.created_at))
    else:
        query = query.order_by(desc(Comment.created_at))

    parent_comments = query.offset((page - 1) * size).limit(size).all()

    parent_ids = [p.id for p in parent_comments]
    if parent_ids:
        replies = db.query(Comment).filter(
            Comment.parent_id.in_(parent_ids),
            Comment.is_approved == True
        ).order_by(Comment.created_at).all()
        
        reply_map = {}
        for reply in replies:
            if reply.parent_id not in reply_map:
                reply_map[reply.parent_id] = []
            reply_map[reply.parent_id].append(reply)
        
        for parent in parent_comments:
            parent_replies = reply_map.get(parent.id, [])
            for reply in parent_replies:
                reply.__dict__['replies'] = []
            db.expunge(parent)
            parent.__dict__['replies'] = parent_replies

    return parent_comments, total

def get_comments_by_project(
    db: Session,
    project_id: int,
    page: int = 1,
    size: int = 10,
    sort: str = "newest"
) -> Tuple[List[Comment], int]:
    query = db.query(Comment).filter(
        Comment.project_id == project_id,
        Comment.is_approved == True,
        Comment.parent_id == None
    )

    total = query.count()

    if sort == "hottest":
        query = query.order_by(desc(Comment.like_count), desc(Comment.created_at))
    else:
        query = query.order_by(desc(Comment.created_at))

    parent_comments = query.offset((page - 1) * size).limit(size).all()

    parent_ids = [p.id for p in parent_comments]
    if parent_ids:
        replies = db.query(Comment).filter(
            Comment.parent_id.in_(parent_ids),
            Comment.is_approved == True
        ).order_by(Comment.created_at).all()
        
        reply_map = {}
        for reply in replies:
            if reply.parent_id not in reply_map:
                reply_map[reply.parent_id] = []
            reply_map[reply.parent_id].append(reply)
        
        for parent in parent_comments:
            parent_replies = reply_map.get(parent.id, [])
            for reply in parent_replies:
                reply.__dict__['replies'] = []
            db.expunge(parent)
            parent.__dict__['replies'] = parent_replies

    return parent_comments, total

def delete_comment(db: Session, comment_id: int) -> None:
    comment = get_comment_by_id(db, comment_id)
    if comment:
        db.query(Comment).filter(Comment.parent_id == comment_id).delete()
        db.delete(comment)
        db.commit()

def toggle_comment_like(db: Session, user_id: int, comment_id: int) -> bool:
    like = db.query(CommentLike).filter(
        CommentLike.user_id == user_id,
        CommentLike.comment_id == comment_id
    ).first()

    comment = get_comment_by_id(db, comment_id)
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

    if like:
        db.delete(like)
        comment.like_count -= 1
        db.commit()
        return False
    else:
        new_like = CommentLike(user_id=user_id, comment_id=comment_id)
        db.add(new_like)
        comment.like_count += 1
        db.commit()
        return True

def get_all_comments(
    db: Session,
    page: int = 1,
    size: int = 20,
    content: Optional[str] = None,
    article_id: Optional[int] = None,
    project_id: Optional[int] = None,
    status: Optional[str] = None,
    comment_type: Optional[str] = None
) -> Tuple[List[Comment], int]:
    query = db.query(Comment)

    if content:
        query = query.filter(Comment.content.like(f"%{content}%"))
    if article_id:
        query = query.filter(Comment.article_id == article_id)
    if project_id:
        query = query.filter(Comment.project_id == project_id)
    if status:
        is_approved = status == "approved"
        query = query.filter(Comment.is_approved == is_approved)
    if comment_type == "article":
        query = query.filter(Comment.article_id.isnot(None))
    elif comment_type == "project":
        query = query.filter(Comment.project_id.isnot(None))
    elif comment_type == "guestbook":
        query = query.filter(Comment.article_id.is_(None), Comment.project_id.is_(None), Comment.parent_id.is_(None))
    else:
        query = query.filter(
            Comment.article_id.isnot(None) | Comment.project_id.isnot(None)
        )

    total = query.count()
    comments = query.order_by(Comment.created_at.desc()).offset((page - 1) * size).limit(size).all()
    return comments, total

def create_guestbook(db: Session, user_id: int, guestbook_create: GuestbookCreate) -> Guestbook:
    guestbook = Guestbook(
        user_id=user_id,
        content=guestbook_create.content
    )
    db.add(guestbook)
    db.commit()
    db.refresh(guestbook)
    return guestbook

def get_guestbooks(db: Session) -> list:
    guestbooks = db.query(Guestbook).order_by(
        desc(Guestbook.is_top),
        desc(Guestbook.created_at)
    ).all()
    return guestbooks

def update_guestbook(db: Session, guestbook_id: int, reply: str = None, is_top: bool = None) -> Guestbook:
    guestbook = db.query(Guestbook).filter(Guestbook.id == guestbook_id).first()
    if not guestbook:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Guestbook not found")
    if reply is not None:
        guestbook.reply = reply
    if is_top is not None:
        guestbook.is_top = is_top
    db.commit()
    db.refresh(guestbook)
    return guestbook

def delete_guestbook(db: Session, guestbook_id: int) -> None:
    guestbook = db.query(Guestbook).filter(Guestbook.id == guestbook_id).first()
    if not guestbook:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Guestbook not found")
    db.delete(guestbook)
    db.commit()

def get_guestbook_messages(
    db: Session,
    page: int = 1,
    size: int = 10,
    sort: str = "newest"
) -> Tuple[List[Comment], int]:
    query = db.query(Comment).filter(
        Comment.article_id == None,
        Comment.project_id == None,
        Comment.is_approved == True,
        Comment.parent_id == None
    )

    total = query.count()

    if sort == "hottest":
        query = query.order_by(desc(Comment.like_count), desc(Comment.created_at))
    else:
        query = query.order_by(desc(Comment.created_at))

    parent_comments = query.offset((page - 1) * size).limit(size).all()

    parent_ids = [p.id for p in parent_comments]
    if parent_ids:
        replies = db.query(Comment).filter(
            Comment.parent_id.in_(parent_ids),
            Comment.is_approved == True
        ).order_by(Comment.created_at).all()

        reply_map = {}
        for reply in replies:
            if reply.parent_id not in reply_map:
                reply_map[reply.parent_id] = []
            reply_map[reply.parent_id].append(reply)

        for parent in parent_comments:
            parent_replies = reply_map.get(parent.id, [])
            for reply in parent_replies:
                reply.__dict__['replies'] = []
            db.expunge(parent)
            parent.__dict__['replies'] = parent_replies

    return parent_comments, total

def create_guestbook_message(db: Session, comment_create: CommentCreate, ip_address: str = None) -> Comment:
    comment = Comment(
        article_id=None,
        project_id=None,
        user_id=None,
        guest_name=comment_create.guest_name or "游客",
        guest_email=comment_create.guest_email,
        ip_address=ip_address,
        content=comment_create.content,
        parent_id=comment_create.parent_id,
        reply_to_id=comment_create.reply_to_id,
        reply_to_name=comment_create.reply_to_name
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment