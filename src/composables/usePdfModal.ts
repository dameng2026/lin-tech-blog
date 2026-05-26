import { ref } from 'vue'

const isVisible = ref(false)

export function usePdfModal() {
  const openModal = () => {
    isVisible.value = true
  }

  const closeModal = () => {
    isVisible.value = false
  }

  const handleDownload = (password: string) => {
    alert(`下载密钥: ${password}\n\n正在下载简历...`)
    closeModal()
  }

  return {
    isVisible,
    openModal,
    closeModal,
    handleDownload
  }
}