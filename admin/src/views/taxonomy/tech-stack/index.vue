<template>
  <div class="tech-stack-page art-full-height">
    <ArtBreadcrumb :items="breadcrumbItems" />
    <ElCard class="mt-4 art-table-card rounded-lg shadow-sm border border-[var(--art-card-border)]">
      <ArtTableHeader v-model:columns="columnChecks" :loading="loading" @refresh="refreshData" layout="refresh,size,fullscreen,columns,settings">
        <template #left>
          <ElSpace wrap>
            <ElInput v-model="searchKeyword" placeholder="搜索技术栈..." clearable style="width: 200px" @input="handleSearch" />
            <ElSelect v-model="sortBy" placeholder="排序方式" style="width: 150px" @change="handleSortChange">
              <ElOption label="按使用次数" value="count" />
              <ElOption label="按字母顺序" value="name" />
            </ElSelect>
          </ElSpace>
        </template>
      </ArtTableHeader>
      <ArtTable :loading="loading" :data="data" :columns="columns" :pagination="pagination"
        @pagination:size-change="handleSizeChange" @pagination:current-change="handleCurrentChange" />
    </ElCard>
  </div>
</template>

<script setup lang="ts">
import { ref, h } from 'vue'
import { ElCard, ElInput, ElSelect, ElOption, ElSpace } from 'element-plus'
import ArtBreadcrumb from '@/components/core/layouts/art-breadcrumb/index.vue'
import ArtTableHeader from '@/components/core/tables/art-table-header/index.vue'
import ArtTable from '@/components/core/tables/art-table/index.vue'
import { useTable } from '@/hooks/core/useTable'
import { fetchTechStackStats } from '@/api/taxonomy'
import { onMounted } from 'vue'

defineOptions({ name: 'TechStack' })

const breadcrumbItems = [
  { label: '首页', path: '/content/articles' },
  { label: '技术栈管理', path: '/content/tags' }
]

const searchKeyword = ref('')
const sortBy = ref('count')

const columnChecks = ref<string[]>([])

const { columns, data, loading, pagination, getData, handleSizeChange, handleCurrentChange, refreshData } = useTable({
  core: {
    apiFn: fetchTechStackStats,
    apiParams: { page: 1, size: 20, sort_by: 'count' },
    columnsFactory: () => [
      { type: 'index', width: 60, label: '序号' },
      { prop: 'name', label: '技术栈名称', minWidth: 150 },
      { prop: 'article_count', label: '文章使用次数', width: 120, align: 'center' },
      { prop: 'project_count', label: '项目使用次数', width: 120, align: 'center' },
      { prop: 'total_count', label: '总使用次数', width: 120, align: 'center',
        formatter: (row: any) => h('span', { class: 'font-semibold text-primary' }, `${row.total_count || 0}次`)
      },
    ]
  }
})

const handleSearch = () => {
  refreshData({ keyword: searchKeyword.value })
}

const handleSortChange = (val: string) => {
  refreshData({ sort_by: val })
}

onMounted(() => { getData() })
</script>

<style lang="scss" scoped>
.tech-stack-page { padding: 20px; }
.tech-stack-page .el-card {
  border: 1px solid var(--art-card-border);
  transition: all 0.2s ease;
  &:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
}
</style>