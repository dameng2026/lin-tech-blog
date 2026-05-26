import { AppRouteRecord } from '@/types/router'

export const projectsRoutes: AppRouteRecord = {
  path: '/projects',
  name: 'Projects',
  component: '/index/index',
  meta: {
    title: 'menus.projects.title',
    icon: 'ri:folder-line',
    roles: ['R_SUPER', 'R_ADMIN']
  },
  children: [
    {
      path: 'list',
      name: 'ProjectList',
      component: '/projects/list',
      meta: {
        title: 'menus.projects.list',
        icon: 'ri:list-checks-line',
        keepAlive: true,
        authList: [
          { title: '新增', authMark: 'add' },
          { title: '编辑', authMark: 'edit' },
          { title: '删除', authMark: 'delete' }
        ]
      }
    },
    {
      path: 'create',
      name: 'ProjectCreate',
      component: '/projects/create',
      meta: {
        title: 'menus.projects.create',
        icon: 'ri:plus-line',
        keepAlive: true,
        authList: [{ title: '创建', authMark: 'add' }]
      }
    },
    ]
}