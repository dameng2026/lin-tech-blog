<template>
  <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-5">
    <div
      v-for="(item, index) in dataList"
      :key="index"
      class="art-card relative flex flex-col justify-center h-35 px-5"
    >
      <span class="text-g-700 text-sm">{{ item.des }}</span>
      <ArtCountTo class="text-[26px] font-medium mt-2" :target="item.num" :duration="1300" />
      <div class="flex-c mt-1">
        <span class="text-xs text-g-600">较上周</span>
        <span
          class="ml-1 text-xs font-semibold"
          :class="[item.change.indexOf('+') === -1 ? 'text-danger' : 'text-success']"
        >
          {{ item.change }}
        </span>
      </div>
      <div
        class="absolute top-0 bottom-0 right-5 m-auto size-12.5 rounded-xl flex-cc bg-theme/10"
      >
        <ArtSvgIcon :icon="item.icon" class="text-xl text-theme" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue'

  interface Props {
    articlesCount: number
    projectsCount: number
    usersCount: number
    totalViews: number
    daysRunning: number
  }

  const props = defineProps<Props>()

  interface CardDataItem {
    des: string
    icon: string
    startVal: number
    duration: number
    num: number
    change: string
  }

  const dataList = computed<CardDataItem[]>(() => [
    {
      des: '文章总数',
      icon: 'ri:article-line',
      startVal: 0,
      duration: 1000,
      num: props.articlesCount,
      change: '+15%'
    },
    {
      des: '项目总数',
      icon: 'ri:code-box-line',
      startVal: 0,
      duration: 1000,
      num: props.projectsCount,
      change: '+8%'
    },
    {
      des: '用户总数',
      icon: 'ri:group-line',
      startVal: 0,
      duration: 1000,
      num: props.usersCount,
      change: '+30%'
    },
    {
      des: '总访问量',
      icon: 'ri:eye-line',
      startVal: 0,
      duration: 1000,
      num: props.totalViews,
      change: '+22%'
    },
    {
      des: '运行天数',
      icon: 'ri:calendar-check-line',
      startVal: 0,
      duration: 1300,
      num: props.daysRunning,
      change: '+1'
    }
  ])
</script>
