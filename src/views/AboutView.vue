﻿﻿﻿﻿﻿<template>
  <div class="page-container p-[1.75rem] bg-[#fefefe]">
    <div class="min-h-screen">
      <div class="mx-auto w-full min-h-screen">
        <!-- ===== 顶部个人信息 - 移动端 ===== -->
        <div class="lg:hidden bg-white rounded-2xl shadow-sm p-5 mb-4">
          <div class="flex items-center gap-4 mb-4">
            <div class="w-20 h-20 rounded-full bg-gray-200 overflow-hidden flex-shrink-0">
              <img src="/images/avatar.png" alt="Lin" class="w-full h-full object-cover">
            </div>
            <div>
              <h1 class="text-xl font-bold text-gray-900 mb-1">Lin</h1>
              <p class="text-sm text-gray-600">全栈开发 & AI 应用探索</p>
            </div>
          </div>
          <p class="text-gray-600 text-sm mb-4">我热衷于构建智能、高效、有价值的产品。探索 Agent、LLM 应用与前端工程化的边界，让技术真正服务于人。</p>
          <div class="grid grid-cols-2 gap-4">
            <div class="flex items-center text-xs text-gray-500">
              <img src="/icons/position-grey.svg" alt="地址" class="w-4 h-4 mr-2">
              中国 · 深圳
            </div>
            <div class="flex items-center text-xs text-gray-500">
              <img src="/icons/email-grey.svg" alt="邮箱" class="w-4 h-4 mr-2">
              lin@example.com
            </div>
            <div class="flex items-center text-xs text-gray-500">
              <img src="/icons/github-grey.svg" alt="GitHub" class="w-4 h-4 mr-2">
              github.com/linxxxx
            </div>
            <div class="flex items-center text-xs text-gray-500">
              <img src="/icons/project-grey.svg" alt="开发经验" class="w-4 h-4 mr-2">
              5 年开发经验
            </div>
          </div>
        </div>

        <!-- ===== 顶部个人信息 - 桌面端 ===== -->
        <div class="hidden lg:block bg-[#f2f5fd] rounded-2xl pt-12 pr-12 pl-16 mb-4 overflow-hidden relative min-h-[420px]">
          <!-- 3D插画作为背景 -->
          <div class="absolute right-0 top-0 w-[50%] h-[95%] flex items-center justify-end pointer-events-none pr-8 pt-4">
            <img src="/images/hero-3d.png" alt="AI Cube" class="w-auto h-full object-contain object-right-center">
          </div>

          <!-- 内容区域 -->
          <div class="relative z-10 h-full flex flex-col justify-between py-8">
            <div class="flex flex-row items-start gap-10 flex-1">
              <!-- 头像 -->
              <div class="w-44 h-44 rounded-full bg-gray-200 overflow-hidden flex-shrink-0 -mt-4">
              <img src="/images/avatar.png" alt="Lin" class="w-full object-cover object-top">
            </div>

            <!-- 文字信息 -->
            <div class="flex-1 max-w-[19rem] pt-1">
              <h1 class="text-[2rem] font-bold text-gray-900 mb-4">Lin</h1>
              <p class="text-[1.15rem] text-gray-600 mb-[2.5rem]">全栈开发 & AI 应用探索。</p>
              <p class="text-gray-500 leading-loose text-[0.9rem]">
                我热衷于构建智能、高效、有价值的产品。探索 Agent、LLM 应用与前端工程化的边界，让技术真正服务于人。</p>
            </div>
          </div>

          <!-- 联系方式（单独一行） -->
          <div class="flex flex-wrap gap-14 mt-12">
            <div class="flex items-center text-[0.8rem] text-gray-500">
              <img src="/icons/position-grey.svg" alt="地址" class="w-5 h-5 mr-3">
              中国 · 深圳
            </div>
            <div class="flex items-center text-[0.8rem] text-gray-500">
              <img src="/icons/email-grey.svg" alt="邮箱" class="w-5 h-5 mr-3">
              lin@example.com
            </div>
            <div class="flex items-center text-[0.8rem] text-gray-500">
              <img src="/icons/github-grey.svg" alt="GitHub" class="w-5 h-5 mr-3">
              github.com/linxxxx
            </div>
            <div class="flex items-center text-[0.8rem] text-gray-500">
              <img src="/icons/project-grey.svg" alt="开发经验" class="w-5 h-5 mr-3">
              5 年开发经验</div>
          </div>
        </div>
      </div>

      <!-- 技术栈和核心技能 -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4">
        <!-- 技术栈 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6">
          <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26] mb-3 lg:mb-4">技术栈</h2>
          <div class="flex flex-wrap gap-2 lg:gap-3">
            <span class="px-2.5 py-1.5 bg-gray-100 rounded-lg text-xs lg:text-sm text-gray-700">TypeScript</span>
            <span class="px-2.5 py-1.5 bg-gray-100 rounded-lg text-xs lg:text-sm text-gray-700">JavaScript</span>
            <span class="px-2.5 py-1.5 bg-gray-100 rounded-lg text-xs lg:text-sm text-gray-700">React</span>
            <span class="px-2.5 py-1.5 bg-gray-100 rounded-lg text-xs lg:text-sm text-gray-700">Next.js</span>
            <span class="px-2.5 py-1.5 bg-gray-100 rounded-lg text-xs lg:text-sm text-gray-700">Node.js</span>
            <span class="px-2.5 py-1.5 bg-gray-100 rounded-lg text-xs lg:text-sm text-gray-700">Python</span>
            <span class="px-2.5 py-1.5 bg-gray-100 rounded-lg text-xs lg:text-sm text-gray-700">LangChain</span>
            <span class="px-2.5 py-1.5 bg-gray-100 rounded-lg text-xs lg:text-sm text-gray-700">FastAPI</span>
            <span class="px-2.5 py-1.5 bg-gray-100 rounded-lg text-xs lg:text-sm text-gray-700">Tailwind CSS</span>
            <span class="px-2.5 py-1.5 bg-gray-100 rounded-lg text-xs lg:text-sm text-gray-700">PostgreSQL</span>
            <span class="px-2.5 py-1.5 bg-gray-100 rounded-lg text-xs lg:text-sm text-gray-700">Docker</span>
            <span class="px-2.5 py-1.5 bg-gray-100 rounded-lg text-xs lg:text-sm text-gray-700">Git</span>
          </div>
        </div>

        <!-- 核心技能 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6">
          <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26] mb-3 lg:mb-4">核心技能</h2>
          <div class="space-y-3 lg:space-y-4">
            <div>
              <div class="flex justify-between mb-1.5">
                <span class="text-xs lg:text-sm text-gray-700">TypeScript</span>
                <span class="text-xs lg:text-sm text-gray-500">90%</span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-1">
                <div class="bg-blue-600 h-1 rounded-full" style="width: 90%"></div>
              </div>
            </div>
            <div>
              <div class="flex justify-between mb-1.5">
                <span class="text-xs lg:text-sm text-gray-700">React / Next.js</span>
                <span class="text-xs lg:text-sm text-gray-500">85%</span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-1">
                <div class="bg-blue-600 h-1 rounded-full" style="width: 85%"></div>
              </div>
            </div>
            <div>
              <div class="flex justify-between mb-1.5">
                <span class="text-xs lg:text-sm text-gray-700">Python</span>
                <span class="text-xs lg:text-sm text-gray-500">80%</span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-1">
                <div class="bg-blue-600 h-1 rounded-full" style="width: 80%"></div>
              </div>
            </div>
            <div>
              <div class="flex justify-between mb-1.5">
                <span class="text-xs lg:text-sm text-gray-700">LangChain</span>
                <span class="text-xs lg:text-sm text-gray-500">75%</span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-1">
                <div class="bg-blue-600 h-1 rounded-full" style="width: 75%"></div>
              </div>
            </div>
            <div>
              <div class="flex justify-between mb-1.5">
                <span class="text-xs lg:text-sm text-gray-700">Node.js</span>
                <span class="text-xs lg:text-sm text-gray-500">70%</span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-1">
                <div class="bg-blue-600 h-1 rounded-full" style="width: 70%"></div>
              </div>
            </div>
            <div>
              <div class="flex justify-between mb-1.5">
                <span class="text-xs lg:text-sm text-gray-700">Tailwind CSS</span>
                <span class="text-xs lg:text-sm text-gray-500">85%</span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-1">
                <div class="bg-blue-600 h-1 rounded-full" style="width: 85%"></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 工作经历和教育背景 -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4">
        <!-- 工作经历 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6">
          <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26] mb-4 lg:mb-6">工作经历</h2>
          <div class="relative">
            <!-- 时间线 -->
            <div class="absolute left-0 top-2 bottom-0 w-0.5 bg-[#edf0f7] ml-2"></div>
            <div class="space-y-6 lg:space-y-8">
              <div class="relative pl-6 lg:pl-8">
                <div class="absolute left-0 top-1.5 w-3 h-3 lg:w-3.5 lg:h-3.5 bg-blue-500 rounded-full border-2 border-white shadow"></div>
                <p class="text-[#959db0] text-xs lg:text-[0.95rem] mb-1 lg:mb-2">2022.05 - 至今</p>
                <h3 class="text-sm lg:text-[1.2rem] font-semibold text-[#161b26] mb-1 lg:mb-2">高级全栈开发工程师 · 某科技公司</h3>
                <p class="text-[#6f7687] text-xs lg:text-[0.95rem] leading-relaxed mb-2 lg:mb-4">负责 AI 平台与智能工具链的设计与开发，主导多个核心模块的架构与实现。</p>
                <div class="flex flex-wrap gap-1.5 lg:gap-2">
                  <span class="px-2 py-1 bg-[#f6f6fb] rounded-lg text-xs text-[#6f7687]">TypeScript</span>
                  <span class="px-2 py-1 bg-[#f6f6fb] rounded-lg text-xs text-[#6f7687]">React</span>
                  <span class="px-2 py-1 bg-[#f6f6fb] rounded-lg text-xs text-[#6f7687]">Node.js</span>
                  <span class="px-2 py-1 bg-[#f6f6fb] rounded-lg text-xs text-[#6f7687]">Python</span>
                  <span class="px-2 py-1 bg-[#f6f6fb] rounded-lg text-xs text-[#6f7687]">Docker</span>
                </div>
              </div>
              <div class="relative pl-6 lg:pl-8">
                <div class="absolute left-0 top-1.5 w-3 h-3 lg:w-3.5 lg:h-3.5 bg-blue-500 rounded-full border-2 border-white shadow"></div>
                <p class="text-[#959db0] text-xs lg:text-[0.95rem] mb-1 lg:mb-2">2020.03 - 2022.04</p>
                <h3 class="text-sm lg:text-[1.2rem] font-semibold text-[#161b26] mb-1 lg:mb-2">全栈开发工程师 · 某互联网公司</h3>
                <p class="text-[#6f7687] text-xs lg:text-[0.95rem] leading-relaxed mb-2 lg:mb-4">参与公司中台系统与业务平台的研发，负责前端架构设计与后端服务开发。</p>
                <div class="flex flex-wrap gap-1.5 lg:gap-2">
                  <span class="px-2 py-1 bg-[#f6f6fb] rounded-lg text-xs text-[#6f7687]">React</span>
                  <span class="px-2 py-1 bg-[#f6f6fb] rounded-lg text-xs text-[#6f7687]">TypeScript</span>
                  <span class="px-2 py-1 bg-[#f6f6fb] rounded-lg text-xs text-[#6f7687]">Nest.js</span>
                  <span class="px-2 py-1 bg-[#f6f6fb] rounded-lg text-xs text-[#6f7687]">PostgreSQL</span>
                </div>
              </div>
              <div class="relative pl-6 lg:pl-8">
                <div class="absolute left-0 top-1.5 w-3 h-3 lg:w-3.5 lg:h-3.5 bg-blue-500 rounded-full border-2 border-white shadow"></div>
                <p class="text-[#959db0] text-xs lg:text-[0.95rem] mb-1 lg:mb-2">2018.07 - 2020.02</p>
                <h3 class="text-sm lg:text-[1.2rem] font-semibold text-[#161b26] mb-1 lg:mb-2">前端开发工程师 · 某创业公司</h3>
                <p class="text-[#6f7687] text-xs lg:text-[0.95rem] leading-relaxed mb-2 lg:mb-4">负责产品前端开发与性能优化，参与从 0 到 1 的产品建设。</p>
                <div class="flex flex-wrap gap-1.5 lg:gap-2">
                  <span class="px-2 py-1 bg-[#f6f6fb] rounded-lg text-xs text-[#6f7687]">JavaScript</span>
                  <span class="px-2 py-1 bg-[#f6f6fb] rounded-lg text-xs text-[#6f7687]">Vue.js</span>
                  <span class="px-2 py-1 bg-[#f6f6fb] rounded-lg text-xs text-[#6f7687]">HTML/CSS</span>
                  <span class="px-2 py-1 bg-[#f6f6fb] rounded-lg text-xs text-[#6f7687]">Webpack</span>
                </div>
              </div>
            </div>
          </div>
          <button @click="openModal" class="text-blue-600 hover:underline flex items-center mt-4 lg:mt-6 text-xs lg:text-[0.95rem] font-medium">
            查看完整履历（PDF）<span class="ml-2">→</span>
          </button>
        </div>
        <!-- 教育背景和我的理念 -->
        <div class="flex flex-col h-full">
          <!-- 教育背景 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6 mb-4">
            <div class="flex items-center mb-3 lg:mb-5">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#eef3ff] rounded-xl flex items-center justify-center mr-3 lg:mr-4">
                <img src="/icons/education.svg" alt="教育背景" class="w-5 h-5 lg:w-6 lg:h-6">
              </div>
              <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26]">教育背景</h2>
            </div>
            <div class="space-y-4 lg:space-y-6">
              <div>
                <div class="flex justify-between items-start mb-2 lg:mb-3">
                  <div>
                    <p class="text-[#959db0] text-xs lg:text-[0.95rem] mb-1 lg:mb-2">2014.09 - 2018.06</p>
                    <h3 class="text-sm lg:text-[1.2rem] font-semibold text-[#161b26]">计算机科学与技术 · 本科</h3>
                    <p class="text-[#959db0] text-xs lg:text-[0.95rem] mt-1 lg:mt-2">某某大学</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- 我的理念 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6 flex-1">
            <div class="flex items-center mb-4 lg:mb-6">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#eef3ff] rounded-xl flex items-center justify-center mr-3 lg:mr-4">
                <img src="/icons/quotation.svg" alt="我的理念" class="w-5 h-5 lg:w-6 lg:h-6">
              </div>
              <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26]">我的理念</h2>
            </div>
            <div class="space-y-3 lg:space-y-5">
              <p class="text-[#6f7687] text-xs lg:text-[0.95rem] leading-relaxed">技术的价值不在于复杂，而在于解决问题；产品的价值不在于功能，而在于用户体验。</p>
              <div class="flex items-center">
                <div class="w-5 h-5 lg:w-6 lg:h-6 text-blue-500 mr-3 lg:mr-4 flex items-center justify-center">
                  <img src="/icons/quotation.svg" alt="引用" class="w-4 h-4 lg:w-5 lg:h-5">
                </div>
                <p class="text-[#6f7687] text-xs lg:text-[0.95rem] font-medium">持续学习，保持好奇心</p>
              </div>
              <div class="flex items-center">
                <div class="w-5 h-5 lg:w-6 lg:h-6 text-blue-500 mr-3 lg:mr-4 flex items-center justify-center">
                  <img src="/icons/quotation.svg" alt="引用" class="w-4 h-4 lg:w-5 lg:h-5">
                </div>
                <p class="text-[#6f7687] text-xs lg:text-[0.95rem] font-medium">注重工程质量与用户体验</p>
              </div>
              <div class="flex items-center">
                <div class="w-5 h-5 lg:w-6 lg:h-6 text-blue-500 mr-3 lg:mr-4 flex items-center justify-center">
                  <img src="/icons/quotation.svg" alt="引用" class="w-4 h-4 lg:w-5 lg:h-5">
                </div>
                <p class="text-[#6f7687] text-xs lg:text-[0.95rem] font-medium">用技术创造实际价值</p>
              </div>
              <div class="flex items-center">
                <div class="w-5 h-5 lg:w-6 lg:h-6 text-blue-500 mr-3 lg:mr-4 flex items-center justify-center">
                  <img src="/icons/quotation.svg" alt="引用" class="w-4 h-4 lg:w-5 lg:h-5">
                </div>
                <p class="text-[#6f7687] text-xs lg:text-[0.95rem] font-medium">开放分享，互相成长</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 兴趣爱好和站点数据 -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4">
        <!-- 兴趣爱好 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6">
          <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26] mb-3 lg:mb-4">兴趣爱好</h2>
          <div class="flex justify-between">
            <div class="flex flex-col items-center">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#f6f6fb] rounded-lg flex items-center justify-center mb-1.5 lg:mb-2">
                <img src="/icons/explore.svg" alt="技术探索" class="w-5 h-5 lg:w-6 lg:h-6 text-blue-600">
              </div>
              <span class="text-xs lg:text-sm text-gray-700">技术探索</span>
            </div>
            <div class="flex flex-col items-center">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#f6f6fb] rounded-lg flex items-center justify-center mb-1.5 lg:mb-2">
                <img src="/icons/contribution.svg" alt="开源贡献" class="w-5 h-5 lg:w-6 lg:h-6 text-blue-600">
              </div>
              <span class="text-xs lg:text-sm text-gray-700">开源贡献</span>
            </div>
            <div class="flex flex-col items-center">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#f6f6fb] rounded-lg flex items-center justify-center mb-1.5 lg:mb-2">
                <img src="/icons/reading.svg" alt="阅读写作" class="w-5 h-5 lg:w-6 lg:h-6 text-blue-600">
              </div>
              <span class="text-xs lg:text-sm text-gray-700">阅读写作</span>
            </div>
            <div class="flex flex-col items-center">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#f6f6fb] rounded-lg flex items-center justify-center mb-1.5 lg:mb-2">
                <img src="/icons/travel.svg" alt="旅行" class="w-5 h-5 lg:w-6 lg:h-6 text-blue-600">
              </div>
              <span class="text-xs lg:text-sm text-gray-700">旅行</span>
            </div>
            <div class="flex flex-col items-center">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#f6f6fb] rounded-lg flex items-center justify-center mb-1.5 lg:mb-2">
                <img src="/icons/sports.svg" alt="健身运动" class="w-5 h-5 lg:w-6 lg:h-6 text-blue-600">
              </div>
              <span class="text-xs lg:text-sm text-gray-700">健身运动</span>
            </div>
          </div>
        </div>
        <!-- 站点数据 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6">
          <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26] mb-3 lg:mb-4">站点数据</h2>
          <div class="flex justify-between">
            <div class="flex flex-col items-center">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#f6f6fb] rounded-lg flex items-center justify-center mb-2 lg:mb-3">
                <img src="/icons/article-blue.svg" alt="文章" class="w-5 h-5 lg:w-6 lg:h-6 text-blue-600">
              </div>
              <div class="text-xs text-gray-900 mt-0.5 lg:mt-1">文章</div>
              <div class="text-lg lg:text-1xl font-bold text-gray-900">32</div>
            </div>
            <div class="flex flex-col items-center">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#f6f6fb] rounded-lg flex items-center justify-center mb-2 lg:mb-3">
                <img src="/icons/project-grey.svg" alt="项目" class="w-5 h-5 lg:w-6 lg:h-6 text-blue-600">
              </div>
              <div class="text-xs text-gray-900 mt-0.5 lg:mt-1">项目</div>
              <div class="text-lg lg:text-1xl font-bold text-gray-900">12</div>
            </div>
            <div class="flex flex-col items-center">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#f6f6fb] rounded-lg flex items-center justify-center mb-2 lg:mb-3">
                <img src="/icons/eye.svg" alt="访问" class="w-5 h-5 lg:w-6 lg:h-6 text-blue-600">
              </div>
              <div class="text-xs text-gray-900 mt-0.5 lg:mt-1">访问</div>
              <div class="text-lg lg:text-1xl font-bold text-gray-900">18.6k</div>
            </div>
            <div class="flex flex-col items-center">
              <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#f6f6fb] rounded-lg flex items-center justify-center mb-2 lg:mb-3">
                <img src="/icons/calendar.svg" alt="运行天数" class="w-5 h-5 lg:w-6 lg:h-6 text-blue-600">
              </div>
              <div class="text-xs text-gray-900 mt-0.5 lg:mt-1">运行天数</div>
              <div class="text-lg lg:text-1xl font-bold text-gray-900">236</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 最近发布和联系方式 -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
        <!-- 最近发布 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6">
          <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26] mb-3 lg:mb-4">最近发布</h2>
          <div class="space-y-3 lg:space-y-4">
            <div class="flex items-center justify-between">
              <div class="flex items-center flex-1 min-w-0">
                <span class="w-1.5 h-1.5 lg:w-2 lg:h-2 bg-blue-500 rounded-full mr-2 lg:mr-3 flex-shrink-0"></span>
                <span class="text-blue-600 hover:text-blue-700 cursor-pointer text-xs lg:text-sm truncate">深入理解 Agent：从原理到实践</span>
              </div>
              <span class="text-gray-400 text-xs lg:text-sm flex-shrink-0 ml-2">2 天前</span>
            </div>
            <div class="flex items-center justify-between">
              <div class="flex items-center flex-1 min-w-0">
                <span class="w-1.5 h-1.5 lg:w-2 lg:h-2 bg-blue-500 rounded-full mr-2 lg:mr-3 flex-shrink-0"></span>
                <span class="text-blue-600 hover:text-blue-700 cursor-pointer text-xs lg:text-sm truncate">更新了项目 ChatFlow - 智能对话工作流平台</span>
              </div>
              <span class="text-gray-400 text-xs lg:text-sm flex-shrink-0 ml-2">5 天前</span>
            </div>
            <div class="flex items-center justify-between">
              <div class="flex items-center flex-1 min-w-0">
                <span class="w-1.5 h-1.5 lg:w-2 lg:h-2 bg-blue-500 rounded-full mr-2 lg:mr-3 flex-shrink-0"></span>
                <span class="text-blue-600 hover:text-blue-700 cursor-pointer text-xs lg:text-sm truncate">发布了新文章《React 19 新特性详解与实践》</span>
              </div>
              <span class="text-gray-400 text-xs lg:text-sm flex-shrink-0 ml-2">8 天前</span>
            </div>
          </div>
        </div>
        <!-- 联系方式 -->
        <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-4 lg:p-6 min-h-[170px] relative overflow-hidden">
            <h2 class="text-base lg:text-[1.3rem] font-semibold text-[#161b26] mb-3 lg:mb-4">联系方式</h2>
            <p class="text-[#8a91a1] text-xs lg:text-[0.82rem] mb-4 lg:mb-6">欢迎交流与合作，一起探索技术的边界。</p>
            <div class="space-y-3 lg:space-y-4">
              <div class="flex items-center text-xs lg:text-[0.86rem] text-[#5f6677]"><img src="/icons/email-grey.svg" class="w-4 h-4 lg:w-5 lg:h-5 mr-2 lg:mr-3 opacity-70" alt="邮箱">lin@example.com</div>
              <div class="flex items-center text-xs lg:text-[0.86rem] text-[#5f6677]"><img src="/icons/github-grey.svg" class="w-4 h-4 lg:w-5 lg:h-5 mr-2 lg:mr-3 opacity-70" alt="GitHub">github.com/linxxxx</div>
              <div class="flex items-center text-xs lg:text-[0.86rem] text-[#5f6677]"><img src="/icons/position-grey.svg" class="w-4 h-4 lg:w-5 lg:h-5 mr-2 lg:mr-3 opacity-70" alt="地址">中国 · 深圳</div>
            </div>
            <div class="hidden lg:block absolute right-6 bottom-4 w-[170px] opacity-90 pointer-events-none">
              <img src="/images/hero-3d.png" alt="decor" class="w-full h-auto object-contain">
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { usePdfModal } from '../composables/usePdfModal'

const { openModal } = usePdfModal()

// 关于页面逻辑
</script>

<style scoped>
.page-container {
  background: #ffffff;
  padding: 1.75rem;
}
</style>
