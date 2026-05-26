from fastapi import APIRouter, Depends, Query, Request, HTTPException
from sqlalchemy.orm import Session
from typing import Optional, List
from ..dependencies import get_current_admin, get_current_admin_optional
from ...crud.project import (
    create_project, get_project_by_id, get_projects, update_project, delete_project,
    increment_project_view_count, get_project_category_stats, get_project_tech_stack_stats
)
from ...models.project import Project
from ...models.site_settings import SiteSettings
from ...schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
from ...core.database import get_db
from .auth import wrap_response

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("/categories/stats")
def list_project_category_stats(db: Session = Depends(get_db)):
    stats = get_project_category_stats(db)
    return wrap_response(data=stats)

@router.get("/tech-stacks/stats")
def list_project_tech_stack_stats(db: Session = Depends(get_db)):
    stats = get_project_tech_stack_stats(db)
    return wrap_response(data=stats)

@router.get("/")
def list_projects(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    tech_stack: Optional[str] = None,
    status: Optional[str] = None,
    include_paused: bool = Query(False),
    category_id: Optional[int] = Query(None, ge=1),
    db: Session = Depends(get_db)
):
    projects, total = get_projects(db, page, size, tech_stack, status, include_paused, category_id)
    project_responses = [ProjectResponse.model_validate(p) for p in projects]
    return wrap_response(data={"projects": project_responses, "total": total, "page": page, "size": size})

@router.get("/{project_id}")
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = get_project_by_id(db, project_id)
    if not project:
        return wrap_response(code=404, msg="Project not found")
    increment_project_view_count(db, project_id)
    return wrap_response(data=ProjectResponse.model_validate(project))

@router.post("/", dependencies=[Depends(get_current_admin)])
def create_new_project(project_create: ProjectCreate, db: Session = Depends(get_db)):
    project = create_project(db, project_create)
    return wrap_response(data=ProjectResponse.model_validate(project))

@router.put("/{project_id}", dependencies=[Depends(get_current_admin)])
def update_existing_project(
    project_id: int,
    project_update: ProjectUpdate,
    db: Session = Depends(get_db)
):
    project = get_project_by_id(db, project_id)
    if not project:
        return wrap_response(code=404, msg="Project not found")
    project = update_project(db, project_id, project_update)
    return wrap_response(data=ProjectResponse.model_validate(project))

@router.delete("/{project_id}", dependencies=[Depends(get_current_admin)])
def delete_existing_project(project_id: int, db: Session = Depends(get_db)):
    project = get_project_by_id(db, project_id)
    if not project:
        return wrap_response(code=404, msg="Project not found")
    delete_project(db, project_id)
    return wrap_response(data={"message": "Project deleted successfully"})

@router.post("/{project_id}/like")
def like_project(
    project_id: int,
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_optional)
):
    settings = db.query(SiteSettings).first()
    login_enabled = bool(settings.login_enabled) if settings else True

    if login_enabled and not current_user:
        raise HTTPException(status_code=401, detail="请先登录")

    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="项目不存在")

    project.like_count = (project.like_count or 0) + 1
    db.commit()
    db.refresh(project)

    return wrap_response(data={"liked": True, "like_count": project.like_count})