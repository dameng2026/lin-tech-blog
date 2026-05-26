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
            <div class="relative w-full h-52 lg:w-[30rem] lg:h-80 mr-0 lg:mr-8 mt-4 lg:mt-0">
              <img src="/images/Blogroll-3d.png" alt="Links 3D Illustration" class="w-full h-full object-contain">
            </div>
          </div>
        </div>

        <!-- 筛选和搜索-->
        <div class="mb-4 lg:mb-6">
          <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-3 lg:gap-4">
            <!-- 分类标签 -->
            <div class="flex flex-wrap gap-2 lg:gap-4">
              <button @click="switchCategory('')" :class="['px-3 lg:px-4 py-1.5 lg:py-2 text-xs lg:text-sm font-medium transition-colors', activeCategory === '' ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-600 hover:text-gray-900 hover:border-b-2 hover:border-gray-200']">
                全部友链 <span class="text-blue-600 bg-[#eaf1fe] px-2 lg:px-3 py-0.5 rounded-full text-xs font-medium">{{ categoryStats['全部友链'] || 0 }}</span>
              </button>
              <button v-for="cat in categories" :key="cat" @click="switchCategory(cat)" :class="['px-3 lg:px-4 py-1.5 lg:py-2 text-xs lg:text-sm font-medium transition-colors', activeCategory === cat ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-600 hover:text-gray-900 hover:border-b-2 hover:border-gray-200']">
                {{ cat }} <span :class="['px-2 lg:px-3 py-0.5 rounded-full text-xs font-medium', activeCategory === cat ? 'text-blue-600 bg-[#eaf1fe]' : 'text-gray-500 bg-[#f3f4f6]']">{{ categoryStats[cat] || 0 }}</span>
              </button>
            </div>

            <!-- 搜索和排序-->
            <div class="flex items-center gap-2 lg:gap-3">
              <div class="relative flex-1 lg:w-64">
                <input v-model="searchQuery" type="text" placeholder="搜索友链" class="w-full pl-8 lg:pl-10 pr-3 lg:pr-4 py-1.5 lg:py-2 bg-gray-50 border border-gray-200 rounded-lg text-xs lg:text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent">
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
        <div v-if="loading" class="text-center py-12 text-gray-400">加载中...</div>
        <div v-else-if="filteredLinks.length === 0" class="text-center py-12 text-gray-400">暂无友链数据</div>
        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 lg:gap-4">
          <div v-for="(link, index) in filteredLinks" :key="link.id" class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-3 lg:p-6 hover:shadow-[0_10px_30px_rgba(34,60,80,0.08)] transition-shadow h-auto lg:h-[160px]">
            <div class="flex flex-col h-full">
              <div class="flex items-start gap-2 lg:gap-3 h-full">
                <div v-if="link.logo" class="w-10 h-10 lg:w-12 lg:h-12 rounded-full overflow-hidden flex-shrink-0">
                  <img :src="link.logo" :alt="link.name" class="w-full h-full object-cover" @error="($event.target.style.display='none');$event.target.nextElementSibling.style.display='flex'">
                  <div :class="['w-10 h-10 lg:w-12 lg:h-12 rounded-full items-center justify-center flex-shrink-0', getAvatarBg(link, index)]" style="display:none">
                    <span class="text-white font-bold text-sm lg:text-base">{{ getInitial(link.name) }}</span>
                  </div>
                </div>
                <div v-else :class="['w-10 h-10 lg:w-12 lg:h-12 rounded-full flex items-center justify-center flex-shrink-0', getAvatarBg(link, index)]">
                  <span class="text-white font-bold text-sm lg:text-base">{{ getInitial(link.name) }}</span>
                </div>
                <div class="flex-1 h-full flex flex-col">
                  <h3 class="font-semibold text-gray-900 hover:text-blue-600 cursor-pointer text-xs lg:text-sm" @click="visitLink(link.url)">{{ link.name }}</h3>
                  <p class="text-xs text-gray-500 mt-2 lg:mt-3 line-clamp-2 lg:line-clamp-3">{{ link.description || '暂无描述' }}</p>
                  <span :class="['self-start px-1.5 lg:px-2 py-0.5 rounded text-xs mt-auto', getCategoryClass(link.category)]">{{ link.category }}</span>
                </div>
                <img src="/icons/redirect.svg" alt="link" class="w-3 h-3 lg:w-4 lg:h-4 text-gray-300 hover:text-blue-600 flex-shrink-0 mt-0.5 lg:mt-1 cursor-pointer" @click="visitLink(link.url)">
              </div>
            </div>
          </div>
        </div>

        <!-- 分页控件 -->
        <div v-if="totalPages > 1" class="mt-4 lg:mt-8 bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-3 lg:p-6">
          <div class="flex flex-col lg:flex-row justify-between items-center gap-2 lg:gap-0">
            <div class="flex-1 flex justify-center">
              <nav class="flex items-center space-x-1">
                <button @click="goToPage(currentPage - 1)" :disabled="currentPage <= 1" class="w-7 h-7 lg:w-8 lg:h-8 rounded-md border border-gray-200 text-gray-400 hover:bg-gray-50 hover:text-gray-600 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center">
                  <svg class="w-3 h-3 lg:w-4 lg:h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
                  </svg>
                </button>
                <template v-for="p in totalPages" :key="p">
                  <button v-if="p <= 5 || p === totalPages || Math.abs(p - currentPage) <= 1" @click="goToPage(p)" :class="['w-7 h-7 lg:w-8 lg:h-8 rounded-md text-xs lg:text-sm', p === currentPage ? 'bg-blue-500 text-white border border-blue-500' : 'border border-gray-200 text-gray-600 hover:bg-gray-50']">{{ p }}</button>
                  <span v-else-if="p === 6 || p === totalPages - 1" class="text-gray-400">...</span>
                </template>
                <button @click="goToPage(currentPage + 1)" :disabled="currentPage >= totalPages" class="w-7 h-7 lg:w-8 lg:h-8 rounded-md border border-gray-200 text-gray-400 hover:bg-gray-50 hover:text-gray-600 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center">
                  <svg class="w-3 h-3 lg:w-4 lg:h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                  </svg>
                </button>
              </nav>
            </div>
            <span class="text-xs lg:text-sm text-gray-500">{{ total }} 条友链</span>
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
                <img :src="authorAvatar" alt="avatar" class="w-full h-full object-cover" />
              </div>
              <h3 class="font-bold text-xl text-gray-900 mb-1">{{ authorName }}</h3>
              <p class="text-sm text-gray-600">{{ authorPosition }}</p>
          </div>

          <!-- 第二块：个人信息-->
          <div class="w-full space-y-3 mb-6">
            <div v-if="authorLocation" class="flex items-center text-sm text-gray-600">
              <img src="/icons/position-black.svg" alt="地址" class="w-4 h-4 mr-2" />
              {{ authorLocation }}
            </div>
            <div v-if="authorEmail" class="flex items-center text-sm text-gray-600">
              <img src="/icons/email-black.svg" alt="邮箱" class="w-4 h-4 mr-2" />
              {{ authorEmail }}
            </div>
            <div v-if="authorGithub" class="flex items-center text-sm text-gray-600">
              <img src="/icons/github-black.svg" alt="GitHub" class="w-4 h-4 mr-2">
              {{ authorGithub }}
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
              <span class="text-lg font-bold text-gray-900">{{ categoryStats['全部友链'] || 0 }}</span>
            </div>
            <!-- 技术博客-->
            <div class="text-center flex flex-col items-center">
              <div class="w-12 h-12 rounded-full bg-[#fdf5e1] flex items-center justify-center mb-2">
                <img src="/icons/blog.svg" alt="blog" class="w-6 h-6">
              </div>
              <span class="text-xs text-gray-500 mb-1">我的博客</span>
              <span class="text-lg font-bold text-gray-900">{{ categoryStats['技术博客'] || 0 }}</span>
            </div>
            <!-- 开源项目-->
            <div class="text-center flex flex-col items-center">
              <div class="w-12 h-12 rounded-full bg-[#eff8f4] flex items-center justify-center mb-2">
                <img src="/icons/opensource.svg" alt="opensource" class="w-6 h-6">
              </div>
              <span class="text-xs text-gray-500 mb-1">开源项目</span>
              <span class="text-lg font-bold text-gray-900">{{ categoryStats['开源项目'] || 0 }}</span>
            </div>
            <!-- 独立开发者-->
            <div class="text-center flex flex-col items-center">
              <div class="w-12 h-12 rounded-full bg-[#fef9ec] flex items-center justify-center mb-2">
                <img src="/icons/developer.svg" alt="independent" class="w-6 h-6">
              </div>
              <span class="text-xs text-gray-500 mb-1">独立开发者</span>
              <span class="text-lg font-bold text-gray-900">{{ categoryStats['独立开发者'] || 0 }}</span>
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
            
            <div v-if="applySuccess" class="p-6 text-center py-12">
              <div class="text-4xl mb-3">🎉</div>
              <p class="text-green-600 font-semibold">申请已提交！</p>
              <p class="text-gray-500 text-sm mt-1">等待管理员审核</p>
            </div>
            <form v-else @submit.prevent="submitApply" class="p-6 space-y-5">
              <!-- 网站信息 -->
              <div>
                <h4 class="text-sm font-semibold text-gray-700 mb-3">网站信息</h4>
                
                <div class="space-y-4">
                  <div>
                    <label class="block text-xs text-gray-500 mb-1">网站名称 <span class="text-red-500">*</span></label>
                    <input v-model="applyForm.name" type="text" required placeholder="请输入网站名称" class="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                  </div>
                  
                  <div>
                    <label class="block text-xs text-gray-500 mb-1">网站地址 <span class="text-red-500">*</span></label>
                    <input v-model="applyForm.url" type="text" required placeholder="请输入完整的网站地址（需包含 http/https）" class="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                  </div>
                  
                  <div>
                    <label class="block text-xs text-gray-500 mb-1">网站描述 <span class="text-red-500">*</span></label>
                    <textarea v-model="applyForm.description" required placeholder="简要描述您的网站内容、定位与特色（0-100字）" rows="2" class="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"></textarea>
                    <span class="text-xs text-gray-400 float-right">{{ (applyForm.description || '').length }} / 100</span>
                  </div>
                  
                  <div class="grid grid-cols-2 gap-4">
                    <div>
                      <label class="block text-xs text-gray-500 mb-1">网站图标</label>
                      <input v-model="applyForm.logo" type="text" placeholder="请输入网站图标地址" class="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                    </div>
                    <div>
                      <label class="block text-xs text-gray-500 mb-1">网站分类</label>
                      <select v-model="applyForm.category" class="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                        <option value="">请选择网站分类</option>
                        <option v-for="cat in categoryOptions" :key="cat" :value="cat">{{ cat }}</option>
                      </select>
                    </div>
                  </div>
                </div>
              </div>
              
              <div v-if="applyError" class="text-sm text-red-500 bg-red-50 px-4 py-2 rounded-lg">{{ applyError }}</div>
            </form>
            
            <div v-if="!applySuccess" class="flex gap-3 p-6 border-t border-gray-100">
              <button @click="showApplyModal = false" class="flex-1 py-2.5 bg-gray-100 text-gray-700 rounded-lg text-sm hover:bg-gray-200 transition-colors">
                取消
              </button>
              <button @click="submitApply" :disabled="applySubmitting" class="flex-1 py-2.5 bg-blue-600 text-white rounded-lg text-sm hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed">
                {{ applySubmitting ? '提交中...' : '提交申请' }}
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
import { ref, onMounted, computed } from 'vue'
import { usePdfModal } from '../composables/usePdfModal'
import { fetchFriendLinks, fetchFriendLinkStats, applyFriendLink, fetchFriendLinkCategories } from '../api/friendLinks'
import { fetchSiteSettings } from '../api/site'

const showApplyModal = ref(false)
const showInfoModal = ref(false)
const { openModal } = usePdfModal()

const friendLinks = ref([])
const total = ref(0)
const currentPage = ref(1)
const pageSize = ref(12)
const loading = ref(true)
const activeCategory = ref('')
const searchQuery = ref('')
const categoryStats = ref({})
const siteSettings = ref(null)

const applyForm = ref({
  name: '',
  url: '',
  description: '',
  logo: '',
  category: '技术博客'
})
const applySubmitting = ref(false)
const applyError = ref('')
const applySuccess = ref(false)
const categoryOptions = ref(['技术博客', '开源项目', '独立开发者'])

const categories = computed(() => {
  const cats = Object.keys(categoryStats.value).filter(k => k !== '全部友链')
  return cats
})

const filteredLinks = computed(() => {
  let links = friendLinks.value
  if (searchQuery.value.trim()) {
    const q = searchQuery.value.toLowerCase()
    links = links.filter(l =>
      l.name.toLowerCase().includes(q) || (l.description || '').toLowerCase().includes(q)
    )
  }
  return links
})

const totalPages = computed(() => Math.ceil(total.value / pageSize.value))

const authorName = computed(() => siteSettings.value?.author_name || 'Lin')
const authorPosition = computed(() => siteSettings.value?.description || '全栈开发 & AI 应用探索。')
const authorEmail = computed(() => siteSettings.value?.email || '')
const authorGithub = computed(() => (siteSettings.value?.github_url || '').replace(/^https?:\/\//, ''))
const authorLocation = computed(() => siteSettings.value?.location || '中国 · 深圳')
const authorAvatar = computed(() => siteSettings.value?.admin_avatar || '/images/avatar.png')

onMounted(async () => {
  await Promise.all([loadFriendLinks(), loadStats(), loadSettings(), loadCategoryOptions()])
})

async function loadCategoryOptions() {
  try {
    const data = await fetchFriendLinkCategories()
    const cats = data?.data?.categories || data?.categories || []
    if (cats.length > 0) {
      categoryOptions.value = cats
    }
  } catch {}
}

async function loadSettings() {
  try {
    const data = await fetchSiteSettings()
    if (data) siteSettings.value = data
  } catch {}
}

async function loadFriendLinks() {
  loading.value = true
  try {
    const res = await fetchFriendLinks({
      status: 'approved',
      category: activeCategory.value || undefined,
      page: currentPage.value,
      size: pageSize.value
    })
    const d = res?.data || res
    if (d) {
      friendLinks.value = d.friend_links || []
      total.value = d.total || 0
    }
  } catch {
    friendLinks.value = []
    total.value = 0
  } finally {
    loading.value = false
  }
}

async function loadStats() {
  try {
    const data = await fetchFriendLinkStats({ status: 'approved' })
    if (data) categoryStats.value = data.data || data
  } catch {}
}

function switchCategory(category) {
  activeCategory.value = category
  currentPage.value = 1
  loadFriendLinks()
}

function goToPage(page) {
  if (page < 1 || page > totalPages.value) return
  currentPage.value = page
  loadFriendLinks()
}

function visitLink(url) {
  if (url) window.open(url, '_blank')
}

const categoryColorMap = {
  '技术博客': 'bg-blue-100 text-blue-600',
  '开源项目': 'bg-green-100 text-green-600',
  '独立开发': 'bg-purple-100 text-purple-600',
  '独立开发者': 'bg-purple-100 text-purple-600',
}

function getCategoryClass(category) {
  return categoryColorMap[category] || 'bg-gray-100 text-gray-600'
}

const avatarBgColors = [
  'bg-gray-900', 'bg-blue-600', 'bg-green-600', 'bg-purple-600',
  'bg-pink-600', 'bg-teal-500', 'bg-indigo-600', 'bg-red-500',
  'bg-gradient-to-br from-pink-500 via-purple-500 to-cyan-500',
]

function getAvatarBg(link, index) {
  if (link.logo) return ''
  return avatarBgColors[index % avatarBgColors.length]
}

function getInitial(name) {
  if (!name) return '?'
  return name.charAt(0).toUpperCase()
}

const openApplyModal = () => {
  applyError.value = ''
  applySuccess.value = false
  applyForm.value = { name: '', url: '', description: '', logo: '', category: '技术博客' }
  showApplyModal.value = true
}

const openInfoModal = () => {
  showInfoModal.value = true
}

async function submitApply() {
  if (!applyForm.value.name || !applyForm.value.url || !applyForm.value.description) {
    applyError.value = '请填写必填项'
    return
  }
  applySubmitting.value = true
  applyError.value = ''
  try {
    await applyFriendLink(applyForm.value)
    applySuccess.value = true
    setTimeout(() => { showApplyModal.value = false }, 1500)
  } catch (err) {
    applyError.value = err.response?.data?.detail || '提交失败，请稍后重试'
  } finally {
    applySubmitting.value = false
  }
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
