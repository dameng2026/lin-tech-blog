from sqlalchemy.orm import Session
from ..models.oauth import OAuthUser
from ..schemas.oauth import OAuthUserCreate

def get_oauth_user_by_provider(db: Session, provider: str, provider_id: str):
    return db.query(OAuthUser).filter(
        OAuthUser.provider == provider,
        OAuthUser.provider_id == provider_id
    ).first()

def create_oauth_user(db: Session, oauth_user_create: OAuthUserCreate):
    oauth_user = OAuthUser(
        user_id=oauth_user_create.user_id,
        provider=oauth_user_create.provider,
        provider_id=oauth_user_create.provider_id,
        access_token=oauth_user_create.access_token,
        refresh_token=oauth_user_create.refresh_token,
        expires_at=oauth_user_create.expires_at,
        profile_data=oauth_user_create.profile_data
    )
    db.add(oauth_user)
    db.commit()
    db.refresh(oauth_user)
    return oauth_user

def update_oauth_user(db: Session, oauth_user_id: int, access_token: str = None, refresh_token: str = None, expires_at: int = None):
    oauth_user = db.query(OAuthUser).filter(OAuthUser.id == oauth_user_id).first()
    if not oauth_user:
        return None
    if access_token:
        oauth_user.access_token = access_token
    if refresh_token:
        oauth_user.refresh_token = refresh_token
    if expires_at:
        oauth_user.expires_at = expires_at
    db.commit()
    db.refresh(oauth_user)
    return oauth_user