<template>
  <div class="education-page">
    <art-page-content>
      <template #header>
        <art-breadcrumb :items="breadcrumbItems" />
        <art-header-bar title="教育背景" :action="headerAction" />
      </template>

      <template #body>
        <el-card>
          <el-timeline>
            <el-timeline-item
              v-for="edu in education"
              :key="edu.id"
              :timestamp="`${edu.start_date} - ${edu.end_date}`"
              placement="top"
            >
              <el-card shadow="hover">
                <div class="flex justify-between items-start">
                  <div>
                    <h3 class="text-xl font-bold">{{ edu.degree }}</h3>
                    <div class="text-gray-600">{{ edu.school }}</div>
                    <div class="text-gray-500">{{ edu.major }}</div>
                  </div>
                  <div class="flex gap-2">
                    <el-button size="small" @click="handleEdit(edu)">编辑</el-button>
                    <el-button size="small" type="danger" @click="handleDelete(edu.id)">删除</el-button>
                  </div>
                </div>
              </el-card>
            </el-timeline-item>
          </el-timeline>
        </el-card>
      </template>
    </art-page-content>

    <el-dialog v-model="dialogVisible" :title="isEdit ? '编辑教育背景' : '添加教育背景'" width="500px">
      <el-form :model="form" label-width="100px">
        <el-form-item label="学历" required>
          <el-input v-model="form.degree" placeholder="如: 硕士, 本科" />
        </el-form-item>
        <el-form-item label="学校" required>
          <el-input v-model="form.school" placeholder="如: 某某大学" />
        </el-form-item>
        <el-form-item label="专业" required>
          <el-input v-model="form.major" placeholder="如: 计算机科学与技术" />
        </el-form-item>
        <el-form-item label="开始时间" required>
          <el-date-picker v-model="form.start_date" type="month" placeholder="选择开始时间" />
        </el-form-item>
        <el-form-item label="结束时间">
          <el-date-picker v-model="form.end_date" type="month" placeholder="选择结束时间" />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" size="small" @click="handleSubmit">保存</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElCard, ElTimeline, ElTimelineItem, ElButton, ElDialog, ElForm, ElFormItem, ElInput, ElDatePicker } from 'element-plus'
import ArtPageContent from '@/components/core/layouts/art-page-content/index.vue'
import ArtBreadcrumb from '@/components/core/layouts/art-breadcrumb/index.vue'
import ArtHeaderBar from '@/components/core/layouts/art-header-bar/index.vue'
import { fetchEducation, createEducation, updateEducation, deleteEducation } from '@/api/profile'

const breadcrumbItems = [
  { label: '首页', path: '/' },
  { label: '简历管理', path: '/profile/resume' },
  { label: '教育背景', path: '/profile/education' }
]

const education = ref<any[]>([])
const dialogVisible = ref(false)
const isEdit = ref(false)
const form = ref({
  id: 0,
  degree: '',
  school: '',
  major: '',
  start_date: '',
  end_date: '',
  order: 0
})

const headerAction = {
  type: 'button',
  text: '添加教育',
  icon: 'ri:add-line',
  click: () => handleAdd()
}

function formatDate(date: Date): string {
  const y = date.getFullYear()
  const m = String(date.getMonth() + 1).padStart(2, '0')
  return `${y}.${m}`
}

async function loadEducation() {
  try {
    education.value = await fetchEducation()
  } catch (error) {
    console.error('加载教育背景失败:', error)
  }
}

function handleAdd() {
  isEdit.value = false
  form.value = { id: 0, degree: '', school: '', major: '', start_date: '', end_date: '', order: 0 }
  dialogVisible.value = true
}

function handleEdit(edu: any) {
  isEdit.value = true
  form.value = { ...edu }
  dialogVisible.value = true
}

async function handleDelete(id: number) {
  try {
    await deleteEducation(id)
    ElMessage.success('删除成功')
    loadEducation()
  } catch (error) {
    ElMessage.error('删除失败')
  }
}

async function handleSubmit() {
  try {
    const payload = { ...form.value }
    delete payload.id
    if (payload.start_date instanceof Date) payload.start_date = formatDate(payload.start_date)
    if (payload.end_date instanceof Date) payload.end_date = formatDate(payload.end_date)
    if (isEdit.value) {
      await updateEducation(form.value.id, payload)
    } else {
      await createEducation(payload)
    }
    ElMessage.success(isEdit.value ? '修改成功' : '添加成功')
    dialogVisible.value = false
    loadEducation()
  } catch (error) {
    ElMessage.error('操作失败')
  }
}

onMounted(() => {
  loadEducation()
})
</script>

<style scoped>
.education-page {
  min-height: 100%;
}

.education-page .el-card {
  transition: all 0.2s ease;
}
.education-page .el-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

.education-page .el-timeline-item .el-card {
  border: 1px solid var(--art-card-border);
  transition: box-shadow 0.3s ease;
}

.education-page .el-timeline-item .el-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}
</style>
