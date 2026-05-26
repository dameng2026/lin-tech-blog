<template>
  <div class="category-page art-full-height">
    <ElCard class="art-table-card" style="margin-top: 0">
      <ArtTableHeader v-model:columns="columnChecks" :loading="loading" @refresh="refreshData">
        <template #left>
          <ElSpace wrap>
            <ElButton @click="showDialog('add')" v-ripple type="primary">
              <template #icon><IconifyIconOffline icon="ri:add-line" /></template>
              新增分类
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
        :title="dialogType === 'add' ? '新增分类' : '编辑分类'"
        width="500px"
        :close-on-click-modal="false"
      >
        <ElForm :model="formData" :rules="rules" ref="formRef" label-width="100px">
          <ElFormItem label="分类名称" prop="name">
            <ElInput v-model="formData.name" placeholder="请输入分类名称" />
          </ElFormItem>
          <ElFormItem label="Slug" prop="slug">
            <ElInput v-model="formData.slug" placeholder="请输入URL别名（英文）" />
          </ElFormItem>
          <ElFormItem label="描述">
            <ElInput v-model="formData.description" type="textarea" :rows="3" placeholder="请输入分类描述" />
          </ElFormItem>
          <ElFormItem label="排序">
            <ElInputNumber v-model="formData.order" :min="0" :max="999" />
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
  import { fetchCategories, createCategory, updateCategory, deleteCategory } from '@/api/taxonomy'
  import { ElMessage, ElMessageBox, FormInstance, FormRules } from 'element-plus'
  import IconifyIconOffline from '@/components/core/iconify-icon-offline/index.vue'

  defineOptions({ name: 'Categories' })

  const formRef = ref<FormInstance>()
  const dialogVisible = ref(false)
  const dialogType = ref<'add' | 'edit'>('add')
  const submitLoading = ref(false)
  const currentId = ref<number>()

  const formData = ref({
    name: '',
    slug: '',
    description: '',
    order: 0
  })

  const rules: FormRules = {
    name: [{ required: true, message: '请输入分类名称', trigger: 'blur' }],
    slug: [{ required: true, message: '请输入URL别名', trigger: 'blur' }]
  }

  const { data, columns, columnChecks, loading, pagination, getData, handleSizeChange, handleCurrentChange, refreshData } = useTable({
    core: {
      apiFn: fetchCategories,
      apiParams: { skip: 0, limit: 20 },
      columnsFactory: () => [
        { type: 'index', width: 60, label: '序号' },
        { prop: 'id', label: 'ID', width: 80 },
        { prop: 'name', label: '分类名称' },
        { prop: 'slug', label: 'Slug' },
        { prop: 'order', label: '排序', width: 100 },
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
        description: row.description || '',
        order: row.order || 0
      }
    } else {
      currentId.value = undefined
      formData.value = { name: '', slug: '', description: '', order: 0 }
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
          await createCategory(formData.value)
          ElMessage.success('新增成功')
        } else {
          await updateCategory(currentId.value!, formData.value)
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
    ElMessageBox.confirm(`确定要删除分类"${row.name}"吗？`, '删除确认', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    }).then(async () => {
      await deleteCategory(row.id)
      ElMessage.success('删除成功')
      refreshData()
    }).catch(() => {})
  }
</script>

<style scoped>
  .category-page {
    padding: 16px;
  }
</style>
