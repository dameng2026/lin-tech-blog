from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_current_admin
from .auth import wrap_response
from ...crud.taxonomy import (
    create_category, get_categories, get_category_by_id, update_category, delete_category,
    create_tag, get_tags, get_tag_by_id, update_tag, delete_tag, toggle_category_status
)
from ...schemas.taxonomy import (
    CategoryCreate, CategoryUpdate, CategoryResponse,
    TagCreate, TagUpdate, TagResponse
)
from ...core.database import get_db

router = APIRouter(prefix="/taxonomy", tags=["taxonomy"])

@router.get("/categories")
def list_categories(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1),
    include_inactive: bool = Query(False, description="是否包含已暂停的分类"),
    db: Session = Depends(get_db)
):
    categories, _ = get_categories(db, skip, limit, include_inactive)
    return wrap_response(data=categories)

@router.post("/categories", dependencies=[Depends(get_current_admin)])
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return wrap_response(data=create_category(db, category))

@router.put("/categories/{category_id}", dependencies=[Depends(get_current_admin)])
def update_existing_category(category_id: int, category_update: CategoryUpdate, db: Session = Depends(get_db)):
    category = update_category(db, category_id, category_update)
    if not category:
        return {"code": 404, "msg": "分类不存在", "data": None}
    return wrap_response(data=category)

@router.patch("/categories/{category_id}/toggle-status", dependencies=[Depends(get_current_admin)])
def toggle_category(category_id: int, db: Session = Depends(get_db)):
    category = toggle_category_status(db, category_id)
    if not category:
        return {"code": 404, "msg": "分类不存在", "data": None}
    status_text = "已启用" if category.is_active else "已暂停"
    return wrap_response(data={"id": category.id, "is_active": category.is_active}, msg=status_text)

@router.delete("/categories/{category_id}", dependencies=[Depends(get_current_admin)])
def delete_existing_category(category_id: int, db: Session = Depends(get_db)):
    category = get_category_by_id(db, category_id)
    if not category:
        return {"code": 404, "msg": "分类不存在", "data": None}
    delete_category(db, category_id)
    return wrap_response(data={"id": category_id}, msg="删除成功")

@router.get("/tags")
def list_tags(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1),
    db: Session = Depends(get_db)
):
    tags, _ = get_tags(db, skip, limit)
    return wrap_response(data=tags)

@router.post("/tags", dependencies=[Depends(get_current_admin)])
def create_new_tag(tag: TagCreate, db: Session = Depends(get_db)):
    return wrap_response(data=create_tag(db, tag))

@router.put("/tags/{tag_id}", dependencies=[Depends(get_current_admin)])
def update_existing_tag(tag_id: int, tag_update: TagUpdate, db: Session = Depends(get_db)):
    return wrap_response(data=update_tag(db, tag_id, tag_update))

@router.delete("/tags/{tag_id}", dependencies=[Depends(get_current_admin)])
def delete_existing_tag(tag_id: int, db: Session = Depends(get_db)):
    delete_tag(db, tag_id)
    return wrap_response(data={"message": "Tag deleted successfully"})


@router.get("/tech-stacks")
def get_tech_stack_stats(db: Session = Depends(get_db)):
    from ...models.article import Article
    from ...models.project import Project
    from collections import Counter
    import json

    article_tag_counts = Counter()
    article_tag_article_counts = Counter()
    project_tech_counts = Counter()
    project_tech_project_counts = Counter()

    articles = db.query(Article.tags).filter(Article.tags.isnot(None)).all()
    for (tags,) in articles:
        if tags:
            if isinstance(tags, list):
                tag_list = [str(t).strip() for t in tags if str(t).strip()]
            else:
                tag_list = [t.strip() for t in str(tags).split(',') if t.strip()]
            for tag in tag_list:
                article_tag_counts[tag] += 1
            for tag in set(tag_list):
                article_tag_article_counts[tag] += 1

    projects = db.query(Project.tech_stack).filter(Project.tech_stack.isnot(None)).all()
    for (tech_stack,) in projects:
        if tech_stack:
            if isinstance(tech_stack, list):
                tech_list = [str(t).strip() for t in tech_stack if str(t).strip()]
            else:
                try:
                    tech_list = json.loads(tech_stack) if isinstance(tech_stack, str) else [str(t).strip() for t in str(tech_stack).split(',') if str(t).strip()]
                except Exception:
                    tech_list = [t.strip() for t in str(tech_stack).split(',') if t.strip()]
            for tech in tech_list:
                tech = str(tech).strip()
                if tech:
                    project_tech_counts[tech] += 1
            for tech in set(str(t).strip() for t in tech_list if str(t).strip()):
                project_tech_project_counts[tech] += 1

    all_techs = set(list(article_tag_counts.keys()) + list(project_tech_counts.keys()))

    result = []
    for tech in all_techs:
        result.append({
            "name": tech,
            "article_count": article_tag_counts.get(tech, 0),
            "project_count": project_tech_counts.get(tech, 0),
            "total_count": article_tag_counts.get(tech, 0) + project_tech_counts.get(tech, 0),
            "article_article_count": article_tag_article_counts.get(tech, 0),
            "project_project_count": project_tech_project_counts.get(tech, 0),
        })

    result.sort(key=lambda x: x["total_count"], reverse=True)

    return wrap_response(data={
        "list": result,
        "total": len(result),
        "page": 1,
        "size": len(result)
    })
