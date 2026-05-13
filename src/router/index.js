import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticlesView from '../views/ArticlesView.vue'
import ArticleDetailView from '../views/ArticleDetailView.vue'
import ProjectsView from '../views/ProjectsView.vue'
import ProjectDetailView from '../views/ProjectDetailView.vue'
import AboutView from '../views/AboutView.vue'
import LinksView from '../views/LinksView.vue'
import LeaveMessageView from '../views/LeaveMessageView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/articles',
    name: 'articles',
    component: ArticlesView
  },
  {
    path: '/article/:id',
    name: 'articleDetail',
    component: ArticleDetailView
  },
  {
    path: '/projects',
    name: 'projects',
    component: ProjectsView
  },
  {
    path: '/project/:id',
    name: 'projectDetail',
    component: ProjectDetailView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/links',
    name: 'links',
    component: LinksView
  },
  {
    path: '/messages',
    name: 'messages',
    component: LeaveMessageView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router