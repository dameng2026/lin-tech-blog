"""
数据库初始化脚本：
1. 删除 admin 和 admins 表（简化后不再需要）
2. 清空 users 表
3. 插入管理员账号：admin / 12356
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import bcrypt
from sqlalchemy import create_engine, MetaData, Table, insert
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.app.core.config import settings


def get_password_hash(password: str) -> str:
    password_bytes = password[:72].encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')


def init_database():
    print("开始数据库初始化...")
    print(f"数据库连接: {settings.DATABASE_URL}")

    engine = create_engine(settings.DATABASE_URL)
    metadata = MetaData()
    metadata.reflect(bind=engine)

    with engine.connect() as conn:
        conn.execute(text("SET FOREIGN_KEY_CHECKS = 0"))

        for tbl in ["admin", "admins"]:
            if tbl in metadata.tables:
                conn.execute(text(f"DROP TABLE IF EXISTS {tbl}"))
                print(f"✓ 已删除 {tbl} 表")

        if "users" in metadata.tables:
            conn.execute(text("DELETE FROM users"))
            print("✓ 已清空 users 表")

        conn.execute(text("SET FOREIGN_KEY_CHECKS = 1"))
        conn.commit()

    password_hash = get_password_hash("12356")

    with Session(engine) as session:
        users_table = Table("users", metadata, autoload_with=engine)
        result = session.execute(
            insert(users_table).values(
                username="admin",
                email="admin@blog.com",
                password_hash=password_hash,
                role="admin",
                nickname="系统管理员",
                is_active=True
            )
        )
        session.commit()
        admin_id = result.inserted_primary_key[0]

        print(f"✓ 管理员账号已创建: id={admin_id}, username=admin, password=12356")

    print("\n数据库初始化完成！")


if __name__ == "__main__":
    init_database()
