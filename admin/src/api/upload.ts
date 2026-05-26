import request from '@/utils/http'

export function uploadFile(file: File, type?: string) {
  const formData = new FormData()
  formData.append('file', file)
  if (type) {
    formData.append('type', type)
  }

  return request.post<{ url: string; filename: string }>({
    url: '/v1/upload/image',
    data: formData,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}

export function uploadFiles(files: File[], type?: string) {
  const formData = new FormData()
  files.forEach((file) => {
    formData.append('files', file)
  })
  if (type) {
    formData.append('type', type)
  }

  return request.post<{ urls: string[]; filenames: string[] }>({
    url: '/v1/upload/batch',
    data: formData,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}