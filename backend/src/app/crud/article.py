from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from typing import Optional, List, Dict
import re
from ..models.article import Article, ArticleLike, ArticleCollect
from ..models.comment import Comment
from ..models.statistics import ViewLog
from ..schemas.article import ArticleCreate, ArticleUpdate
from ..utils.read_time import calculate_read_time as calculate_read_time_utils
from fastapi import HTTPException, status

# 阅读速度配置（字符/分钟）
READING_SPEED = 400

def calculate_read_time(content: str) -> int:
    """计算阅读时长（分钟）"""
    return calculate_read_time_utils(content)

def generate_catalog(content: str) -> List[Dict[str, str]]:
    catalog = []
    headings = re.findall(r'<h([1-6])[^>]*>(.*?)</h\1>', content, re.DOTALL)
    for level, text in headings:
        text = re.sub(r'<[^>]+>', '', text).strip()
        if text:
            anchor = re.sub(r'[^\w\u4e00-\u9fff]+', '-', text.lower()).strip('-')
            catalog.append({
                'level': int(level),
                'title': text,
                'anchor': anchor
            })
    return catalog

def create_article(db: Session, article_create: ArticleCreate) -> Article:
    read_time = article_create.read_time if article_create.read_time else calculate_read_time(article_create.content)
    catalog = article_create.catalog if article_create.catalog else generate_catalog(article_create.content)
    
    article = Article(
        title=article_create.title,
        cover=article_create.cover,
        summary=article_create.summary,
        content=article_create.content,
        category=article_create.category,
        tags=article_create.tags,
        tech_stack=article_create.tech_stack,
        catalog=catalog,
        read_time=read_time,
        allow_comment=article_create.allow_comment,
        source_type=article_create.source_type or "original",
        repost_url=article_create.repost_url,
        author_name=article_create.author_name,
        author_avatar=article_create.author_avatar,
        author_bio=article_create.author_bio,
        seo_title=article_create.seo_title,
        seo_keywords=article_create.seo_keywords,
        seo_description=article_create.seo_description
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article

def get_article_by_id(db: Session, article_id: int) -> Article:
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    return article

def get_articles(
    db: Session,
    page: int = 1,
    size: int = 10,
    category: Optional[str] = None,
    tag: Optional[str] = None,
    tech_stack: Optional[str] = None,
    sort_by: str = "created_at"
) -> tuple:
    query = db.query(Article).filter(Article.is_published == True)
    
    if category:
        query = query.filter(Article.category == category)
    if tag:
        query = query.filter(func.json_contains(Article.tags, f'["{tag}"]'))
    if tech_stack:
        query = query.filter(func.json_contains(Article.tech_stack, f'["{tech_stack}"]'))
    
    if sort_by == "view_count":
        query = query.order_by(desc(Article.view_count))
    elif sort_by == "like_count":
        query = query.order_by(desc(Article.like_count))
    else:
        query = query.order_by(desc(Article.created_at))
    
    total = query.count()
    articles = query.offset((page - 1) * size).limit(size).all()
    return articles, total

def update_article(db: Session, article_id: int, article_update: ArticleUpdate) -> Article:
    article = get_article_by_id(db, article_id)
    if article_update.title is not None:
        article.title = article_update.title
    if article_update.cover is not None:
        article.cover = article_update.cover
    if article_update.summary is not None:
        article.summary = article_update.summary
    if article_update.content is not None:
        article.content = article_update.content
        # 更新内容时重新计算阅读时间
        if not article_update.read_time:
            article.read_time = calculate_read_time(article_update.content)
    if article_update.category is not None:
        article.category = article_update.category
    if article_update.tags is not None:
        article.tags = article_update.tags
    if article_update.tech_stack is not None:
        article.tech_stack = article_update.tech_stack
    if article_update.read_time is not None:
        article.read_time = article_update.read_time
    if article_update.source_type is not None:
        article.source_type = article_update.source_type
    if article_update.repost_url is not None:
        article.repost_url = article_update.repost_url
    if article_update.allow_comment is not None:
        article.allow_comment = article_update.allow_comment
    if article_update.author_name is not None:
        article.author_name = article_update.author_name
    if article_update.author_avatar is not None:
        article.author_avatar = article_update.author_avatar
    if article_update.author_bio is not None:
        article.author_bio = article_update.author_bio
    if article_update.seo_title is not None:
        article.seo_title = article_update.seo_title
    if article_update.seo_keywords is not None:
        article.seo_keywords = article_update.seo_keywords
    if article_update.seo_description is not None:
        article.seo_description = article_update.seo_description
    db.commit()
    db.refresh(article)
    return article

def delete_article(db: Session, article_id: int) -> None:
    article = get_article_by_id(db, article_id)
    db.query(Comment).filter(Comment.article_id == article_id).delete()
    db.query(ArticleLike).filter(ArticleLike.article_id == article_id).delete()
    db.query(ArticleCollect).filter(ArticleCollect.article_id == article_id).delete()
    db.query(ViewLog).filter(ViewLog.article_id == article_id).delete()
    db.delete(article)
    db.commit()

def get_related_articles(db: Session, article_id: int, limit: int = 3):
    article = get_article_by_id(db, article_id)
    if not article:
        return []

    related = []
    if article.category:
        related = db.query(Article).filter(
            Article.is_published == True,
            Article.id != article_id,
            Article.category == article.category
        ).order_by(desc(Article.created_at)).limit(limit).all()

    if len(related) < limit and article.tags and isinstance(article.tags, list):
        existing_ids = [r.id for r in related] + [article_id]
        for tag in article.tags:
            if len(related) >= limit:
                break
            tag_matches = db.query(Article).filter(
                Article.is_published == True,
                Article.id.notin_(existing_ids),
                func.json_contains(Article.tags, f'["{tag}"]')
            ).order_by(desc(Article.created_at)).limit(limit - len(related)).all()
            related.extend(tag_matches)
            existing_ids.extend([r.id for r in tag_matches])

    return related[:limit]

def increment_view_count(db: Session, article_id: int) -> None:
    article = get_article_by_id(db, article_id)
    article.view_count += 1
    db.commit()

def toggle_like(db: Session, user_id: int, article_id: int) -> bool:
    like = db.query(ArticleLike).filter(
        ArticleLike.user_id == user_id,
        ArticleLike.article_id == article_id
    ).first()
    
    if like:
        db.delete(like)
        article = get_article_by_id(db, article_id)
        article.like_count -= 1
        db.commit()
        return False
    else:
        new_like = ArticleLike(user_id=user_id, article_id=article_id)
        db.add(new_like)
        article = get_article_by_id(db, article_id)
        article.like_count += 1
        db.commit()
        return True

def toggle_collect(db: Session, user_id: int, article_id: int) -> bool:
    collect = db.query(ArticleCollect).filter(
        ArticleCollect.user_id == user_id,
        ArticleCollect.article_id == article_id
    ).first()
    
    if collect:
        db.delete(collect)
        article = get_article_by_id(db, article_id)
        article.collect_count -= 1
        db.commit()
        return False
    else:
        new_collect = ArticleCollect(user_id=user_id, article_id=article_id)
        db.add(new_collect)
        article = get_article_by_id(db, article_id)
        article.collect_count += 1
        db.commit()
        return True