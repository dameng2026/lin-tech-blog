<template>
  <div class="guestbook-page art-full-height">
    <ArtBreadcrumb :items="breadcrumbItems" />
    <ElCard class="mt-4 art-table-card rounded-lg shadow-sm border border-[var(--art-card-border)]">
      <ArtTableHeader v-model:columns="columnChecks" :loading="loading" @refresh="refreshData" layout="refresh,size,fullscreen,columns,settings">
        <template #left>
          <ElSpace wrap>
            <ElInput v-model="searchKeyword" placeholder="搜索留言内容..." clearable style="width: 220px" @input="handleSearch" />
            <ElSelect v-model="filterStatus" placeholder="审核状态" clearable style="width: 120px" @change="handleFilterChange">
              <ElOption label="全部" value="" />
              <ElOption label="已审核" value="approved" />
              <ElOption label="待审核" value="pending" />
            </ElSelect>
          </ElSpace>
        </template>
      </ArtTableHeader>
      <ArtTable :loading="loading" :data="data" :columns="columns" :pagination="pagination"
        @pagination:size-change="handleSizeChange" @pagination:current-change="handleCurrentChange" />
    </ElCard>

    <ElDialog v-model="replyVisible" title="回复留言" width="500px" destroy-on-close>
      <ElForm :model="replyForm" label-width="80px">
        <ElFormItem label="留言内容"><p class="text-sm text-gray-600 p-2 bg-gray-50 rounded">{{ replyForm.originalContent }}</p></ElFormItem>
        <ElFormItem label="留言者"><ElInput :model-value="replyForm.username" disabled /></ElFormItem>
        <ElFormItem label="回复内容"><ElInput v-model="replyForm.reply" type="textarea" :rows="3" placeholder="请输入回复内容" /></ElFormItem>
      </ElForm>
      <template #footer>
        <ElButton @click="replyVisible = false">取消</ElButton>
        <ElButton type="primary" @click="handleReply">回复</ElButton>
      </template>
    </ElDialog>
  </div>
</template>

<script setup lang="ts">
import { ref, h, onMounted } from 'vue'
import { ElCard, ElInput, ElSelect, ElOption, ElSpace, ElButton, ElMessage, ElMessageBox, ElDialog, ElForm, ElFormItem, ElTag } from 'element-plus'
import ArtBreadcrumb from '@/components/core/layouts/art-breadcrumb/index.vue'
import ArtTableHeader from '@/components/core/tables/art-table-header/index.vue'
import ArtTable from '@/components/core/tables/art-table/index.vue'
import { useTable } from '@/hooks/core/useTable'
import { fetchGuestbooks, deleteComment, approveComment, replyGuestbookMessage } from '@/api/comments'

defineOptions({ name: 'GuestbookManager' })

const breadcrumbItems = [
  { label: '首页', path: '/content/articles' },
  { label: '留言板管理', path: '/community/messages' }
]

const searchKeyword = ref('')
const filterStatus = ref('')
const replyVisible = ref(false)
const replyForm = ref({ id: 0, originalContent: '', username: '', reply: '' })

const columnChecks = ref<string[]>([])

const { columns, data, loading, pagination, getData, handleSizeChange, handleCurrentChange, refreshData, replaceSearchParams } = useTable({
  core: {
    apiFn: fetchGuestbooks,
    apiParams: { page: 1, size: 10, keyword: undefined as string | undefined, status: undefined as string | undefined },
    columnsFactory: () => [
      { type: 'index', width: 60, label: '序号' },
      { prop: 'id', label: '留言ID', width: 80 },
      { prop: 'content', label: '留言内容', minWidth: 250, showOverflowTooltip: true },
      { prop: 'created_at', label: '提交时间', width: 170 },
      { prop: 'user_id', label: '用户ID', width: 80 },
      { prop: 'username', label: '用户名', width: 120 },
      { prop: 'guest_email', label: '邮箱', width: 180 },
      { prop: 'ip_address', label: 'IP地址', width: 140 },
      {
        prop: 'is_approved', label: '状态', width: 90,
        formatter: (row: any) => h(ElTag, { type: row.is_approved ? 'success' : 'warning', size: 'small' }, row.is_approved ? '已审核' : '待审核')
      },
      {
        prop: 'operation', label: '操作', width: 240, fixed: 'right',
        formatter: (row: any) => h('div', { class: 'flex gap-1' }, [
          ...(row.is_approved ? [] : [h(ElButton, { type: 'success', size: 'small', onClick: () => handleApprove(row) }, '审核通过')]),
          h(ElButton, { type: 'primary', size: 'small', onClick: () => openReply(row) }, '回复'),
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

const handleSearch = () => {
  replaceSearchParams({ page: 1, size: 10, keyword: searchKeyword.value || undefined, status: filterStatus.value || undefined })
  getData()
}
const handleFilterChange = () => {
  replaceSearchParams({ page: 1, size: 10, keyword: searchKeyword.value || undefined, status: filterStatus.value || undefined })
  getData()
}

const handleApprove = async (row: any) => {
  try { await approveComment(row.id); ElMessage.success('审核通过'); refreshData() }
  catch { ElMessage.error('操作失败') }
}

const openReply = (row: any) => {
  replyForm.value = { id: row.id, originalContent: row.content, username: row.username || row.guest_name || '', reply: '' }
  replyVisible.value = true
}

const handleReply = async () => {
  if (!replyForm.value.reply.trim()) { ElMessage.warning('请输入回复内容'); return }
  try { await replyGuestbookMessage(replyForm.value.id, replyForm.value.reply); ElMessage.success('回复成功'); replyVisible.value = false; refreshData() }
  catch { ElMessage.error('回复失败') }
}

const handleDelete = (row: any) => {
  ElMessageBox.confirm('确定要删除那条留言吗？', '删除确认', { confirmButtonText: '确定', cancelButtonText: '取消', type: 'warning' })
    .then(async () => { await deleteComment(row.id); ElMessage.success('删除成功'); refreshData() })
    .catch(() => {})
}

onMounted(() => { getData() })
</script>

<style lang="scss" scoped>
.guestbook-page { padding: 20px; }
.guestbook-page .el-card {
  border: 1px solid var(--art-card-border);
  transition: all 0.2s ease;
  &:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
}
</style>
