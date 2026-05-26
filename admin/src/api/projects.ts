import request from '@/utils/http'

export function fetchProjects(params?: {
  page?: number
  size?: number
  tech_stack?: string
  status?: string
  show_paused?: boolean
}) {
  return request.get<{ projects: any[]; total: number }>({
    url: '/v1/projects',
    params
  })
}

export const fetchProjectList = fetchProjects

export function fetchProject(id: number) {
  return request.get<any>({
    url: `/v1/projects/${id}`
  })
}

export function createProject(data: {
  name: string
  cover?: string
  tags?: string[]
  github_url?: string
  demo_url?: string
  summary?: string
  tech_stack?: string[]
  status?: string
  description?: string
  project_type?: string
  start_date?: string
  end_date?: string
  last_update?: string
  open_source_license?: string
  database_type?: string
  deployment_platform?: string
  docs_url?: string
  content?: string
  catalog?: any[]
  is_paid?: boolean
  is_featured?: boolean
  repost_url?: string
  category_id?: number
}) {
  return request.post<any>({
    url: '/v1/projects',
    params: data
  })
}

export function updateProject(id: number, data: any) {
  return request.put<any>({
    url: `/v1/projects/${id}`,
    params: data
  })
}

export function deleteProject(id: number) {
  return request.del({
    url: `/v1/projects/${id}`
  })
}
