import request from '@/utils/http'

export interface Category {
  id: number
  name: string
  description?: string
  is_active: boolean
  created_at: string
  updated_at?: string
}

export function fetchCategories(params?: { skip?: number; limit?: number; include_inactive?: boolean }) {
  return request.get<Category[]>({
    url: '/v1/taxonomy/categories',
    params
  })
}

export function createCategory(data: {
  name: string
  description?: string
}) {
  return request.post<Category>({
    url: '/v1/taxonomy/categories',
    data
  })
}

export function updateCategory(id: number, data: {
  name?: string
  description?: string
  is_active?: boolean
}) {
  return request.put<Category>({
    url: `/v1/taxonomy/categories/${id}`,
    data
  })
}

export function toggleCategoryStatus(id: number) {
  return request.patch<{ id: number; is_active: boolean }>({
    url: `/v1/taxonomy/categories/${id}/toggle-status`
  })
}

export function deleteCategory(id: number) {
  return request.del({
    url: `/v1/taxonomy/categories/${id}`
  })
}

export function fetchTags(params?: { skip?: number; limit?: number }) {
  return request.get<any[]>({
    url: '/v1/taxonomy/tags',
    params
  })
}

export function createTag(data: { name: string; slug: string }) {
  return request.post<any>({
    url: '/v1/taxonomy/tags',
    data
  })
}

export function updateTag(id: number, data: {
  name?: string
  slug?: string
  is_active?: boolean
}) {
  return request.put<any>({
    url: `/v1/taxonomy/tags/${id}`,
    data
  })
}

export function deleteTag(id: number) {
  return request.del({
    url: `/v1/taxonomy/tags/${id}`
  })
}

export function fetchTechStackStats(params?: { sort_by?: string; keyword?: string; page?: number; size?: number }) {
  return request.get({
    url: '/v1/taxonomy/tech-stacks',
    params
  })
}
