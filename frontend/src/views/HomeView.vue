<template>
  <!-- 上半部分：首屏区 -->
  <div class="home-page p-[1.75rem] bg-[#f8f9fd]">
    <div class="grid grid-cols-1 lg:grid-cols-5 gap-6 mb-8 home-top-grid" style="margin-left: -1.75rem">
      <!-- 左侧：Hero 首屏区（占宽80%）-->
      <div class="lg:col-span-4 bg-[linear-gradient(to_right,#fcfdfd_0%,#fcfdfd_30%,transparent_100%)]">
        <div class="rounded-xl p-8 pb-[70px] relative overflow-hidden shadow-sm h-[420px] home-hero-card">
          <!-- 3D 插画作为绝对定位背景（最终设计图效果）-->
          <div class="absolute right-0 top-0 w-[40%] h-[100%] flex items-center justify-end pointer-events-none">
            <img src="/images/hero-3d.png" alt="AI Cube"
              class="w-auto h-full object-contain object-right-center ml-auto" />
          </div>

          <div class="relative z-10">
            <!-- 顶部标签：宽度由内容撑开，不占满整行 -->
            <p
              class="inline-flex items-center text-sm mb-4 bg-blue-50 px-3 py-1.5 rounded-full pl-[1rem] text-blue-700">
               <img src="/icons/applaud.svg" alt="Applaud" class="w-4 h-4 mr-2" />
              你好，我是 {{ siteSettings.author_name || 'Lin' }}
            </p>

            <h1 class="text-[2rem] font-bold text-gray-900 mb-4 tracking-wide pl-[1rem]">
              专注 <span class="text-blue-600">Agent 开发与前端技术</span>
            </h1>
            <h2 class="text-[2rem] font-bold text-gray-900 mb-6 tracking-wide pl-[1rem]">
              构建智能与体验兼备的产品
            </h2>

            <div class="text-gray-600 text-[15px] mb-4 max-w-2xl space-y-2 leading-relaxed pl-[1rem]">
              <p>{{ siteSettings.description || '热爱技术，喜欢构建有价值的应用。' }}</p>
              <p>在 Agent、LLM 应用、前端工程化等领域不断探索与实践。</p>
            </div>

            <div class="flex flex-wrap gap-4 mb-8 pl-[1rem]">
              <button @click="router.push('/projects')"
                class="px-7 py-3 bg-blue-600 text-white rounded-lg font-medium text-[15px] hover:bg-blue-700 transition-all">
                查看我的项目</button>
              <button @click="router.push('/articles')"
                class="px-7 py-3 bg-white text-gray-900 border border-gray-300 rounded-lg font-medium text-[15px] hover:bg-gray-50 transition-all">
                阅读我的文章
              </button>
            </div>

            <div class="flex flex-wrap gap-3 mb-4">
              <span class="flex items-center px-4 py-2 bg-white rounded-lg text-[0.75rem] font-medium text-gray-700">
                <img src="/icons/typescript.svg" alt="TypeScript" class="w-4 h-4 mr-2" />
                TypeScript
              </span>
              <span class="flex items-center px-4 py-2 bg-white rounded-lg text-[0.75rem] font-medium text-gray-700">
                <img src="/icons/react.svg" alt="React" class="w-4 h-4 mr-2" />
                React
              </span>
              <span class="flex items-center px-4 py-2 bg-white rounded-lg text-[0.75rem] font-medium text-gray-700">
                <img src="/icons/next-js.svg" alt="Next.js" class="w-4 h-4 mr-2" />
                Next.js
              </span>
              <span class="flex items-center px-4 py-2 bg-white rounded-lg text-[0.75rem] font-medium text-gray-700">
                <img src="/icons/langChain.svg" alt="LangChain" class="w-4 h-4 mr-2" />
                LangChain
              </span>
              <span class="flex items-center px-4 py-2 bg-white rounded-lg text-[0.75rem] font-medium text-gray-700">
                <img src="/icons/python.svg" alt="Python" class="w-4 h-4 mr-2" />
                Python
              </span>
              <span class="flex items-center px-4 py-2 bg-white rounded-lg text-[0.75rem] font-medium text-gray-700">
                <img src="/icons/tailwind.svg" alt="Tailwind CSS" class="w-4 h-4 mr-2" />
                Tailwind CSS
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- 右侧：个人简介卡片（占宽20%）-->
      <div class="lg:col-span-1 home-profile-col">
        <div class="bg-white rounded-xl shadow-sm p-6 h-full flex flex-col home-profile-card">
          <!-- 第一块：头像和个人信息 -->
          <div class="flex flex-col items-center mb-6">
            <div class="w-[5rem] h-[5rem] rounded-full overflow-hidden flex-shrink-0 mb-3">
              <img 
                :src="siteSettings.admin_avatar || '/images/avatar.png'" 
                :alt="siteSettings.author_name || 'Lin'" 
                class="w-full h-full object-cover" />
            </div>
            <h3 class="font-bold text-xl text-gray-900 mb-1">{{ siteSettings.author_name || 'Lin' }}</h3>
            <p class="text-sm text-gray-600">{{ siteSettings.description || '全栈开发 & AI 应用探索。' }}</p>
          </div>

          <!-- 第二块：个人信息 -->
          <div class="w-full space-y-3 mb-6">
            <div class="flex items-center text-sm text-gray-600">
              <img src="/icons/position-black.svg" alt="地址" class="w-4 h-4 mr-2" />
              {{ siteSettings.location || '中国 · 深圳' }}
            </div>
            <div class="flex items-center text-sm text-gray-600">
              <img src="/icons/email-black.svg" alt="邮箱" class="w-4 h-4 mr-2" />
              {{ siteSettings.email || 'lin@example.com' }}
            </div>
            <div class="flex items-center text-sm text-gray-600">
              <img src="/icons/github-black.svg" alt="GitHub" class="w-4 h-4 mr-2" />
              {{ siteSettings.github_url ? siteSettings.github_url.replace('https://', '').replace('http://', '') : 'github.com/linxxxx' }}
            </div>
            <div class="flex items-center text-sm text-gray-600">
              <img src="/icons/project-black.svg" alt="开发经验" class="w-4 h-4 mr-2" />
              5 年开发经验            
            </div>
          </div>

          <!-- 第三块：下载简历 -->
          <button
            @click="openModal"
            class="w-full py-2.5 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-all flex items-center justify-center mt-auto">
            <img src="/icons/download.svg" alt="下载" class="w-4 h-4 mr-2" />
            下载简历(PDF)
          </button>
        </div>
      </div>
    </div>

    <!-- 下半部分：内容区 -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 home-content-grid" style="margin-left: -1.75rem">
      <!-- 左侧：精选项目、最新文章等模块（占宽约75%）-->
      <div class="lg:col-span-9 bg-white p-8 home-main-col">
        <!-- 精选项目 -->
        <div class="mb-8">
          <div class="flex justify-between items-center mb-4 home-section-header">
            <h2 class="text-[1.3rem] font-bold text-gray-900">精选项目</h2>
            <a href="#" @click.prevent="router.push('/projects')" class="text-gray-600 hover:text-gray-700 text-sm font-medium flex items-center gap-1">查看更多
              <img src="/icons/next-grey.svg" alt="arrow" class="w-4 h-4" /></a>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 home-project-grid">
            <div v-if="loadingProjects" v-for="n in 3" :key="'ps'+n"
              class="bg-white rounded-xl shadow-sm flex flex-col h-[340px] animate-pulse">
              <div class="flex-[55] bg-gray-200 rounded-t-xl"></div>
              <div class="flex-[45] p-4 space-y-3">
                <div class="h-5 bg-gray-200 rounded w-3/4"></div>
                <div class="h-4 bg-gray-200 rounded w-full"></div>
                <div class="flex gap-2">
                  <div class="h-5 w-12 bg-gray-200 rounded"></div>
                  <div class="h-5 w-12 bg-gray-200 rounded"></div>
                </div>
              </div>
            </div>
            <div v-else-if="featuredProjects.length === 0"
              class="col-span-3 text-center py-8 text-gray-400 text-sm">
              暂无项目
            </div>
            <div v-for="project in featuredProjects" :key="project.id"
              class="bg-white rounded-xl shadow-sm hover:shadow-md transition-all hover:-translate-y-1 flex flex-col h-[340px] cursor-pointer home-project-card"
              @click="goToProjectDetail(project.id)">
              <div class="flex-[55] bg-gray-100 rounded-t-xl overflow-hidden">
                <img :src="getCoverUrl(project.cover)" :alt="project.name" class="w-full h-full object-cover" />
              </div>
              <div class="flex-[45] p-4 overflow-hidden flex flex-col">
                <h3 class="font-semibold text-gray-900 mb-2 flex-shrink-0 line-clamp-1">{{ project.name }}</h3>
                <p class="text-sm text-gray-600 mb-3 flex-1 overflow-hidden line-clamp-2">{{ project.summary || project.description }}</p>
                <div class="flex flex-wrap gap-2 flex-shrink-0">
                  <span v-for="tag in getProjectTags(project).slice(0, 3)" :key="tag"
                    class="px-[0.8rem] py-[0.3rem] bg-gray-100 rounded-lg text-xs text-gray-700">{{ tag }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 最新文章 -->
        <div>
          <div class="flex justify-between items-center mb-4 home-section-header">
            <h2 class="text-[1.3rem] font-bold text-gray-900 pl-[0.7rem]">
              最新文章            </h2>
            <a href="#" @click.prevent="router.push('/articles')" class="text-gray-600 hover:text-gray-700 text-sm font-medium flex items-center gap-1">查看更多
              <img src="/icons/next-grey.svg" alt="arrow" class="w-4 h-4" /></a>
          </div>
          <div class="space-y-4">
            <div v-if="loadingArticles" v-for="n in 2" :key="'as'+n"
              class="bg-white rounded-xl shadow-sm px-[0.7rem] py-[0.7rem] flex gap-4 h-[160px] animate-pulse">
              <div class="w-60 h-full flex-shrink-0 bg-gray-200 rounded-lg"></div>
              <div class="flex-1 flex flex-col justify-between py-[0.7rem] space-y-3">
                <div class="h-5 bg-gray-200 rounded w-3/4"></div>
                <div class="h-4 bg-gray-200 rounded w-full"></div>
                <div class="flex gap-2">
                  <div class="h-3 w-16 bg-gray-200 rounded"></div>
                  <div class="h-3 w-12 bg-gray-200 rounded"></div>
                </div>
              </div>
            </div>
            <div v-else-if="latestArticles.length === 0"
              class="text-center py-8 text-gray-400 text-sm">
              暂无文章
            </div>
            <div v-for="article in latestArticles" :key="article.id"
              class="bg-white rounded-xl shadow-sm hover:shadow-md transition-all hover:-translate-y-1 px-[0.7rem] py-[0.7rem] flex gap-4 h-[160px] home-article-card cursor-pointer"
              @click="goToArticleDetail(article.id)">
              <div class="w-60 h-full flex-shrink-0">
                <img :src="getCoverUrl(article.cover)" :alt="article.title" class="w-full h-full object-cover rounded-lg" />
              </div>
              <div class="flex-1 flex flex-col justify-between py-[0.7rem]">
                <h3 class="font-semibold text-gray-900 line-clamp-1">{{ article.title }}</h3>
                <p class="text-sm text-gray-600 line-clamp-2">{{ article.summary }}</p>
                <div class="flex items-center text-xs text-gray-500">
                  <img src="/icons/time.svg" alt="date" class="w-3 h-3 mr-1" />
                  <span>{{ formatDate(article.created_at) }}</span>
                  <span class="mx-2">|</span>
                  <img src="/icons/folder.svg" alt="category" class="w-3 h-3 mr-1" />
                  <span>{{ article.category || '未分类' }}</span>
                  <span class="mx-2">|</span>
                  <img src="/icons/reading.svg" alt="views" class="w-3 h-3 mr-1" />
                  <span>{{ formatViews(article.view_count) }}</span>
                </div>
              </div>
              <div class="flex items-center justify-center mr-10">
                <img src="/icons/flag-grey.svg" alt="favorite" class="w-5 h-5 text-gray-400" />
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 右侧：技术栈、站点数据、最近动态等模块（占宽约25%）-->
      <div class="lg:col-span-3 home-sidebar-col">
        <!-- 技术栈 -->
        <div class="bg-white rounded-xl shadow-sm px-[2rem] py-6 mb-6 home-widget-card">
          <h3 class="font-semibold text-gray-900 mb-3">技术栈</h3>
          <div class="flex flex-wrap gap-2">
            <span v-for="stack in (techStacks.length ? techStacks.slice(0, 12) : [])" :key="stack.name"
              class="px-[1rem] py-[0.5rem] bg-gray-100 rounded-lg text-xs text-gray-700">{{ stack.name }}</span>
            <span v-if="techStacks.length === 0" class="text-gray-400 text-xs">暂无数据</span>
          </div>
        </div>

        <!-- 站点数据 -->
        <div class="bg-white rounded-xl shadow-sm px-[2rem] py-6 mb-6 home-widget-card">
          <h3 class="font-semibold text-gray-900 mb-4">站点数据</h3>
          <div class="flex justify-between">
            <div class="flex flex-col items-center">
              <div class="w-12 h-12 rounded-full bg-[#f6f7fb] flex items-center justify-center mb-3">
                <img src="/icons/article-blue.svg" alt="文章" class="w-6 h-6 text-blue-600" />
              </div>
              <div class="text-[0.8rem] text-gray-500 py-1">文章</div>
              <div class="text-2xl font-bold text-gray-900">{{ stats.articles_count || 0 }}</div>
            </div>
            <div class="flex flex-col items-center">
              <div class="w-12 h-12 rounded-full bg-[#f6f7fb] flex items-center justify-center mb-3">
                <img src="/icons/project-grey.svg" alt="项目" class="w-6 h-6 text-blue-600" />
              </div>
              <div class="text-[0.8rem] text-gray-500 py-1">项目</div>
              <div class="text-2xl font-bold text-gray-900">{{ stats.projects_count || 0 }}</div>
            </div>
            <div class="flex flex-col items-center">
              <div class="w-12 h-12 rounded-full bg-[#f6f7fb] flex items-center justify-center mb-3">
                <img src="/icons/eye.svg" alt="访问量" class="w-6 h-6 text-blue-600" />
              </div>
              <div class="text-[0.8rem] text-gray-500 py-1">访问量</div>
              <div class="text-2xl font-bold text-gray-900">{{ formatViews(stats.total_views || 0) }}</div>
            </div>
            <div class="flex flex-col items-center">
              <div class="w-12 h-12 rounded-full bg-[#f6f7fb] flex items-center justify-center mb-3">
                <img src="/icons/calendar.svg" alt="运行天数" class="w-6 h-6 text-blue-600" />
              </div>
              <div class="text-[0.8rem] text-gray-500 py-1">运行天数</div>
              <div class="text-2xl font-bold text-gray-900">{{ runningDays || 0 }}</div>
            </div>
          </div>
        </div>

        <!-- 最近动态 -->
        <div class="bg-white rounded-xl shadow-sm px-[2rem] py-6 home-widget-card">
          <h3 class="font-semibold text-gray-900 mb-3">最近动态</h3>
          <div class="space-y-3">
            <div v-for="item in recentActivity" :key="item.id" class="flex items-start gap-3 py-2">
              <div class="w-1.5 h-1.5 rounded-full bg-blue-600 mt-1.5 flex-shrink-0"></div>
              <div class="flex-1 text-[0.8rem]">
                <div class="flex justify-between">
                  <p class="text-gray-900">
                    {{ item.type === 'article' ? '发布了新文章' : '更新了项目' }}
                    <a href="#" class="text-blue-600 hover:underline" @click.prevent="item.type === 'article' ? goToArticleDetail(item.id) : goToProjectDetail(item.id)">{{ item.title }}</a>
                  </p>
                  <p class="text-gray-500">{{ getRelativeTime(item.created_at) }}</p>
                </div>
              </div>
            </div>
            <div v-if="!recentActivity.length" class="text-center py-4 text-gray-400 text-xs">暂无动态</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { usePdfModal } from '../composables/usePdfModal'
import { fetchSiteSettings, fetchSiteStatistics } from '../api/site'
import { fetchProjects } from '../api/projects'
import { fetchArticles } from '../api/articles'
import { fetchProfileSkills } from '../api/profile'

const router = useRouter()
const { openModal } = usePdfModal()

const siteSettings = ref({})
const stats = ref({ articles_count: 0, projects_count: 0, total_views: 0, days_running: 0 })
const featuredProjects = ref([])
const latestArticles = ref([])
const techStacks = ref([])
const loadingProjects = ref(false)
const loadingArticles = ref(false)

const runningDays = computed(() => {
  if (stats.value.days_running) return stats.value.days_running
  if (!siteSettings.value.site_start_date) return 0
  const startDate = new Date(siteSettings.value.site_start_date)
  const now = new Date()
  const diffTime = Math.abs(now - startDate)
  return Math.ceil(diffTime / (1000 * 60 * 60 * 24))
})

function formatDate(dateStr) {
  if (!dateStr) return ''
  const date = new Date(dateStr)
  const y = date.getFullYear()
  const m = String(date.getMonth() + 1).padStart(2, '0')
  const d = String(date.getDate()).padStart(2, '0')
  return `${y}-${m}-${d}`
}

function formatViews(count) {
  if (!count) return '0'
  if (count >= 1000) return (count / 1000).toFixed(count % 1000 === 0 ? 0 : 1).replace('.0', '') + 'k'
  return String(count)
}

function getCoverUrl(cover) {
  if (!cover) return '/images/default-cover.svg'
  return cover
}

function getProjectTags(project) {
  const tags = project.tags || []
  const techStack = project.tech_stack || []
  return [...new Set([...tags, ...techStack])]
}

function getRelativeTime(dateStr) {
  if (!dateStr) return ''
  const now = new Date()
  const date = new Date(dateStr)
  const diff = Math.floor((now - date) / (1000 * 60 * 60 * 24))
  if (diff === 0) return '今天'
  if (diff === 1) return '昨天'
  if (diff < 30) return `${diff} 天前`
  if (diff < 365) return `${Math.floor(diff / 30)} 个月前`
  return `${Math.floor(diff / 365)} 年前`
}

const goToProjectDetail = (id) => {
  if (id) router.push(`/project/${id}`)
}

const goToArticleDetail = (id) => {
  if (id) router.push(`/article/${id}`)
}

const recentActivity = computed(() => {
  const articles = latestArticles.value.slice(0, 3).map(a => ({
    id: a.id, title: a.title, type: 'article', created_at: a.created_at
  }))
  const projects = featuredProjects.value.slice(0, 2).map(p => ({
    id: p.id, title: p.name, type: 'project', created_at: p.created_at
  }))
  const all = [...articles, ...projects].sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
  return all.slice(0, 5)
})

const trackVisit = async () => {
  try {
    await fetch('http://localhost:8000/api/v1/statistics/site/visit', { method: 'POST' })
  } catch {}
}

onMounted(async () => {
  loadingArticles.value = true
  loadingProjects.value = true
  try {
    const [settings, statistics, projectsData, articlesData, skills] = await Promise.all([
      fetchSiteSettings(),
      fetchSiteStatistics(),
      fetchProjects({ page: 1, size: 3, sort_by: 'created_at' }),
      fetchArticles({ page: 1, size: 3, sort_by: 'created_at' }),
      fetchProfileSkills()
    ])
    if (settings) siteSettings.value = settings
    if (statistics) stats.value = statistics
    if (projectsData && projectsData.projects) featuredProjects.value = projectsData.projects
    if (articlesData && articlesData.articles) latestArticles.value = articlesData.articles
    if (skills) techStacks.value = skills
  } catch (e) {
    console.error('Failed to load homepage data:', e)
  } finally {
    loadingArticles.value = false
    loadingProjects.value = false
  }

  trackVisit()
})
</script>

<style scoped>
.home-page {
  background: #f8f9fd;
  padding: 1.75rem;
}

@media (max-width: 768px) {
  .home-profile-col {
    display: none;
  }

  .home-page {
    padding: 0.75rem 0.75rem 1rem;
  }

  .home-top-grid,
  .home-content-grid {
    margin-left: 0 !important;
  }

  .home-top-grid,
  .home-content-grid {
    gap: 0.75rem;
  }

  .home-hero-card {
    height: auto;
    min-height: 0;
    padding: 1rem;
    padding-bottom: 1rem;
    border-radius: 1rem;
  }

  .home-hero-card > .absolute {
    position: relative;
    right: auto;
    top: auto;
    width: 100%;
    height: auto;
    justify-content: center;
    margin-bottom: 0.75rem;
  }

  .home-hero-card > .absolute img {
    width: min(100%, 19rem);
    height: auto;
    margin-left: 0;
  }

  .home-hero-card .relative.z-10 {
    padding-top: 0;
  }

  .home-hero-card p.inline-flex,
  .home-hero-card h1,
  .home-hero-card h2,
  .home-hero-card .text-gray-600,
  .home-hero-card .flex.flex-wrap.gap-4,
  .home-hero-card .flex.flex-wrap.gap-3 {
    padding-left: 0;
  }

  .home-hero-card p.inline-flex {
    font-size: 0.75rem;
    margin-bottom: 0.75rem;
    padding: 0.35rem 0.75rem;
  }

  .home-hero-card h1,
  .home-hero-card h2 {
    font-size: 1.45rem;
    line-height: 1.22;
    margin-bottom: 0.5rem;
    letter-spacing: 0;
  }

  .home-hero-card .text-gray-600 {
    font-size: 0.8rem;
    line-height: 1.7;
    margin-bottom: 0.75rem;
  }

  .home-hero-card .flex.flex-wrap.gap-4 {
    gap: 0.85rem;
    margin-bottom: 0.85rem;
  }

  .home-hero-card .flex.flex-wrap.gap-4 button {
    width: 100%;
    padding: 0.8rem 1rem;
    font-size: 0.95rem;
    border-radius: 0.85rem;
  }

  .home-hero-card .flex.flex-wrap.gap-3 {
    display: none;
  }

  .home-hero-card .flex.flex-wrap.gap-3 span {
    padding: 0.4rem 0.7rem;
    border-radius: 0.75rem;
    font-size: 0.7rem;
  }

  .home-profile-card,
  .home-main-col,
  .home-widget-card {
    padding: 0.9rem;
    border-radius: 1rem;
  }

  .home-profile-card {
    align-items: center;
  }

  .home-profile-card .mb-6 {
    margin-bottom: 0.85rem;
  }

  .home-profile-card .w-\[5rem\] {
    width: 4.25rem;
    height: 4.25rem;
  }

  .home-profile-card h3 {
    font-size: 1.05rem;
  }

  .home-profile-card p,
  .home-profile-card .space-y-3 .flex {
    font-size: 0.82rem;
  }

  .home-profile-card button {
    padding: 0.75rem 0.9rem;
    border-radius: 0.8rem;
  }

  .home-main-col {
    padding-top: 1rem;
    padding-bottom: 1rem;
  }

  .home-section-header {
    margin-bottom: 0.75rem;
  }

  .home-section-header h2 {
    font-size: 1.05rem;
  }

  .home-section-header a {
    font-size: 0.75rem;
  }

  .home-project-grid {
    grid-template-columns: 1fr;
  }

  .home-project-card {
    height: auto;
    min-height: 0;
  }

  .home-project-card .flex-\[55\] {
    flex: 0 0 auto;
    aspect-ratio: 16 / 9;
  }

  .home-project-card .flex-\[45\] {
    padding: 0.9rem;
  }

  .home-project-card h3 {
    font-size: 0.95rem;
    line-height: 1.35;
  }

  .home-project-card p {
    font-size: 0.8rem;
    line-height: 1.6;
  }

  .home-project-card .flex.flex-wrap.gap-2 {
    gap: 0.35rem;
  }

  .home-article-card {
    height: auto;
    gap: 0.75rem;
    padding: 0.75rem;
    align-items: stretch;
  }

  .home-article-card .w-60 {
    width: 5.8rem;
    height: 5.8rem;
    flex-shrink: 0;
  }

  .home-article-card h3 {
    font-size: 0.92rem;
    line-height: 1.4;
  }

  .home-article-card p {
    font-size: 0.76rem;
    line-height: 1.55;
  }

  .home-article-card .mr-10 {
    display: none;
  }

  .home-article-card .flex.items-center.text-xs,
  .home-article-card .text-xs.text-gray-500 {
    font-size: 0.68rem;
  }

  .home-widget-card {
    margin-bottom: 0.75rem;
  }

  .home-widget-card .flex.justify-between {
    gap: 0.75rem;
  }

  .home-widget-card h3 {
    font-size: 0.95rem;
  }

  .home-widget-card .flex.flex-wrap.gap-2 span {
    padding: 0.38rem 0.7rem;
    border-radius: 0.7rem;
  }

  .home-widget-card .flex.justify-between > div {
    flex: 1;
  }

  .home-widget-card .flex.justify-between {
    flex-wrap: wrap;
    gap: 0.6rem 0;
  }

  .home-widget-card .flex.justify-between .text-2xl {
    font-size: 1.35rem;
  }

  .home-widget-card .space-y-3 .flex.justify-between {
    align-items: flex-start;
  }

  .home-widget-card .space-y-3 .flex.justify-between p:last-child {
    margin-left: 0.5rem;
    flex-shrink: 0;
  }
}
</style>