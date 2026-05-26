"""
内容过滤服务
用于评论内容的安全检查，包括违禁词检测、广告模式识别、频率限制
"""
import re
import time
from typing import Dict, Tuple
from sqlalchemy.orm import Session
from ..crud.system_setting import get_setting_value


def get_prohibited_words(db: Session) -> list:
    """从系统设置中获取违禁词列表"""
    words_str = get_setting_value(db, "prohibited_words", "")
    if not words_str:
        return []
    words = [w.strip() for w in words_str.replace("\n", ",").split(",")]
    return [w for w in words if w]


def check_content(content: str, db: Session) -> Tuple[bool, str]:
    """
    检查评论内容是否包含违规内容
    返回 (是否通过, 提示信息)
    """
    if not content or not content.strip():
        return False, "评论内容不能为空"

    if len(content) > 2000:
        return False, "评论内容不能超过2000个字符"

    # 1. 违禁词检测
    prohibited_words = get_prohibited_words(db)
    for word in prohibited_words:
        if word in content:
            return False, "评论内容包含不当信息，请修改后重新提交"

    # 2. 广告模式检测
    ad_patterns = [
        r"(?:联系|添加|加)\s*(?:微信|QQ|V信|vx|薇信)",
        r"(?:扫码|扫描)\s*(?:二维码|关注)",
        r"(?:点击|进入)\s*(?:链接|网址)",
        r"https?://(?:[^\s/$.?#].[^\s]*)",
        r"(?:兼职|刷单|日赚|月入|招代理|招合作)",
        r"(?:免费.*?领取|限时.*?优惠|名额有限)",
    ]
    for pattern in ad_patterns:
        if re.search(pattern, content):
            return False, "评论内容包含广告信息"

    return True, ""


def get_client_ip(request) -> str:
    """从请求中获取客户端IP地址"""
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    real_ip = request.headers.get("X-Real-IP")
    if real_ip:
        return real_ip.strip()
    return request.client.host if request.client else "unknown"


_rate_limit_cache: Dict[str, list] = {}


def check_rate_limit(ip_address: str) -> Tuple[bool, str]:
    """
    检查IP评论频率限制
    同一IP 10秒内最多3次，24小时内最多100次
    """
    now = time.time()
    if ip_address not in _rate_limit_cache:
        _rate_limit_cache[ip_address] = []

    timestamps = _rate_limit_cache[ip_address]
    timestamps = [t for t in timestamps if now - t < 86400]
    _rate_limit_cache[ip_address] = timestamps

    recent = [t for t in timestamps if now - t < 10]
    if len(recent) >= 3:
        remaining = int(10 - (now - recent[0]))
        return False, f"评论过于频繁，请{remaining}秒后再试"

    if len(timestamps) >= 100:
        return False, "今日评论次数已达上限"

    timestamps.append(now)
    return True, ""