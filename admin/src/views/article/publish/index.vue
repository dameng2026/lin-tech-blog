<!-- 文章发布页面 -->
<template>
  <div class="article-publish-page">
    <div>
      <div class="max-w-250 mx-auto my-5">
        <!-- 文章标题、类型 -->
        <div class="p-5 mb-5 bg-[var(--default-box-color)] rounded-xl shadow-sm border border-[var(--art-card-border)]">
          <ElRow :gutter="10">
            <ElCol :span="18">
              <ElInput
                v-model.trim="articleName"
                placeholder="请输入文章标题（最多100个字符）"
                maxlength="100"
              />
            </ElCol>
            <ElCol :span="6">
              <ElSelect v-model="articleType" placeholder="请选择文章类型" filterable>
                <ElOption
                  v-for="item in articleTypes"
                  :key="item.id"
                  :label="item.name"
                  :value="item.id"
                />
              </ElSelect>
            </ElCol>
          </ElRow>

          <!-- 转载URL -->
          <ElRow class="mt-2.5">
            <ElCol :span="24">
              <ElInput
                v-model="repostUrl"
                placeholder="转载URL（填写后自动标记为转载，为空则标记为原创）"
                clearable
                @blur="handleRepostUrlChange"
              />
            </ElCol>
          </ElRow>
        </div>

        <!-- 标签 -->
        <div class="p-5 mb-5 bg-[var(--default-box-color)] rounded-xl shadow-sm border border-[var(--art-card-border)]">
          <ElRow>
            <ElCol :span="24">
              <div class="flex flex-wrap items-center gap-2 p-2 border border-[var(--default-border)] rounded-lg min-h-10">
                <ElTag
                  v-for="(tag, index) in tags"
                  :key="index"
                  closable
                  size="small"
                  type="info"
                  @close="removeTag(index)"
                >
                  {{ tag }}
                </ElTag>
                <ElInput
                  v-model="tagInput"
                  placeholder="输入标签后按回车或逗号添加"
                  size="small"
                  class="flex-1 min-w-40"
                  @keydown="handleTagInputKeydown"
                  @blur="handleTagInputBlur"
                />
              </div>
            </ElCol>
          </ElRow>
        </div>

        <!-- 富文本编辑器 -->
        <ArtWangEditor class="mt-2.5" v-model="editorHtml" />

        <!-- 目录管理 -->
        <div class="p-5 mt-5 bg-[var(--default-box-color)] rounded-xl shadow-sm border border-[var(--art-card-border)]">
          <h2 class="mb-5 text-xl font-medium">文章目录</h2>

          <div v-if="catalog.length > 0" class="mb-4 space-y-2">
            <div
              v-for="(item, index) in catalog"
              :key="index"
              class="flex items-center gap-2 py-2 px-3 rounded-lg bg-gray-50 hover:bg-gray-100 transition-colors group"
              :style="{ marginLeft: (item.level - 1) * 24 + 'px' }"
            >
              <div class="flex items-center gap-1">
                <ElIcon class="cursor-move text-gray-400 hover:text-gray-600"><Link /></ElIcon>
                <span
                  v-if="catalogEditingIndex !== index"
                  class="text-sm flex-1 truncate"
                  @click="startEditCatalog(index)"
                >{{ item.title }}</span>
                <ElInput
                  v-else
                  v-model="catalog[index].title"
                  :class="['flex-1', `catalog-item-input-${index}`]"
                  size="small"
                  @blur="finishEditCatalog"
                  @keyup.enter="finishEditCatalog"
                  ref="editInputRef"
                  placeholder="请输入章节标题"
                />
              </div>
              <div class="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                <ElButton
                  text
                  size="small"
                  @click="indentCatalog(index)"
                  :disabled="item.level >= 3"
                  :class="{ 'text-gray-300 cursor-not-allowed': item.level >= 3 }"
                >
                  <ElIcon class="text-blue-500"><CirclePlus /></ElIcon>
                </ElButton>
                <ElButton
                  text
                  size="small"
                  @click="outdentCatalog(index)"
                  :disabled="item.level <= 1"
                  :class="{ 'text-gray-300 cursor-not-allowed': item.level <= 1 }"
                >
                  <ElIcon class="text-blue-500"><Minus /></ElIcon>
                </ElButton>
                <ElButton
                  text
                  size="small"
                  @click="moveCatalogUp(index)"
                  :disabled="index === 0"
                  :class="{ 'text-gray-300 cursor-not-allowed': index === 0 }"
                >
                  <ElIcon class="text-blue-500"><ArrowUp /></ElIcon>
                </ElButton>
                <ElButton
                  text
                  size="small"
                  @click="moveCatalogDown(index)"
                  :disabled="index === catalog.length - 1"
                  :class="{ 'text-gray-300 cursor-not-allowed': index === catalog.length - 1 }"
                >
                  <ElIcon class="text-blue-500"><ArrowDown /></ElIcon>
                </ElButton>
                <ElButton
                  text
                  size="small"
                  @click="startEditCatalog(index)"
                  v-if="catalogEditingIndex !== index"
                >
                  <ElIcon class="text-gray-500"><Edit /></ElIcon>
                </ElButton>
                <ElButton text size="small" type="danger" @click="removeCatalogItem(index)">
                  <ElIcon><Close /></ElIcon>
                </ElButton>
              </div>
            </div>
          </div>

          <div class="flex gap-2">
            <ElButton
              size="small"
              type="primary"
              @click="generateCatalog"
              :loading="catalogLoading"
              :disabled="catalogLoading"
            >
              <ElIcon><MagicStick /></ElIcon>
              自动获取章节
            </ElButton>
            <ElButton size="small" @click="clearCatalog">清空目录</ElButton>
          </div>

          <div class="mt-4">
            <ElButton size="small" @click="addCatalogItem">
              <ElIcon><Plus /></ElIcon>
              添加章节
            </ElButton>
          </div>
        </div>

        <!-- 自动获取章节弹窗 -->
        <ElDialog
          v-model="showCatalogModal"
          title="自动获取章节"
          :closable="!catalogLoading && !!catalogError"
          :mask-closable="!catalogLoading && !!catalogError"
          :footer="null"
          width="480px"
        >
          <div v-if="!catalogError" class="flex flex-col items-center py-8">
            <div class="relative w-20 h-20 mb-6">
              <div class="absolute inset-0 rounded-full bg-blue-100 animate-pulse"></div>
              <div class="absolute inset-2 rounded-full bg-blue-500 flex items-center justify-center">
                <ElIcon class="text-white text-2xl"><MagicStick /></ElIcon>
              </div>
              <div class="absolute -top-1 -right-1 w-6 h-6 bg-green-500 rounded-full animate-ping"></div>
            </div>
            <p class="text-lg font-medium text-gray-800 mb-2">{{ catalogStatus }}</p>
            <div class="mt-6 w-full">
              <div class="flex justify-between text-sm text-gray-500 mb-2">
                <span>{{ catalogStageName }}</span>
                <span>{{ catalogProgress }}%</span>
              </div>
              <div class="h-3 bg-gray-200 rounded-full overflow-hidden">
                <div
                  class="h-full bg-gradient-to-r from-blue-500 to-cyan-500 rounded-full transition-all duration-700 ease-out"
                  :style="{ width: catalogProgress + '%' }"
                ></div>
              </div>
            </div>
            <p class="mt-4 text-xs text-gray-400">正在处理第 {{ catalogStage }} / {{ catalogTotalStages }} 阶段</p>
          </div>

          <div v-else class="flex flex-col items-center py-8">
            <div class="w-16 h-16 mb-6 rounded-full bg-red-100 flex items-center justify-center">
              <ElIcon class="text-red-500 text-3xl"><WarningFilled /></ElIcon>
            </div>
            <p class="text-lg font-medium text-gray-800 mb-2">操作失败</p>
            <p class="text-gray-500 text-center mb-6">{{ catalogError }}</p>
            <div class="flex gap-3">
              <ElButton @click="closeCatalogModal">取消</ElButton>
              <ElButton type="primary" @click="retryGenerateCatalog">重试</ElButton>
            </div>
          </div>
        </ElDialog>

        <div class="p-5 mt-5 bg-[var(--default-box-color)] rounded-xl shadow-sm border border-[var(--art-card-border)]">
          <h2 class="mb-5 text-xl font-medium">发布设置</h2>
          <ElForm>
            <ElFormItem label="封面">
              <div class="mt-2.5 space-y-3">
                <div class="flex gap-3">
                  <ElUpload
                     :show-file-list="false"
                     :before-upload="beforeUpload"
                     :http-request="handleFileUpload"
                     ref="uploadRef"
                   >
                    <div
                      v-if="!cover"
                      class="flex-cc flex-col w-65 h-40 border border-dashed border-[#d9d9d9] rounded-md"
                    >
                      <ElIcon class="!text-xl !text-g-600"><Plus /></ElIcon>
                      <div class="mt-2 text-sm text-g-600">点击上传封面</div>
                    </div>
                    <img v-else :src="cover" class="block w-65 h-40 object-cover rounded-md" />
                  </ElUpload>
                  <div v-if="cover" class="flex flex-col gap-2">
                    <ElButton size="small" @click="cover = ''">移除封面</ElButton>
                    <ElButton size="small" @click="triggerUpload">重新上传</ElButton>
                  </div>
                </div>
                <div class="flex items-center gap-2">
                  <ElInput
                    v-model="coverUrlInput"
                    placeholder="或输入图片URL链接"
                    size="small"
                    clearable
                    class="flex-1"
                  />
                  <ElButton size="small" type="primary" @click="handleUrlUpload" :disabled="!coverUrlInput">确认</ElButton>
                </div>
                <div class="text-xs text-g-700">建议尺寸 16:9，jpg/png 格式</div>
              </div>
            </ElFormItem>
            <ElFormItem label="可见">
              <ElSwitch v-model="visible" />
            </ElFormItem>
          </ElForm>

          <div class="flex justify-end">
            <ElButton type="primary" @click="submit" class="w-25" :loading="isSubmitting">
              {{ pageMode === PageModeEnum.Edit ? '保存' : '发布' }}
            </ElButton>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { Plus, Link, MagicStick, Close, WarningFilled, Edit, ArrowUp, ArrowDown, Minus, CirclePlus } from '@element-plus/icons-vue'
  import { useUserStore } from '@/store/modules/user'
  import EmojiText from '@/utils/ui/emojo'
  import { PageModeEnum } from '@/enums/formEnum'
  import { fetchCategories } from '@/api/taxonomy'
  import { createArticle, updateArticle, fetchArticle } from '@/api/articles'
  import { useCommon } from '@/hooks/core/useCommon'

  defineOptions({ name: 'ArticlePublish' })

  interface ArticleType {
    id: number
    name: string
  }

  interface CatalogItem {
    level: number
    title: string
  }

  const MAX_IMAGE_SIZE = 2
  const EMPTY_EDITOR_CONTENT = '<p><br></p>'

  const route = useRoute()
const router = useRouter()
  const userStore = useUserStore()
  const { accessToken } = userStore

  const pageMode = ref<PageModeEnum>(PageModeEnum.Add)
  const articleName = ref('')
  const articleType = ref<number>()
  const articleTypes = ref<ArticleType[]>([])
  const editorHtml = ref('')
  const createDate = ref('')
  const cover = ref('')
  const visible = ref(true)
  const coverUrlInput = ref('')
  const repostUrl = ref('')
  const uploadRef = ref<InstanceType<typeof ElUpload> | null>(null)
  const catalog = ref<CatalogItem[]>([])
  const catalogLoading = ref(false)
  const catalogStatus = ref('')
  const catalogError = ref('')
  const showCatalogModal = ref(false)
  const catalogProgress = ref(0)
  const catalogStage = ref(0)
  const catalogTotalStages = ref(5)
  const catalogStageName = ref('')
  const catalogEditingIndex = ref<number>(-1)
  const editInputRef = ref<InstanceType<typeof ElInput> | null>(null)
  const isSubmitting = ref(false)
  const articleId = ref<number | null>(null)
  const tags = ref<string[]>([])
  const tagInput = ref('')

  const initPageMode = () => {
    const { id } = route.query
    pageMode.value = id ? PageModeEnum.Edit : PageModeEnum.Add

    if (pageMode.value === PageModeEnum.Edit) {
      getArticleDetail()
    } else {
      createDate.value = formatDate(useNow().value)
    }
  }

  const getArticleTypes = async () => {
    try {
      const categories = await fetchCategories()
      if (categories && Array.isArray(categories)) {
        articleTypes.value = categories.map((cat: any) => ({
          id: cat.id,
          name: cat.name
        }))
      }
    } catch (error) {
      console.error('获取文章分类失败:', error)
      ElMessage.error('获取文章分类失败')
    }
  }

  const getArticleDetail = async () => {
    const { id } = route.query
    if (!id) return
    try {
      const res = await fetchArticle(Number(id))
      if (res) {
        articleId.value = res.id
        articleName.value = res.title || ''
        editorHtml.value = res.content || ''
        cover.value = res.cover || ''
        visible.value = res.is_published !== false
        repostUrl.value = res.repost_url || ''
        catalog.value = (res.catalog || []).map((item: any) => ({
          level: item.level || 1,
          title: item.title || ''
        }))
        if (res.category) {
          const matched = articleTypes.value.find((t: any) => t.name === res.category)
          if (matched) {
            articleType.value = matched.id
          }
        }
      }
    } catch (error) {
      console.error('获取文章详情失败:', error)
      ElMessage.error('获取文章详情失败')
    }
  }

  const stripHtml = (html: string): string => {
    const div = document.createElement('div')
    div.innerHTML = html
    return div.textContent || div.innerText || ''
  }

  const formatDate = (date: string | Date): string => {
    return useDateFormat(date, 'YYYY-MM-DD').value
  }

  const validateArticle = (): boolean => {
    if (!articleName.value.trim()) {
      ElMessage.error('请输入文章标题')
      return false
    }

    if (!articleType.value) {
      ElMessage.error('请选择文章类型')
      return false
    }

    if (!editorHtml.value || editorHtml.value === EMPTY_EDITOR_CONTENT) {
      ElMessage.error('请输入文章内容')
      return false
    }

    if (!cover.value) {
      ElMessage.error('请上传封面图片')
      return false
    }

    return true
  }

  const cleanCodeContent = (content: string): string => {
    return content.replace(/(\s*)<\/code>/g, '</code>')
  }

  const stripImages = (html: string): string => {
    return html.replace(/<img[^>]*>/gi, '')
  }

  const addTag = () => {
    const raw = tagInput.value
    const parts = raw.split(/[,，\n]/).map(s => s.trim()).filter(Boolean)
    for (const part of parts) {
      if (part && !tags.value.includes(part)) {
        tags.value.push(part)
      }
    }
    tagInput.value = ''
  }

  const removeTag = (index: number) => {
    tags.value.splice(index, 1)
  }

  const handleTagInputKeydown = (e: Event | KeyboardEvent) => {
    const evt = e as KeyboardEvent
    if (evt.key === 'Enter' || evt.key === ',') {
      evt.preventDefault()
      addTag()
    }
  }

  const handleTagInputBlur = () => {
    if (tagInput.value.trim()) {
      addTag()
    }
  }

  const buildArticlePayload = (): Api.Article.ArticleCreate => {
    const categoryItem = articleTypes.value.find(item => item.id === articleType.value)
    const plainText = stripHtml(editorHtml.value)
    const isRepost = !!repostUrl.value.trim()

    return {
      title: articleName.value.trim(),
      cover: cover.value || undefined,
      summary: plainText.slice(0, 200),
      content: cleanCodeContent(editorHtml.value),
      category: categoryItem?.name,
      tags: tags.value.length > 0 ? tags.value : [],
      catalog: catalog.value.length > 0 ? catalog.value.map(item => ({
        level: String(item.level),
        title: item.title
      })) : [],
      source_type: isRepost ? 'repost' : 'original',
      repost_url: isRepost ? repostUrl.value.trim() : undefined,
      allow_comment: true
    }
  }

  const addArticle = async () => {
    if (!validateArticle()) return

    isSubmitting.value = true
    try {
      const payload = buildArticlePayload()
      const result = await createArticle(payload)
      if (result) {
        ElMessage.success('文章发布成功！')
        setTimeout(() => {
          router.push({ name: 'ArticleList' })
        }, 800)
      }
    } catch (error: any) {
      console.error('发布文章失败:', error)
      ElMessage.error(error?.msg || '发布文章失败，请稍后重试')
    } finally {
      isSubmitting.value = false
    }
  }

  const editArticle = async () => {
    if (!validateArticle()) return

    if (!articleId.value) {
      ElMessage.error('文章ID不存在')
      return
    }

    isSubmitting.value = true
    try {
      const payload = buildArticlePayload()
      const result = await updateArticle(articleId.value, payload)
      if (result) {
        ElMessage.success('文章保存成功！')
        setTimeout(() => {
          router.push({ name: 'ArticleList' })
        }, 800)
      }
    } catch (error: any) {
      console.error('保存文章失败:', error)
      ElMessage.error(error?.msg || '保存文章失败，请稍后重试')
    } finally {
      isSubmitting.value = false
    }
  }

  const submit = () => {
    if (pageMode.value === PageModeEnum.Edit) {
      editArticle()
    } else {
      addArticle()
    }
  }

  const handleFileUpload = async (options: any) => {
    const file = options.file as File
    try {
      const formData = new FormData()
      formData.append('file', file)
      const { default: request } = await import('@/utils/http')
      const res: any = await request.post({
        url: '/v1/upload/image',
        params: formData,
        headers: { 'Content-Type': 'multipart/form-data' }
      })
      if (res.code === 200 && res.data?.url) {
        cover.value = res.data.url
        ElMessage.success(`封面上传成功 ${EmojiText[200]}`)
      } else if (res.url) {
        cover.value = res.url
        ElMessage.success(`封面上传成功 ${EmojiText[200]}`)
      } else {
        ElMessage.error(`封面上传失败`)
      }
    } catch (error) {
      console.error('封面上传失败:', error)
      ElMessage.error(`封面上传失败 ${EmojiText[500]}`)
    }
  }

  const triggerUpload = () => {
    uploadRef.value?.$el.querySelector('input[type=file]')?.click()
  }

  const handleUrlUpload = () => {
    const url = coverUrlInput.value.trim()
    if (!url) {
      ElMessage.warning('请输入图片URL')
      return
    }

    try {
      new URL(url)
    } catch {
      ElMessage.warning('请输入有效的图片URL')
      return
    }

    const imageExtPattern = /\.(jpg|jpeg|png|gif|svg|webp|awebp|bmp|ico)([\?#&]|$)/i
    if (!imageExtPattern.test(url)) {
      ElMessage.warning('请输入有效的图片URL（支持 jpg/png/gif/svg/webp 格式）')
      return
    }

    cover.value = url
    coverUrlInput.value = ''
    ElMessage.success('封面已设置')
  }

  const handleRepostUrlChange = () => {
    const url = repostUrl.value.trim()
    if (url) {
      const originalType = articleTypes.value.find(item => item.name === '原创')
      const repostType = articleTypes.value.find(item => item.name === '转载')
      if (repostType) {
        articleType.value = repostType.id
      }
    } else {
      const originalType = articleTypes.value.find(item => item.name === '原创')
      if (originalType) {
        articleType.value = originalType.id
      }
    }
  }

  const beforeUpload = (file: File): boolean => {
    const isImage = file.type.startsWith('image/')
    const isLt2M = file.size / 1024 / 1024 < MAX_IMAGE_SIZE

    if (!isImage) {
      ElMessage.error('只能上传图片文件')
      return false
    }

    if (!isLt2M) {
      ElMessage.error(`图片大小不能超过 ${MAX_IMAGE_SIZE}MB`)
      return false
    }

    return true
  }

  const addCatalogItem = () => {
    catalog.value.push({ level: 1, title: '' })
  }

  const removeCatalogItem = (index: number) => {
    catalog.value.splice(index, 1)
  }

  const clearCatalog = () => {
    catalog.value = []
    catalogEditingIndex.value = -1
  }

  const startEditCatalog = (index: number) => {
    catalogEditingIndex.value = index
    setTimeout(() => {
      const inputEl = document.querySelector(`.catalog-item-input-${index}`) as HTMLInputElement
      if (inputEl) {
        inputEl.focus()
        inputEl.select()
      }
    }, 0)
  }

  const finishEditCatalog = () => {
    catalogEditingIndex.value = -1
  }

  const indentCatalog = (index: number) => {
    if (catalog.value[index] && catalog.value[index].level < 3) {
      catalog.value[index].level++
    }
  }

  const outdentCatalog = (index: number) => {
    if (catalog.value[index] && catalog.value[index].level > 1) {
      catalog.value[index].level--
    }
  }

  const moveCatalogUp = (index: number) => {
    if (index > 0) {
      const temp = catalog.value[index]
      catalog.value[index] = catalog.value[index - 1]
      catalog.value[index - 1] = temp
    }
  }

  const moveCatalogDown = (index: number) => {
    if (index < catalog.value.length - 1) {
      const temp = catalog.value[index]
      catalog.value[index] = catalog.value[index + 1]
      catalog.value[index + 1] = temp
    }
  }

  const generateCatalog = async () => {
    if (!editorHtml.value) {
      ElMessage.warning('请先输入文章内容')
      return
    }

    catalogLoading.value = true
    catalogStatus.value = '正在预处理内容...'
    catalogStageName.value = '准备中'
    catalogProgress.value = 0
    catalogStage.value = 1
    catalogError.value = ''
    showCatalogModal.value = true

    const cleanContent = stripImages(editorHtml.value)

    if (!cleanContent.trim() || cleanContent === EMPTY_EDITOR_CONTENT) {
      catalogError.value = '文章中无可分析的文本内容（图片已过滤），请填写文字后重试'
      catalogLoading.value = false
      return
    }

    try {
      const response = await fetch('/api/v1/catalog/generate-stream', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken}`
        },
        body: JSON.stringify({ content: cleanContent })
      })

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`)
      }

      const reader = response.body?.getReader()
      if (!reader) {
        throw new Error('无法读取服务器响应')
      }

      const decoder = new TextDecoder()
      let buffer = ''
      let resultCatalog: any[] = []

      while (true) {
        const { done, value } = await reader.read()
        if (done) break

        buffer += decoder.decode(value, { stream: true })

        const parts = buffer.split('\n\n')
        buffer = parts.pop() || ''

        for (const part of parts) {
          const lines = part.split('\n')
          let eventType = ''
          let dataStr = ''

          for (const line of lines) {
            if (line.startsWith('event: ')) {
              eventType = line.slice(7)
            } else if (line.startsWith('data: ')) {
              dataStr = line.slice(6)
            }
          }

          if (!dataStr) continue

          try {
            const eventData = JSON.parse(dataStr)

            if (eventType === 'progress') {
              catalogProgress.value = eventData.progress
              catalogStageName.value = eventData.stage_name || ''
              catalogStatus.value = eventData.stage_name || '处理中...'
            } else if (eventType === 'complete') {
              resultCatalog = eventData.catalog || []
              catalogTotalStages.value = eventData.total_stages || 5
              catalogProgress.value = 100
              catalogStatus.value = '完成！'

              if (resultCatalog.length > 0) {
                catalog.value = resultCatalog.map((item: any) => ({
                  level: item.level || 1,
                  title: item.title || ''
                }))
              }

              showCatalogModal.value = false

              if (resultCatalog.length > 0) {
                ElMessage.success(`已提取 ${resultCatalog.length} 个章节`)
              } else {
                ElMessage.info('未检测到章节结构，请手动添加')
              }
            }
          } catch (parseError) {
            console.warn('SSE 数据解析失败:', parseError)
          }
        }
      }
    } catch (error: any) {
      console.error('生成目录失败:', error)
      catalogError.value = error.message || '生成目录失败，请稍后重试'
    } finally {
      catalogLoading.value = false
    }
  }

  const closeCatalogModal = () => {
    showCatalogModal.value = false
    catalogError.value = ''
    catalogStatus.value = ''
    catalogProgress.value = 0
  }

  const retryGenerateCatalog = () => {
    catalogError.value = ''
    catalogProgress.value = 0
    generateCatalog()
  }

  const { scrollToTop } = useCommon()

  onMounted(() => {
    scrollToTop()
    getArticleTypes()
    initPageMode()
  })
</script>

<style scoped>
.article-publish-page [class*="rounded-xl"][class*="shadow-sm"] {
  transition: all 0.2s ease;
}
.article-publish-page [class*="rounded-xl"][class*="shadow-sm"]:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
</style>
