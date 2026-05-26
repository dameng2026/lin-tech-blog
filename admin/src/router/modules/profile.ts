import { AppRouteRecord } from '@/types/router'

export const profileRoutes: AppRouteRecord = {
  path: '/profile',
  name: 'Profile',
  component: '/index/index',
  meta: {
    title: '个人设置',
    icon: 'ri:user-settings-line',
    roles: ['R_SUPER', 'R_ADMIN', 'user']
  },
  children: [
    {
      path: 'info',
      name: 'ProfileInfo',
      component: '/system/user-center',
      meta: {
        title: '修改信息',
        icon: 'ri:user-edit-line',
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN', 'user']
      }
    },
    {
      path: 'resume',
      name: 'Resume',
      component: '/profile/resume',
      meta: {
        title: '简历管理',
        icon: 'ri:file-list-2-line',
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN', 'user']
      }
    },
    {
      path: 'pdf-key',
      name: 'PdfKey',
      component: '/profile/resume-key',
      meta: {
        title: 'PDF密钥管理',
        icon: 'ri:key-2-line',
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN']
      }
    }
  ]
}
