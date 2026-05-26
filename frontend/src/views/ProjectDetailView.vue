<template>
  <div class="page-container p-[1.75rem] bg-[#fefefe]">
    <div class="min-h-screen">
      <div v-if="loading" class="flex items-center justify-center h-96">
        <div class="text-center">
          <div class="w-12 h-12 border-4 border-blue-600 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
          <p class="text-gray-500">正在加载项目详情...</p>
        </div>
      </div>

      <div v-else-if="error" class="flex items-center justify-center h-96">
        <div class="text-center">
          <div class="text-6xl mb-4">😕</div>
          <h2 class="text-xl font-bold text-gray-900 mb-2">{{ error }}</h2>
          <p class="text-gray-500 mb-4">请检查项目 ID 或返回上一页重试</p>
          <button @click="router.back()" class="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700">返回上一页</button>
        </div>
      </div>

      <template v-else-if="project">
      <div class="flex items-center justify-between mb-5">
        <div class="text-sm text-slate-400 font-medium">首页 &nbsp;| &nbsp; 项目 &nbsp;| &nbsp; {{ project.name }}</div>
      </div>

      <div class="flex flex-col lg:flex-row gap-8">
        <div class="lg:flex-1 space-y-5">
          <!-- 项目头部卡片 -->
          <div class="bg-white rounded-xl shadow-sm p-6">
            <div class="grid grid-cols-[45%_55%] gap-6">
              <div class="rounded-xl overflow-hidden bg-slate-900 h-[350px] shadow-[0_4px_12px_rgba(0,0,0,0.15)]">
                <img :src="coverUrl" class="w-full h-full object-cover opacity-95" :alt="project.name" @error="handleImageError"/>
              </div>
              <div class="flex flex-col justify-between">
                <div>
                  <span v-if="project.is_featured" class="inline-flex items-center gap-1.5 text-xs font-semibold text-blue-600 bg-blue-50 rounded-full px-3 py-1 mb-4">
                    <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                    精选项目</span>
                  <h1 class="text-2xl font-bold text-gray-900 leading-tight">{{ project.name }}</h1>
                  <p class="mt-3 text-sm text-gray-500 leading-relaxed">{{ project.summary || '暂无简介' }}</p>
                  <div class="mt-4 flex flex-wrap gap-2">
                    <span v-for="tag in (project.tags || [])" :key="tag" class="px-3 py-1.5 rounded-full text-xs bg-gray-100 text-gray-600">{{ tag }}</span>
                  </div>
                </div>
                <div class="flex items-center gap-3 mt-6">
                  <button @click="visitDemo" class="bg-blue-600 text-white rounded-lg px-6 h-10 text-sm font-medium hover:bg-blue-700 transition-colors flex items-center gap-2">访问项目 <img src="/icons/redirect.svg" class="w-4 h-4" /></button>
                  <button @click="visitGithub" class="h-10 px-5 rounded-lg border border-gray-200 bg-white text-gray-700 text-sm font-medium hover:bg-gray-50 transition-colors flex items-center gap-2"><img src="/icons/github-black.svg" class="w-4 h-4" /> 查看源码</button>
                  <button @click="handleProjectLike" :class="['h-10 px-4 rounded-lg border text-sm font-medium transition-all flex items-center gap-1.5', projectLiked ? 'border-red-200 bg-red-50 text-red-600' : 'border-gray-200 bg-white text-gray-700 hover:bg-gray-50']">
                    <img :src="projectLiked ? '/icons/like-blue.svg' : '/icons/like-grey.svg'" class="w-4 h-4 transition-transform" :class="likeAnimating ? 'scale-150' : ''" />
                    {{ formatCount(project.like_count || 0) }}
                  </button>
                </div>
              </div>
            </div>

            <div class="mt-6 pt-5 border-t border-gray-100 grid grid-cols-4 gap-4">
              <div class="flex flex-col items-center text-center">
                <div class="w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center mb-2"><img src="/icons/calendar.svg" class="w-4 h-4 text-gray-400" /></div>
                <div class="text-xs text-gray-400 mb-1">开发时间</div>
                <div class="text-sm text-gray-600">{{ projectTimeRange }}</div>
              </div>
              <div class="flex flex-col items-center text-center border-l border-gray-100">
                <div class="w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center mb-2"><img src="/icons/project-grey.svg" class="w-4 h-4" /></div>
                <div class="text-xs text-gray-400 mb-1">项目类型</div>
                <div class="text-sm text-gray-600">{{ project.project_type || '个人项目' }}</div>
              </div>
              <div class="flex flex-col items-center text-center border-l border-gray-100">
                <div class="w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center mb-2"><img src="/icons/code.svg" class="w-4 h-4" /></div>
                <div class="text-xs text-gray-400 mb-1">技术栈</div>
                <div class="text-sm text-gray-600">{{ mainTechStack.join(', ') || '暂无' }}</div>
              </div>
              <div class="flex flex-col items-center text-center border-l border-gray-100">
                <div class="w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center mb-2"><img src="/icons/update.svg" class="w-4 h-4" /></div>
                <div class="text-xs text-gray-400 mb-1">最后更新</div>
                <div class="text-sm text-gray-600">{{ lastUpdateTime }}</div>
              </div>
            </div>
          </div>

          <!-- 项目详情内容 -->
          <div class="bg-white/86 backdrop-blur-[10px] rounded-2xl border border-white shadow-[0_12px_30px_rgba(15,23,42,.06),0_1px_0_rgba(255,255,255,.9)_inset] p-5">
            <!-- 章节目录导航 -->
            <div v-if="catalogItems.length > 0" class="flex gap-6 text-sm font-semibold text-slate-400 border-b border-slate-100 overflow-x-auto">
              <div 
                v-for="item in catalogItems" 
                :key="item.anchor"
                @click="scrollToSection(item.anchor)"
                :class="[
                  'pb-3 cursor-pointer whitespace-nowrap transition-colors',
                  activeSection === item.anchor ? 'border-b-2 border-blue-500 text-blue-600' : 'hover:text-slate-600'
                ]"
              >{{ item.title }}</div>
            </div>

            <div class="py-6">
              <!-- 技术栈展示 -->
              <div v-if="project.tech_stack && project.tech_stack.length > 0" class="mb-8">
                <h2 class="text-[18px] font-bold text-slate-900 mb-4">技术栈</h2>
                <div class="flex flex-wrap gap-4">
                  <div v-for="tech in project.tech_stack" :key="tech" class="flex items-center gap-3 min-w-[150px]">
                    <div class="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-lg font-bold text-slate-600">{{ tech.charAt(0).toUpperCase() }}</div>
                    <div>
                      <div class="text-[14px] font-semibold text-slate-900">{{ tech }}</div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 项目内容（使用数据库内容渲染） -->
              <div v-if="project.content" class="project-content prose prose-slate max-w-none" v-html="processedContent"></div>
              <div v-else class="text-center py-12 text-gray-400"><p>暂无项目内容</p></div>
            </div>
          </div>

          <!-- 评论区 -->
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
                    <span :class="['cursor-pointer transition-colors flex items-center gap-1', commentLikedSet.has(c.id) ? 'text-red-500' : 'hover:text-red-500']" @click="handleCommentLike(c.id)">
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
                            <span :class="['cursor-pointer transition-colors flex items-center gap-1', commentLikedSet.has(r.id) ? 'text-red-500' : 'hover:text-red-500']" @click="handleCommentLike(r.id)">
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
        </div>

        <!-- 右侧边栏 -->
        <div class="lg:w-1/5 space-y-5">
          <!-- 作者信息 -->
          <div class="bg-white rounded-xl shadow-sm p-6 flex flex-col">
            <div class="flex flex-col items-center mb-6">
              <div class="w-[5rem] h-[5rem] rounded-full overflow-hidden flex-shrink-0 mb-3">
                <img :src="authorAvatar" alt="avatar" class="w-full h-full object-cover" />
              </div>
              <h3 class="font-bold text-xl text-gray-900 mb-1">{{ authorName }}</h3>
              <p class="text-sm text-gray-600">{{ authorPosition }}</p>
            </div>
            <div class="w-full space-y-3 mb-6">
              <div v-if="authorLocation" class="flex items-center text-sm text-gray-600"><img src="/icons/position-grey.svg" alt="地址" class="w-4 h-4 mr-2" />{{ authorLocation }}</div>
              <div v-if="authorEmail" class="flex items-center text-sm text-gray-600"><img src="/icons/email-grey.svg" alt="邮箱" class="w-4 h-4 mr-2" />{{ authorEmail }}</div>
              <div v-if="authorGithub" class="flex items-center text-sm text-gray-600"><img src="/icons/github-grey.svg" alt="GitHub" class="w-4 h-4 mr-2" />{{ authorGithub }}</div>
              <div v-if="authorExperience" class="flex items-center text-sm text-gray-600"><img src="/icons/project-grey.svg" alt="开发经验" class="w-4 h-4 mr-2" />{{ authorExperience }}</div>
            </div>
            <button @click="openModal" class="w-full py-2.5 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-all flex items-center justify-center mt-auto">
              <img src="/icons/download.svg" alt="下载" class="w-4 h-4 mr-2" />下载简历(PDF)
            </button>
          </div>

          <!-- 项目信息 -->
          <div class="bg-white/86 backdrop-blur-[10px] rounded-2xl border border-white shadow-[0_12px_30px_rgba(15,23,42,.06),0_1px_0_rgba(255,255,255,.9)_inset] p-5">
            <h3 class="font-bold text-slate-900 mb-4">项目信息</h3>
            <div class="space-y-4 text-[13px]">
              <div class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2"><img src="/icons/project-status-complete.svg" class="w-4 h-4" />项目状态</div>
                <div class="text-[#1e293b] font-medium text-right flex items-center"><span class="w-2 h-2 rounded-full mr-2" :class="statusDotClass"></span>{{ projectStatusDisplay.text }}</div>
              </div>
              <div class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2"><img src="/icons/agreement.svg" class="w-4 h-4" />开源协议</div>
                <div class="text-[#1e293b] font-medium text-right">{{ project.open_source_license || '暂无' }}</div>
              </div>
              <div class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2"><img src="/icons/typescript.svg" class="w-4 h-4" />代码语言</div>
                <div class="text-[#1e293b] font-medium text-right">{{ mainLanguage }}</div>
              </div>
              <div class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2"><img src="/icons/framework.svg" class="w-4 h-4" />主要框架</div>
                <div class="text-[#1e293b] font-medium text-right">{{ mainTechStack.join(', ') || '暂无' }}</div>
              </div>
              <div v-if="project.database_type" class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2"><img src="/icons/database.svg" class="w-4 h-4" />数据库</div>
                <div class="text-[#1e293b] font-medium text-right">{{ project.database_type }}</div>
              </div>
              <div v-if="project.deployment_platform" class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2"><img src="/icons/cloud-platform.svg" class="w-4 h-4" />部署平台</div>
                <div class="text-[#1e293b] font-medium text-right">{{ project.deployment_platform }}</div>
              </div>
            </div>
          </div>

          <!-- 项目链接 -->
          <div class="bg-white/86 backdrop-blur-[10px] rounded-2xl border border-white shadow-[0_12px_30px_rgba(15,23,42,.06),0_1px_0_rgba(255,255,255,.9)_inset] p-5">
            <h3 class="font-bold text-slate-900 mb-4">项目链接</h3>
            <div class="space-y-4 text-[13px]">
              <div v-if="project.demo_url" class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2"><img src="/icons/demo.svg" class="w-4 h-4" />在线演示</div>
                <div @click="visitDemo" class="text-blue-600 font-medium text-right text-xs break-all cursor-pointer hover:underline max-w-[150px]">{{ project.demo_url }}</div>
              </div>
              <div v-if="project.github_url" class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2"><img src="/icons/github-black.svg" class="w-4 h-4" />GitHub 仓库</div>
                <div @click="visitGithub" class="text-blue-600 font-medium text-right text-xs break-all cursor-pointer hover:underline max-w-[150px]">{{ project.github_url }}</div>
              </div>
              <div v-if="project.docs_url" class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2"><img src="/icons/manual.svg" class="w-4 h-4" />文档站点</div>
                <div @click="openExternal(project.docs_url)" class="text-blue-600 font-medium text-right text-xs break-all cursor-pointer hover:underline max-w-[150px]">{{ project.docs_url }}</div>
              </div>
              <div v-if="project.github_url" class="flex justify-between gap-4 items-center">
                <div class="text-[#64748b] flex items-center gap-2"><img src="/icons/feedback.svg" class="w-4 h-4" />问题反馈</div>
                <div @click="visitIssues" class="text-blue-600 font-medium text-right text-xs break-all cursor-pointer hover:underline max-w-[150px]">Issues</div>
              </div>
            </div>
          </div>

          <!-- 相关项目 -->
          <div class="bg-white/86 backdrop-blur-[10px] rounded-2xl border border-white shadow-[0_12px_30px_rgba(15,23,42,.06),0_1px_0_rgba(255,255,255,.9)_inset] p-5">
            <h3 class="font-bold text-slate-900 mb-4">相关项目</h3>
            <div v-if="relatedLoading" class="text-center py-4 text-gray-400 text-sm">加载中...</div>
            <div v-else-if="relatedProjects.length === 0" class="text-center py-4 text-gray-400 text-sm">暂无相关项目</div>
            <div v-else class="space-y-4">
              <div v-for="related in relatedProjects" :key="related.id" @click="goToProject(related.id)" class="flex items-start justify-between gap-3 cursor-pointer group">
                <div class="flex items-start gap-3">
                  <div class="w-8 h-8 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center group-hover:bg-blue-100 transition-colors">
                    <img src="/icons/folder.svg" class="w-4 h-4" />
                  </div>
                  <div>
                    <div class="text-[14px] font-semibold text-slate-900 group-hover:text-blue-600 transition-colors">{{ related.name }}</div>
                    <div class="text-[12px] text-slate-500 mt-1 line-clamp-1">{{ related.summary || '' }}</div>
                  </div>
                </div>
                <div class="text-slate-400 text-sm flex items-center gap-1 flex-shrink-0">
                  <img src="/icons/page-views.svg" class="w-3 h-3" />
                  {{ formatCount(related.view_count || 0) }}
                </div>
              </div>
            </div>
          </div>

          <!-- 项目统计 -->
          <div class="bg-white rounded-[1.1rem] border border-[#edf0f7] shadow-[0_6px_20px_rgba(34,60,80,0.05)] p-6">
            <h3 class="text-base font-semibold text-gray-900 mb-4">项目统计</h3>
            <div class="flex justify-between">
              <div class="flex flex-col items-center">
                <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#f6f6fb] rounded-lg flex items-center justify-center mb-2 lg:mb-3">
                  <img src="/icons/page-views.svg" alt="访问量" class="w-5 h-5 lg:w-6 lg:h-6" />
                </div>
                <div class="text-xs text-gray-900 mt-0.5 lg:mt-1">访问量</div>
                <div class="text-lg lg:text-xl font-bold text-gray-900">{{ formatCount(project.view_count || 0) }}</div>
              </div>
              <div class="flex flex-col items-center">
                <div class="w-10 h-10 lg:w-12 lg:h-12 bg-[#f6f6fb] rounded-lg flex items-center justify-center mb-2 lg:mb-3">
                  <img src="/icons/like-grey.svg" alt="点赞数" class="w-5 h-5 lg:w-6 lg:h-6" />
                </div>
                <div class="text-xs text-gray-900 mt-0.5 lg:mt-1">点赞数</div>
                <div class="text-lg lg:text-xl font-bold text-gray-900">{{ formatCount(project.like_count || 0) }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      </template>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, nextTick, onUnmounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { usePdfModal } from '../composables/usePdfModal'
import { fetchProjectById } from '../api/projects'
import { fetchSiteSettings } from '../api/site'
import { fetchProjectComments, createProjectComment, likeProjectComment, likeProject } from '../api/projectComments'
import { generateGuestName } from '../utils/guestName'

const { openModal } = usePdfModal()
const route = useRoute()
const router = useRouter()

const API_BASE = 'http://localhost:8000'

const loading = ref(true)
const error = ref(null)
const project = ref(null)
const siteSettings = ref(null)

const comments = ref([])
const commentTotal = ref(0)
const commentPage = ref(1)
const commentSort = ref('newest')
const commentLoading = ref(false)
const commentError = ref('')
const submitting = ref(false)
const hasMoreComments = ref(false)
const replyInputId = ref(null)
const replyTargetId = ref(null)
const replyTargetName = ref('')
const replyDraft = ref('')
const replySubmitting = ref(false)
const draft = ref('')
const guestName = ref('')

const projectLiked = ref(false)
const likeAnimating = ref(false)
const commentLikedSet = ref(new Set())

const relatedProjects = ref([])
const relatedLoading = ref(false)

const catalogItems = ref([])
const activeSection = ref('')

let observer = null

onMounted(async () => {
  const projectId = route.params.id
  guestName.value = generateGuestName()
  loadLikedState()

  if (!projectId) {
    error.value = '项目 ID 不存在'
    loading.value = false
    return
  }

  try {
    const [projectData, settingsData] = await Promise.all([
      fetchProjectById(projectId),
      fetchSiteSettings()
    ])

    if (projectData) {
      project.value = projectData
      document.title = `${projectData.name} - 项目详情`
      processCatalog(projectData.catalog)
      await loadComments()
      await loadRelatedProjects(projectId)
      setupSectionObserver()
    } else {
      error.value = '未找到该项目'
    }

    if (settingsData) {
      siteSettings.value = settingsData
    }
  } catch (err) {
    console.error('加载项目详情失败:', err)
    error.value = '加载失败，请稍后重试'
  } finally {
    loading.value = false
  }
})

watch(() => route.params.id, (newId) => {
  if (!newId) return
  if (observer) observer.disconnect()
  activeSection.value = ''
  guestName.value = generateGuestName()
  commentPage.value = 1
  comments.value = []
  commentTotal.value = 0
  projectLiked.value = false
  loadLikedState()
  loadProjectData()
  window.scrollTo({ top: 0, behavior: 'smooth' })
})

async function loadProjectData() {
  loading.value = true
  error.value = null
  try {
    const projectData = await fetchProjectById(route.params.id)
    if (projectData) {
      project.value = projectData
      document.title = `${projectData.name} - 项目详情`
      processCatalog(projectData.catalog)
      await loadComments()
      await loadRelatedProjects(route.params.id)
      setupSectionObserver()
    } else {
      error.value = '未找到该项目'
    }
  } catch {
    error.value = '加载失败，请稍后重试'
  } finally {
    loading.value = false
  }
}

onUnmounted(() => {
  if (observer) observer.disconnect()
})

const coverUrl = computed(() => {
  if (!project.value || !project.value.cover) {
    return 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=900&q=80'
  }
  const cover = project.value.cover
  if (cover.startsWith('http://') || cover.startsWith('https://')) return cover
  return `${API_BASE}${cover.startsWith('/') ? '' : '/'}${cover}`
})

const processedContent = computed(() => {
  if (!project.value || !project.value.content) return ''
  let html = project.value.content
  if (catalogItems.value.length > 0) {
    for (const item of catalogItems.value) {
      const escapedTitle = item.title.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
      const patterns = [
        new RegExp(`(<h1[^>]*>)(\\s*)(${escapedTitle})(\\s*)(</h1>)`, 'gi'),
        new RegExp(`(<h2[^>]*>)(\\s*)(${escapedTitle})(\\s*)(</h2>)`, 'gi'),
        new RegExp(`(<h3[^>]*>)(\\s*)(${escapedTitle})(\\s*)(</h3>)`, 'gi'),
      ]
      for (const pattern of patterns) {
        html = html.replace(pattern, `$1$2$3$4$5`.replace('$1', `<h${item.level} id="${item.anchor}" class="scroll-mt-20">`).replace('$5', `</h${item.level}>`))
      }
    }
  }
  return html
})

const projectTimeRange = computed(() => {
  if (!project.value) return ''
  const start = project.value.start_date ? formatDate(project.value.start_date) : ''
  const end = project.value.end_date ? formatDate(project.value.end_date) : '至今'
  return start && end ? `${start} - ${end}` : '暂无'
})

const lastUpdateTime = computed(() => {
  if (!project.value) return '暂无'
  return project.value.last_update ? formatDate(project.value.last_update) : '暂无'
})

const projectStatusDisplay = computed(() => {
  if (!project.value) return { text: '未知' }
  const statusMap = {
    'active': { text: '进行中' },
    'completed': { text: '已完成' },
    'paused': { text: '已暂停' },
    'archived': { text: '已归档' }
  }
  const status = project.value.status || 'active'
  return statusMap[status] || { text: status }
})

const statusDotClass = computed(() => {
  const status = project.value?.status || 'active'
  const map = { 'active': 'bg-blue-500', 'completed': 'bg-green-500', 'paused': 'bg-yellow-500', 'archived': 'bg-gray-500' }
  return map[status] || 'bg-gray-500'
})

const mainTechStack = computed(() => {
  if (!project.value || !project.value.tech_stack) return []
  return project.value.tech_stack.slice(0, 2)
})

const mainLanguage = computed(() => {
  if (!project.value || !project.value.tech_stack || project.value.tech_stack.length === 0) return '暂无'
  return project.value.tech_stack[0]
})

const authorName = computed(() => {
  return siteSettings.value?.author_name || 'Lin'
})

const authorPosition = computed(() => {
  return siteSettings.value?.description || '全栈开发 & AI 应用探索'
})

const authorEmail = computed(() => {
  return siteSettings.value?.email || ''
})

const authorGithub = computed(() => {
  const url = siteSettings.value?.github_url || ''
  return url.replace(/^https?:\/\//, '')
})

const authorLocation = computed(() => {
  return siteSettings.value?.location || '中国 · 深圳'
})

const authorExperience = computed(() => {
  return '5 年开发经验'
})

const authorAvatar = computed(() => {
  return siteSettings.value?.admin_avatar || '/images/avatar.png'
})

function generateAnchor(title, index) {
  return `catalog-${index}-${encodeURIComponent(title)}`
}

function processCatalog(catalog) {
  if (!catalog || !catalog.length) {
    catalogItems.value = []
    return
  }
  catalogItems.value = catalog.map((item, index) => ({
    anchor: generateAnchor(item.title, index),
    title: item.title,
    level: item.level || 1,
    depth: 0
  }))
}

function scrollToSection(anchor) {
  const element = document.getElementById(anchor)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth', block: 'start' })
    activeSection.value = anchor
  } else {
    const contentEl = document.querySelector('.project-content')
    if (contentEl) {
      const headings = contentEl.querySelectorAll('h1, h2, h3')
      for (const h of headings) {
        if (h.textContent.trim() === catalogItems.value.find(c => c.anchor === anchor)?.title) {
          h.id = anchor
          h.classList.add('scroll-mt-20')
          h.scrollIntoView({ behavior: 'smooth', block: 'start' })
          activeSection.value = anchor
          break
        }
      }
    }
  }
}

function setupSectionObserver() {
  if (observer) observer.disconnect()
  nextTick(() => {
    const contentEl = document.querySelector('.project-content')
    if (!contentEl) return
    const headings = contentEl.querySelectorAll('h1[id], h2[id], h3[id]')
    if (headings.length === 0) return

    observer = new IntersectionObserver((entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          activeSection.value = entry.target.id
        }
      }
    }, { rootMargin: '-80px 0px -60% 0px', threshold: 0 })

    headings.forEach((h) => observer.observe(h))
  })
}

async function loadComments() {
  const projectId = route.params.id
  if (!projectId) return
  commentLoading.value = true
  commentError.value = ''
  try {
    const data = await fetchProjectComments(projectId, { page: commentPage.value, size: 10, sort: commentSort.value })
    if (data) {
      comments.value = commentPage.value === 1 ? (data.comments || []) : [...comments.value, ...(data.comments || [])]
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
  if (!draft.value.trim()) { commentError.value = '请输入评论内容'; return }
  if (draft.value.length > 2000) { commentError.value = '评论内容不能超过2000个字符'; return }
  submitting.value = true
  commentError.value = ''
  try {
    await createProjectComment(route.params.id, { content: draft.value, guest_name: guestName.value })
    draft.value = ''
    commentPage.value = 1
    comments.value = []
    await loadComments()
  } catch (err) {
    commentError.value = err.response?.data?.detail || '提交评论失败'
  } finally {
    submitting.value = false
  }
}

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

async function submitReply(parentCommentId, replyToId = null, replyToName = null) {
  if (!replyDraft.value.trim()) { commentError.value = '请输入回复内容'; return }
  replySubmitting.value = true
  commentError.value = ''
  try {
    await createProjectComment(route.params.id, {
      content: replyDraft.value,
      guest_name: guestName.value,
      parent_id: parentCommentId,
      reply_to_id: replyToId,
      reply_to_name: replyToName
    })
    replyDraft.value = ''
    replyInputId.value = null
    replyTargetId.value = null
    replyTargetName.value = ''
    commentPage.value = 1
    comments.value = []
    await loadComments()
  } catch (err) {
    commentError.value = err.response?.data?.detail || '提交回复失败'
  } finally {
    replySubmitting.value = false
  }
}

async function handleCommentLike(commentId) {
  const key = `comment_liked_${commentId}`
  if (commentLikedSet.value.has(commentId)) return
  try {
    const result = await likeProjectComment(commentId)
    commentLikedSet.value.add(commentId)
    localStorage.setItem(key, '1')
    for (const c of comments.value) {
      if (c.id === commentId) {
        c.like_count = (c.like_count || 0) + 1
        break
      }
      if (c.replies) {
        for (const r of c.replies) {
          if (r.id === commentId) {
            r.like_count = (r.like_count || 0) + 1
            break
          }
        }
      }
    }
  } catch (err) {
    if (err.response?.status === 401) {
      commentError.value = '请先登录后再进行点赞操作'
    }
  }
}

async function handleProjectLike() {
  if (projectLiked.value) return
  try {
    likeAnimating.value = true
    const result = await likeProject(route.params.id)
    if (result) {
      projectLiked.value = true
      project.value.like_count = result.like_count || (project.value.like_count || 0) + 1
      localStorage.setItem(`project_liked_${route.params.id}`, '1')
    }
    setTimeout(() => { likeAnimating.value = false }, 300)
  } catch (err) {
    likeAnimating.value = false
    if (err.response?.status === 401) {
      commentError.value = '请先登录后再进行点赞操作'
    }
  }
}

function loadLikedState() {
  const projectId = route.params.id
  projectLiked.value = !!localStorage.getItem(`project_liked_${projectId}`)
  const likedComments = JSON.parse(localStorage.getItem('comment_liked_ids') || '[]')
  commentLikedSet.value = new Set(likedComments)
}

async function loadRelatedProjects(projectId) {
  const cacheKey = `related_projects_${projectId}`
  const cached = sessionStorage.getItem(cacheKey)
  if (cached) {
    try { relatedProjects.value = JSON.parse(cached); return } catch { sessionStorage.removeItem(cacheKey) }
  }

  relatedLoading.value = true
  try {
    const response = await fetch(`${API_BASE}/api/v1/projects/?size=100`)
    if (response.ok) {
      const data = await response.json()
      if (data.code === 200 && data.data) {
        let projects = data.data.projects || []
        const currentProject = project.value
        let related = []

        if (currentProject && currentProject.category_id) {
          related = projects.filter(p => p.id !== parseInt(projectId) && p.category_id === currentProject.category_id)
        }

        if (related.length < 3) {
          const byViews = projects
            .filter(p => p.id !== parseInt(projectId))
            .sort((a, b) => (b.view_count || 0) - (a.view_count || 0))
            .slice(0, 3)
          for (const p of byViews) {
            if (related.length < 3 && !related.find(r => r.id === p.id)) related.push(p)
          }
        }

        relatedProjects.value = related.slice(0, 3)
        sessionStorage.setItem(cacheKey, JSON.stringify(relatedProjects.value))
      } else {
        relatedProjects.value = []
      }
    }
  } catch {
    relatedProjects.value = []
  } finally {
    relatedLoading.value = false
  }
}

function goToProject(id) {
  router.push(`/project/${id}`)
}

const avatarColors = ['bg-blue-100 text-blue-600','bg-green-100 text-green-600','bg-purple-100 text-purple-600','bg-pink-100 text-pink-600','bg-yellow-100 text-yellow-600','bg-red-100 text-red-600','bg-indigo-100 text-indigo-600','bg-teal-100 text-teal-600']

function getAvatarColor(name) {
  let hash = 0
  for (let i = 0; i < (name || '').length; i++) hash = name.charCodeAt(i) + ((hash << 5) - hash)
  return avatarColors[Math.abs(hash) % avatarColors.length]
}

function formatDate(dateStr) {
  if (!dateStr) return ''
  const date = new Date(dateStr)
  return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}`
}

function formatCount(num) {
  if (num >= 1000) return (num / 1000).toFixed(1).replace(/\.0$/, '') + 'k'
  return num.toString()
}

function handleImageError(event) {
  event.target.src = 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=900&q=80'
}

function visitDemo() {
  if (project.value?.demo_url) window.open(project.value.demo_url, '_blank')
}

function visitGithub() {
  if (project.value?.github_url) window.open(project.value.github_url, '_blank')
}

function visitIssues() {
  if (project.value?.github_url) window.open(`${project.value.github_url.replace(/\/$/, '')}/issues`, '_blank')
}

function openExternal(url) {
  if (url) window.open(url, '_blank')
}
</script>

<style scoped>
.page-container { background: #ffffff; padding: 1.75rem; }

.project-content :deep(h1),
.project-content :deep(h2),
.project-content :deep(h3) { scroll-margin-top: 5rem; }

.project-content :deep(img) { max-width: 100%; height: auto; border-radius: 0.5rem; margin: 1rem 0; }
.project-content :deep(pre) { background: #f8fafc; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; font-size: 0.875rem; }
.project-content :deep(code) { background: #f1f5f9; padding: 0.125rem 0.375rem; border-radius: 0.25rem; font-size: 0.875rem; }
.project-content :deep(pre code) { background: none; padding: 0; }
.project-content :deep(a) { color: #2563eb; text-decoration: underline; }
.project-content :deep(ul), .project-content :deep(ol) { padding-left: 1.5rem; margin: 0.5rem 0; }
.project-content :deep(li) { margin: 0.25rem 0; }
.project-content :deep(p) { margin: 0.5rem 0; line-height: 1.75; }
.project-content :deep(table) { width: 100%; border-collapse: collapse; margin: 1rem 0; }
.project-content :deep(th), .project-content :deep(td) { border: 1px solid #e2e8f0; padding: 0.5rem 0.75rem; text-align: left; }
.project-content :deep(th) { background: #f8fafc; font-weight: 600; }

.line-clamp-1 { display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical; overflow: hidden; }

@media (max-width: 768px) {
  .page-container { padding: 0.75rem 0.75rem 1rem; }
  .page-container > .min-h-screen > .flex.items-center.justify-between.mb-5 { margin-bottom: 0.7rem; }
  .page-container > .min-h-screen > .flex.items-center.justify-between.mb-5 .text-sm.text-slate-400.font-medium { font-size: 0.7rem; line-height: 1.4; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row { gap: 0.75rem; }
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 { min-width: 0; }
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 { padding: 0.9rem; border-radius: 1rem; }
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 .grid.grid-cols-\[45\%_55\%\] { grid-template-columns: 1fr; gap: 0.9rem; }
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 .rounded-xl.overflow-hidden.bg-slate-900.h-\[350px\] { height: 11.5rem; border-radius: 1rem; }
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 .flex.flex-col.justify-between { gap: 0.65rem; }
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 h1 { font-size: 1.3rem; line-height: 1.25; }
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 p { font-size: 0.8rem; line-height: 1.7; }
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 .mt-6.flex.items-center.gap-3 { margin-top: 0.9rem; flex-wrap: wrap; gap: 0.5rem; }
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .bg-white.rounded-xl.shadow-sm.p-6 .mt-6.flex.items-center.gap-3 button { flex: 1 1 calc(50% - 0.25rem); min-width: 0; justify-content: center; padding: 0.8rem 0.9rem; font-size: 0.78rem; }
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mt-6.pt-5.border-t.border-gray-100.grid.grid-cols-4.gap-4 { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.75rem 0.5rem; margin-top: 1rem; padding-top: 1rem; }
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:flex-1 > .mt-6.pt-5.border-t.border-gray-100.grid.grid-cols-4.gap-4 > div:nth-child(n+2) { border-left: 0; }
  .page-container > .min-h-screen > .flex.flex-col.lg\:flex-row > .lg\:w-1\/5 { display: none; }
}
</style>
