"""
数据库迁移脚本：更新 comments 表结构
1. 添加 guest_name 字段
2. 添加 guest_email 字段
3. 添加 ip_address 字段
4. 修改 user_id 字段为可空
5. 添加复合索引
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import create_engine, text
from src.app.core.config import settings


def migrate_comments():
    print("开始数据库迁移...")
    print(f"数据库连接: {settings.DATABASE_URL}")

    engine = create_engine(settings.DATABASE_URL)

    with engine.connect() as conn:
        # 检查字段是否存在
        checks = {}
        for col in ["guest_name", "guest_email", "ip_address"]:
            result = conn.execute(text(f"""
                SELECT COUNT(*) as cnt
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE table_name = 'comments' AND column_name = '{col}'
            """))
            checks[col] = result.fetchone()[0] > 0

        # 检查 user_id 是否可空
        result = conn.execute(text("""
            SELECT IS_NULLABLE
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE table_name = 'comments' AND column_name = 'user_id'
        """))
        user_id_nullable = result.fetchone()
        user_id_is_nullable = user_id_nullable and user_id_nullable[0] == 'YES' if user_id_nullable else True

        # 检查索引是否存在
        result = conn.execute(text("""
            SELECT COUNT(*) as cnt
            FROM INFORMATION_SCHEMA.STATISTICS
            WHERE table_name = 'comments' AND index_name = 'idx_article_created'
        """))
        has_idx_article_created = result.fetchone()[0] > 0

        result = conn.execute(text("""
            SELECT COUNT(*) as cnt
            FROM INFORMATION_SCHEMA.STATISTICS
            WHERE table_name = 'comments' AND index_name = 'idx_article_likes'
        """))
        has_idx_article_likes = result.fetchone()[0] > 0

        result = conn.execute(text("""
            SELECT COUNT(*) as cnt
            FROM INFORMATION_SCHEMA.STATISTICS
            WHERE table_name = 'comments' AND index_name = 'idx_ip_created'
        """))
        has_idx_ip_created = result.fetchone()[0] > 0

        print(f"\n当前字段状态:")
        print(f"  - guest_name 字段: {'已存在' if checks['guest_name'] else '不存在'}")
        print(f"  - guest_email 字段: {'已存在' if checks['guest_email'] else '不存在'}")
        print(f"  - ip_address 字段: {'已存在' if checks['ip_address'] else '不存在'}")
        print(f"  - user_id 可空: {'是' if user_id_is_nullable else '否'}")
        print(f"  - idx_article_created 索引: {'已存在' if has_idx_article_created else '不存在'}")
        print(f"  - idx_article_likes 索引: {'已存在' if has_idx_article_likes else '不存在'}")
        print(f"  - idx_ip_created 索引: {'已存在' if has_idx_ip_created else '不存在'}")

        migrations_done = []

        # 添加 guest_name 字段
        if not checks["guest_name"]:
            conn.execute(text("""
                ALTER TABLE comments
                ADD COLUMN guest_name VARCHAR(100)
            """))
            migrations_done.append("添加 guest_name 字段")
            print(f"\n✓ 已添加 guest_name 字段")

        # 添加 guest_email 字段
        if not checks["guest_email"]:
            conn.execute(text("""
                ALTER TABLE comments
                ADD COLUMN guest_email VARCHAR(255)
            """))
            migrations_done.append("添加 guest_email 字段")
            print(f"✓ 已添加 guest_email 字段")

        # 添加 ip_address 字段
        if not checks["ip_address"]:
            conn.execute(text("""
                ALTER TABLE comments
                ADD COLUMN ip_address VARCHAR(45)
            """))
            migrations_done.append("添加 ip_address 字段")
            print(f"✓ 已添加 ip_address 字段")

        # 修改 user_id 为可空
        if not user_id_is_nullable:
            conn.execute(text("""
                ALTER TABLE comments
                MODIFY COLUMN user_id INT
            """))
            migrations_done.append("修改 user_id 字段为可空")
            print(f"✓ 已修改 user_id 字段为可空")

        # 添加复合索引
        if not has_idx_article_created:
            conn.execute(text("""
                CREATE INDEX idx_article_created ON comments(article_id, created_at)
            """))
            migrations_done.append("添加 idx_article_created 索引")
            print(f"✓ 已添加 idx_article_created 索引")

        if not has_idx_article_likes:
            conn.execute(text("""
                CREATE INDEX idx_article_likes ON comments(article_id, like_count)
            """))
            migrations_done.append("添加 idx_article_likes 索引")
            print(f"✓ 已添加 idx_article_likes 索引")

        if not has_idx_ip_created:
            conn.execute(text("""
                CREATE INDEX idx_ip_created ON comments(ip_address, created_at)
            """))
            migrations_done.append("添加 idx_ip_created 索引")
            print(f"✓ 已添加 idx_ip_created 索引")

        conn.commit()

        if migrations_done:
            print(f"\n✓ 完成以下迁移:")
            for m in migrations_done:
                print(f"  - {m}")
        else:
            print(f"\n✓ 无需迁移，表结构已是最新")

    print("\n数据库迁移完成！")


if __name__ == "__main__":
    migrate_comments()