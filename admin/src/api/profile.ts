import request from '@/utils/http'

export interface Skill {
  id: number
  name: string
  category: string
  proficiency: number
  order: number
}

export interface Experience {
  id: number
  title: string
  company: string
  description: string
  start_date: string
  end_date: string
  order: number
}

export interface Education {
  id: number
  degree: string
  school: string
  major: string
  start_date: string
  end_date: string
  order: number
}

export function fetchProfile() {
  return request.get<any>({
    url: '/v1/profile'
  })
}

export function updateProfile(data: { bio?: string; social_links?: Record<string, string> }) {
  return request.put<any>({
    url: '/v1/profile',
    params: data
  })
}

export function setResumeKey(key: string) {
  return request.post({
    url: '/v1/profile/resume/key',
    params: { key }
  })
}

export function downloadResume(key: string) {
  return request.post({
    url: '/v1/profile/resume/download',
    params: { key }
  })
}

export function fetchSkills() {
  return request.get<Skill[]>({
    url: '/v1/profile/skills'
  })
}

export function createSkill(data: Omit<Skill, 'id'>) {
  return request.post<Skill>({
    url: '/v1/profile/skills',
    params: data
  })
}

export function updateSkill(id: number, data: Partial<Skill>) {
  return request.put<Skill>({
    url: `/v1/profile/skills/${id}`,
    params: data
  })
}

export function deleteSkill(id: number) {
  return request.del({
    url: `/v1/profile/skills/${id}`
  })
}

export function fetchExperiences() {
  return request.get<Experience[]>({
    url: '/v1/profile/experiences'
  })
}

export function createExperience(data: Omit<Experience, 'id'>) {
  return request.post<Experience>({
    url: '/v1/profile/experiences',
    params: data
  })
}

export function updateExperience(id: number, data: Partial<Experience>) {
  return request.put<Experience>({
    url: `/v1/profile/experiences/${id}`,
    params: data
  })
}

export function deleteExperience(id: number) {
  return request.del({
    url: `/v1/profile/experiences/${id}`
  })
}

export function fetchEducation() {
  return request.get<Education[]>({
    url: '/v1/profile/education'
  })
}

export function createEducation(data: Omit<Education, 'id'>) {
  return request.post<Education>({
    url: '/v1/profile/education',
    params: data
  })
}

export function updateEducation(id: number, data: Partial<Education>) {
  return request.put<Education>({
    url: `/v1/profile/education/${id}`,
    params: data
  })
}

export function deleteEducation(id: number) {
  return request.del({
    url: `/v1/profile/education/${id}`
  })
}

export function fetchResumeInfo() {
  return request.get({
    url: '/v1/profile/resume/info'
  })
}

export function uploadResume(file: File) {
  const formData = new FormData()
  formData.append('file', file)
  return request.post({
    url: '/v1/profile/resume/upload',
    data: formData,
    headers: { 'Content-Type': 'multipart/form-data' }
  })
}

export function toggleResumeStatus(id: number) {
  return request.put({
    url: `/v1/profile/resume/${id}/toggle`
  })
}

export function deleteResume(id: number) {
  return request.del({
    url: `/v1/profile/resume/${id}`
  })
}

export function fetchResumeKeys() {
  return request.get({
    url: '/v1/resume-keys'
  })
}

export function createResumeKey(data: { length: number; valid_hours: number }) {
  return request.post({
    url: '/v1/resume-keys',
    params: data
  })
}

export function deleteResumeKey(id: number) {
  return request.del({
    url: `/v1/resume-keys/${id}`
  })
}
