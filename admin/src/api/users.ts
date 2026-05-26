import request from '@/utils/http'

export interface User {
  id: number
  username: string
  email: string
  role: string
  status: string
  avatar?: string
  nickname?: string
  bio?: string
  city?: string
  social_links?: Record<string, string>
  created_at: string
}

export function fetchUsers(params?: {
  page?: number
  size?: number
  keyword?: string
  role?: string
}) {
  return request.get<{ users: User[]; total: number }>({
    url: '/v1/users',
    params
  })
}

export function fetchUser(id: number) {
  return request.get<User>({
    url: `/v1/users/${id}`
  })
}

export function createUser(data: Partial<User>) {
  return request.post<User>({
    url: '/v1/users',
    params: data
  })
}

export function updateUser(id: number, data: Partial<User>) {
  return request.put<User>({
    url: `/v1/users/${id}`,
    params: data
  })
}

export function deleteUser(id: number) {
  return request.del({
    url: `/v1/users/${id}`
  })
}

export function updateUserStatus(id: number, status: string) {
  return request.put({
    url: `/v1/users/${id}/status`,
    params: { status }
  })
}

export function updateUserRole(id: number, role: string) {
  return request.put({
    url: `/v1/users/${id}/role`,
    params: { role }
  })
}

export function updateCurrentUser(data: Partial<User>) {
  return request.put<User>({
    url: '/v1/users/me',
    params: data
  })
}

export function uploadAvatar(file: File) {
  const formData = new FormData()
  formData.append('file', file)
  return request.post<{ url: string }>({
    url: '/v1/users/avatar',
    data: formData
  })
}
