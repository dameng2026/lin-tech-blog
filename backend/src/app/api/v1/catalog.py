"""
文章目录生成相关的API端点
"""
import asyncio
import json
import re
from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from typing import Optional, List, Dict, AsyncGenerator
from ..dependencies import get_current_admin
from .auth import wrap_response
from ...crud.system_setting import get_setting_value
from ...crud.ai_config import get_default_config
from ...services.ai_proxy import ai_proxy_service
from ...schemas.catalog import CatalogGenerateRequest
from ...core.database import get_db

router = APIRouter(prefix="/catalog", tags=["catalog"])

def sse_event(event: str, data: dict) -> str:
    """格式化 SSE 事件"""
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"

async def generate_catalog_stream(content: str, db: Session) -> AsyncGenerator[str, None]:
    """流式生成文章目录，通过 SSE 事件推送实时进度"""

    yield sse_event("progress", {"stage": "preprocess", "stage_name": "正在预处理内容...", "progress": 10})
    await asyncio.sleep(0.2)

    yield sse_event("progress", {"stage": "strip_images", "stage_name": "正在移除图片资源...", "progress": 25})
    clean_content = re.sub(r'<img[^>]*>', '', content)
    await asyncio.sleep(0.2)

    yield sse_event("progress", {"stage": "analyze", "stage_name": "正在分析文章结构...", "progress": 45})
    await asyncio.sleep(0.2)

    yield sse_event("progress", {"stage": "generate", "stage_name": "正在生成章节目录...", "progress": 70})

    try:
        ai_enabled = get_setting_value(db, "ai_model_enabled", False)
        catalog = []
        ai_used = False

        if ai_enabled:
            config = get_default_config(db)
            if config:
                catalog = await ai_proxy_service.generate_catalog(clean_content, config)
                ai_used = True

        if not catalog:
            yield sse_event("progress", {"stage": "generate", "stage_name": "正在提取本地章节...", "progress": 80})
            catalog = ai_proxy_service.extract_catalog_from_html(clean_content)
            ai_used = False

        yield sse_event("progress", {"stage": "format", "stage_name": "正在整理目录层级...", "progress": 90})
        await asyncio.sleep(0.2)

        yield sse_event("complete", {"catalog": catalog, "ai_used": ai_used, "total_stages": 5})

    except Exception as e:
        print(f"Catalog generation error: {e}")
        catalog = ai_proxy_service.extract_catalog_from_html(clean_content)
        yield sse_event("complete", {
            "catalog": catalog, "ai_used": False,
            "msg": f"AI生成失败，已使用本地提取",
            "total_stages": 5
        })

@router.post("/generate")
def generate_catalog(
    request: CatalogGenerateRequest = Body(...),
    db: Session = Depends(get_db)
):
    """生成文章目录"""
    content = request.content
    use_ai = request.use_ai

    try:
        ai_enabled = get_setting_value(db, "ai_model_enabled", False)

        catalog = []

        if use_ai and ai_enabled:
            config = get_default_config(db)
            catalog = ai_proxy_service.generate_catalog_sync(content, config)
        else:
            catalog = ai_proxy_service.extract_catalog_from_html(content)

        return wrap_response(data={"catalog": catalog, "ai_used": use_ai and ai_enabled})

    except Exception as e:
        print(f"Catalog generation error: {e}")
        catalog = ai_proxy_service.extract_catalog_from_html(content)
        return wrap_response(data={"catalog": catalog, "ai_used": False, "msg": "AI生成失败，已使用本地提取"})

@router.post("/generate-with-check")
def generate_catalog_with_check(
    request: CatalogGenerateRequest = Body(...),
    db: Session = Depends(get_db)
):
    content = request.content
    """生成文章目录（带开关检查）"""
    ai_enabled = get_setting_value(db, "ai_model_enabled", False)

    if not ai_enabled:
        return wrap_response(
            code=400,
            msg="模型调用功能已关闭，请先在系统设置中开启功能",
            data={"enabled": False}
        )

    try:
        config = get_default_config(db)

        if not config:
            catalog = ai_proxy_service.extract_catalog_from_html(content)
            return wrap_response(data={"catalog": catalog, "ai_used": False, "msg": "未配置AI模型，使用本地提取"})

        catalog = ai_proxy_service.generate_catalog_sync(content, config)

        return wrap_response(data={"catalog": catalog, "ai_used": True})

    except Exception as e:
        print(f"Catalog generation error: {e}")
        catalog = ai_proxy_service.extract_catalog_from_html(content)
        return wrap_response(data={"catalog": catalog, "ai_used": False, "msg": f"AI生成失败: {str(e)[:50]}，已使用本地提取"})

@router.post("/generate-stream")
async def generate_catalog_stream_endpoint(
    request: CatalogGenerateRequest = Body(...),
    db: Session = Depends(get_db)
):
    """流式生成目录，实时推送进度事件"""
    return StreamingResponse(
        generate_catalog_stream(request.content, db),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        }
    )
