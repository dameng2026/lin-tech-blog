"""
种子数据脚本：将前台模板数据填充到数据库
（技能、工作经历、教育背景）
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session
from src.app.core.database import SessionLocal, engine
from src.app.models.profile import Base, Profile, Skill, Experience, Education
from src.app.core.config import settings


def seed_profile_data():
    print("开始填充种子数据...")

    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()
    try:
        profile = db.query(Profile).filter(Profile.id == 1).first()
        if not profile:
            profile = Profile(id=1, bio="", social_links={})
            db.add(profile)
            db.commit()
            db.refresh(profile)
            print("✓ 已创建默认 Profile")

        profile_id = profile.id

        existing_skills = db.query(Skill).filter(Skill.profile_id == profile_id).count()
        existing_experiences = db.query(Experience).filter(Experience.profile_id == profile_id).count()
        existing_education = db.query(Education).filter(Education.profile_id == profile_id).count()

        if existing_skills > 0:
            print(f"- 已有 {existing_skills} 条技能数据，跳过技能种子")
        else:
            skills_data = [
                Skill(profile_id=profile_id, name="TypeScript", proficiency=90, category="前端"),
                Skill(profile_id=profile_id, name="React / Next.js", proficiency=85, category="前端"),
                Skill(profile_id=profile_id, name="Python", proficiency=80, category="后端"),
                Skill(profile_id=profile_id, name="LangChain", proficiency=75, category="后端"),
                Skill(profile_id=profile_id, name="Node.js", proficiency=70, category="后端"),
                Skill(profile_id=profile_id, name="Tailwind CSS", proficiency=85, category="前端"),
            ]
            for skill in skills_data:
                db.add(skill)
            db.commit()
            print(f"✓ 已插入 {len(skills_data)} 条技能数据")

        if existing_experiences > 0:
            print(f"- 已有 {existing_experiences} 条工作经历数据，跳过")
        else:
            experiences_data = [
                Experience(
                    profile_id=profile_id, title="高级全栈开发工程师", company="某科技公司",
                    start_date="2022.05", end_date="",
                    description="负责 AI 平台与智能工具链的设计与开发，主导多个核心模块的架构与实现。",
                    tags=["TypeScript", "React", "Node.js", "Python", "Docker"], order=1
                ),
                Experience(
                    profile_id=profile_id, title="全栈开发工程师", company="某互联网公司",
                    start_date="2020.03", end_date="2022.04",
                    description="参与公司中台系统与业务平台的研发，负责前端架构设计与后端服务开发。",
                    tags=["React", "TypeScript", "Nest.js", "PostgreSQL"], order=2
                ),
                Experience(
                    profile_id=profile_id, title="前端开发工程师", company="某创业公司",
                    start_date="2018.07", end_date="2020.02",
                    description="负责产品前端开发与性能优化，参与从 0 到 1 的产品建设。",
                    tags=["JavaScript", "Vue.js", "HTML/CSS", "Webpack"], order=3
                ),
            ]
            for exp in experiences_data:
                db.add(exp)
            db.commit()
            print(f"✓ 已插入 {len(experiences_data)} 条工作经历数据")

        if existing_education > 0:
            print(f"- 已有 {existing_education} 条教育背景数据，跳过")
        else:
            education_data = [
                Education(
                    profile_id=profile_id, school="某某大学", major="计算机科学与技术",
                    degree="本科", start_date="2014.09", end_date="2018.06", order=1
                ),
            ]
            for edu in education_data:
                db.add(edu)
            db.commit()
            print(f"✓ 已插入 {len(education_data)} 条教育背景数据")

        print("\n种子数据填充完成！")

    except Exception as e:
        db.rollback()
        print(f"✗ 种子数据填充失败: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_profile_data()