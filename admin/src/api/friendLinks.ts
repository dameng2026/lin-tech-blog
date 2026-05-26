import request from '@/utils/http'

export function fetchFriendLinks(params?: { status?: string; category?: string; page?: number; size?: number }) {
  return request.get<any>({
    url: '/v1/friend-links',
    params
  })
}

export function fetchAllFriendLinks(params?: { status?: string; category?: string; page?: number; size?: number }) {
  return request.get<any>({
    url: '/v1/friend-links/admin',
    params
  })
}

export function createFriendLink(data: {
  name: string
  url: string
  logo?: string
  category?: string
  description?: string
  status?: string
}) {
  return request.post<any>({
    url: '/v1/friend-links/apply',
    data
  })
}

export function updateFriendLink(id: number, data: any) {
  return request.put<any>({
    url: `/v1/friend-links/${id}`,
    data
  })
}

export function deleteFriendLink(id: number) {
  return request.del({
    url: `/v1/friend-links/${id}`
  })
}

export function approveFriendLink(id: number) {
  return request.put({
    url: `/v1/friend-links/${id}/approve`
  })
}

export function rejectFriendLink(id: number) {
  return request.put({
    url: `/v1/friend-links/${id}/reject`
  })
}

export function pauseFriendLink(id: number) {
  return request.put({
    url: `/v1/friend-links/${id}/pause`
  })
}

export function resumeFriendLink(id: number) {
  return request.put({
    url: `/v1/friend-links/${id}/resume`
  })
}

export function fetchFriendLinkStats(params?: { status?: string }) {
  return request.get<any>({
    url: '/v1/friend-links/stats',
    params
  })
}

export function fetchFriendLinkCategories() {
  return request.get<any>({
    url: '/v1/friend-links/categories'
  })
}
