<template>
  <div class="resume-page art-full-height">
    <ArtBreadcrumb :items="breadcrumbItems" />

    <ElCard class="mt-4">
      <template #header><span class="font-medium">简历文件管理</span></template>

      <div class="mb-4">
        <div v-if="resumeInfo.exists" class="space-y-4">
          <div class="grid grid-cols-2 gap-4">
            <div><span class="text-gray-500">文件名：</span>{{ resumeInfo.original_name }}</div>
            <div><span class="text-gray-500">文件大小：</span>{{ formatSize(resumeInfo.file_size) }}</div>
            <div><span class="text-gray-500">上传时间：</span>{{ resumeInfo.created_at }}</div>
            <div>
              <span class="text-gray-500">状态：</span>
              <ElTag :type="resumeInfo.is_active ? 'success' : 'danger'">{{ resumeInfo.is_active ? '已启用' : '已暂停' }}</ElTag>
            </div>
          </div>
          <div class="flex gap-2 mt-3">
            <ElButton type="primary" @click="handleUpload">替换文件</ElButton>
            <ElButton :type="resumeInfo.is_active ? 'warning' : 'success'" @click="handleToggleStatus">
              {{ resumeInfo.is_active ? '暂停' : '启用' }}
            </ElButton>
            <ElButton type="danger" @click="handleDelete">删除</ElButton>
          </div>
        </div>
        <div v-else class="text-center py-8 text-gray-400">
          <p class="mb-4">暂无简历文件，请上传PDF格式的简历</p>
          <ElButton type="primary" @click="handleUpload">上传简历</ElButton>
        </div>
      </div>

      <input ref="fileInput" type="file" accept=".pdf" style="display:none" @change="handleFileChange" />
    </ElCard>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import ArtBreadcrumb from '@/components/core/layouts/art-breadcrumb/index.vue'
import { fetchResumeInfo, uploadResume, toggleResumeStatus, deleteResume } from '@/api/profile'

defineOptions({ name: 'Resume' })

const fileInput = ref<HTMLInputElement>()

const breadcrumbItems = [
  { label: '首页', path: '/content/articles' },
  { label: '简历管理', path: '/profile/resume' }
]

const resumeInfo = ref<any>({ exists: false })

function formatSize(bytes: number): string {
  if (!bytes) return '0 B'
  if (bytes < 1024) return bytes + ' B'
  if (bytes < 1048576) return (bytes / 1024).toFixed(1) + ' KB'
  return (bytes / 1048576).toFixed(1) + ' MB'
}

async function loadResumeInfo() {
  try {
    resumeInfo.value = await fetchResumeInfo()
  } catch { }
}

function handleUpload() {
  fileInput.value?.click()
}

async function handleFileChange(e: Event) {
  const file = (e.target as HTMLInputElement).files?.[0]
  if (!file) return
  if (!file.name.toLowerCase().endsWith('.pdf')) {
    ElMessage.error('只允许上传PDF文件')
    return
  }
  if (file.size > 10 * 1024 * 1024) {
    ElMessage.error('文件大小不能超过10MB')
    return
  }
  try {
    await uploadResume(file)
    ElMessage.success('简历上传成功')
    loadResumeInfo()
  } catch {
    ElMessage.error('上传失败')
  } finally {
    (e.target as HTMLInputElement).value = ''
  }
}

async function handleToggleStatus() {
  try {
    await toggleResumeStatus(resumeInfo.value.id)
    ElMessage.success('状态已更新')
    loadResumeInfo()
  } catch {
    ElMessage.error('操作失败')
  }
}

async function handleDelete() {
  try {
    await ElMessageBox.confirm('确定要删除简历文件吗？', '删除确认', { type: 'warning' })
    await deleteResume(resumeInfo.value.id)
    ElMessage.success('删除成功')
    resumeInfo.value = { exists: false }
  } catch (e) {
    if (e !== 'cancel') ElMessage.error('删除失败')
  }
}

onMounted(() => {
  loadResumeInfo()
})
</script>

<style scoped>
.resume-page {
  min-height: 100%;
}

.resume-page .el-card {
  border: 1px solid var(--art-card-border);
  transition: all 0.2s ease;
}
.resume-page .el-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
</style>