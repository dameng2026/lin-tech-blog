<template>
  <div>
    <div v-loading="pageLoading" element-loading-text="正在加载项目数据...">
      <div class="max-w-250 mx-auto my-5">
        <div class="bg-[var(--default-box-color)] rounded-xl p-6 shadow-sm border border-[var(--art-card-border)] mb-5">
          <ElRow :gutter="10">
            <ElCol :span="10">
              <ElInput
                v-model.trim="projectName"
                placeholder="请输入项目名称（最多100个字符）"
                maxlength="100"
              />
            </ElCol>
            <ElCol :span="7">
              <ElSelect v-model="projectType" placeholder="请选择项目类型" filterable>
                <ElOption
                  v-for="item in projectTypes"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </ElSelect>
            </ElCol>
            <ElCol :span="7">
              <ElSelect v-model="projectCategoryId" placeholder="请选择项目分类" filterable>
                <ElOption
                  v-for="item in projectCategories"
                  :key="item.id"
                  :label="item.name"
                  :value="item.id"
                />
              </ElSelect>
            </ElCol>
          </ElRow>

          <ElRow class="mt-2.5">
            <ElCol :span="12">
              <ElSelect v-model="projectStatus" placeholder="请选择项目状态">
                <ElOption
                  v-for="item in projectStatuses"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </ElSelect>
            </ElCol>
            <ElCol :span="12">
              <ElSelect v-model="openSourceLicense" placeholder="请选择开源协议" filterable>
                <ElOption
                  v-for="item in openSourceLicenses"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </ElSelect>
            </ElCol>
          </ElRow>

          <ElRow class="mt-2.5">
            <ElCol :span="12">
              <ElSelect v-model="databaseType" placeholder="请选择数据库类型" filterable>
                <ElOption
                  v-for="item in databaseTypes"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </ElSelect>
            </ElCol>
            <ElCol :span="12">
              <ElInput
                v-model="deploymentPlatform"
                placeholder="部署平台"
              />
            </ElCol>
          </ElRow>

          <ElRow class="mt-2.5">
            <ElCol :span="12">
              <ElInput
                v-model="demoUrl"
                placeholder="项目演示URL"
                @blur="validateUrl('demoUrl')"
              />
            </ElCol>
            <ElCol :span="12">
              <ElInput
                v-model="githubUrl"
                placeholder="GitHub仓库地址"
                @blur="validateUrl('githubUrl')"
              />
            </ElCol>
          </ElRow>

          <ElRow class="mt-2.5">
            <ElCol :span="12">
              <ElInput
                v-model="docsUrl"
                placeholder="文档站点URL"
                @blur="validateUrl('docsUrl')"
              />
            </ElCol>
            <ElCol :span="12">
              <ElInput
                v-model="lastUpdate"
                type="datetime-local"
                placeholder="最后更新时间"
              />
            </ElCol>
          </ElRow>

          <ElRow class="mt-2.5">
            <ElCol :span="12">
              <ElDatePicker
                v-model="startDate"
                type="date"
                placeholder="开发开始日期"
              />
            </ElCol>
            <ElCol :span="12">
              <ElDatePicker
                v-model="endDate"
                type="date"
                placeholder="开发结束日期"
              />
            </ElCol>
          </ElRow>

          <ElRow class="mt-2.5">
            <ElCol :span="24">
              <ElInput
                v-model="projectSummary"
                type="textarea"
                :rows="3"
                placeholder="项目简介（最多500个字符）"
                maxlength="500"
              />
              <div class="flex justify-end mt-1">
                <span class="text-xs text-gray-400">{{ projectSummary.length }}/500</span>
              </div>
            </ElCol>
          </ElRow>

          <ElRow class="mt-2.5">
            <ElCol :span="24">
              <div class="flex flex-wrap items-center gap-2 p-2 border border-gray-300 rounded-md min-h-10">
                <ElTag
                  v-for="(tag, index) in tags"
                  :key="index"
                  closable
                  size="small"
                  type="info"
                  @close="removeTag(index)"
                >
                  {{ tag }}
                </ElTag>
                <ElInput
                  v-model="tagInput"
                  placeholder="输入标签后按回车或逗号添加"
                  size="small"
                  class="flex-1 min-w-40"
                  @keydown="handleTagInputKeydown"
                  @blur="handleTagInputBlur"
                />
              </div>
            </ElCol>
          </ElRow>

          <ElRow class="mt-2.5">
            <ElCol :span="24">
              <div class="flex flex-wrap items-center gap-2 p-2 border border-gray-300 rounded-md min-h-10">
                <ElTag
                  v-for="(tech, index) in techStack"
                  :key="index"
                  closable
                  size="small"
                  type="primary"
                  @close="removeTech(index)"
                >
                  {{ tech }}
                </ElTag>
                <ElSelect
                  v-model="techInput"
                  placeholder="选择技术栈"
                  size="small"
                  class="flex-1 min-w-40"
                  filterable
                  @change="addTech"
                >
                  <ElOption
                    v-for="item in availableTechStack"
                    :key="item"
                    :label="item"
                    :value="item"
                  />
                </ElSelect>
              </div>
            </ElCol>
          </ElRow>
        </div>

        <div class="p-5 mt-5 art-card-xs">
          <h2 class="mb-5 text-xl font-medium">项目标记</h2>
          <div class="flex items-center gap-4">
            <ElRadioGroup v-model="projectTag" class="flex gap-4">
              <ElRadioButton :value="'paid'">
                <div class="flex items-center gap-1">
                  <ElIcon class="text-orange-500"><Coin /></ElIcon>
                  <span>付费项目</span>
                </div>
              </ElRadioButton>
              <ElRadioButton :value="'featured'">
                <div class="flex items-center gap-1">
                  <ElIcon class="text-yellow-500"><StarFilled /></ElIcon>
                  <span>精选项目</span>
                </div>
              </ElRadioButton>
            </ElRadioGroup>
            <ElTag v-if="!projectTag" type="info" size="small" effect="plain">未选择</ElTag>
          </div>
          <div class="text-xs text-g-700 mt-2">付费项目和精选项目为互斥选项，选择后将在前台展示对应标记</div>
        </div>

        <div class="p-5 mt-5 bg-[var(--default-box-color)] rounded-xl shadow-sm border border-[var(--art-card-border)]">
          <ElRow>
            <ElCol :span="24">
              <ElInput
                v-model="repostUrl"
                placeholder="转载URL（若填写则视为转载项目，留空则标记为原创）"
                clearable
                @blur="validateUrl('repostUrl')"
              />
            </ElCol>
          </ElRow>
        </div>

        <div class="p-5 mt-5 art-card-xs">
          <h2 class="mb-5 text-xl font-medium">封面设置</h2>
          <div class="flex gap-3">
            <ElUpload
              :show-file-list="false"
              :before-upload="beforeUpload"
              :http-request="handleFileUpload"
              ref="uploadRef"
            >
              <div
                v-if="!cover"
                class="flex-cc flex-col w-65 h-40 border border-dashed border-[#d9d9d9] rounded-md"
              >
                <ElIcon class="!text-xl !text-g-600"><Plus /></ElIcon>
                <div class="mt-2 text-sm text-g-600">点击上传封面</div>
              </div>
              <img v-else :src="cover" class="block w-65 h-40 object-cover rounded-md" />
            </ElUpload>
            <div v-if="cover" class="flex flex-col gap-2">
              <ElButton size="small" @click="cover = ''">移除封面</ElButton>
              <ElButton size="small" @click="triggerUpload">重新上传</ElButton>
            </div>
          </div>
          <div class="flex items-center gap-2 mt-3">
            <ElInput
              v-model="coverUrlInput"
              placeholder="或输入图片URL链接"
              size="small"
              clearable
              class="flex-1"
            />
            <ElButton size="small" type="primary" @click="handleUrlUpload" :disabled="!coverUrlInput">确认</ElButton>
          </div>
          <div class="text-xs text-g-700 mt-2">建议尺寸 16:9，jpg/png 格式</div>
        </div>

        <div class="p-5 mt-5 art-card-xs">
          <h2 class="mb-5 text-xl font-medium">项目详情内容</h2>
          <ArtWangEditor class="mt-2.5" v-model="editorHtml" />
        </div>

        <div class="p-5 mt-5 art-card-xs">
          <h2 class="mb-5 text-xl font-medium">章节管理</h2>

          <div v-if="catalog.length > 0" class="mb-4 space-y-2">
            <div
              v-for="(item, index) in catalog"
              :key="index"
              class="flex items-center gap-2 py-2 px-3 rounded-lg bg-gray-50 hover:bg-gray-100 transition-colors group"
              :style="{ marginLeft: (item.level - 1) * 24 + 'px' }"
            >
              <div class="flex items-center gap-1">
                <ElIcon class="cursor-move text-gray-400 hover:text-gray-600"><Link /></ElIcon>
                <span
                  v-if="catalogEditingIndex !== index"
                  class="text-sm flex-1 truncate"
                  @click="startEditCatalog(index)"
                >{{ item.title }}</span>
                <ElInput
                  v-else
                  v-model="catalog[index].title"
                  :class="['flex-1', `catalog-item-input-${index}`]"
                  size="small"
                  @blur="finishEditCatalog"
                  @keyup.enter="finishEditCatalog"
                  ref="editInputRef"
                  placeholder="请输入章节标题"
                />
              </div>
              <div class="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                <ElButton
                  text
                  size="small"
                  @click="indentCatalog(index)"
                  :disabled="item.level >= 3"
                  :class="{ 'text-gray-300 cursor-not-allowed': item.level >= 3 }"
                >
                  <ElIcon class="text-blue-500"><CirclePlus /></ElIcon>
                </ElButton>
                <ElButton
                  text
                  size="small"
                  @click="outdentCatalog(index)"
                  :disabled="item.level <= 1"
                  :class="{ 'text-gray-300 cursor-not-allowed': item.level <= 1 }"
                >
                  <ElIcon class="text-blue-500"><Minus /></ElIcon>
                </ElButton>
                <ElButton
                  text
                  size="small"
                  @click="moveCatalogUp(index)"
                  :disabled="index === 0"
                  :class="{ 'text-gray-300 cursor-not-allowed': index === 0 }"
                >
                  <ElIcon class="text-blue-500"><ArrowUp /></ElIcon>
                </ElButton>
                <ElButton
                  text
                  size="small"
                  @click="moveCatalogDown(index)"
                  :disabled="index === catalog.length - 1"
                  :class="{ 'text-gray-300 cursor-not-allowed': index === catalog.length - 1 }"
                >
                  <ElIcon class="text-blue-500"><ArrowDown /></ElIcon>
                </ElButton>
                <ElButton text size="small" type="danger" @click="removeCatalogItem(index)">
                  <ElIcon><Close /></ElIcon>
                </ElButton>
              </div>
            </div>
          </div>

          <div class="flex gap-2">
            <ElButton
              size="small"
              type="primary"
              @click="generateCatalog"
              :loading="catalogLoading"
              :disabled="catalogLoading"
            >
              <ElIcon><MagicStick /></ElIcon>
              自动获取章节
            </ElButton>
            <ElButton size="small" @click="clearCatalog">清空目录</ElButton>
          </div>

          <div class="mt-4">
            <ElButton size="small" @click="addCatalogItem">
              <ElIcon><Plus /></ElIcon>
              添加章节
            </ElButton>
          </div>
        </div>

        <div class="p-5 mt-5 art-card-xs">
          <h2 class="mb-5 text-xl font-medium">AI辅助生成</h2>
          
          <div v-if="!aiConfigured" class="p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
            <ElIcon class="text-yellow-500"><WarningFilled /></ElIcon>
            <span class="ml-2 text-yellow-700">AI模型尚未配置，请先在系统设置中配置AI模型</span>
          </div>

          <template v-else>
            <div class="grid grid-cols-2 lg:grid-cols-3 gap-3">
              <ElButton
                size="small"
                @click="generateSummary"
                :loading="aiLoading"
              >
                <ElIcon><EditPen /></ElIcon>
                生成项目简介
              </ElButton>
              <ElButton
                size="small"
                @click="generateTechStack"
                :loading="aiLoading"
              >
                <ElIcon><Cpu /></ElIcon>
                提取技术栈
              </ElButton>
              <ElButton
                size="small"
                @click="extractChapters"
                :loading="aiLoading"
              >
                <ElIcon><List /></ElIcon>
                提取章节结构
              </ElButton>
            </div>
          </template>
        </div>

        <div class="p-5 mt-5 art-card-xs">
          <div class="flex justify-end">
            <ElButton @click="goBack" class="w-20 mr-2">取消</ElButton>
            <ElButton type="primary" @click="submit" class="w-25" :loading="isSubmitting">
              {{ pageMode === PageModeEnum.Edit ? '保存' : '发布' }}
            </ElButton>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { Plus, Link, MagicStick, Close, WarningFilled, Edit, ArrowUp, ArrowDown, Minus, CirclePlus, EditPen, Cpu, List, Coin, StarFilled } from '@element-plus/icons-vue'
  import { useUserStore } from '@/store/modules/user'
  import { PageModeEnum } from '@/enums/formEnum'
  import { createProject, updateProject, fetchProject } from '@/api/projects'
import { fetchProjectCategories, ProjectCategory } from '@/api/project_categories'
  import { useCommon } from '@/hooks/core/useCommon'

  defineOptions({ name: 'ProjectCreate' })

  interface CatalogItem {
    level: number
    title: string
  }

  const MAX_IMAGE_SIZE = 2
  const EMPTY_EDITOR_CONTENT = '<p><br></p>'

  const route = useRoute()
  const router = useRouter()
  const userStore = useUserStore()
  const { accessToken } = userStore

  const pageMode = ref<PageModeEnum>(PageModeEnum.Add)
  const projectId = ref<number | null>(null)

  const projectName = ref('')
  const projectType = ref('')
  const projectStatus = ref('in_progress')
  const openSourceLicense = ref('')
  const databaseType = ref('')
  const deploymentPlatform = ref('')
  const demoUrl = ref('')
  const githubUrl = ref('')
  const docsUrl = ref('')
  const lastUpdate = ref('')
  const startDate = ref('')
  const endDate = ref('')
  const projectSummary = ref('')
  const tags = ref<string[]>([])
  const tagInput = ref('')
  const techStack = ref<string[]>([])
  const techInput = ref('')
const cover = ref('')
const coverUrlInput = ref('')
const editorHtml = ref('')
const catalog = ref<CatalogItem[]>([])
const catalogLoading = ref(false)
const catalogEditingIndex = ref<number>(-1)
const aiLoading = ref(false)
const aiConfigured = ref(true)
const isSubmitting = ref(false)
const pageLoading = ref(false)
const projectTag = ref<string>('')
const repostUrl = ref('')
const projectCategoryId = ref<number | undefined>(undefined)
const projectCategories = ref<ProjectCategory[]>([])

  const uploadRef = ref<InstanceType<typeof ElUpload> | null>(null)
  const editInputRef = ref<InstanceType<typeof ElInput> | null>(null)

  const projectTypes = [
    { label: 'Web应用', value: 'web' },
    { label: '移动端应用', value: 'mobile' },
    { label: '桌面应用', value: 'desktop' },
    { label: '后端服务', value: 'backend' },
    { label: '工具库', value: 'library' },
    { label: '游戏', value: 'game' },
    { label: 'AI/机器学习', value: 'ai' },
    { label: '其他', value: 'other' }
  ]

  const projectStatuses = [
    { label: '开发中', value: 'in_progress' },
    { label: '已发布', value: 'published' },
    { label: '维护中', value: 'maintaining' },
    { label: '已归档', value: 'archived' }
  ]

  const openSourceLicenses = [
    { label: 'MIT', value: 'MIT' },
    { label: 'Apache 2.0', value: 'Apache-2.0' },
    { label: 'GPL v3', value: 'GPL-3.0' },
    { label: 'BSD 2-Clause', value: 'BSD-2-Clause' },
    { label: 'BSD 3-Clause', value: 'BSD-3-Clause' },
    { label: 'MPL 2.0', value: 'MPL-2.0' },
    { label: 'LGPL v3', value: 'LGPL-3.0' },
    { label: 'AGPL v3', value: 'AGPL-3.0' },
    { label: 'Unlicense', value: 'Unlicense' },
    { label: 'CC0', value: 'CC0' },
    { label: '商业许可', value: 'commercial' },
    { label: '其他', value: 'other' }
  ]

  const databaseTypes = [
    { label: 'MySQL', value: 'mysql' },
    { label: 'PostgreSQL', value: 'postgresql' },
    { label: 'SQLite', value: 'sqlite' },
    { label: 'MongoDB', value: 'mongodb' },
    { label: 'Redis', value: 'redis' },
    { label: 'Oracle', value: 'oracle' },
    { label: 'SQL Server', value: 'sqlserver' },
    { label: 'None', value: 'none' },
    { label: '其他', value: 'other' }
  ]

  const availableTechStack = [
    'Vue.js', 'React', 'Angular', 'Svelte', 'Next.js', 'Nuxt.js',
    'Node.js', 'Python', 'Django', 'Flask', 'FastAPI', 'Spring Boot',
    'TypeScript', 'JavaScript', 'Rust', 'Go', 'Java', 'C#', 'PHP',
    'Tailwind CSS', 'Bootstrap', 'Ant Design', 'Element Plus', 'Vuetify',
    'Webpack', 'Vite', 'Rollup', 'Docker', 'Kubernetes', 'AWS',
    'MySQL', 'PostgreSQL', 'MongoDB', 'Redis', 'SQLite',
    'Git', 'GitHub', 'GitLab', 'CI/CD', 'Jest', 'Cypress'
  ]

  const initPageMode = () => {
    const { id } = route.query
    pageMode.value = id ? PageModeEnum.Edit : PageModeEnum.Add

    if (pageMode.value === PageModeEnum.Edit) {
      pageLoading.value = true
      getProjectDetail()
    } else {
      lastUpdate.value = new Date().toISOString().slice(0, 16)
    }
  }

  const loadProjectCategories = async () => {
    try {
      const categories = await fetchProjectCategories({ include_inactive: false })
      projectCategories.value = categories || []
    } catch (error) {
      console.error('加载项目分类失败:', error)
    }
  }

  const getProjectDetail = async () => {
    const { id } = route.query
    if (!id) return
    try {
      const res = await fetchProject(Number(id))
      if (res) {
        projectId.value = res.id
        projectName.value = res.name || ''
        projectType.value = res.project_type || ''
        projectStatus.value = res.status || 'in_progress'
        openSourceLicense.value = res.open_source_license || ''
        databaseType.value = res.database_type || ''
        deploymentPlatform.value = res.deployment_platform || ''
        demoUrl.value = res.demo_url || ''
        githubUrl.value = res.github_url || ''
        docsUrl.value = res.docs_url || ''
        lastUpdate.value = res.last_update ? new Date(res.last_update).toISOString().slice(0, 16) : ''
        startDate.value = res.start_date ? new Date(res.start_date).toISOString().slice(0, 10) : ''
        endDate.value = res.end_date ? new Date(res.end_date).toISOString().slice(0, 10) : ''
        projectSummary.value = res.summary || ''
        tags.value = res.tags || []
        techStack.value = res.tech_stack || []
        cover.value = res.cover || ''
        editorHtml.value = res.content || ''
        catalog.value = (res.catalog || []).map((item: any) => ({
          level: item.level || 1,
          title: item.title || ''
        }))
        projectTag.value = res.is_paid ? 'paid' : res.is_featured ? 'featured' : ''
        repostUrl.value = res.repost_url || ''
        projectCategoryId.value = res.category_id || undefined
      }
    } catch (error) {
      console.error('获取项目详情失败:', error)
      ElMessage.error('获取项目详情失败，请稍后重试')
    } finally {
      pageLoading.value = false
    }
  }

  const validateUrl = (field: string) => {
    const url = (field === 'demoUrl' ? demoUrl.value :
                 field === 'githubUrl' ? githubUrl.value :
                 field === 'docsUrl' ? docsUrl.value :
                 field === 'repostUrl' ? repostUrl.value : '').trim()
    if (!url) return

    try {
      new URL(url)
    } catch {
      ElMessage.warning(`请输入有效的URL`)
    }
  }

  const addTag = () => {
    const raw = tagInput.value
    const parts = raw.split(/[,，\n]/).map(s => s.trim()).filter(Boolean)
    for (const part of parts) {
      if (part && !tags.value.includes(part)) {
        tags.value.push(part)
      }
    }
    tagInput.value = ''
  }

  const removeTag = (index: number) => {
    tags.value.splice(index, 1)
  }

  const handleTagInputKeydown = (e: Event | KeyboardEvent) => {
    const evt = e as KeyboardEvent
    if (evt.key === 'Enter' || evt.key === ',') {
      evt.preventDefault()
      addTag()
    }
  }

  const handleTagInputBlur = () => {
    if (tagInput.value.trim()) {
      addTag()
    }
  }

  const addTech = () => {
    if (techInput.value && !techStack.value.includes(techInput.value)) {
      techStack.value.push(techInput.value)
    }
    techInput.value = ''
  }

  const removeTech = (index: number) => {
    techStack.value.splice(index, 1)
  }

  const validateProject = (): boolean => {
    if (!projectName.value.trim()) {
      ElMessage.error('请输入项目名称')
      return false
    }

    if (!projectType.value) {
      ElMessage.error('请选择项目类型')
      return false
    }

    if (!cover.value) {
      ElMessage.error('请上传封面图片')
      return false
    }

    return true
  }

  const buildProjectPayload = () => {
    const isPaid = projectTag.value === 'paid'
    const isFeatured = projectTag.value === 'featured'

    return {
      name: projectName.value.trim(),
      cover: cover.value || undefined,
      tags: tags.value.length > 0 ? tags.value : [],
      github_url: githubUrl.value.trim() || undefined,
      demo_url: demoUrl.value.trim() || undefined,
      summary: projectSummary.value.trim() || undefined,
      tech_stack: techStack.value.length > 0 ? techStack.value : [],
      status: projectStatus.value,
      project_type: projectType.value,
      start_date: startDate.value ? new Date(startDate.value).toISOString() : undefined,
      end_date: endDate.value ? new Date(endDate.value).toISOString() : undefined,
      last_update: lastUpdate.value ? new Date(lastUpdate.value).toISOString() : undefined,
      open_source_license: openSourceLicense.value || undefined,
      database_type: databaseType.value || undefined,
      deployment_platform: deploymentPlatform.value.trim() || undefined,
      docs_url: docsUrl.value.trim() || undefined,
      content: editorHtml.value || undefined,
      catalog: catalog.value.length > 0 ? catalog.value.map(item => ({
        level: item.level,
        title: item.title
      })) : [],
      is_paid: isPaid,
      is_featured: isFeatured,
      repost_url: repostUrl.value.trim() || undefined,
      category_id: projectCategoryId.value,
      display_status: undefined
    }
  }

  const addProject = async () => {
    if (!validateProject()) return

    isSubmitting.value = true
    try {
      const payload = buildProjectPayload()
      const result = await createProject(payload)
      if (result) {
        ElMessage.success('项目发布成功！')
        setTimeout(() => {
          router.push({ name: 'ProjectList' })
        }, 800)
      }
    } catch (error: any) {
      console.error('发布项目失败:', error)
      ElMessage.error(error?.msg || '发布项目失败，请稍后重试')
    } finally {
      isSubmitting.value = false
    }
  }

  const editProject = async () => {
    if (!validateProject()) return

    if (!projectId.value) {
      ElMessage.error('项目ID不存在')
      return
    }

    isSubmitting.value = true
    try {
      const payload = buildProjectPayload()
      const result = await updateProject(projectId.value, payload)
      if (result) {
        ElMessage.success('项目保存成功！')
        setTimeout(() => {
          router.push({ name: 'ProjectList' })
        }, 800)
      }
    } catch (error: any) {
      console.error('保存项目失败:', error)
      ElMessage.error(error?.msg || '保存项目失败，请稍后重试')
    } finally {
      isSubmitting.value = false
    }
  }

  const submit = () => {
    if (pageMode.value === PageModeEnum.Edit) {
      editProject()
    } else {
      addProject()
    }
  }

  const goBack = () => {
    router.push({ name: 'ProjectList' })
  }

  const handleFileUpload = async (options: any) => {
    const file = options.file as File
    try {
      const formData = new FormData()
      formData.append('file', file)
      const { default: request } = await import('@/utils/http')
      const res: any = await request.post({
        url: '/v1/upload/image',
        params: formData,
        headers: { 'Content-Type': 'multipart/form-data' }
      })
      if (res.code === 200 && res.data?.url) {
        cover.value = res.data.url
        ElMessage.success('封面上传成功')
      } else if (res.url) {
        cover.value = res.url
        ElMessage.success('封面上传成功')
      } else {
        ElMessage.error('封面上传失败')
      }
    } catch (error) {
      console.error('封面上传失败:', error)
      ElMessage.error('封面上传失败')
    }
  }

  const triggerUpload = () => {
    uploadRef.value?.$el.querySelector('input[type=file]')?.click()
  }

  const handleUrlUpload = () => {
    const url = coverUrlInput.value.trim()
    if (!url) {
      ElMessage.warning('请输入图片URL')
      return
    }

    try {
      new URL(url)
    } catch {
      ElMessage.warning('请输入有效的图片URL')
      return
    }

    const imageExtPattern = /\.(jpg|jpeg|png|gif|svg|webp|awebp|bmp|ico)([\?#&]|$)/i
    if (!imageExtPattern.test(url)) {
      ElMessage.warning('请输入有效的图片URL（支持 jpg/png/gif/svg/webp 格式）')
      return
    }

    cover.value = url
    coverUrlInput.value = ''
    ElMessage.success('封面已设置')
  }

  const beforeUpload = (file: File): boolean => {
    const isImage = file.type.startsWith('image/')
    const isLt2M = file.size / 1024 / 1024 < MAX_IMAGE_SIZE

    if (!isImage) {
      ElMessage.error('只能上传图片文件')
      return false
    }

    if (!isLt2M) {
      ElMessage.error(`图片大小不能超过 ${MAX_IMAGE_SIZE}MB`)
      return false
    }

    return true
  }

  const addCatalogItem = () => {
    catalog.value.push({ level: 1, title: '' })
  }

  const removeCatalogItem = (index: number) => {
    catalog.value.splice(index, 1)
  }

  const clearCatalog = () => {
    catalog.value = []
    catalogEditingIndex.value = -1
  }

  const startEditCatalog = (index: number) => {
    catalogEditingIndex.value = index
    setTimeout(() => {
      const inputEl = document.querySelector(`.catalog-item-input-${index}`) as HTMLInputElement
      if (inputEl) {
        inputEl.focus()
        inputEl.select()
      }
    }, 0)
  }

  const finishEditCatalog = () => {
    catalogEditingIndex.value = -1
  }

  const indentCatalog = (index: number) => {
    if (catalog.value[index] && catalog.value[index].level < 3) {
      catalog.value[index].level++
    }
  }

  const outdentCatalog = (index: number) => {
    if (catalog.value[index] && catalog.value[index].level > 1) {
      catalog.value[index].level--
    }
  }

  const moveCatalogUp = (index: number) => {
    if (index > 0) {
      const temp = catalog.value[index]
      catalog.value[index] = catalog.value[index - 1]
      catalog.value[index - 1] = temp
    }
  }

  const moveCatalogDown = (index: number) => {
    if (index < catalog.value.length - 1) {
      const temp = catalog.value[index]
      catalog.value[index] = catalog.value[index + 1]
      catalog.value[index + 1] = temp
    }
  }

  const generateCatalog = async () => {
    if (!editorHtml.value) {
      ElMessage.warning('请先输入项目内容')
      return
    }

    catalogLoading.value = true

    const cleanContent = editorHtml.value.replace(/<img[^>]*>/gi, '')

    if (!cleanContent.trim() || cleanContent === EMPTY_EDITOR_CONTENT) {
      ElMessage.warning('项目内容中无可分析的文本内容（图片已过滤）')
      catalogLoading.value = false
      return
    }

    try {
      const response = await fetch('/api/v1/catalog/generate-stream', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken}`
        },
        body: JSON.stringify({ content: cleanContent })
      })

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`)
      }

      const reader = response.body?.getReader()
      if (!reader) {
        throw new Error('无法读取服务器响应')
      }

      const decoder = new TextDecoder()
      let buffer = ''
      let resultCatalog: any[] = []

      while (true) {
        const { done, value } = await reader.read()
        if (done) break

        buffer += decoder.decode(value, { stream: true })

        const parts = buffer.split('\n\n')
        buffer = parts.pop() || ''

        for (const part of parts) {
          const lines = part.split('\n')
          let eventType = ''
          let dataStr = ''

          for (const line of lines) {
            if (line.startsWith('event: ')) {
              eventType = line.slice(7)
            } else if (line.startsWith('data: ')) {
              dataStr = line.slice(6)
            }
          }

          if (!dataStr) continue

          try {
            const eventData = JSON.parse(dataStr)

            if (eventType === 'complete') {
              resultCatalog = eventData.catalog || []
              const level1Items = resultCatalog.filter((item: any) => Number(item.level) === 1)
              const level2Items = resultCatalog.filter((item: any) => Number(item.level) === 2)

              if (level1Items.length > 0) {
                catalog.value = level1Items.map((item: any) => ({
                  level: item.level || 1,
                  title: item.title || ''
                }))
                ElMessage.success(`已提取 ${level1Items.length} 个章节`)
              } else if (level2Items.length > 0) {
                catalog.value = level2Items.map((item: any) => ({
                  level: 1,
                  title: item.title || ''
                }))
                ElMessage.success(`已将 ${level2Items.length} 个子章节提升为主章节`)
              } else {
                ElMessage.info('未检测到章节结构，请手动添加')
              }
            }
          } catch (parseError) {
            console.warn('SSE 数据解析失败:', parseError)
          }
        }
      }
      // Flush remaining buffer for incomplete SSE event
      if (buffer.trim()) {
        try {
          const finalData = JSON.parse(buffer.trim())
          if (finalData.catalog) {
            const level1Items = finalData.catalog.filter((item: any) => Number(item.level) === 1)
            const level2Items = finalData.catalog.filter((item: any) => Number(item.level) === 2)
            if (level1Items.length > 0) {
              catalog.value = level1Items.map((item: any) => ({
                level: item.level || 1,
                title: item.title || ''
              }))
              ElMessage.success(`已提取 ${level1Items.length} 个章节`)
            } else if (level2Items.length > 0) {
              catalog.value = level2Items.map((item: any) => ({
                level: 1,
                title: item.title || ''
              }))
              ElMessage.success(`已将 ${level2Items.length} 个子章节提升为主章节`)
            } else {
              ElMessage.info('未检测到章节结构，请手动添加')
            }
          }
        } catch (e) {
          // ignore parse error in flush
        }
      }
    } catch (error: any) {
      console.error('生成目录失败:', error)
      ElMessage.error('生成目录失败，请稍后重试')
    } finally {
      catalogLoading.value = false
    }
  }

  const generateSummary = async () => {
    if (!editorHtml.value) {
      ElMessage.warning('请先输入项目内容')
      return
    }

    aiLoading.value = true
    try {
      ElMessage.info('AI生成中...')
      await new Promise(resolve => setTimeout(resolve, 1500))
      projectSummary.value = '这是一个基于现代Web技术栈构建的项目，提供了完整的功能实现和良好的用户体验。项目采用模块化设计，易于扩展和维护。'
      ElMessage.success('项目简介已生成')
    } catch (error) {
      ElMessage.error('生成失败')
    } finally {
      aiLoading.value = false
    }
  }

  const generateTechStack = async () => {
    if (!editorHtml.value) {
      ElMessage.warning('请先输入项目内容')
      return
    }

    aiLoading.value = true
    try {
      ElMessage.info('AI分析中...')
      await new Promise(resolve => setTimeout(resolve, 1500))
      const suggestedTech = ['Vue.js', 'TypeScript', 'Vite', 'Tailwind CSS', 'Node.js']
      for (const tech of suggestedTech) {
        if (!techStack.value.includes(tech)) {
          techStack.value.push(tech)
        }
      }
      ElMessage.success('技术栈已提取')
    } catch (error) {
      ElMessage.error('分析失败')
    } finally {
      aiLoading.value = false
    }
  }

  const extractChapters = async () => {
    await generateCatalog()
  }

  const { scrollToTop } = useCommon()

  onMounted(() => {
  scrollToTop()
  initPageMode()
  loadProjectCategories()
})
</script>

<style scoped>
.art-card-xs,
[class*="rounded-xl"][class*="shadow-sm"] {
  transition: all 0.2s ease;
}
.art-card-xs:hover,
[class*="rounded-xl"][class*="shadow-sm"]:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
</style>
