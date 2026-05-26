<!-- 通知组件 -->
<template>
  <div
    class="art-notification-panel art-card-sm !shadow-xl"
    :style="{
      transform: show ? 'scaleY(1)' : 'scaleY(0.9)',
      opacity: show ? 1 : 0
    }"
    v-show="visible"
    @click.stop
  >
    <div class="flex-cb px-3.5 mt-3.5">
      <span class="text-base font-medium text-g-800">{{ $t('notice.title') }}</span>
    </div>

    <ul class="box-border flex items-end w-full h-12.5 px-3.5 border-b-d">
      <li
        v-for="(item, index) in barList"
        :key="index"
        class="h-12 leading-12 mr-5 overflow-hidden text-[13px] text-g-700 c-p select-none"
        :class="{ 'bar-active': barActiveIndex === index }"
        @click="changeBar(index)"
      >
        {{ item.name }}
        <span v-if="item.num > 0" class="ml-1 text-theme text-xs font-medium">({{ item.num }})</span>
      </li>
    </ul>

    <div class="w-full h-[calc(100%-95px)]">
      <div class="h-[calc(100%-60px)] overflow-y-scroll scrollbar-thin">
        <!-- 新评论 -->
        <ul v-show="barActiveIndex === 0">
          <li
            v-for="item in commentList"
            :key="'c-' + item.id"
            class="box-border flex-c px-3.5 py-3 c-p border-b border-g-100/60 last:border-b-0 hover:bg-g-200/60"
            @click="goComment(item)"
          >
            <div class="bg-blue-50 text-blue-600 size-9 leading-9 text-center rounded-lg flex-cc flex-shrink-0">
              <ArtSvgIcon class="text-lg" icon="ri:chat-3-line" />
            </div>
            <div class="w-[calc(100%-45px)] ml-3.5 min-w-0">
              <h4 class="text-xs font-normal leading-5 text-g-900 truncate">{{ item.guest_name || item.username || '匿名' }}: {{ item.content }}</h4>
              <p class="mt-1 text-xs text-g-500 truncate">{{ item.content_title || '#' + item.id }}</p>
            </div>
          </li>
          <li v-if="commentList.length === 0" class="text-center py-8 text-g-400 text-xs">
            暂无新评论
          </li>
        </ul>

        <!-- 新留言 -->
        <ul v-show="barActiveIndex === 1">
          <li
            v-for="item in messageList"
            :key="'m-' + item.id"
            class="box-border flex-c px-3.5 py-3 c-p border-b border-g-100/60 last:border-b-0 hover:bg-g-200/60"
            @click="goMessage(item)"
          >
            <div class="bg-green-50 text-green-600 size-9 leading-9 text-center rounded-lg flex-cc flex-shrink-0">
              <ArtSvgIcon class="text-lg" icon="ri:message-2-line" />
            </div>
            <div class="w-[calc(100%-45px)] ml-3.5 min-w-0">
              <h4 class="text-xs font-normal leading-5 text-g-900 truncate">{{ item.guest_name || '匿名' }}: {{ item.content }}</h4>
              <p class="mt-1 text-xs text-g-500">{{ item.created_at?.slice(0, 16) || '' }}</p>
            </div>
          </li>
          <li v-if="messageList.length === 0" class="text-center py-8 text-g-400 text-xs">
            暂无新留言
          </li>
        </ul>

        <!-- 新用户 -->
        <ul v-show="barActiveIndex === 2">
          <li
            v-for="item in userList"
            :key="'u-' + item.id"
            class="box-border flex-c px-3.5 py-3 c-p border-b border-g-100/60 last:border-b-0 hover:bg-g-200/60"
            @click="goUser(item)"
          >
            <div class="bg-purple-50 text-purple-600 size-9 leading-9 text-center rounded-lg flex-cc flex-shrink-0">
              <ArtSvgIcon class="text-lg" icon="ri:user-add-line" />
            </div>
            <div class="w-[calc(100%-45px)] ml-3.5 min-w-0">
              <h4 class="text-xs font-normal leading-5 text-g-900 truncate">{{ item.username }}</h4>
              <p class="mt-1 text-xs text-g-500">{{ item.email || '' }}</p>
            </div>
          </li>
          <li v-if="userList.length === 0" class="text-center py-8 text-g-400 text-xs">
            暂无新用户
          </li>
        </ul>
      </div>

      <div class="relative box-border w-full px-3.5">
        <ElButton class="w-full mt-3" @click="handleViewAll" v-ripple>
          {{ $t('notice.viewAll') }}
        </ElButton>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { computed, ref, watch } from 'vue'
  import { useRouter } from 'vue-router'
  import { useI18n } from 'vue-i18n'
  import { fetchComments, fetchGuestbooks } from '@/api/comments'
  import { fetchUsers } from '@/api/users'

  defineOptions({ name: 'ArtNotification' })

  const { t } = useI18n()
  const router = useRouter()

  const props = defineProps<{
    value: boolean
  }>()

  const emit = defineEmits<{
    'update:value': [value: boolean]
  }>()

  const show = ref(false)
  const visible = ref(false)
  const barActiveIndex = ref(0)

  const commentList = ref<any[]>([])
  const messageList = ref<any[]>([])
  const userList = ref<any[]>([])

  const barList = computed(() => [
    { name: t('notice.bar[0]'), num: commentList.value.length },
    { name: t('notice.bar[1]'), num: messageList.value.length },
    { name: t('notice.bar[2]'), num: userList.value.length }
  ])

  function showNotice(open: boolean) {
    if (open) {
      visible.value = true
      setTimeout(() => {
        show.value = true
      }, 5)
      fetchData()
    } else {
      show.value = false
      setTimeout(() => {
        visible.value = false
      }, 350)
    }
  }

  async function fetchData() {
    try {
      const [commentData, messageData, userData] = await Promise.all([
        fetchComments({ size: 5 }),
        fetchGuestbooks({ size: 5 }),
        fetchUsers({ size: 5 })
      ])
      commentList.value = commentData?.comments || []
      messageList.value = messageData?.comments || []
      userList.value = userData?.users || []
    } catch {}
  }

  function changeBar(index: number) {
    barActiveIndex.value = index
  }

  function goComment(item: any) {
    emit('update:value', false)
    if (item.article_id) {
      router.push({ path: '/community/comments', query: { article_id: item.article_id, title: item.content_title } })
    } else if (item.project_id) {
      router.push({ path: '/community/comments', query: { project_id: item.project_id, title: item.content_title } })
    } else {
      router.push('/community/comments')
    }
  }

  function goMessage(item: any) {
    emit('update:value', false)
    router.push('/content/guestbook')
  }

  function goUser(item: any) {
    emit('update:value', false)
    router.push('/community/users')
  }

  function handleViewAll() {
    const routes = ['/community/comments', '/content/guestbook', '/community/users']
    router.push(routes[barActiveIndex.value])
    emit('update:value', false)
  }

  watch(
    () => props.value,
    (newValue) => {
      showNotice(newValue)
    }
  )
</script>

<style scoped>
  @reference '@styles/core/tailwind.css';

  .art-notification-panel {
    @apply absolute 
    top-14.5 
    right-5 
    w-90 
    h-125 
    overflow-hidden 
    transition-all 
    duration-300
    origin-top 
    will-change-[top,left] 
    max-[640px]:top-[65px]
    max-[640px]:right-0
    max-[640px]:w-full 
    max-[640px]:h-[80vh];
  }

  .bar-active {
    color: var(--theme-color) !important;
    border-bottom: 2px solid var(--theme-color);
  }

  .scrollbar-thin::-webkit-scrollbar {
    width: 5px !important;
  }

  .dark .scrollbar-thin::-webkit-scrollbar-track {
    background-color: var(--default-box-color);
  }

  .dark .scrollbar-thin::-webkit-scrollbar-thumb {
    background-color: #222 !important;
  }
</style>