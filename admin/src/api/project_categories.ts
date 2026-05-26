import request from '@/utils/http'

export interface ProjectCategory {
  id: number
  name: string
  description?: string
  is_active: boolean
  created_at: string
  updated_at?: string
}

export function fetchProjectCategories(params?: { skip?: number; limit?: number; include_inactive?: boolean }) {
  return request.get<ProjectCategory[]>({
    url: '/v1/project-categories',
    params
  })
}

export function createProjectCategory(data: {
  name: string
  description?: string
}) {
  return request.post<ProjectCategory>({
    url: '/v1/project-categories',
    data
  })
}

export function updateProjectCategory(id: number, data: {
  name?: string
  description?: string
  is_active?: boolean
}) {
  return request.put<ProjectCategory>({
    url: `/v1/project-categories/${id}`,
    data
  })
}

export function toggleProjectCategoryStatus(id: number) {
  return request.patch<{ id: number; is_active: boolean }>({
    url: `/v1/project-categories/${id}/toggle-status`
  })
}

export function deleteProjectCategory(id: number) {
  return request.del({
    url: `/v1/project-categories/${id}`
  })
}