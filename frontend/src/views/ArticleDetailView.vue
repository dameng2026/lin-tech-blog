<template>
  <div class="page-container p-3 lg:p-[1.75rem] bg-[#fefefe]">
    <div class="min-h-screen">
      <div v-if="loading" class="flex justify-center items-center py-20">
        <div class="animate-spin rounded-full h-10 w-10 border-b-2 border-blue-600"></div>
      </div>

      <div v-else-if="error" class="text-center py-20">
        <p class="text-gray-500 mb-4">{{ error }}</p>
        <button @click="loadArticle" class="px-4 py-2 bg-blue-50 text-blue-600 rounded-lg text-sm hover:bg-blue-100">重新加载</button>
      </div>

      <template v-else-if="article">
        <div class="flex flex-col lg:flex-row gap-4 lg:gap-8">
          <main class="lg:flex-1">
            <div class="text-[11px] lg:text-[12px] text-[#94a3b8] mb-3 lg:mb-[16px]">
              首页 <span class="mx-2 lg:mx-[8px]">|</span> 文章 <span class="mx-2 lg:mx-[8px]">|</span> {{ article.title }}
            </div>

            <div class="inline-flex items-center px-2 lg:px-[10px] py-1 lg:py-[4px] rounded-full bg-[#eff6ff] text-[#2563eb] text-[11px] lg:text-[12px] font-semibold mb-2 lg:mb-[12px]">{{ article.category || '技术文章' }}</div>
            <h1 class="text-lg lg:text-[26px] leading-[1.2] font-extrabold tracking-[-0.02em] text-[#0f172a]">{{ article.title }}</h1>

            <div v-if="article.source_type === 'repost' && article.repost_url" class="mt-2 lg:mt-[12px] inline-flex items-center px-3 lg:px-[16px] py-2 lg:py-[10px] rounded-lg bg-amber-50 border border-amber-200 text-amber-700 text-xs lg:text-[13px]">
              <svg class="w-4 h-4 mr-2 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" />
              </svg>
              <span>转载自：</span>
              <a :href="article.repost_url" target="_blank" rel="noopener noreferrer" class="ml-1 text-blue-600 hover:underline break-all">
                {{ article.repost_url }}
              </a>
            </div>

            <div class="flex items-center justify-between gap-3 lg:gap-[16px] mt-2 lg:mt-[16px] lg:flex-row flex-col lg:items-center items-start">
              <div class="flex items-center gap-2 lg:gap-[12px]">
                <img class="w-8 h-8 lg:w-[40px] lg:h-[40px] rounded-full object-cover" :src="article.author?.avatar || 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=120&q=80'" alt="avatar" />
                <div>
                  <div class="text-xs lg:text-[14px] font-semibold text-[#1e293b]">{{ article.author?.name || 'Lin' }}</div>
                  <div class="flex gap-2 lg:gap-[14px] mt-1 lg:mt-[4px] text-[10px] lg:text-[12px] text-[#64748b] flex-wrap">
                    <span><img src="/icons/time.svg" alt="时间" class="w-2.5 h-2.5 lg:w-3 lg:h-3 mr-1 inline-block" />{{ formatDate(article.created_at) }}</span>
                    <span><img src="/icons/folder.svg" alt="分类" class="w-2.5 h-2.5 lg:w-3 lg:h-3 mr-1 inline-block" />{{ article.category || '未分类' }}</span>
                    <span><img src="/icons/eye.svg" alt="阅读" class="w-2.5 h-2.5 lg:w-3 lg:h-3 mr-1 inline-block" />阅读 {{ formatViews(article.view_count) }}</span>
                    <span><img src="/icons/reading.svg" alt="阅读时长" class="w-2.5 h-2.5 lg:w-3 lg:h-3 mr-1 inline-block" />{{ article.read_time || 0 }} 分钟</span>
                  </div>
                </div>
              </div>
              <div class="flex gap-2 lg:gap-[12px] flex-wrap lg:w-auto w-full">
                <button @click="handleCollectArticle" :disabled="collectingArticle" class="px-3 lg:px-[16px] py-1.5 lg:py-[8px] border border-[#e2e8f0] bg-white rounded-[8px] lg:rounded-[10px] text-[#475569] text-[10px] lg:text-[12px] shadow-[0_1px_2px_rgba(15,23,42,.04)] flex items-center"><img src="/icons/flag-grey.svg" alt="收藏" class="w-3 h-3 lg:w-3.5 lg:h-3.5 mr-1 lg:mr-1.5" />收藏 <span>{{ article.collect_count || 0 }}</span></button>
                <button @click="handleLikeArticle" :disabled="likingArticle" class="px-3 lg:px-[16px] py-1.5 lg:py-[8px] border border-[#e2e8f0] bg-white rounded-[8px] lg:rounded-[10px] text-[#475569] text-[10px] lg:text-[12px] shadow-[0_1px_2px_rgba(15,23,42,.04)] flex items-center"><img src="/icons/like-grey.svg" alt="点赞" class="w-3 h-3 lg:w-3.5 lg:h-3.5 mr-1 lg:mr-1.5" /><span>{{ article.like_count || 0 }}</span></button>
                <button @click="handleShareArticle" class="px-3 lg:px-[16px] py-1.5 lg:py-[8px] border border-[#e2e8f0] bg-white rounded-[8px] lg:rounded-[10px] text-[#475569] text-[10px] lg:text-[12px] shadow-[0_1px_2px_rgba(15,23,42,.04)] flex items-center"><img src="/icons/share-grey.svg" alt="分享" class="w-3 h-3 lg:w-3.5 lg:h-3.5 mr-1 lg:mr-1.5" />分享</button>
              </div>
            </div>

            <div v-if="article.cover" class="bg-white border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] rounded-[1.1rem] overflow-hidden mt-3 lg:mt-[20px]">
              <img :src="article.cover" :alt="article.title" class="w-full h-auto object-cover" />
            </div>

            <div class="mt-3 lg:mt-[26px] article-content" v-html="article.content"></div>

            <div v-if="article.tags && article.tags.length > 0" class="mt-4 lg:mt-[28px] flex flex-wrap gap-2">
              <span v-for="tag in article.tags" :key="tag"
                class="px-[10px] py-[4px] rounded-full bg-[#f1f5f9] text-[#64748b] text-[12px]">{{ tag }}</span>
            </div>

            <section class="mt-3 lg:mt-[28px]">
              <div class="flex items-center justify-between mb-2 lg:mb-[12px]">
                <div class="text-sm lg:text-[16px] font-bold text-[#0f172a]">评论 ({{ commentTotal }})</div>
                <div class="flex gap-2 lg:gap-[12px]">
                  <button @click="switchSort('newest')" :class="['text-[10px] lg:text-[12px] px-2 py-1 rounded transition-colors', commentSort === 'newest' ? 'text-blue-600 bg-blue-50 font-semibold' : 'text-[#475569] hover:text-blue-600']">最新</button>
                  <button @click="switchSort('hottest')" :class="['text-[10px] lg:text-[12px] px-2 py-1 rounded transition-colors', commentSort === 'hottest' ? 'text-blue-600 bg-blue-50 font-semibold' : 'text-[#475569] hover:text-blue-600']">最热</button>
                </div>
              </div>

              <div class="bg-white border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] rounded-[1.1rem] p-2 lg:p-[12px] flex gap-2 lg:gap-[12px] items-start">
                <div class="w-8 h-8 lg:w-[40px] lg:h-[40px] rounded-full flex-shrink-0 bg-blue-100 flex items-center justify-center text-blue-600 text-xs lg:text-sm font-semibold">{{ guestName.charAt(0) }}</div>
                <div class="flex-1">
                  <div class="text-[10px] lg:text-[11px] text-gray-400 mb-1">评论者：{{ guestName }}</div>
                  <textarea v-model="draft" placeholder="写下你的评论..." class="w-full h-[50px] lg:h-[64px] resize-none border border-[#e2e8f0] rounded-[8px] lg:rounded-[10px] px-2 lg:px-[12px] py-2 lg:py-[10px] text-[11px] lg:text-[13px] outline-none bg-white text-[#0f172a]"></textarea>
                  <div class="flex justify-between items-end mt-2 lg:mt-[10px]">
                    <div class="text-[10px] lg:text-[12px] text-gray-400">{{ draft.length }}/2000</div>
                    <div class="text-right">
                      <button @click="submitComment" :disabled="submitting" class="bg-[#2563eb] text-white border-none rounded-[8px] lg:rounded-[9px] px-3 lg:px-[14px] py-1.5 lg:py-[8px] text-[10px] lg:text-[12px] font-semibold disabled:opacity-50 disabled:cursor-not-allowed">
                        {{ submitting ? '提交中...' : '发布评论' }}
                      </button>
                    </div>
                  </div>
                  <div v-if="commentError" class="text-[10px] lg:text-[11px] text-red-500 mt-1">{{ commentError }}</div>
                </div>
              </div>

              <div v-if="commentLoading" class="text-center py-8 text-gray-400 text-sm">加载评论中...</div>

              <template v-else>
                <div v-for="c in comments" :key="c.id" class="flex gap-2 lg:gap-[12px] py-2 lg:py-[12px] border-b border-[#eef2f7]">
                  <div class="w-8 h-8 lg:w-[40px] lg:h-[40px] rounded-full flex-shrink-0 flex items-center justify-center text-xs lg:text-sm font-semibold" :class="getAvatarColor(c.username)">{{ c.username.charAt(0) }}</div>
                  <div class="flex-1 min-w-0">
                    <div class="flex justify-between gap-2 lg:gap-[10px] items-center">
                      <div class="text-[11px] lg:text-[13px] font-semibold text-[#1e293b] truncate">{{ c.username }}</div>
                      <div class="text-[10px] lg:text-[12px] text-[#94a3b8] flex-shrink-0">{{ formatDate(c.created_at) }}</div>
                    </div>
                    <div class="mt-1 lg:mt-[8px] text-[11px] lg:text-[13px] leading-[1.6] lg:leading-[1.75] text-[#334155] break-words">{{ c.content }}</div>
                    <div class="flex gap-3 lg:gap-[12px] items-center mt-1 lg:mt-[8px] text-[10px] lg:text-[12px] text-[#64748b]">
                      <span class="cursor-pointer hover:text-blue-600 transition-colors flex items-center gap-1" @click="toggleReplyInput(c.id)">
                        <span>回复</span>
                        <span>({{ c.replies?.length || 0 }})</span>
                      </span>
                      <span class="cursor-pointer hover:text-red-500 transition-colors flex items-center gap-1" @click="toggleLike(c.id)">
                        <span>👍</span>
                        <span>{{ c.like_count || 0 }}</span>
                      </span>
                    </div>

                    <div v-if="replyInputId === c.id" class="mt-2 lg:mt-[10px]">
                      <div class="flex gap-2 items-start">
                        <div class="flex-1">
                          <textarea v-model="replyDraft" placeholder="写下你的回复..." class="w-full h-[40px] resize-none border border-[#e2e8f0] rounded-[8px] px-2 py-1.5 text-[11px] lg:text-[13px] outline-none bg-white text-[#0f172a]"></textarea>
                          <div class="flex justify-end gap-2 mt-1">
                            <button @click="replyInputId = null" class="text-[10px] lg:text-[11px] text-gray-400 px-2 py-1">取消</button>
                            <button @click="submitReply(c.id)" :disabled="replySubmitting" class="bg-[#2563eb] text-white border-none rounded-[6px] px-2 lg:px-[10px] py-1 text-[10px] lg:text-[11px] font-semibold disabled:opacity-50">
                              {{ replySubmitting ? '提交中...' : '回复' }}
                            </button>
                          </div>
                        </div>
                      </div>
                    </div>

                    <div v-for="r in c.replies" :key="r.id" class="mt-2 lg:mt-[10px]">
                      <div class="flex items-start gap-2">
                        <div class="w-6 h-6 lg:w-[28px] lg:h-[28px] rounded-full flex-shrink-0 flex items-center justify-center text-[9px] lg:text-[11px] font-semibold" :class="getAvatarColor(r.username)">{{ r.username.charAt(0) }}</div>
                        <div class="flex-1 min-w-0">
                          <div class="flex flex-wrap gap-1 lg:gap-1">
                            <span class="text-[10px] lg:text-[12px] font-semibold text-[#1e293b]">{{ r.username }}</span>
                            <template v-if="r.reply_to_name">
                              <span class="text-[10px] lg:text-[12px] text-[#64748b]">回复</span>
                              <span class="text-[10px] lg:text-[12px] font-semibold text-[#1e293b]">{{ r.reply_to_name }}</span>
                            </template>
                            <span class="text-[10px] lg:text-[12px] text-[#64748b]">：</span>
                            <span class="text-[10px] lg:text-[12px] text-[#334155] break-words">{{ r.content }}</span>
                          </div>
                          <div class="flex justify-between items-center mt-1 lg:mt-[6px]">
                            <div class="text-[9px] lg:text-[11px] text-[#94a3b8]">{{ formatDate(r.created_at) }}</div>
                            <div class="flex gap-2 lg:gap-[10px] items-center text-[9px] lg:text-[11px] text-[#64748b]">
                              <span class="cursor-pointer hover:text-blue-600 transition-colors" @click="toggleReplyInput(r.id, c.id, r.username)">回复</span>
                              <span class="cursor-pointer hover:text-red-500 transition-colors flex items-center gap-1" @click="toggleLike(r.id)">
                                <span>👍</span>
                                <span>{{ r.like_count || 0 }}</span>
                              </span>
                            </div>
                          </div>
                        </div>
                      </div>

                      <div v-if="replyInputId === r.id" class="mt-2 lg:mt-[8px] ml-[26px] lg:ml-[36px]">
                        <div class="flex gap-2 items-start">
                          <div class="flex-1">
                            <textarea v-model="replyDraft" placeholder="写下你的回复..." class="w-full h-[40px] resize-none border border-[#e2e8f0] rounded-[8px] px-2 py-1.5 text-[11px] lg:text-[13px] outline-none bg-white text-[#0f172a]"></textarea>
                            <div class="flex justify-end gap-2 mt-1">
                              <button @click="replyInputId = null" class="text-[10px] lg:text-[11px] text-gray-400 px-2 py-1">取消</button>
                              <button @click="submitReply(c.id, r.id, r.username)" :disabled="replySubmitting" class="bg-[#2563eb] text-white border-none rounded-[6px] px-2 lg:px-[10px] py-1 text-[10px] lg:text-[11px] font-semibold disabled:opacity-50">
                                {{ replySubmitting ? '提交中...' : '回复' }}
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <div v-if="comments.length === 0 && !commentLoading" class="text-center py-8 text-gray-400 text-sm">暂无评论，快来发表第一条评论吧</div>

                <div v-if="hasMoreComments" @click="loadMoreComments" class="bg-white border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] rounded-[1.1rem] mt-2 lg:mt-[12px] text-center p-2 lg:p-[12px] text-[11px] lg:text-[13px] text-[#2563eb] font-semibold cursor-pointer hover:bg-blue-50 transition-colors">加载更多评论...</div>
              </template>
            </section>
          </main>

          <aside class="hidden lg:block lg:w-1/5">
            <!-- 侧边栏粘性区块：个人信息 + 目录 + 文章信息 + 相关文章 -->
            <div class="right-sticky-wrapper">
              <!-- 个人信息 -->
              <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6 mb-5">
                <div class="flex flex-col items-center mb-4">
                  <div class="w-[5rem] h-[5rem] rounded-full overflow-hidden flex-shrink-0 mb-3">
                    <img :src="article.author?.avatar || '/images/avatar.png'" alt="author" class="w-full h-full object-cover" />
                  </div>
                  <h3 class="font-bold text-xl text-gray-900 mb-1">{{ article.author?.name || 'Lin' }}</h3>
                  <p class="text-sm text-gray-600">{{ article.author?.bio || '全栈开发 & AI 应用探索。' }}</p>
                </div>
                <div class="w-full space-y-3 mb-4">
                  <div class="flex items-center text-sm text-gray-600">
                    <img src="/icons/position-grey.svg" alt="地址" class="w-4 h-4 mr-2" />
                    {{ siteSettings?.location || '中国 · 深圳' }}
                  </div>
                  <div class="flex items-center text-sm text-gray-600">
                    <img src="/icons/email-black.svg" alt="邮箱" class="w-4 h-4 mr-2" />
                    {{ siteSettings?.email || 'lin@example.com' }}
                  </div>
                  <div class="flex items-center text-sm text-gray-600">
                    <img src="/icons/github-black.svg" alt="GitHub" class="w-4 h-4 mr-2" />
                    {{ (siteSettings?.github_url || 'github.com/linxxxx').replace(/^https?:\/\//, '') }}
                  </div>
                  <div class="flex items-center text-sm text-gray-600">
                    <img src="/icons/project-black.svg" alt="开发经验" class="w-4 h-4 mr-2" />
                    {{ siteSettings?.experience || '5 年开发经验' }}
                  </div>
                </div>
                <button @click="openModal" class="w-full py-2.5 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-all flex items-center justify-center">
                  <img src="/icons/download.svg" alt="下载" class="w-4 h-4 mr-2" />
                  下载简历(PDF)
                </button>
              </div>

              <!-- 章节目录 -->
              <div v-if="catalogItems.length > 0" class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6 mb-5">
                <h3 class="text-base font-semibold text-gray-900 mb-4">文章目录</h3>
                <ol class="pl-0 m-0 list-none">
                  <li v-for="item in catalogItems" :key="item.anchor"
                    @click="scrollToSection(item.anchor)"
                    :style="{ paddingLeft: (item.depth * 14) + 'px' }"
                    :class="[
                      'cursor-pointer py-1 rounded text-xs leading-relaxed transition-colors',
                      item.depth === 0 ? 'text-sm text-gray-600 hover:bg-blue-50' : 'text-gray-500 hover:bg-blue-50',
                      activeSection === item.anchor ? 'text-blue-600 font-semibold' : ''
                    ]">{{ item.title }}</li>
                </ol>
              </div>

              <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6 mb-5">
                <h3 class="text-base font-semibold text-gray-900 mb-4">文章信息</h3>
                <div class="flex justify-between gap-[10px] text-sm text-gray-600 mb-3"><span>发布时间</span><span>{{ formatDate(article.created_at) }}</span></div>
                <div class="flex justify-between gap-[10px] text-sm text-gray-600 mb-3"><span>最后更新</span><span>{{ formatDate(article.updated_at) }}</span></div>
                <div class="flex justify-between gap-[10px] text-sm text-gray-600 mb-3"><span>阅读时长</span><span>{{ article.read_time || 0 }} 分钟</span></div>
                <div class="flex justify-between gap-[10px] text-sm text-gray-600"><span>字数</span><span>{{ article.word_count || '-' }}</span></div>
              </div>

              <!-- 相关文章 -->
              <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6">
                <h3 class="text-base font-semibold text-gray-900 mb-4">相关文章</h3>
                <div v-if="relatedLoading" class="space-y-3">
                  <div v-for="n in 3" :key="n" class="flex gap-[12px] items-center animate-pulse">
                    <div class="w-[64px] h-[40px] rounded-[6px] bg-gray-200"></div>
                    <div class="flex-1 space-y-2">
                      <div class="h-3 bg-gray-200 rounded w-full"></div>
                      <div class="h-2 bg-gray-200 rounded w-2/3"></div>
                    </div>
                  </div>
                </div>
                <div v-else-if="relatedError" class="text-xs text-gray-400 text-center py-4">{{ relatedError }}</div>
                <template v-else>
                  <div v-for="r in relatedArticles" :key="r.id" class="flex gap-[12px] items-center mb-3 cursor-pointer hover:text-blue-600 transition-colors" @click="goToArticle(r.id)">
                    <img :src="r.cover || '/images/default-cover.svg'" alt="rel" class="w-[64px] h-[40px] rounded-[6px] object-cover" />
                    <div>
                      <div class="text-sm font-medium text-gray-700 whitespace-nowrap overflow-hidden text-ellipsis max-w-[180px]">{{ r.title }}</div>
                      <div class="text-xs text-gray-400 mt-1">{{ formatDate(r.created_at) }}</div>
                    </div>
                  </div>
                </template>
                <div class="text-blue-600 text-sm font-semibold mt-2 cursor-pointer hover:text-blue-700" @click="goToArticleList">查看更多 →</div>
              </div>
            </div>
          </aside>
        </div>
      </template>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch, onBeforeUnmount, nextTick } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { fetchArticle, fetchRelatedArticles, likeArticle, collectArticle } from '../api/articles'
import { fetchArticleComments, createArticleComment } from '../api/comments'
import { fetchSiteSettings } from '../api/site'
import { usePdfModal } from '../composables/usePdfModal'
import { generateGuestName } from '../utils/guestName'

const { openModal } = usePdfModal()
const route = useRoute()
const router = useRouter()

const article = ref(null)
const loading = ref(false)
const error = ref(null)
const draft = ref('')
const activeSection = ref('')
const siteSettings = ref(null)

const relatedArticles = ref([])
const relatedLoading = ref(false)
const relatedError = ref(null)

const comments = ref([])
const commentTotal = ref(0)
const commentPage = ref(1)
const commentSort = ref('newest')
const commentLoading = ref(false)
const commentError = ref('')
const submitting = ref(false)
const hasMoreComments = ref(false)
const replyInputId = ref(null)
const replyDraft = ref('')
const replySubmitting = ref(false)

const guestName = ref('')

const avatarColors = [
  'bg-blue-100 text-blue-600',
  'bg-green-100 text-green-600',
  'bg-purple-100 text-purple-600',
  'bg-pink-100 text-pink-600',
  'bg-yellow-100 text-yellow-600',
  'bg-red-100 text-red-600',
  'bg-indigo-100 text-indigo-600',
  'bg-teal-100 text-teal-600',
]

function getAvatarColor(name) {
  let hash = 0
  for (let i = 0; i < (name || '').length; i++) {
    hash = name.charCodeAt(i) + ((hash << 5) - hash)
  }
  return avatarColors[Math.abs(hash) % avatarColors.length]
}

let observer = null

function buildCatalogTree(catalog) {
  if (!catalog || !catalog.length) return []
  const root = []
  const stack = []
  for (const item of catalog) {
    const node = { ...item, children: [] }
    while (stack.length > 0 && stack[stack.length - 1].level >= item.level) {
      stack.pop()
    }
    if (stack.length === 0) {
      root.push(node)
    } else {
      stack[stack.length - 1].children.push(node)
    }
    stack.push(node)
  }
  function flatten(nodes, depth = 0) {
    const result = []
    for (const node of nodes) {
      result.push({ anchor: node.anchor, title: node.title, level: node.level, depth })
      result.push(...flatten(node.children, depth + 1))
    }
    return result
  }
  return flatten(root)
}

const catalogItems = computed(() => {
  return buildCatalogTree(article.value?.catalog)
})

function formatDate(dateStr) {
  if (!dateStr) return ''
  const date = new Date(dateStr)
  const y = date.getFullYear()
  const m = String(date.getMonth() + 1).padStart(2, '0')
  const d = String(date.getDate()).padStart(2, '0')
  return `${y}-${m}-${d}`
}

function formatViews(count) {
  if (!count && count !== 0) return '0'
  if (count >= 1000) return (count / 1000).toFixed(count % 1000 === 0 ? 0 : 1).replace('.0', '') + 'k'
  return String(count)
}

function scrollToSection(anchor) {
  const element = document.getElementById(anchor)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }
}

function goToArticle(id) {
  router.push(`/article/${id}`)
}

function goToArticleList() {
  router.push('/articles')
}

function setupSectionObserver() {
  if (observer) {
    observer.disconnect()
  }
  nextTick(() => {
    const sections = document.querySelectorAll('[id^="section-"]')
    if (sections.length === 0) return

    observer = new IntersectionObserver((entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          activeSection.value = entry.target.id
        }
      }
    }, { rootMargin: '-80px 0px -60% 0px', threshold: 0 })

    sections.forEach((section) => observer.observe(section))
  })
}

async function loadRelatedArticles() {
  const articleId = route.params.id
  if (!articleId) return

  const cacheKey = `related_articles_${articleId}`
  const cached = sessionStorage.getItem(cacheKey)
  if (cached) {
    try {
      relatedArticles.value = JSON.parse(cached)
      return
    } catch {
      sessionStorage.removeItem(cacheKey)
    }
  }

  relatedLoading.value = true
  relatedError.value = null
  try {
    const data = await fetchRelatedArticles(articleId)
    if (data && data.length > 0) {
      relatedArticles.value = data
      sessionStorage.setItem(cacheKey, JSON.stringify(data))
    } else {
      relatedArticles.value = []
    }
  } catch {
    relatedError.value = '加载失败'
  } finally {
    relatedLoading.value = false
  }
}

async function loadComments() {
  const articleId = route.params.id
  if (!articleId) return

  commentLoading.value = true
  commentError.value = ''
  try {
    const data = await fetchArticleComments(articleId, {
      page: commentPage.value,
      size: 10,
      sort: commentSort.value
    })
    if (data) {
      if (commentPage.value === 1) {
        comments.value = data.comments || []
      } else {
        comments.value = [...comments.value, ...(data.comments || [])]
      }
      commentTotal.value = data.total || 0
      hasMoreComments.value = comments.value.length < data.total
    }
  } catch {
    commentError.value = '加载评论失败'
  } finally {
    commentLoading.value = false
  }
}

function switchSort(sort) {
  if (commentSort.value === sort) return
  commentSort.value = sort
  commentPage.value = 1
  comments.value = []
  loadComments()
}

function loadMoreComments() {
  commentPage.value++
  loadComments()
}

async function submitComment() {
  if (!draft.value.trim()) {
    commentError.value = '请输入评论内容'
    return
  }
  if (draft.value.length > 2000) {
    commentError.value = '评论内容不能超过2000个字符'
    return
  }

  submitting.value = true
  commentError.value = ''
  try {
    const data = await createArticleComment(route.params.id, {
      content: draft.value,
      guest_name: guestName.value
    })
    if (data) {
      draft.value = ''
      commentPage.value = 1
      comments.value = []
      await loadComments()
    }
  } catch (err) {
    if (err.response && err.response.data && err.response.data.detail) {
      commentError.value = err.response.data.detail
    } else {
      commentError.value = '评论提交失败，请稍后重试'
    }
  } finally {
    submitting.value = false
  }
}

const replyTargetId = ref(null)
const replyTargetName = ref('')

function toggleReplyInput(commentId, parentId = null, targetName = '') {
  if (replyInputId.value === commentId) {
    replyInputId.value = null
    replyTargetId.value = null
    replyTargetName.value = ''
  } else {
    replyInputId.value = commentId
    replyTargetId.value = parentId
    replyTargetName.value = targetName
    replyDraft.value = ''
  }
}

async function submitReply(parentId, replyToId = null, replyToName = '') {
  if (!replyDraft.value.trim()) return

  replySubmitting.value = true
  try {
    const data = await createArticleComment(route.params.id, {
      content: replyDraft.value,
      parent_id: parentId,
      reply_to_id: replyToId,
      reply_to_name: replyToName,
      guest_name: guestName.value
    })
    if (data) {
      replyDraft.value = ''
      replyInputId.value = null
      replyTargetId.value = null
      replyTargetName.value = ''
      commentPage.value = 1
      comments.value = []
      await loadComments()
    }
  } catch (err) {
    commentError.value = '回复提交失败'
  } finally {
    replySubmitting.value = false
  }
}

async function loadArticle() {
  const articleId = route.params.id
  if (!articleId) {
    error.value = '文章 ID 不存在'
    return
  }

  loading.value = true
  error.value = null
  try {
    const data = await fetchArticle(articleId)
    if (data) {
      article.value = data
      await nextTick()
      setupSectionObserver()
    } else {
      error.value = '文章不存在或已被删除'
    }
  } catch {
    error.value = '加载文章失败'
  } finally {
    loading.value = false
  }
}

const likingArticle = ref(false)
const collectingArticle = ref(false)

async function handleLikeArticle() {
  if (likingArticle.value) return
  const articleId = route.params.id
  if (!articleId) return
  likingArticle.value = true
  try {
    const result = await likeArticle(articleId)
    if (result && result.data) {
      if (article.value) {
        article.value.like_count = result.data.liked
          ? (article.value.like_count || 0) + 1
          : Math.max(0, (article.value.like_count || 0) - 1)
      }
    }
  } catch {
    console.error('点赞失败')
  } finally {
    likingArticle.value = false
  }
}

async function handleCollectArticle() {
  if (collectingArticle.value) return
  const articleId = route.params.id
  if (!articleId) return
  collectingArticle.value = true
  try {
    const result = await collectArticle(articleId)
    if (result && result.data && article.value) {
      article.value.collect_count = result.data.collected
        ? (article.value.collect_count || 0) + 1
        : Math.max(0, (article.value.collect_count || 0) - 1)
    }
  } catch {
    console.error('收藏失败')
  } finally {
    collectingArticle.value = false
  }
}

async function handleShareArticle() {
  const url = window.location.href
  try {
    await navigator.clipboard.writeText(url)
    alert('链接已复制到剪贴板')
  } catch {
    prompt('复制链接分享：', url)
  }
}

onMounted(async () => {
  guestName.value = generateGuestName()
  const settings = await fetchSiteSettings().catch(() => null)
  if (settings) siteSettings.value = settings
  loadArticle()
  loadRelatedArticles()
  loadComments()
})

watch(() => route.params.id, () => {
  if (observer) observer.disconnect()
  activeSection.value = ''
  guestName.value = generateGuestName()
  commentPage.value = 1
  comments.value = []
  commentTotal.value = 0
  loadArticle()
  loadRelatedArticles()
  loadComments()
  window.scrollTo({ top: 0, behavior: 'smooth' })
})

onBeforeUnmount(() => {
  if (observer) observer.disconnect()
})
</script>

<style scoped>
.hero-grid-overlay {
  background-image:
    linear-gradient(rgba(120, 160, 255, 0.18) 1px, transparent 1px),
    linear-gradient(90deg, rgba(120, 160, 255, 0.18) 1px, transparent 1px);
  background-size: 34px 34px;
}

.right-sticky-wrapper {
  position: sticky;
  top: 16px;
  max-height: calc(100vh - 32px);
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-width: none;
  padding: 10px;
  margin: -10px;
  margin-top: 0;
}

.right-sticky-wrapper::-webkit-scrollbar {
  display: none;
}

.article-content :deep(h1),
.article-content :deep(h2),
.article-content :deep(h3),
.article-content :deep(h4) {
  margin-top: 1.5rem;
  margin-bottom: 0.75rem;
  font-weight: 700;
  color: #0f172a;
}

.article-content :deep(h2) {
  font-size: 1.125rem;
}

.article-content :deep(p) {
  margin-bottom: 0.75rem;
  font-size: 0.875rem;
  line-height: 1.75;
  color: #334155;
}

.article-content :deep(pre) {
  background: #1e293b;
  border-radius: 0.75rem;
  padding: 1rem;
  overflow-x: auto;
  margin: 1rem 0;
}

.article-content :deep(code) {
  font-size: 0.8125rem;
  color: #e2e8f0;
  line-height: 1.6;
}

.article-content :deep(img) {
  max-width: 100%;
  height: auto;
  border-radius: 0.75rem;
  margin: 1rem 0;
}

.article-content :deep(blockquote) {
  border-left: 4px solid #2563eb;
  padding-left: 1rem;
  margin: 1rem 0;
  color: #64748b;
  font-style: italic;
}

.article-content :deep(ul),
.article-content :deep(ol) {
  margin: 0.75rem 0;
  padding-left: 1.5rem;
  color: #334155;
  font-size: 0.875rem;
  line-height: 1.75;
}

.article-content :deep(li) {
  margin-bottom: 0.25rem;
}

.article-content :deep(a) {
  color: #2563eb;
  text-decoration: underline;
}

.article-content :deep(hr) {
  border: none;
  border-top: 1px solid #e2e8f0;
  margin: 1.5rem 0;
}
</style>