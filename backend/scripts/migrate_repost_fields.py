"""
数据库迁移脚本：添加转载相关字段
1. 添加 source_type 字段（默认值为 'original'）
2. 添加 repost_url 字段
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import create_engine, text
from src.app.core.config import settings


def migrate_articles():
    print("开始数据库迁移...")
    print(f"数据库连接: {settings.DATABASE_URL}")

    engine = create_engine(settings.DATABASE_URL)

    with engine.connect() as conn:
        # 检查 source_type 字段是否存在
        result = conn.execute(text("""
            SELECT COUNT(*) as cnt
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE table_name = 'articles' AND column_name = 'source_type'
        """))
        has_source_type = result.fetchone()[0] > 0

        # 检查 repost_url 字段是否存在
        result = conn.execute(text("""
            SELECT COUNT(*) as cnt
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE table_name = 'articles' AND column_name = 'repost_url'
        """))
        has_repost_url = result.fetchone()[0] > 0

        print(f"\n当前字段状态:")
        print(f"  - source_type 字段: {'已存在' if has_source_type else '不存在'}")
        print(f"  - repost_url 字段: {'已存在' if has_repost_url else '不存在'}")

        migrations_done = []

        # 添加 source_type 字段
        if not has_source_type:
            conn.execute(text("""
                ALTER TABLE articles
                ADD COLUMN source_type VARCHAR(20) NOT NULL DEFAULT 'original'
            """))
            migrations_done.append("添加 source_type 字段（默认值为 'original'）")
            print(f"\n✓ 已添加 source_type 字段")

        # 添加 repost_url 字段
        if not has_repost_url:
            conn.execute(text("""
                ALTER TABLE articles
                ADD COLUMN repost_url VARCHAR(500)
            """))
            migrations_done.append("添加 repost_url 字段")
            print(f"✓ 已添加 repost_url 字段")

        conn.commit()

        if migrations_done:
            print(f"\n✓ 完成以下迁移:")
            for m in migrations_done:
                print(f"  - {m}")
        else:
            print(f"\n✓ 无需迁移，表结构已是最新")

    print("\n数据库迁移完成！")


if __name__ == "__main__":
    migrate_articles()
