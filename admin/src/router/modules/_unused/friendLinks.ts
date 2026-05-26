import { AppRouteRecord } from '@/types/router'

export const friendLinksRoutes: AppRouteRecord = {
  path: '/friend-links',
  name: 'FriendLinks',
  component: '/index/index',
  meta: {
    title: 'menus.friendLinks.title',
    icon: 'ri:link-line',
    roles: ['R_SUPER', 'R_ADMIN']
  },
  children: [
    {
      path: 'list',
      name: 'FriendLinkList',
      component: '/friend-links/list',
      meta: {
        title: 'menus.friendLinks.list',
        icon: 'ri:link-2-line',
        keepAlive: true,
        authList: [
          { title: '审核通过', authMark: 'approve' },
          { title: '拒绝', authMark: 'reject' },
          { title: '删除', authMark: 'delete' }
        ]
      }
    },
    {
      path: 'apply',
      name: 'FriendLinkApply',
      component: '/friend-links/apply',
      meta: {
        title: 'menus.friendLinks.apply',
        icon: 'ri:send-plane-line',
        keepAlive: true
      }
    }
  ]
}