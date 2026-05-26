<template>
  <div class="statistics-dashboard">
    <art-page-content>
      <template #header>
        <art-breadcrumb :items="breadcrumbItems" />
        <art-header-bar title="数据统计" :action="headerAction" />
      </template>

      <template #body>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
          <art-stats-card
            title="文章总数"
            :value="stats.articles_count"
            icon="ri:book-open-line"
            color="blue"
          />
          <art-stats-card
            title="项目总数"
            :value="stats.projects_count"
            icon="ri:folder-open-line"
            color="green"
          />
          <art-stats-card
            title="总访问量"
            :value="formatNumber(stats.total_views)"
            icon="ri:eye-line"
            color="purple"
          />
          <art-stats-card
            title="运行天数"
            :value="stats.days_running"
            icon="ri:calendar-line"
            color="orange"
          />
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <el-card title="互动数据" class="h-full rounded-xl shadow-sm border border-[var(--art-card-border)]">
            <div class="space-y-4">
              <div class="flex justify-between items-center">
                <span class="text-gray-600">总点赞数</span>
                <span class="text-2xl font-bold text-blue-500">{{ stats.total_likes }}</span>
              </div>
              <div class="flex justify-between items-center">
                <span class="text-gray-600">总评论数</span>
                <span class="text-2xl font-bold text-green-500">{{ stats.total_comments }}</span>
              </div>
              <div class="flex justify-between items-center">
                <span class="text-gray-600">总收藏数</span>
                <span class="text-2xl font-bold text-purple-500">{{ stats.total_collects }}</span>
              </div>
            </div>
          </el-card>

          <el-card title="GitHub数据" class="h-full">
            <div class="space-y-4">
              <div class="flex justify-between items-center">
                <span class="text-gray-600">GitHub Stars</span>
                <span class="text-2xl font-bold text-yellow-500">{{ stats.github_stars }}</span>
              </div>
              <div class="flex justify-between items-center">
                <span class="text-gray-600">GitHub Followers</span>
                <span class="text-2xl font-bold text-blue-500">{{ stats.github_followers }}</span>
              </div>
              <el-button type="primary" size="small" @click="handleSyncGithub">
                同步GitHub数据
              </el-button>
            </div>
          </el-card>
        </div>

        <div class="mt-6">
          <el-card title="热门文章">
            <el-table :data="hotArticles" border>
              <el-table-column prop="title" label="文章标题" min-width="300" />
              <el-table-column prop="view_count" label="浏览量" width="100" />
              <el-table-column prop="like_count" label="点赞数" width="100" />
              <el-table-column prop="category" label="分类" width="120" />
              <el-table-column prop="created_at" label="发布时间" width="150" />
            </el-table>
          </el-card>
        </div>

        <div class="mt-6">
          <el-card title="热门项目" class="rounded-xl shadow-sm border border-[var(--art-card-border)]">
            <el-table :data="hotProjects" border>
              <el-table-column prop="name" label="项目名称" min-width="200" />
              <el-table-column prop="view_count" label="浏览量" width="100" />
              <el-table-column prop="status" label="状态" width="100">
                <template #default="{ row }">
                  <el-tag :type="getStatusType(row.status)">{{ getStatusText(row.status) }}</el-tag>
                </template>
              </el-table-column>
              <el-table-column prop="created_at" label="创建时间" width="150" />
            </el-table>
          </el-card>
        </div>
      </template>
    </art-page-content>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { ElCard, ElTable, ElTableColumn, ElTag, ElButton } from 'element-plus'
import ArtPageContent from '@/components/core/layouts/art-page-content/index.vue'
import ArtBreadcrumb from '@/components/core/layouts/art-breadcrumb/index.vue'
import ArtHeaderBar from '@/components/core/layouts/art-header-bar/index.vue'
import ArtStatsCard from '@/components/core/cards/art-stats-card/index.vue'
import { fetchSiteStats, updateSiteStats, syncGithubStats, fetchHotArticles, fetchHotProjects } from '@/api/statistics'

const stats = ref({
  articles_count: 0,
  projects_count: 0,
  total_views: 0,
  total_likes: 0,
  total_comments: 0,
  total_collects: 0,
  github_stars: 0,
  github_followers: 0,
  site_start_date: '',
  days_running: 0
})

const hotArticles = ref<any[]>([])
const hotProjects = ref<any[]>([])

const breadcrumbItems = computed(() => [
  { label: '首页', path: '/' },
  { label: '数据统计', path: '/statistics/dashboard' }
])

const headerAction = computed(() => ({
  type: 'button',
  text: '刷新数据',
  icon: 'ri:refresh-line',
  click: () => handleRefresh
}))

function formatNumber(num: number): string {
  if (num >= 10000) {
    return (num / 10000).toFixed(1) + '万'
  }
  return num.toString()
}

function getStatusType(status: string) {
  const types: Record<string, string> = {
    active: 'warning',
    completed: 'success',
    maintenance: 'info'
  }
  return types[status] || 'default'
}

function getStatusText(status: string) {
  const texts: Record<string, string> = {
    active: '开发中',
    completed: '已完成',
    maintenance: '维护中'
  }
  return texts[status] || status
}

async function loadStats() {
  try {
    const response = await fetchSiteStats()
    stats.value = response.data
  } catch (error) {
    console.error('加载统计数据失败:', error)
  }
}

async function loadHotArticles() {
  try {
    const response = await fetchHotArticles({ limit: 5 })
    hotArticles.value = response.data
  } catch (error) {
    console.error('加载热门文章失败:', error)
  }
}

async function loadHotProjects() {
  try {
    const response = await fetchHotProjects({ limit: 5 })
    hotProjects.value = response.data
  } catch (error) {
    console.error('加载热门项目失败:', error)
  }
}

async function handleRefresh() {
  try {
    await updateSiteStats()
    await loadStats()
    await loadHotArticles()
    await loadHotProjects()
    ElMessage.success('数据刷新成功')
  } catch (error) {
    ElMessage.error('刷新失败')
  }
}

async function handleSyncGithub() {
  try {
    await syncGithubStats()
    await loadStats()
    ElMessage.success('GitHub数据同步成功')
  } catch (error) {
    ElMessage.error('同步失败')
  }
}

onMounted(() => {
  loadStats()
  loadHotArticles()
  loadHotProjects()
})
</script>

<style scoped>
.statistics-dashboard {
  min-height: 100%;
}

.statistics-dashboard :deep(.art-stats-card) .text-2xl {
  font-weight: 700;
  color: var(--theme-color);
}

.statistics-dashboard .space-y-4 .text-2xl {
  color: var(--theme-color);
}
</style>