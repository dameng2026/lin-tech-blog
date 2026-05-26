<template>
  <div class="min-h-screen bg-[#f8f9fc]">
    <!-- PDF下载弹窗 -->
    <PdfDownloadModal 
      :visible="isVisible" 
      @close="closeModal" 
      @download="handleDownload" 
    />
    
    <!-- 登录/注册弹窗 -->
    <AuthModal 
      :visible="authVisible" 
      @close="closeAuthModal" 
      @login="handleLogin" 
      @register="handleRegister" 
    />
    
    <!-- 左侧侧边栏 - 桌面端 -->
    <aside class="hidden lg:flex w-64 bg-white border-r border-gray-200 flex-col fixed h-full z-20">
      <div class="p-6 border-b border-gray-200">
        <h1 class="text-xl font-bold text-blue-600 flex items-center">
          <span class="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center text-white font-bold mr-2">M</span>
          {{ siteSettings.site_name || "Lin's Tech Blog" }}
        </h1>
      </div>
      <nav class="flex-1 p-4 overflow-y-auto">
        <ul class="space-y-1">
          <li>
            <router-link to="/" class="flex items-center px-3 py-3 rounded-lg text-gray-600 hover:bg-gray-50" active-class="bg-blue-50 !text-blue-600 !font-medium">
              <img :src="isActiveRoute('/') ? '/icons/home-blue.svg' : '/icons/home-grey.svg'" alt="首页" class="w-5 h-5 mr-3">
              首页
            </router-link>
          </li>
          <li>
            <router-link to="/articles" class="flex items-center px-3 py-3 rounded-lg text-gray-600 hover:bg-gray-50" active-class="bg-blue-50 !text-blue-600 !font-medium">
              <img :src="isActiveRoute('/articles') ? '/icons/article-blue.svg' : '/icons/article-grey.svg'" alt="文章" class="w-5 h-5 mr-3">
              文章
            </router-link>
          </li>
          <li>
            <router-link to="/projects" class="flex items-center px-3 py-3 rounded-lg text-gray-600 hover:bg-gray-50" active-class="bg-blue-50 !text-blue-600 !font-medium">
              <img :src="isActiveRoute('/projects') ? '/icons/project-blue.svg' : '/icons/project-grey.svg'" alt="项目" class="w-5 h-5 mr-3">
              项目
            </router-link>
          </li>
          <li>
            <router-link to="/about" class="flex items-center px-3 py-3 rounded-lg text-gray-600 hover:bg-gray-50" active-class="bg-blue-50 !text-blue-600 !font-medium">
              <img :src="isActiveRoute('/about') ? '/icons/about-blue.svg' : '/icons/about-grey.svg'" alt="关于" class="w-5 h-5 mr-3">
              关于
            </router-link>
          </li>
          <li>
            <router-link to="/links" class="flex items-center px-3 py-3 rounded-lg text-gray-600 hover:bg-gray-50" active-class="bg-blue-50 !text-blue-600 !font-medium">
              <img :src="isActiveRoute('/links') ? '/icons/Blogroll-blue.svg' : '/icons/Blogroll-grey.svg'" alt="友链" class="w-5 h-5 mr-3">
              友链
            </router-link>
          </li>
          <li>
            <router-link to="/messages" class="flex items-center px-3 py-3 rounded-lg text-gray-600 hover:bg-gray-50" active-class="bg-blue-50 !text-blue-600 !font-medium">
              <img :src="isActiveRoute('/messages') ? '/icons/info-blue.svg' : '/icons/info-grey.svg'" alt="留言" class="w-5 h-5 mr-3">
              留言
            </router-link>
          </li>
        </ul>
      </nav>
      <!-- 底部固定区域 -->
      <div class="mt-auto flex flex-col border-t border-gray-200">
        <div class="p-4">
          <!-- 四个按钮 -->
          <div class="flex justify-center space-x-4 mb-4">
            <a :href="`mailto:${siteSettings.email}`" class="w-8 h-8 flex items-center justify-center rounded-full bg-gray-100 hover:bg-gray-200">
              <img src="/icons/email-grey.svg" alt="邮件" class="w-4 h-4">
            </a>
            <a :href="siteSettings.github_url || '#'" class="w-8 h-8 flex items-center justify-center rounded-full bg-gray-100 hover:bg-gray-200">
              <img src="/icons/github-grey.svg" alt="GitHub" class="w-4 h-4">
            </a>
          </div>
          <!-- 深色模式 -->
          <button class="w-full flex items-center justify-center px-4 py-2 bg-gray-100 rounded-lg text-gray-600 hover:bg-gray-200">
            <img src="/icons/moon.svg" alt="深色模式" class="w-4 h-4 mr-2">
            深色模式
          </button>
        </div>
        <div class="p-4 text-xs text-gray-500 text-center border-t border-gray-100 bg-white">
          <p>© {{ currentYear }} {{ siteSettings.site_name || "Lin's Tech Blog" }}</p>
          <p v-if="siteSettings.icp_number">{{ siteSettings.icp_number }}</p>
          <p class="mt-1">已运行 {{ runningDays }} 天</p>
        </div>
      </div>
    </aside>

    <!-- 右侧内容区 -->
    <main class="ml-64 p-6">
      <div>
        <!-- 顶部导航栏 - 桌面端 -->
        <header class="hidden lg:block px-6 py-4 border-b border-gray-200 bg-[#fefefe]">
          <div class="flex justify-between items-center">
            <nav class="flex space-x-6">
              <router-link to="/" :class="isActiveRoute('/') ? 'text-blue-600 font-medium' : 'text-gray-600 hover:text-gray-900'">首页</router-link>
              <router-link to="/articles" :class="isActiveRoute('/articles') ? 'text-blue-600 font-medium' : 'text-gray-600 hover:text-gray-900'">文章</router-link>
              <router-link to="/projects" :class="isActiveRoute('/projects') ? 'text-blue-600 font-medium' : 'text-gray-600 hover:text-gray-900'">项目</router-link>
              <router-link to="/about" :class="isActiveRoute('/about') ? 'text-blue-600 font-medium' : 'text-gray-600 hover:text-gray-900'">关于</router-link>
              <router-link to="/links" :class="isActiveRoute('/links') ? 'text-blue-600 font-medium' : 'text-gray-600 hover:text-gray-900'">友链</router-link>
              <router-link to="/messages" :class="isActiveRoute('/messages') ? 'text-blue-600 font-medium' : 'text-gray-600 hover:text-gray-900'">留言</router-link>
            </nav>
            <div class="flex items-center space-x-4">
              <div class="relative">
                <input type="text" placeholder="搜索文章/项目" class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent" />
                <svg class="w-5 h-5 text-gray-400 absolute left-3 top-2.5" fill="currentColor" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
              </div>
              <button @click="openAuthModal(siteSettings.login_enabled)" class="w-8 h-8 rounded-full bg-blue-600 flex items-center justify-center text-white font-bold cursor-pointer hover:bg-blue-700 transition-colors">
                {{ siteSettings.author_name ? siteSettings.author_name.charAt(0) : 'L' }}
              </button>
            </div>
          </div>
        </header>

        <!-- 顶部导航栏 - 移动端 -->
        <header class="lg:hidden px-4 py-3 border-b border-gray-100 bg-white">
          <div class="flex justify-between items-center">
            <h1 class="text-lg font-bold text-blue-600 flex items-center">
              <span class="w-7 h-7 bg-blue-600 rounded-lg flex items-center justify-center text-white font-bold mr-2">L</span>
              {{ siteSettings.site_name || "Lin's Blog" }}
            </h1>
            <div class="flex items-center space-x-3">
              <div class="relative">
                <input type="text" placeholder="搜索" class="w-28 pl-8 pr-3 py-1.5 text-sm border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent" />
                <svg class="w-4 h-4 text-gray-400 absolute left-2 top-2" fill="currentColor" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
              </div>
              <button @click="openAuthModal(siteSettings.login_enabled)" class="w-8 h-8 rounded-full bg-blue-600 flex items-center justify-center text-white font-bold">
                {{ siteSettings.author_name ? siteSettings.author_name.charAt(0) : 'L' }}
              </button>
            </div>
          </div>
        </header>

        <!-- 路由内容区 -->
        <div>
          <router-view />
        </div>
      </div>
    </main>

    <!-- 移动端底部导航栏 -->
    <nav class="lg:hidden fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 z-50 px-2 py-1">
      <div class="flex justify-around items-center">
        <router-link to="/" class="flex flex-col items-center py-1.5 px-2 rounded-lg" :class="isActiveRoute('/') ? 'text-blue-600' : 'text-gray-500'">
          <img :src="isActiveRoute('/') ? '/icons/home-blue.svg' : '/icons/home-grey.svg'" alt="首页" class="w-5 h-5" />
          <span class="text-[10px] mt-0.5">首页</span>
        </router-link>
        <router-link to="/articles" class="flex flex-col items-center py-1.5 px-2 rounded-lg" :class="isActiveRoute('/articles') ? 'text-blue-600' : 'text-gray-500'">
          <img :src="isActiveRoute('/articles') ? '/icons/article-blue.svg' : '/icons/article-grey.svg'" alt="文章" class="w-5 h-5" />
          <span class="text-[10px] mt-0.5">文章</span>
        </router-link>
        <router-link to="/projects" class="flex flex-col items-center py-1.5 px-2 rounded-lg" :class="isActiveRoute('/projects') ? 'text-blue-600' : 'text-gray-500'">
          <img :src="isActiveRoute('/projects') ? '/icons/project-blue.svg' : '/icons/project-grey.svg'" alt="项目" class="w-5 h-5" />
          <span class="text-[10px] mt-0.5">项目</span>
        </router-link>
        <router-link to="/links" class="flex flex-col items-center py-1.5 px-2 rounded-lg" :class="isActiveRoute('/links') ? 'text-blue-600' : 'text-gray-500'">
          <img :src="isActiveRoute('/links') ? '/icons/Blogroll-blue.svg' : '/icons/Blogroll-grey.svg'" alt="友链" class="w-5 h-5" />
          <span class="text-[10px] mt-0.5">友链</span>
        </router-link>
        <router-link to="/messages" class="flex flex-col items-center py-1.5 px-2 rounded-lg" :class="isActiveRoute('/messages') ? 'text-blue-600' : 'text-gray-500'">
          <img :src="isActiveRoute('/messages') ? '/icons/info-blue.svg' : '/icons/info-grey.svg'" alt="留言" class="w-5 h-5" />
          <span class="text-[10px] mt-0.5">留言</span>
        </router-link>
      </div>
    </nav>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import PdfDownloadModal from './components/PdfDownloadModal.vue'
import AuthModal from './components/AuthModal.vue'
import { usePdfModal } from './composables/usePdfModal'
import { useAuthModal } from './composables/useAuthModal'
import { fetchSiteSettings } from './api/site'

const route = useRoute()
const { isVisible, closeModal, handleDownload } = usePdfModal()
const { isVisible: authVisible, openModal: openAuthModal, closeModal: closeAuthModal, handleLogin, handleRegister } = useAuthModal()

const siteSettings = ref({})

const currentYear = computed(() => new Date().getFullYear())

const runningDays = computed(() => {
  if (!siteSettings.value.site_start_date) return 0
  const startDate = new Date(siteSettings.value.site_start_date)
  const now = new Date()
  const diffTime = Math.abs(now - startDate)
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
  return diffDays
})

const isActiveRoute = (path) => {
  return route.path === path
}

onMounted(async () => {
  const settings = await fetchSiteSettings()
  if (settings) {
    siteSettings.value = settings
    if (settings.site_title) {
      const titleElement = document.getElementById('pageTitle')
      if (titleElement) {
        titleElement.textContent = settings.site_title
      }
    }
  }
})
</script>

<style scoped>
.px-6 {
  padding-left: 1.75rem;
  padding-right: 1.75rem;
}

@media (max-width: 1024px) {
  main {
    margin-left: 0 !important;
    padding: 0.5rem !important;
    padding-bottom: 4.5rem !important;
  }
  
  main > div {
    border-radius: 0 !important;
    box-shadow: none !important;
    border: none !important;
  }
}
</style>
