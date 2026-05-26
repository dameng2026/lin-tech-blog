import { AppRouteRecord } from '@/types/router'

export const linksRoutes: AppRouteRecord = {
  path: '/links',
  name: 'Links',
  component: '/index/index',
  meta: {
    title: '友链系统',
    icon: 'ri:links-line',
    roles: ['R_SUPER', 'R_ADMIN', 'user']
  },
  children: [
    {
      path: 'friend-links',
      name: 'LinksList',
      component: '/links/list',
      meta: {
        title: '友链列表',
        icon: 'ri:link',
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN', 'user']
      }
    },
    {
      path: 'link-approval',
      name: 'LinkApproval',
      component: '/friend-links/list',
      meta: {
        title: '友链审批列表',
        icon: 'ri:file-check-line',
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN', 'user']
      }
    }
  ]
}