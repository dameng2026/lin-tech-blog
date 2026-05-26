<template>
  <div class="page-container p-3 lg:p-[1.75rem] bg-[#fefefe]">
    <div class="min-h-screen">
      <div class="flex flex-col lg:flex-row gap-4 lg:gap-8">
        <main class="lg:flex-1">
          <div class="mb-4 lg:mb-5">
            <h1 class="text-xl lg:text-[40px] leading-none font-extrabold text-slate-900 mb-2 lg:mb-3 tracking-[-0.04em]">留言</h1>
            <p class="text-xs lg:text-[14px] text-slate-500">欢迎在这里留言交流，分享想法或提出建议。我会认真阅读每一条留言并及时回复。</p>
          </div>

          <section class="rounded-[18px] bg-white border border-slate-100 shadow-[0_8px_30px_rgba(15,23,42,0.05)] p-3 lg:p-5 mb-4 lg:mb-5">
            <div class="flex items-center justify-between mb-3 lg:mb-4">
              <h2 class="text-xs lg:text-[15px] font-semibold text-slate-800">留下你的留言</h2>
            </div>
            <textarea v-model="form.message" class="w-full h-[70px] lg:h-[86px] resize-none rounded-[12px] border border-slate-200 bg-slate-50 px-3 lg:px-4 py-2.5 lg:py-3 text-xs lg:text-[13px] outline-none focus:border-blue-400 focus:bg-white" placeholder="写下你的想法、问题或建议..."></textarea>
            <div class="mt-3 lg:mt-4 flex flex-col lg:flex-row items-center gap-2 lg:gap-3">
              <div class="flex items-center gap-2 rounded-[12px] border border-slate-200 bg-white px-3 py-2 min-w-[120px] lg:min-w-[190px]">
                <div class="w-6 h-6 lg:w-7 lg:h-7 rounded-full bg-[radial-gradient(circle_at_30%_30%,#d6e4ff,#1f6bff)] flex items-center justify-center text-white text-xs lg:text-[13px] font-bold">L</div>
                <div class="text-xs lg:text-[13px] text-slate-700"><span class="font-medium">Lin</span> <span class="text-slate-400">（可选）</span></div>
              </div>
              <input v-model="form.email" class="w-full lg:flex-1 rounded-[12px] border border-slate-200 bg-white px-3 lg:px-4 py-2 lg:py-2.5 text-xs lg:text-[13px] outline-none focus:border-blue-400" placeholder="your.email@example.com （可选）" />
              <button @click="postMessage" class="w-full lg:ml-auto rounded-[12px] bg-gradient-to-r from-[#1f5cff] to-[#2f7cff] px-4 lg:px-5 py-2 lg:py-2.5 text-white text-xs lg:text-[13px] font-semibold shadow-[0_10px_18px_rgba(37,99,235,0.2)]">发布留言</button>
            </div>
          </section>

          <div class="flex flex-col lg:flex-row items-center justify-between gap-2 lg:gap-0 mb-3">
            <div class="text-xs lg:text-[14px] font-medium text-slate-700">全部留言 <span class="text-slate-400">({{ totalCount }})</span></div>
            <div class="flex items-center gap-2">
              <button @click="toggleSort('newest')" :class="['h-7 lg:h-9 px-3 lg:px-4 rounded-[10px] border border-slate-200 bg-white text-xs lg:text-[13px]', sortBy === 'newest' ? 'text-blue-600 font-semibold' : 'text-slate-600']">最新</button>
              <button @click="toggleSort('hottest')" :class="['h-7 lg:h-9 px-3 lg:px-4 rounded-[10px] border border-slate-200 bg-white text-xs lg:text-[13px]', sortBy === 'hottest' ? 'text-blue-600 font-semibold' : 'text-slate-600']">最热</button>
            </div>
          </div>

          <div v-if="loading" class="text-center py-8 text-slate-400 text-sm">加载中...</div>

          <section v-else class="space-y-3 lg:space-y-4">
            <article v-for="item in comments" :key="item.id" class="rounded-[16px] bg-white border border-slate-100 shadow-[0_8px_24px_rgba(15,23,42,0.05)] p-3 lg:p-4">
              <div class="flex items-start gap-2 lg:gap-3">
                <div class="w-7 h-7 lg:w-8 lg:h-8 rounded-full overflow-hidden flex-shrink-0 bg-slate-200">
                  <img :src="item.avatar" class="w-full h-full object-cover" />
                </div>
                <div class="min-w-0 flex-1">
                  <div class="flex items-center gap-2 mb-1">
                    <span class="text-xs lg:text-[14px] font-semibold text-slate-800">{{ item.name }}</span>
                    <span class="text-[11px] lg:text-[12px] text-slate-400">{{ item.time }}</span>
                  </div>
                  <p class="text-xs lg:text-[13px] leading-5 lg:leading-6 text-slate-600">{{ item.text }}</p>
                  <button @click="replyTo(item)" class="mt-2 text-[11px] lg:text-[12px] text-slate-500 hover:text-slate-700">回复</button>
                </div>
                <div @click="handleLike(item)" class="flex items-center gap-1 text-xs lg:text-[13px] pl-1 lg:pl-2 pt-0.5 lg:pt-1 cursor-pointer" :class="item.liked ? 'text-blue-500' : 'text-slate-400'">
                  <span>👍</span><span class="text-slate-500">{{ item.likes }}</span>
                </div>
              </div>

              <div v-if="item.reply" class="mt-2 lg:mt-3 ml-9 lg:ml-11 rounded-[14px] bg-[#f5f8ff] border border-blue-50 p-3 lg:p-4">
                <div class="flex items-start gap-2 lg:gap-3">
                  <div class="w-7 h-7 lg:w-8 lg:h-8 rounded-full overflow-hidden flex-shrink-0 bg-slate-200">
                    <img :src="item.reply.avatar" class="w-full h-full object-cover" />
                  </div>
                  <div class="min-w-0 flex-1">
                    <div class="flex items-center gap-2 mb-1">
                      <span class="text-xs lg:text-[14px] font-semibold text-blue-700">{{ item.reply.name }}</span>
                      <span class="text-[11px] lg:text-[12px] text-slate-400">{{ item.reply.time }}</span>
                    </div>
                    <p class="text-xs lg:text-[13px] leading-5 lg:leading-6 text-slate-600">{{ item.reply.text }}</p>
                    <button @click="replyTo(item)" class="mt-2 text-[11px] lg:text-[12px] text-slate-500 hover:text-slate-700">回复</button>
                  </div>
                  <div @click="handleLike(item.reply)" class="flex items-center gap-1 text-slate-400 text-xs lg:text-[13px] pl-1 lg:pl-2 pt-0.5 lg:pt-1 cursor-pointer">
                    <span>👍</span><span class="text-slate-500">{{ item.reply.likes }}</span>
                  </div>
                </div>
              </div>
            </article>
          </section>

          <div class="flex items-center justify-center gap-2 mt-4 lg:mt-6" v-if="totalPages > 1">
            <button @click="changePage(currentPage - 1)" class="w-6 h-6 lg:w-8 lg:h-8 rounded-[8px] border border-slate-200 bg-white text-slate-600 text-xs lg:text-[13px]" :disabled="currentPage <= 1">‹</button>
            <button v-for="p in totalPages" :key="p" @click="changePage(p)" :class="['w-6 h-6 lg:w-8 lg:h-8 rounded-[8px] text-xs lg:text-[13px] font-medium', p === currentPage ? 'bg-[#1f5cff] text-white' : 'border border-slate-200 bg-white text-slate-600']">{{ p }}</button>
            <button @click="changePage(currentPage + 1)" class="w-6 h-6 lg:w-8 lg:h-8 rounded-[8px] border border-slate-200 bg-white text-slate-600 text-xs lg:text-[13px]" :disabled="currentPage >= totalPages">›</button>
          </div>
        </main>

        <aside class="hidden lg:block lg:w-1/5 space-y-4">
          <section class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6 flex flex-col">
            <div class="flex flex-col items-center mb-6">
              <div class="w-[5rem] h-[5rem] rounded-full overflow-hidden flex-shrink-0 mb-3">
                <img :src="siteSettings.avatar || '/images/avatar.png'" alt="avatar" class="w-full h-full object-cover" />
              </div>
              <h3 class="font-bold text-xl text-gray-900 mb-1">{{ siteSettings.author_name || 'Lin' }}</h3>
              <p class="text-sm text-gray-600">{{ siteSettings.description || '全栈开发 & AI 应用探索。' }}</p>
            </div>
            <div class="w-full space-y-3 mb-6">
              <div class="flex items-center text-sm text-gray-600">
                <img src="/icons/position-black.svg" alt="地址" class="w-4 h-4 mr-2" />
                {{ siteSettings.location || '中国 · 深圳' }}
              </div>
              <div class="flex items-center text-sm text-gray-600">
                <img src="/icons/email-black.svg" alt="邮箱" class="w-4 h-4 mr-2" />
                {{ siteSettings.email || 'lin@example.com' }}
              </div>
              <div class="flex items-center text-sm text-gray-600">
                <img src="/icons/github-black.svg" alt="GitHub" class="w-4 h-4 mr-2" />
                {{ siteSettings.github_url || 'github.com/linxxxx' }}
              </div>
              <div class="flex items-center text-sm text-gray-600">
                <img src="/icons/project-black.svg" alt="开发经验" class="w-4 h-4 mr-2" />
                {{ siteSettings.experience || '5 年开发经验' }}
              </div>
            </div>
            <button @click="openModal" class="w-full py-2.5 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-all flex items-center justify-center mt-auto">
              <img src="/icons/download.svg" alt="下载" class="w-4 h-4 mr-2" />
              下载简历(PDF)
            </button>
          </section>

          <section class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] px-[2rem] py-6">
            <h3 class="font-semibold text-gray-900 mb-4">站点数据</h3>
            <div class="flex justify-between">
              <div v-for="s in stats" :key="s.label" class="flex flex-col items-center">
                <div class="w-12 h-12 rounded-full bg-[#f6f7fb] flex items-center justify-center mb-3">
                  <img :src="s.icon" alt="icon" class="w-6 h-6 text-blue-600" />
                </div>
                <div class="text-[0.8rem] text-gray-500 py-1">{{ s.label }}</div>
                <div class="text-2xl font-bold text-gray-900">{{ s.value }}</div>
              </div>
            </div>
          </section>

          <section class="rounded-[18px] bg-white border border-slate-100 shadow-[0_8px_30px_rgba(15,23,42,0.05)] p-5">
            <h3 class="text-[15px] font-semibold text-slate-800 mb-4">最新评论</h3>
            <div class="space-y-4">
              <div v-for="c in recentComments" :key="c.name" class="flex items-center gap-3">
                <img :src="c.avatar" class="w-8 h-8 rounded-full object-cover" />
                <div class="min-w-0 flex-1">
                  <div class="flex items-center justify-between gap-3">
                    <div class="text-[13px] font-medium text-slate-800 truncate">{{ c.name }}</div>
                    <div class="text-[12px] text-slate-400 shrink-0">{{ c.time }}</div>
                  </div>
                  <div class="text-[12px] text-slate-500 truncate">{{ c.text }}</div>
                </div>
              </div>
            </div>
          </section>

          <section class="rounded-[18px] bg-white border border-slate-100 shadow-[0_8px_30px_rgba(15,23,42,0.05)] p-5">
            <h3 class="text-[15px] font-semibold text-slate-800 mb-4">留言须知</h3>
            <ul class="space-y-2 text-[12px] leading-5 text-slate-500 list-disc pl-5">
              <li>请保持友善和理性，尊重他人观点</li>
              <li>欢迎提出问题、建议或分享想法</li>
              <li>垃圾广告将被删除，请勿重复投稿</li>
              <li>博主会尽量在 24 小时内回复留言</li>
            </ul>
          </section>
        </aside>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { usePdfModal } from '../composables/usePdfModal'
import { fetchGuestbookMessages, createGuestbookMessage, likeMessage } from '../api/messages'
import { fetchSiteSettings } from '../api/site'

const { openModal } = usePdfModal()

const form = reactive({
  message: '',
  email: ''
})

const comments = ref([])
const loading = ref(false)
const totalCount = ref(0)
const currentPage = ref(1)
const totalPages = ref(1)
const sortBy = ref('newest')
const submitting = ref(false)
const replyingTo = ref(null)

const siteSettings = ref({})

async function loadSiteSettings() {
  const data = await fetchSiteSettings()
  if (data) siteSettings.value = data
}

async function loadMessages(page = 1) {
  loading.value = true
  try {
    const res = await fetchGuestbookMessages({ page, size: 10, sort: sortBy.value })
    const data = res?.data || res
    if (data && data.comments) {
      comments.value = data.comments.map(c => ({
        id: c.id,
        name: c.guest_name || c.username || '匿名',
        time: formatTime(c.created_at),
        avatar: c.avatar || `https://api.dicebear.com/7.x/initials/svg?seed=${encodeURIComponent(c.guest_name || 'A')}&backgroundColor=1f6bff,d6e4ff`,
        text: c.content,
        likes: c.like_count || 0,
        liked: false,
        reply: c.replies && c.replies.length > 0 ? {
          id: c.replies[0].id,
          name: c.replies[0].guest_name || '博主',
          time: formatTime(c.replies[0].created_at),
          avatar: c.replies[0].avatar || '/images/avatar.png',
          text: c.replies[0].content,
          likes: c.replies[0].like_count || 0
        } : null,
        replies: c.replies || []
      }))
      totalCount.value = data.total || 0
      totalPages.value = Math.ceil(totalCount.value / 10)
      recentComments.value = comments.value.slice(0, 5).map(c => ({
        name: c.name,
        time: c.time,
        text: c.text,
        avatar: c.avatar
      }))
    }
  } catch (e) {
    console.error('加载留言失败', e)
  } finally {
    loading.value = false
  }
}

function formatTime(dateStr) {
  if (!dateStr) return ''
  const date = new Date(dateStr)
  const now = new Date()
  const diff = now - date
  const mins = Math.floor(diff / 60000)
  const hours = Math.floor(diff / 3600000)
  const days = Math.floor(diff / 86400000)
  if (mins < 1) return '刚刚'
  if (mins < 60) return `${mins} 分钟前`
  if (hours < 24) return `${hours} 小时前`
  if (days < 30) return `${days} 天前`
  return date.toLocaleDateString('zh-CN')
}

function replyTo(item) {
  replyingTo.value = item
  form.message = `@${item.name} `
}

function cancelReply() {
  replyingTo.value = null
  form.message = ''
}

async function postMessage() {
  if (!form.message.trim()) return
  submitting.value = true
  try {
    const payload = {
      content: form.message.trim(),
      guest_name: 'Lin',
      guest_email: form.email || undefined
    }
    if (replyingTo.value) {
      payload.parent_id = replyingTo.value.id
      payload.reply_to_id = replyingTo.value.id
      payload.reply_to_name = replyingTo.value.name
    }
    await createGuestbookMessage(payload)
    form.message = ''
    form.email = ''
    replyingTo.value = null
    loadMessages(currentPage.value)
  } catch (e) {
    console.error('留言失败', e)
    alert('留言提交失败，请稍后重试')
  } finally {
    submitting.value = false
  }
}

async function handleLike(item) {
  try {
    const res = await likeMessage(item.id)
    if (res && res.liked !== undefined) {
      item.likes = res.like_count
      item.liked = res.liked
    }
  } catch (e) {
    console.error('点赞失败', e)
  }
}

function changePage(page) {
  if (page < 1 || page > totalPages.value) return
  currentPage.value = page
  loadMessages(page)
}

function toggleSort(sort) {
  sortBy.value = sort
  currentPage.value = 1
  loadMessages(1)
}

const stats = [
  { icon: '/icons/article-blue.svg', label: '文章', value: '32' },
  { icon: '/icons/project-grey.svg', label: '项目', value: '12' },
  { icon: '/icons/eye.svg', label: '访问量', value: '18.6k' },
  { icon: '/icons/calendar.svg', label: '运行天数', value: '236' }
]

const recentComments = ref([])

onMounted(() => {
  loadSiteSettings()
  loadMessages(1)
})
</script>

<style scoped>
.page-container {
  background: #ffffff;
  padding: 1.75rem;
}

@media (max-width: 768px) {
  .page-container {
    padding: 0.75rem 0.75rem 1rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row {
    gap: 0.75rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 {
    min-width: 0;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mb-4.lg\:mb-5 {
    margin-bottom: 0.75rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mb-4.lg\:mb-5 h1 {
    font-size: 1.75rem;
    line-height: 1.1;
    margin-bottom: 0.5rem;
    letter-spacing: -0.04em;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mb-4.lg\:mb-5 p {
    font-size: 0.8rem;
    line-height: 1.6;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mb-4.lg\:mb-5 p br {
    display: none;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .rounded-\[18px\] {
    padding: 0.9rem;
    border-radius: 1rem;
    margin-bottom: 0.75rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .rounded-\[18px\] .flex.items-center.justify-between {
    margin-bottom: 0.6rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .rounded-\[18px\] h2 {
    font-size: 0.95rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .rounded-\[18px\] textarea {
    height: 90px;
    border-radius: 0.9rem;
    font-size: 0.8rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .rounded-\[18px\] .mt-3.lg\:mt-4 {
    margin-top: 0.65rem;
    gap: 0.5rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .rounded-\[18px\] .mt-3.lg\:mt-4 > div,
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .rounded-\[18px\] .mt-3.lg\:mt-4 input,
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .rounded-\[18px\] .mt-3.lg\:mt-4 button {
    width: 100%;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .flex.flex-col.lg\:flex-row.items-center.justify-between {
    align-items: flex-start;
    gap: 0.5rem;
    margin-bottom: 0.65rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .flex.flex-col.lg\:flex-row.items-center.justify-between > div:first-child {
    font-size: 0.9rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .flex.flex-col.lg\:flex-row.items-center.justify-between > .flex.items-center.gap-2 {
    width: 100%;
    justify-content: flex-end;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .space-y-3.lg\:space-y-4 {
    gap: 0.65rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .space-y-3.lg\:space-y-4 > article {
    padding: 0.85rem;
    border-radius: 1rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .space-y-3.lg\:space-y-4 > article .w-7.h-7 {
    width: 2rem;
    height: 2rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .space-y-3.lg\:space-y-4 > article p {
    font-size: 0.8rem;
    line-height: 1.6;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .space-y-3.lg\:space-y-4 > article .mt-2.lg\:mt-3.ml-9.lg\:ml-11 {
    margin-left: 2.25rem;
    padding: 0.75rem;
    border-radius: 0.9rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .space-y-3.lg\:space-y-4 > article .mt-2.lg\:mt-3.ml-9.lg\:ml-11 .w-7.h-7 {
    width: 2rem;
    height: 2rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .flex.items-center.justify-center.gap-2.mt-4.lg\:mt-6 {
    margin-top: 0.85rem;
    gap: 0.35rem;
    flex-wrap: wrap;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .flex.items-center.justify-center.gap-2.mt-4.lg\:mt-6 button {
    width: 1.7rem;
    height: 1.7rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .flex.items-center.justify-center.gap-2.mt-4.lg\:mt-6 span {
    font-size: 0.8rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .flex.items-center.justify-center.gap-2.mt-4.lg\:mt-6 button:last-child {
    width: auto;
    padding: 0 0.55rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:w-1\/5 {
    display: none;
  }
}
</style>
