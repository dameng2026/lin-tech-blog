"""
初始化默认的分类和标签数据
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.app.core.config import settings
from src.app.models.taxonomy import Category, Tag


def init_taxonomy():
    print("开始初始化分类和标签数据...")
    print(f"数据库连接: {settings.DATABASE_URL}")

    engine = create_engine(settings.DATABASE_URL)

    with Session(engine) as session:
        # 检查是否已有数据
        existing_categories = session.query(Category).count()
        existing_tags = session.query(Tag).count()

        if existing_categories > 0:
            print(f"\n✓ 已有 {existing_categories} 个分类，跳过初始化")
        else:
            # 添加默认分类
            default_categories = [
                {"name": "技术博客", "slug": "tech-blog", "description": "技术相关文章", "order": 1},
                {"name": "项目展示", "slug": "projects", "description": "项目案例和作品", "order": 2},
                {"name": "学习笔记", "slug": "notes", "description": "学习过程中的笔记", "order": 3},
                {"name": "工具推荐", "slug": "tools", "description": "好用的工具推荐", "order": 4},
                {"name": "经验分享", "slug": "experience", "description": "工作经验分享", "order": 5},
            ]

            for cat_data in default_categories:
                category = Category(**cat_data)
                session.add(category)

            session.commit()
            print(f"\n✓ 已添加 {len(default_categories)} 个默认分类")

        if existing_tags > 0:
            print(f"✓ 已有 {existing_tags} 个标签，跳过初始化")
        else:
            # 添加默认标签
            default_tags = [
                {"name": "Python", "slug": "python"},
                {"name": "JavaScript", "slug": "javascript"},
                {"name": "Vue", "slug": "vue"},
                {"name": "React", "slug": "react"},
                {"name": "Node.js", "slug": "nodejs"},
                {"name": "数据库", "slug": "database"},
                {"name": "Docker", "slug": "docker"},
                {"name": "Linux", "slug": "linux"},
                {"name": "Git", "slug": "git"},
                {"name": "算法", "slug": "algorithm"},
            ]

            for tag_data in default_tags:
                tag = Tag(**tag_data)
                session.add(tag)

            session.commit()
            print(f"✓ 已添加 {len(default_tags)} 个默认标签")

    print("\n分类和标签初始化完成！")


if __name__ == "__main__":
    init_taxonomy()
