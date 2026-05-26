from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import secrets
import string
from ..dependencies import get_current_admin
from ..v1.auth import wrap_response
from ...models.resume_key import ResumeKey
from ...core.database import get_db

router = APIRouter(prefix="/resume-keys", tags=["resume-keys"])

def generate_key(length=12):
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))

@router.get("/")
def list_keys(db: Session = Depends(get_db), current_user = Depends(get_current_admin)):
    keys = db.query(ResumeKey).order_by(ResumeKey.created_at.desc()).all()
    now = datetime.now()
    result = []
    for k in keys:
        displayed = k.key_value[:4] + '*' * (len(k.key_value) - 8) + k.key_value[-4:] if len(k.key_value) > 8 else '****'
        is_expired = k.expire_at < now
        if is_expired and k.is_active:
            k.is_active = False
            db.commit()
        result.append({
            "id": k.id,
            "key_display": displayed,
            "created_at": k.created_at.isoformat(),
            "expire_at": k.expire_at.isoformat(),
            "is_active": k.is_active and not is_expired,
            "use_count": k.use_count
        })
    return wrap_response(data=result)

@router.post("/")
def create_key(
    length: int = 12,
    valid_hours: int = 1,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin)
):
    if length < 8 or length > 16:
        raise HTTPException(status_code=400, detail="密钥长度必须在8-16位之间")
    key_value = generate_key(length)
    expire_at = datetime.now() + timedelta(hours=valid_hours)
    resume_key = ResumeKey(key_value=key_value, expire_at=expire_at)
    db.add(resume_key)
    db.commit()
    db.refresh(resume_key)
    return wrap_response(data={"id": resume_key.id, "key_value": key_value, "expire_at": expire_at.isoformat()})

@router.delete("/{key_id}")
def delete_key(key_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_admin)):
    key = db.query(ResumeKey).filter(ResumeKey.id == key_id).first()
    if not key:
        raise HTTPException(status_code=404, detail="密钥不存在")
    db.delete(key)
    db.commit()
    return wrap_response(data={"message": "密钥已删除"})

@router.get("/validate/{key_value}")
def validate_key(key_value: str, db: Session = Depends(get_db)):
    key = db.query(ResumeKey).filter(ResumeKey.key_value == key_value, ResumeKey.is_active == True).first()
    if not key:
        return wrap_response(data={"valid": False, "message": "密钥无效"})
    if key.expire_at < datetime.now():
        key.is_active = False
        db.commit()
        return wrap_response(data={"valid": False, "message": "密钥已过期"})
    key.use_count += 1
    db.commit()
    return wrap_response(data={"valid": True})