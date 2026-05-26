from pydantic import BaseModel
from typing import List, Optional

class SiteStatsResponse(BaseModel):
    articles_count: int
    projects_count: int
    total_views: int
    total_likes: int
    total_comments: int
    total_collects: int
    github_stars: int
    github_followers: int
    site_start_date: str
    days_running: int

class ArticleArchiveResponse(BaseModel):
    year: int
    month: int
    article_count: int
    articles: List[dict]

class HotArticleResponse(BaseModel):
    id: int
    title: str
    view_count: int
    like_count: int
    category: str
    created_at: str

class HotProjectResponse(BaseModel):
    id: int
    name: str
    view_count: int
    status: str
    created_at: str