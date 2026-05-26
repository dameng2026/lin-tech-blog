<template>
  <div class="docs-page">
    <!-- 阅读进度条 -->
    <div class="reading-progress" :style="{ width: progressPercent + '%' }"></div>

    <div class="docs-header">
      <div class="docs-header-content">
        <div class="flex items-center gap-4">
          <div class="brand-logo">
            <ArtSvgIcon icon="ri:code-box-line" class="text-blue-500 text-xl" />
          </div>
          <span class="text-lg font-bold text-gray-800">Lin's Blog</span>
          <span class="text-gray-300">|</span>
          <span class="text-gray-500 text-sm font-medium tracking-wide">使用文档</span>
        </div>
        <div class="flex items-center gap-4">
          <div class="search-box">
            <ArtSvgIcon icon="ri:search-line" class="search-icon" />
            <input v-model="searchQuery" type="text" :placeholder="searchFocused ? '' : '搜索文档...'" class="search-input" @focus="searchFocused = true" @blur="searchFocused = false" @input="handleSearch" @keydown.esc="clearSearch" />
            <span v-if="searchQuery" class="search-clear" @click="clearSearch"><ArtSvgIcon icon="ri:close-circle-fill" class="w-4 h-4" /></span>
            <kbd v-if="!searchQuery" class="search-shortcut">Ctrl+K</kbd>
          </div>
          <a :href="githubUrl" target="_blank" class="header-link"><ArtSvgIcon icon="ri:github-line" class="w-4 h-4" /><span class="hidden sm:inline ml-1.5">GitHub</span></a>
          <a href="#/dashboard/console" class="header-link header-link-back"><ArtSvgIcon icon="ri:arrow-go-back-line" class="w-4 h-4" /><span class="hidden sm:inline ml-1.5">返回后台</span></a>
        </div>
      </div>
      <div v-if="searchQuery && searchResults.total > 0" class="search-results-bar">✨ 共找到 <strong>{{ searchResults.total }}</strong> 个匹配项</div>
      <div v-else-if="searchQuery && searchResults.total === 0" class="search-results-bar search-empty">🔍 未找到与 "<strong>{{ searchQuery }}</strong>" 相关的内容</div>
    </div>

    <div class="docs-body">
      <aside class="docs-sidebar">
        <div class="sidebar-content">
          <div v-for="group in navGroups" :key="group.title" class="sidebar-section">
            <div class="sidebar-title" :class="{ 'sidebar-title-expanded': group.expanded }" @click="group.expanded = !group.expanded">
              <span class="sidebar-title-icon"><ArtSvgIcon :icon="group.icon" class="w-3.5 h-3.5" /></span>
              {{ group.title }}
              <ArtSvgIcon icon="ri:arrow-down-s-line" class="sidebar-collapse-arrow" :class="{ 'rotate-180': group.expanded }" />
            </div>
            <div class="sidebar-list-wrapper" :class="{ 'sidebar-list-expanded': group.expanded }">
              <ul class="sidebar-list">
                <li v-for="item in group.items" :key="item.id" :class="{ active: activeNav === item.id }" @click="scrollTo(item.id)">
                  <a :href="`#${item.id}`" @click.prevent><ArtSvgIcon :icon="item.icon" class="w-3.5 h-3.5 mr-2 flex-shrink-0 opacity-60 group-hover:opacity-100" /><span v-html="highlightText(item.label)"></span></a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </aside>

      <main class="docs-content" @scroll="handleScroll"><article>
        <!-- Hero -->
        <section id="intro" class="docs-section docs-hero">
          <div class="hero-glow hero-glow-1"></div>
          <div class="hero-glow hero-glow-2"></div>
          <div class="hero-content">
            <div class="hero-left">
              <p class="hero-badge"><span class="hero-badge-dot"></span>v1.0</p>
              <h1 class="hero-title">Lin's Blog <span class="hero-title-highlight">使用文档</span></h1>
              <p class="hero-desc">基于 Vue 3 + FastAPI 构建的全栈博客管理系统。覆盖 <strong>17 个功能模块</strong>的完整操作指南。</p>
              <div class="hero-actions">
                <a href="#quickstart" class="hero-btn hero-btn-primary" @click.prevent="scrollTo('quickstart')">
                  快速开始 <ArtSvgIcon icon="ri:arrow-right-line" class="w-4 h-4 ml-1 group-hover:translate-x-0.5 transition-transform" />
                </a>
                <a href="#faq" class="hero-btn hero-btn-outline" @click.prevent="scrollTo('faq')">常见问题</a>
              </div>
            </div>
            <div class="hero-right">
              <div class="hero-stats">
                <div class="hero-stat stat-blue">
                  <div class="stat-icon-wrap"><ArtSvgIcon icon="ri:article-line" class="stat-icon text-blue-500" /></div>
                  <span class="stat-num">文章管理</span><span class="stat-label">Markdown 编辑器</span>
                </div>
                <div class="hero-stat stat-green">
                  <div class="stat-icon-wrap"><ArtSvgIcon icon="ri:folder-3-line" class="stat-icon text-green-500" /></div>
                  <span class="stat-num">项目管理</span><span class="stat-label">作品集展示</span>
                </div>
                <div class="hero-stat stat-purple">
                  <div class="stat-icon-wrap"><ArtSvgIcon icon="ri:chat-3-line" class="stat-icon text-purple-500" /></div>
                  <span class="stat-num">评论互动</span><span class="stat-label">实时审核通知</span>
                </div>
                <div class="hero-stat stat-orange">
                  <div class="stat-icon-wrap"><ArtSvgIcon icon="ri:shield-check-line" class="stat-icon text-orange-500" /></div>
                  <span class="stat-num">安全认证</span><span class="stat-label">JWT 权限控制</span>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- 系统概述 -->
        <section id="overview" class="docs-section">
          <h2 class="section-heading"><span class="section-heading-line"></span>系统概述</h2>
          <p class="section-desc">Lin's Blog 系统架构、核心特性和技术栈总览。</p>

          <div class="fcard" id="features">
            <div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-purple"><ArtSvgIcon icon="ri:star-line" class="text-xl" /></div><div class="fc-title">核心特性</div></div>
            <p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />了解 Lin's Blog 的核心能力，帮助您快速评估系统是否满足需求。</p>
            <div class="fc-section-title"><ArtSvgIcon icon="ri:eye-line" /><span>可视化概览</span></div>
            <div class="visual-grid-3">
              <div v-for="f in featuresList" :key="f.title" class="vf-card">
                <div class="vf-icon-wrap"><ArtSvgIcon :icon="f.icon" :class="f.color" /></div>
                <div class="vf-label">{{ f.title }}</div><div class="vf-desc">{{ f.desc }}</div>
              </div>
            </div>
            <div class="fc-section-title"><ArtSvgIcon icon="ri:list-check" /><span>操作步骤</span></div>
            <div v-for="(f, i) in featuresList.slice(0,4)" :key="i" class="step-item"><div class="step-num">{{ i+1 }}</div><div class="step-body"><div class="step-title">{{ f.title }}</div><div class="step-desc">{{ f.desc }}</div></div></div>
            <div class="fc-section-title"><ArtSvgIcon icon="ri:lightbulb-line" /><span>提示与最佳实践</span></div>
            <div class="fc-tip"><ArtSvgIcon icon="ri:lightbulb-line" class="fc-tip-icon text-yellow-500" />所有特性均已在系统中实现，无需额外配置即可使用。</div>
            <div class="fc-tip"><ArtSvgIcon icon="ri:information-line" class="fc-tip-icon text-blue-500" />响应式设计同时支持桌面端和移动端访问管理后台。</div>
          </div>

          <div class="fcard" id="tech">
            <div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-gray"><ArtSvgIcon icon="ri:code-s-slash-line" class="text-xl" /></div><div class="fc-title">技术栈</div></div>
            <p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />了解系统的技术选型，便于二次开发和维护。</p>
            <div class="fc-section-title"><ArtSvgIcon icon="ri:eye-line" /><span>技术组成</span></div>
            <div class="tech-dual">
              <div class="tech-panel">
                <div class="tech-panel-header"><ArtSvgIcon icon="ri:vuejs-line" class="text-green-600 text-lg" /><span>前端</span></div>
                <ul><li v-for="t in frontendTech" :key="t">{{ t }}</li></ul>
              </div>
              <div class="tech-panel">
                <div class="tech-panel-header"><ArtSvgIcon icon="ri:server-line" class="text-blue-600 text-lg" /><span>后端</span></div>
                <ul><li v-for="t in backendTech" :key="t">{{ t }}</li></ul>
              </div>
            </div>
            <div class="fc-tip mt-3"><ArtSvgIcon icon="ri:information-line" class="fc-tip-icon text-blue-500" />前端端口 3006（管理后台）、5173（前台博客）；后端端口 8002。</div>
          </div>

          <div class="fcard" id="quickstart">
            <div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-blue"><ArtSvgIcon icon="ri:rocket-line" class="text-xl" /></div><div class="fc-title">快速开始</div></div>
            <p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />快速在本地启动完整的开发环境。</p>
            <div class="fc-section-title"><ArtSvgIcon icon="ri:computer-line" /><span>环境要求</span></div>
            <div class="env-badges">
              <span class="env-badge"><ArtSvgIcon icon="ri:nodejs-line" /> Node.js ≥ 18</span>
              <span class="env-badge"><ArtSvgIcon icon="ri:python-line" /> Python ≥ 3.10</span>
              <span class="env-badge"><ArtSvgIcon icon="ri:database-2-line" /> MySQL ≥ 8.0</span>
              <span class="env-badge"><ArtSvgIcon icon="ri:terminal-line" /> pnpm ≥ 8</span>
            </div>
            <div class="fc-section-title"><ArtSvgIcon icon="ri:list-check" /><span>操作步骤</span></div>
            <div class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">启动后端服务</div><div class="code-block-terminal"><div class="terminal-dots"><span></span><span></span><span></span></div><pre><code>cd backend
uvicorn src.app.main:app --host 0.0.0.0 --port 8002 --reload</code></pre></div></div></div>
            <div class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">启动管理后台</div><div class="code-block-terminal"><div class="terminal-dots"><span></span><span></span><span></span></div><pre><code>cd admin
pnpm install
pnpm run dev</code></pre></div></div></div>
            <div class="step-item"><div class="step-num">3</div><div class="step-body"><div class="step-title">启动前台博客</div><div class="code-block-terminal"><div class="terminal-dots"><span></span><span></span><span></span></div><pre><code>cd frontend
pnpm install
pnpm run dev</code></pre></div></div></div>
            <div class="fc-section-title"><ArtSvgIcon icon="ri:lightbulb-line" /><span>访问地址</span></div>
            <div class="fc-tip"><ArtSvgIcon icon="ri:link-m" class="fc-tip-icon text-blue-500" />管理后台: <code>localhost:3006</code> &nbsp;|&nbsp; 前台: <code>localhost:5173</code> &nbsp;|&nbsp; API: <code>localhost:8002/api/v1</code></div>
            <div class="fc-tip"><ArtSvgIcon icon="ri:lightbulb-line" class="fc-tip-icon text-yellow-500" />首次启动前请确保 MySQL 数据库已创建并正确配置连接信息。</div>
          </div>
        </section>

        <!-- 其余section保持同样的美化模式 -->
        <section id="dashboard-section" class="docs-section">
          <h2 class="section-heading"><span class="section-heading-line line-blue"></span>数据总览（仪表盘）</h2>
          <p class="section-desc">首页仪表盘提供系统关键数据的实时概览。</p>
          <div class="fcard" id="dashboard">
            <div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-blue"><ArtSvgIcon icon="ri:dashboard-line" class="text-xl" /></div><div class="fc-title">仪表盘</div></div>
            <p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />登录后默认进入的页面，展示核心指标及七日访问趋势图。</p>
            <div class="fc-section-title"><ArtSvgIcon icon="ri:eye-line" /><span>关键指标</span></div>
            <div class="visual-grid-4">
              <div class="vf-card"><div class="vf-icon-wrap"><ArtSvgIcon icon="ri:article-line" class="text-blue-500" /></div><div class="vf-label">文章统计</div><div class="vf-desc">总数 / 今日新增</div></div>
              <div class="vf-card"><div class="vf-icon-wrap"><ArtSvgIcon icon="ri:folder-3-line" class="text-green-500" /></div><div class="vf-label">项目统计</div><div class="vf-desc">总项目数</div></div>
              <div class="vf-card"><div class="vf-icon-wrap"><ArtSvgIcon icon="ri:chat-3-line" class="text-purple-500" /></div><div class="vf-label">评论统计</div><div class="vf-desc">总数 / 待审核</div></div>
              <div class="vf-card"><div class="vf-icon-wrap"><ArtSvgIcon icon="ri:line-chart-line" class="text-orange-500" /></div><div class="vf-label">访问趋势</div><div class="vf-desc">七日折线图</div></div>
            </div>
            <div class="fc-section-title"><ArtSvgIcon icon="ri:list-check" /><span>操作步骤</span></div>
            <div class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">查看数据总览</div><div class="step-desc">登录后台后自动进入仪表盘页面，顶部卡片展示核心数据统计。</div></div></div>
            <div class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">查看访问趋势</div><div class="step-desc">向下滚动查看七日访问量趋势图，了解博客流量变化。</div></div></div>
          </div>
        </section>

        <section id="content-section" class="docs-section">
          <h2 class="section-heading"><span class="section-heading-line line-green"></span>内容管理</h2>
          <p class="section-desc">管理博客的核心内容资产：文章、项目、分类、标签、友链。</p>
          <div class="fcard" id="content-article">
            <div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-blue"><ArtSvgIcon icon="ri:article-line" class="text-xl" /></div><div class="fc-title">文章管理</div><span class="fc-badge">核心</span></div>
            <p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />创建、编辑、发布和管理博客文章。支持 Markdown 编辑器。</p>
            <div class="fc-section-title"><ArtSvgIcon icon="ri:flow-chart" /><span>操作流程</span></div>
            <div class="flow-steps">
              <div class="flow-step"><div class="flow-step-icon gradient-blue"><ArtSvgIcon icon="ri:add-circle-line" /></div><div class="flow-step-label">点击新增</div></div>
              <div class="flow-step-connector"><span></span></div>
              <div class="flow-step"><div class="flow-step-icon gradient-blue"><ArtSvgIcon icon="ri:edit-line" /></div><div class="flow-step-label">编辑内容</div></div>
              <div class="flow-step-connector"><span></span></div>
              <div class="flow-step"><div class="flow-step-icon gradient-blue"><ArtSvgIcon icon="ri:price-tag-3-line" /></div><div class="flow-step-label">设置标签</div></div>
              <div class="flow-step-connector"><span></span></div>
              <div class="flow-step"><div class="flow-step-icon gradient-blue"><ArtSvgIcon icon="ri:image-add-line" /></div><div class="flow-step-label">上传封面</div></div>
              <div class="flow-step-connector"><span></span></div>
              <div class="flow-step"><div class="flow-step-icon gradient-green"><ArtSvgIcon icon="ri:send-plane-line" /></div><div class="flow-step-label">发布</div></div>
            </div>
            <div class="fc-section-title"><ArtSvgIcon icon="ri:list-check" /><span>详细步骤</span></div>
            <div class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">进入文章管理</div><div class="step-desc">点击左侧菜单「内容管理 → 文章列表」，查看所有已发布和草稿文章。</div></div></div>
            <div class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">创建新文章</div><div class="step-desc">点击页面右上角「新增」按钮，进入文章编辑器。</div></div></div>
            <div class="step-item"><div class="step-num">3</div><div class="step-body"><div class="step-title">撰写内容</div><div class="step-desc">填写标题，使用 Markdown 编辑器编写正文，右侧可实时预览。</div></div></div>
            <div class="step-item"><div class="step-num">4</div><div class="step-body"><div class="step-title">设置属性</div><div class="step-desc">选择分类、添加标签、上传封面图片（推荐 16:9 比例）。</div></div></div>
            <div class="step-item"><div class="step-num">5</div><div class="step-body"><div class="step-title">发布文章</div><div class="step-desc">点击「发布」按钮，文章将显示在前台博客页面。</div></div></div>
            <div class="fc-section-title"><ArtSvgIcon icon="ri:lightbulb-line" /><span>提示与最佳实践</span></div>
            <div class="fc-tip"><ArtSvgIcon icon="ri:markdown-line" class="fc-tip-icon text-purple-500" />支持标准 Markdown 语法，编辑器内置工具栏可快速插入标题、表格、代码块。</div>
            <div class="fc-tip"><ArtSvgIcon icon="ri:save-line" class="fc-tip-icon text-green-500" />未完成可保存为草稿。草稿不会在前台展示。</div></div>

          <div class="fcard" id="content-project">
            <div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-green"><ArtSvgIcon icon="ri:folder-3-line" class="text-xl" /></div><div class="fc-title">项目管理</div></div>
            <p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />展示个人项目作品集。支持项目详情、封面图、技术栈标签和外部链接。</p>
            <div class="fc-section-title"><ArtSvgIcon icon="ri:flow-chart" /><span>操作流程</span></div>
            <div class="flow-steps">
              <div class="flow-step"><div class="flow-step-icon gradient-green"><ArtSvgIcon icon="ri:add-circle-line" /></div><div class="flow-step-label">新增项目</div></div>
              <div class="flow-step-connector"><span></span></div>
              <div class="flow-step"><div class="flow-step-icon gradient-green"><ArtSvgIcon icon="ri:edit-line" /></div><div class="flow-step-label">填写信息</div></div>
              <div class="flow-step-connector"><span></span></div>
              <div class="flow-step"><div class="flow-step-icon gradient-green"><ArtSvgIcon icon="ri:stack-line" /></div><div class="flow-step-label">技术栈</div></div>
              <div class="flow-step-connector"><span></span></div>
              <div class="flow-step"><div class="flow-step-icon gradient-blue"><ArtSvgIcon icon="ri:check-line" /></div><div class="flow-step-label">保存</div></div>
            </div></div>

          <div class="fcard" id="content-category"><div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-orange"><ArtSvgIcon icon="ri:price-tag-3-line" class="text-xl" /></div><div class="fc-title">分类管理</div></div><p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />管理文章分类体系，提供归档和筛选能力。</p><div class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">查看分类</div><div class="step-desc">点击「内容管理 → 分类管理」查看所有分类及其关联数量。</div></div></div><div class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">新增分类</div><div class="step-desc">填写分类名称，选择类型（文章/项目/友链），保存即生效。</div></div></div></div>

          <div class="fcard" id="content-tag"><div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-pink"><ArtSvgIcon icon="ri:hashtag" class="text-xl" /></div><div class="fc-title">标签管理</div></div><p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />管理标签体系，为文章和项目提供多维度检索。</p><div class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">查看标签</div><div class="step-desc">点击「内容管理 → 标签管理」查看所有标签。</div></div></div><div class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">新增标签</div><div class="step-desc">输入标签名称，选择标签类型，点击确认即可创建。</div></div></div></div>

          <div class="fcard" id="content-friendlinks"><div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-indigo"><ArtSvgIcon icon="ri:link-m" class="text-xl" /></div><div class="fc-title">友链管理</div></div><p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />管理友情链接，支持审核、分类和状态管理。</p><div class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">管理友链</div><div class="step-desc">在「友链系统 → 友链列表」中查看和管理所有友链。</div></div></div><div class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">审核友链</div><div class="step-desc">新申请的友链状态为「待审核」，在「友链审核」页面操作。</div></div></div></div>
        </section>

        <section id="community-section" class="docs-section">
          <h2 class="section-heading"><span class="section-heading-line line-purple"></span>互动社区</h2>
          <p class="section-desc">管理用户互动：评论、留言、用户管理、消息通知。</p>

          <div class="fcard" id="community-comment"><div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-purple"><ArtSvgIcon icon="ri:chat-3-line" class="text-xl" /></div><div class="fc-title">评论管理</div></div><p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />查看和管理文章、项目的所有评论。支持审核、删除操作。</p><div class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">查看评论</div><div class="step-desc">点击「互动社区 → 评论管理」，查看所有评论列表。</div></div></div><div class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">筛选评论</div><div class="step-desc">使用筛选功能按类型（文章/项目）、审核状态过滤。</div></div></div><div class="step-item"><div class="step-num">3</div><div class="step-body"><div class="step-title">审核评论</div><div class="step-desc">新评论需审核通过后才能在前台显示。</div></div></div><div class="fc-tip"><ArtSvgIcon icon="ri:information-line" class="fc-tip-icon text-blue-500" />评论管理不包含留言板留言，留言板数据在「留言管理」中单独管理。</div></div>

          <div class="fcard" id="community-guestbook"><div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-green"><ArtSvgIcon icon="ri:message-2-line" class="text-xl" /></div><div class="fc-title">留言管理</div></div><p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />管理留言板的留言内容，支持审核、删除操作。</p><div class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">查看留言</div><div class="step-desc">点击「互动社区 → 留言管理」查看所有留言。</div></div></div><div class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">审核留言</div><div class="step-desc">审核通过后在前台留言板显示。</div></div></div></div>

          <div class="fcard" id="community-user"><div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-blue"><ArtSvgIcon icon="ri:team-line" class="text-xl" /></div><div class="fc-title">用户管理</div></div><p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />管理系统用户，支持角色分配、状态管理和密码重置。</p><div class="role-grid"><div class="role-card role-admin"><ArtSvgIcon icon="ri:vip-crown-line" /><span>管理员</span><em>全部权限</em></div><div class="role-card role-user"><ArtSvgIcon icon="ri:user-line" /><span>普通用户</span><em>内容管理</em></div><div class="role-card role-super"><ArtSvgIcon icon="ri:shield-user-line" /><span>超级管理员</span><em>系统配置</em></div></div><div class="step-item mt-3"><div class="step-num">1</div><div class="step-body"><div class="step-title">查看用户</div><div class="step-desc">点击「互动社区 → 用户管理」查看所有系统用户。</div></div></div><div class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">管理用户</div><div class="step-desc">可启用/禁用用户、修改角色、重置密码。</div></div></div></div>

          <div class="fcard" id="community-notification"><div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-yellow"><ArtSvgIcon icon="ri:notification-3-line" class="text-xl" /></div><div class="fc-title">消息通知</div><span class="fc-badge fc-badge-new">NEW</span></div><p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />顶部铃声图标展示实时通知：新评论、新留言、新用户。</p><div class="flow-steps"><div class="flow-step"><div class="flow-step-icon gradient-blue"><ArtSvgIcon icon="ri:chat-3-line" /></div><div class="flow-step-label">新评论</div></div><div class="flow-step"><div class="flow-step-icon gradient-green"><ArtSvgIcon icon="ri:message-2-line" /></div><div class="flow-step-label">新留言</div></div><div class="flow-step"><div class="flow-step-icon gradient-purple"><ArtSvgIcon icon="ri:user-add-line" /></div><div class="flow-step-label">新用户</div></div></div></div>
        </section>

        <section id="system-section" class="docs-section">
          <h2 class="section-heading"><span class="section-heading-line line-gray"></span>系统设置</h2>
          <p class="section-desc">配置博客站点的全局参数。</p>
          <div class="fcard" id="system-site"><div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-blue"><ArtSvgIcon icon="ri:global-line" class="text-xl" /></div><div class="fc-title">站点设置</div></div><p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />配置站点名称、描述、作者信息、位置、邮箱、社交媒体链接、站点图标。保存后实时同步到前台。</p><div class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">进入站点设置</div><div class="step-desc">点击「系统设置 → 站点设置」。</div></div></div><div class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">修改配置</div><div class="step-desc">修改站点名称、作者信息、位置、邮箱、GitHub 等。</div></div></div><div class="step-item"><div class="step-num">3</div><div class="step-body"><div class="step-title">保存生效</div><div class="step-desc">点击「保存」立即生效。前台刷新后可看到更新。</div></div></div></div>

          <div class="fcard" id="system-profile"><div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-pink"><ArtSvgIcon icon="ri:user-heart-line" class="text-xl" /></div><div class="fc-title">关于我管理</div></div><p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />管理个人简历信息。首页「技术栈」区域展示此处设置的技能。</p><div class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">编辑工作经历</div><div class="step-desc">添加公司名称、职位、起止时间、工作描述等。</div></div></div><div class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">管理技能</div><div class="step-desc">添加个人技术技能。首页会动态展示这些技能。</div></div></div></div>
        </section>

        <section id="profile-section" class="docs-section">
          <h2 class="section-heading"><span class="section-heading-line line-orange"></span>个人设置</h2>
          <p class="section-desc">管理个人账户信息和安全设置。</p>
          <div class="fcard" id="profile-info"><div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-blue"><ArtSvgIcon icon="ri:user-3-line" class="text-xl" /></div><div class="fc-title">修改信息</div></div><p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />修改个人资料：头像、姓名、邮箱、GitHub 等。所有修改即时生效。</p><div class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">进入个人信息页</div><div class="step-desc">点击「个人设置 → 修改信息」。顶部可上传头像，下方编辑表单。</div></div></div><div class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">修改并保存</div><div class="step-desc">修改姓名、邮箱、GitHub 链接等，点击「保存修改」。</div></div></div></div>

          <div class="fcard" id="profile-password"><div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-red"><ArtSvgIcon icon="ri:lock-password-line" class="text-xl" /></div><div class="fc-title">更改密码</div><span class="fc-badge">已优化</span></div><p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />修改登录密码。需验证当前密码，新密码 ≥ 6 位，成功后自动退出。</p><div class="flow-steps"><div class="flow-step"><div class="flow-step-icon gradient-red"><ArtSvgIcon icon="ri:key-line" /></div><div class="flow-step-label">当前密码</div></div><div class="flow-step-connector"><span></span></div><div class="flow-step"><div class="flow-step-icon gradient-orange"><ArtSvgIcon icon="ri:shield-keyhole-line" /></div><div class="flow-step-label">新密码(≥6)</div></div><div class="flow-step-connector"><span></span></div><div class="flow-step"><div class="flow-step-icon gradient-green"><ArtSvgIcon icon="ri:check-double-line" /></div><div class="flow-step-label">确认密码</div></div><div class="flow-step-connector"><span></span></div><div class="flow-step"><div class="flow-step-icon gradient-blue"><ArtSvgIcon icon="ri:logout-box-line" /></div><div class="flow-step-label">自动退出</div></div></div></div>

          <div class="fcard" id="profile-resume"><div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-red"><ArtSvgIcon icon="ri:file-pdf-2-line" class="text-xl" /></div><div class="fc-title">简历管理</div></div><p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />上传和管理简历 PDF 文件。支持上传、替换、启用/暂停、删除。</p><div class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">上传简历</div><div class="step-desc">点击「个人设置 → 简历管理」，选择 PDF 文件（≤10MB）上传。</div></div></div><div class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">管理简历</div><div class="step-desc">上传后可替换、暂停/启用或删除文件。</div></div></div><div class="fc-tip"><ArtSvgIcon icon="ri:file-pdf-2-line" class="fc-tip-icon text-red-500" />仅支持 PDF 格式，文件大小不超过 10MB。</div></div>

          <div class="fcard" id="profile-pdfkey"><div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-yellow"><ArtSvgIcon icon="ri:key-2-line" class="text-xl" /></div><div class="fc-title">PDF 密钥管理</div></div><p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />生成和管理 PDF 访问密钥，用于控制简历下载权限。</p><div class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">生成密钥</div><div class="step-desc">在「PDF 密钥管理」页面点击「生成密钥」。</div></div></div><div class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">管理密钥</div><div class="step-desc">查看密钥列表，删除过期密钥。</div></div></div></div>
        </section>

        <section id="statistics-section" class="docs-section">
          <h2 class="section-heading"><span class="section-heading-line line-teal"></span>统计分析</h2>
          <p class="section-desc">多维度数据分析，帮助了解博客运营状况。</p>
          <div class="fcard" id="statistics-overview"><div class="fc-header"><div class="fc-icon-wrap fc-icon-gradient-green"><ArtSvgIcon icon="ri:trending-up-line" class="text-xl" /></div><div class="fc-title">统计分析</div></div><p class="fc-purpose"><ArtSvgIcon icon="ri:lightbulb-flash-line" class="w-4 h-4 mr-2 text-yellow-500 inline-block" />查看博客的统计数据：文章统计、访问趋势、归档分析等。</p><div class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">统计概览</div><div class="step-desc">点击「统计分析 → 统计概览」查看核心数据仪表盘。</div></div></div><div class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">文章统计</div><div class="step-desc">查看各文章的阅读量、评论数等详细数据。</div></div></div><div class="step-item"><div class="step-num">3</div><div class="step-body"><div class="step-title">归档分析</div><div class="step-desc">按时间维度查看文章发布和访问分布。</div></div></div></div>
        </section>

        <section id="faq" class="docs-section">
          <h2 class="section-heading"><span class="section-heading-line line-pink"></span>常见问题 FAQ</h2>
          <p class="section-desc">共 {{ faqList.length }} 个问答，点击展开查看解答。</p>
          <div class="faq-list">
            <div v-for="(item, idx) in faqList" :key="idx" class="faq-item" :class="{ 'faq-item-open': item.open }">
              <div class="faq-question" @click="item.open = !item.open">
                <span class="faq-q-badge">Q</span><span class="faq-q-text">{{ item.q }}</span>
                <ArtSvgIcon icon="ri:arrow-down-s-line" class="faq-arrow" :class="{ 'rotate-180': item.open }" />
              </div>
              <div v-show="item.open" class="faq-answer">
                <span class="faq-a-badge">A</span><div class="faq-a-content">{{ item.a }}</div>
              </div>
            </div>
          </div>
          <div class="faq-more"><p class="text-sm text-gray-400">没有找到答案？请查阅 <a :href="githubUrl" target="_blank" class="text-blue-500 hover:underline font-medium">GitHub 仓库</a> 或联系开发者。</p></div>
        </section>

        <footer class="docs-footer">
          <div class="footer-glow"></div>
          <div class="footer-content">
            <span class="footer-brand">Lin's Blog <span class="footer-version">v1.0</span></span>
            <span class="footer-divider">·</span>
            <a :href="githubUrl" target="_blank" class="footer-link"><ArtSvgIcon icon="ri:github-line" class="w-3.5 h-3.5 mr-1 inline-block" />GitHub</a>
          </div>
          <p class="footer-sub">最后更新：2026-05-25 &nbsp;|&nbsp; 文档覆盖 {{ totalDocFeatures }} 个功能模块</p>
        </footer>
      </article></main>

      <aside class="docs-toc">
        <div class="toc-content">
          <h4 class="toc-title">📑 本页目录</h4>
          <ul class="toc-list">
            <li v-for="item in tocItems" :key="item.id" :class="{ 'toc-active': activeNav === item.id }">
              <a :href="`#${item.id}`" @click.prevent="scrollTo(item.id)">{{ item.label }}</a>
            </li>
          </ul>
        </div>
      </aside>
    </div>

    <!-- 回到顶部 -->
    <button class="back-to-top" :class="{ visible: showBackTop }" @click="scrollToTop" title="回到顶部">
      <ArtSvgIcon icon="ri:arrow-up-line" class="w-5 h-5" />
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, onUnmounted } from 'vue'

defineOptions({ name: 'DocsPage' })

const githubUrl = 'https://github.com/dameng2026'
const activeNav = ref('intro')
const searchQuery = ref('')
const searchFocused = ref(false)
const showBackTop = ref(false)
const progressPercent = ref(0)
const totalDocFeatures = 17

interface NavGroup { title: string; icon: string; expanded: boolean; items: { id: string; label: string; icon: string }[] }

const navGroups = reactive<NavGroup[]>([
  { title: '系统概述', icon: 'ri:book-2-line', expanded: true, items: [
    { id: 'features', label: '核心特性', icon: 'ri:star-line' }, { id: 'tech', label: '技术栈', icon: 'ri:code-s-slash-line' }, { id: 'quickstart', label: '快速开始', icon: 'ri:rocket-line' },
  ]},
  { title: '数据总览', icon: 'ri:dashboard-line', expanded: true, items: [{ id: 'dashboard', label: '仪表盘', icon: 'ri:dashboard-line' }]},
  { title: '内容管理', icon: 'ri:file-list-3-line', expanded: true, items: [
    { id: 'content-article', label: '文章管理', icon: 'ri:article-line' }, { id: 'content-project', label: '项目管理', icon: 'ri:folder-3-line' },
    { id: 'content-category', label: '分类管理', icon: 'ri:price-tag-3-line' }, { id: 'content-tag', label: '标签管理', icon: 'ri:hashtag' },
    { id: 'content-friendlinks', label: '友链管理', icon: 'ri:link-m' },
  ]},
  { title: '互动社区', icon: 'ri:user-community-line', expanded: true, items: [
    { id: 'community-comment', label: '评论管理', icon: 'ri:chat-3-line' }, { id: 'community-guestbook', label: '留言管理', icon: 'ri:message-2-line' },
    { id: 'community-user', label: '用户管理', icon: 'ri:team-line' }, { id: 'community-notification', label: '消息通知', icon: 'ri:notification-3-line' },
  ]},
  { title: '系统设置', icon: 'ri:settings-3-line', expanded: true, items: [
    { id: 'system-site', label: '站点设置', icon: 'ri:global-line' }, { id: 'system-profile', label: '关于我管理', icon: 'ri:user-heart-line' },
  ]},
  { title: '个人设置', icon: 'ri:user-settings-line', expanded: true, items: [
    { id: 'profile-info', label: '修改信息', icon: 'ri:user-3-line' }, { id: 'profile-password', label: '更改密码', icon: 'ri:lock-password-line' },
    { id: 'profile-resume', label: '简历管理', icon: 'ri:file-pdf-2-line' }, { id: 'profile-pdfkey', label: 'PDF密钥', icon: 'ri:key-2-line' },
  ]},
  { title: '统计分析', icon: 'ri:bar-chart-2-line', expanded: true, items: [{ id: 'statistics-overview', label: '统计分析', icon: 'ri:trending-up-line' }]},
  { title: '帮助', icon: 'ri:question-line', expanded: true, items: [{ id: 'faq', label: '常见问题', icon: 'ri:question-answer-line' }]},
])

const featuresList = [
  { icon: 'ri:palette-line', color: 'text-purple-500', title: '现代化 UI', desc: 'Element Plus' }, { icon: 'ri:zap-line', color: 'text-yellow-500', title: '高效性能', desc: 'Vue 3 + Vite' },
  { icon: 'ri:shield-line', color: 'text-blue-500', title: '安全可靠', desc: 'JWT + 加密' }, { icon: 'ri:responsive-line', color: 'text-green-500', title: '响应式', desc: '桌面+移动端' },
  { icon: 'ri:markdown-line', color: 'text-indigo-500', title: 'Markdown', desc: '实时预览' }, { icon: 'ri:chat-3-line', color: 'text-pink-500', title: '评论互动', desc: '审核+通知' },
]
const frontendTech = ['Vue 3', 'TypeScript', 'Element Plus', 'Vite', 'Pinia']
const backendTech = ['Python', 'FastAPI', 'MySQL', 'JWT', 'SQLAlchemy']

const tocItems = [
  { id: 'intro', label: '介绍' }, { id: 'overview', label: '系统概述' }, { id: 'dashboard-section', label: '数据总览' },
  { id: 'content-section', label: '内容管理' }, { id: 'community-section', label: '互动社区' }, { id: 'system-section', label: '系统设置' },
  { id: 'profile-section', label: '个人设置' }, { id: 'statistics-section', label: '统计分析' }, { id: 'faq', label: '常见问题' },
]

const faqList = reactive([
  { q: '如何发布一篇文章？', a: '登录后台，点击「内容管理 → 文章列表」，点击「新增」，使用 Markdown 编辑器撰写内容，选择分类和标签，上传封面图（可选），点击「发布」即可。', open: false },
  { q: '忘记密码怎么办？', a: '在登录页面点击「忘记密码」，输入注册邮箱获取验证码后重置。如无法重置请联系管理员。', open: false },
  { q: '评论列表为什么没有留言板数据？', a: '评论管理默认只显示文章和项目评论。留言板数据在「互动社区 → 留言管理」中单独管理。', open: false },
  { q: '修改密码后会自动退出吗？', a: '是的。修改成功后 1.5 秒自动退出，需用新密码重新登录。', open: false },
  { q: '如何上传简历？', a: '「个人设置 → 简历管理」，选择 PDF 文件（≤10MB）上传。可替换、暂停/启用或删除。', open: false },
  { q: '站点设置多久生效？', a: '保存后立即生效，前台刷新即可看到最新配置。', open: false },
  { q: '统计页面在哪里？', a: '点击「统计分析」菜单查看运营数据，包含统计概览、文章统计和归档分析。', open: false },
  { q: '消息通知怎么看？', a: '点击顶部导航栏铃声图标，查看新评论、新留言、新用户通知。', open: false },
])

const searchResults = reactive({ total: 0 })

function highlightText(text: string): string { if (!searchQuery.value || !text) return text; const e = searchQuery.value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); return text.replace(new RegExp(`(${e})`, 'gi'), '<mark class="search-highlight">$1</mark>') }
function handleSearch() { if (!searchQuery.value) { searchResults.total = 0; return } const t = document.querySelector('.docs-content')?.textContent || ''; const e = searchQuery.value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); const m = t.match(new RegExp(e, 'gi')); searchResults.total = m ? m.length : 0; navGroups.forEach(g => { g.expanded = true }) }
function clearSearch() { searchQuery.value = ''; searchResults.total = 0 }
function scrollTo(id: string) { activeNav.value = id; const el = document.getElementById(id); if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' }) }
function scrollToTop() { document.querySelector('.docs-content')?.scrollTo({ top: 0, behavior: 'smooth' }) }

function handleScroll() {
  const main = document.querySelector('.docs-content')
  if (main) {
    const st = main.scrollTop
    const sh = main.scrollHeight - main.clientHeight
    progressPercent.value = sh > 0 ? Math.round((st / sh) * 100) : 0
    showBackTop.value = st > 400
  }
  for (let i = tocItems.length - 1; i >= 0; i--) {
    const el = document.getElementById(tocItems[i].id); if (el && el.getBoundingClientRect().top <= 120) { activeNav.value = tocItems[i].id; break }
  }
}
function handleKeydown(e: KeyboardEvent) { if ((e.ctrlKey || e.metaKey) && e.key === 'k') { e.preventDefault(); (document.querySelector('.search-input') as HTMLInputElement)?.focus() } }
onMounted(() => document.addEventListener('keydown', handleKeydown))
onUnmounted(() => document.removeEventListener('keydown', handleKeydown))
</script>

<style scoped>
.docs-page { min-height: 100vh; background: linear-gradient(180deg, #f8fafc 0%, #f5f7fa 100%); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }

/* Reading Progress */
.reading-progress { position: fixed; top: 0; left: 0; height: 3px; background: linear-gradient(90deg, #1890ff, #722ed1); z-index: 200; transition: width 0.2s ease; border-radius: 0 2px 2px 0; }

/* Header */
.docs-header { position: sticky; top: 0; z-index: 100; background: rgba(255,255,255,0.92); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border-bottom: 1px solid rgba(0,0,0,0.06); }
.docs-header-content { display: flex; justify-content: space-between; align-items: center; padding: 10px 24px; max-width: 1440px; margin: 0 auto; }
.brand-logo { width: 32px; height: 32px; border-radius: 8px; background: linear-gradient(135deg, #e6f7ff, #f0f5ff); display: flex; align-items: center; justify-content: center; }
.header-link { display: flex; align-items: center; color: #666; font-size: 13px; text-decoration: none; padding: 5px 12px; border-radius: 6px; transition: all 0.2s; }
.header-link:hover { background: #f0f0f0; color: #333; }
.header-link-back { background: #f0f5ff; color: #1890ff; } .header-link-back:hover { background: #e6f7ff; }
.search-box { position: relative; display: flex; align-items: center; }
.search-icon { position: absolute; left: 12px; color: #999; font-size: 16px; pointer-events: none; z-index: 1; }
.search-input { width: 220px; height: 36px; padding: 0 36px 0 36px; border: 1px solid #e0e0e0; border-radius: 8px; font-size: 13px; color: #333; background: #f9f9f9; outline: none; transition: all 0.25s; }
.search-input:focus { width: 300px; border-color: #1890ff; background: white; box-shadow: 0 0 0 3px rgba(24,144,255,0.1); }
.search-clear { position: absolute; right: 8px; cursor: pointer; color: #ccc; display: flex; align-items: center; } .search-clear:hover { color: #999; }
.search-shortcut { position: absolute; right: 10px; padding: 1px 6px; font-size: 11px; color: #999; background: #eee; border-radius: 3px; font-family: inherit; pointer-events: none; }
.search-results-bar { padding: 6px 24px; font-size: 12px; color: #1890ff; background: #e6f7ff; border-top: 1px solid #bae7ff; font-weight: 500; }
.search-results-bar.search-empty { background: #fff7e6; border-top-color: #ffd591; color: #d48806; }
.search-highlight { background: linear-gradient(180deg, transparent 60%, #ffd54f 60%); color: #333; padding: 1px 2px; }

/* Layout */
.docs-body { display: flex; max-width: 1440px; margin: 0 auto; }
.docs-sidebar { width: 240px; flex-shrink: 0; background: white; border-right: 1px solid #e8e8e8; min-height: calc(100vh - 56px); position: sticky; top: 56px; overflow-y: auto; padding-bottom: 24px; }
.sidebar-content { padding: 16px 0; }
.sidebar-section { margin-bottom: 4px; }
.sidebar-title { display: flex; align-items: center; gap: 6px; font-size: 11px; color: #999; padding: 10px 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; cursor: pointer; user-select: none; transition: all 0.2s; }
.sidebar-title:hover { color: #666; background: #fafafa; }
.sidebar-title-expanded { color: #555; }
.sidebar-title-icon { opacity: 0.5; transition: opacity 0.2s; } .sidebar-title:hover .sidebar-title-icon { opacity: 0.8; }
.sidebar-collapse-arrow { margin-left: auto; font-size: 14px; transition: transform 0.25s; opacity: 0.5; }
.sidebar-list-wrapper { overflow: hidden; transition: max-height 0.3s ease; max-height: 0; } .sidebar-list-expanded { max-height: 600px; }
.sidebar-list { list-style: none; margin: 0; padding: 0; }
.sidebar-list li a { display: flex; align-items: center; font-size: 13px; color: #666; text-decoration: none; padding: 8px 16px 8px 28px; transition: all 0.2s; border-left: 2px solid transparent; position: relative; }
.sidebar-list li.active a { background: linear-gradient(90deg, #e6f7ff 0%, transparent 100%); color: #1890ff; border-left-color: #1890ff; font-weight: 500; }
.sidebar-list li:hover:not(.active) a { background: #fafafa; color: #333; }

/* Content */
.docs-content { flex: 1; padding: 32px 40px; min-width: 0; overflow-y: auto; scroll-behavior: smooth; }
.docs-section { margin-bottom: 56px; }
.docs-hero { position: relative; background: linear-gradient(135deg, #e8f4fd 0%, #f5f7fa 30%, #faf5ff 70%, #fce4ec 100%); border-radius: 16px; padding: 56px 48px; margin-bottom: 48px; overflow: hidden; border: 1px solid rgba(24,144,255,0.08); }
.hero-glow { position: absolute; border-radius: 50%; filter: blur(60px); opacity: 0.15; pointer-events: none; }
.hero-glow-1 { width: 300px; height: 300px; background: #1890ff; top: -80px; right: -60px; }
.hero-glow-2 { width: 250px; height: 250px; background: #722ed1; bottom: -60px; left: -40px; }
.hero-content { display: flex; align-items: center; gap: 56px; position: relative; z-index: 1; }
.hero-left { flex: 1; }
.hero-badge { display: inline-flex; align-items: center; gap: 6px; padding: 4px 14px; font-size: 12px; color: #1890ff; background: rgba(24,144,255,0.08); border: 1px solid rgba(24,144,255,0.15); border-radius: 20px; margin-bottom: 16px; font-weight: 500; }
.hero-badge-dot { width: 6px; height: 6px; border-radius: 50%; background: #1890ff; animation: pulse 2s ease-in-out infinite; }
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }
.hero-title { font-size: 36px; font-weight: 800; color: #1a1a2e; margin: 0 0 16px; line-height: 1.2; letter-spacing: -0.5px; }
.hero-title-highlight { background: linear-gradient(135deg, #1890ff, #722ed1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.hero-desc { font-size: 16px; color: #666; line-height: 1.8; margin-bottom: 28px; max-width: 520px; }
.hero-desc strong { color: #1890ff; font-weight: 600; }
.hero-actions { display: flex; gap: 12px; }
.hero-btn { display: inline-flex; align-items: center; padding: 11px 24px; font-size: 14px; border-radius: 10px; text-decoration: none; font-weight: 600; transition: all 0.25s; }
.hero-btn-primary { background: linear-gradient(135deg, #1890ff, #096dd9); color: white; box-shadow: 0 4px 14px rgba(24,144,255,0.35); }
.hero-btn-primary:hover { transform: translateY(-1px); box-shadow: 0 6px 20px rgba(24,144,255,0.45); }
.hero-btn-outline { background: white; color: #333; border: 1px solid #d9d9d9; }
.hero-btn-outline:hover { border-color: #1890ff; color: #1890ff; background: #f0f5ff; }
.hero-right { flex-shrink: 0; }
.hero-stats { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.hero-stat { display: flex; flex-direction: column; align-items: center; padding: 20px 18px; background: rgba(255,255,255,0.85); backdrop-filter: blur(8px); border-radius: 14px; border: 1px solid rgba(0,0,0,0.06); min-width: 120px; transition: all 0.25s; }
.hero-stat:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,0.06); }
.stat-icon-wrap { width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 8px; }
.stat-blue .stat-icon-wrap { background: #e6f7ff; } .stat-green .stat-icon-wrap { background: #f6ffed; }
.stat-purple .stat-icon-wrap { background: #f9f0ff; } .stat-orange .stat-icon-wrap { background: #fff7e6; }
.stat-icon { font-size: 22px; }
.stat-num { font-size: 14px; font-weight: 700; color: #333; }
.stat-label { font-size: 11px; color: #999; margin-top: 3px; }

/* Section headings */
.section-heading { font-size: 26px; font-weight: 800; color: #1a1a2e; margin: 0 0 6px; display: flex; align-items: center; gap: 12px; letter-spacing: -0.3px; }
.section-heading-line { display: inline-block; width: 4px; height: 24px; border-radius: 2px; background: linear-gradient(180deg, #1890ff, #722ed1); }
.section-heading-line.line-blue { background: linear-gradient(180deg, #1890ff, #40a9ff); }
.section-heading-line.line-green { background: linear-gradient(180deg, #52c41a, #73d13d); }
.section-heading-line.line-purple { background: linear-gradient(180deg, #722ed1, #b37feb); }
.section-heading-line.line-gray { background: linear-gradient(180deg, #595959, #8c8c8c); }
.section-heading-line.line-orange { background: linear-gradient(180deg, #fa8c16, #ffa940); }
.section-heading-line.line-teal { background: linear-gradient(180deg, #13c2c2, #36cfc9); }
.section-heading-line.line-pink { background: linear-gradient(180deg, #eb2f96, #ff85c0); }
.section-desc { font-size: 15px; color: #999; margin: 8px 0 28px; }

/* Feature Card */
.fcard { background: white; border-radius: 14px; padding: 28px 32px; margin-bottom: 20px; border: 1px solid #f0f0f0; position: relative; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
.fcard:hover { border-color: #e0e0e0; box-shadow: 0 4px 20px rgba(0,0,0,0.06); transform: translateY(-1px); }
.fc-header { display: flex; align-items: flex-start; gap: 14px; margin-bottom: 16px; }
.fc-icon-wrap { width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: white; }
.fc-icon-gradient-blue { background: linear-gradient(135deg, #1890ff, #40a9ff); }
.fc-icon-gradient-green { background: linear-gradient(135deg, #52c41a, #73d13d); }
.fc-icon-gradient-purple { background: linear-gradient(135deg, #722ed1, #b37feb); }
.fc-icon-gradient-orange { background: linear-gradient(135deg, #fa8c16, #ffa940); }
.fc-icon-gradient-pink { background: linear-gradient(135deg, #eb2f96, #ff85c0); }
.fc-icon-gradient-indigo { background: linear-gradient(135deg, #2f54eb, #597ef7); }
.fc-icon-gradient-red { background: linear-gradient(135deg, #f5222d, #ff4d4f); }
.fc-icon-gradient-yellow { background: linear-gradient(135deg, #fadb14, #ffec3d); }
.fc-icon-gradient-gray { background: linear-gradient(135deg, #595959, #8c8c8c); }
.fc-title { font-size: 19px; font-weight: 700; color: #1a1a2e; line-height: 44px; }
.fc-badge { font-size: 11px; font-weight: 700; color: white; background: linear-gradient(135deg, #1890ff, #722ed1); padding: 3px 10px; border-radius: 6px; margin-left: 10px; vertical-align: middle; letter-spacing: 0.5px; }
.fc-badge-new { background: linear-gradient(135deg, #52c41a, #13c2c2); }
.fc-purpose { font-size: 14px; color: #555; line-height: 1.8; margin-bottom: 20px; padding: 12px 16px; background: linear-gradient(135deg, #fafafa, #f0f5ff); border-radius: 10px; border-left: 3px solid #1890ff; font-weight: 500; }
.fc-section-title { font-size: 14px; font-weight: 700; color: #444; margin: 24px 0 14px; padding-bottom: 10px; border-bottom: 1px solid #f5f5f5; display: flex; align-items: center; gap: 8px; text-transform: uppercase; letter-spacing: 0.5px; font-size: 12px; }

.visual-grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
.visual-grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
.vf-card { text-align: center; padding: 20px 12px; background: #fafbfc; border-radius: 12px; border: 1px solid #f0f0f0; transition: all 0.2s; }
.vf-card:hover { background: white; border-color: #e0e0e0; box-shadow: 0 4px 12px rgba(0,0,0,0.04); transform: translateY(-1px); }
.vf-icon-wrap { width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; margin: 0 auto 8px; font-size: 22px; background: white; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
.vf-label { font-size: 13px; font-weight: 700; color: #333; }
.vf-desc { font-size: 11px; color: #999; margin-top: 3px; }

.flow-steps { display: flex; align-items: center; flex-wrap: wrap; gap: 0; }
.flow-step { display: flex; flex-direction: column; align-items: center; gap: 8px; }
.flow-step-icon { width: 48px; height: 48px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 22px; color: white; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
.flow-step-icon.gradient-blue { background: linear-gradient(135deg, #1890ff, #40a9ff); }
.flow-step-icon.gradient-green { background: linear-gradient(135deg, #52c41a, #73d13d); }
.flow-step-icon.gradient-red { background: linear-gradient(135deg, #f5222d, #ff4d4f); }
.flow-step-icon.gradient-orange { background: linear-gradient(135deg, #fa8c16, #ffa940); }
.flow-step-icon.gradient-purple { background: linear-gradient(135deg, #722ed1, #b37feb); }
.flow-step-label { font-size: 12px; color: #666; font-weight: 600; }
.flow-step-connector { display: flex; align-items: center; margin: 0 -8px; margin-bottom: 28px; }
.flow-step-connector span { display: block; width: 32px; height: 2px; background: linear-gradient(90deg, #d9d9d9, #e8e8e8); border-radius: 1px; }

.tech-dual { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.tech-panel { background: #fafbfc; border-radius: 12px; padding: 20px; border: 1px solid #f0f0f0; transition: all 0.2s; }
.tech-panel:hover { border-color: #e0e0e0; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
.tech-panel-header { display: flex; align-items: center; gap: 8px; font-size: 16px; font-weight: 700; color: #333; margin-bottom: 14px; padding-bottom: 10px; border-bottom: 1px solid #f0f0f0; }
.tech-panel ul { list-style: none; margin: 0; padding: 0; }
.tech-panel li { font-size: 13px; color: #666; padding: 6px 0 6px 20px; position: relative; transition: all 0.15s; }
.tech-panel li:hover { color: #333; }
.tech-panel li::before { content: ''; position: absolute; left: 0; top: 13px; width: 7px; height: 7px; border-radius: 50%; background: linear-gradient(135deg, #1890ff, #40a9ff); }

.env-badges { display: flex; flex-wrap: wrap; gap: 10px; }
.env-badge { display: inline-flex; align-items: center; gap: 8px; padding: 10px 18px; background: linear-gradient(135deg, #f0f5ff, #e6f7ff); border: 1px solid #d6e4ff; border-radius: 10px; font-size: 13px; color: #1890ff; font-weight: 600; transition: all 0.2s; }
.env-badge:hover { transform: translateY(-1px); box-shadow: 0 4px 12px rgba(24,144,255,0.1); }

.role-grid { display: flex; gap: 14px; }
.role-card { display: flex; flex-direction: column; align-items: center; gap: 6px; padding: 20px 24px; border-radius: 14px; border: 1px solid #e8e8e8; text-align: center; transition: all 0.25s; }
.role-card:hover { transform: translateY(-2px); }
.role-card span { font-weight: 700; font-size: 14px; }
.role-card em { font-size: 11px; color: #999; font-style: normal; }
.role-admin { background: linear-gradient(135deg, #fff1f0, #fff2f0); border-color: #ffa39e; } .role-admin span { color: #cf1322; }
.role-user { background: linear-gradient(135deg, #e6f7ff, #f0f5ff); border-color: #91d5ff; } .role-user span { color: #1890ff; }
.role-super { background: linear-gradient(135deg, #f9f0ff, #faf5ff); border-color: #d3adf7; } .role-super span { color: #722ed1; }

.step-item { display: flex; gap: 14px; margin-bottom: 16px; }
.step-num { width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #1890ff, #40a9ff); color: white; border-radius: 50%; font-size: 13px; font-weight: 800; flex-shrink: 0; margin-top: 2px; box-shadow: 0 2px 8px rgba(24,144,255,0.25); }
.step-body { flex: 1; }
.step-title { font-size: 14px; font-weight: 700; color: #1a1a2e; margin: 0 0 4px; }
.step-desc { font-size: 13px; color: #666; line-height: 1.7; }

.code-block-terminal { background: #1a1a2e; border-radius: 10px; padding: 14px 18px; overflow-x: auto; margin-top: 8px; position: relative; }
.terminal-dots { display: flex; gap: 6px; margin-bottom: 10px; }
.terminal-dots span { width: 10px; height: 10px; border-radius: 50%; }
.terminal-dots span:nth-child(1) { background: #ff5f56; } .terminal-dots span:nth-child(2) { background: #ffbd2e; } .terminal-dots span:nth-child(3) { background: #27c93f; }
.code-block-terminal pre { margin: 0; } .code-block-terminal code { font-size: 12px; line-height: 1.7; color: #e2e8f0; font-family: 'SF Mono', Monaco, 'Cascadia Code', monospace; }

.fc-tip { display: flex; align-items: flex-start; gap: 10px; font-size: 13px; color: #666; line-height: 1.6; margin-bottom: 10px; }
.fc-tip code { background: #f0f0f0; padding: 1px 6px; border-radius: 4px; font-family: 'SF Mono', Monaco, monospace; font-size: 12px; color: #d63384; }
.fc-tip-icon { font-size: 17px; flex-shrink: 0; margin-top: 1px; }

.faq-list { display: flex; flex-direction: column; gap: 12px; margin-top: 20px; }
.faq-item { background: white; border-radius: 14px; border: 1px solid #f0f0f0; overflow: hidden; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
.faq-item:hover { border-color: #e0e0e0; }
.faq-item-open { border-color: #91d5ff !important; box-shadow: 0 4px 16px rgba(24,144,255,0.1); }
.faq-question { display: flex; align-items: flex-start; gap: 12px; padding: 18px 22px; cursor: pointer; user-select: none; transition: background 0.2s; }
.faq-question:hover { background: #fafbfc; }
.faq-q-badge { width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #e6f7ff, #bae7ff); color: #1890ff; border-radius: 8px; font-size: 13px; font-weight: 800; flex-shrink: 0; margin-top: 1px; }
.faq-q-text { flex: 1; font-size: 15px; color: #1a1a2e; font-weight: 600; line-height: 1.5; }
.faq-arrow { font-size: 20px; color: #bbb; flex-shrink: 0; margin-top: 3px; transition: transform 0.3s; }
.faq-item-open .faq-arrow { color: #1890ff; }
.faq-answer { display: flex; gap: 12px; padding: 0 22px 20px; animation: faqIn 0.3s ease; }
@keyframes faqIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
.faq-a-badge { width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #f6ffed, #d9f7be); color: #52c41a; border-radius: 8px; font-size: 13px; font-weight: 800; flex-shrink: 0; }
.faq-a-content { flex: 1; font-size: 14px; color: #666; line-height: 1.9; }
.faq-more { margin-top: 20px; text-align: center; }

/* TOC */
.docs-toc { width: 190px; flex-shrink: 0; padding: 32px 16px; }
.toc-content { position: sticky; top: 80px; }
.toc-title { font-size: 11px; color: #bbb; margin-bottom: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; }
.toc-list { list-style: none; margin: 0; padding: 0; }
.toc-list li { padding: 2px 0; }
.toc-list li a { font-size: 13px; color: #999; text-decoration: none; display: block; padding: 4px 10px; border-radius: 6px; transition: all 0.2s; border-left: 2px solid transparent; }
.toc-list li a:hover { color: #1890ff; background: #f0f5ff; }
.toc-list li.toc-active a { color: #1890ff; background: linear-gradient(90deg, #e6f7ff 0%, transparent 100%); border-left-color: #1890ff; font-weight: 600; }

/* Footer */
.docs-footer { margin-top: 56px; padding: 36px 0 48px; text-align: center; position: relative; }
.footer-glow { position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 200px; height: 1px; background: linear-gradient(90deg, transparent, #d9d9d9, transparent); }
.footer-content { display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 8px; }
.footer-brand { font-size: 14px; font-weight: 700; color: #555; }
.footer-version { font-size: 11px; color: #1890ff; background: #e6f7ff; padding: 2px 8px; border-radius: 4px; margin-left: 6px; font-weight: 600; }
.footer-divider { color: #ddd; }
.footer-link { font-size: 13px; color: #999; text-decoration: none; transition: color 0.2s; } .footer-link:hover { color: #333; }
.footer-sub { margin-top: 4px !important; font-size: 12px !important; color: #bbb !important; }

/* Back to top */
.back-to-top { position: fixed; bottom: 32px; right: 32px; width: 44px; height: 44px; border-radius: 14px; background: white; border: 1px solid #e8e8e8; box-shadow: 0 4px 14px rgba(0,0,0,0.08); display: flex; align-items: center; justify-content: center; cursor: pointer; opacity: 0; transform: translateY(12px); transition: all 0.3s; z-index: 50; color: #666; }
.back-to-top.visible { opacity: 1; transform: translateY(0); }
.back-to-top:hover { background: #1890ff; color: white; border-color: #1890ff; box-shadow: 0 6px 20px rgba(24,144,255,0.3); transform: translateY(-2px); }

@media (max-width: 1200px) { .docs-toc { display: none; } .visual-grid-3, .visual-grid-4 { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 768px) {
  .docs-sidebar { display: none; } .docs-content { padding: 20px 16px; } .docs-hero { padding: 36px 24px; }
  .hero-content { flex-direction: column; gap: 28px; } .hero-title { font-size: 26px; } .hero-right { width: 100%; }
  .hero-stats { grid-template-columns: 1fr 1fr; } .visual-grid-3, .visual-grid-4 { grid-template-columns: 1fr; }
  .tech-dual { grid-template-columns: 1fr; } .flow-steps { flex-direction: column; align-items: flex-start; }
  .flow-step-connector { display: none; } .role-grid { flex-direction: column; }
  .back-to-top { bottom: 20px; right: 16px; }
}
</style>