<template>
  <div class="comment-page art-full-height">
    <ArtBreadcrumb :items="breadcrumbItems" />
    <div v-if="contextTitle" class="flex items-center gap-3 mb-4 p-4 bg-white rounded-lg shadow-sm border border-[var(--art-card-border)]">
      <ElButton size="small" @click="goBack">
        <template #icon><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg></template>
        返回列表
      </ElButton>
      <span class="text-sm text-gray-600">当前查看：</span>
      <ElTag type="info" effect="plain">{{ contextBreadcrumb }}</ElTag>
      <span class="text-sm font-medium text-gray-800">{{ contextTitle }}</span>
    </div>
    <ElCard class="mt-4 art-table-card rounded-lg shadow-sm border border-[var(--art-card-border)]">
      <ArtTableHeader v-model:columns="columnChecks" :loading="loading" @refresh="refreshData" layout="refresh,size,fullscreen,columns,settings">
        <template #left>
          <ElSpace wrap>
            <ElInput v-model="searchKeyword" placeholder="搜索评论内容..." clearable style="width: 200px" @input="handleSearch" />
            <ElSelect v-model="filterType" placeholder="内容类型" clearable style="width: 120px" @change="handleFilterChange">
              <ElOption label="全部" value="" />
              <ElOption label="文章" value="article" />
              <ElOption label="项目" value="project" />
            </ElSelect>
            <ElSelect v-model="filterStatus" placeholder="审核状态" clearable style="width: 120px" @change="handleFilterChange">
              <ElOption label="全部" value="" />
              <ElOption label="已审核" value="approved" />
              <ElOption label="待审核" value="pending" />
            </ElSelect>
            <ElSelect v-model="sortOrder" placeholder="排序" clearable style="width: 120px" @change="handleFilterChange">
              <ElOption label="最新优先" value="desc" />
              <ElOption label="最早优先" value="asc" />
            </ElSelect>
          </ElSpace>
        </template>
      </ArtTableHeader>
      <ArtTable :loading="loading" :data="data" :columns="columns" :pagination="pagination"
        @pagination:size-change="handleSizeChange" @pagination:current-change="handleCurrentChange" />
    </ElCard>

    <ElDialog v-model="replyVisible" title="回复评论" width="500px" :close-on-click-modal="false">
      <div class="mb-4 p-3 bg-gray-50 rounded-lg">
        <div class="text-sm text-gray-500 mb-1">原评论：</div>
        <div class="text-sm text-gray-800">{{ currentComment?.content }}</div>
      </div>
      <ElInput v-model="replyContent" type="textarea" :rows="3" placeholder="请输入回复内容" />
      <template #footer>
        <ElButton @click="replyVisible = false">取消</ElButton>
        <ElButton type="primary" @click="handleReplySubmit" :loading="replyLoading">确定</ElButton>
      </template>
    </ElDialog>
  </div>
</template>

<script setup lang="ts">
import { ref, h, computed, onMounted, nextTick } from 'vue'
import { ElCard, ElInput, ElSelect, ElOption, ElSpace, ElButton, ElMessage, ElMessageBox, ElDialog, ElTag } from 'element-plus'
import ArtBreadcrumb from '@/components/core/layouts/art-breadcrumb/index.vue'
import ArtTableHeader from '@/components/core/tables/art-table-header/index.vue'
import ArtTable from '@/components/core/tables/art-table/index.vue'
import { useTable } from '@/hooks/core/useTable'
import { fetchCommentList, deleteComment, approveComment, createComment } from '@/api/comments'
import { useRoute, useRouter, onBeforeRouteUpdate } from 'vue-router'

defineOptions({ name: 'Comments' })

const route = useRoute()
const router = useRouter()

const contextTitle = computed(() => route.query.title as string || '')
const contextBreadcrumb = computed(() => {
  if (route.query.article_id) return '文章'
  if (route.query.project_id) return '项目'
  return ''
})

const breadcrumbItems = computed(() => [
  { label: '首页', path: '/content/articles' },
  { label: '评论管理', path: '/community/comments' }
])

const searchKeyword = ref('')
const filterType = ref('')
const filterStatus = ref('')
const sortOrder = ref('desc')
const replyVisible = ref(false)
const replyContent = ref('')
const replyLoading = ref(false)
const currentComment = ref<any>(null)

const columnChecks = ref<string[]>([])

const { columns, data, loading, pagination, getData, replaceSearchParams, handleSizeChange, handleCurrentChange, refreshData } = useTable({
  core: {
    apiFn: fetchCommentList,
    apiParams: { page: 1, size: 10, article_id: undefined as number | undefined, project_id: undefined as number | undefined, content: undefined as string | undefined, type: undefined as string | undefined, status: undefined as string | undefined },
    columnsFactory: () => [
      { type: 'index', width: 60, label: '序号' },
      { prop: 'id', label: 'ID', width: 70 },
      {
        prop: 'content_type', label: '内容类型', width: 90,
        formatter: (row: any) => {
          const type = row.content_type === 'article' ? '文章' : (row.content_type === 'project' ? '项目' : '')
          const tagType = row.content_type === 'article' ? 'primary' : (row.content_type === 'project' ? 'success' : 'info')
          return h(ElTag, { type: tagType, size: 'small' }, type)
        }
      },
      {
        prop: 'content_title', label: '关联内容', minWidth: 160, showOverflowTooltip: true,
        formatter: (row: any) => {
          const link = row.content_type === 'article' ? '/content/articles' : '/content/projects'
          return h('a', {
            href: `#${link}`,
            class: 'text-[var(--el-color-primary)] hover:underline cursor-pointer',
            onClick: (e: Event) => { e.preventDefault(); router.push(link) }
          }, row.content_title || `#${row.content_id}`)
        }
      },
      { prop: 'content', label: '评论内容', minWidth: 250, showOverflowTooltip: true },
      { prop: 'username', label: '评论人', width: 120 },
      {
        prop: 'is_approved', label: '状态', width: 90,
        formatter: (row: any) => h(ElTag, { type: row.is_approved ? 'success' : 'warning', size: 'small' }, row.is_approved ? '已审核' : '待审核')
      },
      { prop: 'created_at', label: '评论时间', width: 170 },
      {
        prop: 'operation', label: '操作', width: 220, fixed: 'right',
        formatter: (row: any) => h('div', { class: 'flex gap-1' }, [
          h(ElButton, { type: 'primary', size: 'small', onClick: () => openReply(row) }, '回复'),
          h(ElButton, {
            type: row.is_approved ? 'warning' : 'success', size: 'small',
            onClick: () => toggleApprove(row)
          }, row.is_approved ? '取消审核' : '审核通过'),
          h(ElButton, { type: 'danger', size: 'small', onClick: () => handleDelete(row) }, '删除')
        ])
      }
    ]
  },
  transform: {
    responseAdapter: (response: any) => ({
      records: response.comments || [],
      total: response.total || 0,
      current: response.page || 1,
      size: response.size || 10
    })
  }
})

function goBack() {
  const link = route.query.article_id ? '/content/articles' : '/content/projects'
  router.push(link)
}

function buildApiParams() {
  return {
    page: 1, size: 10,
    article_id: route.query.article_id ? Number(route.query.article_id) : undefined,
    project_id: route.query.project_id ? Number(route.query.project_id) : undefined,
    content: searchKeyword.value || undefined,
    type: filterType.value || undefined,
    status: filterStatus.value || undefined
  }
}

const handleSearch = () => {
  replaceSearchParams(buildApiParams())
  getData()
}

const handleFilterChange = () => {
  replaceSearchParams(buildApiParams())
  getData()
}

const toggleApprove = async (row: any) => {
  try {
    await approveComment(row.id)
    ElMessage.success(row.is_approved ? '已取消审核' : '审核通过')
    refreshData()
  } catch { ElMessage.error('操作失败') }
}

const handleDelete = (row: any) => {
  ElMessageBox.confirm('确定要删除该评论吗？', '删除确认', { confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning' })
    .then(async () => { await deleteComment(row.id); ElMessage.success('删除成功'); refreshData() })
    .catch(() => {})
}

const openReply = (row: any) => {
  currentComment.value = row
  replyContent.value = ''
  replyVisible.value = true
}

const handleReplySubmit = async () => {
  if (!replyContent.value.trim()) { ElMessage.warning('请输入回复内容'); return }
  replyLoading.value = true
  try {
    await createComment({
      article_id: currentComment.value.article_id || undefined,
      project_id: currentComment.value.project_id || undefined,
      content: replyContent.value,
      parent_id: currentComment.value.id
    })
    ElMessage.success('回复成功')
    replyVisible.value = false
    refreshData()
  } catch { ElMessage.error('回复失败') }
  finally { replyLoading.value = false }
}

function loadData() {
  if (route.query.article_id) {
    filterType.value = 'article'
  } else if (route.query.project_id) {
    filterType.value = 'project'
  } else {
    filterType.value = ''
  }
  replaceSearchParams(buildApiParams())
  getData()
}

onMounted(loadData)

onBeforeRouteUpdate(() => {
  nextTick(() => {
    loadData()
  })
})
</script>

<style lang="scss" scoped>
.comment-page { padding: 20px; }
.comment-page .el-card {
  border: 1px solid var(--art-card-border);
  transition: all 0.2s ease;
  &:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
}
</style>
