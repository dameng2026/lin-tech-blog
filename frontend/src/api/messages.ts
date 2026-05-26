import api from './site'

export function fetchGuestbookMessages(params = {}) {
  const query = { page: params.page || 1, size: params.size || 10, sort: params.sort || 'newest' }
  return api.get('/comments/guestbook/messages', { params: query }).then(r => r.data)
}

export function createGuestbookMessage(data) {
  return api.post('/comments/guestbook/messages', data).then(r => r.data)
}

export function replyGuestbookMessage(data) {
  return api.post('/comments/guestbook/messages', data).then(r => r.data)
}

export function likeMessage(messageId) {
  return api.post(`/comments/${messageId}/like`).then(r => r.data)
}