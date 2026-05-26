<template>
  <div class="experiences-page">
    <art-page-content>
      <template #header>
        <art-breadcrumb :items="breadcrumbItems" />
        <art-header-bar title="工作经历" :action="headerAction" />
      </template>

      <template #body>
        <el-card>
          <el-timeline>
            <el-timeline-item
              v-for="exp in experiences"
              :key="exp.id"
              :timestamp="`${exp.start_date} - ${exp.end_date}`"
              placement="top"
            >
              <el-card shadow="hover">
                <div class="flex justify-between items-start">
                  <div>
                    <h3 class="text-xl font-bold">{{ exp.title }}</h3>
                    <div class="text-gray-600">{{ exp.company }}</div>
                    <p class="mt-2 text-gray-700">{{ exp.description }}</p>
                  </div>
                  <div class="flex gap-2">
                    <el-button size="small" @click="handleEdit(exp)">编辑</el-button>
                    <el-button size="small" type="danger" @click="handleDelete(exp.id)">删除</el-button>
                  </div>
                </div>
              </el-card>
            </el-timeline-item>
          </el-timeline>
        </el-card>
      </template>
    </art-page-content>

    <el-dialog v-model="dialogVisible" :title="isEdit ? '编辑工作经历' : '添加工作经历'" width="600px">
      <el-form :model="form" label-width="100px">
        <el-form-item label="职位名称" required>
          <el-input v-model="form.title" placeholder="如: 前端开发工程师" />
        </el-form-item>
        <el-form-item label="公司名称" required>
          <el-input v-model="form.company" placeholder="如: 某某科技有限公司" />
        </el-form-item>
        <el-form-item label="开始时间" required>
          <el-date-picker v-model="form.start_date" type="month" placeholder="选择开始时间" />
        </el-form-item>
        <el-form-item label="结束时间">
          <el-date-picker v-model="form.end_date" type="month" placeholder="选择结束时间" />
        </el-form-item>
        <el-form-item label="工作描述">
          <el-input v-model="form.description" type="textarea" :rows="4" placeholder="描述工作内容和成就" />
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
import { fetchExperiences, createExperience, updateExperience, deleteExperience } from '@/api/profile'

const breadcrumbItems = [
  { label: '首页', path: '/' },
  { label: '简历管理', path: '/profile/resume' },
  { label: '工作经历', path: '/profile/experiences' }
]

const experiences = ref<any[]>([])
const dialogVisible = ref(false)
const isEdit = ref(false)
const form = ref({
  id: 0,
  title: '',
  company: '',
  start_date: '',
  end_date: '',
  description: '',
  order: 0
})

const headerAction = {
  type: 'button',
  text: '添加经历',
  icon: 'ri:add-line',
  click: () => handleAdd()
}

async function loadExperiences() {
  try {
    const response = await fetchExperiences()
    experiences.value = response.data
  } catch (error) {
    console.error('加载工作经历失败:', error)
  }
}

function handleAdd() {
  isEdit.value = false
  form.value = { id: 0, title: '', company: '', start_date: '', end_date: '', description: '', order: 0 }
  dialogVisible.value = true
}

function handleEdit(exp: any) {
  isEdit.value = true
  form.value = { ...exp }
  dialogVisible.value = true
}

async function handleDelete(id: number) {
  try {
    await deleteExperience(id)
    ElMessage.success('删除成功')
    loadExperiences()
  } catch (error) {
    ElMessage.error('删除失败')
  }
}

async function handleSubmit() {
  try {
    if (isEdit.value) {
      await updateExperience(form.value.id, form.value)
    } else {
      await createExperience(form.value)
    }
    ElMessage.success(isEdit.value ? '修改成功' : '添加成功')
    dialogVisible.value = false
    loadExperiences()
  } catch (error) {
    ElMessage.error('操作失败')
  }
}

onMounted(() => {
  loadExperiences()
})
</script>

<style scoped>
.experiences-page {
  min-height: 100%;
}

.experiences-page .el-card {
  transition: all 0.2s ease;
}
.experiences-page .el-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

.experiences-page .el-timeline-item .el-card {
  border: 1px solid var(--art-card-border);
  transition: box-shadow 0.3s ease;
}

.experiences-page .el-timeline-item .el-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}
</style>
