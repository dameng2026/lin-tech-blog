<template>
  <div class="page-container p-3 lg:p-[1.75rem] bg-[#fefefe]">
    <div class="min-h-screen">
      <div class="flex flex-col lg:flex-row gap-4 lg:gap-8">
        <!-- 中间主内容区 -->
        <div class="lg:flex-1">
          <!-- 顶部区域 -->
          <div class="bg-gradient-to-b from-[#f5f9fe] to-[#f4f7fe] rounded-2xl shadow-sm px-4 lg:px-16 py-6 lg:py-8 mb-4 lg:mb-6">
            <div class="flex flex-col lg:flex-row gap-4 lg:gap-8 items-center">
              <div class="flex-1 text-center lg:text-left">
                <h1 class="text-xl lg:text-[2.25rem] font-bold text-gray-900 mb-2 lg:mb-4 tracking-wider">友链</h1>
              <p class="text-gray-600 text-sm lg:text-base mb-2 lg:mb-4 tracking-wide">与优秀的人同行，让技术与思想在交流中共同成长</p>
              <p class="text-gray-500 text-xs lg:text-sm mb-4 lg:mb-10 tracking-wide">欢迎技术博客、开源项目、独立开发者等优质站点交换友链</p>
              <div class="flex gap-3 lg:gap-6 justify-center lg:justify-start">
                <button @click="openApplyModal" class="px-4 lg:px-9 py-2.5 lg:py-4 bg-blue-600 text-white rounded-lg text-xs lg:text-sm font-medium hover:bg-blue-700 transition-colors flex items-center gap-2 lg:gap-3">
                  <span>申请友链</span>
                  <img src="/icons/aircraft-while.svg" alt="plane" class="w-3 h-3 lg:w-4 lg:h-4">
                </button>
                <button @click="openInfoModal" class="px-4 lg:px-9 py-2.5 lg:py-4 bg-gray-100 text-gray-700 rounded-lg text-xs lg:text-sm hover:bg-gray-200 transition-colors flex items-center gap-2 lg:gap-3">
                  <span>友链说明</span>
                  <img src="/icons/manual.svg" alt="file" class="w-3 h-3 lg:w-4 lg:h-4">
                </button>
              </div>
            </div>
            <div class="relative w-32 h-32 lg:w-81 lg:h-80 mr-0 lg:mr-8 mt-4 lg:mt-0">
              <img src="/images/Blogroll-3d.png" alt="Links 3D Illustration" class="w-full h-full object-contain">
            </div>
          </div>
        </div>

        <!-- 筛选和搜索-->
        <div class="mb-4 lg:mb-6">
          <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-3 lg:gap-4">
            <!-- 分类标签 -->
            <div class="flex flex-wrap gap-2 lg:gap-4">
              <button class="px-3 lg:px-4 py-1.5 lg:py-2 text-blue-600 text-xs lg:text-sm font-medium border-b-2 border-blue-600">
                全部友链 <span class="text-blue-600 bg-[#eaf1fe] px-2 lg:px-3 py-0.5 rounded-full text-xs font-medium">28</span>
              </button>
              <button class="px-3 lg:px-4 py-1.5 lg:py-2 text-gray-600 text-xs lg:text-sm hover:text-gray-900 hover:border-b-2 hover:border-gray-200 transition-colors">
                技术博客 <span class="text-gray-500 bg-[#f3f4f6] px-2 lg:px-3 py-0.5 rounded-full text-xs font-medium">18</span>
              </button>
              <button class="px-3 lg:px-4 py-1.5 lg:py-2 text-gray-600 text-xs lg:text-sm hover:text-gray-900 hover:border-b-2 hover:border-gray-200 transition-colors">
                开源项目<span class="text-gray-500 bg-[#f3f4f6] px-2 lg:px-3 py-0.5 rounded-full text-xs font-medium">6</span>
              </button>
              <button class="px-3 lg:px-4 py-1.5 lg:py-2 text-gray-600 text-xs lg:text-sm hover:text-gray-900 hover:border-b-2 hover:border-gray-200 transition-colors">
                独立开发者 <span class="text-gray-500 bg-[#f3f4f6] px-2 lg:px-3 py-0.5 rounded-full text-xs font-medium">4</span>
              </button>
            </div>

            <!-- 搜索和排序-->
            <div class="flex items-center gap-2 lg:gap-3">
              <div class="relative flex-1 lg:w-64">
                <input type="text" placeholder="搜索友链" class="w-full pl-8 lg:pl-10 pr-3 lg:pr-4 py-1.5 lg:py-2 bg-gray-50 border border-gray-200 rounded-lg text-xs lg:text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                <svg class="w-3 h-3 lg:w-4 lg:h-4 text-gray-400 absolute left-2.5 lg:left-3 top-1/2 -translate-y-1/2" fill="currentColor" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
              </div>
              <button class="px-3 lg:px-4 py-1.5 lg:py-2 bg-gray-50 text-gray-600 rounded-lg text-xs lg:text-sm hover:bg-gray-100 flex items-center gap-1.5 lg:gap-2 border border-gray-200">
                <span>排序: A-Z</span>
                <svg class="w-3 h-3 lg:w-4 lg:h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- 友链列表 -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 lg:gap-4">
          <!-- 友链卡片 1 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-3 lg:p-6 hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-shadow h-auto lg:h-[160px]">
            <div class="flex flex-col h-full">
              <div class="flex items-start gap-2 lg:gap-3 h-full">
                <div class="w-10 h-10 lg:w-12 lg:h-12 rounded-full bg-gray-900 flex items-center justify-center flex-shrink-0">
                  <span class="text-white font-bold text-sm lg:text-base">H</span>
                </div>
                <div class="flex-1 h-full flex flex-col">
                  <h3 class="font-semibold text-gray-900 hover:text-blue-600 cursor-pointer text-xs lg:text-sm">Hux Blog</h3>
                  <p class="text-xs text-gray-500 mt-2 lg:mt-3 line-clamp-2 lg:line-clamp-3">专注分享 Web 开发、编程技术与个人成长。</p>
                  <span class="self-start px-1.5 lg:px-2 py-0.5 bg-blue-100 text-blue-600 rounded text-xs mt-auto">技术博客</span>
                </div>
                <img src="/icons/redirect.svg" alt="link" class="w-3 h-3 lg:w-4 lg:h-4 text-gray-300 hover:text-blue-600 flex-shrink-0 mt-0.5 lg:mt-1">
              </div>
            </div>
          </div>

          <!-- 友链卡片 2 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-3 lg:p-6 hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-shadow h-auto lg:h-[160px]">
            <div class="flex flex-col h-full">
              <div class="flex items-start gap-2 lg:gap-3 h-full">
                <div class="w-10 h-10 lg:w-12 lg:h-12 rounded-full bg-gray-900 flex items-center justify-center flex-shrink-0">
                  <span class="text-white font-bold text-sm lg:text-base">A</span>
                </div>
                <div class="flex-1 h-full flex flex-col">
                  <h3 class="font-semibold text-gray-900 hover:text-blue-600 cursor-pointer text-xs lg:text-sm">阮一峰的网络日志</h3>
                  <p class="text-xs text-gray-500 mt-2 lg:mt-3 line-clamp-2 lg:line-clamp-3">关注网络应用、编程技术和开源软件。</p>
                  <span class="self-start px-1.5 lg:px-2 py-0.5 bg-blue-100 text-blue-600 rounded text-xs mt-auto">技术博客</span>
                </div>
                <img src="/icons/redirect.svg" alt="link" class="w-3 h-3 lg:w-4 lg:h-4 text-gray-300 hover:text-blue-600 flex-shrink-0 mt-0.5 lg:mt-1">
              </div>
            </div>
          </div>

          <!-- 友链卡片 3 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-3 lg:p-6 hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-shadow h-auto lg:h-[160px]">
            <div class="flex flex-col h-full">
              <div class="flex items-start gap-2 lg:gap-3 h-full">
                <div class="w-10 h-10 lg:w-12 lg:h-12 rounded-full overflow-hidden flex-shrink-0">
                  <img src="https://neeko-copilot.bytedance.net/api/text_to_image?prompt=professional%20asian%20male%20developer%20avatar%2C%20portrait%2C%20friendly%2C%20clean%20background&image_size=square" alt="avatar" class="w-full h-full object-cover">
                </div>
                <div class="flex-1 h-full flex flex-col">
                  <h3 class="font-semibold text-gray-900 hover:text-blue-600 cursor-pointer text-xs lg:text-sm">张洪Heo</h3>
                  <p class="text-xs text-gray-500 mt-2 lg:mt-3 line-clamp-2 lg:line-clamp-3">分享 PHP、Laravel、Vue 等开发经验。</p>
                  <span class="self-start px-1.5 lg:px-2 py-0.5 bg-blue-100 text-blue-600 rounded text-xs mt-auto">技术博客</span>
                </div>
                <img src="/icons/redirect.svg" alt="link" class="w-3 h-3 lg:w-4 lg:h-4 text-gray-300 hover:text-blue-600 flex-shrink-0 mt-0.5 lg:mt-1">
              </div>
            </div>
          </div>

          <!-- 友链卡片 4 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-3 lg:p-6 hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-shadow h-auto lg:h-[160px]">
            <div class="flex flex-col h-full">
              <div class="flex items-start gap-2 lg:gap-3 h-full">
                <div class="w-10 h-10 lg:w-12 lg:h-12 rounded-full bg-gradient-to-br from-pink-500 via-purple-500 to-cyan-500 flex items-center justify-center flex-shrink-0">
                  <span class="text-white font-bold text-sm lg:text-base">F</span>
                </div>
                <div class="flex-1 h-full flex flex-col">
                  <h3 class="font-semibold text-gray-900 hover:text-blue-600 cursor-pointer text-xs lg:text-sm">Frontier</h3>
                  <p class="text-xs text-gray-500 mt-2 lg:mt-3 line-clamp-2 lg:line-clamp-3">一款开源的全栈管理后台框架。</p>
                  <span class="self-start px-1.5 lg:px-2 py-0.5 bg-green-100 text-green-600 rounded text-xs mt-auto">开源项目</span>
                </div>
                <img src="/icons/redirect.svg" alt="link" class="w-3 h-3 lg:w-4 lg:h-4 text-gray-300 hover:text-blue-600 flex-shrink-0 mt-0.5 lg:mt-1">
              </div>
            </div>
          </div>

          <!-- 友链卡片 5 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-3 lg:p-6 hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-shadow h-auto lg:h-[160px]">
            <div class="flex flex-col h-full">
              <div class="flex items-start gap-2 lg:gap-3 h-full">
                <div class="w-10 h-10 lg:w-12 lg:h-12 rounded-full bg-green-600 flex items-center justify-center flex-shrink-0">
                  <span class="text-white font-bold text-sm lg:text-base">V</span>
                </div>
                <div class="flex-1 h-full flex flex-col">
                  <h3 class="font-semibold text-gray-900 hover:text-blue-600 cursor-pointer text-xs lg:text-sm">Vue.js</h3>
                  <p class="text-xs text-gray-500 mt-2 lg:mt-3 line-clamp-2 lg:line-clamp-3">渐进式 JavaScript 框架。</p>
                  <span class="self-start px-1.5 lg:px-2 py-0.5 bg-green-100 text-green-600 rounded text-xs mt-auto">开源项目</span>
                </div>
                <img src="/icons/jump.svg" alt="link" class="w-3 h-3 lg:w-4 lg:h-4 text-gray-300 hover:text-blue-600 flex-shrink-0 mt-0.5 lg:mt-1">
              </div>
            </div>
          </div>

          <!-- 友链卡片 6 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-3 lg:p-6 hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-shadow h-auto lg:h-[160px]">
            <div class="flex flex-col h-full">
              <div class="flex items-start gap-2 lg:gap-3 h-full">
                <div class="w-10 h-10 lg:w-12 lg:h-12 rounded-full bg-teal-500 flex items-center justify-center flex-shrink-0">
                  <svg class="w-5 h-5 lg:w-6 lg:h-6 text-white" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 00-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.74-.55 2.92-1.27 4.86-2.11 5.83-2.51 2.78-1.16 3.35-1.36 3.73-1.36.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .38z"/>
                  </svg>
                </div>
                <div class="flex-1 h-full flex flex-col">
                  <h3 class="font-semibold text-gray-900 hover:text-blue-600 cursor-pointer text-xs lg:text-sm">Tailwind CSS</h3>
                  <p class="text-xs text-gray-500 mt-2 lg:mt-3 line-clamp-2 lg:line-clamp-3">一个实用优先的 CSS 框架。</p>
                  <span class="self-start px-1.5 lg:px-2 py-0.5 bg-green-100 text-green-600 rounded text-xs mt-auto">开源项目</span>
                </div>
                <img src="/icons/jump.svg" alt="link" class="w-3 h-3 lg:w-4 lg:h-4 text-gray-300 hover:text-blue-600 flex-shrink-0 mt-0.5 lg:mt-1">
              </div>
            </div>
          </div>

          <!-- 友链卡片 7 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-3 lg:p-6 hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-shadow h-auto lg:h-[160px]">
            <div class="flex flex-col h-full">
              <div class="flex items-start gap-2 lg:gap-3 h-full">
                <div class="w-10 h-10 lg:w-12 lg:h-12 rounded-lg bg-green-600 flex items-center justify-center flex-shrink-0">
                  <svg class="w-5 h-5 lg:w-6 lg:h-6 text-white" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
                  </svg>
                </div>
                <div class="flex-1 h-full flex flex-col">
                  <h3 class="font-semibold text-gray-900 hover:text-blue-600 cursor-pointer text-xs lg:text-sm">Node.js</h3>
                  <p class="text-xs text-gray-500 mt-2 lg:mt-3 line-clamp-2 lg:line-clamp-3">基于 Chrome V8 引擎的 JavaScript 运行时。</p>
                  <span class="self-start px-1.5 lg:px-2 py-0.5 bg-green-100 text-green-600 rounded text-xs mt-auto">开源项目</span>
                </div>
                <img src="/icons/jump.svg" alt="link" class="w-3 h-3 lg:w-4 lg:h-4 text-gray-300 hover:text-blue-600 flex-shrink-0 mt-0.5 lg:mt-1">
              </div>
            </div>
          </div>

          <!-- 友链卡片 8 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-3 lg:p-6 hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-shadow h-auto lg:h-[160px]">
            <div class="flex flex-col h-full">
              <div class="flex items-start gap-2 lg:gap-3 h-full">
                <div class="w-10 h-10 lg:w-12 lg:h-12 rounded-full overflow-hidden flex-shrink-0">
                  <img src="https://neeko-copilot.bytedance.net/api/text_to_image?prompt=silhouette%20of%20person%20looking%20at%20sunset%2C%20minimalist%2C%20peaceful&image_size=square" alt="avatar" class="w-full h-full object-cover">
                </div>
                <div class="flex-1 h-full flex flex-col">
                  <h3 class="font-semibold text-gray-900 hover:text-blue-600 cursor-pointer text-xs lg:text-sm">独立开发者 - 小林</h3>
                  <p class="text-xs text-gray-500 mt-2 lg:mt-3 line-clamp-2 lg:line-clamp-3">独立开发者，专注于效率工具与产品设计。</p>
                  <span class="self-start px-1.5 lg:px-2 py-0.5 bg-purple-100 text-purple-600 rounded text-xs mt-auto">独立开发</span>
                </div>
                <img src="/icons/jump.svg" alt="link" class="w-3 h-3 lg:w-4 lg:h-4 text-gray-300 hover:text-blue-600 flex-shrink-0 mt-0.5 lg:mt-1">
              </div>
            </div>
          </div>

          <!-- 友链卡片 9 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-3 lg:p-6 hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-shadow h-auto lg:h-[160px]">
            <div class="flex flex-col h-full">
              <div class="flex items-start gap-2 lg:gap-3 h-full">
                <div class="w-10 h-10 lg:w-12 lg:h-12 rounded-full overflow-hidden flex-shrink-0">
                  <img src="https://neeko-copilot.bytedance.net/api/text_to_image?prompt=professional%20asian%20male%20avatar%2C%20clean%20background%2C%20modern%20style&image_size=square" alt="avatar" class="w-full h-full object-cover">
                </div>
                <div class="flex-1 h-full flex flex-col">
                  <h3 class="font-semibold text-gray-900 hover:text-blue-600 cursor-pointer text-xs lg:text-sm">独立开发者 - Kai</h3>
                  <p class="text-xs text-gray-500 mt-2 lg:mt-3 line-clamp-2 lg:line-clamp-3">专注 Mac 工具与生产力应用开发。</p>
                  <span class="self-start px-1.5 lg:px-2 py-0.5 bg-purple-100 text-purple-600 rounded text-xs mt-auto">独立开发</span>
                </div>
                <img src="/icons/jump.svg" alt="link" class="w-3 h-3 lg:w-4 lg:h-4 text-gray-300 hover:text-blue-600 flex-shrink-0 mt-0.5 lg:mt-1">
              </div>
            </div>
          </div>

          <!-- 友链卡片 10 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-3 lg:p-6 hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-shadow h-auto lg:h-[160px]">
            <div class="flex flex-col h-full">
              <div class="flex items-start gap-2 lg:gap-3 h-full">
                <div class="w-10 h-10 lg:w-12 lg:h-12 rounded-full overflow-hidden flex-shrink-0">
                  <img src="https://neeko-copilot.bytedance.net/api/text_to_image?prompt=cute%20cat%20avatar%2C%20cartoon%20style%2C%20friendly&image_size=square" alt="avatar" class="w-full h-full object-cover">
                </div>
                <div class="flex-1 h-full flex flex-col">
                  <h3 class="font-semibold text-gray-900 hover:text-blue-600 cursor-pointer text-xs lg:text-sm">喵喵日志</h3>
                  <p class="text-xs text-gray-500 mt-2 lg:mt-3 line-clamp-2 lg:line-clamp-3">记录生活，分享技术，保持热爱。</p>
                  <span class="self-start px-1.5 lg:px-2 py-0.5 bg-blue-100 text-blue-600 rounded text-xs mt-auto">技术博客</span>
                </div>
                <img src="/icons/jump.svg" alt="link" class="w-3 h-3 lg:w-4 lg:h-4 text-gray-300 hover:text-blue-600 flex-shrink-0 mt-0.5 lg:mt-1">
              </div>
            </div>
          </div>

          <!-- 友链卡片 11 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-3 lg:p-6 hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-shadow h-auto lg:h-[160px]">
            <div class="flex flex-col h-full">
              <div class="flex items-start gap-2 lg:gap-3 h-full">
                <div class="w-10 h-10 lg:w-12 lg:h-12 rounded-full bg-yellow-400 flex items-center justify-center flex-shrink-0">
                  <span class="text-gray-900 font-bold text-xs lg:text-sm">JS</span>
                </div>
                <div class="flex-1 h-full flex flex-col">
                  <h3 class="font-semibold text-gray-900 hover:text-blue-600 cursor-pointer text-xs lg:text-sm">JavaScript 中文</h3>
                  <p class="text-xs text-gray-500 mt-2 lg:mt-3 line-clamp-2 lg:line-clamp-3">致力于推动 JavaScript 技术。</p>
                  <span class="self-start px-1.5 lg:px-2 py-0.5 bg-blue-100 text-blue-600 rounded text-xs mt-auto">技术博客</span>
                </div>
                <img src="/icons/jump.svg" alt="link" class="w-3 h-3 lg:w-4 lg:h-4 text-gray-300 hover:text-blue-600 flex-shrink-0 mt-0.5 lg:mt-1">
              </div>
            </div>
          </div>

          <!-- 友链卡片 12 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-3 lg:p-6 hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-shadow h-auto lg:h-[160px]">
            <div class="flex flex-col h-full">
              <div class="flex items-start gap-2 lg:gap-3 h-full">
                <div class="w-10 h-10 lg:w-12 lg:h-12 rounded-full bg-gray-100 flex items-center justify-center flex-shrink-0">
                  <span class="text-gray-800 font-bold text-sm lg:text-base">A</span>
                </div>
                <div class="flex-1 h-full flex flex-col">
                  <h3 class="font-semibold text-gray-900 hover:text-blue-600 cursor-pointer text-xs lg:text-sm">Ant Design</h3>
                  <p class="text-xs text-gray-500 mt-2 lg:mt-3 line-clamp-2 lg:line-clamp-3">企业级产品设计体系。</p>
                  <span class="self-start px-1.5 lg:px-2 py-0.5 bg-green-100 text-green-600 rounded text-xs mt-auto">开源项目</span>
                </div>
                <img src="/icons/jump.svg" alt="link" class="w-3 h-3 lg:w-4 lg:h-4 text-gray-300 hover:text-blue-600 flex-shrink-0 mt-0.5 lg:mt-1">
              </div>
            </div>
          </div>
        </div>

        <!-- 分页控件 -->
        <div class="mt-4 lg:mt-8 bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-3 lg:p-6">
          <div class="flex flex-col lg:flex-row justify-between items-center gap-2 lg:gap-0">
            <div class="flex-1 flex justify-center">
              <nav class="flex items-center space-x-1">
                <button class="w-7 h-7 lg:w-8 lg:h-8 rounded-md border border-gray-200 text-gray-400 hover:bg-gray-50 hover:text-gray-600 disabled:opacity-50 flex items-center justify-center">
                  <svg class="w-3 h-3 lg:w-4 lg:h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
                  </svg>
                </button>
                <button class="w-7 h-7 lg:w-8 lg:h-8 rounded-md bg-blue-500 text-white border border-blue-500 text-xs lg:text-sm">1</button>
                <button class="w-7 h-7 lg:w-8 lg:h-8 rounded-md border border-gray-200 text-gray-600 hover:bg-gray-50 text-xs lg:text-sm">2</button>
                <button class="w-7 h-7 lg:w-8 lg:h-8 rounded-md border border-gray-200 text-gray-600 hover:bg-gray-50 text-xs lg:text-sm">3</button>
                <button class="w-7 h-7 lg:w-8 lg:h-8 rounded-md border border-gray-200 text-gray-400 hover:bg-gray-50 hover:text-gray-600 flex items-center justify-center">
                  <svg class="w-3 h-3 lg:w-4 lg:h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                  </svg>
                </button>
              </nav>
            </div>
            <span class="text-xs lg:text-sm text-gray-500">28 条友链</span>
          </div>
        </div>

        <!-- 底部版权信息 -->
        <div class="mt-6 lg:mt-12 text-center text-xs lg:text-sm text-gray-500">
          <p>© 2024 Lin's Tech Blog</p>
          <p class="mt-1 lg:mt-2">浙ICP?024000000。</p>
        </div>
      </div>

      <!-- 右侧边栏 -->
      <div class="hidden lg:block lg:w-1/5">
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6 flex flex-col">
          <!-- 第一块：头像和个人信息-->
          <div class="flex flex-col items-center mb-6">
            <div class="w-[5rem] h-[5rem] rounded-full overflow-hidden flex-shrink-0 mb-3">
              <img src="/images/avatar.png" alt="Lin" class="w-full h-full object-cover">
            </div>
            <h3 class="font-bold text-xl text-gray-900 mb-1">Lin</h3>
            <p class="text-sm text-gray-600">全栈开发 & AI 应用探索。</p>
          </div>

          <!-- 第二块：个人信息-->
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
              <img src="/icons/github-black.svg" alt="GitHub" class="w-4 h-4 mr-2">
              github.com/linxxx
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
        </div>

        <!-- 友链统计 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6 flex flex-col">
          <h4 class="font-semibold text-gray-900 mb-4">友链统计</h4>
          <div class="grid grid-cols-4 gap-2">
            <!-- 总友链数 -->
            <div class="text-center flex flex-col items-center">
              <div class="w-12 h-12 rounded-full bg-[#e9f1fd] flex items-center justify-center mb-2">
                <img src="/icons/Blogroll-blue.svg" alt="links" class="w-6 h-6">
              </div>
              <span class="text-xs text-gray-500 mb-1">总友链数</span>
              <span class="text-lg font-bold text-gray-900">26</span>
            </div>
            <!-- 技术博客-->
            <div class="text-center flex flex-col items-center">
              <div class="w-12 h-12 rounded-full bg-[#fdf5e1] flex items-center justify-center mb-2">
                <img src="/icons/blog.svg" alt="blog" class="w-6 h-6">
              </div>
              <span class="text-xs text-gray-500 mb-1">我的博客</span>
              <span class="text-lg font-bold text-gray-900">18</span>
            </div>
            <!-- 开源项目-->
            <div class="text-center flex flex-col items-center">
              <div class="w-12 h-12 rounded-full bg-[#eff8f4] flex items-center justify-center mb-2">
                <img src="/icons/opensource.svg" alt="opensource" class="w-6 h-6">
              </div>
              <span class="text-xs text-gray-500 mb-1">开源项目</span>
              <span class="text-lg font-bold text-gray-900">6</span>
            </div>
            <!-- 独立开发者-->
            <div class="text-center flex flex-col items-center">
              <div class="w-12 h-12 rounded-full bg-[#fef9ec] flex items-center justify-center mb-2">
                <img src="/icons/developer.svg" alt="independent" class="w-6 h-6">
              </div>
              <span class="text-xs text-gray-500 mb-1">独立开发者</span>
              <span class="text-lg font-bold text-gray-900">4</span>
            </div>
          </div>
        </div>

        <!-- 申请友链 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6 mt-5">
          <h4 class="font-semibold text-gray-900 mb-3">申请友链</h4>
          <p class="text-xs text-gray-500 mb-4">
            如果你希望与我交换友链，请先查看友链要求。如果符合，请通过表单提交友链信息</p>
          <button @click="openApplyModal" class="w-full py-3 border border-gray-200 text-gray-700 rounded-xl text-sm hover:bg-gray-50 transition-colors flex items-center justify-center gap-2">
            <img src="/icons/aircraft-black.svg" class="w-5 h-5" />
            申请友链
          </button>
        </div>

        <!-- 友链要求 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6 mt-5">
          <h4 class="font-semibold text-gray-900 mb-3">友链要求</h4>
          <ul class="space-y-2 text-xs text-gray-500">
            <li class="flex items-start">
              <span class="w-1.5 h-1.5 rounded-full bg-green-500 mt-1.5 mr-2"></span>
              <span>内容积极向上，专注技术分享</span>
            </li>
            <li class="flex items-start">
              <span class="w-1.5 h-1.5 rounded-full bg-green-500 mt-1.5 mr-2"></span>
              <span>网站设计简洁美观，访问体验良好</span>
            </li>
            <li class="flex items-start">
              <span class="w-1.5 h-1.5 rounded-full bg-green-500 mt-1.5 mr-2"></span>
              <span>稳定运营，无违法违规内容</span>
            </li>
            <li class="flex items-start">
              <span class="w-1.5 h-1.5 rounded-full bg-green-500 mt-1.5 mr-2"></span>
              <span>已在网站底部或专门页面添加本站链</span>
            </li>
          </ul>
          <button @click="openInfoModal" class="w-full mt-4 py-3 border border-gray-200 text-gray-700 rounded-xl text-sm hover:bg-gray-50 transition-colors flex items-center justify-center gap-2">
            <img src="/icons/file.svg" class="w-5 h-5" />
            查看友链说明
          </button>
        </div>
      </div>

        <!-- 申请友链弹窗 -->
        <div v-if="showApplyModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4" @click.self="showApplyModal = false">
          <div class="bg-white rounded-2xl shadow-xl w-full max-w-lg max-h-[90vh] overflow-y-auto">
            <div class="flex items-center gap-4 p-6 border-b border-gray-100">
              <div class="w-12 h-12 rounded-full bg-[#e9f1fd] flex items-center justify-center">
                <img src="/icons/redirect.svg" alt="plane" class="w-6 h-6">
              </div>
              <div class="flex-1">
                <h3 class="text-lg font-bold text-gray-900">申请友链</h3>
                <p class="text-sm text-gray-500">感谢您对本站的关注与支持！请填写以下信息，我们会在审核后尽快与您联系。</p>
              </div>
              <button @click="showApplyModal = false" class="w-8 h-8 rounded-full hover:bg-gray-100 flex items-center justify-center">
                <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                </svg>
              </button>
            </div>
            
            <div class="p-6 space-y-5">
              <!-- 网站信息 -->
              <div>
                <h4 class="text-sm font-semibold text-gray-700 mb-3">网站信息</h4>
                
                <div class="space-y-4">
                  <div>
                    <label class="block text-xs text-gray-500 mb-1">网站名称 <span class="text-red-500">*</span></label>
                    <input type="text" placeholder="请输入网站名称" class="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                  </div>
                  
                  <div>
                    <label class="block text-xs text-gray-500 mb-1">网站地址 <span class="text-red-500">*</span></label>
                    <input type="text" placeholder="请输入完整的网站地址（需包含 http/https）" class="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                  </div>
                  
                  <div>
                    <label class="block text-xs text-gray-500 mb-1">网站描述 <span class="text-red-500">*</span></label>
                    <textarea placeholder="简要描述您的网站内容、定位与特色?0-100字）" rows="2" class="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"></textarea>
                    <span class="text-xs text-gray-400 float-right">0 / 100</span>
                  </div>
                  
                  <div class="grid grid-cols-2 gap-4">
                    <div>
                      <label class="block text-xs text-gray-500 mb-1">网站图标</label>
                      <input type="text" placeholder="请输入网站图标地址" class="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                    </div>
                    <div>
                      <label class="block text-xs text-gray-500 mb-1">网站分类</label>
                      <select class="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                        <option>请选择网站分类</option>
                        <option>技术博客</option>
                        <option>开源项目</option>
                        <option>独立开发</option>
                      </select>
                    </div>
                  </div>
                  
                  <div>
                    <label class="block text-xs text-gray-500 mb-1">站长昵称 <span class="text-red-500">*</span></label>
                    <input type="text" placeholder="请输入站长昵称" class="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                  </div>
                </div>
              </div>
              
              <!-- 联系方式 -->
              <div>
                <h4 class="text-sm font-semibold text-gray-700 mb-3">联系方式</h4>
                
                <div class="space-y-4">
                  <div>
                    <label class="block text-xs text-gray-500 mb-1">邮箱 <span class="text-red-500">*</span></label>
                    <input type="email" placeholder="请输入您的邮箱地址" class="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                  </div>
                  
                  <div>
                    <label class="block text-xs text-gray-500 mb-1">备注（可选）</label>
                    <textarea placeholder="您想对我们说的话..." rows="2" class="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"></textarea>
                  </div>
                </div>
              </div>
              
              <!-- 同意条款 -->
              <div class="flex items-start gap-2">
                <input type="checkbox" id="agree" class="mt-1 w-4 h-4 text-blue-600 rounded focus:ring-blue-500">
                <label for="agree" class="text-xs text-gray-500">我已阅读并同意 <span class="text-blue-600">《友链交换说明》</span></label>
              </div>
            </div>
            
            <div class="flex gap-3 p-6 border-t border-gray-100">
              <button @click="showApplyModal = false" class="flex-1 py-2.5 bg-gray-100 text-gray-700 rounded-lg text-sm hover:bg-gray-200 transition-colors">
                取消
              </button>
              <button class="flex-1 py-2.5 bg-blue-600 text-white rounded-lg text-sm hover:bg-blue-700 transition-colors">
                提交申请
              </button>
            </div>
          </div>
        </div>

        <!-- 友链说明弹窗 -->
        <div v-if="showInfoModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4" @click.self="showInfoModal = false">
          <div class="bg-white rounded-2xl shadow-xl w-full max-w-lg max-h-[90vh] overflow-y-auto">
            <div class="flex items-center gap-4 p-6 border-b border-gray-100">
              <div class="w-12 h-12 rounded-full bg-blue-100 flex items-center justify-center">
                <img src="/icons/file.svg" alt="file" class="w-6 h-6">
              </div>
              <div class="flex-1">
                <h3 class="text-lg font-bold text-gray-900">友链交换说明</h3>
                <p class="text-sm text-gray-500">请在申请友链前仔细阅读以下说。</p>
              </div>
              <button @click="showInfoModal = false" class="w-8 h-8 rounded-full hover:bg-gray-100 flex items-center justify-center">
                <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                </svg>
              </button>
            </div>
            
            <div class="p-6 space-y-6">
              <!-- 申请条件 -->
              <div>
                <h4 class="text-sm font-semibold text-gray-900 mb-4">申请条件</h4>
                <div class="grid grid-cols-2 gap-3">
                  <div class="bg-[#f0f7ff] rounded-xl p-4 text-center">
                    <div class="w-12 h-12 rounded-full bg-blue-100 flex items-center justify-center mx-auto mb-2">
                      <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
                      </svg>
                    </div>
                    <h5 class="text-xs font-semibold text-gray-700 mb-1">内容合规</h5>
                    <p class="text-xs text-gray-500">网站内容合法合规，无违规信息</p>
                  </div>
                  
                  <div class="bg-[#fffbeb] rounded-xl p-4 text-center">
                    <div class="w-12 h-12 rounded-full bg-green-100 flex items-center justify-center mx-auto mb-2">
                      <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
                      </svg>
                    </div>
                    <h5 class="text-xs font-semibold text-gray-700 mb-1">内容优质</h5>
                    <p class="text-xs text-gray-500">原创内容为主，具有一定质量和价。</p>
                  </div>
                  
                  <div class="bg-[#f0fdf4] rounded-xl p-4 text-center">
                    <div class="w-12 h-12 rounded-full bg-orange-100 flex items-center justify-center mx-auto mb-2">
                      <svg class="w-5 h-5 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
                      </svg>
                    </div>
                    <h5 class="text-xs font-semibold text-gray-700 mb-1">稳定运营</h5>
                    <p class="text-xs text-gray-500">网站稳定更新，且持续稳定更新</p>
                  </div>
                  
                  <div class="bg-[#faf5ff] rounded-xl p-4 text-center">
                    <div class="w-12 h-12 rounded-full bg-purple-100 flex items-center justify-center mx-auto mb-2">
                      <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"></path>
                      </svg>
                    </div>
                    <h5 class="text-xs font-semibold text-gray-700 mb-1">相关性</h5>
                    <p class="text-xs text-gray-500">网站主题与本站内容相关或互补</p>
                  </div>
                </div>
              </div>
              
              <!-- 交换原则 -->
              <div>
                <h4 class="text-sm font-semibold text-gray-900 mb-3">交换原则</h4>
                <ul class="space-y-2">
                  <li class="flex items-start gap-2 text-xs text-gray-500">
                    <svg class="w-4 h-4 text-green-500 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                    </svg>
                    <span>我们会定期检查友链质量，不符合要求的友链可能会被移除</span>
                  </li>
                  <li class="flex items-start gap-2 text-xs text-gray-500">
                    <svg class="w-4 h-4 text-green-500 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                    </svg>
                    <span>友链位置：我们会将您的网站放在友链页面显眼位置</span>
                  </li>
                  <li class="flex items-start gap-2 text-xs text-gray-500">
                    <svg class="w-4 h-4 text-green-500 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                    </svg>
                    <span>互换要求：申请友链即表示同意在贵站添加本站友链</span>
                  </li>
                  <li class="flex items-start gap-2 text-xs text-gray-500">
                    <svg class="w-4 h-4 text-green-500 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                    </svg>
                    <span>审核时间：我们会在3-7个工作日内完成审核并通过邮件通知您</span>
                  </li>
                </ul>
              </div>
              
              <!-- 友链信息 -->
              <div>
                <h4 class="text-sm font-semibold text-gray-900 mb-3">友链信息</h4>
                
                <div class="bg-[#f8fafc] rounded-xl p-4">
                  <div class="flex items-center gap-3 mb-3">
                    <div class="w-10 h-10 rounded-lg bg-blue-600 flex items-center justify-center">
                      <span class="text-white font-bold">L</span>
                    </div>
                    <div>
                      <h5 class="text-sm font-semibold text-gray-900">Lin's Tech Blog</h5>
                      <p class="text-xs text-gray-500">专注 Agent 开发及前端技术，构建智能与体验兼备的产品</p>
                    </div>
                  </div>
                  
                  <div class="grid grid-cols-2 gap-2 text-xs">
                    <div>
                      <span class="text-gray-400">网站地址</span>
                      <span class="text-blue-600">https://linxxx.github.io</span>
                    </div>
                    <div>
                      <span class="text-gray-400">网站描述</span>
                      <span class="text-gray-600">专注 Agent 开发与前端技</span>
                    </div>
                    <div>
                      <span class="text-gray-400">网站图标</span>
                      <span class="text-blue-600">https://linxxx.github.io/favicon.ico</span>
                    </div>
                    <div>
                      <span class="text-gray-400">网站图标</span>
                      <span class="text-blue-600">https://linxxx.github.io/favicon.ico</span>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- 注意事项 -->
              <div>
                <h4 class="text-sm font-semibold text-gray-900 mb-3">注意事项</h4>
                <div class="bg-[#eff6ff] rounded-xl p-4 border border-blue-100">
                  <div class="flex items-start gap-2">
                    <svg class="w-4 h-4 text-blue-500 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                    </svg>
                    <div class="text-xs text-gray-600">
                      <p>请确保在贵站友情链接页添加本站链接，审核时我们会进行人工核查</p>
                      <p class="mt-1">友链仅限技术类、设计类、开源类、开源社区等相关网站，恕不接受非相关网站申请</p>
                      <p class="mt-1">本站保留对友链申请的最终审核权。</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
            <div class="p-6 border-t border-gray-100">
              <button @click="showInfoModal = false" class="w-full py-2.5 bg-gray-100 text-gray-700 rounded-lg text-sm hover:bg-gray-200 transition-colors">
                我已了解，关?              </button>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { usePdfModal } from '../composables/usePdfModal'

const showApplyModal = ref(false)
const showInfoModal = ref(false)
const { openModal } = usePdfModal()

const openApplyModal = () => {
  showApplyModal.value = true
}

const openInfoModal = () => {
  showInfoModal.value = true
}
</script>

<style scoped>
.page-container {
  background: #fffefe;
  padding: 1.75rem;
}

@media (max-width: 768px) {
  .page-container {
    padding: 0.75rem 0.75rem 1rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row {
    gap: 0.75rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mb-4.lg\:mb-6 {
    margin-bottom: 0.8rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 {
    min-width: 0;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-gradient-to-b {
    position: relative;
    padding: 1rem 1rem 1.15rem;
    border-radius: 1rem;
    min-height: 0;
    overflow: hidden;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-gradient-to-b > .flex.flex-col.lg\:flex-row {
    flex-direction: column;
    align-items: flex-start;
    gap: 0;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-gradient-to-b .flex-1.text-center.lg\:text-left {
    width: 100%;
    text-align: center;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-gradient-to-b .flex-1.text-center.lg\:text-left > h1,
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-gradient-to-b .flex-1.text-center.lg\:text-left > p,
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-gradient-to-b .flex-1.text-center.lg\:text-left > div {
    text-align: center;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-gradient-to-b h1 {
    font-size: 1.55rem;
    line-height: 1.2;
    margin-bottom: 0.55rem;
    letter-spacing: 0;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-gradient-to-b > .flex.flex-col.lg\:flex-row > .flex-1.text-center.lg\:text-left > p:nth-of-type(1) {
    font-size: 0.95rem;
    line-height: 1.55;
    margin-bottom: 0.45rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-gradient-to-b > .flex.flex-col.lg\:flex-row > .flex-1.text-center.lg\:text-left > p:nth-of-type(2) {
    font-size: 0.8rem;
    line-height: 1.55;
    margin-bottom: 0.75rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-gradient-to-b p {
    line-height: 1.7;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-gradient-to-b .flex.gap-3.lg\:gap-6 {
    width: 100%;
    flex-direction: row;
    gap: 1rem;
    margin-top: 0.15rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-gradient-to-b .flex.gap-3.lg\:gap-6 button {
    width: calc(50% - 0.5rem);
    justify-content: center;
    padding: 0.85rem 1rem;
    border-radius: 1rem;
    font-size: 0.9rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-gradient-to-b .relative.w-32 {
    width: 100%;
    height: auto;
    margin-right: 0;
    margin-top: 0.2rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-gradient-to-b .relative.w-32 img {
    width: min(100%, 18rem);
    margin: 0 auto;
    display: block;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mb-4.lg\:mb-6 .flex.flex-col.lg\:flex-row.lg\:items-center.lg\:justify-between {
    gap: 0.75rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mb-4.lg\:mb-6 .flex.flex-wrap.gap-2.lg\:gap-4 {
    gap: 0.5rem;
    overflow-x: auto;
    flex-wrap: nowrap;
    padding-bottom: 0.1rem;
    scrollbar-width: none;
    -ms-overflow-style: none;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mb-4.lg\:mb-6 .flex.flex-wrap.gap-2.lg\:gap-4::-webkit-scrollbar {
    display: none;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mb-4.lg\:mb-6 .flex.flex-wrap.gap-2.lg\:gap-4 button {
    white-space: nowrap;
    border-radius: 0.95rem;
    padding-top: 0.6rem;
    padding-bottom: 0.6rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mb-4.lg\:mb-6 .flex.items-center.gap-2.lg\:gap-3 {
    width: 100%;
    gap: 0.5rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mb-4.lg\:mb-6 .relative.flex-1.lg\:w-64 {
    min-width: 0;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .grid.grid-cols-1.md\:grid-cols-2.lg\:grid-cols-3 {
    grid-template-columns: 1fr;
    gap: 0.75rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .grid.grid-cols-1.md\:grid-cols-2.lg\:grid-cols-3 > div {
    padding: 0.9rem;
    border-radius: 1rem;
    min-height: 0;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .grid.grid-cols-1.md\:grid-cols-2.lg\:grid-cols-3 > div .w-10.h-10 {
    width: 2.75rem;
    height: 2.75rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .grid.grid-cols-1.md\:grid-cols-2.lg\:grid-cols-3 > div h3 {
    font-size: 0.92rem;
    line-height: 1.35;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .grid.grid-cols-1.md\:grid-cols-2.lg\:grid-cols-3 > div p {
    margin-top: 0.45rem;
    line-height: 1.55;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .grid.grid-cols-1.md\:grid-cols-2.lg\:grid-cols-3 > div .self-start {
    margin-top: auto;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mt-4.lg\:mt-8 {
    margin-top: 0.75rem;
    padding: 0.9rem;
    border-radius: 1rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mt-4.lg\:mt-8 nav {
    flex-wrap: nowrap;
    overflow-x: auto;
    scrollbar-width: none;
    -ms-overflow-style: none;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mt-4.lg\:mt-8 nav::-webkit-scrollbar {
    display: none;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mt-4.lg\:mt-8 .text-xs.lg\:text-sm.text-gray-500 {
    display: none;
  }
}

.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.line-clamp-4 {
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
