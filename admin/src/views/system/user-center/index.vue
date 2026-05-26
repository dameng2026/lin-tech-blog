<template>
  <div class="w-full h-full p-4">
    <div class="relative flex-b mt-2.5 max-md:block max-md:mt-1">
      <div class="w-112 mr-5 max-md:w-full max-md:mr-0">
        <div class="art-card-sm rounded-xl shadow-sm border border-[var(--art-card-border)] relative p-9 pb-6 overflow-hidden text-center">
          <img class="absolute top-0 left-0 w-full h-50 object-cover" src="@imgs/user/bg.webp" />
          <div class="relative z-10 w-20 h-20 mx-auto mt-30 object-cover border-2 border-white rounded-full overflow-hidden cursor-pointer" @click="triggerAvatarUpload">
            <img v-if="previewAvatar" :src="previewAvatar" alt="头像" class="w-full h-full object-cover" />
            <img v-else-if="siteSettings.admin_avatar" :src="getImageUrl(siteSettings.admin_avatar)" alt="头像" class="w-full h-full object-cover" />
            <img v-else src="@imgs/user/avatar.webp" alt="默认头像" class="w-full h-full object-cover" />
            <input type="file" ref="avatarInputRef" class="hidden" accept="image/*" @change="handleAvatarChange" />
            <div v-if="isUploading" class="absolute inset-0 bg-black/50 flex items-center justify-center">
              <div class="w-8 h-8 border-4 border-white border-t-transparent rounded-full animate-spin"></div>
            </div>
          </div>
          <div class="mt-3 text-sm text-gray-500">点击头像上传</div>
          
          <h2 class="mt-5 text-xl font-normal">{{ siteSettings.author_name || '未设置姓名' }}</h2>
          <p class="mt-2 text-sm text-gray-600">{{ siteSettings.description || '暂无简介' }}</p>

          <div class="w-75 mx-auto mt-7.5 text-left">
            <div v-if="siteSettings.author_name" class="mt-2.5">
              <ArtSvgIcon icon="ri:user-3-line" class="text-g-700" />
              <span class="ml-2 text-sm">{{ siteSettings.author_name }}</span>
            </div>
            <div v-if="siteSettings.location" class="mt-2.5">
              <ArtSvgIcon icon="ri:map-pin-line" class="text-g-700" />
              <span class="ml-2 text-sm">{{ siteSettings.location }}</span>
            </div>
            <div v-if="siteSettings.email" class="mt-2.5">
              <ArtSvgIcon icon="ri:mail-line" class="text-g-700" />
              <span class="ml-2 text-sm">{{ siteSettings.email }}</span>
            </div>
            <div v-if="siteSettings.github_url" class="mt-2.5">
              <ArtSvgIcon icon="ri:github-line" class="text-g-700" />
              <span class="ml-2 text-sm">{{ siteSettings.github_url }}</span>
            </div>
          </div>

          <div class="mt-10">
            <h3 class="text-sm font-medium">标签</h3>
            <div class="flex flex-wrap justify-center mt-3.5">
              <div
                v-for="item in labelList"
                :key="item"
                class="py-1 px-1.5 mr-2.5 mb-2.5 text-xs border border-g-300 rounded"
              >
                {{ item }}
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="flex-1 overflow-hidden max-md:w-full max-md:mt-3.5">
        <div class="art-card-sm rounded-xl shadow-sm border border-[var(--art-card-border)]">
          <h1 class="p-4 text-xl font-normal border-b border-g-300">基本设置</h1>

          <ElForm
            :model="form"
            class="box-border p-5 [&>.el-row_.el-form-item]:w-[calc(50%-10px)] [&>.el-row_.el-input]:w-full [&>.el-row_.el-select]:w-full"
            ref="ruleFormRef"
            :rules="rules"
            label-width="86px"
            label-position="top"
          >
            <ElRow>
              <ElFormItem label="姓名（作者名称）" prop="author_name">
                <ElInput v-model="form.author_name" placeholder="请输入姓名" />
              </ElFormItem>
              <ElFormItem label="邮箱" prop="email" class="ml-5">
                <ElInput v-model="form.email" placeholder="请输入邮箱" />
              </ElFormItem>
            </ElRow>

            <ElRow>
              <ElFormItem label="GitHub 地址" prop="github_url">
                <ElInput v-model="form.github_url" placeholder="请输入 GitHub 地址" />
              </ElFormItem>
              <ElFormItem label="位置" prop="location" class="ml-5">
                <ElInput v-model="form.location" placeholder="请输入位置信息" />
              </ElFormItem>
            </ElRow>

            <ElRow>
              <ElFormItem label="微信号" prop="wechat">
                <ElInput v-model="form.wechat" placeholder="请输入微信号" />
              </ElFormItem>
              <ElFormItem label="QQ号" prop="qq" class="ml-5">
                <ElInput v-model="form.qq" placeholder="请输入QQ号" />
              </ElFormItem>
            </ElRow>

            <ElRow>
              <ElFormItem label="手机号" prop="phone">
                <ElInput v-model="form.phone" placeholder="请输入手机号" />
              </ElFormItem>
              <ElFormItem label="个人简介" prop="description" class="ml-5">
                <ElInput v-model="form.description" type="textarea" :rows="2" placeholder="请输入个人简介" />
              </ElFormItem>
            </ElRow>

            <div class="flex-c justify-end mt-5 [&_.el-button]:!w-27.5">
              <ElButton type="primary" class="w-22.5" v-ripple @click="handleSave" :loading="saving">
                保存设置
              </ElButton>
            </div>
          </ElForm>
        </div>

        <div class="art-card-sm rounded-xl shadow-sm border border-[var(--art-card-border)] my-5">
          <h1 class="p-4 text-xl font-normal border-b border-g-300">更改密码</h1>

          <ElForm :model="pwdForm" class="box-border p-5" label-width="86px" label-position="top">
            <ElFormItem label="当前密码" prop="password">
              <ElInput
                v-model="pwdForm.password"
                type="password"
                show-password
                placeholder="请输入当前密码"
              />
            </ElFormItem>

            <ElFormItem label="新密码" prop="newPassword">
              <ElInput
                v-model="pwdForm.newPassword"
                type="password"
                show-password
                placeholder="请输入新密码"
              />
            </ElFormItem>

            <ElFormItem label="确认新密码" prop="confirmPassword">
              <ElInput
                v-model="pwdForm.confirmPassword"
                type="password"
                show-password
                placeholder="请确认新密码"
              />
            </ElFormItem>

            <div class="flex-c justify-end mt-5 [&_.el-button]:!w-27.5">
              <ElButton type="primary" class="w-22.5" v-ripple @click="handleChangePassword">
                更改密码
              </ElButton>
            </div>
          </ElForm>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { useUserStore } from '@/store/modules/user'
  import type { FormInstance, FormRules } from 'element-plus'
  import { fetchSiteSettings, updateSiteSettings, uploadAvatar } from '@/api/settings'
  import { changePassword } from '@/api/auth'
  import { ElMessage } from 'element-plus'

  defineOptions({ name: 'UserCenter' })

  const userStore = useUserStore()
  const userInfo = computed(() => userStore.getUserInfo)
  const avatarInputRef = ref<HTMLInputElement>()
  
  const siteSettings = ref<any>({
    author_name: '',
    email: '',
    github_url: '',
    description: '',
    admin_avatar: '',
    location: '',
    wechat: '',
    qq: '',
    phone: ''
  })
  
  const previewAvatar = ref('')
  const isUploading = ref(false)
  const saving = ref(false)

  const form = reactive({
    author_name: '',
    email: '',
    github_url: '',
    description: '',
    location: '',
    wechat: '',
    qq: '',
    phone: ''
  })

  const pwdForm = reactive({
    password: '',
    newPassword: '',
    confirmPassword: ''
  })

  const rules = reactive<FormRules>({
    author_name: [
      { required: true, message: '请输入姓名', trigger: 'blur' }
    ],
    email: [
      { required: true, message: '请输入邮箱', trigger: 'blur' },
      { type: 'email', message: '请输入正确的邮箱格式', trigger: 'blur' }
    ]
  })

  const labelList: Array<string> = ['全栈开发', 'AI 应用', '技术探索']

  const getImageUrl = (path: string) => {
    if (!path) return ''
    if (path.startsWith('http')) return path
    return `http://localhost:8000${path}`
  }

  const loadSiteSettings = async () => {
    try {
      const data = await fetchSiteSettings()
      if (data) {
        siteSettings.value = data
        form.author_name = data.author_name || ''
        form.email = data.email || ''
        form.github_url = data.github_url || ''
        form.description = data.description || ''
        form.location = data.location || ''
        form.wechat = data.wechat || ''
        form.qq = data.qq || ''
        form.phone = data.phone || ''
        previewAvatar.value = ''
      }
    } catch (error) {
      console.error('加载站点设置失败:', error)
    }
  }

  const triggerAvatarUpload = () => {
    avatarInputRef.value?.click()
  }

  const handleAvatarChange = async (event: Event) => {
    const target = event.target as HTMLInputElement
    const file = target.files?.[0]
    if (!file) return
    
    if (!file.type.startsWith('image/')) {
      ElMessage.error('请选择图片文件')
      return
    }
    
    if (file.size > 5 * 1024 * 1024) {
      ElMessage.error('图片大小不能超过5MB')
      return
    }
    
    previewAvatar.value = URL.createObjectURL(file)
    isUploading.value = true
    
    try {
      const result = await uploadAvatar(file)
      if (result && result.avatar_url) {
        siteSettings.value.admin_avatar = result.avatar_url
        ElMessage.success('头像上传成功')
      } else {
        ElMessage.error('头像上传失败')
        previewAvatar.value = ''
      }
    } catch (error) {
      console.error('头像上传失败:', error)
      ElMessage.error('头像上传失败')
      previewAvatar.value = ''
    } finally {
      isUploading.value = false
      if (avatarInputRef.value) {
        avatarInputRef.value.value = ''
      }
    }
  }

  const handleSave = async () => {
    saving.value = true
    try {
      const submitData = {
        author_name: form.author_name,
        email: form.email,
        github_url: form.github_url,
        description: form.description,
        admin_avatar: siteSettings.value.admin_avatar,
        location: form.location,
        wechat: form.wechat,
        qq: form.qq,
        phone: form.phone
      }
      await updateSiteSettings(submitData)
      siteSettings.value = { ...siteSettings.value, ...submitData }
      ElMessage.success('设置保存成功')
    } catch (error) {
      console.error('保存失败:', error)
      ElMessage.error('设置保存失败')
    } finally {
      saving.value = false
    }
  }

  const handleChangePassword = async () => {
    if (!pwdForm.password) {
      ElMessage.error('请输入当前密码')
      return
    }
    if (!pwdForm.newPassword) {
      ElMessage.error('请输入新密码')
      return
    }
    if (pwdForm.newPassword.length < 6) {
      ElMessage.error('新密码长度不能少于6位')
      return
    }
    if (pwdForm.newPassword === pwdForm.password) {
      ElMessage.error('新密码不能与当前密码相同')
      return
    }
    if (pwdForm.newPassword !== pwdForm.confirmPassword) {
      ElMessage.error('两次输入的密码不一致')
      return
    }
    try {
      await changePassword({ old_password: pwdForm.password, new_password: pwdForm.newPassword })
      ElMessage.success('密码修改成功，请重新登录')
      setTimeout(() => {
        userStore.logOut()
      }, 1500)
    } catch (error: any) {
      const msg = error?.response?.data?.detail || error?.message || '密码修改失败'
      ElMessage.error(msg)
    }
  }

  onMounted(() => {
    loadSiteSettings()
  })
</script>

<style scoped>
.bg-transparent {
  background: transparent !important;
}

.art-card-sm {
  transition: all 0.2s ease;
}
.art-card-sm:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
</style>
