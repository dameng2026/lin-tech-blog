from pydantic import BaseModel
from typing import List, Optional

class LatestArticle(BaseModel):
    id: int
    title: str
    created_at: str

class LatestProject(BaseModel):
    id: int
    name: str
    created_at: str

class PendingItems(BaseModel):
    friend_links: int = 0
    guestbook_messages: int = 0
    unapproved_comments: int = 0
    resume_key_requests: int = 0

class DashboardSummaryResponse(BaseModel):
    articles_count: int
    projects_count: int
    users_count: int
    total_views: int
    total_likes: int
    total_comments: int
    total_collects: int
    days_running: int
    visit_trend: List[int]
    latest_articles: List[LatestArticle]
    latest_projects: List[LatestProject]
    pending: PendingItems
