import random
import string
from ..core.redis import redis_client
from ..core.config import settings

def generate_verify_code(length: int = 6) -> str:
    return ''.join(random.choices(string.digits, k=length))

def store_verify_code(key: str, code: str) -> None:
    redis_client.setex(key, settings.VERIFY_CODE_EXPIRE_SECONDS, code)

def verify_code(key: str, code: str) -> bool:
    stored_code = redis_client.get(key)
    if stored_code is None:
        return False
    return stored_code.decode() == code

def delete_verify_code(key: str) -> None:
    redis_client.delete(key)