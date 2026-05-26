<template>
  <div class="page-container p-3 lg:p-[1.75rem] bg-[#fefefe]">
    <div class="min-h-screen">
      <div class="">
        <div class="flex flex-col lg:flex-row gap-4 lg:gap-8">

          <!-- 中间主内容区 -->
          <div class="lg:flex-1">
            <!-- 顶部区域 -->
            <div class="mb-4 lg:mb-8">
              <h1 class="text-xl lg:text-3xl font-bold text-gray-900">项目</h1>
              <p class="text-gray-600 mt-2 text-xs lg:text-sm">用代码构建想法，让创意落地成为有价值的产品。</p>

              <!-- 分类标签 -->
              <div class="flex flex-wrap gap-1.5 lg:gap-2 mt-3 lg:mt-4">
                <button
                  v-for="cat in categories"
                  :key="cat.id || 'all'"
                  @click="onCategoryClick(cat.id ? cat.name : '')"
                  :class="[
                    'px-3 py-1 rounded-full text-xs lg:text-sm font-medium transition-colors',
                    activeCategory === (cat.id ? cat.name : '')
                      ? 'bg-blue-50 text-blue-600'
                      : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                  ]"
                >
                  {{ cat.name }}
                </button>
              </div>
            </div>

            <!-- 项目列表 -->
            <div class="space-y-4 lg:space-y-5">
              <!-- 加载状态：骨架屏 -->
              <template v-if="loading">
                <div v-for="n in 3" :key="n"
                  class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-3 lg:p-6 flex flex-col lg:flex-row gap-3 lg:gap-4 min-h-[180px] animate-pulse">
                  <div class="w-full h-32 lg:w-60 lg:h-full flex-shrink-0 bg-gray-200 rounded-lg"></div>
                  <div class="flex-1 space-y-3 py-1">
                    <div class="h-5 bg-gray-200 rounded w-3/4"></div>
                    <div class="h-4 bg-gray-200 rounded w-full"></div>
                    <div class="h-4 bg-gray-200 rounded w-2/3"></div>
                    <div class="flex gap-2">
                      <div class="h-5 w-12 bg-gray-200 rounded"></div>
                      <div class="h-5 w-12 bg-gray-200 rounded"></div>
                    </div>
                    <div class="flex gap-4">
                      <div class="h-4 w-20 bg-gray-200 rounded"></div>
                      <div class="h-4 w-16 bg-gray-200 rounded"></div>
                    </div>
                  </div>
                </div>
              </template>

              <!-- 错误状态 -->
              <div v-else-if="error" class="text-center py-12">
                <p class="text-gray-500 mb-4">{{ error }}</p>
                <button @click="loadProjects" class="px-4 py-2 bg-blue-50 text-blue-600 rounded-lg text-sm hover:bg-blue-100">重新加载</button>
              </div>

              <!-- 空数据 -->
              <div v-else-if="projects.length === 0" class="text-center py-12">
                <p class="text-gray-500">暂无项目</p>
              </div>

              <!-- 项目卡片 -->
              <div v-else v-for="project in projects" :key="project.id"
                class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-all hover:-translate-y-1 p-3 lg:p-6 flex flex-col lg:flex-row gap-3 lg:gap-4 min-h-[180px] cursor-pointer"
                @click="goToProjectDetail(project.id)">
                <div class="w-full h-32 lg:w-60 lg:h-full flex-shrink-0 project-cover-wrapper">
                  <img :src="getCoverUrl(project.cover)" :alt="project.name" class="w-full h-full object-cover rounded-lg">
                </div>
                <div class="flex-1 flex flex-col justify-between py-1">
                  <div>
                    <h2 class="text-base lg:text-[1.3rem] font-bold text-gray-900 line-clamp-2">{{ project.name }}</h2>
                    <p class="text-gray-500 text-xs lg:text-sm mt-2 lg:mt-3 line-clamp-2">{{ project.summary }}</p>
                    <div v-if="displayTags(project).length > 0" class="flex flex-wrap gap-1.5 lg:gap-2 mt-2 lg:mt-3">
                      <span v-for="tag in displayTags(project)" :key="tag"
                        class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-[0.75rem] rounded-lg">{{ tag }}</span>
                    </div>
                  </div>
                  <div class="flex items-center text-xs text-gray-500 mt-2">
                    <img src="/icons/calendar.svg" alt="日期" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                    <span>{{ formatDate(project.created_at) }}</span>
                    <span class="w-1 h-1 bg-gray-300 rounded-full mx-1.5 lg:mx-2"></span>
                    <img src="/icons/eye.svg" alt="阅读" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                    <span>{{ formatViews(project.view_count) }}</span>
                    <span class="w-1 h-1 bg-gray-300 rounded-full mx-1.5 lg:mx-2"></span>
                    <img src="/icons/like-grey.svg" alt="点赞" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                    <span>{{ formatViews(project.like_count) }}</span>
                  </div>
                </div>
                <div class="flex items-center">
                  <img src="/icons/flag-grey.svg" alt="收藏" class="w-4 h-4 lg:w-5 lg:h-5 text-gray-300 hover:text-yellow-500 cursor-pointer">
                </div>
              </div>
            </div>

            <!-- 分页控件 -->
            <div class="mt-6 lg:mt-8 flex justify-center">
              <nav class="flex items-center space-x-1">
                <button @click="onPageChange(currentPage - 1)" :disabled="currentPage <= 1"
                  class="px-2 py-1 rounded-md border border-gray-300 text-gray-600 hover:bg-gray-50 text-xs lg:text-sm disabled:opacity-40 disabled:cursor-not-allowed">
                  上一页
                </button>
                <template v-for="page in totalPages" :key="page">
                  <button @click="onPageChange(page)"
                    :class="[
                      'px-2 py-1 rounded-md text-xs lg:text-sm',
                      page === currentPage
                        ? 'bg-blue-50 text-blue-600 border border-blue-200'
                        : 'border border-gray-300 text-gray-600 hover:bg-gray-50'
                    ]">
                    {{ page }}
                  </button>
                </template>
                <button @click="onPageChange(currentPage + 1)" :disabled="currentPage >= totalPages"
                  class="px-2 py-1 rounded-md border border-gray-300 text-gray-600 hover:bg-gray-50 text-xs lg:text-sm disabled:opacity-40 disabled:cursor-not-allowed">
                  下一页
                </button>
              </nav>
            </div>

            <!-- 底部版权信息 -->
            <div class="mt-8 lg:mt-12 text-center text-xs lg:text-sm text-gray-500">
              <p>© 2024 Lin's Tech Blog</p>
              <p class="mt-1 lg:mt-2">浙ICP备024000000。</p>
            </div>
          </div>

          <!-- 右侧边栏 - 移动端隐藏 -->
          <div class="hidden lg:block lg:w-1/5">
            <!-- 技术栈 -->
            <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6 mb-5">
              <h3 class="text-base font-semibold text-gray-900 mb-4">技术栈</h3>
              <div class="flex flex-wrap gap-2 tech-stack-container">
                <button v-for="stack in techStats" :key="stack.name"
                  @click="onTechClick(stack.name)"
                  :class="[
                    'px-3 py-1.5 rounded-lg text-xs transition-colors',
                    selectedTech === stack.name
                      ? 'bg-blue-100 text-blue-600 font-medium'
                      : 'bg-gray-50 text-gray-600 hover:bg-gray-200'
                  ]">{{ stack.name }}</button>
              </div>
            </div>

            <!-- 项目分类 -->
            <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6 mb-5">
              <h3 class="text-base font-semibold text-gray-900 mb-4">项目分类</h3>
              <ul class="space-y-3">
                <li v-for="cat in categoryStats" :key="cat.name"
                  class="flex items-center cursor-pointer hover:text-blue-600 transition-colors"
                  @click="onCategoryClick(cat.name)">
                  <span :class="[
                    'w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0 mr-3',
                    activeCategory === cat.name ? 'bg-blue-500' : 'bg-gray-100'
                  ]">
                    <span :class="[
                      'w-2 h-2 rounded-full',
                      activeCategory === cat.name ? 'bg-white' : 'bg-gray-400'
                    ]"></span>
                  </span>
                  <span :class="[
                    'flex-1 text-sm',
                    activeCategory === cat.name ? 'text-blue-600 font-medium' : 'text-gray-600'
                  ]">{{ cat.name }}</span>
                  <span class="text-gray-400 text-sm">{{ cat.count }}</span>
                </li>
              </ul>
            </div>

            <!-- 热门项目 -->
            <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6 mb-5">
              <h3 class="text-base font-semibold text-gray-900 mb-4">热门项目</h3>
              <ul class="space-y-3">
                <li v-for="(project, index) in hotProjects" :key="project.id" class="flex items-start cursor-pointer hover:text-blue-600 transition-colors" @click="goToProjectDetail(project.id)">
                  <span :class="[
                    'w-2 h-2 rounded-full mt-2 mr-3 flex-shrink-0',
                    index < 3 ? 'bg-blue-500' : 'bg-gray-300'
                  ]"></span>
                  <div class="flex-1 min-w-0">
                    <a class="text-gray-700 hover:text-blue-600 text-sm line-clamp-1">{{ project.name }}</a>
                    <p class="text-gray-400 text-xs mt-1">阅读 {{ formatViews(project.view_count) }}</p>
                  </div>
                </li>
              </ul>
            </div>

            <!-- 我在做什么 -->
            <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-4">我在做什么</h3>
              <p class="text-gray-500 text-sm leading-relaxed mb-6">
                探索 Agent、LLM 与前端工程化的边界，<br>
                构建更智能、更高效的开发体验。
              </p>
              <div class="relative">
                <img src="/images/hero-3d.png" alt="AI 3D Illustration" class="w-full h-auto object-contain">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import {
  fetchProjects,
  fetchProjectCategories,
  fetchProjectCategoryStats,
  fetchProjectTechStackStats,
  fetchHotProjects
} from '../api/projects'

const router = useRouter()

const projects = ref([])
const total = ref(0)
const currentPage = ref(1)
const pageSize = ref(8)
const categories = ref([])
const activeCategory = ref('')
const loading = ref(false)
const error = ref(null)

const totalPages = ref(0)

const categoryStats = ref([])
const techStats = ref([])
const selectedTech = ref('')
const hotProjects = ref([])

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

const API_BASE = 'http://localhost:8000'

function getCoverUrl(cover) {
  if (!cover) return '/images/default-cover.svg'
  return cover
}

function displayTags(project) {
  const tags = project.tags || []
  const techStack = project.tech_stack || []
  const combined = [...new Set([...tags, ...techStack])]
  return combined
}

function goToProjectDetail(id) {
  router.push(`/project/${id}`)
}

async function loadProjects() {
  loading.value = true
  error.value = null
  try {
    const params = {
      page: currentPage.value,
      size: pageSize.value,
      sort_by: 'created_at'
    }
    if (activeCategory.value) {
      const matched = categories.value.find(c => c.name === activeCategory.value)
      if (matched && matched.id) {
        params.category_id = matched.id
      }
    }
    if (selectedTech.value) {
      params.tech_stack = selectedTech.value
    }
    const data = await fetchProjects(params)
    if (data) {
      projects.value = data.projects || []
      total.value = data.total || 0
      totalPages.value = Math.ceil(total.value / pageSize.value) || 1
    } else {
      projects.value = []
      total.value = 0
      totalPages.value = 1
    }
  } catch (e) {
    error.value = '加载项目列表失败'
    projects.value = []
  } finally {
    loading.value = false
  }
}

async function loadCategories() {
  try {
    const data = await fetchProjectCategories()
    if (data && Array.isArray(data)) {
      const activeCategories = data.filter(c => c.is_active !== false)
      categories.value = [{ name: '全部', id: '' }, ...activeCategories]
    }
  } catch (e) {
    categories.value = [{ name: '全部', id: '' }]
  }
}

async function loadSidebarData() {
  const [catStats, techs, hot] = await Promise.all([
    fetchProjectCategoryStats(),
    fetchProjectTechStackStats(),
    fetchHotProjects(5)
  ])
  if (catStats) categoryStats.value = catStats
  if (techs) techStats.value = techs
  if (hot) hotProjects.value = hot
}

function onCategoryClick(categoryName) {
  if (activeCategory.value === categoryName) return
  activeCategory.value = categoryName
  currentPage.value = 1
}

function onTechClick(techName) {
  selectedTech.value = selectedTech.value === techName ? '' : techName
  currentPage.value = 1
}

function onPageChange(page) {
  if (page < 1 || page > totalPages.value) return
  currentPage.value = page
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

onMounted(() => {
  loadCategories()
  loadProjects()
  loadSidebarData()
})

watch([currentPage, activeCategory, selectedTech], () => {
  loadProjects()
})
</script>

<style scoped>
.page-container {
  background: #ffffff;
  padding: 1.75rem;
}

.project-cover-wrapper {
  aspect-ratio: 16 / 10;
  overflow: hidden;
}

.project-cover-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.project-cover-wrapper:hover img {
  transform: scale(1.05);
}

.tech-stack-container {
  overflow: hidden;
  max-height: 200px;
}
</style>