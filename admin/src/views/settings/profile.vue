<template>
  <div class="profile-page art-full-height">
    <ArtBreadcrumb :items="breadcrumbItems" />

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 mt-4">
      <ElCard class="rounded-xl shadow-sm border border-[var(--art-card-border)]">
        <template #header><span class="font-semibold">技术栈标签管理</span></template>
        <div class="space-y-4">
          <div v-for="(tag, idx) in techStackTags" :key="idx" class="flex items-center gap-2 p-2 bg-gray-50 rounded">
            <ElInput v-model="tag.name" placeholder="技术名称" size="small" style="flex: 1" />
            <ElSelect v-model="tag.category" placeholder="分类" size="small" style="width: 110px">
              <ElOption label="前端" value="前端" />
              <ElOption label="后端" value="后端" />
              <ElOption label="数据库" value="数据库" />
              <ElOption label="DevOps" value="DevOps" />
              <ElOption label="其他" value="其他" />
            </ElSelect>
            <ElButton type="danger" size="small" @click="removeTechStackTag(idx)">删除</ElButton>
          </div>
          <div class="flex gap-2">
            <ElButton type="primary" @click="addTechStackTag" size="small">添加标签</ElButton>
            <ElButton type="primary" @click="saveTechStackTags" :loading="savingTechStack" size="small">保存更改</ElButton>
          </div>
          <div class="mt-4 p-4 bg-gray-50 rounded-lg">
            <h4 class="text-sm font-medium text-gray-700 mb-3">前台预览效果：</h4>
            <div class="flex flex-wrap gap-2">
              <span v-for="tag in techStackTags" :key="tag.name" class="px-3 py-1 bg-[#f0f3ff] text-[#1f5cff] rounded-full text-xs font-medium border border-[#cad4fc] transition-all duration-200 hover:shadow-md hover:scale-105">{{ tag.name }}</span>
            </div>
          </div>
        </div>
      </ElCard>

      <ElCard>
        <template #header><span class="font-semibold">基本信息</span></template>
        <ElForm :model="form" label-width="100px">
          <ElFormItem label="名称">
            <ElInput v-model="form.author_name" placeholder="作者名称" />
          </ElFormItem>
          <ElFormItem label="简介">
            <ElInput v-model="form.description" placeholder="一句话简介" />
          </ElFormItem>
          <ElFormItem label="个人介绍">
            <ElInput v-model="form.bio" type="textarea" :rows="4" placeholder="个人详细介绍" />
          </ElFormItem>
          <ElFormItem label="位置">
            <ElInput v-model="form.location" placeholder="所在地" />
          </ElFormItem>
          <ElFormItem label="邮箱">
            <ElInput v-model="form.email" placeholder="联系邮箱" />
          </ElFormItem>
          <ElFormItem label="GitHub">
            <ElInput v-model="form.github_url" placeholder="GitHub 地址" />
          </ElFormItem>
          <ElFormItem label="开发经验">
            <ElInput v-model="form.experience" placeholder="如: 5 年开发经验" />
          </ElFormItem>
          <ElFormItem>
            <ElButton type="primary" @click="saveSettings" :loading="saving">保存设置</ElButton>
          </ElFormItem>
        </ElForm>
      </ElCard>

      <ElCard>
        <template #header><span class="font-semibold">个人理念与兴趣爱好</span></template>
        <ElForm :model="form" label-width="120px">
          <ElFormItem label="核心理念">
            <ElInput v-model="form.bio_motto" type="textarea" :rows="2" placeholder="核心理念描述" />
          </ElFormItem>
          <ElFormItem label="理念列表">
            <ElInput v-model="form.bio_motto_items" type="textarea" :rows="4" placeholder="每行一条理念，如：&#10;持续学习，保持好奇心&#10;注重工程质量与用户体验" />
          </ElFormItem>
          <ElFormItem label="兴趣爱好">
            <ElInput v-model="form.bio_interests" placeholder="多个兴趣用英文逗号分隔，如：技术探索,开源贡献,阅读写作" />
          </ElFormItem>
          <ElFormItem>
            <ElButton type="primary" @click="saveSettings" :loading="saving">保存设置</ElButton>
          </ElFormItem>
        </ElForm>
      </ElCard>

      <ElCard>
        <template #header>
          <div class="flex justify-between items-center">
            <span class="font-semibold">技能管理</span>
            <ElButton type="primary" size="small" @click="addSkill">添加技能</ElButton>
          </div>
        </template>
        <div class="space-y-3">
          <div v-for="(skill, idx) in skills" :key="idx" class="flex items-center gap-2 p-2 bg-gray-50 rounded">
            <ElInput v-model="skill.name" placeholder="技能名称" size="small" style="flex: 1" />
            <ElSelect v-model="skill.category" placeholder="分类" size="small" style="width: 110px">
              <ElOption label="前端" value="前端" />
              <ElOption label="后端" value="后端" />
              <ElOption label="数据库" value="数据库" />
              <ElOption label="DevOps" value="DevOps" />
              <ElOption label="其他" value="其他" />
            </ElSelect>
            <ElInput v-model.number="skill.proficiency" placeholder="熟练度" type="number" size="small" :min="0" :max="100" style="width: 90px" />
            <ElButton type="danger" size="small" @click="skills.splice(idx, 1)">删除</ElButton>
          </div>
          <ElButton type="primary" @click="saveSkills" :loading="savingSkills">保存技能</ElButton>
        </div>
      </ElCard>

      <ElCard>
        <template #header>
          <div class="flex justify-between items-center">
            <span class="font-semibold">工作经历</span>
            <ElButton type="primary" size="small" @click="addExperience">添加经历</ElButton>
          </div>
        </template>
        <div class="space-y-4">
          <div v-for="(exp, idx) in experiences" :key="idx" class="p-3 bg-gray-50 rounded space-y-2">
            <div class="flex gap-2">
              <ElInput v-model="exp.title" placeholder="职位名称" size="small" />
              <ElInput v-model="exp.company" placeholder="公司名称" size="small" />
            </div>
            <div class="flex gap-2">
              <ElInput v-model="exp.start_date" placeholder="开始日期" size="small" />
              <ElInput v-model="exp.end_date" placeholder="结束日期(留空为至今)" size="small" />
            </div>
            <ElInput v-model="exp.description" type="textarea" :rows="2" placeholder="工作描述" size="small" />
            <ElInput v-model="exp.tagsInput" placeholder="技术标签,英文逗号分隔" size="small" />
            <ElButton type="danger" size="small" @click="experiences.splice(idx, 1)">删除</ElButton>
          </div>
          <ElButton type="primary" @click="saveExperiences" :loading="savingExperiences">保存经历</ElButton>
        </div>
      </ElCard>

      <ElCard>
        <template #header>
          <div class="flex justify-between items-center">
            <span class="font-semibold">教育背景</span>
            <ElButton type="primary" size="small" @click="addEducation">添加教育</ElButton>
          </div>
        </template>
        <div class="space-y-4">
          <div v-for="(edu, idx) in education" :key="idx" class="p-3 bg-gray-50 rounded space-y-2">
            <ElInput v-model="edu.school" placeholder="学校名称" size="small" />
            <ElInput v-model="edu.major" placeholder="专业" size="small" />
            <ElInput v-model="edu.degree" placeholder="学位(如: 本科)" size="small" />
            <div class="flex gap-2">
              <ElInput v-model="edu.start_date" placeholder="开始日期" size="small" />
              <ElInput v-model="edu.end_date" placeholder="结束日期" size="small" />
            </div>
            <ElButton type="danger" size="small" @click="education.splice(idx, 1)">删除</ElButton>
          </div>
          <ElButton type="primary" @click="saveEducation" :loading="savingEducation">保存教育</ElButton>
        </div>
      </ElCard>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import { ElCard, ElForm, ElFormItem, ElInput, ElSelect, ElOption, ElButton, ElMessage } from 'element-plus'
import ArtBreadcrumb from '@/components/core/layouts/art-breadcrumb/index.vue'
import { fetchSiteSettings, updateSiteSettings } from '@/api/settings'
import { fetchSkills, createSkill, updateSkill, deleteSkill } from '@/api/profile'
import { fetchExperiences, createExperience, updateExperience, deleteExperience } from '@/api/profile'
import { fetchEducation, createEducation, updateEducation, deleteEducation } from '@/api/profile'

defineOptions({ name: 'ProfileManager' })

const breadcrumbItems = [
  { label: '首页', path: '/content/articles' },
  { label: '关于我管理', path: '/settings/profile' }
]

const saving = ref(false)
const savingSkills = ref(false)
const savingExperiences = ref(false)
const savingEducation = ref(false)

async function saveSettings() {
  saving.value = true
  try {
    await updateSiteSettings({
      author_name: form.author_name,
      description: form.description,
      bio: form.bio,
      location: form.location,
      email: form.email,
      github_url: form.github_url,
      experience: form.experience,
      bio_motto: form.bio_motto,
      bio_motto_items: form.bio_motto_items,
      bio_interests: form.bio_interests
    })
    ElMessage.success('个人信息保存成功')
  } catch { ElMessage.error('保存失败') }
  saving.value = false
}

const form = reactive({
  author_name: '', description: '', bio: '', location: '', email: '', github_url: '',
  experience: '', bio_motto: '', bio_motto_items: '', bio_interests: ''
})

const skills = ref<{ id?: number; name: string; category: string; proficiency: number }[]>([])
const techStackTags = ref<{ name: string; category?: string }[]>([])
const savingTechStack = ref(false)
const experiences = ref<{ id?: number; title: string; company: string; start_date: string; end_date: string; description: string; tagsInput: string }[]>([])
const education = ref<{ id?: number; school: string; major: string; degree: string; start_date: string; end_date: string }[]>([])

async function loadData() {
  try {
    const settings = await fetchSiteSettings()
    if (settings) {
      form.author_name = settings.author_name || ''
      form.description = settings.description || ''
      form.bio = settings.bio || ''
      form.location = settings.location || ''
      form.email = settings.email || ''
      form.github_url = settings.github_url || ''
      form.experience = settings.experience || ''
      form.bio_motto = settings.bio_motto || ''
      form.bio_motto_items = settings.bio_motto_items || ''
      form.bio_interests = settings.bio_interests || ''
    }
    const [skillsData, experiencesData, educationData] = await Promise.all([
      fetchSkills().catch(() => []),
      fetchExperiences().catch(() => []),
      fetchEducation().catch(() => [])
    ])
    if (skillsData) {
        skills.value = skillsData.map((s: any) => ({ id: s.id, name: s.name, category: s.category || '其他', proficiency: s.proficiency || 80 }))
        techStackTags.value = skillsData.map((s: any) => ({ name: s.name, category: s.category || '其他' }))
      }
    if (experiencesData) experiences.value = experiencesData.map((e: any) => ({ ...e, company: e.company || '', tagsInput: (e.tags || []).join(',') }))
    if (educationData) education.value = educationData
  } catch (e) { console.error('加载失败', e) }
}

async function saveSkills() {
  savingSkills.value = true
  try {
    for (const skill of skills.value) {
      if (skill.id) {
        await updateSkill(skill.id, { name: skill.name, category: skill.category, proficiency: skill.proficiency })
      } else {
        await createSkill({ name: skill.name, category: skill.category || 'core', proficiency: skill.proficiency, order: 0 })
      }
    }
    ElMessage.success('保存成功')
    await loadData()
  } catch { ElMessage.error('保存失败') }
  savingSkills.value = false
}

async function saveExperiences() {
  savingExperiences.value = true
  try {
    for (const exp of experiences.value) {
      const payload = {
        title: exp.title,
        company: exp.company || '',
        description: exp.description,
        start_date: exp.start_date,
        end_date: exp.end_date,
        tags: exp.tagsInput ? exp.tagsInput.split(',').map((t: string) => t.trim()).filter(Boolean) : [],
        order: 0
      }
      if (exp.id) {
        await updateExperience(exp.id, payload)
      } else {
        await createExperience(payload)
      }
    }
    ElMessage.success('保存成功')
    await loadData()
  } catch { ElMessage.error('保存失败') }
  savingExperiences.value = false
}

async function saveEducation() {
  savingEducation.value = true
  try {
    for (const edu of education.value) {
      const payload = {
        degree: edu.degree,
        school: edu.school,
        major: edu.major,
        start_date: edu.start_date,
        end_date: edu.end_date,
        order: 0
      }
      if (edu.id) {
        await updateEducation(edu.id, payload)
      } else {
        await createEducation(payload)
      }
    }
    ElMessage.success('保存成功')
    await loadData()
  } catch { ElMessage.error('保存失败') }
  savingEducation.value = false
}

function addSkill() { skills.value.push({ name: '', category: '前端', proficiency: 80 }) }
function addExperience() { experiences.value.push({ title: '', company: '', start_date: '', end_date: '', description: '', tagsInput: '' }) }
function addEducation() { education.value.push({ school: '', major: '', degree: '', start_date: '', end_date: '' }) }

function addTechStackTag() { techStackTags.value.push({ name: '', category: '前端' }) }

function removeTechStackTag(idx: number) { techStackTags.value.splice(idx, 1) }

async function saveTechStackTags() {
  savingTechStack.value = true
  try {
    const existing = await fetchSkills().catch(() => [])
    const existingNames = new Set((existing || []).map((s: any) => s.name))
    for (const tag of techStackTags.value) {
      if (!tag.name) continue
      const data = { name: tag.name, category: tag.category || '其他', proficiency: 80, order: 0 }
      if (!existingNames.has(tag.name)) {
        await createSkill(data)
      } else {
        const found = (existing || []).find((s: any) => s.name === tag.name)
        if (found) await updateSkill(found.id, data)
      }
    }
    const tagNames = new Set(techStackTags.value.map((t: any) => t.name))
    for (const s of (existing || [])) {
      if (!tagNames.has(s.name)) {
        await deleteSkill(s.id)
      }
    }
    ElMessage.success('技术栈标签保存成功')
    await loadData()
  } catch { ElMessage.error('保存失败') }
  savingTechStack.value = false
}

onMounted(loadData)
</script>

<style lang="scss" scoped>
.profile-page { padding: 20px; }

.profile-page .el-card {
  transition: all 0.2s ease;
}
.profile-page .el-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
</style>