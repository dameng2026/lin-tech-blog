import { ref } from 'vue'

const isVisible = ref(false)

export function useAuthModal() {
  const openModal = (loginEnabled: number = 1) => {
    if (loginEnabled === 0) {
      alert('暂未开放登录')
      return
    }
    isVisible.value = true
  }

  const closeModal = () => {
    isVisible.value = false
  }

  const handleLogin = (form: { email: string; password: string; remember: boolean }) => {
    alert(`登录成功！\n邮箱: ${form.email}\n记住我: ${form.remember}`)
    closeModal()
  }

  const handleRegister = (form: { username: string; email: string; password: string }) => {
    alert(`注册成功！\n用户名: ${form.username}\n邮箱: ${form.email}`)
    closeModal()
  }

  return {
    isVisible,
    openModal,
    closeModal,
    handleLogin,
    handleRegister
  }
}