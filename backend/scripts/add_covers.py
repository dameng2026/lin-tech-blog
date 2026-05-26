"""
为文章和项目添加封面图
使用前端本地 public/images/ 目录中的 SVG 占位图
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session
from sqlalchemy import text
from src.app.core.database import SessionLocal
from src.app.models.project import Project
from src.app.models.article import Article


# 文章分类 -> 本地封面图映射
ARTICLE_COVER_MAP = {
    "AI 应用": "/images/cover-ai.svg",
    "前端技术": "/images/cover-frontend.svg",
    "后端技术": "/images/cover-backend.svg",
    "项目实战": "/images/cover-tools.svg",
    "技术思考": "/images/cover-thought.svg",
}

# 项目类型 -> 本地封面图映射
PROJECT_COVER_MAP = {
    "AI 应用": "/images/cover-ai.svg",
    "前端": "/images/cover-frontend.svg",
    "后端": "/images/cover-backend.svg",
    "工具": "/images/cover-tools.svg",
    "其他": "/images/cover-project.svg",
}


def add_project_covers(db: Session):
    """为项目添加封面图"""
    projects = db.query(Project).all()
    
    type_count = {}
    for project in projects:
        category = project.project_type or "其他"
        type_count[category] = type_count.get(category, 0) + 1
        cover = PROJECT_COVER_MAP.get(category, PROJECT_COVER_MAP["其他"])
        project.cover = cover
    
    db.commit()
    print(f"✓ 已为 {len(projects)} 个项目添加封面图")


def add_article_covers(db: Session):
    """为文章添加封面图"""
    articles = db.query(Article).all()
    
    cat_count = {}
    for article in articles:
        category = article.category or "技术思考"
        cat_count[category] = cat_count.get(category, 0) + 1
        cover = ARTICLE_COVER_MAP.get(category, ARTICLE_COVER_MAP["技术思考"])
        article.cover = cover
    
    db.commit()
    print(f"✓ 已为 {len(articles)} 篇文章添加封面图")


def main():
    print("为文章和项目添加封面图...")
    
    db = SessionLocal()
    try:
        add_project_covers(db)
        add_article_covers(db)
        
        print("\n✓ 封面图添加完成！")
        print("\n📊 统计：")
        projects = db.query(Project).filter(Project.cover.isnot(None)).count()
        articles = db.query(Article).filter(Article.cover.isnot(None)).count()
        print(f"  - 项目封面图：{projects} 个")
        print(f"  - 文章封面图：{articles} 篇")
        
    except Exception as e:
        db.rollback()
        print(f"\n✗ 添加失败: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()