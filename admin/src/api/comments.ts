import request from '@/utils/http'

export function fetchComments(params?: { 
  article_id?: number
  project_id?: number
  content?: string
  status?: string
  type?: string
  page?: number
  size?: number 
}) {
  return request.get<{ comments: any[]; total: number; page: number; size: number }>({
    url: '/v1/comments',
    params
  })
}

export const fetchCommentList = fetchComments

export function fetchComment(id: number) {
  return request.get<any>({
    url: `/v1/comments/${id}`
  })
}

export function createComment(data: {
  article_id?: number
  project_id?: number
  content: string
  parent_id?: number
  guest_name?: string
  guest_email?: string
}) {
  const url = data.article_id 
    ? `/v1/comments/article/${data.article_id}` 
    : data.project_id 
      ? `/v1/comments/project/${data.project_id}` 
      : '/v1/comments/guestbook/messages'
  return request.post<any>({
    url,
    data: { content: data.content, parent_id: data.parent_id, guest_name: data.guest_name, guest_email: data.guest_email }
  })
}

export function deleteComment(id: number) {
  return request.del({
    url: `/v1/comments/${id}`
  })
}

export function approveComment(id: number) {
  return request.put<any>({
    url: `/v1/comments/${id}/approve`
  })
}

export function likeComment(id: number) {
  return request.post({
    url: `/v1/comments/${id}/like`
  })
}

export function fetchGuestbooks(params?: { 
  page?: number
  size?: number 
  sort?: string
  keyword?: string
  status?: string
}) {
  return request.get<{ comments: any[]; total: number; page: number; size: number }>({
    url: '/v1/comments/guestbook/messages',
    params
  })
}

export function createGuestbook(content: string) {
  return request.post<any>({
    url: '/v1/comments/guestbook',
    params: { content }
  })
}

export function updateGuestbook(id: number, data: { reply?: string; is_top?: boolean }) {
  return request.put<any>({
    url: `/v1/comments/guestbook/${id}`,
    params: data
  })
}

export function deleteGuestbook(id: number) {
  return request.del({
    url: `/v1/comments/guestbook/${id}`
  })
}

export function replyGuestbookMessage(parentId: number, content: string, guestName: string = '博主') {
  return request.post<any>({
    url: '/v1/comments/guestbook/messages',
    data: {
      content,
      guest_name: guestName,
      parent_id: parentId,
      reply_to_id: parentId
    }
  })
}
