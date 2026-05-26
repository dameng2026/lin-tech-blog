<template>
  <!-- 上半部分：首屏区 -->
  <div class="home-page p-[1.75rem] bg-[#f8f9fd]">
    <div class="grid grid-cols-1 lg:grid-cols-5 gap-6 mb-8 home-top-grid" style="margin-left: -1.75rem">
      <!-- 左侧：Hero 首屏区（占宽80%）-->
      <div class="lg:col-span-4 bg-[linear-gradient(to_right,#fcfdfd_0%,#fcfdfd_30%,transparent_100%)]">
        <div class="rounded-xl p-8 pb-[70px] relative overflow-hidden shadow-sm h-[420px] home-hero-card">
          <!-- 3D 插画作为绝对定位背景（最终设计图效果）-->
          <div class="absolute right-0 top-0 w-[40%] h-[100%] flex items-center justify-end pointer-events-none">
            <img src="/images/hero-3d.png" alt="AI Cube"
              class="w-auto h-full object-contain object-right-center ml-auto" />
          </div>

          <div class="relative z-10">
            <!-- 顶部标签：宽度由内容撑开，不占满整行 -->
            <p
              class="inline-flex items-center text-sm mb-4 bg-blue-50 px-3 py-1.5 rounded-full pl-[1rem] text-blue-700">
               <img src="/icons/applaud.svg" alt="Applaud" class="w-4 h-4 mr-2" />
              你好，我是 Lin
            </p>

            <h1 class="text-[2rem] font-bold text-gray-900 mb-4 tracking-wide pl-[1rem]">
              专注 <span class="text-blue-600">Agent 开发与前端技术</span>
            </h1>
            <h2 class="text-[2rem] font-bold text-gray-900 mb-6 tracking-wide pl-[1rem]">
              构建智能与体验兼备的产品
            </h2>

            <div class="text-gray-600 text-[15px] mb-4 max-w-2xl space-y-2 leading-relaxed pl-[1rem]">
              <p>热爱技术，喜欢构建有价值的应用。</p>
              <p>在 Agent、LLM 应用、前端工程化等领域不断探索与实践。</p>
            </div>

            <div class="flex flex-wrap gap-4 mb-8 pl-[1rem]">
              <button
                class="px-7 py-3 bg-blue-600 text-white rounded-lg font-medium text-[15px] hover:bg-blue-700 transition-all">
                查看我的项目</button>
              <button
                class="px-7 py-3 bg-white text-gray-900 border border-gray-300 rounded-lg font-medium text-[15px] hover:bg-gray-50 transition-all">
                阅读我的文章
              </button>
            </div>

            <div class="flex flex-wrap gap-3 mb-4">
              <span class="flex items-center px-4 py-2 bg-white rounded-lg text-[0.75rem] font-medium text-gray-700">
                <img src="/icons/typescript.svg" alt="TypeScript" class="w-4 h-4 mr-2" />
                TypeScript
              </span>
              <span class="flex items-center px-4 py-2 bg-white rounded-lg text-[0.75rem] font-medium text-gray-700">
                <img src="/icons/react.svg" alt="React" class="w-4 h-4 mr-2" />
                React
              </span>
              <span class="flex items-center px-4 py-2 bg-white rounded-lg text-[0.75rem] font-medium text-gray-700">
                <img src="/icons/next-js.svg" alt="Next.js" class="w-4 h-4 mr-2" />
                Next.js
              </span>
              <span class="flex items-center px-4 py-2 bg-white rounded-lg text-[0.75rem] font-medium text-gray-700">
                <img src="/icons/langChain.svg" alt="LangChain" class="w-4 h-4 mr-2" />
                LangChain
              </span>
              <span class="flex items-center px-4 py-2 bg-white rounded-lg text-[0.75rem] font-medium text-gray-700">
                <img src="/icons/python.svg" alt="Python" class="w-4 h-4 mr-2" />
                Python
              </span>
              <span class="flex items-center px-4 py-2 bg-white rounded-lg text-[0.75rem] font-medium text-gray-700">
                <img src="/icons/tailwind.svg" alt="Tailwind CSS" class="w-4 h-4 mr-2" />
                Tailwind CSS
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- 右侧：个人简介卡片（占宽20%）-->
      <div class="lg:col-span-1 home-profile-col">
        <div class="bg-white rounded-xl shadow-sm p-6 h-full flex flex-col home-profile-card">
          <!-- 第一块：头像和个人信息 -->
          <div class="flex flex-col items-center mb-6">
            <div class="w-[5rem] h-[5rem] rounded-full overflow-hidden flex-shrink-0 mb-3">
              <img src="/images/avatar.png" alt="Lin" class="w-full h-full object-cover" />
            </div>
            <h3 class="font-bold text-xl text-gray-900 mb-1">Lin</h3>
            <p class="text-sm text-gray-600">全栈开发 & AI 应用探索。</p>
          </div>

          <!-- 第二块：个人信息 -->
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
              5 年开发经验            </div>
          </div>

          <!-- 第三块：下载简历 -->
          <button
            @click="openModal"
            class="w-full py-2.5 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-all flex items-center justify-center mt-auto">
            <img src="/icons/download.svg" alt="下载" class="w-4 h-4 mr-2" />
            下载简历(PDF)
          </button>
        </div>
      </div>
    </div>

    <!-- 下半部分：内容区 -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 home-content-grid" style="margin-left: -1.75rem">
      <!-- 左侧：精选项目、最新文章等模块（占宽约75%）-->
      <div class="lg:col-span-9 bg-white p-8 home-main-col">
        <!-- 精选项目 -->
        <div class="mb-8">
          <div class="flex justify-between items-center mb-4 home-section-header">
            <h2 class="text-[1.3rem] font-bold text-gray-900">精选项目</h2>
            <a href="#" class="text-gray-600 hover:text-gray-700 text-sm font-medium flex items-center gap-1">查看更多
              <img src="/icons/next-grey.svg" alt="arrow" class="w-4 h-4" /></a>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 home-project-grid">
            <!-- 项目卡片 1 -->
            <div
              class="bg-white rounded-xl shadow-sm hover:shadow-md transition-all hover:-translate-y-1 flex flex-col h-[340px] cursor-pointer home-project-card" @click="goToProjectDetail()">
              <div class="flex-[55] bg-gray-100 rounded-t-xl overflow-hidden">
                <img
                  src="https://images.unsplash.com/photo-1677442136019-21780ecad96a?auto=format&fit=crop&w=800&q=80"
                  alt="ChatFlow" class="w-full h-full object-cover" />
              </div>
              <div class="flex-[45] p-4 overflow-hidden flex flex-col">
                <h3 class="font-semibold text-gray-900 mb-2 flex-shrink-0">
                  ChatFlow - 智能对话工作流平台                </h3>
                <p class="text-sm text-gray-600 mb-3 flex-1 overflow-hidden">
                  基于 Agent 架构的对话式 AI
                  平台，支持多轮对话、工作流编排与知识管理。                </p>
                <div class="flex flex-wrap gap-2 flex-shrink-0">
                  <span class="px-[0.8rem] py-[0.3rem] bg-gray-100 rounded-lg text-xs text-gray-700">Next.js</span>
                  <span class="px-[0.8rem] py-[0.3rem] bg-gray-100 rounded-lg text-xs text-gray-700">TypeScript</span>
                  <span class="px-[0.8rem] py-[0.3rem] bg-gray-100 rounded-lg text-xs text-gray-700">LangChain</span>
                </div>
              </div>
            </div>

            <!-- 项目卡片 2 -->
            <div
              class="bg-white rounded-xl shadow-sm hover:shadow-md transition-all hover:-translate-y-1 flex flex-col h-[340px] cursor-pointer home-project-card" @click="goToProjectDetail()">
              <div class="flex-[55] bg-gray-100 rounded-t-xl overflow-hidden">
                <img
                  src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=800&q=80"
                  alt="LLM Knowledge Hub" class="w-full h-full object-cover" />
              </div>
              <div class="flex-[45] p-4 overflow-hidden flex flex-col">
                <h3 class="font-semibold text-gray-900 mb-2 flex-shrink-0">
                  LLM Knowledge Hub
                </h3>
                <p class="text-sm text-gray-600 mb-3 flex-1 overflow-hidden">
                  个人知识管理大语言系统，支持文档解析、内向搜索与 RAG 增强。                </p>
                <div class="flex flex-wrap gap-2 flex-shrink-0">
                  <span class="px-[0.8rem] py-[0.3rem] bg-gray-100 rounded-lg text-xs text-gray-700">Python</span>
                  <span class="px-[0.8rem] py-[0.3rem] bg-gray-100 rounded-lg text-xs text-gray-700">FastAPI</span>
                  <span class="px-[0.8rem] py-[0.3rem] bg-gray-100 rounded-lg text-xs text-gray-700">Milvus</span>
                </div>
              </div>
            </div>

            <!-- 项目卡片 3 -->
            <div
              class="bg-white rounded-xl shadow-sm hover:shadow-md transition-all hover:-translate-y-1 flex flex-col h-[340px] cursor-pointer home-project-card" @click="goToProjectDetail()">
              <div class="flex-[55] bg-gray-100 rounded-t-xl overflow-hidden">
                <img
                  src="https://images.unsplash.com/photo-1633356122544-f134324a6cee?auto=format&fit=crop&w=800&q=80"
                  alt="Frontier UI" class="w-full h-full object-cover" />
              </div>
              <div class="flex-[45] p-4 overflow-hidden flex flex-col">
                <h3 class="font-semibold text-gray-900 mb-2 flex-shrink-0">
                  Frontier UI
                </h3>
                <p class="text-sm text-gray-600 mb-3 flex-1 overflow-hidden">
                  一个现代化的前端组件库，专注于易用性、可访问性与性能特性。                </p>
                <div class="flex flex-wrap gap-2 flex-shrink-0">
                  <span class="px-[0.8rem] py-[0.3rem] bg-gray-100 rounded-lg text-xs text-gray-700">React</span>
                  <span class="px-[0.8rem] py-[0.3rem] bg-gray-100 rounded-lg text-xs text-gray-700">TypeScript</span>
                  <span class="px-[0.8rem] py-[0.3rem] bg-gray-100 rounded-lg text-xs text-gray-700">Tailwind CSS</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 最新文章 -->
        <div>
          <div class="flex justify-between items-center mb-4 home-section-header">
            <h2 class="text-[1.3rem] font-bold text-gray-900 pl-[0.7rem]">
              最新文章            </h2>
            <a href="#" class="text-gray-600 hover:text-gray-700 text-sm font-medium flex items-center gap-1">查看更多
              <img src="/icons/next-grey.svg" alt="arrow" class="w-4 h-4" /></a>
          </div>
          <div class="space-y-4">
            <!-- 文章卡片 1 -->
            <div
              class="bg-white rounded-xl shadow-sm hover:shadow-md transition-all hover:-translate-y-1 px-[0.7rem] py-[0.7rem] flex gap-4 h-[160px] home-article-card">
              <div class="w-60 h-full flex-shrink-0">
                <img
                  src="https://oss.zibll.com/zibll.com/2021/04/%E7%BC%93%E5%AD%98%E5%8A%A0%E9%80%9F-%E5%88%97%E8%A1%A8%E5%9B%BE.jpg"
                  alt="深入理解 Agent" class="w-full h-full object-cover rounded-lg" />
              </div>
              <div class="flex-1 flex flex-col justify-between py-[0.7rem]">
                <h3 class="font-semibold text-gray-900">
                  深入理解 Agent：从原理到实践                </h3>
                <p class="text-sm text-gray-600">
                  系统介绍 Agent
                  的核心概念、设计模式与实现路径，并通过一个完整案例带你构建属于自己的
                  Agent 系统。                </p>
                <div class="flex items-center text-xs text-gray-500">
                  <img src="/icons/time.svg" alt="date" class="w-3 h-3 mr-1" />
                  <span>2024-04-20</span>
                  <span class="mx-2">|</span>
                  <img src="/icons/folder.svg" alt="category" class="w-3 h-3 mr-1" />
                  <span>agent</span>
                  <span class="mx-2">|</span>
                  <img src="/icons/reading.svg" alt="views" class="w-3 h-3 mr-1" />
                  <span>1.2k</span>
                </div>
              </div>
              <div class="flex items-center justify-center mr-10">
                <img src="/icons/flag-grey.svg" alt="favorite" class="w-5 h-5 text-gray-400" />
              </div>
            </div>

            <!-- 文章卡片 2 -->
            <div
              class="bg-white rounded-xl shadow-sm hover:shadow-md transition-all hover:-translate-y-1 px-[0.7rem] py-[0.7rem] flex gap-4 h-[160px] home-article-card">
              <div class="w-60 h-full flex-shrink-0">
                <img
                  src="https://oss.zibll.com/zibll.com/2025/09/20250924132242563-%E5%95%86%E5%9F%8E-%E7%89%B9%E8%89%B2%E5%9B%BE.jpg?x-oss-process=image%2Fquality,q_50%2Fresize,m_fill,w_700,h_485"
                  alt="React 19 新特性详解与实践" class="w-full h-full object-cover rounded-lg" />
              </div>
              <div class="flex-1 flex flex-col justify-between py-[0.7rem]">
                <h3 class="font-semibold text-gray-900">
                  React 19 新特性详解与实践
                </h3>
                <p class="text-sm text-gray-600">
                  全面解析 React 19 的新特性，结合实际场景，Server
                  Components、Actions 等能力的最佳实践。                </p>
                <div class="flex items-center text-xs text-gray-500">
                  <img src="/icons/time.svg" alt="date" class="w-3 h-3 mr-1" />
                  <span>2024-04-12</span>
                  <span class="mx-2">|</span>
                  <img src="/icons/folder.svg" alt="category" class="w-3 h-3 mr-1" />
                  <span>React</span>
                  <span class="mx-2">|</span>
                  <img src="/icons/reading.svg" alt="views" class="w-3 h-3 mr-1" />
                  <span>869</span>
                </div>
              </div>
              <div class="flex items-center justify-center mr-10">
                <img src="/icons/flag-grey.svg" alt="favorite" class="w-5 h-5 text-gray-400" />
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 右侧：技术栈、站点数据、最近动态等模块（占宽约25%）-->
      <div class="lg:col-span-3 home-sidebar-col">
        <!-- 技术栈 -->
        <div class="bg-white rounded-xl shadow-sm px-[2rem] py-6 mb-6 home-widget-card">
          <h3 class="font-semibold text-gray-900 mb-3">技术栈</h3>
          <div class="flex flex-wrap gap-2">
            <span class="px-[1rem] py-[0.5rem] bg-gray-100 rounded-lg text-xs text-gray-700">TypeScript</span>
            <span class="px-[1rem] py-[0.5rem] bg-gray-100 rounded-lg text-xs text-gray-700">JavaScript</span>
            <span class="px-[1rem] py-[0.5rem] bg-gray-100 rounded-lg text-xs text-gray-700">React</span>
            <span class="px-[1rem] py-[0.5rem] bg-gray-100 rounded-lg text-xs text-gray-700">Next.js</span>
            <span class="px-[1rem] py-[0.5rem] bg-gray-100 rounded-lg text-xs text-gray-700">Node.js</span>
            <span class="px-[1rem] py-[0.5rem] bg-gray-100 rounded-lg text-xs text-gray-700">Python</span>
            <span class="px-[1rem] py-[0.5rem] bg-gray-100 rounded-lg text-xs text-gray-700">LangChain</span>
            <span class="px-[1rem] py-[0.5rem] bg-gray-100 rounded-lg text-xs text-gray-700">FastAPI</span>
            <span class="px-[1rem] py-[0.5rem] bg-gray-100 rounded-lg text-xs text-gray-700">Tailwind CSS</span>
            <span class="px-[1rem] py-[0.5rem] bg-gray-100 rounded-lg text-xs text-gray-700">PostgreSQL</span>
            <span class="px-[1rem] py-[0.5rem] bg-gray-100 rounded-lg text-xs text-gray-700">Docker</span>
            <span class="px-[1rem] py-[0.5rem] bg-gray-100 rounded-lg text-xs text-gray-700">Git</span>
          </div>
        </div>

        <!-- 站点数据 -->
        <div class="bg-white rounded-xl shadow-sm px-[2rem] py-6 mb-6 home-widget-card">
          <h3 class="font-semibold text-gray-900 mb-4">站点数据</h3>
          <div class="flex justify-between">
            <div class="flex flex-col items-center">
              <div class="w-12 h-12 rounded-full bg-[#f6f7fb] flex items-center justify-center mb-3">
                <img src="/icons/article-blue.svg" alt="文章" class="w-6 h-6 text-blue-600" />
              </div>
              <div class="text-[0.8rem] text-gray-500 py-1">文章</div>
              <div class="text-2xl font-bold text-gray-900">32</div>
            </div>
            <div class="flex flex-col items-center">
              <div class="w-12 h-12 rounded-full bg-[#f6f7fb] flex items-center justify-center mb-3">
                <img src="/icons/project-grey.svg" alt="项目" class="w-6 h-6 text-blue-600" />
              </div>
              <div class="text-[0.8rem] text-gray-500 py-1">项目</div>
              <div class="text-2xl font-bold text-gray-900">12</div>
            </div>
            <div class="flex flex-col items-center">
              <div class="w-12 h-12 rounded-full bg-[#f6f7fb] flex items-center justify-center mb-3">
                <img src="/icons/eye.svg" alt="访问量" class="w-6 h-6 text-blue-600" />
              </div>
              <div class="text-[0.8rem] text-gray-500 py-1">访问量</div>
              <div class="text-2xl font-bold text-gray-900">18.6k</div>
            </div>
            <div class="flex flex-col items-center">
              <div class="w-12 h-12 rounded-full bg-[#f6f7fb] flex items-center justify-center mb-3">
                <img src="/icons/calendar.svg" alt="运行天数" class="w-6 h-6 text-blue-600" />
              </div>
              <div class="text-[0.8rem] text-gray-500 py-1">运行天数</div>
              <div class="text-2xl font-bold text-gray-900">236</div>
            </div>
          </div>
        </div>

        <!-- 最近动态 -->
        <div class="bg-white rounded-xl shadow-sm px-[2rem] py-6 home-widget-card">
          <h3 class="font-semibold text-gray-900 mb-3">最近动态</h3>
          <div class="space-y-3">
            <div class="flex items-start gap-3 py-2">
              <div class="w-1.5 h-1.5 rounded-full bg-blue-600 mt-1.5 flex-shrink-0"></div>
              <div class="flex-1 text-[0.8rem]">
                <div class="flex justify-between">
                  <p class="text-gray-900">
                    发布了新文章
                    <a href="#" class="text-blue-600 hover:underline">《深入理解 Agent：从原理到实践》</a>
                  </p>
                  <p class="text-gray-500">2 天前</p>
                </div>
              </div>
            </div>
            <div class="flex items-start gap-3 py-2">
              <div class="w-1.5 h-1.5 rounded-full bg-blue-600 mt-1.5 flex-shrink-0"></div>
              <div class="flex-1 text-[0.8rem]">
                <div class="flex justify-between">
                  <p class="text-gray-900">
                    更新了项目
                    <a href="#" class="text-blue-600 hover:underline">ChatFlow - 智能对话工作流平台</a>
                  </p>
                  <p class="text-gray-500">5 天前</p>
                </div>
              </div>
            </div>
            <div class="flex items-start gap-3 py-2">
              <div class="w-1.5 h-1.5 rounded-full bg-blue-600 mt-1.5 flex-shrink-0"></div>
              <div class="flex-1 text-[0.8rem]">
                <div class="flex justify-between">
                  <p class="text-gray-900">
                    发布了新文章
                    <a href="#" class="text-blue-600 hover:underline">《React 19 新特性详解与实践》</a>
                  </p>
                  <p class="text-gray-500">8 天前</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { usePdfModal } from '../composables/usePdfModal'

const router = useRouter()
const { openModal } = usePdfModal()

const goToProjectDetail = () => {
  router.push('/project/1')
}
</script>

<style scoped>
.home-page {
  background: #f8f9fd;
  padding: 1.75rem;
}

@media (max-width: 768px) {
  .home-profile-col {
    display: none;
  }

  .home-page {
    padding: 0.75rem 0.75rem 1rem;
  }

  .home-top-grid,
  .home-content-grid {
    margin-left: 0 !important;
  }

  .home-top-grid,
  .home-content-grid {
    gap: 0.75rem;
  }

  .home-hero-card {
    height: auto;
    min-height: 0;
    padding: 1rem;
    padding-bottom: 1rem;
    border-radius: 1rem;
  }

  .home-hero-card > .absolute {
    position: relative;
    right: auto;
    top: auto;
    width: 100%;
    height: auto;
    justify-content: center;
    margin-bottom: 0.75rem;
  }

  .home-hero-card > .absolute img {
    width: min(100%, 19rem);
    height: auto;
    margin-left: 0;
  }

  .home-hero-card .relative.z-10 {
    padding-top: 0;
  }

  .home-hero-card p.inline-flex,
  .home-hero-card h1,
  .home-hero-card h2,
  .home-hero-card .text-gray-600,
  .home-hero-card .flex.flex-wrap.gap-4,
  .home-hero-card .flex.flex-wrap.gap-3 {
    padding-left: 0;
  }

  .home-hero-card p.inline-flex {
    font-size: 0.75rem;
    margin-bottom: 0.75rem;
    padding: 0.35rem 0.75rem;
  }

  .home-hero-card h1,
  .home-hero-card h2 {
    font-size: 1.45rem;
    line-height: 1.22;
    margin-bottom: 0.5rem;
    letter-spacing: 0;
  }

  .home-hero-card .text-gray-600 {
    font-size: 0.8rem;
    line-height: 1.7;
    margin-bottom: 0.75rem;
  }

  .home-hero-card .flex.flex-wrap.gap-4 {
    gap: 0.85rem;
    margin-bottom: 0.85rem;
  }

  .home-hero-card .flex.flex-wrap.gap-4 button {
    width: 100%;
    padding: 0.8rem 1rem;
    font-size: 0.95rem;
    border-radius: 0.85rem;
  }

  .home-hero-card .flex.flex-wrap.gap-3 {
    display: none;
  }

  .home-hero-card .flex.flex-wrap.gap-3 span {
    padding: 0.4rem 0.7rem;
    border-radius: 0.75rem;
    font-size: 0.7rem;
  }

  .home-profile-card,
  .home-main-col,
  .home-widget-card {
    padding: 0.9rem;
    border-radius: 1rem;
  }

  .home-profile-card {
    align-items: center;
  }

  .home-profile-card .mb-6 {
    margin-bottom: 0.85rem;
  }

  .home-profile-card .w-\[5rem\] {
    width: 4.25rem;
    height: 4.25rem;
  }

  .home-profile-card h3 {
    font-size: 1.05rem;
  }

  .home-profile-card p,
  .home-profile-card .space-y-3 .flex {
    font-size: 0.82rem;
  }

  .home-profile-card button {
    padding: 0.75rem 0.9rem;
    border-radius: 0.8rem;
  }

  .home-main-col {
    padding-top: 1rem;
    padding-bottom: 1rem;
  }

  .home-section-header {
    margin-bottom: 0.75rem;
  }

  .home-section-header h2 {
    font-size: 1.05rem;
  }

  .home-section-header a {
    font-size: 0.75rem;
  }

  .home-project-grid {
    grid-template-columns: 1fr;
  }

  .home-project-card {
    height: auto;
    min-height: 0;
  }

  .home-project-card .flex-\[55\] {
    flex: 0 0 auto;
    aspect-ratio: 16 / 9;
  }

  .home-project-card .flex-\[45\] {
    padding: 0.9rem;
  }

  .home-project-card h3 {
    font-size: 0.95rem;
    line-height: 1.35;
  }

  .home-project-card p {
    font-size: 0.8rem;
    line-height: 1.6;
  }

  .home-project-card .flex.flex-wrap.gap-2 {
    gap: 0.35rem;
  }

  .home-article-card {
    height: auto;
    gap: 0.75rem;
    padding: 0.75rem;
    align-items: stretch;
  }

  .home-article-card .w-60 {
    width: 5.8rem;
    height: 5.8rem;
    flex-shrink: 0;
  }

  .home-article-card h3 {
    font-size: 0.92rem;
    line-height: 1.4;
  }

  .home-article-card p {
    font-size: 0.76rem;
    line-height: 1.55;
  }

  .home-article-card .mr-10 {
    display: none;
  }

  .home-article-card .flex.items-center.text-xs,
  .home-article-card .text-xs.text-gray-500 {
    font-size: 0.68rem;
  }

  .home-widget-card {
    margin-bottom: 0.75rem;
  }

  .home-widget-card .flex.justify-between {
    gap: 0.75rem;
  }

  .home-widget-card h3 {
    font-size: 0.95rem;
  }

  .home-widget-card .flex.flex-wrap.gap-2 span {
    padding: 0.38rem 0.7rem;
    border-radius: 0.7rem;
  }

  .home-widget-card .flex.justify-between > div {
    flex: 1;
  }

  .home-widget-card .flex.justify-between {
    flex-wrap: wrap;
    gap: 0.6rem 0;
  }

  .home-widget-card .flex.justify-between .text-2xl {
    font-size: 1.35rem;
  }

  .home-widget-card .space-y-3 .flex.justify-between {
    align-items: flex-start;
  }

  .home-widget-card .space-y-3 .flex.justify-between p:last-child {
    margin-left: 0.5rem;
    flex-shrink: 0;
  }
}
</style>
