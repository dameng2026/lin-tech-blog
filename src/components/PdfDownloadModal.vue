<template>
  <Teleport to="body">
    <Transition name="modal">
      <div v-if="visible" class="fixed inset-0 z-50 flex items-center justify-center">
        <!-- 遮罩层-->
        <div class="absolute inset-0 bg-black/50 backdrop-blur-sm" @click="handleClose"></div>
        
        <!-- 弹窗内容 -->
        <div class="relative bg-white rounded-2xl w-full max-w-[400px] mx-4 shadow-2xl overflow-hidden">
          <!-- 关闭按钮 -->
          <button 
            @click="handleClose" 
            class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center text-gray-400 hover:text-gray-600 transition-colors"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>

          <!-- 内容区域 -->
          <div class="p-6 pt-10">
            <!-- PDF图标 -->
            <div class="flex flex-col items-center">
              <div class="relative">
                <div class="w-20 h-20 rounded-full bg-blue-50 flex items-center justify-center">
                  <svg class="w-10 h-10 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                  </svg>
                </div>
                <div class="absolute -bottom-2 left-1/2 -translate-x-1/2 px-2 py-0.5 bg-red-500 text-white text-xs font-bold rounded">PDF</div>
              </div>
            </div>

            <!-- 标题 -->
            <div class="text-center mt-6">
              <h3 class="text-xl font-bold text-gray-900">下载 PDF 报告</h3>
              <p class="text-sm text-gray-500 mt-2">为了确保报告安全，请输入下载密钥以验证身。</p>
            </div>

            <!-- 表单区域 -->
            <div class="mt-6">
              <label class="block text-sm font-medium text-gray-700 mb-2">下载密钥</label>
              <div class="relative">
                <div class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
                  </svg>
                </div>
                <input 
                  v-model="password"
                  :type="showPassword ? 'text' : 'password'"
                  placeholder="请输入下载密码"
                  class="w-full pl-12 pr-12 py-3 border border-gray-200 rounded-xl text-sm outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition-all"
                />
                <button 
                  @click="togglePassword"
                  class="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 transition-colors"
                >
                  <svg v-if="!showPassword" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                  </svg>
                  <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"/>
                  </svg>
                </button>
              </div>
              <p class="mt-3 text-xs text-gray-400 flex items-center gap-1">
                <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/>
                </svg>
                下载密钥由报告创建者提供，请妥善保管              </p>
            </div>

            <!-- 按钮区域 -->
            <div class="mt-8 flex gap-3">
              <button 
                @click="handleClose"
                class="flex-1 py-3 border border-gray-200 rounded-xl text-gray-700 font-medium hover:bg-gray-50 transition-colors"
              >
                取消
              </button>
              <button 
                @click="handleDownload"
                class="flex-1 py-3 bg-blue-600 text-white rounded-xl font-medium hover:bg-blue-700 transition-colors"
              >
                确认并下载              </button>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['close', 'download'])

const password = ref('')
const showPassword = ref(false)

const togglePassword = () => {
  showPassword.value = !showPassword.value
}

const handleClose = () => {
  emit('close')
}

const handleDownload = () => {
  if (password.value) {
    emit('download', password.value)
  } else {
    alert('请输入下载密码')
  }
}
</script>

<style scoped>
.modal-enter-active,
.modal-leave-active {
  transition: all 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .relative,
.modal-leave-to .relative {
  transform: scale(0.95) translateY(20px);
}
</style>