from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from datetime import datetime
from ..models.statistics import SiteStats, ArticleArchive, ViewLog
from ..models.article import Article
from ..models.project import Project
from ..models.comment import Comment
from ..models.article import ArticleLike, ArticleCollect
from typing import List, Optional

def get_or_create_site_stats(db: Session):
    stats = db.query(SiteStats).first()
    if not stats:
        stats = SiteStats(
            articles_count=0,
            projects_count=0,
            total_views=0,
            total_likes=0,
            total_comments=0,
            total_collects=0,
            github_stars=0,
            github_followers=0,
            site_start_date=datetime.now()
        )
        db.add(stats)
        db.commit()
        db.refresh(stats)
    return stats

def update_site_stats(db: Session):
    stats = get_or_create_site_stats(db)
    
    stats.articles_count = db.query(func.count(Article.id)).filter(Article.is_published == True).scalar()
    stats.projects_count = db.query(func.count(Project.id)).scalar()
    stats.total_views = db.query(func.sum(Article.view_count)).scalar() or 0
    stats.total_likes = db.query(func.sum(ArticleLike.id)).count()
    stats.total_comments = db.query(func.count(Comment.id)).filter(Comment.is_approved == True).scalar()
    stats.total_collects = db.query(func.count(ArticleCollect.id)).scalar()
    
    db.commit()
    db.refresh(stats)
    return stats

def get_site_stats(db: Session):
    return get_or_create_site_stats(db)

def update_github_stats(db: Session, stars: int, followers: int):
    stats = get_or_create_site_stats(db)
    stats.github_stars = stars
    stats.github_followers = followers
    stats.cached_at = datetime.now()
    db.commit()
    db.refresh(stats)
    return stats

def get_article_archive(db: Session) -> List[dict]:
    articles = db.query(Article).filter(Article.is_published == True).all()
    archive = {}
    
    for article in articles:
        year = article.created_at.year
        month = article.created_at.month
        key = f"{year}-{month:02d}"
        
        if key not in archive:
            archive[key] = {
                "year": year,
                "month": month,
                "article_count": 0,
                "articles": []
            }
        
        archive[key]["article_count"] += 1
        archive[key]["articles"].append({
            "id": article.id,
            "title": article.title,
            "created_at": article.created_at.strftime("%Y-%m-%d")
        })
    
    result = sorted(archive.values(), key=lambda x: (x["year"], x["month"]), reverse=True)
    return result

def get_hot_articles(db: Session, limit: int = 10) -> List[Article]:
    return db.query(Article).filter(Article.is_published == True)\
        .order_by(Article.view_count.desc())\
        .limit(limit)\
        .all()

def get_hot_projects(db: Session, limit: int = 10) -> List[Project]:
    return db.query(Project)\
        .order_by(Project.view_count.desc())\
        .limit(limit)\
        .all()

def log_view(db: Session, article_id: int, ip_address: str = None, user_agent: str = None):
    view_log = ViewLog(
        article_id=article_id,
        ip_address=ip_address,
        user_agent=user_agent
    )
    db.add(view_log)
    db.commit()
    return view_log