from sqlalchemy.orm import Session
from sqlalchemy import or_
from ..models.user import User
from ..schemas.user import UserCreate, UserUpdate
from ..security.password import get_password_hash, verify_password
from ..core.exceptions import NotFoundException, ConflictException, BadRequestException

def create_user(db: Session, user_create: UserCreate) -> User:
    db_user = db.query(User).filter(
        or_(User.username == user_create.username, User.email == user_create.email)
    ).first()
    if db_user:
        raise ConflictException("Username or email already exists")
    
    hashed_password = get_password_hash(user_create.password)
    user = User(
        username=user_create.username,
        email=user_create.email,
        password_hash=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db: Session, user_id: int) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise NotFoundException("用户不存在")
    return user

def get_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str) -> User:
    return db.query(User).filter(User.username == username).first()

def update_user(db: Session, user_id: int, user_update: UserUpdate) -> User:
    user = get_user_by_id(db, user_id)
    if user_update.nickname is not None:
        user.nickname = user_update.nickname
    if user_update.avatar is not None:
        user.avatar = user_update.avatar
    if user_update.bio is not None:
        user.bio = user_update.bio
    if user_update.city is not None:
        user.city = user_update.city
    if user_update.social_links is not None:
        user.social_links = user_update.social_links
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int) -> None:
    user = get_user_by_id(db, user_id)
    db.delete(user)
    db.commit()

def authenticate_user(db: Session, username: str = None, email: str = None, password: str = None) -> User:
    if email:
        user = get_user_by_email(db, email)
    elif username:
        user = get_user_by_username(db, username)
    else:
        raise BadRequestException("用户名或邮箱不能为空")
    
    if not user:
        raise NotFoundException("账号或密码错误")
    
    if password and not verify_password(password, user.password_hash):
        raise BadRequestException("账号或密码错误")
    
    return user