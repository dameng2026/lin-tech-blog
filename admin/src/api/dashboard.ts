import request from '@/utils/http'

export interface LatestArticle {
  id: number
  title: string
  created_at: string
}

export interface LatestProject {
  id: number
  name: string
  created_at: string
}

export interface PendingItems {
  friend_links: number
  guestbook_messages: number
  unapproved_comments: number
  resume_key_requests: number
}

export interface DashboardSummary {
  articles_count: number
  projects_count: number
  users_count: number
  total_views: number
  total_likes: number
  total_comments: number
  total_collects: number
  days_running: number
  visit_trend: number[]
  latest_articles: LatestArticle[]
  latest_projects: LatestProject[]
  pending: PendingItems
}

export function fetchDashboardSummary() {
  return request.get<DashboardSummary>({
    url: '/v1/dashboard/summary'
  })
}
