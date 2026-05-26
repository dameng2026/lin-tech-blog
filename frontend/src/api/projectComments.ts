import api from './site'

export function fetchProjectComments(projectId, params = {}) {
  return api.get(`/comments/project/${projectId}`, { params }).then(r => r.data?.data || r.data)
}

export function createProjectComment(projectId, data) {
  return api.post(`/comments/project/${projectId}`, data).then(r => r.data?.data || r.data)
}

export function likeProjectComment(commentId) {
  return api.post(`/comments/${commentId}/like`).then(r => r.data?.data || r.data)
}

export function likeProject(projectId) {
  return api.post(`/projects/${projectId}/like`).then(r => r.data?.data || r.data)
}
