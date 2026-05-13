<template>
  <Teleport to="body">
    <Transition name="modal">
      <div v-if="visible" class="fixed inset-0 z-50 flex items-center justify-center">
        <!-- 遮罩层 -->
        <div class="absolute inset-0 bg-black/30 backdrop-blur-sm" @click="handleClose"></div>

        <!-- 弹窗内容 -->
        <div class="relative w-full max-w-[454px] mx-4 overflow-hidden rounded-[18px] bg-white shadow-[0_28px_80px_rgba(15,23,42,0.18)] ring-1 ring-black/5">
          <!-- 关闭按钮 -->
          <button
            @click="handleClose"
            class="absolute right-4 top-4 z-10 flex h-8 w-8 items-center justify-center rounded-full text-[#667085] transition-colors hover:bg-gray-100 hover:text-gray-700"
          >
            <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>

          <!-- 内容区域 -->
          <div class="px-8 pb-8 pt-10">
            <!-- 登录表单（账号登录和验证码登录共用） -->
            <div v-if="currentForm === 'login' || currentForm === 'codeLogin'" class="text-[#101828]">
              <div class="flex items-center justify-between gap-4">
                <div class="flex-1">
                  <div class="text-[24px] font-semibold leading-none flex items-center gap-2">欢迎回来 <img src="/icons/applaud.svg" alt="applaud" class="w-6 h-6" /></div>
                  <div class="mt-3 text-[14px] leading-6 text-[#667085]">登录以继续阅读和管理你的内容</div>
                </div>
                <img src="/images/lock-3d.png" alt="lock illustration" class="mr-1 mt-[-2px] h-[140px] w-[150px] object-contain select-none pointer-events-none" />
              </div>

              <div class="mt-[34px] flex border-b border-[#EAECF0] text-[14px]">
                <button 
                  :class="currentForm === 'login' ? 'relative pb-4 text-[#101828]' : 'pb-4 text-[#98A2B3]'" 
                  @click="currentForm = 'login'"
                >
                  账号登录
                  <span v-if="currentForm === 'login'" class="absolute bottom-[-1px] left-0 h-[2px] w-full rounded-full bg-[#2563EB]"></span>
                </button>
                <button 
                  :class="currentForm === 'codeLogin' ? 'relative ml-10 pb-4 text-[#101828]' : 'ml-10 pb-4 text-[#98A2B3]'" 
                  @click="currentForm = 'codeLogin'"
                >
                  验证码登录
                  <span v-if="currentForm === 'codeLogin'" class="absolute bottom-[-1px] left-0 h-[2px] w-full rounded-full bg-[#2563EB]"></span>
                </button>
              </div>

              <!-- 账号登录输入框 -->
              <div v-if="currentForm === 'login'" class="mt-6 space-y-4">
                <div class="flex h-[40px] items-center gap-3 rounded-[8px] border border-[#D0D5DD] px-3 text-[14px] text-[#667085]">
                  <span>✉️</span>
                  <input v-model="loginForm.email" type="email" placeholder="邮箱地址" class="w-full bg-transparent outline-none placeholder:text-[#98A2B3]" />
                </div>
                <div class="flex h-[40px] items-center gap-3 rounded-[8px] border border-[#D0D5DD] px-3 text-[14px] text-[#667085]">
                  <span>🔒</span>
                  <input v-model="loginForm.password" :type="showLoginPassword ? 'text' : 'password'" placeholder="密码" class="w-full bg-transparent outline-none placeholder:text-[#98A2B3]" />
                  <button class="text-[#98A2B3]" @click="showLoginPassword = !showLoginPassword">👁️</button>
                </div>

                <div class="flex items-center justify-between pt-1 text-[13px]">
                  <label class="flex items-center gap-2 text-[#344054]"><input v-model="loginForm.remember" type="checkbox" class="h-4 w-4 rounded border-[#D0D5DD] text-[#2563EB] focus:ring-[#2563EB]" />记住我</label>
                  <button class="text-[#2563EB] hover:underline" @click="currentForm = 'forgotPassword'">忘记密码</button>
                </div>

                <button class="mt-1 flex h-[40px] w-full items-center justify-center rounded-[6px] bg-[#2563EB] text-[14px] font-medium text-white shadow-[0_8px_18px_rgba(37,99,235,0.25)]" @click="handleLogin">登录</button>
              </div>

              <!-- 验证码登录输入框 -->
              <div v-if="currentForm === 'codeLogin'" class="mt-6 space-y-4">
                <div class="flex h-[40px] items-center gap-3 rounded-[8px] border border-[#D0D5DD] px-3 text-[14px] text-[#667085]">
                  <span>✉️</span>
                  <input v-model="codeLoginForm.email" type="email" placeholder="邮箱地址" class="w-full bg-transparent outline-none placeholder:text-[#98A2B3]" />
                </div>
                <div class="flex gap-2">
                  <div class="flex h-[40px] flex-1 items-center rounded-[8px] border border-[#D0D5DD] px-3 text-[14px] text-[#667085]">
                    <input v-model="codeLoginForm.code" type="text" placeholder="请输入6位验证码" class="w-full bg-transparent outline-none placeholder:text-[#98A2B3]" />
                  </div>
                  <button class="h-[40px] shrink-0 rounded-[8px] border border-[#D0D5DD] px-4 text-[13px] font-medium text-[#2563EB] disabled:text-[#98A2B3]" :disabled="loginCodeCountdown > 0" @click="startCodeCountdown('login')">{{ loginCodeCountdown > 0 ? `获取验证码(${loginCodeCountdown}s)` : '获取验证码' }}</button>
                </div>
                <div class="text-[12px] text-[#98A2B3]">验证码已发送至您的邮箱，请查收</div>

                <div class="flex items-center justify-between text-[13px]">
                  <label class="flex items-center gap-2 text-[#344054]"><input v-model="loginForm.remember" type="checkbox" class="h-4 w-4 rounded border-[#D0D5DD] text-[#2563EB] focus:ring-[#2563EB]" />记住我</label>
                  <button class="text-[#2563EB] hover:underline" @click="currentForm = 'forgotPassword'">收不到验证码</button>
                </div>

                <button class="flex h-[40px] w-full items-center justify-center rounded-[6px] bg-[#2563EB] text-[14px] font-medium text-white shadow-[0_8px_18px_rgba(37,99,235,0.25)]" @click="handleCodeLogin">登录</button>
              </div>

              <!-- 共同的第三方登录和注册链接 -->
              <div class="mt-6 flex items-center gap-4 py-3 text-[13px] text-[#98A2B3]"><span class="h-px flex-1 bg-[#EAECF0]"></span><span>或使用以下方式登录</span><span class="h-px flex-1 bg-[#EAECF0]"></span></div>

              <div class="flex justify-center gap-6">
                <button class="flex h-10 w-18 items-center justify-center rounded-[8px] border border-[#D0D5DD] bg-white px-6">
                  <img src="/icons/github-black.svg" alt="GitHub" class="w-5 h-5" />
                </button>
                <button class="flex h-10 w-18 items-center justify-center rounded-[8px] border border-[#D0D5DD] bg-white px-6">
                  <img src="/icons/goole.svg" alt="Google" class="w-5 h-5" />
                </button>
                <button class="flex h-10 w-18 items-center justify-center rounded-[8px] border border-[#D0D5DD] bg-white px-6">
                  <img src="/icons/qq.svg" alt="QQ" class="w-5 h-5" />
                </button>
              </div>

              <div class="pt-2 text-center text-[14px] text-[#667085]">还没有账号? <button class="text-[#2563EB] hover:underline" @click="currentForm = 'register'">去注册</button></div>
            </div>

            <div v-if="currentForm === 'register'" class="text-[#101828]">
              <div class="flex items-start justify-between gap-4">
                <div class="pt-10">
                  <div class="text-[24px] font-semibold leading-none">创建你的账号 🚀</div>
                  <div class="mt-3 text-[14px] leading-6 text-[#667085]">加入 Lin's Tech Blog，记录与分享你的技术见解</div>
                </div>
                <img src="/images/lock-3d.png" alt="user illustration" class="mr-1 mt-[-2px] h-[140px] w-[150px] object-contain select-none pointer-events-none" />
              </div>
              <div class="mt-8 space-y-4">
                <div class="flex h-[40px] items-center gap-3 rounded-[8px] border border-[#D0D5DD] px-3 text-[14px] text-[#667085]"><span>👤</span><input v-model="registerForm.username" type="text" placeholder="用户名" class="w-full bg-transparent outline-none placeholder:text-[#98A2B3]" /></div>
                <div class="-mt-2 pl-1 text-[12px] text-[#98A2B3]">3-20 个字符，可包含字母、数字和下划线</div>
                <div class="flex h-[40px] items-center gap-3 rounded-[8px] border border-[#D0D5DD] px-3 text-[14px] text-[#667085]"><span>✉️</span><input v-model="registerForm.email" type="email" placeholder="邮箱地址" class="w-full bg-transparent outline-none placeholder:text-[#98A2B3]" /></div>
                <div class="flex h-[40px] items-center gap-3 rounded-[8px] border border-[#D0D5DD] px-3 text-[14px] text-[#667085]"><span>🔒</span><input v-model="registerForm.password" :type="showRegisterPassword ? 'text' : 'password'" placeholder="密码" class="w-full bg-transparent outline-none placeholder:text-[#98A2B3]" /><button class="text-[#98A2B3]" @click="showRegisterPassword = !showRegisterPassword">👁️</button></div>
                <div class="-mt-2 pl-1 text-[12px] text-[#98A2B3]">至少 8 位，包含字母和数字</div>
                <div class="flex h-[40px] items-center gap-3 rounded-[8px] border border-[#D0D5DD] px-3 text-[14px] text-[#667085]"><span>🔒</span><input v-model="registerForm.confirmPassword" type="password" placeholder="确认密码" class="w-full bg-transparent outline-none placeholder:text-[#98A2B3]" /><button class="text-[#98A2B3]" @click="showRegisterPassword = !showRegisterPassword">👁️</button></div>
                <label class="flex items-start gap-2 pt-1 text-[13px] text-[#344054]"><input v-model="registerForm.agree" type="checkbox" class="mt-0.5 h-4 w-4 rounded border-[#D0D5DD] text-[#2563EB] focus:ring-[#2563EB]" />我已阅读并同意《<span class="text-[#2563EB]">服务条款</span>》和《<span class="text-[#2563EB]">隐私政策</span>》</label>
                <button class="mt-1 flex h-[40px] w-full items-center justify-center rounded-[6px] bg-[#2563EB] text-[14px] font-medium text-white shadow-[0_8px_18px_rgba(37,99,235,0.25)]" @click="handleRegister">注册</button>
                <div class="flex items-center gap-4 py-3 text-[13px] text-[#98A2B3]"><span class="h-px flex-1 bg-[#EAECF0]"></span><span>或使用以下方式注册</span><span class="h-px flex-1 bg-[#EAECF0]"></span></div>
                <div class="flex justify-center gap-6 pt-1">
                  <button class="flex h-10 w-18 items-center justify-center rounded-[8px] border border-[#D0D5DD] bg-white px-6">
                    <img src="/icons/github-black.svg" alt="GitHub" class="w-5 h-5" />
                  </button>
                  <button class="flex h-10 w-18 items-center justify-center rounded-[8px] border border-[#D0D5DD] bg-white px-6">
                    <img src="/icons/goole.svg" alt="Google" class="w-5 h-5" />
                  </button>
                  <button class="flex h-10 w-18 items-center justify-center rounded-[8px] border border-[#D0D5DD] bg-white px-6">
                    <img src="/icons/qq.svg" alt="QQ" class="w-5 h-5" />
                  </button>
                </div>
                <div class="pt-2 text-center text-[14px] text-[#667085]">已有账号? <button class="text-[#2563EB] hover:underline" @click="currentForm = 'login'">去登录</button></div>
              </div>
            </div>

            <div v-if="currentForm === 'forgotPassword'" class="text-[#101828]">
              <div class="flex items-start justify-between gap-4">
                <div class="pt-16">
                  <div class="text-[24px] font-semibold leading-none">忘记密码</div>
                  <div class="mt-3 text-[14px] leading-6 text-[#667085]">通过邮箱验证码重置你的密码</div>
                </div>
                <img src="/images/lock-3d.png" alt="lock illustration" class="mr-1 mt-[-2px] h-[140px] w-[150px] object-contain select-none pointer-events-none" />
              </div>
              <div class="mt-10 space-y-4">
                <div class="flex h-[40px] items-center gap-3 rounded-[8px] border border-[#D0D5DD] px-3 text-[14px] text-[#667085]"><span>✉️</span><input v-model="forgotForm.email" type="email" placeholder="邮箱地址" class="w-full bg-transparent outline-none placeholder:text-[#98A2B3]" /></div>
                <div class="flex h-[40px] items-center gap-3 rounded-[8px] border border-[#D0D5DD] px-3 text-[14px] text-[#667085]"><span>🔢</span><input v-model="forgotForm.code" type="text" placeholder="验证码" class="w-full bg-transparent outline-none placeholder:text-[#98A2B3]" /><button class="shrink-0 rounded-[6px] px-3 py-1.5 text-[12px] font-medium text-[#2563EB] disabled:text-[#98A2B3]" :disabled="forgotCodeCountdown > 0" @click="startCodeCountdown('forgot')">{{ forgotCodeCountdown > 0 ? `${forgotCodeCountdown}s` : '获取验证码' }}</button></div>
                <div class="flex h-[40px] items-center gap-3 rounded-[8px] border border-[#D0D5DD] px-3 text-[14px] text-[#667085]"><span>🔒</span><input v-model="forgotForm.newPassword" :type="showNewPassword ? 'text' : 'password'" placeholder="新密码" class="w-full bg-transparent outline-none placeholder:text-[#98A2B3]" /><button class="text-[#98A2B3]" @click="showNewPassword = !showNewPassword">👁️</button></div>
                <div class="flex h-[40px] items-center gap-3 rounded-[8px] border border-[#D0D5DD] px-3 text-[14px] text-[#667085]"><span>🔒</span><input v-model="forgotForm.confirmPassword" type="password" placeholder="确认新密码" class="w-full bg-transparent outline-none placeholder:text-[#98A2B3]" /></div>
                <button class="mt-1 flex h-[40px] w-full items-center justify-center rounded-[6px] bg-[#2563EB] text-[14px] font-medium text-white shadow-[0_8px_18px_rgba(37,99,235,0.25)]" @click="handleResetPassword">重置密码</button>
                <div class="pt-2 text-center text-[14px] text-[#667085]"><button class="text-[#2563EB] hover:underline" @click="currentForm = 'login'">返回登录</button></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { ref, reactive, onBeforeUnmount } from 'vue'

const props = defineProps({ visible: { type: Boolean, default: false } })
const emit = defineEmits(['close', 'login', 'register', 'reset-password'])
const currentForm = ref('login')
const showLoginPassword = ref(false)
const showRegisterPassword = ref(false)
const showNewPassword = ref(false)
const loginCodeCountdown = ref(0)
const forgotCodeCountdown = ref(0)
let loginCodeTimer = null
let forgotCodeTimer = null
const startCodeCountdown = (type) => {
  if (type === 'login') {
    if (loginCodeCountdown.value > 0) return
    loginCodeCountdown.value = 60
    loginCodeTimer = setInterval(() => { loginCodeCountdown.value--; if (loginCodeCountdown.value <= 0) { clearInterval(loginCodeTimer); loginCodeTimer = null } }, 1000)
  } else {
    if (forgotCodeCountdown.value > 0) return
    forgotCodeCountdown.value = 60
    forgotCodeTimer = setInterval(() => { forgotCodeCountdown.value--; if (forgotCodeCountdown.value <= 0) { clearInterval(forgotCodeTimer); forgotCodeTimer = null } }, 1000)
  }
}
const loginForm = reactive({ email: '', password: '', remember: true })
const codeLoginForm = reactive({ email: '', code: '' })
const registerForm = reactive({ username: '', email: '', password: '', confirmPassword: '', agree: false })
const forgotForm = reactive({ email: '', code: '', newPassword: '', confirmPassword: '' })
const handleClose = () => emit('close')
const handleLogin = () => { if (!loginForm.email || !loginForm.password) return alert('请填写完整的登录信息'); emit('login', { ...loginForm }) }
const handleCodeLogin = () => { if (!codeLoginForm.email) return alert('请输入邮箱地址'); if (!codeLoginForm.code) return alert('请输入验证码'); emit('login', { ...codeLoginForm, type: 'code' }) }
const handleRegister = () => { if (!registerForm.username || !registerForm.email || !registerForm.password) return alert('请填写完整的注册信息'); if (registerForm.password !== registerForm.confirmPassword) return alert('两次输入的密码不一致'); if (!registerForm.agree) return alert('请阅读并同意服务条款和隐私政策'); emit('register', { ...registerForm }) }
const handleResetPassword = () => { if (!forgotForm.email) return alert('请输入邮箱地址'); if (!forgotForm.code) return alert('请输入验证码'); if (!forgotForm.newPassword) return alert('请输入新密码'); if (forgotForm.newPassword !== forgotForm.confirmPassword) return alert('两次输入的密码不一致'); emit('reset-password', { ...forgotForm }); alert('密码重置成功'); currentForm.value = 'login' }
onBeforeUnmount(() => { if (loginCodeTimer) clearInterval(loginCodeTimer); if (forgotCodeTimer) clearInterval(forgotCodeTimer) })
</script>

<style scoped>
.modal-enter-active,.modal-leave-active{transition:all .3s cubic-bezier(.4,0,.2,1)}
.modal-enter-from,.modal-leave-to{opacity:0}
.modal-enter-from .relative,.modal-leave-to .relative{transform:scale(.95) translateY(16px)}
</style>