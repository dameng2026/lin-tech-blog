<template>
  <div class="art-card h-128 p-5">
    <div class="art-card-header">
      <div class="title">
        <h4>待处理事项</h4>
        <p>待处理<span class="text-danger">{{ totalPending }}</span></p>
      </div>
    </div>

    <div class="h-[calc(100%-40px)] overflow-auto">
      <ElScrollbar>
        <div
          class="flex-cb h-17.5 border-b border-g-300 text-sm last:border-b-0"
          v-for="(item, index) in list"
          :key="index"
        >
          <div class="flex items-center gap-3">
            <ArtSvgIcon :icon="item.icon" class="text-lg" :class="item.iconClass" />
            <div>
              <p class="text-sm">{{ item.title }}</p>
              <p class="text-g-500 mt-1">{{ item.status }}</p>
            </div>
          </div>
        </div>
        <div
          v-if="list.length === 0"
          class="flex items-center justify-center h-40 text-g-500 text-sm"
        >
          暂无待处理事项
        </div>
      </ElScrollbar>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue'

  interface PendingItem {
    title: string
    status: string
    icon: string
    iconClass: string
  }

  interface Props {
    friendLinks: number
    guestbookMessages: number
    unapprovedComments: number
    resumeKeyRequests: number
  }

  const props = defineProps<Props>()

  const totalPending = computed(() => {
    return props.friendLinks + props.guestbookMessages + props.unapprovedComments + props.resumeKeyRequests
  })

  const list = computed<PendingItem[]>(() => {
    const items: PendingItem[] = []
    if (props.friendLinks > 0) {
      items.push({
        title: '友链申请待审核',
        status: `${props.friendLinks} 条待处理`,
        icon: 'ri:link-m',
        iconClass: 'text-warning'
      })
    }
    if (props.guestbookMessages > 0) {
      items.push({
        title: '留言板新留言',
        status: `${props.guestbookMessages} 条未读`,
        icon: 'ri:message-3-line',
        iconClass: 'text-primary'
      })
    }
    if (props.unapprovedComments > 0) {
      items.push({
        title: '新的评论',
        status: `${props.unapprovedComments} 条待审核`,
        icon: 'ri:chat-4-line',
        iconClass: 'text-info'
      })
    }
    if (props.resumeKeyRequests > 0) {
      items.push({
        title: '下载密钥生成请求',
        status: `${props.resumeKeyRequests} 条请求`,
        icon: 'ri:key-2-line',
        iconClass: 'text-danger'
      })
    }
    return items
  })
</script>
