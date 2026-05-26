import api from './site'

export async function fetchProfile() {
  try {
    const response = await api.get('/profile/')
    if (response.data && response.data.code === 200 && response.data.data) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取个人资料失败:', error)
    return null
  }
}

export async function fetchProfileSkills() {
  try {
    const response = await api.get('/profile/skills')
    if (response.data && response.data.code === 200 && Array.isArray(response.data.data)) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取技能列表失败:', error)
    return null
  }
}

export async function fetchProfileExperiences() {
  try {
    const response = await api.get('/profile/experiences')
    if (response.data && response.data.code === 200 && Array.isArray(response.data.data)) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取工作经历失败:', error)
    return null
  }
}

export async function fetchProfileEducation() {
  try {
    const response = await api.get('/profile/education')
    if (response.data && response.data.code === 200 && Array.isArray(response.data.data)) {
      return response.data.data
    }
    return null
  } catch (error) {
    console.error('获取教育背景失败:', error)
    return null
  }
}
