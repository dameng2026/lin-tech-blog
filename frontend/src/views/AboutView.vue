﻿﻿﻿﻿<template>
  <div class="page-container p-[1.75rem] bg-[#fefefe]">
    <div class="min-h-screen">
      <div class="mx-auto w-full min-h-screen">
        <!-- ===== 顶部个人信息 - 移动端 ===== -->
        <div class="lg:hidden bg-white rounded-2xl shadow-sm p-5 mb-4">
          <div class="flex items-center gap-4 mb-4">
            <div class="w-20 h-20 rounded-full bg-gray-200 overflow-hidden flex-shrink-0">
              <img src="/images/avatar.png" alt="Lin" class="w-full h-full object-cover">
            </div>
            <div>
              <h1 class="text-xl font-bold text-gray-900 mb-1">{{ siteInfo.author_name }}</h1>
            <p class="text-sm text-gray-600">{{ siteInfo.description }}</p>
            </div>
          </div>
          <p class="text-gray-600 text-sm mb-4">{{ siteInfo.bio }}</p>
          <div class="grid grid-cols-2 gap-4">
            <div class="flex items-center text-xs text-gray-500">
              <img src="/icons/position-grey.svg" alt="地址" class="w-4 h-4 mr-2">
              {{ siteInfo.location }}
            </div>
            <div class="flex items-center text-xs text-gray-500">
              <img src="/icons/email-grey.svg" alt="邮箱" class="w-4 h-4 mr-2">
              {{ siteInfo.email }}
            </div>
            <div class="flex items-center text-xs text-gray-500">
              <img src="/icons/github-grey.svg" alt="GitHub" class="w-4 h-4 mr-2">
              {{ siteInfo.github_url }}
            </div>
            <div class="flex items-center text-xs text-gray-500">
              <img src="/icons/project-grey.svg" alt="开发经验" class="w-4 h-4 mr-2">
              {{ siteInfo.experience }}
            </div>
          </div>
        </div>

        <!-- ===== 顶部个人信息 - 桌面端 ===== -->
        <div class="hidden lg:block bg-[#f2f5fd] rounded-2xl pt-12 pr-12 pl-16 mb-4 overflow-hidden relative min-h-[420px]">
          <div class="absolute right-0 top-0 w-[50%] h-[95%] flex items-center justify-end pointer-events-none pr-8 pt-4">
            <img src="/images/hero-3d.png" alt="AI Cube" class="w-auto h-full object-contain object-right-center">
          </div>

          <div class="relative z-10 h-full flex flex-col justify-between py-8">
            <div class="flex flex-row items-start gap-10 flex-1">
              <div class="w-44 h-44 rounded-full bg-gray-200 overflow-hidden flex-shrink-0 -mt-4">
              <img src="/images/avatar.png" alt="Lin" class="w-full object-cover object-top">
            </div>

            <div class="flex-1 max-w-[19rem] pt-1">
              <h1 class="text-[2rem] font-bold text-gray-900 mb-4">{{ siteInfo.author_name }}</h1>
              <p class="text-[1.15rem] text-gray-600 mb-[2.5rem]">{{ siteInfo.description }}</p>
              <p class="text-gray-500 leading-loose text-[0.9rem]">{{ siteInfo.bio }}</p>
            </div>
          </div>

          <div class="flex flex-wrap gap-14 mt-12">
            <div class="flex items-center text-[0.8rem] text-gray-500">
              <img src="/icons/position-grey.svg" alt="地址" class="w-5 h-5 mr-3">
              {{ siteInfo.location }}
            </div>
            <div class="flex items-center text-[0.8rem] text-gray-500">
              <img src="/icons/email-grey.svg" alt="邮箱" class="w-5 h-5 mr-3">
              {{ siteInfo.email }}
            </div>
            <div class="flex items-center text-[0.8rem] text-gray-500">
              <img src="/icons/github-grey.svg" alt="GitHub" class="w-5 h-5 mr-3">
              {{ siteInfo.github_url }}
            </div>
            <div class="flex items-center text-[0.8rem] text-gray-500">
              <img src="/icons/project-grey.svg" alt="开发经验" class="w-5 h-5 mr-3">
              {{ siteInfo.experience }}</div>
          </div>
        </div>
      </div>

      <!-- 技术栈和核心技能 -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4">
        <!-- 技术栈 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6">
          <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26] mb-3 lg:mb-4">技术栈</h2>
          <div class="flex flex-wrap gap-2">
            <span v-for="tech in techStack" :key="tech" class="px-3 py-1 bg-[#f0f3ff] text-[#1f5cff] rounded-full text-xs font-medium border border-[#cad4fc]">{{ tech }}</span>
          </div>
        </div>

        <!-- 核心技能 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6">
          <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26] mb-3 lg:mb-4">核心技能</h2>
          <div class="space-y-3 lg:space-y-4">
            <div v-for="skill in coreSkills" :key="skill.name">
              <div class="flex justify-between mb-1.5">
                <span class="text-xs lg:text-sm text-gray-700">{{ skill.name }}</span>
                <span class="text-xs lg:text-sm text-gray-500">{{ skill.level }}%</span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-1">
                <div class="bg-blue-600 h-1 rounded-full" :style="{ width: skill.level + '%' }"></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 工作经历和教育背景 -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4">
        <!-- 工作经历 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6">
          <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26] mb-4 lg:mb-6">工作经历</h2>
          <div class="relative">
            <!-- 时间线 -->
            <div class="absolute left-0 top-2 bottom-0 w-0.5 bg-[#edf0f7] ml-2"></div>
            <div class="space-y-6 lg:space-y-8">
              <div v-for="(exp, idx) in workExperiences" :key="idx" class="relative pl-6 lg:pl-8">
                <div class="absolute left-0 top-1.5 w-3 h-3 lg:w-3.5 lg:h-3.5 bg-blue-500 rounded-full border-2 border-white shadow"></div>
                <p class="text-[#959db0] text-xs lg:text-[0.95rem] mb-1 lg:mb-2">{{ exp.period }}</p>
                <h3 class="text-sm lg:text-[1.2rem] font-semibold text-[#161b26] mb-1 lg:mb-2">{{ exp.title }}</h3>
                <p class="text-[#6f7687] text-xs lg:text-[0.95rem] leading-relaxed mb-2 lg:mb-4">{{ exp.desc }}</p>
                <div class="flex flex-wrap gap-1.5 lg:gap-2">
                  <span v-for="tag in exp.tags" :key="tag" class="px-2 py-1 bg-[#f6f6fb] rounded-lg text-xs text-[#6f7687]">{{ tag }}</span>
                </div>
              </div>
            </div>
          </div>
          <button @click="openModal" class="text-blue-600 hover:underline flex items-center mt-4 lg:mt-6 text-xs lg:text-[0.95rem] font-medium">
            查看完整履历（PDF）<span class="ml-2">→</span>
          </button>
        </div>
        <!-- 教育背景和我的理念 -->
        <div class="flex flex-col h-full">
          <!-- 教育背景 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6 mb-4">
            <div class="flex items-center mb-3 lg:mb-5">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#eef3ff] rounded-xl flex items-center justify-center mr-3 lg:mr-4">
                <img src="/icons/education.svg" alt="教育背景" class="w-5 h-5 lg:w-6 lg:h-6">
              </div>
              <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26]">教育背景</h2>
            </div>
            <div class="space-y-4 lg:space-y-6">
              <div v-for="(edu, idx) in educations" :key="idx">
                <div class="flex justify-between items-start mb-2 lg:mb-3">
                  <div>
                    <p class="text-[#959db0] text-xs lg:text-[0.95rem] mb-1 lg:mb-2">{{ edu.period }}</p>
                    <h3 class="text-sm lg:text-[1.2rem] font-semibold text-[#161b26]">{{ edu.degree }}</h3>
                    <p class="text-[#959db0] text-xs lg:text-[0.95rem] mt-1 lg:mt-2">{{ edu.school }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- 我的理念 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6 flex-1">
            <div class="flex items-center mb-4 lg:mb-6">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#eef3ff] rounded-xl flex items-center justify-center mr-3 lg:mr-4">
                <img src="/icons/quotation.svg" alt="我的理念" class="w-5 h-5 lg:w-6 lg:h-6">
              </div>
              <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26]">我的理念</h2>
            </div>
            <div class="space-y-3 lg:space-y-5">
              <p class="text-[#6f7687] text-xs lg:text-[0.95rem] leading-relaxed">{{ mottoText }}</p>
              <div v-for="(item, idx) in mottoItems" :key="idx" class="flex items-center">
                <div class="w-5 h-5 lg:w-6 lg:h-6 text-blue-500 mr-3 lg:mr-4 flex items-center justify-center">
                  <img src="/icons/quotation.svg" alt="引用" class="w-4 h-4 lg:w-5 lg:h-5">
                </div>
                <p class="text-[#6f7687] text-xs lg:text-[0.95rem] font-medium">{{ item }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 兴趣爱好和站点数据 -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4">
        <!-- 兴趣爱好 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6">
          <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26] mb-3 lg:mb-4">兴趣爱好</h2>
          <div class="flex justify-between">
            <div v-for="(interest, idx) in interestNames" :key="idx" class="flex flex-col items-center">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#f6f6fb] rounded-lg flex items-center justify-center mb-1.5 lg:mb-2">
                <img :src="`/icons/${interestIcons[interest] || 'explore'}.svg`" :alt="interest" class="w-5 h-5 lg:w-6 lg:h-6 text-blue-600">
              </div>
              <span class="text-xs lg:text-sm text-gray-700">{{ interest }}</span>
            </div>
          </div>
        </div>
        <!-- 站点数据 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6">
          <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26] mb-3 lg:mb-4">站点数据</h2>
          <div class="flex justify-between">
            <div class="flex flex-col items-center">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#f6f6fb] rounded-lg flex items-center justify-center mb-2 lg:mb-3">
                <img src="/icons/article-blue.svg" alt="文章" class="w-5 h-5 lg:w-6 lg:h-6 text-blue-600">
              </div>
              <div class="text-xs text-gray-900 mt-0.5 lg:mt-1">文章</div>
              <div class="text-lg lg:text-1xl font-bold text-gray-900">{{ siteStats.articles_count }}</div>
            </div>
            <div class="flex flex-col items-center">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#f6f6fb] rounded-lg flex items-center justify-center mb-2 lg:mb-3">
                <img src="/icons/project-grey.svg" alt="项目" class="w-5 h-5 lg:w-6 lg:h-6 text-blue-600">
              </div>
              <div class="text-xs text-gray-900 mt-0.5 lg:mt-1">项目</div>
              <div class="text-lg lg:text-1xl font-bold text-gray-900">{{ siteStats.projects_count }}</div>
            </div>
            <div class="flex flex-col items-center">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#f6f6fb] rounded-lg flex items-center justify-center mb-2 lg:mb-3">
                <img src="/icons/eye.svg" alt="访问" class="w-5 h-5 lg:w-6 lg:h-6 text-blue-600">
              </div>
              <div class="text-xs text-gray-900 mt-0.5 lg:mt-1">访问</div>
              <div class="text-lg lg:text-1xl font-bold text-gray-900">{{ siteStats.total_views }}</div>
            </div>
            <div class="flex flex-col items-center">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#f6f6fb] rounded-lg flex items-center justify-center mb-2 lg:mb-3">
                <img src="/icons/calendar.svg" alt="运行天数" class="w-5 h-5 lg:w-6 lg:h-6 text-blue-600">
              </div>
              <div class="text-xs text-gray-900 mt-0.5 lg:mt-1">运行天数</div>
              <div class="text-lg lg:text-1xl font-bold text-gray-900">{{ siteStats.days_since_start }}</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 最近发布和联系方式 -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
        <!-- 最近发布 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6">
          <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26] mb-3 lg:mb-4">最近发布</h2>
          <div class="space-y-3 lg:space-y-4">
            <div v-for="(post, idx) in recentPosts" :key="idx" class="flex items-center justify-between">
              <div class="flex items-center flex-1 min-w-0">
                <span class="w-1.5 h-1.5 lg:w-2 lg:h-2 bg-blue-500 rounded-full mr-2 lg:mr-3 flex-shrink-0"></span>
                <a v-if="post.link" :href="post.link" class="text-blue-600 hover:text-blue-700 cursor-pointer text-xs lg:text-sm truncate">{{ post.title }}</a>
                <span v-else class="text-blue-600 text-xs lg:text-sm truncate">{{ post.title }}</span>
              </div>
              <span class="text-gray-400 text-xs lg:text-sm flex-shrink-0 ml-2">{{ post.time }}</span>
            </div>
            <div v-if="recentPosts.length === 0" class="text-gray-400 text-xs lg:text-sm text-center py-4">暂无最近动态</div>
          </div>
        </div>
        <!-- 联系方式 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6 min-h-[170px] relative overflow-hidden">
            <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26] mb-3 lg:mb-4">联系方式</h2>
            <p class="text-[#8a91a1] text-xs lg:text-[0.82rem] mb-4 lg:mb-6">欢迎交流与合作，一起探索技术的边界。</p>
            <div class="space-y-3 lg:space-y-4">
              <div class="flex items-center text-xs lg:text-[0.86rem] text-[#5f6677]"><img src="/icons/email-grey.svg" class="w-4 h-4 lg:w-5 lg:h-5 mr-2 lg:mr-3 opacity-70" alt="邮箱">{{ siteInfo.email }}</div>
              <div class="flex items-center text-xs lg:text-[0.86rem] text-[#5f6677]"><img src="/icons/github-grey.svg" class="w-4 h-4 lg:w-5 lg:h-5 mr-2 lg:mr-3 opacity-70" alt="GitHub">{{ siteInfo.github_url }}</div>
              <div class="flex items-center text-xs lg:text-[0.86rem] text-[#5f6677]"><img src="/icons/position-grey.svg" class="w-4 h-4 lg:w-5 lg:h-5 mr-2 lg:mr-3 opacity-70" alt="地址">{{ siteInfo.location }}</div>
            </div>
            <div class="hidden lg:block absolute right-6 bottom-4 w-[170px] opacity-90 pointer-events-none">
              <img src="/images/hero-3d.png" alt="decor" class="w-full h-auto object-contain">
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { usePdfModal } from '../composables/usePdfModal'
import { fetchProfile, fetchProfileSkills, fetchProfileExperiences, fetchProfileEducation } from '../api/profile'
import { fetchSiteSettings, fetchSiteStatistics } from '../api/site'
import { fetchArticles } from '../api/articles'
import { fetchProjects } from '../api/projects'

const { openModal } = usePdfModal()

const profile = ref({})
const skills = ref([])
const experiences = ref([])
const education = ref([])
const loading = ref(true)

const siteInfo = ref({
  author_name: '',
  description: '',
  bio: '',
  location: '',
  email: '',
  github_url: '',
  experience: ''
})

const mottoText = ref('')
const mottoItems = ref<string[]>([])
const interestNames = ref<string[]>([])
const interestIcons: Record<string, string> = {
  '技术探索': 'explore', '开源贡献': 'contribution', '阅读写作': 'reading',
  '旅行': 'travel', '健身运动': 'sports', '摄影': 'photography',
  '音乐': 'music', '游戏': 'game', '电影': 'movie', '美食': 'food'
}

const siteStats = ref({
  articles_count: 0,
  projects_count: 0,
  total_views: '0',
  days_since_start: 0
})

const recentPosts = ref<{ title: string; time: string; link?: string; type: string }[]>([])

const techStack = ref<string[]>([])
const coreSkills = ref<{ name: string; level: number }[]>([])
const workExperiences = ref<{ period: string; title: string; desc: string; tags: string[] }[]>([])
const educations = ref<{ period: string; degree: string; school: string }[]>([])

function timeAgo(dateStr: string): string {
  if (!dateStr) return ''
  const now = new Date()
  const date = new Date(dateStr)
  const diffMs = now.getTime() - date.getTime()
  const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24))
  if (diffDays === 0) return '今天'
  if (diffDays === 1) return '昨天'
  if (diffDays < 7) return `${diffDays} 天前`
  if (diffDays < 30) return `${Math.floor(diffDays / 7)} 周前`
  if (diffDays < 365) return `${Math.floor(diffDays / 30)} 个月前`
  return `${Math.floor(diffDays / 365)} 年前`
}

function formatViews(views: number): string {
  if (!views) return '0'
  if (views >= 10000) return (views / 10000).toFixed(1).replace(/\.0$/, '') + 'w'
  if (views >= 1000) return (views / 1000).toFixed(1).replace(/\.0$/, '') + 'k'
  return String(views)
}

async function loadData() {
  loading.value = true
  try {
    const [profileData, settingsData, skillsData, experiencesData, educationData, statsData, articlesData, projectsData] = await Promise.all([
      fetchProfile().catch(() => null),
      fetchSiteSettings().catch(() => null),
      fetchProfileSkills().catch(() => null),
      fetchProfileExperiences().catch(() => null),
      fetchProfileEducation().catch(() => null),
      fetchSiteStatistics().catch(() => null),
      fetchArticles({ page: 1, size: 3, sort_by: 'created_at' }).catch(() => null),
      fetchProjects({ page: 1, size: 3, sort_by: 'created_at' }).catch(() => null)
    ])

    if (settingsData) {
      siteInfo.value = {
        author_name: settingsData.author_name ?? '',
        description: settingsData.description ?? '',
        bio: settingsData.bio ?? '',
        location: settingsData.location ?? '',
        email: settingsData.email ?? '',
        github_url: settingsData.github_url ?? '',
        experience: settingsData.experience ?? ''
      }
      if (settingsData.bio_motto) mottoText.value = settingsData.bio_motto
      if (settingsData.bio_motto_items) {
        mottoItems.value = settingsData.bio_motto_items.split('\n').filter((s: string) => s.trim())
      }
      if (settingsData.bio_interests) {
        interestNames.value = settingsData.bio_interests.split(',').map((s: string) => s.trim()).filter(Boolean)
      }
    }

    if (profileData?.bio) siteInfo.value.bio = profileData.bio

    if (skillsData && skillsData.length > 0) {
      coreSkills.value = skillsData.map((s: any) => ({
        name: s.name,
        level: s.proficiency ?? 0
      }))
      techStack.value = skillsData.map((s: any) => s.name)
    }

    if (experiencesData && experiencesData.length > 0) {
      workExperiences.value = experiencesData.map((e: any) => ({
        period: `${e.start_date ?? ''} - ${e.end_date || '至今'}`,
        title: e.company ? `${e.title ?? ''} · ${e.company}` : (e.title ?? ''),
        desc: e.description ?? '',
        tags: e.tags ?? []
      }))
    }

    if (educationData && educationData.length > 0) {
      educations.value = educationData.map((e: any) => ({
        period: `${e.start_date ?? ''} - ${e.end_date ?? ''}`,
        degree: `${e.major ?? ''} · ${e.degree ?? ''}`,
        school: e.school ?? ''
      }))
    }

    if (statsData) {
      const d = statsData.data || statsData
      siteStats.value = {
        articles_count: d.articles_count ?? 0,
        projects_count: d.projects_count ?? 0,
        total_views: d.total_views != null ? formatViews(d.total_views) : '0',
        days_since_start: d.days_running ?? d.days_since_start ?? 0
      }
    }

    const posts: { title: string; time: string; link?: string; type: string }[] = []
    if (articlesData) {
      const articles = articlesData.articles || articlesData.records || articlesData.data || (Array.isArray(articlesData) ? articlesData : [])
      const list = Array.isArray(articles) ? articles : []
      for (const article of list.slice(0, 3)) {
        posts.push({
          title: article.title ?? '未知文章',
          time: timeAgo(article.created_at || article.publish_time),
          link: article.link || `/article/${article.id}`,
          type: 'article'
        })
      }
    }
    if (projectsData) {
      const projects = projectsData.projects || projectsData.records || projectsData.data || (Array.isArray(projectsData) ? projectsData : [])
      const list = Array.isArray(projects) ? projects : []
      for (const project of list.slice(0, 3)) {
        posts.push({
          title: `更新了项目 ${project.title ?? '未知项目'}`,
          time: timeAgo(project.created_at || project.updated_at),
          link: project.link || `/project/${project.id}`,
          type: 'project'
        })
      }
    }
    posts.sort((a, b) => {
      const order = ['今天', '昨天']
      const aIdx = order.includes(a.time) ? 0 : 1
      const bIdx = order.includes(b.time) ? 0 : 1
      return aIdx - bIdx
    })
    recentPosts.value = posts.slice(0, 3)

  } catch (e) {
    console.error('加载关于我数据失败', e)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadData()
})
</script>

<style scoped>
.page-container {
  background: #ffffff;
  padding: 1.75rem;
}
</style>
