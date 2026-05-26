<!-- 文章详情页面 -->
<template>
  <div class="article-detail page-content">
    <div class="max-w-200 mx-auto mt-15">
      <div class="bg-[var(--default-box-color)] rounded-xl shadow-sm border border-[var(--art-card-border)] p-8">
        <h1 class="text-3xl font-semibold">{{ articleTitle }}</h1>
        <div class="mt-12.5 markdown-body" v-highlight v-html="articleHtml"></div>
      </div>
    </div>
    <ArtBackToTop />
  </div>
</template>

<script setup lang="ts">
  import '@/assets/styles/core/md.scss'
  import '@/assets/styles/custom/one-dark-pro.scss'
  import { useCommon } from '@/hooks/core/useCommon'
  import { fetchArticle } from '@/api/articles'

  defineOptions({ name: 'ArticleDetail' })

  const route = useRoute()
  const articleId = computed(() => Number(route.params.id))
  const articleTitle = ref('')
  const articleHtml = shallowRef('')
  const articleMeta = ref<Record<string, any>>({})
  const loading = ref(false)
  const error = ref<string | null>(null)

  const getArticleDetail = async () => {
    if (!articleId.value) return

    loading.value = true
    error.value = null

    try {
      const res = await fetchArticle(articleId.value)
      if (res) {
        articleTitle.value = res.title || ''
        articleHtml.value = res.content || ''
        articleMeta.value = res
      }
    } catch (err) {
      error.value = '文章加载失败'
      console.error('获取文章详情失败:', err)
    } finally {
      loading.value = false
    }
  }

  const { scrollToTop } = useCommon()

  onMounted(() => {
    scrollToTop()
    getArticleDetail()
  })
</script>

<style lang="scss" scoped>
  .article-detail {
    :deep(.markdown-body) {
      margin-top: 60px;

      img {
        width: 100%;
        border: 1px solid var(--art-gray-200);
      }

      pre {
        position: relative;

        &:hover {
          .copy-button {
            opacity: 1;
          }
        }

        &::before {
          position: absolute;
          top: 0;
          left: 50px;
          width: 1px;
          height: 100%;
          content: '';
          background: var(--default-bg-color);
        }
      }

      .code-wrapper {
        overflow-x: auto;
      }

      .line-number {
        position: sticky;
        left: 0;
        z-index: 2;
        box-sizing: border-box;
        display: inline-block;
        width: 50px;
        margin-right: 10px;
        font-size: 14px;
        color: var(--art-gray-500);
        text-align: center;
      }

      .copy-button {
        position: absolute;
        top: 6px;
        right: 6px;
        z-index: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        font-size: 20px;
        line-height: 40px;
        color: var(--art-gray-500);
        text-align: center;
        cursor: pointer;
        background-color: var(--default-bg-color);
        border: none;
        border-radius: 8px;
        opacity: 0;
        transition: all 0.2s;
      }
    }
  }

  .article-detail .max-w-200 > div {
    transition: all 0.2s ease;
  }
  .article-detail .max-w-200 > div:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  }
</style>
