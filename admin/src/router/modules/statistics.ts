import { AppRouteRecord } from '@/types/router'

export const statisticsRoutes: AppRouteRecord = {
  path: '/statistics',
  name: 'Statistics',
  component: '/index/index',
  meta: {
    title: 'menus.statistics.title',
    icon: 'ri:bar-chart-2-line',
    roles: ['R_SUPER', 'R_ADMIN']
  },
  children: [
    {
      path: 'dashboard',
      name: 'StatisticsDashboard',
      component: '/statistics/dashboard',
      meta: {
        title: 'menus.statistics.dashboard',
        icon: 'ri:dashboard-line',
        keepAlive: true
      }
    },
    {
      path: 'articles',
      name: 'ArticleStatistics',
      component: '/statistics/articles',
      meta: {
        title: 'menus.statistics.articles',
        icon: 'ri:trending-up-line',
        keepAlive: true
      }
    },
    {
      path: 'archive',
      name: 'ArticleArchive',
      component: '/statistics/archive',
      meta: {
        title: 'menus.statistics.archive',
        icon: 'ri:archive-line',
        keepAlive: true
      }
    }
  ]
}
