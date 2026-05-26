"""
数据库修复脚本：
1. 检查并添加 articles 表中缺失的列
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import create_engine, text
from src.app.core.config import settings


def fix_database():
    print("开始修复数据库...")
    print(f"数据库连接: {settings.DATABASE_URL}")

    engine = create_engine(settings.DATABASE_URL)

    with engine.connect() as conn:
        columns_to_add = [
            ("catalog", "JSON"),
            ("allow_comment", "BOOLEAN DEFAULT true"),
            ("author_name", "VARCHAR(100)"),
            ("author_avatar", "VARCHAR(500)"),
            ("author_bio", "TEXT"),
            ("seo_title", "VARCHAR(255)"),
            ("seo_keywords", "VARCHAR(500)"),
            ("seo_description", "TEXT"),
        ]

        for column_name, column_type in columns_to_add:
            result = conn.execute(text("""
                SELECT COUNT(*) 
                FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE table_name = 'articles' AND column_name = :col_name
            """), {"col_name": column_name})
            has_column = result.scalar() > 0

            if not has_column:
                conn.execute(text(f"ALTER TABLE articles ADD COLUMN {column_name} {column_type}"))
                print(f"✓ 已添加 {column_name} 列到 articles 表")
            else:
                print(f"✓ {column_name} 列已存在")

        conn.commit()

    print("\n数据库修复完成！")


if __name__ == "__main__":
    fix_database()