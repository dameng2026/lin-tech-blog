"""
数据更新脚本：
1. 将 admin 密码修改为 123456
2. 根据模板设计图更新用户个人资料、技能、工作经历、教育背景等数据
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session
from src.app.core.database import SessionLocal, engine
from src.app.models.user import User
from src.app.models.profile import Profile, Skill, Experience, Education
from src.app.security.password import get_password_hash


def update_admin_password(db: Session, new_password: str = "123456"):
    """更新管理员密码"""
    admin = db.query(User).filter(User.username == "admin").first()
    if admin:
        admin.password_hash = get_password_hash(new_password)
        db.commit()
        print(f"✓ 管理员密码已更新为: {new_password}")
    else:
        print("✗ 未找到 admin 用户")


def update_profile(db: Session):
    """更新用户个人资料"""
    profile = db.query(Profile).filter(Profile.id == 1).first()
    if not profile:
        profile = Profile(id=1, user_id=1)
        db.add(profile)
    
    profile.bio = "全栈开发者 & AI 应用探索者\n\n热衷于构建智能、高效、有价值的产品。\n探索 Agent、Agent、LLM 应用与前端工程化的边界，\n让技术真正服务于人。"
    profile.social_links = {
        "email": "lin@example.com",
        "github": "github.com/linxxx",
        "location": "中国 · 深圳",
        "experience": "5年开发经验"
    }
    db.commit()
    print("✓ 个人资料已更新")


def update_skills(db: Session):
    """更新技能数据"""
    profile_id = 1
    
    db.query(Skill).filter(Skill.profile_id == profile_id).delete()
    
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
    print(f"✓ 已更新 {len(skills_data)} 条技能数据")


def update_experiences(db: Session):
    """更新工作经历"""
    profile_id = 1
    
    db.query(Experience).filter(Experience.profile_id == profile_id).delete()
    
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
    print(f"✓ 已更新 {len(experiences_data)} 条工作经历")


def update_education(db: Session):
    """更新教育背景"""
    profile_id = 1
    
    db.query(Education).filter(Education.profile_id == profile_id).delete()
    
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
    print(f"✓ 已更新 {len(education_data)} 条教育背景")


def update_admin_user(db: Session):
    """更新管理员用户信息"""
    admin = db.query(User).filter(User.username == "admin").first()
    if admin:
        admin.nickname = "Lin"
        admin.bio = "全栈开发者 & AI 应用探索者"
        admin.city = "深圳"
        db.commit()
        print("✓ 管理员用户信息已更新")


def main():
    print("开始更新数据库数据...")
    
    db = SessionLocal()
    try:
        update_admin_password(db)
        update_admin_user(db)
        update_profile(db)
        update_skills(db)
        update_experiences(db)
        update_education(db)
        
        print("\n✓ 所有数据更新完成！")
        
    except Exception as e:
        db.rollback()
        print(f"\n✗ 数据更新失败: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()