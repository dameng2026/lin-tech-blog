import request from '@/utils/http'

export interface ArticleListParams {
  page?: number
  size?: number
  category?: string
  tag?: string
  tech_stack?: string
  sort_by?: string
}

export function fetchArticles(params: ArticleListParams) {
  return request.get<{ articles: any[]; total: number; page: number; size: number }>({
    url: '/v1/articles/',
    params
  })
}

export const fetchArticleList = fetchArticles

export function fetchArticle(id: number) {
  return request.get<any>({
    url: `/v1/articles/${id}`
  })
}

export function createArticle(data: Api.Article.ArticleCreate) {
  return request.post<Api.Article.ArticleResponse>({
    url: '/v1/articles/',
    params: data
  })
}

export function updateArticle(id: number, data: Api.Article.ArticleUpdate) {
  return request.put<Api.Article.ArticleResponse>({
    url: `/v1/articles/${id}`,
    params: data
  })
}

export function deleteArticle(id: number) {
  return request.del({
    url: `/v1/articles/${id}`
  })
}

export function likeArticle(id: number) {
  return request.post({
    url: `/v1/articles/${id}/like`
  })
}

export function collectArticle(id: number) {
  return request.post({
    url: `/v1/articles/${id}/collect`
  })
}