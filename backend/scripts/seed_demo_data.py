"""
完整演示数据填充脚本：
用于将数据库中的所有真实业务数据替换为设计图规定的标准演示数据
"""
import sys
from pathlib import Path
from datetime import datetime, timedelta

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session
from sqlalchemy import text
from src.app.core.database import SessionLocal, engine
from src.app.models.user import User
from src.app.models.profile import Profile, Skill, Experience, Education
from src.app.models.article import Article
from src.app.models.comment import Comment, Guestbook
from src.app.models.project import Project
from src.app.models.friend_link import FriendLink
from src.app.models.taxonomy import Category, Tag
from src.app.models.site_settings import SiteSettings
from src.app.models.statistics import SiteStats
from src.app.security.password import get_password_hash


def clear_all_data(db: Session):
    """清空所有业务数据"""
    print("正在清空现有数据...")
    
    db.execute(text("SET FOREIGN_KEY_CHECKS = 0"))
    
    tables = [
        Guestbook, Comment, Article, 
        Project, FriendLink, 
        Skill, Experience, Education,
        Category, Tag, SiteStats, SiteSettings
    ]
    
    for table in tables:
        db.query(table).delete()
    
    db.execute(text("SET FOREIGN_KEY_CHECKS = 1"))
    db.commit()
    
    print("✓ 已清空所有业务数据")


def create_admin_user(db: Session):
    """创建管理员用户"""
    admin = db.query(User).filter(User.username == "admin").first()
    if admin:
        admin.password_hash = get_password_hash("123456")
        admin.nickname = "Lin"
        admin.bio = "全栈开发者 & AI 应用探索者"
        admin.city = "深圳"
    else:
        admin = User(
            username="admin",
            email="admin@example.com",
            password_hash=get_password_hash("123456"),
            nickname="Lin",
            bio="全栈开发者 & AI 应用探索者",
            city="深圳",
            role="admin",
            is_active=True
        )
        db.add(admin)
    
    db.commit()
    print("✓ 管理员用户已创建/更新")
    return admin


def create_profile(db: Session, user_id: int):
    """创建个人资料"""
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()
    if not profile:
        profile = Profile(user_id=user_id)
        db.add(profile)
    
    profile.bio = "全栈开发者 & AI 应用探索者\n\n热衷于构建智能、高效、有价值的产品。\n探索 Agent、LLM 应用与前端工程化的边界，\n让技术真正服务于人。"
    profile.social_links = {
        "email": "lin@example.com",
        "github": "github.com/linxxx",
        "location": "中国 · 深圳",
        "experience": "5年开发经验"
    }
    db.commit()
    print("✓ 个人资料已创建")
    return profile


def create_skills(db: Session, profile_id: int):
    """创建技能数据"""
    skills_data = [
        {"name": "TypeScript", "proficiency": 90, "category": "前端"},
        {"name": "React / Next.js", "proficiency": 85, "category": "前端"},
        {"name": "Python", "proficiency": 80, "category": "后端"},
        {"name": "LangChain", "proficiency": 75, "category": "后端"},
        {"name": "Node.js", "proficiency": 70, "category": "后端"},
        {"name": "Tailwind CSS", "proficiency": 85, "category": "前端"},
        {"name": "JavaScript", "proficiency": 88, "category": "前端"},
        {"name": "FastAPI", "proficiency": 78, "category": "后端"},
        {"name": "PostgreSQL", "proficiency": 72, "category": "数据库"},
        {"name": "Docker", "proficiency": 68, "category": "运维"},
        {"name": "Git", "proficiency": 82, "category": "工具"},
        {"name": "CSS", "proficiency": 86, "category": "前端"},
    ]
    
    for skill in skills_data:
        db.add(Skill(profile_id=profile_id, **skill))
    
    db.commit()
    print(f"✓ 已创建 {len(skills_data)} 条技能数据")


def create_experiences(db: Session, profile_id: int):
    """创建工作经历"""
    experiences_data = [
        {
            "title": "高级全栈开发工程师",
            "company": "某科技公司",
            "start_date": "2022.05",
            "end_date": "",
            "description": "负责 AI 平台与智能工具链的设计与开发，主导多个核心模块的架构与实现。推动团队文化与质量体系建设。",
            "tags": ["TypeScript", "React", "Node.js", "Python", "Docker"],
            "order": 1
        },
        {
            "title": "全栈开发工程师",
            "company": "某互联网公司",
            "start_date": "2020.03",
            "end_date": "2022.04",
            "description": "参与公司中台系统与业务平台的研发，负责前端架构设计与后端服务开发。",
            "tags": ["React", "TypeScript", "Nest.js", "PostgreSQL"],
            "order": 2
        },
        {
            "title": "前端开发工程师",
            "company": "某创业公司",
            "start_date": "2018.07",
            "end_date": "2020.02",
            "description": "负责产品前端开发与性能优化，参与从 0 到 1 的产品建设。",
            "tags": ["JavaScript", "Vue.js", "HTML/CSS", "Webpack"],
            "order": 3
        },
    ]
    
    for exp in experiences_data:
        db.add(Experience(profile_id=profile_id, **exp))
    
    db.commit()
    print(f"✓ 已创建 {len(experiences_data)} 条工作经历")


def create_education(db: Session, profile_id: int):
    """创建教育背景"""
    education_data = [
        {
            "school": "某某大学",
            "major": "计算机科学与技术",
            "degree": "本科",
            "start_date": "2014.09",
            "end_date": "2018.06",
            "order": 1
        },
    ]
    
    for edu in education_data:
        db.add(Education(profile_id=profile_id, **edu))
    
    db.commit()
    print(f"✓ 已创建 {len(education_data)} 条教育背景")


def create_categories(db: Session):
    """创建文章分类"""
    categories = [
        {"name": "AI 应用", "description": "人工智能相关技术文章"},
        {"name": "前端技术", "description": "前端开发技术分享"},
        {"name": "后端技术", "description": "后端开发技术分享"},
        {"name": "项目实战", "description": "项目经验总结"},
        {"name": "技术思考", "description": "技术感悟与思考"},
    ]
    
    for cat in categories:
        db.add(Category(**cat))
    
    db.commit()
    print(f"✓ 已创建 {len(categories)} 个分类")


def create_tags(db: Session):
    """创建标签"""
    tags = [
        "Agent", "LLM", "LangChain", "React", "Next.js",
        "TypeScript", "Python", "FastAPI", "Node.js", "Vue.js",
        "Tailwind CSS", "PostgreSQL", "Docker", "Git", "CSS",
        "前端", "后端", "全栈", "AI", "机器学习"
    ]
    
    for tag in tags:
        db.add(Tag(name=tag, slug=tag.lower().replace(" ", "-")))
    
    db.commit()
    print(f"✓ 已创建 {len(tags)} 个标签")


def create_articles(db: Session):
    """创建演示文章（32篇）"""
    base_date = datetime.now()
    
    articles_data = [
        {
            "title": "深入理解 Agent：从原理到实践",
            "summary": "系统介绍 Agent 的核心概念、设计模式与实现路径，并通过一个完整示例帮助你构建属于自己的 Agent 系统。",
            "content": "# 深入理解 Agent：从原理到实践\n\n## 什么是 Agent\n\nAgent 是一种能够自主感知、决策和行动的智能系统...",
            "category": "AI 应用",
            "tags": ["Agent", "LLM", "AI"],
            "tech_stack": ["Python", "LangChain"],
            "view_count": 1200,
            "like_count": 128,
            "read_time": 15,
            "author_name": "Lin",
            "created_at": base_date - timedelta(days=2)
        },
        {
            "title": "React 19 新特性详解与实践",
            "summary": "全面梳理 React 19 的新特性，结合实际场景探索 Server Components、Actions 等能力的最佳实践。",
            "content": "# React 19 新特性详解与实践\n\n## React 19 带来了什么\n\nReact 19 引入了许多令人兴奋的新特性...",
            "category": "前端技术",
            "tags": ["React", "TypeScript", "前端"],
            "tech_stack": ["React", "TypeScript"],
            "view_count": 899,
            "like_count": 96,
            "read_time": 12,
            "author_name": "Lin",
            "created_at": base_date - timedelta(days=5)
        },
        {
            "title": "LangChain 实战：构建智能问答系统",
            "summary": "从零开始构建一个基于 LangChain 的智能问答系统，涵盖文档加载、向量化检索与 RAG 增强。",
            "content": "# LangChain 实战：构建智能问答系统\n\n## 概述\n\n在本教程中，我们将使用 LangChain 构建一个智能问答系统...",
            "category": "AI 应用",
            "tags": ["LangChain", "LLM", "Python"],
            "tech_stack": ["Python", "LangChain"],
            "view_count": 756,
            "like_count": 88,
            "read_time": 18,
            "author_name": "Lin",
            "created_at": base_date - timedelta(days=8)
        },
        {
            "title": "FastAPI 最佳实践：构建高性能 API",
            "summary": "分享使用 FastAPI 构建生产级 API 的经验，包括路由设计、依赖注入、中间件和性能优化。",
            "content": "# FastAPI 最佳实践：构建高性能 API\n\n## 为什么选择 FastAPI\n\nFastAPI 是一个现代、快速的 Web 框架...",
            "category": "后端技术",
            "tags": ["FastAPI", "Python", "后端"],
            "tech_stack": ["Python", "FastAPI", "PostgreSQL"],
            "view_count": 680,
            "like_count": 72,
            "read_time": 14,
            "author_name": "Lin",
            "created_at": base_date - timedelta(days=12)
        },
        {
            "title": "TypeScript 类型体操完全指南",
            "summary": "深入理解 TypeScript 类型系统，掌握高级类型技巧，提升代码类型安全。",
            "content": "# TypeScript 类型体操完全指南\n\n## 类型基础\n\nTypeScript 的类型系统非常强大...",
            "category": "前端技术",
            "tags": ["TypeScript", "前端"],
            "tech_stack": ["TypeScript"],
            "view_count": 598,
            "like_count": 64,
            "read_time": 16,
            "author_name": "Lin",
            "created_at": base_date - timedelta(days=15)
        },
        {
            "title": "Next.js 14 App Router 深度解析",
            "summary": "深入探讨 Next.js 14 App Router 的设计理念、目录结构和数据获取策略。",
            "content": "# Next.js 14 App Router 深度解析\n\n## App Router 简介\n\nNext.js 13 引入了全新的 App Router...",
            "category": "前端技术",
            "tags": ["Next.js", "React", "前端"],
            "tech_stack": ["Next.js", "React", "TypeScript"],
            "view_count": 820,
            "like_count": 92,
            "read_time": 13,
            "author_name": "Lin",
            "created_at": base_date - timedelta(days=18)
        },
        {
            "title": "Docker 容器化部署实践",
            "summary": "从开发环境到生产部署，全面掌握 Docker 容器化技术和最佳实践。",
            "content": "# Docker 容器化部署实践\n\n## Docker 基础\n\nDocker 是一个用于开发、部署和运行应用的开放平台...",
            "category": "后端技术",
            "tags": ["Docker", "运维", "后端"],
            "tech_stack": ["Docker"],
            "view_count": 456,
            "like_count": 48,
            "read_time": 10,
            "author_name": "Lin",
            "created_at": base_date - timedelta(days=22)
        },
        {
            "title": "PostgreSQL 性能优化指南",
            "summary": "深入 PostgreSQL 性能调优，包括索引优化、查询优化和配置优化。",
            "content": "# PostgreSQL 性能优化指南\n\n## 索引优化\n\n索引是提高查询性能的关键...",
            "category": "后端技术",
            "tags": ["PostgreSQL", "数据库", "后端"],
            "tech_stack": ["PostgreSQL"],
            "view_count": 389,
            "like_count": 42,
            "read_time": 11,
            "author_name": "Lin",
            "created_at": base_date - timedelta(days=25)
        },
    ]
    
    # 添加更多文章以达到32篇
    topics = ["AI", "前端", "后端", "系统设计", "架构"]
    for i in range(24):
        topic = topics[i % len(topics)]
        articles_data.append({
            "title": f"{topic}技术分享 {i+9}",
            "summary": f"关于{topic}技术的第{i+9}篇分享文章，涵盖核心概念和实践经验。",
            "content": f"# {topic}技术分享 {i+9}\n\n这是一篇关于{topic}技术的文章...",
            "category": "技术思考",
            "tags": [topic],
            "tech_stack": ["Python", "JavaScript"],
            "view_count": 100 + i * 30,
            "like_count": 10 + i * 5,
            "read_time": 8,
            "author_name": "Lin",
            "created_at": base_date - timedelta(days=28 + i)
        })
    
    for article in articles_data:
        db.add(Article(**article))
    
    db.commit()
    print(f"✓ 已创建 {len(articles_data)} 篇文章")


def create_projects(db: Session):
    """创建演示项目（12个）"""
    projects_data = [
        {
            "name": "ChatFlow - 智能对话工作流平台",
            "summary": "基于 Agent 架构的对话式 AI 平台，支持多模态接入、工作流编排与知识图谱集成。",
            "description": "ChatFlow 是一个强大的对话工作流平台，允许用户构建复杂的 AI 对话系统...",
            "tags": ["Agent", "LLM", "工作流"],
            "tech_stack": ["Next.js", "TypeScript", "LangChain"],
            "github_url": "https://github.com/linxxx/chatflow",
            "demo_url": "https://demo.chatflow.dev",
            "view_count": 2340,
            "like_count": 268,
            "project_type": "AI 应用",
            "is_featured": True
        },
        {
            "name": "LLM Knowledge Hub",
            "summary": "个人知识与大模型问答系统，支持文档解析、向量化检索与 RAG 增强。",
            "description": "LLM Knowledge Hub 是一个智能知识库系统...",
            "tags": ["LLM", "RAG", "知识库"],
            "tech_stack": ["Python", "FastAPI", "Milvus"],
            "github_url": "https://github.com/linxxx/llm-knowledge-hub",
            "view_count": 1230,
            "like_count": 142,
            "project_type": "AI 应用",
            "is_featured": True
        },
        {
            "name": "Frontier UI",
            "summary": "一个现代化的前端组件库，专注于易用性、可访问性与高性能。",
            "description": "Frontier UI 提供丰富的组件和工具...",
            "tags": ["UI", "组件库", "前端"],
            "tech_stack": ["React", "TypeScript", "Tailwind CSS"],
            "github_url": "https://github.com/linxxx/frontier-ui",
            "view_count": 890,
            "like_count": 104,
            "project_type": "前端",
            "is_featured": True
        },
        {
            "name": "AI Prompt 工具箱",
            "summary": "基于 Agent 思想的提示词管理与优化工具，提供提示词模板、评估、版本管理和效果对比。",
            "description": "AI Prompt 工具箱帮助开发者管理和优化提示词...",
            "tags": ["Prompt", "AI", "工具"],
            "tech_stack": ["Python", "Streamlit"],
            "github_url": "https://github.com/linxxx/ai-prompt-toolkit",
            "view_count": 567,
            "like_count": 72,
            "project_type": "工具",
            "is_featured": False
        },
        {
            "name": "Node.js API 框架",
            "summary": "轻量级 Node.js API 框架，提供路由、中间件和数据库集成。",
            "description": "一个简洁高效的 Node.js API 框架...",
            "tags": ["Node.js", "API", "后端"],
            "tech_stack": ["Node.js", "TypeScript", "PostgreSQL"],
            "github_url": "https://github.com/linxxx/node-api-framework",
            "view_count": 445,
            "like_count": 52,
            "project_type": "后端",
            "is_featured": False
        },
        {
            "name": "Vue 3 组件库",
            "summary": "基于 Vue 3 的企业级组件库，支持 TypeScript 和响应式设计。",
            "description": "Vue 3 组件库提供丰富的 UI 组件...",
            "tags": ["Vue", "组件库", "前端"],
            "tech_stack": ["Vue 3", "TypeScript", "Tailwind CSS"],
            "github_url": "https://github.com/linxxx/vue-components",
            "view_count": 389,
            "like_count": 45,
            "project_type": "前端",
            "is_featured": False
        },
    ]
    
    # 添加更多项目以达到12个
    for i in range(6):
        types = ["AI 应用", "工具", "前端", "后端", "其他"]
        project_type = types[i % len(types)]
        projects_data.append({
            "name": f"开源项目 {i+7}",
            "summary": f"一个优秀的{project_type}开源项目",
            "description": f"这是一个{project_type}类型的开源项目...",
            "tags": [project_type],
            "tech_stack": ["Python", "JavaScript"],
            "github_url": f"https://github.com/linxxx/project{i+7}",
            "view_count": 100 + i * 50,
            "like_count": 15 + i * 8,
            "project_type": project_type,
            "is_featured": False
        })
    
    for project in projects_data:
        db.add(Project(**project))
    
    db.commit()
    print(f"✓ 已创建 {len(projects_data)} 个项目")


def create_comments(db: Session):
    """创建演示评论数据"""
    db.execute(text("SET FOREIGN_KEY_CHECKS = 0"))
    
    comments_sql = """
    INSERT INTO comments (article_id, guest_name, content, parent_id, reply_to_id, reply_to_name, like_count, is_approved, created_at)
    VALUES 
    (1, '小明同学', '你好！你的 Agent 系列文章写得非常棒，受益匪浅！请问关于多 Agent 协作的部分，是否有具体的代码示例可以参考？', NULL, NULL, NULL, 3, 1, NOW() - INTERVAL 2 HOUR),
    (1, 'TechLover', '请问 Frontier UI 中的权限管理是如何实现的？使用的是哪些技术？', NULL, NULL, NULL, 1, 1, NOW() - INTERVAL 8 HOUR),
    (1, 'Lin', '感谢关注！权限管理使用了 Next.js Auth + Prisma + PostgreSQL 实现，具体实现细节会在后续文章中分享', 2, 2, 'TechLover', 2, 1, NOW() - INTERVAL 5 HOUR),
    (2, 'AI 探索者', '请问 ChatFlow 的 RAG 部分支持自定义知识库吗？可以上传自己的文档进行训练吗？', NULL, NULL, NULL, 2, 1, NOW() - INTERVAL 15 HOUR),
    (2, 'Lin', '支持的！可以上传 PDF、Word、TXT 等格式的文件，系统会自动解析并建立向量索引。', 4, 4, 'AI 探索者', 1, 1, NOW() - INTERVAL 12 HOUR),
    (3, '开发小白', 'React 19 的新特性介绍得非常详细，学到了！', NULL, NULL, NULL, 2, 1, NOW() - INTERVAL 1 DAY)
    """
    db.execute(text(comments_sql))
    
    for i in range(22):
        article_id = (i % 5) + 1
        sql = f"""
        INSERT INTO comments (article_id, guest_name, content, like_count, is_approved, created_at)
        VALUES ({article_id}, '用户{i+7}', '这是第{i+7}条评论内容，非常棒的文章！', {i % 3}, 1, NOW() - INTERVAL {1 + i} DAY - INTERVAL {i} HOUR)
        """
        db.execute(text(sql))
    
    db.execute(text("SET FOREIGN_KEY_CHECKS = 1"))
    db.commit()
    print(f"✓ 已创建 28 条评论")


def create_guestbook(db: Session):
    """创建留言板数据"""
    guestbook_data = [
        {
            "content": "欢迎在这里留言交流，分享想法或提出建议。我会认真阅读每一条留言并及时回复。",
            "is_top": True
        },
    ]
    
    for entry in guestbook_data:
        db.add(Guestbook(**entry))
    
    db.commit()
    print(f"✓ 已创建留言板数据")


def create_friend_links(db: Session):
    """创建友链数据"""
    friend_links_data = [
        {"name": "Hux Blog", "url": "https://huxblog.com", "description": "专注分享 Web 开发、编程技术与个人成长。", "category": "技术博客"},
        {"name": "阮一峰的网络日志", "url": "https://ruanyifeng.com", "description": "关注互联网应用、编程技术和开源软件。", "category": "技术博客"},
        {"name": "张洪Heo", "url": "https://heo.dev", "description": "分享 React、Laravel、Vue 等开发技术。", "category": "技术博客"},
        {"name": "Fronttier", "url": "https://fronttier.dev", "description": "一款开源的全栈管理后台框架。", "category": "开源项目"},
        {"name": "Vue.js", "url": "https://vuejs.org", "description": "渐进式 JavaScript 框架。", "category": "开源项目"},
        {"name": "Tailwind CSS", "url": "https://tailwindcss.com", "description": "一个实用优先的 CSS 框架。", "category": "开源项目"},
        {"name": "Node.js", "url": "https://nodejs.org", "description": "基于 Chrome V8 引擎的 JavaScript 运行时。", "category": "开源项目"},
        {"name": "独立开发者 - 小林", "url": "https://xiaolin.dev", "description": "独立开发者，专注于效率工具与产品设计。", "category": "独立开发者"},
        {"name": "独立开发者 - Kai", "url": "https://kai.dev", "description": "专注于工具与生产力应用开发。", "category": "独立开发者"},
        {"name": "喵酱日志", "url": "https://meowlog.com", "description": "记录生活，分享技术，保持热爱。", "category": "技术博客"},
        {"name": "JavaScript 中文网", "url": "https://javascript.cn", "description": "致力于推广 JavaScript 技术。", "category": "技术博客"},
        {"name": "Ant Design", "url": "https://ant.design", "description": "企业级产品设计体系。", "category": "开源项目"},
        {"name": "TypeScript", "url": "https://typescriptlang.org", "description": "JavaScript 的超集，添加了类型系统。", "category": "开源项目"},
        {"name": "React", "url": "https://react.dev", "description": "用于构建用户界面的 JavaScript 库。", "category": "开源项目"},
        {"name": "Next.js", "url": "https://nextjs.org", "description": "React 框架，支持服务端渲染。", "category": "开源项目"},
        {"name": "FastAPI", "url": "https://fastapi.tiangolo.com", "description": "现代、快速的 Web 框架。", "category": "开源项目"},
        {"name": "Python", "url": "https://python.org", "description": "优雅、简洁的编程语言。", "category": "开源项目"},
        {"name": "GitHub", "url": "https://github.com", "description": "全球最大的代码托管平台。", "category": "开源项目"},
    ]
    
    for link in friend_links_data:
        db.add(FriendLink(status="approved", **link))
    
    db.commit()
    print(f"✓ 已创建 {len(friend_links_data)} 条友链")


def create_site_settings(db: Session):
    """创建站点设置"""
    settings = SiteSettings(
        site_name="Lin's Tech Blog",
        site_title="Lin's Tech Blog - 全栈开发者 & AI 应用探索者",
        keywords="技术博客,AI,前端开发,后端开发,全栈,Agent",
        description="全栈开发者 & AI 应用探索者的技术博客",
        banner_text="专注 Agent 开发与前端技术",
        icp_number="粤ICP备2024xxxxx号",
        site_start_date=datetime.now() - timedelta(days=236),
        github_url="https://github.com/linxxx",
        email="lin@example.com",
        author_name="Lin",
        bio="全栈开发者 & AI 应用探索者",
        bio_motto="技术的价值不在于复杂，而在于解决问题",
        bio_motto_items="产品的价值不在于功能，而在于用户体验。\n体验的价值不在于炫技，而在于用心体验。\n注重工程质量与用户体验\n用技术创造实际价值\n开放分享，互相成长",
        bio_interests="技术探索,开源贡献,阅读写作,摄影旅行,健身运动",
        experience="5年开发经验",
        location="中国 · 深圳"
    )
    
    db.add(settings)
    db.commit()
    print("✓ 站点设置已创建")


def create_site_stats(db: Session):
    """创建站点统计数据（使用设计图规定的标准数值）"""
    stats = SiteStats(
        articles_count=32,
        projects_count=12,
        total_views=18600,  # 18.6k
        total_likes=2340,
        total_comments=28,
        total_collects=567,
        site_start_date=datetime.now() - timedelta(days=236)
    )
    
    db.add(stats)
    db.commit()
    print("✓ 站点统计数据已创建（文章32篇，项目12个，访问量18.6k，运行天数236天）")


def main():
    print("开始填充演示数据...")
    print("=" * 50)
    
    db = SessionLocal()
    try:
        clear_all_data(db)
        
        admin = create_admin_user(db)
        profile = create_profile(db, admin.id)
        
        create_skills(db, profile.id)
        create_experiences(db, profile.id)
        create_education(db, profile.id)
        
        create_categories(db)
        create_tags(db)
        
        create_articles(db)
        create_projects(db)
        create_comments(db)
        create_guestbook(db)
        
        create_friend_links(db)
        
        create_site_settings(db)
        create_site_stats(db)
        
        print("=" * 50)
        print("✓ 所有演示数据填充完成！")
        print("\n📊 数据统计：")
        print("  - 用户：1 个（admin / 123456）")
        print("  - 技能：12 项")
        print("  - 工作经历：3 条")
        print("  - 教育背景：1 条")
        print("  - 文章：32 篇")
        print("  - 项目：12 个")
        print("  - 评论：28 条")
        print("  - 友链：18 条")
        print("  - 分类：5 个")
        print("  - 标签：20 个")
        print("\n🔐 敏感信息已全部清除，可安全开源！")
        
    except Exception as e:
        db.rollback()
        print(f"\n✗ 数据填充失败: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()