from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from ...crud.statistics import get_site_stats
from ...crud.article import get_articles
from ...crud.project import get_projects
from .auth import wrap_response
from ...models.user import User
from ...models.comment import Comment, Guestbook
from ...models.friend_link import FriendLink
from ...models.profile import ResumeKey
from ...models.statistics import ViewLog
from ...schemas.dashboard import DashboardSummaryResponse, LatestArticle, LatestProject, PendingItems
from ...core.database import get_db

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/summary")
def get_dashboard_summary(db: Session = Depends(get_db)):
    stats = get_site_stats(db)
    days_running = (datetime.now() - stats.site_start_date).days if stats.site_start_date else 0

    users_count = db.query(func.count(User.id)).scalar()

    today = datetime.now()
    seven_days_ago = today - timedelta(days=6)
    visit_trend = []
    for i in range(7):
        day_start = datetime(seven_days_ago.year, seven_days_ago.month, seven_days_ago.day) + timedelta(days=i)
        day_end = day_start + timedelta(days=1)
        count = db.query(func.count(ViewLog.id)).filter(
            ViewLog.view_time >= day_start,
            ViewLog.view_time < day_end
        ).scalar()
        visit_trend.append(count)

    articles, _ = get_articles(db, page=1, size=5)
    latest_articles = [
        LatestArticle(id=a.id, title=a.title, created_at=a.created_at.strftime("%Y-%m-%d"))
        for a in articles
    ]

    projects, _ = get_projects(db, page=1, size=5)
    latest_projects = [
        LatestProject(id=p.id, name=p.name, created_at=p.created_at.strftime("%Y-%m-%d"))
        for p in projects
    ]

    pending_friend_links = db.query(func.count(FriendLink.id)).filter(FriendLink.status == "pending").scalar()
    guestbook_messages = db.query(func.count(Guestbook.id)).scalar()
    unapproved_comments = db.query(func.count(Comment.id)).filter(Comment.is_approved == False).scalar()
    resume_key_requests = db.query(func.count(ResumeKey.id)).scalar()

    data = DashboardSummaryResponse(
        articles_count=stats.articles_count,
        projects_count=stats.projects_count,
        users_count=users_count,
        total_views=stats.total_views,
        total_likes=stats.total_likes,
        total_comments=stats.total_comments,
        total_collects=stats.total_collects,
        days_running=days_running,
        visit_trend=visit_trend,
        latest_articles=latest_articles,
        latest_projects=latest_projects,
        pending=PendingItems(
            friend_links=pending_friend_links,
            guestbook_messages=guestbook_messages,
            unapproved_comments=unapproved_comments,
            resume_key_requests=resume_key_requests
        )
    )
    return wrap_response(data=data.model_dump())
