import request from '@/utils/http'

export interface SiteStats {
  articles_count: number
  projects_count: number
  total_views: number
  total_likes: number
  total_comments: number
  total_collects: number
  github_stars: number
  github_followers: number
  site_start_date: string
  days_running: number
}

export interface HotArticle {
  id: number
  title: string
  view_count: number
  like_count: number
  category: string
  created_at: string
}

export interface HotProject {
  id: number
  name: string
  view_count: number
  status: string
  created_at: string
}

export interface ArticleArchive {
  year: number
  month: number
  article_count: number
  articles: {
    id: number
    title: string
    created_at: string
  }[]
}

export interface VisitTrend {
  date: string
  count: number
}

export function fetchSiteStats() {
  return request.get<SiteStats>({
    url: '/v1/statistics/site'
  })
}

export function fetchVisitTrend(params?: { days?: number }) {
  return request.get<VisitTrend[]>({
    url: '/v1/statistics/visit-trend',
    params
  })
}

export function fetchHotArticles(params?: { limit?: number }) {
  return request.get<HotArticle[]>({
    url: '/v1/statistics/articles/hot',
    params
  })
}

export function fetchHotProjects(params?: { limit?: number }) {
  return request.get<HotProject[]>({
    url: '/v1/statistics/projects/hot',
    params
  })
}

export function fetchArticleArchive() {
  return request.get<ArticleArchive[]>({
    url: '/v1/statistics/articles/archive'
  })
}

export function fetchLatestComments(params?: { limit?: number }) {
  return request.get<any[]>({
    url: '/v1/statistics/latest-comments',
    params
  })
}

export function updateSiteStats() {
  return request.post<any>({
    url: '/v1/statistics/site/update'
  })
}

export function syncGithubStats() {
  return request.post<any>({
    url: '/v1/statistics/github/sync'
  })
}