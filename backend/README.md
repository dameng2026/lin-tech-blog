# Lin Tech Blog Backend

基于 FastAPI 的个人博客后端服务。

## 技术栈

- **框架**: FastAPI 0.104+
- **数据库**: MySQL 8.0+
- **ORM**: SQLAlchemy 2.0+
- **认证**: JWT + Redis
- **文件上传**: python-multipart

## 功能模块

1. **用户认证模块 (Auth & User)**
   - 注册/登录（账号密码 + 验证码）
   - 第三方登录预留
   - 找回密码
   - 个人信息管理
   - RBAC 权限控制

2. **核心内容管理 (CMS)**
   - 文章管理（CRUD、标签/技术栈筛选）
   - 项目管理（展示、统计）

3. **互动与社区功能**
   - 评论系统（嵌套评论）
   - 留言板
   - 点赞/收藏

4. **友链系统**
   - 友链展示
   - 申请流程（审批机制）

5. **个人简历与 PDF 生成**
   - 技能树（进度条）
   - 工作经历/教育背景
   - PDF 简历下载（密钥验证）

6. **数据统计与分析**
   - 站点数据统计
   - 热门文章/项目推荐

7. **文件存储与资产管理**
   - 文件上传接口
   - 静态资源服务

## 快速开始

### 环境要求

- Python 3.10+
- MySQL 8.0+
- Redis 6.0+

### 安装依赖

```bash
cd backend
pip install -r requirements.txt
```

### 配置环境变量

复制 `.env` 文件并修改配置：

```bash
cp .env.example .env
```

修改 `.env` 中的数据库配置：

```env
DATABASE_URL=mysql+mysqlconnector://root:password@localhost:3306/blog_db
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your-secret-key-here
```

### 创建数据库

```sql
CREATE DATABASE blog_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 启动服务

```bash
python start.py
```

服务将在 `http://localhost:8000` 启动。

### API 文档

启动后访问：
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API 端点

### 认证
- `POST /api/v1/auth/register` - 注册
- `POST /api/v1/auth/login` - 登录
- `POST /api/v1/auth/verify-code` - 发送验证码
- `POST /api/v1/auth/login-with-code` - 验证码登录
- `POST /api/v1/auth/reset-password` - 重置密码
- `GET /api/v1/auth/me` - 获取当前用户
- `PUT /api/v1/auth/me` - 更新个人信息

### 文章
- `GET /api/v1/articles` - 文章列表
- `GET /api/v1/articles/{id}` - 文章详情
- `POST /api/v1/articles` - 创建文章（管理员）
- `PUT /api/v1/articles/{id}` - 更新文章（管理员）
- `DELETE /api/v1/articles/{id}` - 删除文章（管理员）
- `POST /api/v1/articles/{id}/like` - 点赞
- `POST /api/v1/articles/{id}/collect` - 收藏

### 评论
- `GET /api/v1/comments/article/{id}` - 文章评论
- `POST /api/v1/comments/article/{id}` - 发表评论
- `DELETE /api/v1/comments/{id}` - 删除评论（管理员）
- `POST /api/v1/comments/{id}/like` - 评论点赞
- `GET /api/v1/comments/guestbook` - 留言板
- `POST /api/v1/comments/guestbook` - 发表留言
- `PUT /api/v1/comments/guestbook/{id}` - 回复/置顶（管理员）
- `DELETE /api/v1/comments/guestbook/{id}` - 删除留言（管理员）

### 项目
- `GET /api/v1/projects` - 项目列表
- `GET /api/v1/projects/{id}` - 项目详情
- `POST /api/v1/projects` - 创建项目（管理员）
- `PUT /api/v1/projects/{id}` - 更新项目（管理员）
- `DELETE /api/v1/projects/{id}` - 删除项目（管理员）

### 友链
- `GET /api/v1/friend-links` - 友链列表
- `GET /api/v1/friend-links/admin` - 管理后台（管理员）
- `POST /api/v1/friend-links/apply` - 申请友链
- `PUT /api/v1/friend-links/{id}` - 审核友链（管理员）
- `DELETE /api/v1/friend-links/{id}` - 删除友链（管理员）

### 个人资料
- `GET /api/v1/profile` - 获取个人资料
- `PUT /api/v1/profile` - 更新个人资料（管理员）
- `GET/POST/PUT/DELETE /api/v1/profile/skills` - 技能管理
- `GET/POST/PUT/DELETE /api/v1/profile/experiences` - 工作经历管理
- `GET/POST/PUT/DELETE /api/v1/profile/education` - 教育背景管理
- `POST /api/v1/profile/resume/key` - 设置简历密码（管理员）
- `POST /api/v1/profile/resume/download` - 下载简历

### 统计
- `GET /api/v1/statistics/site` - 站点统计
- `GET /api/v1/statistics/popular/articles` - 热门文章
- `GET /api/v1/statistics/popular/projects` - 热门项目

### 文件上传
- `POST /api/v1/upload/image` - 上传图片（管理员）
- `POST /api/v1/upload/file` - 上传文件（管理员）

## 项目结构

```
backend/
├── src/
│   └── app/
│       ├── api/
│       │   ├── v1/
│       │   │   ├── auth.py
│       │   │   ├── articles.py
│       │   │   ├── comments.py
│       │   │   ├── projects.py
│       │   │   ├── friend_links.py
│       │   │   ├── profile.py
│       │   │   ├── statistics.py
│       │   │   └── upload.py
│       │   ├── __init__.py
│       │   └── dependencies.py
│       ├── core/
│       │   ├── config.py
│       │   ├── database.py
│       │   ├── redis.py
│       │   └── exceptions.py
│       ├── crud/
│       │   ├── user.py
│       │   ├── article.py
│       │   ├── comment.py
│       │   ├── project.py
│       │   ├── friend_link.py
│       │   └── profile.py
│       ├── models/
│       │   ├── user.py
│       │   ├── article.py
│       │   ├── comment.py
│       │   ├── project.py
│       │   ├── friend_link.py
│       │   └── profile.py
│       ├── schemas/
│       │   ├── user.py
│       │   ├── article.py
│       │   ├── comment.py
│       │   ├── project.py
│       │   ├── friend_link.py
│       │   └── profile.py
│       ├── security/
│       │   ├── password.py
│       │   └── jwt.py
│       ├── utils/
│       │   └── verify_code.py
│       ├── __init__.py
│       └── main.py
├── .env
├── requirements.txt
├── start.py
└── README.md
```

## 开发

### 运行测试

```bash
cd backend
pytest
```

### 代码风格

使用 `black` 和 `flake8` 进行代码格式化和检查。

## 生产部署

使用 Gunicorn 或 Uvicorn 部署：

```bash
uvicorn src.app.main:app --host 0.0.0.0 --port 8000
```

建议配合 Nginx 作为反向代理。

## 许可证

MIT License
