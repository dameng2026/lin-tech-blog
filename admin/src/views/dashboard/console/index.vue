<template>
  <div v-loading="loading" class="console-dashboard">
    <CardList
      :articles-count="summary.articles_count"
      :projects-count="summary.projects_count"
      :users-count="summary.users_count"
      :total-views="summary.total_views"
      :days-running="summary.days_running"
    />

    <ElRow :gutter="20" class="mt-4">
      <ElCol :sm="24" :md="12" :lg="12">
        <ArtLineChartCard
          title="近七天访问趋势"
          :chart-data="summary.visit_trend"
          :show-area-color="true"
        />
      </ElCol>
      <ElCol :sm="24" :md="12" :lg="12">
        <ArtDataListCard
          title="最新文章"
          subtitle="最近发布的5篇文章"
          :list="articleList"
          :show-more-button="summary.latest_articles.length > 0"
          @more="goTo('/content/articles')"
        />
      </ElCol>
    </ElRow>

    <ElRow :gutter="20" class="mt-4">
      <ElCol :sm="24" :md="12" :lg="12">
        <ArtDataListCard
          title="最新项目"
          subtitle="最近添加的5个项目"
          :list="projectList"
          :show-more-button="summary.latest_projects.length > 0"
          @more="goTo('/content/projects')"
        />
      </ElCol>
      <ElCol :sm="24" :md="12" :lg="12">
        <TodoList
          :friend-links="summary.pending.friend_links"
          :guestbook-messages="summary.pending.guestbook_messages"
          :unapproved-comments="summary.pending.unapproved_comments"
          :resume-key-requests="summary.pending.resume_key_requests"
        />
      </ElCol>
    </ElRow>

    <ElRow :gutter="20" class="mt-4">
      <ElCol :span="24">
        <div class="art-card p-5 rounded-xl shadow-sm">
          <p class="text-lg font-medium mb-4">快捷操作</p>
          <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-7 gap-4">
            <button
              v-for="action in quickActions"
              :key="action.path"
              class="flex flex-col items-center gap-2 p-4 border border-[var(--art-card-border)] rounded-lg hover:bg-[var(--art-hover-color)] hover:border-[var(--theme-color)]/30 transition-all duration-200"
              @click="goTo(action.path)"
            >
              <ArtSvgIcon :icon="action.icon" class="text-2xl text-theme" />
              <span class="text-sm text-g-600">{{ action.label }}</span>
            </button>
          </div>
        </div>
      </ElCol>
    </ElRow>
  </div>
</template>

<script setup lang="ts">
  import { ref, computed, onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  import { ElMessage } from 'element-plus'
  import CardList from './modules/card-list.vue'
  import TodoList from './modules/todo-list.vue'
  import { fetchDashboardSummary } from '@/api/dashboard'
  import type { DashboardSummary, LatestArticle, LatestProject } from '@/api/dashboard'

  defineOptions({ name: 'Console' })

  const router = useRouter()
  const loading = ref(false)

  const summary = ref<DashboardSummary>({
    articles_count: 0,
    projects_count: 0,
    users_count: 0,
    total_views: 0,
    total_likes: 0,
    total_comments: 0,
    total_collects: 0,
    days_running: 0,
    visit_trend: [],
    latest_articles: [],
    latest_projects: [],
    pending: {
      friend_links: 0,
      guestbook_messages: 0,
      unapproved_comments: 0,
      resume_key_requests: 0
    }
  })

  const articleList = computed(() => {
    return summary.value.latest_articles.map((a: LatestArticle) => ({
      title: a.title,
      status: '',
      time: a.created_at,
      class: 'bg-theme/10 text-theme',
      icon: 'ri:article-line'
    }))
  })

  const projectList = computed(() => {
    return summary.value.latest_projects.map((p: LatestProject) => ({
      title: p.name,
      status: '',
      time: p.created_at,
      class: 'bg-success/10 text-success',
      icon: 'ri:code-box-line'
    }))
  })

  const quickActions = [
    { label: '撰写文章', icon: 'ri:edit-2-line', path: '/content/publish' },
    { label: '添加项目', icon: 'ri:add-box-line', path: '/projects/create' },
    { label: '管理友链', icon: 'ri:link-m', path: '/links/friend-links' },
    { label: '密钥管理', icon: 'ri:key-2-line', path: '/profile/pdf-key' },
    { label: '评论管理', icon: 'ri:chat-3-line', path: '/community/comments' },
    { label: '留言管理', icon: 'ri:message-3-line', path: '/community/messages' },
    { label: '站点设置', icon: 'ri:settings-4-line', path: '/settings/site' }
  ]

  function goTo(path: string) {
    router.push(path)
  }

  async function loadDashboardData() {
    loading.value = true
    try {
      const response = await fetchDashboardSummary()
      summary.value = response
    } catch (error) {
      ElMessage.error('加载仪表盘数据失败')
    } finally {
      loading.value = false
    }
  }

  onMounted(() => {
    loadDashboardData()
  })
</script>

<style lang="scss" scoped>
.console-dashboard {
  :deep(.art-card) {
    .text-\[26px\] {
      font-weight: 700;
      color: var(--theme-color);
    }
  }

  .art-card,
  [class*="rounded-xl"][class*="shadow-sm"] {
    transition: all 0.2s ease;
  }
  .art-card:hover,
  [class*="rounded-xl"][class*="shadow-sm"]:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  }
}
</style>
