from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from .api import api_router
from .core.config import settings
from .core.database import engine, Base
from .core.exceptions import CustomHTTPException
import os
import traceback
import sys

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lin Tech Blog API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3006",
        "http://127.0.0.1:3006",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_origin_regex="https?://(localhost|127\\.0\\.0\\.1):(3006|517[0-9])",
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["Content-Type", "Authorization"],
)

os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=settings.UPLOAD_DIR), name="uploads")

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Lin Tech Blog API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.on_event("startup")
async def startup_event():
    if settings.SECRET_KEY == "your-secret-key-here-change-in-production":
        print("============================================")
        print("WARNING: Using default SECRET_KEY!")
        print("Please set a strong SECRET_KEY in .env file")
        print("============================================")
    if settings.ENVIRONMENT != "development":
        if settings.SECRET_KEY == "your-secret-key-here-change-in-production":
            print("ERROR: Cannot use default SECRET_KEY in production!")
            sys.exit(1)

# 全局异常处理
@app.exception_handler(CustomHTTPException)
async def custom_http_exception_handler(request: Request, exc: CustomHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": exc.status_code, "msg": exc.detail, "data": None}
    )

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": exc.status_code, "msg": exc.detail, "data": None}
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        field = ".".join(str(x) for x in error["loc"])
        errors.append(f"{field}: {error['msg']}")
    return JSONResponse(
        status_code=400,
        content={"code": 400, "msg": "Validation Error", "data": errors}
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print(f"Unexpected error: {exc}")
    traceback.print_exc()
    return JSONResponse(
        status_code=500,
        content={"code": 500, "msg": "服务器内部错误，请稍后重试", "data": None}
    )