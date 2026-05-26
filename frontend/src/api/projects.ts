import api from './site'

export async function fetchProjects(params = {}) {
  try {
    const response = await api.get('/projects/', { params })
    if (response.data && response.data.code === 200) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取项目列表失败:', error)
    return null
  }
}

export async function fetchProjectCategories() {
  try {
    const response = await api.get('/project-categories/')
    if (response.data && response.data.code === 200) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取项目分类失败:', error)
    return null
  }
}

export async function fetchProjectCategoryStats() {
  try {
    const response = await api.get('/projects/categories/stats')
    if (response.data && response.data.code === 200) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取项目分类统计失败:', error)
    return null
  }
}

export async function fetchProjectTechStackStats() {
  try {
    const response = await api.get('/projects/tech-stacks/stats')
    if (response.data && response.data.code === 200) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取技术栈统计失败:', error)
    return null
  }
}

export async function fetchHotProjects(limit = 5) {
  try {
    const response = await api.get('/statistics/projects/hot', { params: { limit } })
    if (response.data && response.data.code === 200) {
      return response.data.data
    }
    if (response.data && Array.isArray(response.data)) {
      return response.data
    }
    return []
  } catch (error) {
    console.error('获取热门项目失败:', error)
    return []
  }
}

export async function fetchProjectById(projectId) {
  try {
    const response = await api.get(`/projects/${projectId}`)
    if (response.data && response.data.code === 200) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取项目详情失败:', error)
    throw error
  }
}