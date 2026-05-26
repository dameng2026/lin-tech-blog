"""
更新项目数据，创建更丰富、更真实的项目信息
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session
from sqlalchemy import text
from src.app.core.database import SessionLocal
from src.app.models.project import Project


def update_projects(db: Session):
    """更新项目数据"""
    db.execute(text("SET FOREIGN_KEY_CHECKS = 0"))
    db.query(Project).delete()
    db.execute(text("SET FOREIGN_KEY_CHECKS = 1"))
    
    projects_data = [
        {
            "name": "ChatFlow - 智能对话工作流平台",
            "summary": "基于 Agent 架构的对话式 AI 平台，支持多模态接入、工作流编排与知识图谱集成。",
            "description": "ChatFlow 是一个强大的对话工作流平台，允许用户构建复杂的 AI 对话系统。支持多轮对话、工具调用、知识库检索等高级功能。",
            "tags": ["Agent", "LLM", "工作流", "AI"],
            "tech_stack": ["Next.js", "TypeScript", "LangChain", "Prisma", "PostgreSQL"],
            "github_url": "https://github.com/linxxx/chatflow",
            "demo_url": "https://demo.chatflow.dev",
            "view_count": 2340,
            "like_count": 268,
            "project_type": "AI 应用",
            "is_featured": True,
            "status": "active",
            "open_source_license": "MIT",
        },
        {
            "name": "LLM Knowledge Hub",
            "summary": "个人知识与大模型问答系统，支持文档解析、向量化检索与 RAG 增强。",
            "description": "LLM Knowledge Hub 是一个智能知识库系统，支持上传多种格式文档，自动进行向量化存储，并提供基于 RAG 的智能问答功能。",
            "tags": ["LLM", "RAG", "知识库", "向量数据库"],
            "tech_stack": ["Python", "FastAPI", "Milvus", "LangChain"],
            "github_url": "https://github.com/linxxx/llm-knowledge-hub",
            "view_count": 1230,
            "like_count": 142,
            "project_type": "AI 应用",
            "is_featured": True,
            "status": "active",
            "open_source_license": "Apache 2.0",
        },
        {
            "name": "Frontier UI",
            "summary": "一个现代化的前端组件库，专注于易用性、可访问性与高性能。",
            "description": "Frontier UI 提供丰富的组件和工具，帮助开发者快速构建高质量的 Web 应用。包含完整的设计系统和主题支持。",
            "tags": ["UI", "组件库", "前端", "设计系统"],
            "tech_stack": ["React", "TypeScript", "Tailwind CSS", "Storybook"],
            "github_url": "https://github.com/linxxx/frontier-ui",
            "view_count": 890,
            "like_count": 104,
            "project_type": "前端",
            "is_featured": True,
            "status": "active",
            "open_source_license": "MIT",
        },
        {
            "name": "AI Prompt 工具箱",
            "summary": "基于 Agent 思想的提示词管理与优化工具，提供提示词模板、评估、版本管理和效果对比。",
            "description": "AI Prompt 工具箱帮助开发者管理和优化提示词，支持多种大模型，提供提示词版本控制和效果对比分析。",
            "tags": ["Prompt", "AI", "工具", "LLM"],
            "tech_stack": ["Python", "Streamlit", "OpenAI API"],
            "github_url": "https://github.com/linxxx/ai-prompt-toolkit",
            "view_count": 567,
            "like_count": 72,
            "project_type": "工具",
            "is_featured": False,
            "status": "active",
            "open_source_license": "MIT",
        },
        {
            "name": "Node.js API 框架",
            "summary": "轻量级 Node.js API 框架，提供路由、中间件和数据库集成。",
            "description": "一个简洁高效的 Node.js API 框架，内置 JWT 认证、请求验证、错误处理等功能，支持多种数据库。",
            "tags": ["Node.js", "API", "后端", "框架"],
            "tech_stack": ["Node.js", "TypeScript", "PostgreSQL", "Redis"],
            "github_url": "https://github.com/linxxx/node-api-framework",
            "view_count": 445,
            "like_count": 52,
            "project_type": "后端",
            "is_featured": False,
            "status": "active",
            "open_source_license": "MIT",
        },
        {
            "name": "Vue 3 组件库",
            "summary": "基于 Vue 3 的企业级组件库，支持 TypeScript 和响应式设计。",
            "description": "Vue 3 组件库提供丰富的 UI 组件，支持 Composition API，提供完整的类型定义和文档。",
            "tags": ["Vue", "组件库", "前端", "TypeScript"],
            "tech_stack": ["Vue 3", "TypeScript", "Tailwind CSS", "Vite"],
            "github_url": "https://github.com/linxxx/vue-components",
            "view_count": 389,
            "like_count": 45,
            "project_type": "前端",
            "is_featured": False,
            "status": "active",
            "open_source_license": "MIT",
        },
        {
            "name": "DataFlow Studio",
            "summary": "可视化数据处理流程编辑器，支持拖拽式构建数据管道。",
            "description": "DataFlow Studio 是一个可视化的数据处理工具，允许用户通过拖拽方式构建复杂的数据处理流程。",
            "tags": ["数据处理", "可视化", "ETL", "工具"],
            "tech_stack": ["React", "TypeScript", "D3.js", "Python"],
            "github_url": "https://github.com/linxxx/dataflow-studio",
            "view_count": 678,
            "like_count": 82,
            "project_type": "工具",
            "is_featured": False,
            "status": "active",
            "open_source_license": "Apache 2.0",
        },
        {
            "name": "Markdown 编辑器",
            "summary": "功能强大的 Markdown 编辑器，支持实时预览和导出功能。",
            "description": "一个现代化的 Markdown 编辑器，支持实时预览、代码高亮、图表渲染和多种导出格式。",
            "tags": ["Markdown", "编辑器", "前端", "工具"],
            "tech_stack": ["React", "TypeScript", "Tailwind CSS", "Remark"],
            "github_url": "https://github.com/linxxx/markdown-editor",
            "view_count": 523,
            "like_count": 64,
            "project_type": "工具",
            "is_featured": False,
            "status": "active",
            "open_source_license": "MIT",
        },
        {
            "name": "实时协作平台",
            "summary": "基于 WebRTC 的实时协作工具，支持多人同时编辑。",
            "description": "实时协作平台提供文档协作、白板共享和视频会议功能，支持多人实时协作。",
            "tags": ["协作", "WebRTC", "实时", "团队"],
            "tech_stack": ["Next.js", "TypeScript", "WebRTC", "Socket.io"],
            "github_url": "https://github.com/linxxx/collab-platform",
            "view_count": 412,
            "like_count": 48,
            "project_type": "工具",
            "is_featured": False,
            "status": "active",
            "open_source_license": "MIT",
        },
        {
            "name": "微服务网关",
            "summary": "轻量级 API 网关，支持负载均衡、限流和监控。",
            "description": "微服务网关提供统一的 API 入口，支持负载均衡、服务发现、限流熔断和实时监控。",
            "tags": ["微服务", "网关", "后端", "DevOps"],
            "tech_stack": ["Go", "Docker", "Kubernetes", "Redis"],
            "github_url": "https://github.com/linxxx/microservice-gateway",
            "view_count": 356,
            "like_count": 42,
            "project_type": "后端",
            "is_featured": False,
            "status": "active",
            "open_source_license": "Apache 2.0",
        },
        {
            "name": "移动端 UI 组件库",
            "summary": "专为移动端设计的 React Native 组件库。",
            "description": "移动端 UI 组件库提供丰富的原生级组件，支持 iOS 和 Android 双平台。",
            "tags": ["React Native", "移动端", "UI", "组件库"],
            "tech_stack": ["React Native", "TypeScript", "Tailwind CSS"],
            "github_url": "https://github.com/linxxx/mobile-ui",
            "view_count": 289,
            "like_count": 35,
            "project_type": "前端",
            "is_featured": False,
            "status": "active",
            "open_source_license": "MIT",
        },
        {
            "name": "自动化测试框架",
            "summary": "基于 Playwright 的自动化测试框架，支持端到端测试。",
            "description": "自动化测试框架提供声明式测试语法，支持并行测试和可视化报告。",
            "tags": ["测试", "自动化", "Playwright", "E2E"],
            "tech_stack": ["TypeScript", "Playwright", "Jest", "Docker"],
            "github_url": "https://github.com/linxxx/auto-test-framework",
            "view_count": 234,
            "like_count": 28,
            "project_type": "工具",
            "is_featured": False,
            "status": "active",
            "open_source_license": "MIT",
        },
    ]
    
    for project in projects_data:
        db.add(Project(**project))
    
    db.commit()
    print(f"✓ 已更新 {len(projects_data)} 个项目")


def main():
    print("更新项目数据...")
    
    db = SessionLocal()
    try:
        update_projects(db)
        print("\n✓ 项目数据更新完成！")
        
    except Exception as e:
        db.rollback()
        print(f"\n✗ 更新失败: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()