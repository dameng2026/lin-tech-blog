<template>
  <div class="guestbook-page art-full-height">
    <ElCard class="art-table-card" style="margin-top: 0">
      <ArtTableHeader v-model:columns="columnChecks" :loading="loading" @refresh="refreshData">
        <template #left>
          <ElSpace wrap>
            <ElSelect v-model="filterStatus" placeholder="审核状态" clearable style="width: 120px" @change="handleFilterChange">
              <ElOption label="待审" value="pending" />
              <ElOption label="通过" value="approved" />
              <ElOption label="隐藏" value="hidden" />
            </ElSelect>
          </ElSpace>
        </template>
      </ArtTableHeader>

      <ArtTable
        :loading="loading"
        :data="data"
        :columns="columns"
        :pagination="pagination"
        @pagination:size-change="handleSizeChange"
        @pagination:current-change="handleCurrentChange"
      />

      <ElDialog
        v-model="replyDialogVisible"
        title="回复留言"
        width="500px"
        :close-on-click-modal="false"
      >
        <ElForm :model="replyForm" ref="replyFormRef" label-width="80px">
          <ElFormItem label="回复内容">
            <ElInput v-model="replyForm.reply" type="textarea" :rows="4" placeholder="请输入回复内容" />
          </ElFormItem>
        </ElForm>
        <template #footer>
          <ElButton @click="replyDialogVisible = false">取消</ElButton>
          <ElButton type="primary" @click="handleReplySubmit" :loading="submitLoading">提交回复</ElButton>
        </template>
      </ElDialog>
    </ElCard>
  </div>
</template>

<script setup lang="ts">
  import { useTable } from '@/hooks/core/useTable'
  import { fetchGuestbooks, updateGuestbook, deleteGuestbook } from '@/api/comments'
  import { ElMessage, ElMessageBox, FormInstance } from 'element-plus'

  defineOptions({ name: 'Guestbook' })

  const filterStatus = ref<string>('')
  const replyDialogVisible = ref(false)
  const replyFormRef = ref<FormInstance>()
  const submitLoading = ref(false)
  const currentGuestbookId = ref<number>()
  const replyForm = ref({ reply: '' })

  const { data, columns, columnChecks, loading, pagination, getData, handleSizeChange, handleCurrentChange, refreshData } = useTable({
    core: {
      apiFn: fetchGuestbooks,
      apiParams: {},
      columnsFactory: () => [
        { type: 'index', width: 60, label: '序号' },
        { prop: 'id', label: 'ID', width: 80 },
        { prop: 'content', label: '留言内容', showOverflowTooltip: true },
        { prop: 'username', label: '留言人', width: 120 },
        { prop: 'reply', label: '博主回复', showOverflowTooltip: true },
        {
          prop: 'is_top',
          label: '状态',
          width: 100,
          formatter: (row) => {
            if (row.is_top) {
              return h('el-tag', { type: 'warning' }, () => '置顶')
            }
            return row.reply ? h('el-tag', { type: 'success' }, () => '已回复') : h('el-tag', { type: 'info' }, () => '待回复')
          }
        },
        { prop: 'created_at', label: '留言时间', width: 180 },
        {
          prop: 'operation',
          label: '操作',
          width: 220,
          fixed: 'right',
          formatter: (row) => [
            { type: 'primary', text: '回复', onClick: () => showReplyDialog(row) },
            { type: 'warning', text: '置顶', onClick: () => toggleTop(row) },
            { type: 'danger', text: '删除', onClick: () => handleDelete(row) }
          ]
        }
      ]
    }
  })

  const handleFilterChange = () => {
    refreshData()
  }

  const showReplyDialog = (row: any) => {
    currentGuestbookId.value = row.id
    replyForm.value.reply = row.reply || ''
    replyDialogVisible.value = true
  }

  const handleReplySubmit = async () => {
    submitLoading.value = true
    try {
      await updateGuestbook(currentGuestbookId.value!, { reply: replyForm.value.reply })
      ElMessage.success('回复成功')
      replyDialogVisible.value = false
      refreshData()
    } catch (error) {
      ElMessage.error('回复失败')
    } finally {
      submitLoading.value = false
    }
  }

  const toggleTop = (row: any) => {
    ElMessageBox.confirm(`确定要${row.is_top ? '取消置顶' : '置顶'}该留言吗？`, '操作确认', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    }).then(async () => {
      await updateGuestbook(row.id, { is_top: !row.is_top })
      ElMessage.success(row.is_top ? '已取消置顶' : '已置顶')
      refreshData()
    }).catch(() => {})
  }

  const handleDelete = (row: any) => {
    ElMessageBox.confirm(`确定要删除该留言吗？`, '删除确认', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    }).then(async () => {
      await deleteGuestbook(row.id)
      ElMessage.success('删除成功')
      refreshData()
    }).catch(() => {})
  }
</script>

<style scoped>
  .guestbook-page {
    padding: 16px;
  }
</style>
