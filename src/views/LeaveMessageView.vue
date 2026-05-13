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
            <div class="text-xs lg:text-[14px] font-medium text-slate-700">全部留言 <span class="text-slate-400">(28)</span></div>
            <div class="flex items-center gap-2">
              <button class="h-7 lg:h-9 px-3 lg:px-4 rounded-[10px] border border-slate-200 bg-white text-xs lg:text-[13px] text-slate-600 flex items-center gap-2">全部</button>
              <button class="h-7 lg:h-9 px-3 lg:px-4 rounded-[10px] border border-slate-200 bg-white text-xs lg:text-[13px] text-slate-600 flex items-center gap-2">最新</button>
            </div>
          </div>

          <section class="space-y-3 lg:space-y-4">
            <article v-for="item in comments" :key="item.name + item.time" class="rounded-[16px] bg-white border border-slate-100 shadow-[0_8px_24px_rgba(15,23,42,0.05)] p-3 lg:p-4">
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
                  <button class="mt-2 text-[11px] lg:text-[12px] text-slate-500 hover:text-slate-700">回复</button>
                </div>
                <div class="flex items-center gap-1 text-slate-400 text-xs lg:text-[13px] pl-1 lg:pl-2 pt-0.5 lg:pt-1">
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
                    <button class="mt-2 text-[11px] lg:text-[12px] text-slate-500 hover:text-slate-700">回复</button>
                  </div>
                  <div class="flex items-center gap-1 text-slate-400 text-xs lg:text-[13px] pl-1 lg:pl-2 pt-0.5 lg:pt-1">
                    <span>👍</span><span class="text-slate-500">{{ item.reply.likes }}</span>
                  </div>
                </div>
              </div>
            </article>
          </section>

          <div class="flex items-center justify-center gap-2 mt-4 lg:mt-6">
            <button class="w-6 h-6 lg:w-8 lg:h-8 rounded-[8px] bg-[#1f5cff] text-white text-xs lg:text-[13px] font-medium">1</button>
            <button class="w-6 h-6 lg:w-8 lg:h-8 rounded-[8px] border border-slate-200 bg-white text-slate-600 text-xs lg:text-[13px]">2</button>
            <button class="w-6 h-6 lg:w-8 lg:h-8 rounded-[8px] border border-slate-200 bg-white text-slate-600 text-xs lg:text-[13px]">3</button>
            <span class="px-1 text-slate-400">...</span>
            <button class="w-6 h-6 lg:w-8 lg:h-8 rounded-[8px] border border-slate-200 bg-white text-slate-600 text-xs lg:text-[13px]">6</button>
            <button class="w-6 h-6 lg:w-8 lg:h-8 rounded-[8px] border border-slate-200 bg-white text-slate-600 text-xs lg:text-[13px]">下一页</button>
          </div>
        </main>

        <aside class="hidden lg:block lg:w-1/5 space-y-4">
          <section class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6 flex flex-col">
            <div class="flex flex-col items-center mb-6">
              <div class="w-[5rem] h-[5rem] rounded-full overflow-hidden flex-shrink-0 mb-3">
                <img src="/images/avatar.png" alt="Lin" class="w-full h-full object-cover" />
              </div>
              <h3 class="font-bold text-xl text-gray-900 mb-1">Lin</h3>
              <p class="text-sm text-gray-600">全栈开发 & AI 应用探索。</p>
            </div>
            <div class="w-full space-y-3 mb-6">
              <div class="flex items-center text-sm text-gray-600">
                <img src="/icons/position-black.svg" alt="地址" class="w-4 h-4 mr-2" />
                中国 · 深圳
              </div>
              <div class="flex items-center text-sm text-gray-600">
                <img src="/icons/email-black.svg" alt="邮箱" class="w-4 h-4 mr-2" />
                lin@example.com
              </div>
              <div class="flex items-center text-sm text-gray-600">
                <img src="/icons/github-black.svg" alt="GitHub" class="w-4 h-4 mr-2" />
                github.com/linxxxx
              </div>
              <div class="flex items-center text-sm text-gray-600">
                <img src="/icons/project-black.svg" alt="开发经验" class="w-4 h-4 mr-2" />
                5 年开发经验
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
              <div v-for="c in recent" :key="c.name" class="flex items-center gap-3">
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
import { usePdfModal } from '../composables/usePdfModal'

const { openModal } = usePdfModal()

const form = {
  message: '',
  email: ''
}

const comments = [
  {
    name: '小明同学',
    time: '2 小时前',
    avatar: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=120&q=80',
    text: '你好！你的 Agent 系列文章写得非常棒，受益匪浅！请问关于多 Agent 协作的部分，是否有具体的代码示例可以参考？',
    likes: 3,
    reply: null
  },
  {
    name: 'TechLover',
    time: '1 天前',
    avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=120&q=80',
    text: '项目很有启发性！想请教 Frontier UI 中的权限管理是如何实现的？使用的是哪种技术栈?',
    likes: 1,
    reply: {
      name: 'Lin（博主）',
      time: '20 小时前',
      avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=120&q=80',
      text: '感谢关注！权限管理使用了 Next.js Auth + Prisma + PostgreSQL 实现，具体实现细节会在后续文章中分享 😊',
      likes: 2
    }
  },
  {
    name: 'AI 探索者',
    time: '3 天前',
    avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=120&q=80',
    text: '请问 ChatFlow 的 RAG 部分支持自定义知识库吗？可以上传自己的文档进行训练吗?',
    likes: 2,
    reply: {
      name: 'Lin（博主）',
      time: '2 天前',
      avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=120&q=80',
      text: '支持的！可以上传 PDF、Word、TXT 等格式的文档，系统会自动解析并建立向量索引。',
      likes: 1
    }
  }
]

const stats = [
  { icon: '/icons/article-blue.svg', label: '文章', value: '32' },
  { icon: '/icons/project-grey.svg', label: '项目', value: '12' },
  { icon: '/icons/eye.svg', label: '访问量', value: '18.6k' },
  { icon: '/icons/calendar.svg', label: '运行天数', value: '236' }
]

const recent = [
  { name: '小明同学', time: '2 小时前', avatar: comments[0].avatar, text: '你好！你的 Agent 系列文章写得非常...' },
  { name: 'TechLover', time: '1 天前', avatar: comments[1].avatar, text: '项目很有启发性！想请教 Front...' },
  { name: 'AI 探索者', time: '3 天前', avatar: comments[2].avatar, text: '请问 ChatFlow 的 RAG 部分支持自定...' },
  { name: '开发小王', time: '5 天前', avatar: 'https://images.unsplash.com/photo-1511367461989-f85a21fda167?auto=format&fit=crop&w=120&q=80', text: 'React 19 的新特性介绍很详细，学习了...' }
]

function postMessage() {
  alert('留言已提交（示例）')
}
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
