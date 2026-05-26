import { AppRouteRecord } from '@/types/router'

export const settingsRoutes: AppRouteRecord = {
  path: '/settings',
  name: 'Settings',
  component: '/index/index',
  meta: {
    title: '系统设置',
    icon: 'ri:settings-3-line',
    roles: ['R_SUPER', 'R_ADMIN']
  },
  children: [
    {
      path: 'site',
      name: 'SiteSettings',
      component: '/settings/site',
      meta: {
        title: '站点设置',
        icon: 'ri:earth-line',
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN']
      }
    },
    {
      path: 'profile',
      name: 'ProfileManager',
      component: '/settings/profile',
      meta: {
        title: '关于我管理',
        icon: 'ri:user-heart-line',
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN']
      }
    }
  ]
}
