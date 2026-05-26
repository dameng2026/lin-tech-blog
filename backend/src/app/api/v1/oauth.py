from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..dependencies import get_current_user
from ...crud.oauth import get_oauth_user_by_provider, create_oauth_user, update_oauth_user
from ...crud.user import create_user, get_user_by_id
from ...schemas.user import UserCreate, UserResponse, TokenResponse
from ...schemas.oauth import OAuthUserResponse
from ...models.oauth import OAuthUser
from ...security.jwt import create_access_token, create_refresh_token
from ...security.password import get_password_hash
from ...core.database import get_db
from datetime import datetime
from typing import Optional
import httpx
import json

router = APIRouter(prefix="/oauth", tags=["oauth"])

GITHUB_CLIENT_ID = "your-github-client-id"
GITHUB_CLIENT_SECRET = "your-github-client-secret"
GITHUB_REDIRECT_URI = "http://localhost:8080/api/v1/oauth/github/callback"

@router.get("/github/authorize")
def github_authorize():
    return {
        "url": f"https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&redirect_uri={GITHUB_REDIRECT_URI}&scope=user:email"
    }

@router.get("/github/callback")
async def github_callback(code: str, db: Session = Depends(get_db)):
    async with httpx.AsyncClient() as client:
        token_response = await client.post(
            "https://github.com/login/oauth/access_token",
            data={
                "client_id": GITHUB_CLIENT_ID,
                "client_secret": GITHUB_CLIENT_SECRET,
                "code": code
            },
            headers={"Accept": "application/json"}
        )
        
        token_data = token_response.json()
        if "access_token" not in token_data:
            raise HTTPException(status_code=400, detail="Failed to get access token")
        
        user_response = await client.get(
            "https://api.github.com/user",
            headers={"Authorization": f"token {token_data['access_token']}"}
        )
        
        github_user = user_response.json()
        email_response = await client.get(
            "https://api.github.com/user/emails",
            headers={"Authorization": f"token {token_data['access_token']}"}
        )
        emails = email_response.json()
        email = next((e["email"] for e in emails if e["primary"]), github_user.get("email"))
        
        oauth_user = get_oauth_user_by_provider(db, "github", str(github_user["id"]))
        
        if oauth_user:
            user = get_user_by_id(db, oauth_user.user_id)
        else:
            user = create_user(db, UserCreate(
                username=github_user["login"],
                email=email or f"{github_user['login']}@github.com",
                password=get_password_hash(f"github_{github_user['id']}_random")
            ))
            
            create_oauth_user(db, OAuthUserResponse(
                user_id=user.id,
                provider="github",
                provider_id=str(github_user["id"]),
                access_token=token_data.get("access_token"),
                refresh_token=token_data.get("refresh_token"),
                profile_data=github_user
            ))
        
        access_token = create_access_token(data={"sub": user.id})
        refresh_token = create_refresh_token(data={"sub": user.id})
        
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "user": user
        }

@router.get("/{provider}/connect", dependencies=[Depends(get_current_user)])
def connect_oauth(provider: str, current_user: UserResponse = Depends(get_current_user), db: Session = Depends(get_db)):
    if provider == "github":
        return {
            "url": f"https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&redirect_uri={GITHUB_REDIRECT_URI}&scope=user:email"
        }
    raise HTTPException(status_code=400, detail="Unsupported provider")

@router.delete("/{provider}", dependencies=[Depends(get_current_user)])
def disconnect_oauth(provider: str, current_user: UserResponse = Depends(get_current_user), db: Session = Depends(get_db)):
    oauth_user = db.query(OAuthUser).filter(
        OAuthUser.user_id == current_user.id,
        OAuthUser.provider == provider
    ).first()
    if oauth_user:
        db.delete(oauth_user)
        db.commit()
        return {"message": f"{provider} account disconnected"}
    raise HTTPException(status_code=404, detail="OAuth connection not found")