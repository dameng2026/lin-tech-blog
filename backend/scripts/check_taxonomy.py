"""
检查 taxonomy 数据表结构和数据
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import create_engine, text, inspect
from src.app.core.config import settings


def check_taxonomy():
    print("开始检查 taxonomy 数据...")
    print(f"数据库连接: {settings.DATABASE_URL}")

    engine = create_engine(settings.DATABASE_URL)
    inspector = inspect(engine)

    # 检查表是否存在
    tables = inspector.get_table_names()
    print(f"\n所有表: {tables}")

    # 检查 categories 表
    if 'categories' in tables:
        print("\n✓ categories 表存在")
        columns = inspector.get_columns('categories')
        print(f"  列: {[c['name'] for c in columns]}")

        with engine.connect() as conn:
            result = conn.execute(text('SELECT * FROM categories'))
            rows = result.fetchall()
            print(f"  总记录数: {len(rows)}")
            if rows:
                for row in rows:
                    print(f"    - {row}")
            else:
                print("  ⚠ 表为空")
    else:
        print("\n✗ categories 表不存在")

    # 检查 tags 表
    if 'tags' in tables:
        print("\n✓ tags 表存在")
        columns = inspector.get_columns('tags')
        print(f"  列: {[c['name'] for c in columns]}")

        with engine.connect() as conn:
            result = conn.execute(text('SELECT * FROM tags'))
            rows = result.fetchall()
            print(f"  总记录数: {len(rows)}")
            if rows:
                for row in rows:
                    print(f"    - {row}")
            else:
                print("  ⚠ 表为空")
    else:
        print("\n✗ tags 表不存在")


if __name__ == "__main__":
    check_taxonomy()
