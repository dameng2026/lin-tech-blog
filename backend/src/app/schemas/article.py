from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict

class ArticleCreate(BaseModel):
    title: str
    cover: Optional[str] = None
    summary: Optional[str] = None
    content: str
    category: Optional[str] = None
    tags: Optional[List[str]] = []
    tech_stack: Optional[List[str]] = []
    catalog: Optional[List[Dict[str, str]]] = []
    read_time: Optional[int] = 0
    allow_comment: Optional[bool] = True
    source_type: Optional[str] = "original"
    repost_url: Optional[str] = None
    
    author_name: Optional[str] = None
    author_avatar: Optional[str] = None
    author_bio: Optional[str] = None
    
    seo_title: Optional[str] = None
    seo_keywords: Optional[str] = None
    seo_description: Optional[str] = None

class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    cover: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = []
    tech_stack: Optional[List[str]] = []
    catalog: Optional[List[Dict[str, str]]] = []
    read_time: Optional[int] = None
    allow_comment: Optional[bool] = None
    source_type: Optional[str] = None
    repost_url: Optional[str] = None
    
    author_name: Optional[str] = None
    author_avatar: Optional[str] = None
    author_bio: Optional[str] = None
    
    seo_title: Optional[str] = None
    seo_keywords: Optional[str] = None
    seo_description: Optional[str] = None

class ArticleAuthor(BaseModel):
    name: Optional[str]
    avatar: Optional[str]
    bio: Optional[str]

class ArticleResponse(BaseModel):
    id: int
    title: str
    cover: Optional[str]
    summary: Optional[str]
    content: str
    category: Optional[str]
    tags: List[str]
    tech_stack: List[str]
    catalog: List[Dict[str, str]]
    read_time: int
    view_count: int
    like_count: int
    collect_count: int
    comment_count: int
    is_published: bool
    allow_comment: bool
    source_type: str
    repost_url: Optional[str]
    author: ArticleAuthor
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class ArticleListResponse(BaseModel):
    articles: List[ArticleResponse]
    total: int
    page: int
    size: int

class ArticleReadStatus(BaseModel):
    is_liked: bool
    is_collected: bool