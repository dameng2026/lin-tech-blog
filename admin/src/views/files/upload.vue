<template>
  <div class="file-upload-page">
    <art-page-content>
      <template #header>
        <art-breadcrumb :items="breadcrumbItems" />
        <art-header-bar title="文件上传" />
      </template>

      <template #body>
        <el-card class="rounded-xl shadow-sm border border-[var(--art-card-border)]">
          <el-upload
            ref="uploadRef"
            :auto-upload="false"
            :limit="10"
            :on-change="handleChange"
            :on-remove="handleRemove"
            drag
            action="#"
            multiple
            class="w-full"
          >
            <i class="ri-upload-cloud-2-line text-6xl text-blue-400 mb-4"></i>
            <div class="text-lg mb-2">将文件拖拽到此处，或<em>点击上传</em></div>
            <div class="text-gray-400">支持图片、PDF等文件，单个文件不超过50MB</div>
          </el-upload>

          <div class="mt-4">
            <el-select v-model="fileType" placeholder="选择文件类型" class="mb-4">
              <el-option label="通用文件" value="common" />
              <el-option label="文章封面" value="article" />
              <el-option label="项目Logo" value="project" />
              <el-option label="用户头像" value="avatar" />
              <el-option label="友链Logo" value="friendlink" />
            </el-select>
          </div>

          <div class="flex gap-4">
            <el-button type="primary" size="small" @click="handleUpload">开始上传</el-button>
            <el-button @click="handleClear">清空列表</el-button>
          </div>

          <el-divider />

          <div v-if="uploadList.length > 0" class="mt-4">
            <div class="text-lg font-bold mb-4">上传队列</div>
            <el-table :data="uploadList" border>
              <el-table-column prop="name" label="文件名" min-width="200" />
              <el-table-column prop="size" label="大小" width="100">
                <template #default="{ row }">
                  {{ formatSize(row.size) }}
                </template>
              </el-table-column>
              <el-table-column prop="status" label="状态" width="100">
                <template #default="{ row }">
                  <el-tag v-if="row.status === 'ready'" type="info">等待上传</el-tag>
                  <el-tag v-else-if="row.status === 'uploading'" type="warning">上传中</el-tag>
                  <el-tag v-else-if="row.status === 'success'" type="success">成功</el-tag>
                  <el-tag v-else type="danger">失败</el-tag>
                </template>
              </el-table-column>
              <el-table-column label="操作" width="100">
                <template #default="{ row, $index }">
                  <el-button size="small" type="danger" @click="handleRemoveFile($index)">移除</el-button>
                </template>
              </el-table-column>
            </el-table>
          </div>
        </el-card>
      </template>
    </art-page-content>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { ElCard, ElUpload, ElButton, ElSelect, ElOption, ElTable, ElTableColumn, ElTag, ElDivider } from 'element-plus'
import ArtPageContent from '@/components/core/layouts/art-page-content/index.vue'
import ArtBreadcrumb from '@/components/core/layouts/art-breadcrumb/index.vue'
import ArtHeaderBar from '@/components/core/layouts/art-header-bar/index.vue'
import { uploadFile } from '@/api/upload'

const breadcrumbItems = [
  { label: '首页', path: '/' },
  { label: '文件管理', path: '/files/list' },
  { label: '文件上传', path: '/files/upload' }
]

const uploadRef = ref()
const fileType = ref('common')
const uploadList = ref<any[]>([])

function formatSize(bytes: number): string {
  if (bytes < 1024) return bytes + ' B'
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB'
  return (bytes / (1024 * 1024)).toFixed(1) + ' MB'
}

function handleChange(file: any, fileList: any[]) {
  uploadList.value = fileList.map((f: any) => ({
    name: f.name,
    size: f.size,
    file: f.raw,
    status: 'ready'
  }))
}

function handleRemove(file: any, fileList: any[]) {
  uploadList.value = fileList.map((f: any) => ({
    name: f.name,
    size: f.size,
    file: f.raw,
    status: 'ready'
  }))
}

function handleRemoveFile(index: number) {
  uploadList.value.splice(index, 1)
  uploadRef.value.handleRemove(uploadList.value[index])
}

function handleClear() {
  uploadList.value = []
  uploadRef.value.clearFiles()
}

async function handleUpload() {
  if (uploadList.value.length === 0) {
    ElMessage.warning('请先选择文件')
    return
  }

  let successCount = 0
  let failCount = 0

  for (let i = 0; i < uploadList.value.length; i++) {
    const item = uploadList.value[i]
    if (item.status === 'success') continue

    item.status = 'uploading'

    try {
      await uploadFile(item.file, fileType.value)
      item.status = 'success'
      successCount++
    } catch (error) {
      item.status = 'error'
      failCount++
    }
  }

  if (failCount === 0) {
    ElMessage.success(`成功上传 ${successCount} 个文件`)
  } else {
    ElMessage.warning(`成功 ${successCount} 个，失败 ${failCount} 个`)
  }
}
</script>

<style scoped>
.file-upload-page {
  min-height: 100%;
}

.file-upload-page .el-card {
  transition: all 0.2s ease;
  &:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  }
}
</style>
