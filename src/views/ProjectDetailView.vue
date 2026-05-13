<template>
  <div class="page-container p-[1.75rem] bg-[#fefefe]">

    <div class="min-h-screen">
      <!-- 面包屑和搜索 -->
      <div class="flex items-center justify-between mb-5">
        <div class="text-sm text-slate-400 font-medium">首页 &nbsp;| &nbsp; 项目 &nbsp;| &nbsp; ChatFlow - 智能对话工作流平台</div>
      </div>

      <div class="flex flex-col lg:flex-row gap-8">
        <!-- 左侧主内容区 -->
        <div class="lg:flex-1 space-y-5">
          <!-- 项目头部卡片 -->
          <div class="bg-white rounded-xl shadow-sm p-6">
            <div class="grid grid-cols-[45%_55%] gap-6">
              <div class="rounded-xl overflow-hidden bg-slate-900 h-[350px] shadow-[0_4px_12px_rgba(0,0,0,0.15)]">
                <img :src="heroImg" class="w-full h-full object-cover opacity-95" alt="ChatFlow"/>
              </div>
              <div class="flex flex-col justify-between">
                <div>
                  <span class="inline-flex items-center gap-1.5 text-xs font-semibold text-blue-600 bg-blue-50 rounded-full px-3 py-1 mb-4">
                    <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                    精选项目</span>
                  <h1 class="text-2xl font-bold text-gray-900 leading-tight">ChatFlow - 智能对话工作流平台</h1>
                  <p class="mt-3 text-sm text-gray-500 leading-relaxed">基于 Agent 的智能对话平台，支持多模型接入<br>工作流编排与知识库集成。</p>
                  <div class="mt-4 flex flex-wrap gap-2">
                    <span v-for="t in tags" :key="t" class="px-3 py-1.5 rounded-full text-xs bg-gray-100 text-gray-600">{{t}}</span>
                  </div>
                </div>
                <div class="flex items-center gap-3 mt-6">
                  <button class="bg-blue-600 text-white rounded-lg px-6 h-10 text-sm font-medium hover:bg-blue-700 transition-colors flex items-center gap-2">访问项目 <img src="/icons/redirect.svg" class="w-4 h-4" /></button>
                  <button class="h-10 px-5 rounded-lg border border-gray-200 bg-white text-gray-700 text-sm font-medium hover:bg-gray-50 transition-colors flex items-center gap-2"><img src="/icons/github-black.svg" class="w-4 h-4" /> 查看源码</button>
                  <button class="h-10 px-4 rounded-lg border border-gray-200 bg-white text-gray-700 text-sm font-medium hover:bg-gray-50 transition-colors flex items-center gap-1.5"><img src="/icons/like-grey.svg" class="w-4 h-4" /> 1.2k</button>
                </div>
              </div>
            </div>

            <div class="mt-6 pt-5 border-t border-gray-100 grid grid-cols-4 gap-4">
              <div class="flex flex-col items-center text-center">
                <div class="w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center mb-2">
                  <img src="/icons/calendar.svg" class="w-4 h-4 text-gray-400" />
                </div>
                <div class="text-xs text-gray-400 mb-1">开发时间</div>
                <div class="text-sm text-gray-600">2024.01 - 2024.04</div>
              </div>
              <div class="flex flex-col items-center text-center border-l border-gray-100">
                <div class="w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center mb-2">
                  <img src="/icons/project-grey.svg" class="w-4 h-4" />
                </div>
                <div class="text-xs text-gray-400 mb-1">项目类型</div>
                <div class="text-sm text-gray-600">个人项目</div>
              </div>
              <div class="flex flex-col items-center text-center border-l border-gray-100">
                <div class="w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center mb-2">
                  <img src="/icons/code.svg" class="w-4 h-4" />
                </div>
                <div class="text-xs text-gray-400 mb-1">技术栈</div>
                <div class="text-sm text-gray-600">Next.js, TypeScript</div>
              </div>
              <div class="flex flex-col items-center text-center border-l border-gray-100">
                <div class="w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center mb-2">
                  <img src="/icons/update.svg" class="w-4 h-4" />
                </div>
                <div class="text-xs text-gray-400 mb-1">最后更新</div>
                <div class="text-sm text-gray-600">2024-05-20</div>
              </div>
            </div>
          </div>

          <!-- 项目详情内容 -->
          <div class="bg-white/86 backdrop-blur-[10px] rounded-2xl border border-white shadow-[0_12px_30px_rgba(15,23,42,.06),0_1px_0_rgba(255,255,255,.9)_inset] p-5">
            <div class="flex gap-6 text-sm font-semibold text-slate-400 border-b border-slate-100">
              <div class="pb-3 border-b-2 border-blue-500 text-blue-600 cursor-pointer">项目介绍</div>
              <div class="pb-3 cursor-pointer hover:text-slate-600">功能特性</div>
              <div class="pb-3 cursor-pointer hover:text-slate-600">技术架构</div>
              <div class="pb-3 cursor-pointer hover:text-slate-600">使用指南</div>
              <div class="pb-3 cursor-pointer hover:text-slate-600">更新日志</div>
            </div>

            <div class="py-6 space-y-7">
              <div>
                <h2 class="text-[18px] font-bold text-slate-900 mb-3">项目简介</h2>
                <p class="text-[14px] leading-7 text-slate-500 max-w-[760px]">ChatFlow 是一个基于 Agent 的智能对话工作流平台，致力于为开发者和企业提供强大、灵活的 AI 对话解决方案。通过可视化的工作流编排、多模型支持和知识库集成，帮助用户快速构建智能对话应用。</p>
              </div>

              <div>
                <h2 class="text-[18px] font-bold text-slate-900 mb-4">核心功能</h2>
                <div class="grid grid-cols-3 gap-5">
                  <div v-for="f in features" :key="f.title" class="p-1">
                    <div class="flex items-start gap-3">
                      <div class="w-8 h-8 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center font-bold">{{f.icon}}</div>
                      <div>
                        <div class="font-semibold text-slate-900 text-[14px]">{{f.title}}</div>
                        <div class="mt-1 text-[12px] leading-6 text-slate-500">{{f.desc}}</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div>
                <h2 class="text-[18px] font-bold text-slate-900 mb-4">技术栈</h2>
                <div class="flex flex-wrap gap-4">
                  <div v-for="s in stack" :key="s.name" class="flex items-center gap-3 min-w-[150px]">
                    <div class="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-xl">{{s.badge}}</div>
                    <div>
                      <div class="text-[14px] font-semibold text-slate-900">{{s.name}}</div>
                      <div class="text-[12px] text-slate-500">{{s.sub}}</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 评论 -->
          <section class="mt-[28px]">
            <div class="flex items-center justify-between mb-[12px]">
              <div class="text-[16px] font-bold text-[#0f172a]">评论 (28)</div>
              <div class="text-[12px] text-[#475569]">最新</div>
            </div>

            <div class="bg-white border border-[#e2e8f0] shadow-[0_1px_2px_rgba(15,23,42,.04)] rounded-[12px] p-[12px] flex gap-[12px] items-start">
              <img class="w-[40px] h-[40px] rounded-full object-cover" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=120&q=80" alt="avatar" />
              <div class="flex-1">
                <textarea v-model="draft" placeholder="写下你的评论..." class="w-full h-[64px] resize-none border border-[#e2e8f0] rounded-[10px] px-[12px] py-[10px] text-[13px] outline-none bg-white text-[#0f172a]"></textarea>
                <div class="flex justify-between items-end mt-[10px]">
                  <div class="text-right">
                    <button @click="publish" class="bg-[#2563eb] text-white border-none rounded-[9px] px-[14px] py-[8px] text-[12px] font-semibold">发布评论</button>
                    <div class="text-[12px] text-[#94a3b8] mt-[8px]">0/1000</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="flex gap-[12px] py-[12px] border-b border-[#eef2f7]" v-for="c in comments" :key="c.name + c.time">
              <img class="w-[40px] h-[40px] rounded-full object-cover flex-shrink-0" :src="c.avatar" alt="user" />
              <div class="flex-1">
                <div class="flex justify-between gap-[10px] items-center">
                  <div class="text-[13px] font-semibold text-[#1e293b]">{{ c.name }} <span v-if="c.badge" class="inline-flex px-[6px] py-[2px] rounded-full bg-[#eff6ff] text-[#2563eb] text-[10px] ml-[6px]">{{ c.badge }}</span></div>
                  <div class="text-[12px] text-[#94a3b8]">{{ c.time }}</div>
                </div>
                <div class="mt-[8px] text-[13px] leading-[1.75] text-[#334155]">{{ c.text }}</div>
                <div class="flex gap-[12px] items-center mt-[8px] text-[12px] text-[#64748b]"><span>👍 {{ c.likes }}</span><span>回复</span></div>
                <div v-if="c.reply" class="mt-[10px] rounded-[12px] bg-[#f8fbff] p-[12px]">
                  <div class="flex justify-between gap-[10px] items-center mb-[6px]">
                    <div class="text-[13px] font-semibold text-[#1e293b]">Lin <span class="inline-flex px-[6px] py-[2px] rounded-full bg-[#dbeafe] text-[#2563eb] text-[10px] ml-[6px]">作者</span></div>
                    <div class="text-[12px] text-[#94a3b8]">2024-05-20 12:02</div>
                  </div>
                  <div class="text-[13px] leading-[1.7] text-[#334155]">这个要根据具体场景来定：<br>1. 复杂推理任务：推荐 GPT-4 / Claude 3<br>2. 成本敏感场景：可以考虑 GPT-3.5 / 开源模型<br>3. 本地部署需求：建议使用 Llama 3 / Qwen 系列<br>文章第 5 节有更详细的对比，欢迎查看～</div>
                  <div class="flex gap-[12px] items-center mt-[8px] text-[12px] text-[#64748b]"><span>👍 12</span><span>回复</span></div>
                </div>
              </div>
            </div>

            <div class="bg-white border border-[#e2e8f0] shadow-[0_1px_2px_rgba(15,23,42,.04)] rounded-[12px] mt-[12px] text-center p-[12px] text-[13px] text-[#2563eb] font-semibold">加载更多评论...</div>
          </section>
        </div>

        <!-- 右侧边栏 -->
        <div class="lg:w-1/5 space-y-5">
          <!-- 作者信?-->
          <div class="bg-white rounded-xl shadow-sm p-6 flex flex-col">
            <div class="flex flex-col items-center mb-6">
              <div class="w-[5rem] h-[5rem] rounded-full overflow-hidden flex-shrink-0 mb-3">
                <img src="/images/avatar.png" alt="Lin" class="w-full h-full object-cover" />
              </div>
              <h3 class="font-bold text-xl text-gray-900 mb-1">Lin</h3>
              <p class="text-sm text-gray-600">全栈开发?& AI 应用探索。</p>
            </div>
            <div class="w-full space-y-3 mb-6">
              <div class="flex items-center text-sm text-gray-600">
                <img src="/icons/position-grey.svg" alt="地址" class="w-4 h-4 mr-2" />
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
          </div>

          <!-- 项目信息 -->
          <div class="bg-white/86 backdrop-blur-[10px] rounded-2xl border border-white shadow-[0_12px_30px_rgba(15,23,42,.06),0_1px_0_rgba(255,255,255,.9)_inset] p-5">
            <h3 class="font-bold text-slate-900 mb-4">项目信息</h3>
            <div class="space-y-4 text-[13px]">
              <div class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2">
                  <img src="/icons/project-status-complete.svg" class="w-4 h-4" />
                  项目状态
                </div>
                <div class="text-[#1e293b] font-medium text-right flex items-center">
                  <span class="w-2 h-2 rounded-full bg-green-500 mr-2"></span>已完成
                </div>
              </div>
              <div class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2">
                  <img src="/icons/agreement.svg" class="w-4 h-4" />
                  开源协议
                </div>
                <div class="text-[#1e293b] font-medium text-right">MIT</div>
              </div>
              <div class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2">
                  <img src="/icons/typescript.svg" class="w-4 h-4" />
                  代码语言
                </div>
                <div class="text-[#1e293b] font-medium text-right">TypeScript 92%</div>
              </div>
              <div class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2">
                  <img src="/icons/framework.svg" class="w-4 h-4" />
                  主要框架
                </div>
                <div class="text-[#1e293b] font-medium text-right">Next.js, React</div>
              </div>
              <div class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2">
                  <img src="/icons/database.svg" class="w-4 h-4" />
                  数据库
                </div>
                <div class="text-[#1e293b] font-medium text-right">PostgreSQL, Redis</div>
              </div>
              <div class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2">
                  <img src="/icons/cloud-platform.svg" class="w-4 h-4" />
                  部署平台
                </div>
                <div class="text-[#1e293b] font-medium text-right">Vercel, Docker</div>
              </div>
            </div>
          </div>

          <!-- 项目链接 -->
          <div class="bg-white/86 backdrop-blur-[10px] rounded-2xl border border-white shadow-[0_12px_30px_rgba(15,23,42,.06),0_1px_0_rgba(255,255,255,.9)_inset] p-5">
            <h3 class="font-bold text-slate-900 mb-4">项目链接</h3>
            <div class="space-y-4 text-[13px]">
              <div class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2">
                  <img src="/icons/demo.svg" class="w-4 h-4" />
                  在线演示
                </div>
                <div class="text-blue-600 font-medium text-right text-xs break-all cursor-pointer hover:underline">https://chatflow.lin.com</div>
              </div>
              <div class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2">
                  <img src="/icons/github-black.svg" class="w-4 h-4" />
                  GitHub 仓库
                </div>
                <div class="text-blue-600 font-medium text-right text-xs break-all cursor-pointer hover:underline">github.com/linxxx/chatflow</div>
              </div>
              <div class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2">
                  <img src="/icons/manual.svg" class="w-4 h-4" />
                  文档站点
                </div>
                <div class="text-blue-600 font-medium text-right text-xs break-all cursor-pointer hover:underline">docs.chatflow.lin.com</div>
              </div>
              <div class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2">
                  <img src="/icons/feedback.svg" class="w-4 h-4" />
                  问题反馈
                </div>
                <div class="text-blue-600 font-medium text-right text-xs break-all cursor-pointer hover:underline">github.com/linxxx/chatflow/issues</div>
              </div>
            </div>
          </div>

          <!-- 相关项目 -->
          <div class="bg-white/86 backdrop-blur-[10px] rounded-2xl border border-white shadow-[0_12px_30px_rgba(15,23,42,.06),0_1px_0_rgba(255,255,255,.9)_inset] p-5">
            <h3 class="font-bold text-slate-900 mb-4">相关项目</h3>
            <div class="space-y-4">
              <div class="flex items-start justify-between gap-3 cursor-pointer group">
                <div class="flex items-start gap-3">
                  <div class="w-8 h-8 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center group-hover:bg-blue-100 transition-colors">
                    <img src="/icons/folder.svg" class="w-4 h-4" />
                  </div>
                  <div>
                    <div class="text-[14px] font-semibold text-slate-900 group-hover:text-blue-600 transition-colors">LLM Knowledge Hub</div>
                    <div class="text-[12px] text-slate-500 mt-1">个人知识库与大模型问答系统</div>
                  </div>
                </div>
                <div class="text-slate-400 text-sm flex items-center gap-1">
                  <img src="/icons/star-blue.svg" class="w-3 h-3" />
                  856
                </div>
              </div>
              <div class="flex items-start justify-between gap-3 cursor-pointer group">
                <div class="flex items-start gap-3">
                  <div class="w-8 h-8 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center group-hover:bg-blue-100 transition-colors">
                    <img src="/icons/folder.svg" class="w-4 h-4" />
                  </div>
                  <div>
                    <div class="text-[14px] font-semibold text-slate-900 group-hover:text-blue-600 transition-colors">Frontier UI</div>
                    <div class="text-[12px] text-slate-500 mt-1">现代化的前端组件库</div>
                  </div>
                </div>
                <div class="text-slate-400 text-sm flex items-center gap-1">
                  <img src="/icons/star-blue.svg" class="w-3 h-3" />
                  623
                </div>
              </div>
              <div class="flex items-start justify-between gap-3 cursor-pointer group">
                <div class="flex items-start gap-3">
                  <div class="w-8 h-8 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center group-hover:bg-blue-100 transition-colors">
                    <img src="/icons/folder.svg" class="w-4 h-4" />
                  </div>
                  <div>
                    <div class="text-[14px] font-semibold text-slate-900 group-hover:text-blue-600 transition-colors">AI Prompt Studio</div>
                    <div class="text-[12px] text-slate-500 mt-1">提示词管理与优化工具</div>
                  </div>
                </div>
                <div class="text-slate-400 text-sm flex items-center gap-1">
                  <img src="/icons/star-blue.svg" class="w-3 h-3" />
                  432
                </div>
              </div>
            </div>
          </div>

          <!-- 项目统计 -->
          <div class="bg-white rounded-xl shadow-sm px-[2rem] py-6">
            <h3 class="font-semibold text-gray-900 mb-4">项目统计</h3>
            <div class="flex justify-between">
              <div class="flex flex-col items-center">
                <div class="w-12 h-12 rounded-full bg-[#f6f7fb] flex items-center justify-center mb-3">
                  <img src="/icons/page-views.svg" alt="访问量" class="w-6 h-6 text-blue-600" />
                </div>
                <div class="text-[0.8rem] text-gray-500 py-1">访问量</div>
                <div class="text-2xl font-bold text-gray-900">18.6k</div>
              </div>
              <div class="flex flex-col items-center">
                <div class="w-12 h-12 rounded-full bg-[#f6f7fb] flex items-center justify-center mb-3">
                  <img src="/icons/like-grey.svg" alt="点赞数" class="w-6 h-6 text-blue-600" />
                </div>
                <div class="text-[0.8rem] text-gray-500 py-1">点赞数</div>
                <div class="text-2xl font-bold text-gray-900">1.2k</div>
              </div>
              <div class="flex flex-col items-center">
                <div class="w-12 h-12 rounded-full bg-[#f6f7fb] flex items-center justify-center mb-3">
                  <img src="/icons/access count.svg" alt="使用数" class="w-6 h-6 text-blue-600" />
                </div>
                <div class="text-[0.8rem] text-gray-500 py-1">使用数</div>
                <div class="text-2xl font-bold text-gray-900">3.4k</div>
              </div>
              <div class="flex flex-col items-center">
                <div class="w-12 h-12 rounded-full bg-[#f6f7fb] flex items-center justify-center mb-3">
                  <img src="/icons/fork.svg" alt="Fork数" class="w-6 h-6 text-blue-600" />
                </div>
                <div class="text-[0.8rem] text-gray-500 py-1">Fork数</div>
                <div class="text-2xl font-bold text-gray-900">256</div>
              </div>
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

const { openModal } = usePdfModal()

const heroImg = ref('https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=900&q=80')

const tags = ref(['Next.js', 'TypeScript', 'LangChain', 'PostgreSQL', 'Docker'])

const features = ref([
  { icon: '?', title: '多模型支持', desc: '支持 OpenAI、Anthropic、Google 等多种大语言模型，能够智能切换与组合' },
  { icon: '?', title: '工作流编辑', desc: '可视化工作流编辑器，支持条件分支、循环、并行等复杂流程' },
  { icon: '?', title: '知识库集', desc: '支持文档上传、向量检索、智能知识问答，让模型更懂业务' },
  { icon: '?', title: '工具调用', desc: '集成多种实用工具?API，扩?Agent 的能力边界' },
  { icon: '?', title: '会话管理', desc: '完整的会话历史管理，支持多轮对话上下文和配置' },
  { icon: '?', title: '数据分析', desc: '内置数据分析和可视化功能，帮助观察对话质量与使用情况' },
])

const stack = ref([
  { badge: 'N', name: 'Next.js', sub: 'React 框架' },
  { badge: 'TS', name: 'TypeScript', sub: '类型安全' },
  { badge: '?', name: 'Tailwind CSS', sub: '样式框架' },
  { badge: '?', name: 'PostgreSQL', sub: '主数据库' },
  { badge: '?', name: 'Redis', sub: '缓存存储' },
  { badge: 'λ', name: 'LangChain', sub: 'AI 框架' },
])

const info = ref([
  { icon: 'status', label: '项目状态', value: '<span class="w-2 h-2 rounded-full bg-green-500 mr-2 inline-block"></span>已完成' },
  { icon: 'license', label: '开源协议', value: 'MIT' },
  { icon: 'language', label: '代码语言', value: 'TypeScript 92%' },
  { icon: 'language', label: '代码语言', value: 'TypeScript 92%' },
  { icon: 'framework', label: '主要框架', value: 'Next.js, React' },
  { icon: 'database', label: '数据库', value: 'PostgreSQL, Redis' },
  { icon: 'deploy', label: '部署平台', value: 'Vercel, Docker' },
])

const links = ref([
  { icon: 'link', label: '在线演示', value: 'https://chatflow.lin.com' },
  { icon: 'link', label: '在线演示', value: 'https://chatflow.lin.com/chatflow' },
  { icon: 'github', label: 'GitHub 仓库', value: 'github.com/linxxx/chatflow' },
  { icon: 'docs', label: '文档站点', value: 'docs.chatflow.lin.com' },
  { icon: 'issue', label: '问题反馈', value: 'github.com/linxxx/chatflow/issues' },
  { icon: 'issue', label: '问题反馈', value: 'github.com/linxxx/chatflow/issues' },
])

const related = ref([
  { title: 'LLM Knowledge Hub', desc: '个人知识库与大模型问答系统', star: '856' },
  { title: 'Frontier UI', desc: '现代化的前端组件库', star: '623' },
  { title: 'AI Prompt Studio', desc: '提示词管理与优化工具', star: '432' },
])

const stats = ref([
  { icon: 'eye', label: '访问量', value: '18.6k' },
  { icon: 'star', label: '点赞数', value: '1.2k' },   
  { icon: 'users', label: '使用数', value: '3.4k' },
  { icon: 'fork', label: 'Fork数', value: '256' },
])

const draft = ref('')
const comments = ref([
  { name: '张三', badge: '置顶', time: '2024-05-20 11:20', text: '这个项目很有创意！特别是工作流编排功能，非常适合我们团队使用', likes: 18, avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=120&q=80' },
  { name: '李四', time: '2024-05-20 11:45', text: '请问支持本地部署吗？想要在内部网络中使用', likes: 5, avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=120&q=80', reply: true },
  { name: '王五', time: '2024-05-20 13:15', text: '文档写得很详细，期待后续更新', likes: 3, avatar: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=120&q=80' },
])
const publish = () => alert(draft.value ? `发布?${draft.value}` : '请输入评论内容')
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

  .page-container > .min-h-screen > .flex.items-center.justify-between.mb-5 {
    margin-bottom: 0.7rem;
  }

  .page-container > .min-h-screen > .flex.items-center.justify-between.mb-5 .text-sm.text-slate-400.font-medium {
    font-size: 0.7rem;
    line-height: 1.4;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row {
    gap: 0.75rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 {
    min-width: 0;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 {
    padding: 0.9rem;
    border-radius: 1rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 .grid.grid-cols-\[45\%_55\%\] {
    grid-template-columns: 1fr;
    gap: 0.9rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 .rounded-xl.overflow-hidden.bg-slate-900.h-\[350px\] {
    height: 11.5rem;
    border-radius: 1rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 .flex.flex-col.justify-between {
    gap: 0.65rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 .inline-flex.items-center.gap-1\.5 {
    padding: 0.35rem 0.7rem;
    margin-bottom: 0.6rem;
    border-radius: 9999px;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 h1 {
    font-size: 1.3rem;
    line-height: 1.25;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 p {
    font-size: 0.8rem;
    line-height: 1.7;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 .mt-4.flex.flex-wrap.gap-2 {
    gap: 0.4rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 .mt-4.flex.flex-wrap.gap-2 span {
    padding: 0.35rem 0.65rem;
    font-size: 0.72rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 .mt-6.flex.items-center.gap-3 {
    margin-top: 0.9rem;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 .mt-6.flex.items-center.gap-3 button {
    flex: 1 1 calc(50% - 0.25rem);
    min-width: 0;
    justify-content: center;
    padding: 0.8rem 0.9rem;
    font-size: 0.78rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 .mt-6.flex.items-center.gap-3 button:last-child {
    flex-basis: 100%;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 .mt-6.flex.items-center.gap-3 button:first-child,
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 .mt-6.flex.items-center.gap-3 button:nth-child(2) {
    flex-basis: calc(50% - 0.25rem);
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mt-6.pt-5.border-t.border-gray-100.grid.grid-cols-4.gap-4 {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.75rem 0.5rem;
    margin-top: 1rem;
    padding-top: 1rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mt-6.pt-5.border-t.border-gray-100.grid.grid-cols-4.gap-4 > div {
    padding: 0.65rem 0.4rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mt-6.pt-5.border-t.border-gray-100.grid.grid-cols-4.gap-4 > div:nth-child(n+2) {
    border-left: 0;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mt-6.pt-5.border-t.border-gray-100.grid.grid-cols-4.gap-4 > div .text-xs.text-gray-400.mb-1 {
    font-size: 0.7rem;
    margin-bottom: 0.35rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mt-6.pt-5.border-t.border-gray-100.grid.grid-cols-4.gap-4 > div .text-sm.text-gray-600 {
    font-size: 0.78rem;
    line-height: 1.35;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5 {
    padding: 0.9rem;
    border-radius: 1rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5 .flex.gap-6.text-sm.font-semibold.text-slate-400.border-b.border-slate-100 {
    gap: 0.9rem;
    overflow-x: auto;
    white-space: nowrap;
    scrollbar-width: none;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5 .flex.gap-6.text-sm.font-semibold.text-slate-400.border-b.border-slate-100::-webkit-scrollbar {
    display: none;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5 .py-6.space-y-7 {
    padding-top: 1rem;
    padding-bottom: 1rem;
    gap: 1.25rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5 .grid.grid-cols-3.gap-5 {
    grid-template-columns: 1fr;
    gap: 0.9rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5 .grid.grid-cols-3.gap-5 > div {
    padding: 0.1rem 0;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5 .grid.grid-cols-3.gap-5 > div .w-8.h-8 {
    width: 2.2rem;
    height: 2.2rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5 .grid.grid-cols-3.gap-5 > div .font-semibold.text-slate-900.text-\[14px\] {
    font-size: 0.84rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5 .grid.grid-cols-3.gap-5 > div .mt-1.text-\[12px\].leading-6.text-slate-500 {
    font-size: 0.73rem;
    line-height: 1.45;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5 .grid.grid-cols-3.gap-5 > div .flex.items-start.gap-3 {
    gap: 0.65rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5 .grid.grid-cols-3.gap-5 > div {
    width: 100%;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5 .flex.flex-wrap.gap-4 {
    gap: 0.7rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5 .flex.flex-wrap.gap-4 > div {
    min-width: 0;
    width: 100%;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5 .flex.flex-wrap.gap-4 > div .min-w-\[150px\] {
    min-width: 0;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5 .flex.flex-wrap.gap-4 > div .flex.items-center.gap-3 {
    width: 100%;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5 .flex.flex-wrap.gap-4 > div .w-10.h-10 {
    width: 2.5rem;
    height: 2.5rem;
  }

  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:w-1\/5 {
    display: none;
  }

  .page-container > .min-h-screen > .flex.items-center.justify-between.mb-5,
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mt-6.pt-5.border-t.border-gray-100.grid.grid-cols-4.gap-4,
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white\/86.backdrop-blur-\[10px\].rounded-2xl.border.border-white.shadow-\[0_12px_30px_rgba\(15\,23\,42\,\.06\)\,0_1px_0_rgba\(255\,255\,255\,\.9\)_inset\].p-5,
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 {
    width: 100%;
  }
}
</style>
