"""
数据库迁移脚本：
1. 为 experiences 表添加 tags 列
2. 为 site_settings 表添加 bio_motto, bio_motto_items, bio_interests 列
3. 插入默认模板数据
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import create_engine, text, inspect
from src.app.core.config import settings


def run_migration():
    print("开始数据库迁移...")
    print(f"数据库连接: {settings.DATABASE_URL}")

    engine = create_engine(settings.DATABASE_URL)
    inspector = inspect(engine)

    with engine.connect() as conn:
        # 1. experiences 表添加 tags 列
        if "experiences" in inspector.get_table_names():
            columns = [c["name"] for c in inspector.get_columns("experiences")]
            if "tags" not in columns:
                conn.execute(text("ALTER TABLE experiences ADD COLUMN tags JSON DEFAULT ('[]')"))
                print("✓ experiences 表已添加 tags 列")
            else:
                print("- experiences.tags 列已存在")
        else:
            print("- experiences 表不存在，跳过")

        # 2. site_settings 表添加新列
        if "site_settings" in inspector.get_table_names():
            columns = [c["name"] for c in inspector.get_columns("site_settings")]
            for col_name, col_def in [
                ("bio_motto", "TEXT"),
                ("bio_motto_items", "TEXT"),
                ("bio_interests", "TEXT"),
            ]:
                if col_name not in columns:
                    conn.execute(text(f"ALTER TABLE site_settings ADD COLUMN {col_name} {col_def}"))
                    print(f"✓ site_settings 表已添加 {col_name} 列")
                else:
                    print(f"- site_settings.{col_name} 列已存在")

        # 3. 插入默认模板数据到 site_settings 首页数据
        result = conn.execute(text("SELECT id, bio_motto, bio_motto_items, bio_interests FROM site_settings LIMIT 1"))
        row = result.fetchone()
        if row:
            needs_update = False
            updates = []
            if not row[1]:  # bio_motto
                updates.append("bio_motto = '技术的价值不在于复杂，而在于解决问题；产品的价值不在于功能，而在于用户体验。'")
                needs_update = True
            if not row[2]:  # bio_motto_items
                updates.append("bio_motto_items = '持续学习，保持好奇心\n注重工程质量与用户体验\n用技术创造实际价值\n开放分享，互相成长'")
                needs_update = True
            if not row[3]:  # bio_interests
                updates.append("bio_interests = '技术探索,开源贡献,阅读写作,旅行,健身运动'")
                needs_update = True
            if needs_update:
                set_clause = ", ".join(updates)
                conn.execute(text(f"UPDATE site_settings SET {set_clause} WHERE id = {row[0]}"))
                print("✓ 默认模板数据已插入 site_settings")
            else:
                print("- 模板数据已存在，跳过")
        else:
            print("- site_settings 表无数据，跳过")

        conn.commit()

    print("\n数据库迁移完成！")


if __name__ == "__main__":
    run_migration()