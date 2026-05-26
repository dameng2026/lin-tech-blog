from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..dependencies import get_current_user, get_current_admin
from ...crud.user import create_user, authenticate_user, update_user, get_user_by_id
from ...schemas.user import UserCreate, UserLogin, UserUpdate, UserResponse, TokenResponse, VerifyCodeRequest, ResetPasswordRequest, ChangePasswordRequest
from ...security.jwt import create_access_token, create_refresh_token
from ...utils.verify_code import generate_verify_code, store_verify_code, verify_code, delete_verify_code
from ...core.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

def wrap_response(code: int = 200, msg: str = "success", data: any = None):
    return {"code": code, "msg": msg, "data": data}

@router.post("/register")
def register(user_create: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user_create)
    user_dict = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "nickname": user.nickname,
        "avatar": user.avatar,
        "bio": user.bio,
        "city": user.city,
        "social_links": user.social_links,
        "role": user.role,
        "created_at": user.created_at.isoformat()
    }
    return wrap_response(data=user_dict)

@router.post("/login")
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    try:
        username = user_login.userName or user_login.username
        user = authenticate_user(db, username, user_login.email, user_login.password)
        if not user:
            raise HTTPException(status_code=401, detail="账号或密码错误")
        access_token = create_access_token(data={"sub": user.id})
        refresh_token = create_refresh_token(data={"sub": user.id})
        return wrap_response(data={
            "token": access_token,
            "refreshToken": refresh_token
        })
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        print(f"Login error: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"服务器内部错误：{str(e)}")

@router.post("/verify-code")
def send_verify_code(request: VerifyCodeRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, email=request.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    code = generate_verify_code()
    store_verify_code(f"verify_code:{request.email}", code)
    
    return wrap_response(msg="Verification code sent")

@router.post("/login-with-code")
def login_with_code(user_login: UserLogin, db: Session = Depends(get_db)):
    if not user_login.email or not user_login.code:
        raise HTTPException(status_code=400, detail="Email and code are required")
    
    if not verify_code(f"verify_code:{user_login.email}", user_login.code):
        raise HTTPException(status_code=400, detail="Invalid or expired verification code")
    
    user = authenticate_user(db, email=user_login.email)
    delete_verify_code(f"verify_code:{user_login.email}")
    
    access_token = create_access_token(data={"sub": user.id})
    refresh_token = create_refresh_token(data={"sub": user.id})
    return wrap_response(data={
        "token": access_token,
        "refreshToken": refresh_token
    })

@router.post("/reset-password")
def reset_password(request: ResetPasswordRequest, db: Session = Depends(get_db)):
    if not verify_code(f"verify_code:{request.email}", request.code):
        raise HTTPException(status_code=400, detail="Invalid or expired verification code")
    
    user = authenticate_user(db, email=request.email)
    from ...security.password import get_password_hash
    user.password_hash = get_password_hash(request.new_password)
    db.commit()
    delete_verify_code(f"verify_code:{request.email}")
    
    return wrap_response(msg="Password reset successfully")

@router.get("/me")
def get_current_user_info(current_user: UserResponse = Depends(get_current_user)):
    role_map = {
        "admin": "R_ADMIN",
        "user": "R_USER",
        "super": "R_SUPER"
    }
    return wrap_response(data={
        "userId": current_user.id,
        "userName": current_user.username,
        "email": current_user.email,
        "avatar": current_user.avatar,
        "roles": [role_map.get(current_user.role, current_user.role)],
        "buttons": []
    })

@router.post("/change-password")
def change_password(
    req: ChangePasswordRequest,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    from ...security.password import verify_password, get_password_hash
    
    if not req.old_password or not req.new_password:
        raise HTTPException(status_code=400, detail="请输入当前密码和新密码")
    
    if len(req.new_password) < 6:
        raise HTTPException(status_code=400, detail="新密码长度不能少于6位")
    
    if not verify_password(req.old_password, current_user.password_hash):
        raise HTTPException(status_code=400, detail="当前密码不正确")
    
    if req.old_password == req.new_password:
        raise HTTPException(status_code=400, detail="新密码不能与当前密码相同")
    
    current_user.password_hash = get_password_hash(req.new_password)
    db.commit()
    
    return wrap_response(msg="密码修改成功")

@router.put("/me")
def update_current_user(
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    user = update_user(db, current_user.id, user_update)
    user_dict = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "nickname": user.nickname,
        "avatar": user.avatar,
        "bio": user.bio,
        "city": user.city,
        "social_links": user.social_links,
        "role": user.role,
        "created_at": user.created_at.isoformat()
    }
    return wrap_response(data=user_dict)
