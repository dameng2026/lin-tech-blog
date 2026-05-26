from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional
from ..crud.user import get_user_by_id
from ..schemas.user import UserResponse
from ..security.jwt import verify_token
from ..core.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login", auto_error=False)

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> UserResponse:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if not token:
        raise credentials_exception

    payload = verify_token(token)
    user_id = payload.get("sub")
    if user_id is None:
        raise credentials_exception

    user = get_user_by_id(db, user_id)
    if user is None:
        raise credentials_exception

    return user

async def get_current_admin(
    current_user: UserResponse = Depends(get_current_user)
) -> UserResponse:
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    return current_user

async def get_current_user_optional(
    token: Optional[str] = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> Optional[UserResponse]:
    if not token:
        return None
    try:
        payload = verify_token(token)
        user_id = payload.get("sub")
        if user_id is None:
            return None
        user = get_user_by_id(db, user_id)
        return user
    except Exception:
        return None

async def get_current_admin_optional(
    current_user: Optional[UserResponse] = Depends(get_current_user_optional)
) -> Optional[UserResponse]:
    if current_user and current_user.role == "admin":
        return current_user
    return None