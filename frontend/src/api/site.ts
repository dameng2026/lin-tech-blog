import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
  timeout: 10000
})

export const fetchSiteSettings = async () => {
  try {
    const response = await api.get('/settings/site')
    if (response.data && response.data.code === 200) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取站点设置失败:', error)
    return null
  }
}

export const fetchSiteStatistics = async () => {
  try {
    const response = await api.get('/statistics/site')
    if (response.data && response.data.code === 200) {
      return response.data.data
    }
    if (response.data && response.data.articles_count !== undefined) {
      return response.data
    }
    return null
  } catch (error) {
    console.error('获取站点统计失败:', error)
    return null
  }
}

export default api