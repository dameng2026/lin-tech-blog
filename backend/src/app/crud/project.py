from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from typing import Optional, List
import random
from datetime import datetime, timezone
from ..models.project import Project
from ..models.project_category import ProjectCategory
from ..models.comment import Comment
from ..schemas.project import ProjectCreate, ProjectUpdate

def create_project(db: Session, project_create: ProjectCreate) -> Project:
    project = Project(
        name=project_create.name,
        cover=project_create.cover,
        tags=project_create.tags,
        github_url=project_create.github_url,
        demo_url=project_create.demo_url,
        summary=project_create.summary,
        tech_stack=project_create.tech_stack,
        status=project_create.status,
        description=project_create.description,
        project_type=project_create.project_type,
        start_date=project_create.start_date,
        end_date=project_create.end_date,
        last_update=project_create.last_update,
        open_source_license=project_create.open_source_license,
        database_type=project_create.database_type,
        deployment_platform=project_create.deployment_platform,
        docs_url=project_create.docs_url,
        content=project_create.content,
        catalog=project_create.catalog,
        is_paid=project_create.is_paid,
        is_featured=project_create.is_featured,
        repost_url=project_create.repost_url if project_create.repost_url else None,
        category_id=project_create.category_id,
        display_status=project_create.display_status or "active",
        publish_time=datetime.now(timezone.utc),
        like_count=project_create.like_count if project_create.like_count is not None else random.randint(0, 99),
        view_count=project_create.view_count if project_create.view_count is not None else random.randint(0, 99)
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def get_project_by_id(db: Session, project_id: int) -> Optional[Project]:
    project = db.query(Project).filter(Project.id == project_id).first()
    return project

def get_projects(
    db: Session,
    page: int = 1,
    size: int = 10,
    tech_stack: Optional[str] = None,
    status: Optional[str] = None,
    include_paused: bool = False,
    category_id: Optional[int] = None
) -> tuple:
    query = db.query(Project)
    
    if tech_stack:
        query = query.filter(func.json_contains(Project.tech_stack, f'["{tech_stack}"]'))
    if status:
        query = query.filter(Project.status == status)
    if not include_paused:
        query = query.filter(Project.display_status != "paused")
    if category_id is not None:
        query = query.filter(Project.category_id == category_id)
    
    query = query.order_by(desc(Project.created_at))
    total = query.count()
    projects = query.offset((page - 1) * size).limit(size).all()
    return projects, total

def update_project(db: Session, project_id: int, project_update: ProjectUpdate) -> Project:
    project = get_project_by_id(db, project_id)
    if project_update.name is not None:
        project.name = project_update.name
    if project_update.cover is not None:
        project.cover = project_update.cover
    if project_update.tags is not None:
        project.tags = project_update.tags
    if project_update.github_url is not None:
        project.github_url = project_update.github_url
    if project_update.demo_url is not None:
        project.demo_url = project_update.demo_url
    if project_update.summary is not None:
        project.summary = project_update.summary
    if project_update.tech_stack is not None:
        project.tech_stack = project_update.tech_stack
    if project_update.status is not None:
        project.status = project_update.status
    if project_update.description is not None:
        project.description = project_update.description
    if project_update.project_type is not None:
        project.project_type = project_update.project_type
    if project_update.start_date is not None:
        project.start_date = project_update.start_date
    if project_update.end_date is not None:
        project.end_date = project_update.end_date
    if project_update.last_update is not None:
        project.last_update = project_update.last_update
    if project_update.open_source_license is not None:
        project.open_source_license = project_update.open_source_license
    if project_update.database_type is not None:
        project.database_type = project_update.database_type
    if project_update.deployment_platform is not None:
        project.deployment_platform = project_update.deployment_platform
    if project_update.docs_url is not None:
        project.docs_url = project_update.docs_url
    if project_update.content is not None:
        project.content = project_update.content
    if project_update.catalog is not None:
        project.catalog = project_update.catalog
    if project_update.is_paid is not None:
        project.is_paid = project_update.is_paid
    if project_update.is_featured is not None:
        project.is_featured = project_update.is_featured
    if project_update.repost_url is not None:
        project.repost_url = project_update.repost_url if project_update.repost_url else None
    if project_update.category_id is not None:
        project.category_id = project_update.category_id
    if project_update.display_status is not None:
        project.display_status = project_update.display_status
    db.commit()
    db.refresh(project)
    return project

def delete_project(db: Session, project_id: int) -> None:
    project = get_project_by_id(db, project_id)
    db.query(Comment).filter(Comment.project_id == project_id).delete()
    db.delete(project)
    db.commit()

def increment_project_view_count(db: Session, project_id: int) -> None:
    project = get_project_by_id(db, project_id)
    project.view_count += 1
    db.commit()

def get_project_category_stats(db: Session) -> list:
    results = (
        db.query(
            ProjectCategory.id,
            ProjectCategory.name,
            func.count(Project.id).label("count")
        )
        .outerjoin(Project, Project.category_id == ProjectCategory.id)
        .filter(ProjectCategory.is_active == True)
        .group_by(ProjectCategory.id, ProjectCategory.name)
        .order_by(desc("count"))
        .all()
    )
    return [{"id": r.id, "name": r.name, "count": r.count} for r in results]

def get_project_tech_stack_stats(db: Session) -> list:
    projects = db.query(Project.tech_stack).filter(
        Project.tech_stack.isnot(None),
        Project.tech_stack != "[]",
        Project.display_status != "paused"
    ).all()
    stack_count = {}
    for p in projects:
        if p.tech_stack and isinstance(p.tech_stack, list):
            for stack in p.tech_stack:
                stack_count[stack] = stack_count.get(stack, 0) + 1
    sorted_stacks = sorted(stack_count.items(), key=lambda x: x[1], reverse=True)
    return [{"name": name, "count": count} for name, count in sorted_stacks]