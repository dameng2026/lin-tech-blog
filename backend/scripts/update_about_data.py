"""
更新关于我页面数据，使其与设计图一致
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session
from sqlalchemy import text
from src.app.core.database import SessionLocal
from src.app.models.profile import Skill, Experience, Education, Profile
from src.app.models.site_settings import SiteSettings


def update_skills(db: Session):
    """更新技能数据，添加缺失的技术栈"""
    profile_id = 1
    
    db.execute(text("SET FOREIGN_KEY_CHECKS = 0"))
    db.query(Skill).filter(Skill.profile_id == profile_id).delete()
    db.execute(text("SET FOREIGN_KEY_CHECKS = 1"))
    
    skills_data = [
        {"name": "TypeScript", "proficiency": 90, "category": "前端"},
        {"name": "JavaScript", "proficiency": 88, "category": "前端"},
        {"name": "React", "proficiency": 85, "category": "前端"},
        {"name": "Next.js", "proficiency": 85, "category": "前端"},
        {"name": "Node.js", "proficiency": 70, "category": "后端"},
        {"name": "Python", "proficiency": 80, "category": "后端"},
        {"name": "LangChain", "proficiency": 75, "category": "后端"},
        {"name": "FastAPI", "proficiency": 78, "category": "后端"},
        {"name": "Tailwind CSS", "proficiency": 85, "category": "前端"},
        {"name": "CSS", "proficiency": 86, "category": "前端"},
        {"name": "PostgreSQL", "proficiency": 72, "category": "数据库"},
        {"name": "Docker", "proficiency": 68, "category": "运维"},
        {"name": "Git", "proficiency": 82, "category": "工具"},
        {"name": "Vue.js", "proficiency": 75, "category": "前端"},
        {"name": "Prisma", "proficiency": 72, "category": "数据库"},
    ]
    
    for skill in skills_data:
        db.add(Skill(profile_id=profile_id, **skill))
    
    db.commit()
    print("✓ 技能数据已更新（15个技术栈）")


def update_experiences(db: Session):
    """更新工作经历"""
    profile_id = 1
    
    db.execute(text("SET FOREIGN_KEY_CHECKS = 0"))
    db.query(Experience).filter(Experience.profile_id == profile_id).delete()
    db.execute(text("SET FOREIGN_KEY_CHECKS = 1"))
    
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
    print("✓ 工作经历已更新（3条）")


def update_education(db: Session):
    """更新教育背景，添加时间信息"""
    profile_id = 1
    
    db.execute(text("SET FOREIGN_KEY_CHECKS = 0"))
    db.query(Education).filter(Education.profile_id == profile_id).delete()
    db.execute(text("SET FOREIGN_KEY_CHECKS = 1"))
    
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
    print("✓ 教育背景已更新（添加时间信息）")


def update_site_settings(db: Session):
    """更新站点设置，完善理念和兴趣爱好"""
    settings = db.query(SiteSettings).first()
    if not settings:
        settings = SiteSettings()
        db.add(settings)
    
    settings.author_name = "Lin"
    settings.bio = "全栈开发者 & AI 应用探索者"
    settings.bio_motto = "技术的价值不在于复杂，而在于解决问题"
    settings.bio_motto_items = "\n".join([
        "技术的价值不在于复杂，而在于解决问题",
        "产品的价值不在于功能，而在于用户体验",
        "体验的价值不在于炫技，而在于用心体验",
        "注重工程质量与用户体验",
        "用技术创造实际价值",
        "开放分享，互相成长"
    ])
    settings.bio_interests = "技术探索,开源贡献,阅读写作,摄影旅行,健身运动"
    settings.experience = "5年开发经验"
    settings.location = "中国 · 深圳"
    
    db.commit()
    print("✓ 站点设置已更新（完善理念和兴趣）")


def main():
    print("更新关于我页面数据...")
    
    db = SessionLocal()
    try:
        update_skills(db)
        update_experiences(db)
        update_education(db)
        update_site_settings(db)
        
        print("\n✓ 所有数据更新完成！")
        
    except Exception as e:
        db.rollback()
        print(f"\n✗ 更新失败: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()