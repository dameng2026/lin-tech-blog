<template>
  <div class="article-page art-full-height">
    <ArtBreadcrumb :items="breadcrumbItems" />
    
    <!-- 搜索过滤和操作栏 -->
    <ElCard class="mb-4 rounded-lg shadow-sm border border-[var(--art-card-border)]">
      <div class="flex justify-between items-center">
        <ElForm :inline="true" :model="searchForm" class="flex-1">
          <ElFormItem label="文章标题">
            <ElInput v-model="searchForm.title" placeholder="输入文章标题" clearable />
          </ElFormItem>
          <ElFormItem label="分类">
            <ArtCategorySelect v-model="searchForm.category" placeholder="选择分类" width="160px" />
          </ElFormItem>
          <ElFormItem>
            <ElButton type="primary" @click="handleSearch">搜索</ElButton>
            <ElButton @click="handleReset">重置</ElButton>
          </ElFormItem>
        </ElForm>
        <div class="ml-4">
          <ElButton type="primary" @click="handlePublish" v-auth="'add'">发布文章</ElButton>
        </div>
      </div>
    </ElCard>

    <!-- 表格 -->
    <ElCard class="art-table-card rounded-lg shadow-sm border border-[var(--art-card-border)]">
      <ArtTableHeader v-model:columns="columnChecks" :loading="loading" @refresh="refreshData" layout="refresh,size,fullscreen,columns,settings">
      </ArtTableHeader>

      <ArtTable
        :loading="loading"
        :data="data"
        :columns="columns"
        :pagination="pagination"
        @selection-change="handleSelectionChange"
        @pagination:size-change="handleSizeChange"
        @pagination:current-change="handleCurrentChange"
      />
    </ElCard>
  </div>
</template>

<script setup lang="ts">
import { ref, h, onMounted } from 'vue'
import { ElCard, ElForm, ElFormItem, ElInput, ElButton, ElSpace, ElMessage, ElMessageBox } from 'element-plus'
import ArtBreadcrumb from '@/components/core/layouts/art-breadcrumb/index.vue'
import ArtTableHeader from '@/components/core/tables/art-table-header/index.vue'
import ArtTable from '@/components/core/tables/art-table/index.vue'
import ArtButtonTable from '@/components/core/forms/art-button-table/index.vue'
import ArtSvgIcon from '@/components/core/base/art-svg-icon/index.vue'
import ArtCategorySelect from '@/components/core/forms/art-category-select/index.vue'
import { router } from '@/router'
import { useTable } from '@/hooks/core/useTable'
import { fetchArticleList, deleteArticle } from '@/api/articles'

defineOptions({ name: 'ArticleList' })

const breadcrumbItems = [
  { label: '首页', path: '/content/articles' },
  { label: '文章管理', path: '/article/list' }
]

const searchForm = ref({
  title: '',
  category: ''
})

const columnChecks = ref<string[]>([])

const {
  columns,
  data,
  loading,
  pagination,
  getData,
  replaceSearchParams,
  resetSearchParams,
  handleSizeChange,
  handleCurrentChange,
  refreshData
} = useTable({
  core: {
    apiFn: fetchArticleList,
    apiParams: {
      current: 1,
      size: 10,
      ...searchForm.value
    },
    columnsFactory: () => [
      { type: 'selection' },
      { type: 'index', width: 60, label: '序号' },
      {
        prop: 'cover',
        label: '封面',
        width: 120,
        formatter: (row) =>
          h('div', { class: 'flex items-center justify-center' }, [
            h('img', {
              src: row.cover || 'https://via.placeholder.com/80x60',
              style: 'width: 80px; height: 60px; object-fit: cover; border-radius: 4px;'
            })
          ])
      },
      { prop: 'title', label: '标题', minWidth: 200 },
      { prop: 'category', label: '分类', width: 100 },
      { prop: 'view_count', label: '浏览量', width: 100, sortable: true },
      { prop: 'like_count', label: '点赞数', width: 100, sortable: true },
      { prop: 'created_at', label: '发布时间', width: 180, sortable: true,
        formatter: (row) => {
          if (!row.created_at) return '-'
          const d = new Date(row.created_at)
          const pad = (n: number) => String(n).padStart(2, '0')
          return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}`
        }
      },
      {
        prop: 'is_published',
        label: '状态',
        width: 100,
        formatter: (row) =>
          row.is_published ? h('ElTag', { type: 'success' }, '已发布') : h('ElTag', { type: 'warning' }, '草稿')
      },
      {
        prop: 'operation',
        label: '操作',
        width: 220,
        fixed: 'right',
        formatter: (row) =>
          h('div', { class: 'flex gap-2' }, [
            h(ArtButtonTable, { type: 'view', onClick: () => handleView(row) }),
            h(ArtButtonTable, { type: 'edit', onClick: () => handleEdit(row), vAuth: 'edit' }),
            h(ArtButtonTable, { type: 'comment', onClick: () => handleComment(row) }),
            h(ArtButtonTable, { type: 'delete', onClick: () => handleDelete(row), vAuth: 'delete' })
          ])
      }
    ]
  }
})

const handleSelectionChange = (selection) => {
  console.log('选中的文章:', selection)
}

const handleSearch = () => {
  replaceSearchParams({ ...searchForm.value })
  getData()
}

const handleReset = () => {
  searchForm.value = {
    title: '',
    category: ''
  }
  resetSearchParams()
  getData()
}

const handlePublish = () => {
  router.push({ name: 'PublishArticle' })
}

const handleView = (row) => {
  router.push({ name: 'ArticleDetail', params: { id: row.id } })
}

const handleEdit = (row) => {
  router.push({ name: 'PublishArticle', query: { id: row.id } })
}

const handleComment = (row: any) => {
  router.push({ name: 'Comments', query: { article_id: row.id, title: row.title, type: 'article' } })
}

const handleDelete = (row) => {
  ElMessageBox.confirm('确定要删除这篇文章吗？', '删除确认', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning'
  }).then(async () => {
    try {
      await deleteArticle(row.id)
      ElMessage.success('删除成功')
      refreshData()
    } catch (error) {
      ElMessage.error('删除失败')
    }
  })
}

onMounted(() => {
  getData()
})
</script>

<style lang="scss" scoped>
.article-page {
  padding: 20px;

  .el-card {
    transition: all 0.2s ease;
  }
  .el-card:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  }

  :deep(.el-tag) {
    font-size: 12px;
    padding: 0 8px;
    height: 24px;
    line-height: 22px;
    border-radius: 4px;
  }

  :deep(.art-button-table) {
    .el-button {
      --el-button-size: 26px;
    }
  }
}
</style>
