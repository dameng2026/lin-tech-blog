"""
数据库迁移脚本：更新 categories 表结构
1. 移除 slug 和 order 字段
2. 修改 description 字段为 TEXT 类型
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import create_engine, text
from src.app.core.config import settings


def migrate_categories():
    print("开始数据库迁移...")
    print(f"数据库连接: {settings.DATABASE_URL}")

    engine = create_engine(settings.DATABASE_URL)

    with engine.connect() as conn:
        # 检查字段是否存在
        result = conn.execute(text("""
            SELECT COUNT(*) as cnt
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE table_name = 'categories' AND column_name = 'slug'
        """))
        has_slug = result.fetchone()[0] > 0

        result = conn.execute(text("""
            SELECT COUNT(*) as cnt
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE table_name = 'categories' AND column_name = 'order'
        """))
        has_order = result.fetchone()[0] > 0

        result = conn.execute(text("""
            SELECT COLUMN_TYPE
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE table_name = 'categories' AND column_name = 'description'
        """))
        desc_row = result.fetchone()
        current_type = desc_row[0] if desc_row else None

        print(f"\n当前字段状态:")
        print(f"  - slug 字段: {'存在' if has_slug else '不存在'}")
        print(f"  - order 字段: {'存在' if has_order else '不存在'}")
        print(f"  - description 类型: {current_type}")

        migrations_done = []

        # 移除 slug 字段
        if has_slug:
            conn.execute(text("ALTER TABLE categories DROP COLUMN slug"))
            migrations_done.append("移除 slug 字段")
            print(f"\n✓ 已移除 slug 字段")

        # 移除 order 字段
        if has_order:
            conn.execute(text("ALTER TABLE categories DROP COLUMN `order`"))
            migrations_done.append("移除 order 字段")
            print(f"✓ 已移除 order 字段")

        # 修改 description 字段类型
        if current_type and 'text' not in current_type.lower():
            conn.execute(text("ALTER TABLE categories MODIFY COLUMN description TEXT"))
            migrations_done.append("修改 description 字段类型为 TEXT")
            print(f"✓ 已修改 description 字段类型为 TEXT")

        conn.commit()

        if migrations_done:
            print(f"\n✓ 完成以下迁移:")
            for m in migrations_done:
                print(f"  - {m}")
        else:
            print(f"\n✓ 无需迁移，表结构已是最新")

    print("\n数据库迁移完成！")


if __name__ == "__main__":
    migrate_categories()
