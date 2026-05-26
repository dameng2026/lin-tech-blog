import { AppRouteRecord } from '@/types/router'

export const filesRoutes: AppRouteRecord = {
  path: '/files',
  name: 'Files',
  component: '/index/index',
  meta: {
    title: 'menus.files.title',
    icon: 'ri:folder-open-line',
    roles: ['R_SUPER', 'R_ADMIN']
  },
  children: [
    {
      path: 'list',
      name: 'FileList',
      component: '/files/list',
      meta: {
        title: 'menus.files.list',
        icon: 'ri:file-list-line',
        keepAlive: true,
        authList: [
          { title: '上传', authMark: 'upload' },
          { title: '删除', authMark: 'delete' }
        ]
      }
    },
    {
      path: 'upload',
      name: 'FileUpload',
      component: '/files/upload',
      meta: {
        title: 'menus.files.upload',
        icon: 'ri:upload-line',
        keepAlive: true
      }
    }
  ]
}
