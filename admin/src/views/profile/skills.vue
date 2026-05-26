<template>
  <div class="skills-page">
    <art-page-content>
      <template #header>
        <art-breadcrumb :items="breadcrumbItems" />
        <art-header-bar title="技能管理" :action="headerAction" />
      </template>

      <template #body>
        <el-card>
          <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            <div v-for="skill in skills" :key="skill.id" class="bg-[var(--default-box-color)] rounded-xl p-4 shadow-sm border border-[var(--art-card-border)] transition-shadow hover:shadow-md">
              <div class="flex justify-between items-center mb-2">
                <span class="font-bold">{{ skill.name }}</span>
                <div>
                  <el-button size="small" text @click="handleEdit(skill)">
                    <i class="ri-edit-line"></i>
                  </el-button>
                  <el-button size="small" text type="danger" @click="handleDelete(skill.id)">
                    <i class="ri-delete-bin-line"></i>
                  </el-button>
                </div>
              </div>
              <div class="text-sm text-gray-500 mb-2">{{ skill.category }}</div>
              <el-progress :percentage="skill.proficiency" :color="getProgressColor(skill.proficiency)" :stroke-width="8" />
            </div>
          </div>
        </el-card>
      </template>
    </art-page-content>

    <el-dialog v-model="dialogVisible" :title="isEdit ? '编辑技能' : '添加技能'" width="400px">
      <el-form :model="form" label-width="80px">
        <el-form-item label="技能名称" required>
          <el-input v-model="form.name" placeholder="如: Vue, React, Python" />
        </el-form-item>
        <el-form-item label="熟练度" required>
          <el-slider v-model="form.proficiency" :min="0" :max="100" show-input />
        </el-form-item>
        <el-form-item label="分类">
          <el-select v-model="form.category" placeholder="选择分类">
            <el-option label="前端" value="前端" />
            <el-option label="后端" value="后端" />
            <el-option label="数据库" value="数据库" />
            <el-option label="DevOps" value="DevOps" />
            <el-option label="其他" value="其他" />
          </el-select>
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
import { ElCard, ElButton, ElProgress, ElDialog, ElForm, ElFormItem, ElInput, ElSlider, ElSelect, ElOption } from 'element-plus'
import ArtPageContent from '@/components/core/layouts/art-page-content/index.vue'
import ArtBreadcrumb from '@/components/core/layouts/art-breadcrumb/index.vue'
import ArtHeaderBar from '@/components/core/layouts/art-header-bar/index.vue'
import { fetchSkills, createSkill, updateSkill, deleteSkill } from '@/api/profile'

const breadcrumbItems = [
  { label: '首页', path: '/' },
  { label: '简历管理', path: '/profile/resume' },
  { label: '技能管理', path: '/profile/skills' }
]

const skills = ref<any[]>([])
const dialogVisible = ref(false)
const isEdit = ref(false)
const form = ref({
  id: 0,
  name: '',
  proficiency: 50,
  category: '前端'
})

const headerAction = {
  type: 'button',
  text: '添加技能',
  icon: 'ri:add-line',
  click: () => handleAdd()
}

function getProgressColor(percentage: number) {
  if (percentage < 40) return '#909399'
  if (percentage < 70) return '#e6a23c'
  return '#67c23a'
}

async function loadSkills() {
  try {
    skills.value = await fetchSkills()
  } catch (error) {
    console.error('加载技能失败:', error)
  }
}

function handleAdd() {
  isEdit.value = false
  form.value = { id: 0, name: '', proficiency: 50, category: '前端' }
  dialogVisible.value = true
}

function handleEdit(skill: any) {
  isEdit.value = true
  form.value = { ...skill }
  dialogVisible.value = true
}

async function handleDelete(id: number) {
  try {
    await deleteSkill(id)
    ElMessage.success('删除成功')
    loadSkills()
  } catch (error) {
    ElMessage.error('删除失败')
  }
}

async function handleSubmit() {
  try {
    if (isEdit.value) {
      await updateSkill(form.value.id, form.value)
    } else {
      await createSkill(form.value)
    }
    ElMessage.success(isEdit.value ? '修改成功' : '添加成功')
    dialogVisible.value = false
    loadSkills()
  } catch (error) {
    ElMessage.error('操作失败')
  }
}

onMounted(() => {
  loadSkills()
})
</script>

<style scoped>
.skills-page {
  min-height: 100%;
}

.skills-page .grid > div {
  animation: fadeInUp 0.6s ease both;
}

.skills-page .el-card {
  transition: all 0.2s ease;
}
.skills-page .el-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
