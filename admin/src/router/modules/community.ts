import { AppRouteRecord } from '@/types/router'

export const communityRoutes: AppRouteRecord = {
  path: '/community',
  name: 'Community',
  component: '/index/index',
  meta: {
    title: '互动社区',
    icon: 'ri:chat-smile-2-line',
    roles: ['R_SUPER', 'R_ADMIN', 'user']
  },
  children: [
    {
      path: 'comments',
      name: 'Comments',
      component: '/article/comment',
      meta: {
        title: '评论管理',
        icon: 'ri:chat-3-line',
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN', 'user']
      }
    },
    {
      path: 'messages',
      name: 'Messages',
      component: '/content/guestbook',
      meta: {
        title: '留言板管理',
        icon: 'ri:message-3-line',
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN', 'user']
      }
    },
    {
      path: 'users',
      name: 'Users',
      component: '/system/user',
      meta: {
        title: '用户管理',
        icon: 'ri:group-line',
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN']
      }
    }
  ]
}
