import { AppRouteRecord } from '@/types/router'

export const contentRoutes: AppRouteRecord = {
  path: '/content',
  name: 'Content',
  component: '/index/index',
  meta: {
    title: '内容管理',
    icon: 'ri:article-line',
    roles: ['R_SUPER', 'R_ADMIN', 'user']
  },
  children: [
    {
      path: 'articles',
      name: 'Articles',
      component: '/article/list',
      meta: {
        title: '文章管理',
        icon: 'ri:file-text-line',
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN', 'user'],
        authList: [
          { title: '新增', authMark: 'add' },
          { title: '编辑', authMark: 'edit' },
          { title: '删除', authMark: 'delete' }
        ]
      }
    },
    {
      path: 'publish',
      name: 'PublishArticle',
      component: '/article/publish',
      meta: {
        title: '发布文章',
        icon: 'ri:edit-line',
        isHide: true,
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN', 'user']
      }
    },
    {
      path: 'detail/:id',
      name: 'ArticleDetail',
      component: '/article/detail',
      meta: {
        title: '文章详情',
        isHide: true,
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN', 'user']
      }
    },
    {
      path: 'categories',
      name: 'Categories',
      component: '/taxonomy/categories',
      meta: {
        title: '分类管理',
        icon: 'ri:folder-line',
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN', 'user'],
        authList: [
          { title: '新增', authMark: 'add' },
          { title: '编辑', authMark: 'edit' },
          { title: '删除', authMark: 'delete' }
        ]
      }
    },
    {
      path: 'tags',
      name: 'TechStack',
      component: '/taxonomy/tech-stack',
      meta: {
        title: '技术栈管理',
        icon: 'ri:stack-line',
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN', 'user']
      }
    },
    {
      path: 'projects',
      name: 'ProjectList',
      component: '/projects/list',
      meta: {
        title: '项目管理',
        icon: 'ri:folder-line',
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN', 'user'],
        authList: [
          { title: '新增', authMark: 'add' },
          { title: '编辑', authMark: 'edit' },
          { title: '删除', authMark: 'delete' }
        ]
      }
    },
    {
      path: 'project-create',
      name: 'ProjectCreate',
      component: '/projects/create',
      meta: {
        title: '创建项目',
        icon: 'ri:plus-line',
        isHide: true,
        keepAlive: true,
        roles: ['R_SUPER', 'R_ADMIN', 'user']
      }
    }
  ]
}