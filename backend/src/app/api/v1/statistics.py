from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import httpx
from ..dependencies import get_current_admin
from .auth import wrap_response
from ...crud.statistics import (
    get_site_stats, update_site_stats, update_github_stats,
    get_article_archive, get_hot_articles, get_hot_projects
)
from ...schemas.statistics import (
    SiteStatsResponse, ArticleArchiveResponse,
    HotArticleResponse, HotProjectResponse
)
from ...core.database import get_db
from ...core.config import settings
from typing import List

router = APIRouter(prefix="/statistics", tags=["statistics"])

@router.get("/site")
def get_site_statistics(db: Session = Depends(get_db)):
    stats = get_site_stats(db)
    days_running = (datetime.now() - stats.site_start_date).days if stats.site_start_date else 0
    
    return wrap_response(data={
        "articles_count": stats.articles_count,
        "projects_count": stats.projects_count,
        "total_views": stats.total_views,
        "total_likes": stats.total_likes,
        "total_comments": stats.total_comments,
        "total_collects": stats.total_collects,
        "github_stars": stats.github_stars,
        "github_followers": stats.github_followers,
        "site_start_date": stats.site_start_date.strftime("%Y-%m-%d") if stats.site_start_date else "",
        "days_running": days_running
    })

@router.post("/site/update", dependencies=[Depends(get_current_admin)])
def update_site_statistics(db: Session = Depends(get_db)):
    stats = update_site_stats(db)
    days_running = (datetime.now() - stats.site_start_date).days if stats.site_start_date else 0
    
    return wrap_response(data={
        "articles_count": stats.articles_count,
        "projects_count": stats.projects_count,
        "total_views": stats.total_views,
        "total_likes": stats.total_likes,
        "total_comments": stats.total_comments,
        "total_collects": stats.total_collects,
        "github_stars": stats.github_stars,
        "github_followers": stats.github_followers,
        "site_start_date": stats.site_start_date.strftime("%Y-%m-%d") if stats.site_start_date else "",
        "days_running": days_running
    })

@router.post("/site/visit")
def record_site_visit(db: Session = Depends(get_db)):
    from ...models.statistics import SiteStats
    stats = db.query(SiteStats).first()
    if stats:
        stats.total_views = (stats.total_views or 0) + 1
        db.commit()
    if not stats:
        stats = SiteStats(
            articles_count=0, projects_count=0, total_views=1,
            total_likes=0, total_comments=0, total_collects=0,
            site_start_date=datetime.now()
        )
        db.add(stats)
        db.commit()
    return wrap_response(data={"message": "ok"})

@router.post("/github/sync", dependencies=[Depends(get_current_admin)])
async def sync_github_stats(db: Session = Depends(get_db)):
    username = getattr(settings, "GITHUB_USERNAME", "your-github-username")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://api.github.com/users/{username}")
            if response.status_code == 200:
                github_data = response.json()
                update_github_stats(db, github_data.get("public_repos", 0), github_data.get("followers", 0))
                return wrap_response(data={"message": "GitHub stats synced successfully"})
            return wrap_response(code=500, msg="Failed to sync GitHub stats")
    except Exception:
        return wrap_response(code=500, msg="Failed to sync GitHub stats")

@router.get("/visit-trend")
def get_visit_trend(
    days: int = Query(7, ge=1, le=90),
    db: Session = Depends(get_db)
):
    from ...models.statistics import ViewLog
    from sqlalchemy import func

    today = datetime.now()
    trend = []
    for i in range(days):
        day_start = datetime(today.year, today.month, today.day) - timedelta(days=days - 1 - i)
        day_end = day_start + timedelta(days=1)
        count = db.query(func.count(ViewLog.id)).filter(
            ViewLog.view_time >= day_start,
            ViewLog.view_time < day_end
        ).scalar()
        trend.append({
            "date": day_start.strftime("%Y-%m-%d"),
            "count": count
        })

    return wrap_response(data=trend)

@router.get("/latest-comments")
def get_latest_comments(
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db)
):
    from ...models.comment import Comment

    comments = db.query(Comment).filter(
        Comment.is_approved == True
    ).order_by(Comment.created_at.desc()).limit(limit).all()

    return wrap_response(data=[{
        "id": c.id,
        "content": c.content[:100],
        "guest_name": c.guest_name,
        "article_id": c.article_id,
        "project_id": c.project_id,
        "created_at": c.created_at.strftime("%Y-%m-%d %H:%M")
    } for c in comments])

@router.get("/articles/archive")
def get_article_archive_list(db: Session = Depends(get_db)):
    archive = get_article_archive(db)
    return wrap_response(data=[ArticleArchiveResponse(**item).model_dump() for item in archive])

@router.get("/articles/hot")
def get_hot_articles_list(
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db)
):
    articles = get_hot_articles(db, limit)
    return wrap_response(data=[{
        "id": article.id,
        "title": article.title,
        "view_count": article.view_count,
        "like_count": article.like_count,
        "category": article.category,
        "created_at": article.created_at.strftime("%Y-%m-%d")
    } for article in articles])

@router.get("/projects/hot")
def get_hot_projects_list(
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db)
):
    projects = get_hot_projects(db, limit)
    return wrap_response(data=[{
        "id": project.id,
        "name": project.name,
        "view_count": project.view_count,
        "status": project.status,
        "created_at": project.created_at.strftime("%Y-%m-%d")
    } for project in projects])