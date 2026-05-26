<template>
  <div class="art-card p-5 flex-b mb-5 max-sm:mb-4">
    <div>
      <h2 class="text-2xl font-medium">关于项目</h2>
      <p class="text-g-700 mt-1">{{ systemName }} 是一款兼具设计美学与高效开发的后台系统</p>
      <p class="text-g-700 mt-1">使用了 Vue3、TypeScript、Vite、Element Plus 等前沿技术</p>

      <div class="flex flex-wrap gap-3.5 max-w-150 mt-9">
        <div
          class="w-60 flex-cb h-12.5 px-3.5 border border-g-300 c-p rounded-lg text-sm bg-g-100 duration-300 hover:-translate-y-1 max-sm:w-full"
          v-for="link in linkList"
          :key="link.label"
          @click="goPage(link)"
        >
          <span class="text-g-700">{{ link.label }}</span>
          <ArtSvgIcon icon="ri:arrow-right-s-line" class="text-lg text-g-600" />
        </div>
      </div>
    </div>
    <img class="w-75 max-md:!hidden" src="@imgs/draw/draw1.png" alt="draw1" />
  </div>
</template>

<script setup lang="ts">
  import { useRouter } from 'vue-router'
  import AppConfig from '@/config'
  import { WEB_LINKS } from '@/utils/constants'

  const router = useRouter()
  const systemName = AppConfig.systemInfo.name

  interface LinkItem {
    label: string
    type: 'route' | 'external'
    url?: string
    route?: string
  }

  const linkList: LinkItem[] = [
    { label: '前台博客', type: 'external', url: 'http://localhost:5173' },
    { label: '使用文档', type: 'route', route: '/docs' },
    { label: 'Github', type: 'external', url: WEB_LINKS.GITHUB },
    { label: 'API 文档', type: 'external', url: 'http://localhost:8002/docs' }
  ]

  const goPage = (item: LinkItem): void => {
    if (item.type === 'route' && item.route) {
      router.push(item.route)
    } else if (item.type === 'external' && item.url) {
      window.open(item.url, '_blank', 'noopener,noreferrer')
    }
  }
</script>
