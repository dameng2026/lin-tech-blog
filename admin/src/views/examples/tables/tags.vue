<template>
  <div class="tags-page art-full-height">
    <ElCard class="art-table-card" style="margin-top: 0">
      <ArtTableHeader v-model:columns="columnChecks" :loading="loading" @refresh="refreshData">
        <template #left>
          <ElSpace wrap>
            <ElButton @click="showDialog('add')" v-ripple type="primary">
              <template #icon><IconifyIconOffline icon="ri:add-line" /></template>
              新增标签
            </ElButton>
          </ElSpace>
        </template>
      </ArtTableHeader>

      <ArtTable
        :loading="loading"
        :data="data"
        :columns="columns"
        :pagination="pagination"
        @pagination:size-change="handleSizeChange"
        @pagination:current-change="handleCurrentChange"
      />

      <ElDialog
        v-model="dialogVisible"
        :title="dialogType === 'add' ? '新增标签' : '编辑标签'"
        width="500px"
        :close-on-click-modal="false"
      >
        <ElForm :model="formData" :rules="rules" ref="formRef" label-width="100px">
          <ElFormItem label="标签名称" prop="name">
            <ElInput v-model="formData.name" placeholder="请输入标签名称" />
          </ElFormItem>
          <ElFormItem label="Slug" prop="slug">
            <ElInput v-model="formData.slug" placeholder="请输入URL别名（英文）" />
          </ElFormItem>
          <ElFormItem label="状态">
            <ElSwitch v-model="formData.is_active" active-text="启用" inactive-text="禁用" />
          </ElFormItem>
        </ElForm>
        <template #footer>
          <ElButton @click="dialogVisible = false">取消</ElButton>
          <ElButton type="primary" @click="handleSubmit" :loading="submitLoading">确定</ElButton>
        </template>
      </ElDialog>
    </ElCard>
  </div>
</template>

<script setup lang="ts">
  import { useTable } from '@/hooks/core/useTable'
  import { fetchTags, createTag, updateTag, deleteTag } from '@/api/taxonomy'
  import { ElMessage, ElMessageBox, FormInstance, FormRules } from 'element-plus'
  import IconifyIconOffline from '@/components/core/iconify-icon-offline/index.vue'

  defineOptions({ name: 'Tags' })

  const formRef = ref<FormInstance>()
  const dialogVisible = ref(false)
  const dialogType = ref<'add' | 'edit'>('add')
  const submitLoading = ref(false)
  const currentId = ref<number>()

  const formData = ref({
    name: '',
    slug: '',
    is_active: true
  })

  const rules: FormRules = {
    name: [{ required: true, message: '请输入标签名称', trigger: 'blur' }],
    slug: [{ required: true, message: '请输入URL别名', trigger: 'blur' }]
  }

  const { data, columns, columnChecks, loading, pagination, getData, handleSizeChange, handleCurrentChange, refreshData } = useTable({
    core: {
      apiFn: fetchTags,
      apiParams: { skip: 0, limit: 20 },
      columnsFactory: () => [
        { type: 'index', width: 60, label: '序号' },
        { prop: 'id', label: 'ID', width: 80 },
        { prop: 'name', label: '标签名称' },
        { prop: 'slug', label: 'Slug' },
        { prop: 'article_count', label: '使用次数', width: 100 },
        {
          prop: 'is_active',
          label: '状态',
          width: 100,
          formatter: (row) => row.is_active ? '启用' : '禁用'
        },
        {
          prop: 'operation',
          label: '操作',
          width: 150,
          fixed: 'right',
          formatter: (row) => [
            { type: 'edit', onClick: () => showDialog('edit', row) },
            { type: 'delete', onClick: () => handleDelete(row) }
          ]
        }
      ]
    }
  })

  const showDialog = (type: 'add' | 'edit', row?: any) => {
    dialogType.value = type
    if (type === 'edit' && row) {
      currentId.value = row.id
      formData.value = {
        name: row.name,
        slug: row.slug,
        is_active: row.is_active !== false
      }
    } else {
      currentId.value = undefined
      formData.value = { name: '', slug: '', is_active: true }
    }
    dialogVisible.value = true
  }

  const handleSubmit = async () => {
    if (!formRef.value) return
    await formRef.value.validate(async (valid) => {
      if (!valid) return
      submitLoading.value = true
      try {
        if (dialogType.value === 'add') {
          await createTag(formData.value)
          ElMessage.success('新增成功')
        } else {
          await updateTag(currentId.value!, formData.value)
          ElMessage.success('更新成功')
        }
        dialogVisible.value = false
        refreshData()
      } catch (error) {
        ElMessage.error('操作失败')
      } finally {
        submitLoading.value = false
      }
    })
  }

  const handleDelete = (row: any) => {
    ElMessageBox.confirm(`确定要删除标签"${row.name}"吗？`, '删除确认', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    }).then(async () => {
      await deleteTag(row.id)
      ElMessage.success('删除成功')
      refreshData()
    }).catch(() => {})
  }
</script>

<style scoped>
  .tags-page {
    padding: 16px;
  }
</style>
