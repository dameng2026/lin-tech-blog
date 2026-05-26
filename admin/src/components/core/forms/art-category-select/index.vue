<template>
  <el-select
    :model-value="modelValue"
    :placeholder="placeholder"
    clearable
    :style="selectStyle"
    @update:model-value="handleChange"
  >
    <el-option label="全部" value="" />
    <el-option v-for="category in categories" :key="category.id" :label="category.name" :value="category.id">
      <span>{{ category.name }}</span>
    </el-option>
  </el-select>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { fetchCategories } from '@/api/taxonomy'

interface Category {
  id: number
  name: string
  slug: string
  description?: string
  order?: number
  is_active?: boolean
}

const props = defineProps<{
  modelValue: number | string
  placeholder?: string
  width?: string | number
}>()

const emit = defineEmits<{
  (e: 'update:modelValue', value: number | string): void
  (e: 'change', value: number | string): void
}>()

const categories = ref<Category[]>([])

const selectStyle = computed(() => ({
  width: typeof props.width === 'number' ? `${props.width}px` : props.width || '160px'
}))

const handleChange = (value: number | string) => {
  emit('update:modelValue', value)
  emit('change', value)
}

const loadCategories = async () => {
  try {
    const data = await fetchCategories()
    categories.value = (data || []).filter(c => c.is_active !== false)
  } catch (error) {
    console.error('Failed to load categories:', error)
    categories.value = []
  }
}

onMounted(() => {
  loadCategories()
})

defineExpose({
  refresh: loadCategories
})
</script>
