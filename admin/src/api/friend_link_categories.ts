import request from '@/utils/http'

export interface FriendLinkCategory {
  id: number
  name: string
  description?: string
  is_active: boolean
  created_at: string
  updated_at?: string
}

export function fetchFriendLinkCategories(params?: { skip?: number; limit?: number; include_inactive?: boolean }) {
  return request.get<FriendLinkCategory[]>({
    url: '/v1/friend-link-categories',
    params
  })
}

export function createFriendLinkCategory(data: {
  name: string
  description?: string
}) {
  return request.post<FriendLinkCategory>({
    url: '/v1/friend-link-categories',
    data
  })
}

export function updateFriendLinkCategory(id: number, data: {
  name?: string
  description?: string
  is_active?: boolean
}) {
  return request.put<FriendLinkCategory>({
    url: `/v1/friend-link-categories/${id}`,
    data
  })
}

export function toggleFriendLinkCategoryStatus(id: number) {
  return request.patch<{ id: number; is_active: boolean }>({
    url: `/v1/friend-link-categories/${id}/toggle-status`
  })
}

export function deleteFriendLinkCategory(id: number) {
  return request.del({
    url: `/v1/friend-link-categories/${id}`
  })
}