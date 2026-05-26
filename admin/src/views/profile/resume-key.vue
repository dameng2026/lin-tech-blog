<template>
  <div class="resume-key-page art-full-height">
    <ArtBreadcrumb :items="breadcrumbItems" />

    <ElCard class="mt-4 mb-4">
      <template #header><span class="font-medium">生成密钥</span></template>
      <ElForm :inline="true" :model="generateForm">
        <ElFormItem label="密钥长度">
          <ElInputNumber v-model="generateForm.length" :min="8" :max="16" style="width: 120px" />
        </ElFormItem>
        <ElFormItem label="有效期">
          <ElSelect v-model="generateForm.validHours" style="width: 150px">
            <ElOption label="1小时" :value="1" />
            <ElOption label="3小时" :value="3" />
            <ElOption label="1天" :value="24" />
            <ElOption label="7天" :value="168" />
            <ElOption label="自定义" :value="0" />
          </ElSelect>
        </ElFormItem>
        <ElFormItem v-if="generateForm.validHours === 0" label="自定义小时">
          <ElInputNumber v-model="generateForm.customHours" :min="1" :max="720" style="width: 120px" />
        </ElFormItem>
        <ElFormItem>
          <ElButton type="primary" @click="handleGenerate">生成密钥</ElButton>
        </ElFormItem>
      </ElForm>
      <div v-if="newKey" class="mt-3 p-4 bg-green-50 rounded-lg border border-green-200">
        <p class="text-sm text-green-700 mb-2">密钥已生成（请立即复制，关闭后将无法查看完整密钥）：</p>
        <p class="text-xl font-mono font-bold text-green-800">{{ newKey.key_value }}</p>
        <p class="text-sm text-green-600 mt-1">过期时间：{{ newKey.expire_at }}</p>
      </div>
    </ElCard>

    <ElCard class="art-table-card rounded-lg shadow-sm border border-[var(--art-card-border)]">
      <ArtTableHeader v-model:columns="columnChecks" :loading="loading" @refresh="refreshData" layout="refresh,size,fullscreen,columns,settings" />
      <ArtTable :loading="loading" :data="data" :columns="columns" :pagination="pagination"
        @pagination:size-change="handleSizeChange" @pagination:current-change="handleCurrentChange" />
    </ElCard>
  </div>
</template>

<script setup lang="ts">
import { ref, h, onMounted } from 'vue'
import { ElCard, ElForm, ElFormItem, ElInputNumber, ElSelect, ElOption, ElButton, ElMessage, ElMessageBox, ElTag } from 'element-plus'
import ArtBreadcrumb from '@/components/core/layouts/art-breadcrumb/index.vue'
import ArtTableHeader from '@/components/core/tables/art-table-header/index.vue'
import ArtTable from '@/components/core/tables/art-table/index.vue'
import { useTable } from '@/hooks/core/useTable'
import { fetchResumeKeys, createResumeKey, deleteResumeKey } from '@/api/profile'

defineOptions({ name: 'ResumeKeyManager' })

const breadcrumbItems = [
  { label: '首页', path: '/' },
  { label: '简历管理', path: '/profile/resume' },
  { label: 'PDF密钥管理', path: '/profile/pdf-key' }
]

const generateForm = ref({ length: 12, validHours: 24, customHours: 1 })
const newKey = ref<any>(null)

const columnChecks = ref<string[]>([])

const { columns, data, loading, pagination, getData, handleSizeChange, handleCurrentChange, refreshData } = useTable({
  core: {
    apiFn: fetchResumeKeys,
    apiParams: {},
    paginationKey: { current: 'page', size: 'size' },
    columnsFactory: () => [
      { type: 'index', width: 60, label: '序号' },
      { prop: 'key_display', label: '密钥（脱敏）', width: 200 },
      { prop: 'created_at', label: '创建时间', width: 180 },
      { prop: 'expire_at', label: '到期时间', width: 180 },
      {
        prop: 'is_active', label: '状态', width: 100,
        formatter: (row: any) => h(ElTag, { type: row.is_active ? 'success' : 'danger', size: 'small' }, row.is_active ? '有效' : '已失效')
      },
      { prop: 'use_count', label: '使用次数', width: 100, align: 'center' },
      {
        prop: 'operation', label: '操作', width: 100, fixed: 'right',
        formatter: (row: any) => h(ElButton, { type: 'danger', size: 'small', onClick: () => handleDeleteKey(row) }, '删除')
      }
    ]
  }
})

async function handleGenerate() {
  const hours = generateForm.value.validHours === 0 ? generateForm.value.customHours : generateForm.value.validHours
  try {
    newKey.value = await createResumeKey({ length: generateForm.value.length, valid_hours: hours })
    ElMessage.success('密钥生成成功')
    refreshData()
  } catch {
    ElMessage.error('生成失败')
  }
}

function handleDeleteKey(row: any) {
  ElMessageBox.confirm('确定要删除该密钥吗？', '删除确认', { type: 'warning' })
    .then(async () => {
      await deleteResumeKey(row.id)
      ElMessage.success('删除成功')
      refreshData()
    })
    .catch(() => {})
}

onMounted(() => { getData() })
</script>

<style scoped>
.resume-key-page {
  min-height: 100%;
}

.resume-key-page .el-card {
  border: 1px solid var(--art-card-border);
  transition: all 0.2s ease;
}
.resume-key-page .el-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
</style>