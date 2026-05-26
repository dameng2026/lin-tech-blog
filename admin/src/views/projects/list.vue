<template>
  <div class="project-page">
    <ArtBreadcrumb :items="breadcrumbItems" />

    <ElCard>
      <div class="flex justify-between items-center mb-4">
        <ElForm :inline="true" :model="searchForm">
          <ElFormItem label="项目名称">
            <ElInput v-model="searchForm.name" placeholder="输入项目名称" clearable @keyup.enter="handleSearch" />
          </ElFormItem>
          <ElFormItem label="项目状态">
            <ElSelect v-model="searchForm.status" placeholder="选择项目状态" clearable style="width: 140px">
              <ElOption label="全部" :value="undefined" />
              <ElOption label="进行中" value="in_progress" />
              <ElOption label="已完成" value="completed" />
              <ElOption label="已归档" value="archived" />
              <ElOption label="已暂停" value="paused" />
            </ElSelect>
          </ElFormItem>
          <ElFormItem>
            <ElButton type="primary" @click="handleSearch">搜索</ElButton>
            <ElButton @click="handleReset">重置</ElButton>
          </ElFormItem>
        </ElForm>
        <ElButton type="primary" @click="handleCreate">
          <ElIcon class="mr-1"><Plus /></ElIcon>
          新增项目
        </ElButton>
      </div>

      <ElTable :data="projects" v-loading="loading" stripe>
        <ElTableColumn prop="id" label="ID" width="80" />
        <ElTableColumn prop="cover" label="封面" width="120">
          <template #default="{ row }">
            <img
              v-if="row.cover"
              :src="row.cover"
              :alt="row.name"
              style="width: 60px; height: 60px; object-fit: cover; border-radius: 4px"
            />
            <span v-else class="text-gray-400">无封面</span>
          </template>
        </ElTableColumn>
        <ElTableColumn prop="name" label="项目名称" min-width="200">
          <template #default="{ row }">
            <div :class="{ 'text-gray-400': row.display_status === 'paused' }">
              {{ row.name }}
            </div>
          </template>
        </ElTableColumn>
        <ElTableColumn prop="tech_stack" label="技术栈" min-width="150">
          <template #default="{ row }">
            <div class="flex flex-wrap gap-1">
              <ElTag
                v-for="(tech, index) in (row.tech_stack || [])"
                :key="index"
                type="primary"
                size="small"
              >
                {{ tech }}
              </ElTag>
              <span v-if="!row.tech_stack || row.tech_stack.length === 0" class="text-gray-400 text-sm">无</span>
            </div>
          </template>
        </ElTableColumn>
        <ElTableColumn prop="status" label="项目状态" width="100" align="center">
          <template #default="{ row }">
            <ElTag :type="getStatusType(row.status)" size="small">
              {{ getStatusText(row.status) }}
            </ElTag>
          </template>
        </ElTableColumn>
        <ElTableColumn prop="display_status" label="展示状态" width="100" align="center">
          <template #default="{ row }">
            <ElTag :type="row.display_status === 'paused' ? 'danger' : 'success'" size="small">
              {{ row.display_status === 'paused' ? '暂停中' : '进行中' }}
            </ElTag>
          </template>
        </ElTableColumn>
        <ElTableColumn prop="created_at" label="创建时间" width="180">
          <template #default="{ row }">
            {{ formatDate(row.created_at) }}
          </template>
        </ElTableColumn>
        <ElTableColumn prop="publish_time" label="发布时间" width="180">
          <template #default="{ row }">
            {{ formatDate(row.publish_time) }}
          </template>
        </ElTableColumn>
        <ElTableColumn prop="like_count" label="点赞数" width="80" align="center" />
        <ElTableColumn prop="view_count" label="阅读量" width="80" align="center" />
        <ElTableColumn label="操作" width="200" fixed="right" align="center">
          <template #default="{ row }">
            <div class="flex gap-2 justify-center">
              <ElButton type="primary" size="small" text @click="handleEdit(row)">
                编辑
              </ElButton>
              <ElButton type="primary" size="small" text @click="handleComment(row)">评论</ElButton>
              <ElButton :type="row.display_status === 'paused' ? 'success' : 'warning'" size="small" text @click="handleToggleStatus(row)">
                {{ row.display_status === 'paused' ? '启用' : '暂停' }}
              </ElButton>
              <ElButton type="danger" size="small" text @click="handleDelete(row)">
                删除
              </ElButton>
            </div>
          </template>
        </ElTableColumn>
      </ElTable>

      <ElPagination
        v-if="total > 0"
        :current-page="pagination.page"
        :page-size="pagination.size"
        :total="total"
        layout="total, prev, pager, next, jumper"
        @current-change="handlePageChange"
        @size-change="handleSizeChange"
        class="mt-4 flex justify-center"
      />
    </ElCard>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'
import ArtBreadcrumb from '@/components/core/layouts/art-breadcrumb/index.vue'
import { fetchProjects, updateProject, deleteProject } from '@/api/projects'

defineOptions({ name: 'Projects' })

const router = useRouter()

const breadcrumbItems = [
  { label: '首页', path: '/content/articles' },
  { label: '项目管理', path: '/projects/list' },
  { label: '项目列表' }
]

const loading = ref(false)

const projects = ref<any[]>([])
const total = ref(0)
const pagination = reactive({
  page: 1,
  size: 20
})

const searchForm = reactive({
  name: '',
  status: undefined as string | undefined
})

const getStatusType = (status: string) => {
  const statusMap: Record<string, string> = {
    in_progress: 'warning',
    completed: 'success',
    archived: 'info',
    paused: 'danger'
  }
  return statusMap[status] || 'info'
}

const getStatusText = (status: string) => {
  const statusMap: Record<string, string> = {
    in_progress: '进行中',
    completed: '已完成',
    archived: '已归档',
    paused: '已暂停'
  }
  return statusMap[status] || status
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

const loadProjects = async () => {
  loading.value = true
  try {
    const params: any = {
      page: pagination.page,
      size: pagination.size,
      include_paused: true
    }
    if (searchForm.name) {
      params.name = searchForm.name
    }
    if (searchForm.status !== undefined) {
      params.status = searchForm.status
    }
    const response = await fetchProjects(params)
    if (response) {
      projects.value = response.projects || []
      total.value = response.total || 0
    }
  } catch (error) {
    console.error('加载项目列表失败:', error)
    ElMessage.error('加载项目列表失败')
  } finally {
    loading.value = false
  }
}

const handleSearch = () => {
  pagination.page = 1
  loadProjects()
}

const handleReset = () => {
  searchForm.name = ''
  searchForm.status = undefined
  pagination.page = 1
  loadProjects()
}

const handlePageChange = (page: number) => {
  pagination.page = page
  loadProjects()
}

const handleSizeChange = (size: number) => {
  pagination.size = size
  pagination.page = 1
  loadProjects()
}

const handleEdit = (row: any) => {
  router.push(`/projects/create?id=${row.id}`)
}

const handleCreate = () => {
  router.push('/projects/create')
}

const handleToggleStatus = async (row: any) => {
  const isPaused = row.display_status === 'paused'
  const action = isPaused ? '启用' : '暂停'
  const confirmText = isPaused
    ? `确定要${action}项目"${row.name}"吗？`
    : `确定要${action}项目"${row.name}"吗？${action}后该项目将不会在前台显示。`

  try {
    await ElMessageBox.confirm(confirmText, `${action}确认`, {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    })

    await updateProject(row.id, { display_status: isPaused ? 'active' : 'paused' })
    ElMessage.success(`${action}成功`)
    loadProjects()
  } catch (error) {
    if (error !== 'cancel') {
      console.error(`${action}失败:`, error)
    }
  }
}

const handleComment = (row: any) => {
  router.push({ name: 'Comments', query: { project_id: row.id, title: row.name, type: 'project' } })
}

const handleDelete = async (row: any) => {
  try {
    await ElMessageBox.confirm(
      `确定要删除项目"${row.name}"吗？此操作不可恢复。`,
      '删除确认',
      {
        confirmButtonText: '确定删除',
        cancelButtonText: '取消',
        type: 'warning'
      }
    )

    await deleteProject(row.id)
    ElMessage.success('删除成功')
    loadProjects()
  } catch (error) {
    if (error !== 'cancel') {
      console.error('删除失败:', error)
    }
  }
}

onMounted(() => {
  loadProjects()
})
</script>

<style lang="scss" scoped>
.project-page {
  padding: 20px;
}

.project-page .el-card {
  border: 1px solid var(--art-card-border);
  transition: all 0.2s ease;
}
.project-page .el-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
</style>