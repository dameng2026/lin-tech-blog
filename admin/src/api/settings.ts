import request from '@/utils/http'

export function fetchSiteSettings() {
  return request.get<any>({
    url: '/v1/settings/site'
  })
}

export function updateSiteSettings(data: {
  site_name?: string
  site_title?: string
  keywords?: string
  description?: string
  logo?: string
  icp_number?: string
  site_start_date?: string
  github_url?: string
  qq_qrcode?: string
  wechat_qrcode?: string
  admin_avatar?: string
  email?: string
  author_name?: string
  bio?: string
  bio_motto?: string
  bio_motto_items?: string
  bio_interests?: string
  location?: string
  wechat?: string
  qq?: string
  phone?: string
  favicon?: string
  login_enabled?: number
}) {
  return request.put<any>({
    url: '/v1/settings/site',
    params: data
  })
}

export function fetchUploadedFiles(params?: { skip?: number; limit?: number }) {
  return request.get<any[]>({
    url: '/v1/settings/files',
    params
  })
}

export function uploadFile(file: File) {
  const formData = new FormData()
  formData.append('file', file)
  return request.post<any>({
    url: '/v1/settings/files/upload',
    data: formData,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}

export function deleteUploadedFile(id: number) {
  return request.del({
    url: `/v1/settings/files/${id}`
  })
}

export function uploadAvatar(file: File) {
  const formData = new FormData()
  formData.append('file', file)
  return request.post<any>({
    url: '/v1/settings/avatar/upload',
    data: formData,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}
