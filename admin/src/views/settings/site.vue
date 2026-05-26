<template>
  <div class="pb-5">
    <ElCard class="art-card rounded-xl shadow-sm border border-[var(--art-card-border)]">
      <template #header>
        <div class="flex items-center justify-between">
          <h2 class="text-lg font-medium">站点基础设置</h2>
        </div>
      </template>
      
      <ArtForm
        ref="formRef"
        v-model="formData"
        :items="basicFormItems"
        :span="12"
        :labelWidth="100"
        @submit="handleSubmit"
      />
    </ElCard>

    <ElCard class="art-card rounded-xl shadow-sm border border-[var(--art-card-border)] mt-5">
      <template #header>
        <h2 class="text-lg font-medium">违禁词管理</h2>
      </template>
      
      <div class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">违禁词列表</label>
          <ElInput
            v-model="prohibitedWords"
            type="textarea"
            :rows="6"
            placeholder="请输入违禁词，多个词用逗号或换行分隔"
          />
          <p class="text-xs text-gray-400 mt-1">评论内容包含违禁词时将自动拦截，支持逗号或换行分隔</p>
        </div>
        <div class="flex justify-end">
          <ElButton type="primary" @click="saveProhibitedWords" :loading="savingProhibitedWords">
            保存违禁词
          </ElButton>
        </div>
      </div>
    </ElCard>

    <ElCard class="art-card mt-5">
      <template #header>
        <h2 class="text-lg font-medium">AI模型设置</h2>
      </template>
      
      <div class="space-y-6">
        <div class="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
          <div>
            <h3 class="font-medium">AI模型功能开关</h3>
            <p class="text-sm text-gray-500 mt-1">开启后，系统将使用AI模型生成文章目录等功能</p>
          </div>
          <ElSwitch
            v-model="aiModelEnabled"
            :active-value="true"
            :inactive-value="false"
            @change="handleAiModelToggle"
          />
        </div>
        
        <div v-if="aiModelEnabled" class="p-4 bg-gray-50 rounded-lg">
          <ElForm :model="aiConfig" label-width="120px" class="space-y-4">
            <ElFormItem label="模型密钥" prop="apiKey">
              <ElInput
                v-model="aiConfig.apiKey"
                placeholder="请输入AI模型API密钥"
                type="password"
                show-password
              />
            </ElFormItem>
            <ElFormItem label="模型名称" prop="modelType">
              <ElInput
                v-model="aiConfig.modelType"
                placeholder="请输入模型名称（如：gpt-4, kimi等）"
              />
            </ElFormItem>
            <ElFormItem label="模型URL" prop="apiUrl">
              <ElInput
                v-model="aiConfig.apiUrl"
                placeholder="请输入模型API地址"
              />
            </ElFormItem>
            <ElFormItem>
              <ElButton type="primary" @click="saveAiConfig" :loading="savingAiConfig">
                保存配置
              </ElButton>
            </ElFormItem>
          </ElForm>
        </div>
        
        <div class="p-4 bg-blue-50 rounded-lg border border-blue-100">
          <div class="flex items-start gap-3">
            <component :is="Icons.InfoFilled" class="w-5 h-5 text-blue-500 flex-shrink-0 mt-0.5" />
            <div>
              <h4 class="font-medium text-blue-800">使用说明</h4>
              <ul class="text-sm text-blue-600 mt-2 space-y-1">
                <li>• 开启AI模型功能后，发布文章时可以使用"自动获取章节"功能</li>
                <li>• AI模型会自动从文章内容中提取章节目录</li>
                <li>• 建议在系统性能允许的情况下开启此功能</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </ElCard>

    <ElCard class="art-card mt-5">
      <template #header>
        <h2 class="text-lg font-medium">站点图片设置</h2>
      </template>
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">站点Logo</label>
          <div v-if="formData.logo" class="relative">
            <img :src="getImageUrl(formData.logo)" class="w-32 h-32 object-cover rounded-lg mb-2" alt="Logo" />
            <ElUpload
              class="w-32"
              accept=".jpg,.jpeg,.png,.gif,.webp"
              :action="uploadAction"
              :show-file-list="false"
              :before-upload="(file: File) => handleUpload(file, 'logo')"
            >
              <ElButton size="small" class="w-full">重新上传</ElButton>
            </ElUpload>
            <ElButton size="small" type="danger" class="mt-2 w-full" @click="removeImage('logo')">删除图片</ElButton>
          </div>
          <div v-else>
            <ElUpload
              class="w-32 h-32 border-2 border-dashed rounded-lg flex items-center justify-center"
              accept=".jpg,.jpeg,.png,.gif,.webp"
              :action="uploadAction"
              :show-file-list="false"
              :before-upload="(file: File) => handleUpload(file, 'logo')"
            >
              <div class="text-center">
                <Plus class="w-8 h-8 text-gray-400 mx-auto" />
                <p class="text-sm text-gray-400 mt-1">点击上传</p>
              </div>
            </ElUpload>
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">QQ二维码</label>
          <div v-if="formData.qq_qrcode" class="relative">
            <img :src="getImageUrl(formData.qq_qrcode)" class="w-32 h-32 object-cover rounded-lg mb-2" alt="QQ二维码" />
            <ElUpload
              class="w-32"
              accept=".jpg,.jpeg,.png,.gif,.webp"
              :action="uploadAction"
              :show-file-list="false"
              :before-upload="(file: File) => handleUpload(file, 'qq_qrcode')"
            >
              <ElButton size="small" class="w-full">重新上传</ElButton>
            </ElUpload>
            <ElButton size="small" type="danger" class="mt-2 w-full" @click="removeImage('qq_qrcode')">删除图片</ElButton>
          </div>
          <div v-else>
            <ElUpload
              class="w-32 h-32 border-2 border-dashed rounded-lg flex items-center justify-center"
              accept=".jpg,.jpeg,.png,.gif,.webp"
              :action="uploadAction"
              :show-file-list="false"
              :before-upload="(file: File) => handleUpload(file, 'qq_qrcode')"
            >
              <div class="text-center">
                <Plus class="w-8 h-8 text-gray-400 mx-auto" />
                <p class="text-sm text-gray-400 mt-1">点击上传</p>
              </div>
            </ElUpload>
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">微信二维码</label>
          <div v-if="formData.wechat_qrcode" class="relative">
            <img :src="getImageUrl(formData.wechat_qrcode)" class="w-32 h-32 object-cover rounded-lg mb-2" alt="微信二维码" />
            <ElUpload
              class="w-32"
              accept=".jpg,.jpeg,.png,.gif,.webp"
              :action="uploadAction"
              :show-file-list="false"
              :before-upload="(file: File) => handleUpload(file, 'wechat_qrcode')"
            >
              <ElButton size="small" class="w-full">重新上传</ElButton>
            </ElUpload>
            <ElButton size="small" type="danger" class="mt-2 w-full" @click="removeImage('wechat_qrcode')">删除图片</ElButton>
          </div>
          <div v-else>
            <ElUpload
              class="w-32 h-32 border-2 border-dashed rounded-lg flex items-center justify-center"
              accept=".jpg,.jpeg,.png,.gif,.webp"
              :action="uploadAction"
              :show-file-list="false"
              :before-upload="(file: File) => handleUpload(file, 'wechat_qrcode')"
            >
              <div class="text-center">
                <Plus class="w-8 h-8 text-gray-400 mx-auto" />
                <p class="text-sm text-gray-400 mt-1">点击上传</p>
              </div>
            </ElUpload>
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">站点图标(Favicon)</label>
          <div v-if="formData.favicon" class="relative">
            <img :src="getImageUrl(formData.favicon)" class="w-32 h-32 object-cover rounded-lg mb-2" alt="站点图标" />
            <ElUpload
              class="w-32"
              accept=".ico,.jpg,.jpeg,.png,.svg"
              :action="uploadAction"
              :show-file-list="false"
              :before-upload="(file: File) => handleUpload(file, 'favicon')"
            >
              <ElButton size="small" class="w-full">重新上传</ElButton>
            </ElUpload>
            <ElButton size="small" type="danger" class="mt-2 w-full" @click="removeImage('favicon')">删除图片</ElButton>
          </div>
          <div v-else>
            <ElUpload
              class="w-32 h-32 border-2 border-dashed rounded-lg flex items-center justify-center"
              accept=".ico,.jpg,.jpeg,.png,.svg"
              :action="uploadAction"
              :show-file-list="false"
              :before-upload="(file: File) => handleUpload(file, 'favicon')"
            >
              <div class="text-center">
                <Plus class="w-8 h-8 text-gray-400 mx-auto" />
                <p class="text-sm text-gray-400 mt-1">点击上传</p>
              </div>
            </ElUpload>
          </div>
        </div>
      </div>
    </ElCard>

    <ElDialog v-model="dialogVisible" title="图片预览" width="500px">
      <img :src="dialogImageUrl" class="w-full h-auto" alt="预览图片" />
    </ElDialog>
  </div>
</template>

<script setup lang="ts">
  import { ref, onMounted, computed } from 'vue'
  import ArtForm from '@/components/core/forms/art-form/index.vue'
  import { ElCard, ElMessage, ElUpload, ElButton, ElDialog, ElForm, ElFormItem, ElInput } from 'element-plus'
  import { Plus } from '@element-plus/icons-vue'
  import * as Icons from '@element-plus/icons-vue'
  import { fetchSiteSettings, updateSiteSettings, uploadFile } from '@/api/settings'
  import type { UploadFile } from 'element-plus'

  const formRef = ref()
  const formData = ref<Record<string, any>>({
    site_name: '',
    site_title: '',
    keywords: '',
    description: '',
    logo: '',
    icp_number: '',
    site_start_date: '',
    qq_qrcode: '',
    wechat_qrcode: '',
    favicon: '',
    login_enabled: 1
  })

  const aiModelEnabled = ref(false)
  const aiConfig = ref({
    apiKey: '',
    modelType: '',
    apiUrl: ''
  })
  const savingAiConfig = ref(false)
  const prohibitedWords = ref('')
  const savingProhibitedWords = ref(false)
  const dialogVisible = ref(false)
  const dialogImageUrl = ref('')
  const uploadAction = ref('#')

  const getImageUrl = (path: string) => {
    if (!path) return ''
    if (path.startsWith('http')) return path
    return `http://localhost:8000${path}`
  }

  const handleUpload = async (file: File, field: string) => {
    try {
      const data = await uploadFile(file)
      console.log('上传返回数据:', data)
      if (data && data.file_path) {
        formData.value[field] = data.file_path
        console.log(`设置${field}为:`, formData.value[field])
        const fieldNames: Record<string, string> = {
          logo: 'Logo',
          qq_qrcode: 'QQ二维码',
          wechat_qrcode: '微信二维码',
          favicon: '站点图标'
        }
        
        const submitData = {
          site_name: formData.value.site_name,
          site_title: formData.value.site_title,
          keywords: formData.value.keywords,
          description: formData.value.description,
          icp_number: formData.value.icp_number,
          site_start_date: formData.value.site_start_date,
          logo: formData.value.logo,
          qq_qrcode: formData.value.qq_qrcode,
          wechat_qrcode: formData.value.wechat_qrcode,
          favicon: formData.value.favicon
        }
        
        console.log('自动保存图片URL:', submitData)
        await updateSiteSettings(submitData)
        ElMessage.success(`${fieldNames[field] || field}上传并保存成功`)
      } else {
        ElMessage.error('上传失败：返回数据格式不正确')
      }
    } catch (error) {
      console.error('上传失败:', error)
      ElMessage.error('上传失败')
    }
    return false
  }

  const removeImage = (field: string) => {
    formData.value[field] = ''
    const fieldNames: Record<string, string> = {
      logo: 'Logo',
      qq_qrcode: 'QQ二维码',
      wechat_qrcode: '微信二维码',
      favicon: '站点图标'
    }
    ElMessage.success(`${fieldNames[field] || field}已删除`)
  }

  const handleAiModelToggle = async (value: boolean) => {
    try {
      const httpModule = await import('@/utils/http/index')
      await httpModule.default.put({
        url: '/v1/settings/ai-model/enabled',
        params: { enabled: value }
      })
      ElMessage.success(value ? 'AI模型功能已开启' : 'AI模型功能已关闭')
    } catch (error) {
      console.error('设置AI模型开关失败:', error)
      ElMessage.error('设置失败')
      aiModelEnabled.value = !value
    }
  }

  const loadAiModelSettings = async () => {
    try {
      const httpModule = await import('@/utils/http/index')
      const data = await httpModule.default.get({
        url: '/v1/settings/ai-model/enabled'
      })
      if (data) {
        aiModelEnabled.value = data.enabled
      }
    } catch (error) {
      console.error('加载AI模型设置失败:', error)
    }
  }

  const loadAiConfig = async () => {
    try {
      const httpModule = await import('@/utils/http/index')
      const config = await httpModule.default.get({
        url: '/v1/ai-config/default'
      })
      if (config) {
        aiConfig.value = {
          apiKey: config.api_key || '',
          modelType: config.model_type || '',
          apiUrl: config.api_url || ''
        }
      }
    } catch (error) {
      console.error('加载AI配置失败:', error)
    }
  }

  const saveAiConfig = async () => {
    if (!aiConfig.value.apiKey || !aiConfig.value.modelType || !aiConfig.value.apiUrl) {
      ElMessage.error('请填写完整的AI配置信息')
      return
    }

    savingAiConfig.value = true
    try {
      const httpModule = await import('@/utils/http/index')

      const config = await httpModule.default.get({
        url: '/v1/ai-config/default'
      })

      if (config) {
        await httpModule.default.put({
          url: `/v1/ai-config/${config.id}`,
          params: {
            name: '默认配置',
            model_type: aiConfig.value.modelType,
            api_key: aiConfig.value.apiKey,
            api_url: aiConfig.value.apiUrl,
            enabled: true
          }
        })
      } else {
        await httpModule.default.post({
          url: '/v1/ai-config/',
          params: {
            name: '默认配置',
            model_type: aiConfig.value.modelType,
            api_key: aiConfig.value.apiKey,
            api_url: aiConfig.value.apiUrl,
            enabled: true
          }
        })
      }

      ElMessage.success('AI配置保存成功')
    } catch (error) {
      console.error('保存AI配置失败:', error)
      ElMessage.error('保存AI配置失败')
    } finally {
      savingAiConfig.value = false
    }
  }

  const loadProhibitedWords = async () => {
    try {
      const httpModule = await import('@/utils/http/index')
      const data: any = await httpModule.default.get({
        url: '/v1/settings/prohibited_words'
      })
      if (data && data.value) {
        prohibitedWords.value = data.value
      }
    } catch (error) {
      console.error('加载违禁词失败:', error)
    }
  }

  const saveProhibitedWords = async () => {
    savingProhibitedWords.value = true
    try {
      const httpModule = await import('@/utils/http/index')
      await httpModule.default.put({
        url: '/v1/settings/prohibited_words',
        params: {
          value: prohibitedWords.value,
          description: '违禁词列表，多个词用逗号或换行分隔',
          setting_type: 'string'
        }
      })
      ElMessage.success('违禁词保存成功')
    } catch (error) {
      console.error('保存违禁词失败:', error)
      ElMessage.error('保存违禁词失败')
    } finally {
      savingProhibitedWords.value = false
    }
  }

  const basicFormItems = computed(() => [
    {
      label: '站点名称',
      key: 'site_name',
      type: 'input',
      placeholder: '请输入站点名称',
      span: 12
    },
    {
      label: '站点标题',
      key: 'site_title',
      type: 'input',
      placeholder: '请输入站点标题',
      span: 12
    },
    {
      label: '关键词',
      key: 'keywords',
      type: 'input',
      placeholder: '请输入站点关键词，多个用逗号分隔',
      span: 24
    },
    {
      label: '站点描述',
      key: 'description',
      type: 'input',
      props: {
        type: 'textarea',
        rows: 3
      },
      placeholder: '请输入站点描述',
      span: 24
    },
    {
      label: 'ICP备案号',
      key: 'icp_number',
      type: 'input',
      placeholder: '请输入ICP备案号',
      span: 12
    },
    {
      label: '站点开始日期',
      key: 'site_start_date',
      type: 'datetime',
      props: {
        type: 'date',
        valueFormat: 'YYYY-MM-DD'
      },
      placeholder: '请选择站点开始日期',
      span: 12
    },
    {
      label: '前台登录',
      key: 'login_enabled',
      type: 'switch',
      span: 12,
      props: {
        activeValue: 1,
        inactiveValue: 0
      }
    }
  ])

  const handleSubmit = async (data: Record<string, any>) => {
    try {
      const submitData = {
        ...data,
        logo: formData.value.logo,
        qq_qrcode: formData.value.qq_qrcode,
        wechat_qrcode: formData.value.wechat_qrcode,
        favicon: formData.value.favicon
      }
      console.log('提交的数据:', submitData)
      await updateSiteSettings(submitData)
      ElMessage.success('站点设置更新成功')
    } catch (error) {
      ElMessage.error('站点设置更新失败')
    }
  }

  const loadSettings = async () => {
    try {
      const data = await fetchSiteSettings()
      if (data) {
        Object.assign(formData.value, data)
        if (formData.value.site_start_date) {
          formData.value.site_start_date = formatDate(formData.value.site_start_date)
        }
      }
    } catch (error) {
      console.error('加载站点设置失败:', error)
    }
  }

  const formatDate = (dateString: string) => {
    if (!dateString) return ''
    const date = new Date(dateString)
    const year = date.getFullYear()
    const month = String(date.getMonth() + 1).padStart(2, '0')
    const day = String(date.getDate()).padStart(2, '0')
    return `${year}-${month}-${day}`
  }

  onMounted(() => {
    loadSettings()
    loadAiModelSettings()
    loadAiConfig()
    loadProhibitedWords()
  })
</script>

<style scoped>
.art-card {
  transition: all 0.2s ease;
}
.art-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
</style>