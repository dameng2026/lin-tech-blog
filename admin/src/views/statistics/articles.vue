<template>
  <div class="article-stats-page">
    <art-page-content>
      <template #header>
        <art-breadcrumb :items="breadcrumbItems" />
        <art-header-bar title="文章统计" />
      </template>

      <template #body>
        <el-card title="热门文章" class="mb-4 rounded-xl shadow-sm border border-[var(--art-card-border)]">
          <el-table :data="hotArticles" border>
            <el-table-column prop="title" label="文章标题" min-width="300" />
            <el-table-column prop="view_count" label="浏览量" width="120" sortable>
              <template #default="{ row }">
                <span class="text-blue-500 font-bold">{{ row.view_count }}</span>
              </template>
            </el-table-column>
            <el-table-column prop="like_count" label="点赞数" width="120" sortable>
              <template #default="{ row }">
                <span class="text-red-500 font-bold">{{ row.like_count }}</span>
              </template>
            </el-table-column>
            <el-table-column prop="category" label="分类" width="120" />
            <el-table-column prop="created_at" label="发布时间" width="150" />
          </el-table>
        </el-card>

        <el-card title="分类统计" class="rounded-xl shadow-sm border border-[var(--art-card-border)]">
          <div class="grid grid-cols-4 gap-4">
            <div v-for="cat in categoryStats" :key="cat.name" class="p-4 border rounded-lg">
              <div class="text-gray-500">{{ cat.name }}</div>
              <div class="text-2xl font-bold text-blue-500">{{ cat.count }}</div>
            </div>
          </div>
        </el-card>
      </template>
    </art-page-content>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElCard, ElTable, ElTableColumn } from 'element-plus'
import ArtPageContent from '@/components/core/layouts/art-page-content/index.vue'
import ArtBreadcrumb from '@/components/core/layouts/art-breadcrumb/index.vue'
import ArtHeaderBar from '@/components/core/layouts/art-header-bar/index.vue'
import { fetchHotArticles } from '@/api/statistics'

const breadcrumbItems = [
  { label: '首页', path: '/' },
  { label: '数据统计', path: '/statistics/dashboard' },
  { label: '文章统计', path: '/statistics/articles' }
]

const hotArticles = ref<any[]>([])
const categoryStats = ref<any[]>([])

async function loadData() {
  try {
    const response = await fetchHotArticles({ limit: 20 })
    hotArticles.value = response.data
  } catch (error) {
    console.error('加载数据失败:', error)
  }
}

onMounted(() => {
  loadData()
})
</script>

<style scoped>
.article-stats-page {
  min-height: 100%;
}

.article-stats-page .el-card {
  transition: all 0.2s ease;
}
.article-stats-page .el-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
</style>
