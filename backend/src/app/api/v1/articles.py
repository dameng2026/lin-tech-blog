from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, text
from typing import Optional, List
import re
from ..dependencies import get_current_user, get_current_admin
from .auth import wrap_response
from ...crud.article import (
    create_article, get_article_by_id, get_articles, update_article, delete_article,
    increment_view_count, toggle_like, toggle_collect, get_related_articles
)
from ...crud.comment import get_comments_by_article
from ...schemas.article import ArticleCreate, ArticleUpdate, ArticleResponse, ArticleListResponse, ArticleAuthor
from ...schemas.comment import CommentResponse
from ...schemas.user import UserResponse
from ...core.database import get_db
from ...models.article import Article
from ...models.taxonomy import Category

router = APIRouter(prefix="/articles", tags=["articles"])


def _normalize_catalog(catalog: list) -> list:
    result = []
    for item in catalog:
        level = str(int(item.get('level', 1)))
        title = item.get('title', '')
        anchor = item.get('anchor', '')
        if not anchor and title:
            anchor = re.sub(r'[^\w\u4e00-\u9fff]+', '-', title.lower()).strip('-')
        if anchor and title:
            result.append({'level': level, 'title': title, 'anchor': anchor})
    return result


def _inject_heading_ids(content: str, catalog: list) -> str:
    if not content or not catalog:
        return content
    
    idx_map = {}
    for item in catalog:
        lvl = int(item.get('level', 1))
        anchor = item.get('anchor', '')
        title = item.get('title', '')
        if anchor and title:
            if lvl not in idx_map:
                idx_map[lvl] = []
            idx_map[lvl].append({'anchor': anchor, 'title': title})
    
    def add_id(match):
        level = match.group(1)
        attrs = match.group(2) or ''
        inner = match.group(3)
        full_tag = match.group(0)
        inner_text = re.sub(r'<[^>]+>', '', inner).strip()
        
        lvl = int(level)
        if lvl in idx_map and idx_map[lvl]:
            candidate = idx_map[lvl][0]
            if inner_text == candidate['title']:
                idx_map[lvl].pop(0)
                if 'id="' not in attrs:
                    return f'<h{level}{attrs} id="{candidate["anchor"]}">{inner}</h{level}>'
        return full_tag
    
    content = re.sub(r'<h([1-6])([^>]*)>(.*?)</h\1>', add_id, content, flags=re.DOTALL)
    return content


def _build_article_response(article, comment_count: int = 0) -> ArticleResponse:
    catalog = _normalize_catalog(article.catalog or [])
    content = _inject_heading_ids(article.content, catalog)
    return ArticleResponse(
        id=article.id,
        title=article.title,
        cover=article.cover,
        summary=article.summary,
        content=content,
        category=article.category,
        tags=article.tags or [],
        tech_stack=article.tech_stack or [],
        catalog=catalog,
        read_time=article.read_time or 0,
        view_count=article.view_count,
        like_count=article.like_count,
        collect_count=article.collect_count,
        comment_count=comment_count,
        is_published=article.is_published if article.is_published is not None else True,
        allow_comment=article.allow_comment if article.allow_comment is not None else True,
        source_type=article.source_type or "original",
        repost_url=article.repost_url,
        author=ArticleAuthor(
            name=article.author_name,
            avatar=article.author_avatar,
            bio=article.author_bio
        ),
        created_at=article.created_at,
        updated_at=article.updated_at or article.created_at
    )


@router.get("/")
def list_articles(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    category: Optional[str] = None,
    tag: Optional[str] = None,
    tech_stack: Optional[str] = None,
    sort_by: str = Query("created_at", enum=["created_at", "view_count", "like_count"]),
    db: Session = Depends(get_db)
):
    articles, total = get_articles(db, page, size, category, tag, tech_stack, sort_by)
    article_responses = [_build_article_response(a) for a in articles]
    return wrap_response(data={"articles": article_responses, "total": total, "page": page, "size": size})

@router.get("/categories/stats")
def get_category_stats(db: Session = Depends(get_db)):
    categories = db.query(Category).filter(Category.is_active == True).all()
    result = []
    for cat in categories:
        count = db.query(func.count(Article.id)).filter(
            Article.is_published == True,
            Article.category == cat.name
        ).scalar() or 0
        result.append({"name": cat.name, "count": count})
    result.sort(key=lambda x: (-x["count"], x["name"]))
    return wrap_response(data=result)

@router.get("/tags/stats")
def get_tag_stats(db: Session = Depends(get_db)):
    articles = db.query(Article.tags).filter(
        Article.is_published == True,
        Article.tags.isnot(None)
    ).all()
    tag_count = {}
    for (tags,) in articles:
        if tags and isinstance(tags, list):
            for tag in tags:
                tag_count[tag] = tag_count.get(tag, 0) + 1
    result = [{"name": k, "count": v} for k, v in sorted(tag_count.items(), key=lambda x: -x[1])]
    return wrap_response(data=result)

@router.get("/tech-stack/stats")
def get_tech_stack_stats(db: Session = Depends(get_db)):
    articles = db.query(Article.tech_stack).filter(
        Article.is_published == True,
        Article.tech_stack.isnot(None)
    ).all()
    stack_count = {}
    for (tech_stack,) in articles:
        if tech_stack and isinstance(tech_stack, list):
            for stack in tech_stack:
                stack_count[stack] = stack_count.get(stack, 0) + 1
    result = [{"name": k, "count": v} for k, v in sorted(stack_count.items(), key=lambda x: -x[1])]
    return wrap_response(data=result)

@router.get("/{article_id}")
def get_article(article_id: int, db: Session = Depends(get_db)):
    article = get_article_by_id(db, article_id)
    increment_view_count(db, article_id)
    comments, total = get_comments_by_article(db, article_id)
    return wrap_response(data=_build_article_response(article, comment_count=total))

@router.get("/{article_id}/related")
def get_related(article_id: int, limit: int = Query(3, ge=1, le=10), db: Session = Depends(get_db)):
    articles = get_related_articles(db, article_id, limit)
    result = []
    for a in articles:
        result.append({
            "id": a.id,
            "title": a.title,
            "cover": a.cover,
            "created_at": a.created_at,
            "view_count": a.view_count
        })
    return wrap_response(data=result)

@router.post("/", dependencies=[Depends(get_current_admin)])
def create_new_article(article_create: ArticleCreate, db: Session = Depends(get_db)):
    article = create_article(db, article_create)
    return wrap_response(data=_build_article_response(article))

@router.put("/{article_id}", dependencies=[Depends(get_current_admin)])
def update_existing_article(
    article_id: int,
    article_update: ArticleUpdate,
    db: Session = Depends(get_db)
):
    article = update_article(db, article_id, article_update)
    comments, total = get_comments_by_article(db, article_id)
    return wrap_response(data=_build_article_response(article, comment_count=total))

@router.delete("/{article_id}", dependencies=[Depends(get_current_admin)])
def delete_existing_article(article_id: int, db: Session = Depends(get_db)):
    delete_article(db, article_id)
    return wrap_response(data={"message": "Article deleted successfully"})

@router.post("/{article_id}/like")
def like_article(
    article_id: int,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    liked = toggle_like(db, current_user.id, article_id)
    return wrap_response(data={"liked": liked})

@router.post("/{article_id}/collect")
def collect_article(
    article_id: int,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    collected = toggle_collect(db, current_user.id, article_id)
    return wrap_response(data={"collected": collected})