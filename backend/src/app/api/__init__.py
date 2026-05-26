from fastapi import APIRouter
from .v1.auth import router as auth_router
from .v1.articles import router as articles_router
from .v1.comments import router as comments_router
from .v1.dashboard import router as dashboard_router
from .v1.projects import router as projects_router
from .v1.friend_links import router as friend_links_router
from .v1.profile import router as profile_router
from .v1.statistics import router as statistics_router
from .v1.upload import router as upload_router
from .v1.oauth import router as oauth_router
from .v1.taxonomy import router as taxonomy_router
from .v1.settings import router as settings_router
from .v1.users import router as users_router
from .v1.ai_config import router as ai_config_router
from .v1.catalog import router as catalog_router
from .v1.project_categories import router as project_categories_router
from .v1.friend_link_categories import router as friend_link_categories_router
from .v1.system import router as system_router
from .v1.roles import router as roles_router
from .v1.resume_keys import router as resume_keys_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth_router)
api_router.include_router(oauth_router)
api_router.include_router(articles_router)
api_router.include_router(comments_router)
api_router.include_router(dashboard_router)
api_router.include_router(projects_router)
api_router.include_router(friend_links_router)
api_router.include_router(profile_router)
api_router.include_router(statistics_router)
api_router.include_router(upload_router)
api_router.include_router(taxonomy_router)
api_router.include_router(settings_router)
api_router.include_router(users_router)
api_router.include_router(ai_config_router)
api_router.include_router(catalog_router)
api_router.include_router(project_categories_router)
api_router.include_router(friend_link_categories_router)
api_router.include_router(system_router)
api_router.include_router(roles_router)
api_router.include_router(resume_keys_router)
