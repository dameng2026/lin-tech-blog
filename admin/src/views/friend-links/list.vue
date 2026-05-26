<template>
  <div class="friend-links-page art-full-height">
    <ArtBreadcrumb :items="breadcrumbItems" />

    <ElCard class="mb-4">
      <div class="flex justify-between items-center">
        <ElForm :inline="true" :model="searchForm" class="flex-1">
          <ElFormItem label="网站名称">
            <ElInput v-model="searchForm.name" placeholder="搜索申请" clearable @keyup.enter="handleSearch" />
          </ElFormItem>
          <ElFormItem>
            <ElButton type="primary" @click="handleSearch">搜索</ElButton>
            <ElButton @click="handleReset">重置</ElButton>
          </ElFormItem>
        </ElForm>
        <div class="ml-4">
          <ElButton type="primary" @click="handleCreate" v-auth="'add'">新增友链</ElButton>
        </div>
      </div>
    </ElCard>

    <ElCard class="art-table-card">
      <ArtTableHeader v-model:columns="columnChecks" :loading="loading" @refresh="refreshData" layout="refresh,size,fullscreen,columns,settings">
      </ArtTableHeader>

      <ArtTable
        :loading="loading"
        :data="data"
        :columns="columns"
        :pagination="pagination"
        @selection-change="handleSelectionChange"
        @pagination:size-change="handleSizeChange"
        @pagination:current-change="handleCurrentChange"
      />
    </ElCard>

    <ElDialog
      v-model="dialogVisible"
      :title="isEdit ? '编辑友链' : '新增友链'"
      width="600px"
      destroy-on-close
    >
      <ElForm ref="formRef" :model="form" :rules="rules" label-width="100px">
        <ElFormItem label="网站名称" prop="name">
          <ElInput v-model="form.name" placeholder="请输入网站名称" />
        </ElFormItem>
        <ElFormItem label="网站地址" prop="url">
          <ElInput v-model="form.url" placeholder="请输入网站地址" />
        </ElFormItem>
        <ElFormItem label="网站Logo">
          <ElUpload
            drag
            :action="uploadUrl"
            :headers="uploadHeaders"
            :show-file-list="false"
            :on-success="handleUploadSuccess"
            :before-upload="beforeUpload"
            class="w-full"
          >
            <ElIcon class="el-icon--upload"><UploadFilled /></ElIcon>
            <div class="el-upload__text">
              拖拽文件到此处或 <em>点击上传</em>
            </div>
            <template #tip>
              <div class="el-upload__tip">支持 jpg/png 格式，不超过 2MB</div>
            </template>
          </ElUpload>
          <img v-if="form.logo" :src="form.logo" class="mt-2 w-20 h-20 object-cover rounded" />
        </ElFormItem>
        <ElFormItem label="分类" prop="category">
          <ElSelect v-model="form.category" placeholder="请选择分类" style="width: 100%">
            <ElOption v-for="cat in categoryOptions" :key="cat" :label="cat" :value="cat" />
          </ElSelect>
        </ElFormItem>
        <ElFormItem label="网站描述" prop="description">
          <ElInput v-model="form.description" type="textarea" :rows="3" placeholder="请输入网站描述" />
        </ElFormItem>
        <ElFormItem label="状态" prop="status">
          <ElSelect v-model="form.status" placeholder="请选择状态" style="width: 100%">
            <ElOption label="待审核" value="pending" />
            <ElOption label="已通过" value="approved" />
            <ElOption label="已拒绝" value="rejected" />
            <ElOption label="已暂停" value="paused" />
          </ElSelect>
        </ElFormItem>
      </ElForm>
      <template #footer>
        <ElButton @click="dialogVisible = false">取消</ElButton>
        <ElButton type="primary" @click="handleSubmit">保存</ElButton>
      </template>
    </ElDialog>
  </div>
</template>

<script setup lang="ts">
import { ref, h, reactive, onMounted } from 'vue'
import { ElCard, ElForm, ElFormItem, ElInput, ElSelect, ElOption, ElButton, ElSpace, ElMessage, ElMessageBox, ElDialog, ElUpload, ElTag } from 'element-plus'
import { UploadFilled } from '@element-plus/icons-vue'
import { useUserStore } from '@/store/modules/user'
import ArtBreadcrumb from '@/components/core/layouts/art-breadcrumb/index.vue'
import ArtTableHeader from '@/components/core/tables/art-table-header/index.vue'
import ArtTable from '@/components/core/tables/art-table/index.vue'
import ArtButtonTable from '@/components/core/forms/art-button-table/index.vue'
import { useTable } from '@/hooks/core/useTable'
import { fetchAllFriendLinks, createFriendLink, updateFriendLink, deleteFriendLink, pauseFriendLink, resumeFriendLink } from '@/api/friendLinks'
import { fetchFriendLinkCategories as fetchFLCategories } from '@/api/friend_link_categories'

defineOptions({ name: 'FriendLinkApproval' })

const userStore = useUserStore()
const uploadUrl = `${import.meta.env.VITE_API_URL}/api/v1/upload`
const uploadHeaders = { Authorization: userStore.accessToken }

const breadcrumbItems = [
  { label: '首页', path: '/content/articles' },
  { label: '友链审批列表', path: '/links/link-approval' }
]

const searchForm = ref({
  name: '',
  status: 'pending'
})

const columnChecks = ref<string[]>([])
const dialogVisible = ref(false)
const isEdit = ref(false)
const formRef = ref()

const form = reactive({
  id: 0,
  name: '',
  url: '',
  logo: '',
  category: '',
  description: '',
  status: 'pending'
})

const rules = {
  name: [{ required: true, message: '请输入网站名称', trigger: 'blur' }],
  url: [{ required: true, message: '请输入网站地址', trigger: 'blur' }],
  category: [{ required: true, message: '请选择分类', trigger: 'change' }]
}

const categoryOptions = ref<string[]>([])

async function loadCategories() {
  try {
    const data = await fetchFLCategories({ include_inactive: true })
    const cats = data || []
    if (cats.length > 0) {
      categoryOptions.value = cats.map((c: any) => c.name)
    }
  } catch {}
}

loadCategories()

const {
  columns,
  data,
  loading,
  pagination,
  getData,
  replaceSearchParams,
  resetSearchParams,
  handleSizeChange,
  handleCurrentChange,
  refreshData
} = useTable({
  core: {
    apiFn: fetchAllFriendLinks,
    apiParams: {
      page: 1,
      size: 10,
      ...searchForm.value
    },
    paginationKey: {
      current: 'page',
      size: 'size'
    },
    columnsFactory: () => [
      { type: 'selection' },
      { type: 'index', width: 60, label: '序号' },
      {
        prop: 'logo',
        label: 'Logo',
        width: 100,
        formatter: (row) =>
          h('div', { class: 'flex items-center justify-center' }, [
            h('img', {
              src: row.logo || 'https://via.placeholder.com/40',
              style: 'width: 40px; height: 40px; object-fit: cover; border-radius: 4px;'
            })
          ])
      },
      { prop: 'name', label: '网站名称', minWidth: 150 },
      {
        prop: 'url',
        label: '网站地址',
        minWidth: 200,
        formatter: (row) =>
          h('a', {
            href: row.url,
            target: '_blank',
            class: 'text-blue-500 hover:underline'
          }, row.url)
      },
      { prop: 'category', label: '分类', width: 120 },
      {
        prop: 'status',
        label: '状态',
        width: 100,
        formatter: (row) => {
          const statusMap: Record<string, { type: string; text: string }> = {
            pending: { type: 'warning', text: '待审核' },
            approved: { type: 'success', text: '已通过' },
            rejected: { type: 'danger', text: '已拒绝' },
            paused: { type: 'info', text: '已暂停' }
          }
          return h(ElTag, { type: statusMap[row.status]?.type }, statusMap[row.status]?.text)
        }
      },
      { prop: 'createdAt', label: '申请时间', width: 180 },
      {
        prop: 'operation',
        label: '操作',
        width: 180,
        fixed: 'right',
        formatter: (row) => {
          const actions = []

          if (row.status === 'pending') {
            actions.push(h(ArtButtonTable, { type: 'approve', onClick: () => handleApprove(row) }))
            actions.push(h(ArtButtonTable, { type: 'reject', onClick: () => handleReject(row) }))
            actions.push(h(ArtButtonTable, { type: 'pause', onClick: () => handlePause(row) }))
          }
          if (row.status === 'rejected') {
            actions.push(h(ArtButtonTable, { type: 'approve', onClick: () => handleApprove(row) }))
          }
          if (row.status === 'paused') {
            actions.push(h(ArtButtonTable, { type: 'resume', onClick: () => handleResume(row) }))
          }

          actions.push(h(ArtButtonTable, { type: 'delete', onClick: () => handleDelete(row), vAuth: 'delete' }))

          return h('div', { class: 'flex gap-2' }, actions)
        }
      }
    ]
  }
})

const handleSelectionChange = (selection: any) => {
  console.log('选中的友链:', selection)
}

const handleSearch = () => {
  replaceSearchParams({ ...searchForm.value })
  getData()
}

const handleReset = () => {
  searchForm.value = { name: '', status: 'pending' }
  resetSearchParams()
  getData()
}

const handleCreate = () => {
  isEdit.value = false
  Object.assign(form, {
    id: 0,
    name: '',
    url: '',
    logo: '',
    category: categoryOptions.value[0] || '',
    description: '',
    status: 'pending'
  })
  dialogVisible.value = true
}

const handleEdit = (row: any) => {
  isEdit.value = true
  Object.assign(form, { ...row })
  dialogVisible.value = true
}

const handleApprove = (row: any) => {
  ElMessageBox.confirm('确定要通过友链\"' + row.name + '\"的申请吗？', '审核确认', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'success'
  }).then(async () => {
    try {
      await updateFriendLink(row.id, { status: 'approved' })
      ElMessage.success('审核通过')
      refreshData()
    } catch {
      ElMessage.error('操作失败')
    }
  }).catch(() => {})
}

const handleReject = (row: any) => {
  ElMessageBox.confirm('确定要拒绝友链\"' + row.name + '\"的申请吗？', '审核确认', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning'
  }).then(async () => {
    try {
      await updateFriendLink(row.id, { status: 'rejected' })
      ElMessage.success('已拒绝')
      refreshData()
    } catch {
      ElMessage.error('操作失败')
    }
  }).catch(() => {})
}

const handlePause = (row: any) => {
  ElMessageBox.confirm('确定要暂停友链\"' + row.name + '\"吗？暂停后该友链将不会在前台展示。', '暂停确认', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'info'
  }).then(async () => {
    try {
      await pauseFriendLink(row.id)
      ElMessage.success('已暂停')
      refreshData()
    } catch {
      ElMessage.error('操作失败')
    }
  }).catch(() => {})
}

const handleResume = (row: any) => {
  ElMessageBox.confirm('确定要启用友链\"' + row.name + '\"吗？启用后该友链将恢复在前台展示。', '启用确认', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'success'
  }).then(async () => {
    try {
      await resumeFriendLink(row.id)
      ElMessage.success('已启用')
      refreshData()
    } catch {
      ElMessage.error('操作失败')
    }
  }).catch(() => {})
}

const handleDelete = (row: any) => {
  ElMessageBox.confirm('确定要删除友链\"' + row.name + '\"吗？此操作不可恢复。', '删除确认', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning'
  }).then(async () => {
    try {
      await deleteFriendLink(row.id)
      ElMessage.success('删除成功')
      refreshData()
    } catch {
      ElMessage.error('删除失败')
    }
  }).catch(() => {})
}

const handleSubmit = async () => {
  try {
    if (isEdit.value) {
      await updateFriendLink(form.id, form)
      ElMessage.success('更新成功')
    } else {
      await createFriendLink(form)
      ElMessage.success('创建成功')
    }
    dialogVisible.value = false
    refreshData()
  } catch {
    ElMessage.error('操作失败')
  }
}

const beforeUpload = (file: File) => {
  const isImage = file.type.startsWith('image/')
  const isLt2M = file.size / 1024 / 1024 < 2
  if (!isImage) { ElMessage.error('只能上传图片文件!'); return false }
  if (!isLt2M) { ElMessage.error('图片大小不能超过2MB!'); return false }
  return true
}

const handleUploadSuccess = (response: any) => {
  if (response.data?.url) {
    form.logo = response.data.url
    ElMessage.success('上传成功')
  }
}

onMounted(() => {
  getData()
})
</script>

<style lang="scss" scoped>
.friend-links-page {
  padding: 20px;
}

.friend-links-page .el-card {
  border: 1px solid var(--art-card-border);
  transition: all 0.2s ease;
  &:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  }
}
</style>