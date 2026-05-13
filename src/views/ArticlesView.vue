<template>
  <div class="page-container p-3 lg:p-[1.75rem] bg-[#fefefe]">
    <div class="min-h-screen">
      <div class="">
        <div class="flex flex-col lg:flex-row gap-4 lg:gap-8">

          <!-- 中间主内容区 -->
          <div class="lg:flex-1">
            <!-- 顶部区域 -->
            <div class="mb-4 lg:mb-8">
              <h1 class="text-xl lg:text-3xl font-bold text-gray-900">文章</h1>
            <p class="text-gray-600 mt-2 text-xs lg:text-sm">用代码构建想法，让创意落地成为有价值的产品。</p>
            
            <!-- 分类标签 -->
            <div class="flex flex-wrap gap-1.5 lg:gap-2 mt-3 lg:mt-4">
              <a href="#" class="px-3 py-1 bg-blue-50 text-blue-600 rounded-full text-xs lg:text-sm font-medium">全部</a>
              <a href="#" class="px-3 py-1 bg-gray-100 text-gray-600 rounded-full text-xs lg:text-sm hover:bg-gray-200">AI应用</a>
              <a href="#" class="px-3 py-1 bg-gray-100 text-gray-600 rounded-full text-xs lg:text-sm hover:bg-gray-200">工具</a>
              <a href="#" class="px-3 py-1 bg-gray-100 text-gray-600 rounded-full text-xs lg:text-sm hover:bg-gray-200">前端</a>
              <a href="#" class="px-3 py-1 bg-gray-100 text-gray-600 rounded-full text-xs lg:text-sm hover:bg-gray-200">后端</a>
            </div>
          </div>

        <!-- 项目列表 -->
        <div class="space-y-4 lg:space-y-5">
          <!-- 文章 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-all hover:-translate-y-1 p-3 lg:p-6 flex flex-col lg:flex-row gap-3 lg:gap-4 min-h-[180px] cursor-pointer" @click="goToArticleDetail()">
            <div class="w-full h-32 lg:w-60 lg:h-full flex-shrink-0">
              <img src="https://p6-xtjj-sign.byteimg.com/tos-cn-i-73owjymdk6/1721cfed09494cfc828cbbd82b76f0ed~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAgRXJwYW5PbWVy:q75.awebp?rk3s=f64ab15b&x-expires=1778570126&x-signature=mTeeKN%2BRRfyVJV2w5sXz%2B0CIwRM%3D" alt="深入理解 Agent：从原理到实践" class="w-full h-full object-cover rounded-lg">
            </div>
            <div class="flex-1 flex flex-col justify-between py-1">
              <div>
                <h2 class="text-base lg:text-[1.3rem] font-bold text-gray-900 line-clamp-2">深入理解 Agent：从原理到实践</h2>
                <p class="text-gray-500 text-xs lg:text-sm mt-2 lg:mt-3 line-clamp-2">基于 Agent 的知识体系与实践项目，设计并实现一个完整的 Agent 系统，涵盖规划、记忆、工具调用等核心能力。</p>
                <div class="flex flex-wrap gap-1.5 lg:gap-2 mt-2 lg:mt-3">
                  <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-[0.75rem] rounded-lg">Agent</span>
                  <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-[0.75rem] rounded-lg">AI</span>
                  <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-[0.75rem] rounded-lg">LangChain</span>
                </div>
              </div>
              <div class="flex items-center text-xs text-gray-500 mt-2">
                <img src="/icons/calendar.svg" alt="日期" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                <span>2024-05-20</span>
                <span class="w-1 h-1 bg-gray-300 rounded-full mx-1.5 lg:mx-2"></span>
                <img src="/icons/eye.svg" alt="阅读" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                <span>1.2k</span>
                <span class="w-1 h-1 bg-gray-300 rounded-full mx-1.5 lg:mx-2"></span>
                <img src="/icons/like-grey.svg" alt="点赞" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                <span>128</span>
              </div>
            </div>
            <div class="flex items-center">
              <img src="/icons/flag-grey.svg" alt="收藏" class="w-4 h-4 lg:w-5 lg:h-5 text-gray-300 hover:text-yellow-500 cursor-pointer">
            </div>
          </div>

          <!-- 文章 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-all hover:-translate-y-1 p-3 lg:p-6 flex flex-col lg:flex-row gap-3 lg:gap-4 min-h-[180px] cursor-pointer" @click="goToArticleDetail()">
            <div class="w-full h-32 lg:w-60 lg:h-full flex-shrink-0">
              <img src="https://p6-xtjj-sign.byteimg.com/tos-cn-i-73owjymdk6/8fc9c31fa81845f982f3c29779162994~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAgamVmZndhbmc=:q75.awebp?rk3s=f64ab15b&x-expires=1778570126&x-signature=eR0r44eGwmC%2BPgpJwQ7dMKmVm1s%3D" alt="React 19 新特性详解与实践" class="w-full h-full object-cover rounded-lg">
            </div>
            <div class="flex-1 flex flex-col justify-between py-1">
              <div>
                <h2 class="text-base lg:text-[1.3rem] font-bold text-gray-900 line-clamp-2">React 19 新特性详解与实践</h2>
                <p class="text-gray-500 text-xs lg:text-sm mt-2 lg:mt-3 line-clamp-2">全面梳理 React 19 的新特性，结合实际场景探索 Server Components、Actions 等能力的最佳实践。</p>
                <div class="flex flex-wrap gap-1.5 lg:gap-2 mt-2 lg:mt-3">
                  <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-[0.75rem] rounded-lg">React</span>
                  <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-[0.75rem] rounded-lg">TypeScript</span>
                  <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-[0.75rem] rounded-lg">前端</span>
                </div>
              </div>
              <div class="flex items-center text-xs text-gray-500 mt-2">
                <img src="/icons/calendar.svg" alt="日期" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                <span>2024-05-20</span>
                <span class="w-1 h-1 bg-gray-300 rounded-full mx-1.5 lg:mx-2"></span>
                <img src="/icons/eye.svg" alt="阅读" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                <span>899</span>
                <span class="w-1 h-1 bg-gray-300 rounded-full mx-1.5 lg:mx-2"></span>
                <img src="/icons/like-grey.svg" alt="点赞" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                <span>96</span>
              </div>
            </div>
            <div class="flex items-center">
              <img src="/icons/flag-grey.svg" alt="收藏" class="w-4 h-4 lg:w-5 lg:h-5 text-gray-300 hover:text-yellow-500 cursor-pointer">
            </div>
          </div>

          <!-- 文章 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-all hover:-translate-y-1 p-3 lg:p-6 flex flex-col lg:flex-row gap-3 lg:gap-4 min-h-[180px] cursor-pointer" @click="goToArticleDetail()">
            <div class="w-full h-32 lg:w-60 lg:h-full flex-shrink-0">
              <img src="https://p6-xtjj-sign.byteimg.com/tos-cn-i-73owjymdk6/62006a8c1f4048879d0914e9c16ba913~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg5LiJ5Y-q6JCM5paw:q75.awebp?rk3s=f64ab15b&x-expires=1778570126&x-signature=dqLnEb%2FA2bguKbi2VhBDiHXQo5E%3D" alt="LLM Knowledge Hub" class="w-full h-full object-cover rounded-lg">
            </div>
            <div class="flex-1 flex flex-col justify-between py-1">
              <div>
                <h2 class="text-base lg:text-[1.3rem] font-bold text-gray-900 line-clamp-2">LLM Knowledge Hub</h2>
                <p class="text-gray-500 text-xs lg:text-sm mt-2 lg:mt-3 line-clamp-2">个人知识库与大模型问答系统，支持文档解析、向量检索与 RAG 增强，深度管理知识的解决方案。</p>
                <div class="flex flex-wrap gap-1.5 lg:gap-2 mt-2 lg:mt-3">
                  <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-[0.75rem] rounded-lg">Python</span>
                  <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-[0.75rem] rounded-lg">FastAPI</span>
                  <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-[0.75rem] rounded-lg">Milvus</span>
                </div>
              </div>
              <div class="flex items-center text-xs text-gray-500 mt-2">
                <img src="/icons/calendar.svg" alt="日期" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                <span>2024-04-28</span>
                <span class="w-1 h-1 bg-gray-300 rounded-full mx-1.5 lg:mx-2"></span>
                <img src="/icons/eye.svg" alt="阅读" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                <span>1.6k</span>
                <span class="w-1 h-1 bg-gray-300 rounded-full mx-1.5 lg:mx-2"></span>
                <img src="/icons/like-grey.svg" alt="点赞" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                <span>142</span>
              </div>
            </div>
            <div class="flex items-center">
              <img src="/icons/flag-grey.svg" alt="收藏" class="w-4 h-4 lg:w-5 lg:h-5 text-gray-300 hover:text-yellow-500 cursor-pointer">
            </div>
          </div>

          <!-- 文章 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-all hover:-translate-y-1 p-3 lg:p-6 flex flex-col lg:flex-row gap-3 lg:gap-4 min-h-[180px] cursor-pointer" @click="goToArticleDetail()">
            <div class="w-full h-32 lg:w-60 lg:h-full flex-shrink-0">
              <img src="https://p6-xtjj-sign.byteimg.com/tos-cn-i-73owjymdk6/121ee1acb0a54d69b1feae47c195dc4d~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg56iL5bqP5ZGY6bG855qu:q75.awebp?rk3s=f64ab15b&x-expires=1778570126&x-signature=nV56bZPVXQFhQs%2FnrrTBRXGTtGY%3D" alt="ChatFlow - 智能对话工作流平台" class="w-full h-full object-cover rounded-lg">
            </div>
            <div class="flex-1 flex flex-col justify-between py-1">
              <div>
                <h2 class="text-base lg:text-[1.3rem] font-bold text-gray-900 line-clamp-2">ChatFlow - 智能对话工作流平台</h2>
                <p class="text-gray-500 text-xs lg:text-sm mt-2 lg:mt-3 line-clamp-2">基于 Agent 架构的对话式 AI 平台，支持多模型接入、工作流编排与知识集成，构建智能对话系统。</p>
                <div class="flex flex-wrap gap-1.5 lg:gap-2 mt-2 lg:mt-3">
                  <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-[0.75rem] rounded-lg">Next.js</span>
                  <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-[0.75rem] rounded-lg">TypeScript</span>
                  <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-[0.75rem] rounded-lg">LangChain</span>
                </div>
              </div>
              <div class="flex items-center text-xs text-gray-500 mt-2">
                <img src="/icons/calendar.svg" alt="日期" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                <span>2024-04-15</span>
                <span class="w-1 h-1 bg-gray-300 rounded-full mx-1.5 lg:mx-2"></span>
                <img src="/icons/eye.svg" alt="阅读" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                <span>2.3k</span>
                <span class="w-1 h-1 bg-gray-300 rounded-full mx-1.5 lg:mx-2"></span>
                <img src="/icons/like-grey.svg" alt="点赞" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                <span>268</span>
              </div>
            </div>
            <div class="flex items-center">
              <img src="/icons/flag-grey.svg" alt="收藏" class="w-4 h-4 lg:w-5 lg:h-5 text-gray-300 hover:text-yellow-500 cursor-pointer">
            </div>
          </div>

          <!-- 文章 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-all hover:-translate-y-1 p-3 lg:p-6 flex flex-col lg:flex-row gap-3 lg:gap-4 min-h-[180px] cursor-pointer" @click="goToArticleDetail()">
            <div class="w-full h-32 lg:w-60 lg:h-full flex-shrink-0">
              <img src="https://p9-xtjj-sign.byteimg.com/tos-cn-i-73owjymdk6/3d24854d3b704abfb8d66235e9414871~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAgRXJwYW5PbWVy:q75.awebp?rk3s=f64ab15b&x-expires=1778570202&x-signature=YVeR%2FYleUlZdaMEybOtjzC%2FBThE%3D" alt="Frontier UI" class="w-full h-full object-cover rounded-lg">
            </div>
            <div class="flex-1 flex flex-col justify-between py-1">
              <div>
                <h2 class="text-base lg:text-[1.3rem] font-bold text-gray-900 line-clamp-2">Frontier UI</h2>
                <p class="text-gray-500 text-xs lg:text-sm mt-2 lg:mt-3 line-clamp-2">一个现代化的前端组件库，专注于易用性、可访问性与高性能，提供丰富的组件和主题。</p>
                <div class="flex flex-wrap gap-1.5 lg:gap-2 mt-2 lg:mt-3">
                  <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-sm rounded-lg">React</span>
                  <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-sm rounded-lg">TypeScript</span>
                  <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-sm rounded-lg">Tailwind CSS</span>
                </div>
              </div>
              <div class="flex items-center text-xs text-gray-500 mt-2">
                <img src="/icons/calendar.svg" alt="日期" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                <span>2024-03-30</span>
                <span class="w-1 h-1 bg-gray-300 rounded-full mx-1.5 lg:mx-2"></span>
                <img src="/icons/eye.svg" alt="阅读" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                <span>1.1k</span>
                <span class="w-1 h-1 bg-gray-300 rounded-full mx-1.5 lg:mx-2"></span>
                <img src="/icons/like-grey.svg" alt="点赞" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                <span>184</span>
              </div>
            </div>
            <div class="flex items-center">
              <img src="/icons/flag-grey.svg" alt="收藏" class="w-4 h-4 lg:w-5 lg:h-5 text-gray-300 hover:text-yellow-500 cursor-pointer">
            </div>
          </div>

          <!-- 文章 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-all hover:-translate-y-1 p-3 lg:p-6 flex flex-col lg:flex-row gap-3 lg:gap-4 min-h-[180px] cursor-pointer" @click="goToArticleDetail()">
              <div class="w-full h-32 lg:w-60 lg:h-full flex-shrink-0">
                <img src="https://p6-xtjj-sign.byteimg.com/tos-cn-i-73owjymdk6/7dcd89a3ae074df8a5989d768e3b667e~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg5oOz5oOz6IK_5a2Q5Lya5oCO5LmI5YGa:q75.awebp?rk3s=f64ab15b&x-expires=1778570243&x-signature=1AX111FeeVwxmImcjDgsBNLS%2BrA%3D" alt="AI Prompt 工具集" class="w-full h-full object-cover rounded-lg">
              </div>
              <div class="flex-1 flex flex-col justify-between py-1">
                <div>
                  <h2 class="text-base lg:text-[1.3rem] font-bold text-gray-900 line-clamp-2">AI Prompt 工具集</h2>
                  <p class="text-gray-500 text-xs lg:text-sm mt-2 lg:mt-3 line-clamp-2">基于 Agent 思想的提示词管理与优化工具，提供提示词编写、评估、版本管理和效果分析。</p>
                  <div class="flex flex-wrap gap-1.5 lg:gap-2 mt-2 lg:mt-3">
                    <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-[0.75rem] rounded-lg">Python</span>
                    <span class="px-2 py-0.5 bg-[#f5f6fa] text-[#1353fd] text-xs lg:text-[0.75rem] rounded-lg">Streamlit</span>
                  </div>
                </div>
                <div class="flex items-center text-xs text-gray-500 mt-2">
                  <img src="/icons/calendar.svg" alt="日期" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                  <span>2024-03-01</span>
                  <span class="w-1 h-1 bg-gray-300 rounded-full mx-1.5 lg:mx-2"></span>
                  <img src="/icons/eye.svg" alt="阅读" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                  <span>889</span>
                  <span class="w-1 h-1 bg-gray-300 rounded-full mx-1.5 lg:mx-2"></span>
                  <img src="/icons/like-grey.svg" alt="点赞" class="w-3 h-3 lg:w-4 lg:h-4 mr-1.5 lg:mr-2">
                  <span>72</span>
                </div>
              </div>
              <div class="flex items-center">
                <img src="/icons/flag-grey.svg" alt="收藏" class="w-4 h-4 lg:w-5 lg:h-5 text-gray-300 hover:text-yellow-500 cursor-pointer">
              </div>
            </div>
        </div>

        <!-- 分页控件 -->
        <div class="mt-6 lg:mt-8 flex justify-center">
          <nav class="flex items-center space-x-1">
            <a href="#" class="px-2 py-1 rounded-md border border-gray-300 text-gray-600 hover:bg-gray-50 text-xs lg:text-sm">上一页</a>
            <a href="#" class="px-2 py-1 rounded-md bg-blue-50 text-blue-600 border border-blue-200 text-xs lg:text-sm">1</a>
            <a href="#" class="px-2 py-1 rounded-md border border-gray-300 text-gray-600 hover:bg-gray-50 text-xs lg:text-sm">2</a>
            <a href="#" class="px-2 py-1 rounded-md border border-gray-300 text-gray-600 hover:bg-gray-50 text-xs lg:text-sm">3</a>
            <a href="#" class="px-2 py-1 rounded-md border border-gray-300 text-gray-600 hover:bg-gray-50 text-xs lg:text-sm">4</a>
            <span class="px-2 py-1 text-xs lg:text-sm">...</span>
            <a href="#" class="px-2 py-1 rounded-md border border-gray-300 text-gray-600 hover:bg-gray-50 text-xs lg:text-sm">8</a>
            <a href="#" class="px-2 py-1 rounded-md border border-gray-300 text-gray-600 hover:bg-gray-50 text-xs lg:text-sm">下一页</a>
          </nav>
        </div>

        <!-- 底部版权信息 -->
        <div class="mt-8 lg:mt-12 text-center text-xs lg:text-sm text-gray-500">
          <p>© 2024 Lin's Tech Blog</p>
          <p class="mt-1 lg:mt-2">浙ICP备024000000。</p>
        </div>
      </div>

      <!-- 右侧边栏 - 移动端隐藏 -->
      <div class="hidden lg:block lg:w-1/5">
        <!-- 技术栈 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6 mb-5">
          <h3 class="text-base font-semibold text-gray-900 mb-4">技术栈</h3>
          <div class="flex flex-wrap gap-2">
            <span class="bg-gray-50 text-gray-600 px-3 py-1.5 rounded-lg text-xs">TypeScript</span>
            <span class="bg-gray-50 text-gray-600 px-3 py-1.5 rounded-lg text-xs">JavaScript</span>
            <span class="bg-gray-50 text-gray-600 px-3 py-1.5 rounded-lg text-xs">Python</span>
            <span class="bg-gray-50 text-gray-600 px-3 py-1.5 rounded-lg text-xs">React</span>
            <span class="bg-gray-50 text-gray-600 px-3 py-1.5 rounded-lg text-xs">Next.js</span>
            <span class="bg-gray-50 text-gray-600 px-3 py-1.5 rounded-lg text-xs">Node.js</span>
            <span class="bg-gray-50 text-gray-600 px-3 py-1.5 rounded-lg text-xs">LangChain</span>
            <span class="bg-gray-50 text-gray-600 px-3 py-1.5 rounded-lg text-xs">FastAPI</span>
            <span class="bg-gray-50 text-gray-600 px-3 py-1.5 rounded-lg text-xs">ChatGLM</span>
            <span class="bg-gray-50 text-gray-600 px-3 py-1.5 rounded-lg text-xs">Tailwind CSS</span>
            <span class="bg-gray-50 text-gray-600 px-3 py-1.5 rounded-lg text-xs">PostgreSQL</span>
            <span class="bg-gray-50 text-gray-600 px-3 py-1.5 rounded-lg text-xs">Docker</span>
            <span class="bg-gray-50 text-gray-600 px-3 py-1.5 rounded-lg text-xs">Git</span>
          </div>
        </div>

        <!-- 项目分类 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6 mb-5">
          <h3 class="text-base font-semibold text-gray-900 mb-4">文章分类</h3>
          <ul class="space-y-3">
            <li class="flex items-center">
              <span class="w-5 h-5 rounded-full bg-blue-500 flex items-center justify-center flex-shrink-0 mr-3">
                <span class="w-2 h-2 rounded-full bg-white"></span>
              </span>
              <span class="flex-1 text-gray-600">全部</span>
              <span class="text-gray-400 text-sm">44</span>
            </li>
            <li class="flex items-center">
              <span class="w-5 h-5 rounded-full bg-gray-100 flex items-center justify-center flex-shrink-0 mr-3">
                <span class="w-2 h-2 rounded-full bg-gray-400"></span>
              </span>
              <span class="flex-1 text-gray-600">AI应用</span>
              <span class="text-gray-400 text-sm">14</span>
            </li>
            <li class="flex items-center">
              <span class="w-5 h-5 rounded-full bg-gray-100 flex items-center justify-center flex-shrink-0 mr-3">
                <span class="w-2 h-2 rounded-full bg-gray-400"></span>
              </span>
              <span class="flex-1 text-gray-600">工具</span>
              <span class="text-gray-400 text-sm">10</span>
            </li>
            <li class="flex items-center">
              <span class="w-5 h-5 rounded-full bg-gray-100 flex items-center justify-center flex-shrink-0 mr-3">
                <span class="w-2 h-2 rounded-full bg-gray-400"></span>
              </span>
              <span class="flex-1 text-gray-600">前端</span>
              <span class="text-gray-400 text-sm">8</span>
            </li>
            <li class="flex items-center">
              <span class="w-5 h-5 rounded-full bg-gray-100 flex items-center justify-center flex-shrink-0 mr-3">
                <span class="w-2 h-2 rounded-full bg-gray-400"></span>
              </span>
              <span class="flex-1 text-gray-600">后端</span>
              <span class="text-gray-400 text-sm">6</span>
            </li>
            <li class="flex items-center">
              <span class="w-5 h-5 rounded-full bg-gray-100 flex items-center justify-center flex-shrink-0 mr-3">
                <span class="w-2 h-2 rounded-full bg-gray-400"></span>
              </span>
              <span class="flex-1 text-gray-600">其他</span>
              <span class="text-gray-400 text-sm">6</span>
            </li>
          </ul>
        </div>

        <!-- 热门项目 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6 mb-5">
          <h3 class="text-base font-semibold text-gray-900 mb-4">热门项目</h3>
          <ul class="space-y-3">
            <li class="flex items-start">
              <span class="w-2 h-2 rounded-full bg-blue-500 mt-2 mr-3"></span>
              <div class="flex-1">
                <a href="#" class="text-gray-700 hover:text-blue-600 text-sm">深入理解 Agent：从原理到实践</a>
                <p class="text-gray-400 text-xs mt-1">阅读 1.2k</p>
              </div>
            </li>
            <li class="flex items-start">
              <span class="w-2 h-2 rounded-full bg-blue-500 mt-2 mr-3"></span>
              <div class="flex-1">
                <a href="#" class="text-gray-700 hover:text-blue-600 text-sm">ChatFlow - 智能对话工作流平台</a>
                <p class="text-gray-400 text-xs mt-1">阅读 2.3k</p>
              </div>
            </li>
            <li class="flex items-start">
              <span class="w-2 h-2 rounded-full bg-blue-500 mt-2 mr-3"></span>
              <div class="flex-1">
                <a href="#" class="text-gray-700 hover:text-blue-600 text-sm">LLM Knowledge Hub</a>
                <p class="text-gray-400 text-xs mt-1">阅读 1.6k</p>
              </div>
            </li>
            <li class="flex items-start">
              <span class="w-2 h-2 rounded-full bg-gray-300 mt-2 mr-3"></span>
              <div class="flex-1">
                <a href="#" class="text-gray-700 hover:text-blue-600 text-sm">React 19 新特性详解与实践</a>
                <p class="text-gray-400 text-xs mt-1">阅读 899</p>
              </div>
            </li>
            <li class="flex items-start">
              <span class="w-2 h-2 rounded-full bg-gray-300 mt-2 mr-3"></span>
              <div class="flex-1">
                <a href="#" class="text-gray-700 hover:text-blue-600 text-sm">AI Prompt 工具集</a>
                <p class="text-gray-400 text-xs mt-1">阅读 589</p>
              </div>
            </li>
          </ul>
        </div>

        <!-- 我在做什么 -->
         <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">我在做什么</h3>
            <p class="text-gray-500 text-sm leading-relaxed mb-6">
              探索 Agent、LLM 与前端工程化的边界，<br>
              构建更智能、更高效的开发体验。            </p>
            <div class="relative">
              <img src="/images/hero-3d.png" alt="AI 3D Illustration" class="w-full h-auto object-contain">
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

const router = useRouter()

const goToArticleDetail = () => {
  router.push('/article/1')
}
</script>

<style scoped>
.page-container {
  background: #ffffff;
  padding: 1.75rem;
}
</style>