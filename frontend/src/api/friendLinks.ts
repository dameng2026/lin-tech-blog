import api from './site'

export function fetchFriendLinks(params = {}) {
  return api.get('/friend-links/', { params }).then(r => r.data)
}

export function fetchFriendLinkStats(params = {}) {
  return api.get('/friend-links/stats', { params }).then(r => r.data)
}

export function applyFriendLink(data) {
  return api.post('/friend-links/apply', data).then(r => r.data)
}

export function fetchFriendLinkCategories() {
  return api.get('/friend-links/categories').then(r => r.data)
}
