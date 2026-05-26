import api from './site'

export function fetchArticleComments(articleId, params = {}) {
  return api.get(`/comments/article/${articleId}`, { params }).then(r => r.data?.data || r.data)
}

export function createArticleComment(articleId, data) {
  return api.post(`/comments/article/${articleId}`, data).then(r => r.data?.data || r.data)
}

export function likeComment(commentId) {
  return api.post(`/comments/${commentId}/like`).then(r => r.data?.data || r.data)
}