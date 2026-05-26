<template>
  <div class="category-page">
    <ArtBreadcrumb :items="breadcrumbItems" />

    <ElCard class="rounded-xl shadow-sm border border-[var(--art-card-border)]">
      <ElTabs v-model="activeTab" @tab-click="handleTabSwitch">
        <ElTabPane label="文章分类" name="article">
          <template #label>
            <span class="flex items-center gap-1">
              <ElIcon><FolderOpened /></ElIcon>
              文章分类
            </span>
          </template>

          <div class="flex justify-between items-center mb-4">
            <ElForm :inline="true" :model="articleSearchForm">
              <ElFormItem label="分类名称">
                <ElInput v-model="articleSearchForm.name" placeholder="输入分类名称" clearable @keyup.enter="handleArticleSearch" />
              </ElFormItem>
              <ElFormItem label="状态">
                <ElSelect v-model="articleSearchForm.is_active" placeholder="选择状态" clearable style="width: 120px">
                  <ElOption label="全部" :value="undefined" />
                  <ElOption label="正常" :value="true" />
                  <ElOption label="已暂停" :value="false" />
                </ElSelect>
              </ElFormItem>
              <ElFormItem>
                <ElButton type="primary" @click="handleArticleSearch">搜索</ElButton>
                <ElButton @click="handleArticleReset">重置</ElButton>
              </ElFormItem>
            </ElForm>
            <ElButton type="primary" @click="handleCreate('article')" v-auth="'add'">
              <ElIcon class="mr-1"><Plus /></ElIcon>
              新增分类
            </ElButton>
          </div>

          <ElTable :data="articleCategories" v-loading="articleLoading" stripe>
            <ElTableColumn prop="id" label="ID" width="80" />
            <ElTableColumn prop="name" label="名称" min-width="150">
              <template #default="{ row }">
                <div :class="{ 'text-gray-400': !row.is_active }">
                  {{ row.name }}
                </div>
              </template>
            </ElTableColumn>
            <ElTableColumn prop="description" label="介绍" min-width="300">
              <template #default="{ row }">
                <div :class="{ 'text-gray-400': !row.is_active }">
                  {{ row.description || '-' }}
                </div>
              </template>
            </ElTableColumn>
            <ElTableColumn prop="is_active" label="状态" width="100" align="center">
              <template #default="{ row }">
                <ElTag :type="row.is_active ? 'success' : 'danger'" size="small">
                  {{ row.is_active ? '正常' : '已暂停' }}
                </ElTag>
              </template>
            </ElTableColumn>
            <ElTableColumn prop="created_at" label="创建时间" width="180">
              <template #default="{ row }">
                {{ formatDate(row.created_at) }}
              </template>
            </ElTableColumn>
            <ElTableColumn label="操作" width="160" fixed="right" align="center">
              <template #default="{ row }">
                <div class="flex gap-2 justify-center">
                  <ArtButtonTable type="edit" @click="handleEdit(row, 'article')" v-auth="'edit'" :iconClass="!row.is_active ? 'opacity-50 cursor-not-allowed' : ''" :disabled="!row.is_active" />
                  <ArtButtonTable :icon="row.is_active ? 'ri:pause-circle-line' : 'ri:play-circle-line'" :iconClass="row.is_active ? 'bg-warning/12 text-warning' : 'bg-success/12 text-success'" @click="handleToggleStatus(row, 'article')" v-auth="'edit'" />
                  <ArtButtonTable type="delete" @click="handleDelete(row, 'article')" v-auth="'delete'" />
                </div>
              </template>
            </ElTableColumn>
          </ElTable>
        </ElTabPane>

        <ElTabPane label="项目分类" name="project">
          <template #label>
            <span class="flex items-center gap-1">
              <ElIcon><Coin /></ElIcon>
              项目分类
            </span>
          </template>

          <div class="flex justify-between items-center mb-4">
            <ElForm :inline="true" :model="projectSearchForm">
              <ElFormItem label="分类名称">
                <ElInput v-model="projectSearchForm.name" placeholder="输入分类名称" clearable @keyup.enter="handleProjectSearch" />
              </ElFormItem>
              <ElFormItem label="状态">
                <ElSelect v-model="projectSearchForm.is_active" placeholder="选择状态" clearable style="width: 120px">
                  <ElOption label="全部" :value="undefined" />
                  <ElOption label="正常" :value="true" />
                  <ElOption label="已暂停" :value="false" />
                </ElSelect>
              </ElFormItem>
              <ElFormItem>
                <ElButton type="primary" @click="handleProjectSearch">搜索</ElButton>
                <ElButton @click="handleProjectReset">重置</ElButton>
              </ElFormItem>
            </ElForm>
            <ElButton type="primary" @click="handleCreate('project')" v-auth="'add'">
              <ElIcon class="mr-1"><Plus /></ElIcon>
              新增分类
            </ElButton>
          </div>

          <ElTable :data="projectCategories" v-loading="projectLoading" stripe>
            <ElTableColumn prop="id" label="ID" width="80" />
            <ElTableColumn prop="name" label="名称" min-width="150">
              <template #default="{ row }">
                <div :class="{ 'text-gray-400': !row.is_active }">
                  {{ row.name }}
                </div>
              </template>
            </ElTableColumn>
            <ElTableColumn prop="description" label="介绍" min-width="300">
              <template #default="{ row }">
                <div :class="{ 'text-gray-400': !row.is_active }">
                  {{ row.description || '-' }}
                </div>
              </template>
            </ElTableColumn>
            <ElTableColumn prop="is_active" label="状态" width="100" align="center">
              <template #default="{ row }">
                <ElTag :type="row.is_active ? 'success' : 'danger'" size="small">
                  {{ row.is_active ? '正常' : '已暂停' }}
                </ElTag>
              </template>
            </ElTableColumn>
            <ElTableColumn prop="created_at" label="创建时间" width="180">
              <template #default="{ row }">
                {{ formatDate(row.created_at) }}
              </template>
            </ElTableColumn>
            <ElTableColumn label="操作" width="160" fixed="right" align="center">
              <template #default="{ row }">
                <div class="flex gap-2 justify-center">
                  <ArtButtonTable type="edit" @click="handleEdit(row, 'project')" v-auth="'edit'" :iconClass="!row.is_active ? 'opacity-50 cursor-not-allowed' : ''" :disabled="!row.is_active" />
                  <ArtButtonTable :icon="row.is_active ? 'ri:pause-circle-line' : 'ri:play-circle-line'" :iconClass="row.is_active ? 'bg-warning/12 text-warning' : 'bg-success/12 text-success'" @click="handleToggleStatus(row, 'project')" v-auth="'edit'" />
                  <ArtButtonTable type="delete" @click="handleDelete(row, 'project')" v-auth="'delete'" />
                </div>
              </template>
            </ElTableColumn>
          </ElTable>
        </ElTabPane>

        <ElTabPane label="友链分类" name="friend-link">
          <template #label>
            <span class="flex items-center gap-1">
              <ElIcon><Link /></ElIcon>
              友链分类
            </span>
          </template>

          <div class="flex justify-between items-center mb-4">
            <ElForm :inline="true" :model="friendLinkSearchForm">
              <ElFormItem label="分类名称">
                <ElInput v-model="friendLinkSearchForm.name" placeholder="输入分类名称" clearable @keyup.enter="handleFriendLinkSearch" />
              </ElFormItem>
              <ElFormItem label="状态">
                <ElSelect v-model="friendLinkSearchForm.is_active" placeholder="选择状态" clearable style="width: 120px">
                  <ElOption label="全部" :value="undefined" />
                  <ElOption label="正常" :value="true" />
                  <ElOption label="已暂停" :value="false" />
                </ElSelect>
              </ElFormItem>
              <ElFormItem>
                <ElButton type="primary" @click="handleFriendLinkSearch">搜索</ElButton>
                <ElButton @click="handleFriendLinkReset">重置</ElButton>
              </ElFormItem>
            </ElForm>
            <ElButton type="primary" @click="handleCreate('friend-link')" v-auth="'add'">
              <ElIcon class="mr-1"><Plus /></ElIcon>
              新增分类
            </ElButton>
          </div>

          <ElTable :data="friendLinkCategories" v-loading="friendLinkLoading" stripe>
            <ElTableColumn prop="id" label="ID" width="80" />
            <ElTableColumn prop="name" label="名称" min-width="150">
              <template #default="{ row }">
                <div :class="{ 'text-gray-400': !row.is_active }">
                  {{ row.name }}
                </div>
              </template>
            </ElTableColumn>
            <ElTableColumn prop="description" label="介绍" min-width="300">
              <template #default="{ row }">
                <div :class="{ 'text-gray-400': !row.is_active }">
                  {{ row.description || '-' }}
                </div>
              </template>
            </ElTableColumn>
            <ElTableColumn prop="is_active" label="状态" width="100" align="center">
              <template #default="{ row }">
                <ElTag :type="row.is_active ? 'success' : 'danger'" size="small">
                  {{ row.is_active ? '正常' : '已暂停' }}
                </ElTag>
              </template>
            </ElTableColumn>
            <ElTableColumn prop="created_at" label="创建时间" width="180">
              <template #default="{ row }">
                {{ formatDate(row.created_at) }}
              </template>
            </ElTableColumn>
            <ElTableColumn label="操作" width="160" fixed="right" align="center">
              <template #default="{ row }">
                <div class="flex gap-2 justify-center">
                  <ArtButtonTable type="edit" @click="handleEdit(row, 'friend-link')" v-auth="'edit'" :iconClass="!row.is_active ? 'opacity-50 cursor-not-allowed' : ''" :disabled="!row.is_active" />
                  <ArtButtonTable :icon="row.is_active ? 'ri:pause-circle-line' : 'ri:play-circle-line'" :iconClass="row.is_active ? 'bg-warning/12 text-warning' : 'bg-success/12 text-success'" @click="handleToggleStatus(row, 'friend-link')" v-auth="'edit'" />
                  <ArtButtonTable type="delete" @click="handleDelete(row, 'friend-link')" v-auth="'delete'" />
                </div>
              </template>
            </ElTableColumn>
          </ElTable>
        </ElTabPane>
      </ElTabs>
    </ElCard>

    <ElDialog v-model="dialogVisible" :title="dialogTitle" width="500px" @close="handleDialogClose" class="category-dialog">
      <ElForm ref="formRef" :model="formData" :rules="formRules" label-width="80px">
        <ElFormItem label="分类名称" prop="name">
          <ElInput v-model="formData.name" placeholder="请输入分类名称" maxlength="50" show-word-limit />
        </ElFormItem>
        <ElFormItem label="介绍" prop="description">
          <ElInput v-model="formData.description" type="textarea" placeholder="请输入分类介绍（可选）" :rows="4" maxlength="500" show-word-limit />
        </ElFormItem>
      </ElForm>
      <template #footer>
        <div class="flex justify-end gap-2">
          <ElButton @click="dialogVisible = false" size="small">取消</ElButton>
          <ElButton type="primary" @click="handleSubmit" :loading="submitLoading" size="small">确定</ElButton>
        </div>
      </template>
    </ElDialog>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage, ElMessageBox, FormInstance, FormRules, TabsPaneContext } from 'element-plus'
import { Plus, FolderOpened, Coin, Link } from '@element-plus/icons-vue'
import ArtBreadcrumb from '@/components/core/layouts/art-breadcrumb/index.vue'
import ArtButtonTable from '@/components/core/forms/art-button-table/index.vue'
import {
  fetchCategories,
  createCategory,
  updateCategory,
  toggleCategoryStatus,
  deleteCategory,
  Category
} from '@/api/taxonomy'
import {
  fetchProjectCategories,
  createProjectCategory,
  updateProjectCategory,
  toggleProjectCategoryStatus,
  deleteProjectCategory,
  ProjectCategory
} from '@/api/project_categories'
import {
  fetchFriendLinkCategories as fetchFLCategories,
  createFriendLinkCategory,
  updateFriendLinkCategory,
  toggleFriendLinkCategoryStatus,
  deleteFriendLinkCategory,
  FriendLinkCategory
} from '@/api/friend_link_categories'

defineOptions({ name: 'CategoryManagement' })

const router = useRouter()

const breadcrumbItems = [
  { label: '首页', path: '/content/articles' },
  { label: '内容管理', path: '/content' },
  { label: '分类管理' }
]

const activeTab = ref('article')

const articleLoading = ref(false)
const projectLoading = ref(false)
const friendLinkLoading = ref(false)
const submitLoading = ref(false)
const dialogVisible = ref(false)
const dialogTitle = ref('新增分类')
const dialogType = ref<'article' | 'project' | 'friend-link'>('article')
const isEdit = ref(false)
const currentId = ref<number>()
const editingRow = ref<any>(null)

const articleCategories = ref<Category[]>([])
const projectCategories = ref<ProjectCategory[]>([])
const friendLinkCategories = ref<FriendLinkCategory[]>([])

const articleSearchForm = reactive({
  name: '',
  is_active: undefined as boolean | undefined
})

const projectSearchForm = reactive({
  name: '',
  is_active: undefined as boolean | undefined
})

const friendLinkSearchForm = reactive({
  name: '',
  is_active: undefined as boolean | undefined
})

const formRef = ref<FormInstance>()
const formData = reactive({
  name: '',
  description: ''
})

const formRules: FormRules = {
  name: [
    { required: true, message: '请输入分类名称', trigger: 'blur' },
    { min: 1, max: 50, message: '长度在 1 到 50 个字符', trigger: 'blur' }
  ],
  description: [
    { max: 500, message: '长度不能超过 500 个字符', trigger: 'blur' }
  ]
}

const loadArticleCategories = async () => {
  articleLoading.value = true
  try {
    const data = await fetchCategories({
      skip: 0,
      limit: 100,
      include_inactive: true
    })
    let filteredData = data || []
    if (articleSearchForm.name) {
      filteredData = filteredData.filter(c =>
        c.name.toLowerCase().includes(articleSearchForm.name.toLowerCase())
      )
    }
    if (articleSearchForm.is_active !== undefined) {
      filteredData = filteredData.filter(c => c.is_active === articleSearchForm.is_active)
    }
    articleCategories.value = filteredData
  } catch (error) {
    console.error('加载文章分类失败:', error)
    ElMessage.error('加载文章分类失败')
  } finally {
    articleLoading.value = false
  }
}

const loadProjectCategories = async () => {
  projectLoading.value = true
  try {
    const data = await fetchProjectCategories({
      skip: 0,
      limit: 100,
      include_inactive: true
    })
    let filteredData = data || []
    if (projectSearchForm.name) {
      filteredData = filteredData.filter(c =>
        c.name.toLowerCase().includes(projectSearchForm.name.toLowerCase())
      )
    }
    if (projectSearchForm.is_active !== undefined) {
      filteredData = filteredData.filter(c => c.is_active === projectSearchForm.is_active)
    }
    projectCategories.value = filteredData
  } catch (error) {
    console.error('加载项目分类失败:', error)
    ElMessage.error('加载项目分类失败')
  } finally {
    projectLoading.value = false
  }
}

const loadFriendLinkCategories = async () => {
  friendLinkLoading.value = true
  try {
    const data = await fetchFLCategories({
      skip: 0,
      limit: 100,
      include_inactive: true
    })
    let filteredData = data || []
    if (friendLinkSearchForm.name) {
      filteredData = filteredData.filter(c =>
        c.name.toLowerCase().includes(friendLinkSearchForm.name.toLowerCase())
      )
    }
    if (friendLinkSearchForm.is_active !== undefined) {
      filteredData = filteredData.filter(c => c.is_active === friendLinkSearchForm.is_active)
    }
    friendLinkCategories.value = filteredData
  } catch (error) {
    console.error('加载友链分类失败:', error)
    ElMessage.error('加载友链分类失败')
  } finally {
    friendLinkLoading.value = false
  }
}

const handleTabSwitch = (tab: TabsPaneContext) => {
  if (tab.paneName === 'article' && articleCategories.value.length === 0) {
    loadArticleCategories()
  } else if (tab.paneName === 'project' && projectCategories.value.length === 0) {
    loadProjectCategories()
  } else if (tab.paneName === 'friend-link' && friendLinkCategories.value.length === 0) {
    loadFriendLinkCategories()
  }
}

const handleArticleSearch = () => {
  loadArticleCategories()
}

const handleArticleReset = () => {
  articleSearchForm.name = ''
  articleSearchForm.is_active = undefined
  loadArticleCategories()
}

const handleProjectSearch = () => {
  loadProjectCategories()
}

const handleProjectReset = () => {
  projectSearchForm.name = ''
  projectSearchForm.is_active = undefined
  loadProjectCategories()
}

const handleFriendLinkSearch = () => {
  loadFriendLinkCategories()
}

const handleFriendLinkReset = () => {
  friendLinkSearchForm.name = ''
  friendLinkSearchForm.is_active = undefined
  loadFriendLinkCategories()
}

const handleView = (row: any, type: 'article' | 'project' | 'friend-link') => {
  if (type === 'article') {
    router.push('/content/articles')
  } else if (type === 'friend-link') {
    router.push('/friend-links/list')
  } else {
    router.push('/projects/list')
  }
}

const handleCreate = (type: 'article' | 'project' | 'friend-link') => {
  dialogType.value = type
  const typeLabel = type === 'article' ? '文章' : type === 'project' ? '项目' : '友链'
  dialogTitle.value = `新增${typeLabel}分类`
  isEdit.value = false
  currentId.value = undefined
  editingRow.value = null
  formData.name = ''
  formData.description = ''
  dialogVisible.value = true
}

const handleEdit = (row: any, type: 'article' | 'project' | 'friend-link') => {
  dialogType.value = type
  const typeLabel = type === 'article' ? '文章' : type === 'project' ? '项目' : '友链'
  dialogTitle.value = `修改${typeLabel}分类`
  isEdit.value = true
  currentId.value = row.id
  editingRow.value = row
  formData.name = row.name
  formData.description = row.description || ''
  dialogVisible.value = true
}

const handleToggleStatus = async (row: any, type: 'article' | 'project' | 'friend-link') => {
  const action = row.is_active ? '暂停' : '启用'
  const confirmText = row.is_active
    ? `确定要${action}分类"${row.name}"吗？${action}后该分类将不会在前台显示。`
    : `确定要${action}分类"${row.name}"吗？`

  try {
    await ElMessageBox.confirm(confirmText, `${action}确认`, {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    })

    if (type === 'article') {
      const result = await toggleCategoryStatus(row.id)
      ElMessage.success(result.msg || `${action}成功`)
      loadArticleCategories()
    } else if (type === 'friend-link') {
      const result = await toggleFriendLinkCategoryStatus(row.id)
      ElMessage.success(result.msg || `${action}成功`)
      loadFriendLinkCategories()
    } else {
      const result = await toggleProjectCategoryStatus(row.id)
      ElMessage.success(result.msg || `${action}成功`)
      loadProjectCategories()
    }
  } catch (error) {
    if (error !== 'cancel') {
      console.error(`${action}失败:`, error)
    }
  }
}

const handleDelete = async (row: any, type: 'article' | 'project' | 'friend-link') => {
  const typeLabel = type === 'article' ? '文章' : type === 'project' ? '项目' : '友链'
  try {
    await ElMessageBox.confirm(
      `确定要删除${typeLabel}分类"${row.name}"吗？此操作不可恢复。`,
      '删除确认',
      {
        confirmButtonText: '确定删除',
        cancelButtonText: '取消',
        type: 'warning'
      }
    )

    if (type === 'article') {
      await deleteCategory(row.id)
    } else if (type === 'friend-link') {
      await deleteFriendLinkCategory(row.id)
    } else {
      await deleteProjectCategory(row.id)
    }
    ElMessage.success('删除成功')
    if (type === 'article') loadArticleCategories()
    else if (type === 'friend-link') loadFriendLinkCategories()
    else loadProjectCategories()
  } catch (error) {
    if (error !== 'cancel') {
      console.error('删除失败:', error)
    }
  }
}

const handleSubmit = async () => {
  if (!formRef.value) return

  await formRef.value.validate(async (valid) => {
    if (!valid) return

    submitLoading.value = true
    try {
      const payload = {
        name: formData.name,
        description: formData.description || undefined
      }

      if (isEdit.value && currentId.value) {
        if (dialogType.value === 'article') {
          await updateCategory(currentId.value, payload)
        } else if (dialogType.value === 'friend-link') {
          await updateFriendLinkCategory(currentId.value, payload)
        } else {
          await updateProjectCategory(currentId.value, payload)
        }
        ElMessage.success('修改成功')
      } else {
        if (dialogType.value === 'article') {
          await createCategory(payload)
        } else if (dialogType.value === 'friend-link') {
          await createFriendLinkCategory(payload)
        } else {
          await createProjectCategory(payload)
        }
        ElMessage.success('创建成功')
      }

      dialogVisible.value = false
      if (dialogType.value === 'article') loadArticleCategories()
      else if (dialogType.value === 'friend-link') loadFriendLinkCategories()
      else loadProjectCategories()
    } catch (error) {
      console.error('保存失败:', error)
      ElMessage.error('保存失败')
    } finally {
      submitLoading.value = false
    }
  })
}

const handleDialogClose = () => {
  formRef.value?.resetFields()
}

const formatDate = (dateStr: string) => {
  if (!dateStr) return '-'
  const date = new Date(dateStr)
  return date.toLocaleString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  })
}

onMounted(() => {
  loadArticleCategories()
  loadProjectCategories()
})
</script>

<style lang="scss" scoped>
.category-page {
  padding: 20px;
}

.category-page .el-card {
  transition: all 0.2s ease;
  &:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  }
}

.category-dialog {
  :deep(.el-dialog__body) {
    padding: 24px;
  }
}
</style>