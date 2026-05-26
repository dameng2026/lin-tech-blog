<template>
  <div class="article-archive-page">
    <art-page-content>
      <template #header>
        <art-breadcrumb :items="breadcrumbItems" />
        <art-header-bar title="文章归档" />
      </template>

      <template #body>
        <el-card class="rounded-xl shadow-sm border border-[var(--art-card-border)]">
          <el-timeline>
            <el-timeline-item
              v-for="group in archiveData"
              :key="`${group.year}-${group.month}`"
              :timestamp="`${group.year}年${group.month}月`"
              placement="top"
            >
              <div class="mb-2 text-lg font-bold">共 {{ group.article_count }} 篇文章</div>
              <el-card shadow="hover">
                <div v-for="article in group.articles" :key="article.id" class="py-2 border-b last:border-b-0">
                  <a :href="`/article/${article.id}`" class="text-blue-500 hover:underline">
                    {{ article.title }}
                  </a>
                  <span class="ml-4 text-gray-400 text-sm">{{ article.created_at }}</span>
                </div>
              </el-card>
            </el-timeline-item>
          </el-timeline>
        </el-card>
      </template>
    </art-page-content>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElCard, ElTimeline, ElTimelineItem } from 'element-plus'
import ArtPageContent from '@/components/core/layouts/art-page-content/index.vue'
import ArtBreadcrumb from '@/components/core/layouts/art-breadcrumb/index.vue'
import ArtHeaderBar from '@/components/core/layouts/art-header-bar/index.vue'
import { fetchArticleArchive } from '@/api/statistics'

const breadcrumbItems = [
  { label: '首页', path: '/' },
  { label: '数据统计', path: '/statistics/dashboard' },
  { label: '文章归档', path: '/statistics/archive' }
]

const archiveData = ref<any[]>([])

async function loadData() {
  try {
    const response = await fetchArticleArchive()
    archiveData.value = response.data
  } catch (error) {
    console.error('加载归档数据失败:', error)
  }
}

onMounted(() => {
  loadData()
})
</script>

<style scoped>
.article-archive-page {
  min-height: 100%;
}

.article-archive-page .el-card {
  transition: all 0.2s ease;
}
.article-archive-page .el-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
</style>
