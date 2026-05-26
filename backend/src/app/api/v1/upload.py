from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
import os
import uuid
from typing import List
from ..dependencies import get_current_admin
from ..v1.auth import wrap_response
from ...core.config import settings
from ...core.database import get_db

router = APIRouter(prefix="/upload", tags=["upload"])

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "pdf", "svg"}

def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def save_upload_file(file: UploadFile) -> str:
    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="File type not allowed")

    if file.size and file.size > settings.MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File size exceeds limit")

    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

    ext = file.filename.rsplit(".", 1)[1].lower()
    filename = f"{uuid.uuid4()}.{ext}"
    file_path = os.path.join(settings.UPLOAD_DIR, filename)

    return filename, file_path

@router.post("/image")
async def upload_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin)
):
    filename, file_path = save_upload_file(file)
    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)
    return wrap_response(data={"url": f"/uploads/{filename}"})

@router.post("/batch")
async def upload_batch(
    files: List[UploadFile] = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin)
):
    urls = []
    for file in files:
        filename, file_path = save_upload_file(file)
        contents = await file.read()
        with open(file_path, "wb") as f:
            f.write(contents)
        urls.append(f"/uploads/{filename}")
    return wrap_response(data={"urls": urls, "filenames": urls})

@router.post("/file")
async def upload_file_generic(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin)
):
    filename, file_path = save_upload_file(file)
    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)
    return wrap_response(data={"url": f"/uploads/{filename}"})