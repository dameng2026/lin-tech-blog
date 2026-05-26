import { AppRouteRecord } from '@/types/router'
import { dashboardRoutes } from './dashboard'
import { contentRoutes } from './content'
import { communityRoutes } from './community'
import { linksRoutes } from './links'
import { profileRoutes } from './profile'
import { settingsRoutes } from './settings'

export const routeModules: AppRouteRecord[] = [
  dashboardRoutes,
  contentRoutes,
  communityRoutes,
  linksRoutes,
  profileRoutes,
  settingsRoutes
]
