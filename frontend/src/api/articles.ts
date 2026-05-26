import api from './site'

export async function fetchArticles(params = {}) {
  try {
    const response = await api.get('/articles/', { params })
    if (response.data && response.data.code === 200) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取文章列表失败:', error)
    return null
  }
}

export async function fetchCategories() {
  try {
    const response = await api.get('/taxonomy/categories')
    if (response.data && response.data.code === 200) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取分类列表失败:', error)
    return null
  }
}

export async function fetchCategoryStats() {
  try {
    const response = await api.get('/articles/categories/stats')
    if (response.data && response.data.code === 200) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取分类统计失败:', error)
    return null
  }
}

export async function fetchTagStats() {
  try {
    const response = await api.get('/articles/tags/stats')
    if (response.data && response.data.code === 200) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取标签统计失败:', error)
    return null
  }
}

export async function fetchTechStackStats() {
  try {
    const response = await api.get('/articles/tech-stack/stats')
    if (response.data && response.data.code === 200) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取技术栈统计失败:', error)
    return null
  }
}

export async function fetchArticle(id) {
  try {
    const response = await api.get(`/articles/${id}`)
    if (response.data && response.data.code === 200) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取文章详情失败:', error)
    return null
  }
}

export async function fetchRelatedArticles(articleId) {
  try {
    const response = await api.get(`/articles/${articleId}/related`)
    if (response.data && response.data.code === 200) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取相关文章失败:', error)
    return null
  }
}

export async function fetchHotArticles(limit = 5) {
  try {
    const response = await api.get('/statistics/articles/hot', { params: { limit } })
    if (response.data && response.data.code === 200) {
      return response.data.data
    }
    if (response.data && Array.isArray(response.data)) {
      return response.data
    }
    return []
  } catch (error) {
    console.error('获取热门文章失败:', error)
    return []
  }
}

export async function likeArticle(articleId) {
  try {
    const response = await api.post(`/articles/${articleId}/like`)
    return response.data
  } catch (error) {
    console.error('点赞文章失败:', error)
    return null
  }
}

export async function collectArticle(articleId) {
  try {
    const response = await api.post(`/articles/${articleId}/collect`)
    return response.data
  } catch (error) {
    console.error('收藏文章失败:', error)
    return null
  }
}