from pydantic import BaseModel

class OAuthUserCreate(BaseModel):
    user_id: int
    provider: str
    provider_id: str
    access_token: str = None
    refresh_token: str = None
    expires_at: int = None
    profile_data: dict = None

class OAuthUserResponse(BaseModel):
    id: int
    user_id: int
    provider: str
    provider_id: str
    created_at: str

    class Config:
        from_attributes = True