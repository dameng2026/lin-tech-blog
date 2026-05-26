<!-- 表格按钮 -->
<template>
  <div
    :class="[
      'inline-flex items-center justify-center w-8 h-8 text-base c-p rounded-md align-middle transition-all duration-200 hover:scale-105 active:scale-95',
      buttonClass
    ]"
    :style="{ backgroundColor: buttonBgColor, color: iconColor }"
    @click="handleClick"
  >
    <ArtSvgIcon :icon="iconContent" class="w-4 h-4" />
  </div>
</template>

<script setup lang="ts">
  defineOptions({ name: 'ArtButtonTable' })

  interface Props {
    /** 按钮类型 */
    type?: 'add' | 'edit' | 'delete' | 'more' | 'view' | 'comment' | 'toggle' | 'approve' | 'reject' | 'pause' | 'resume'
    /** 按钮图标 */
    icon?: string
    /** 按钮样式类 */
    iconClass?: string
    /** icon 颜色 */
    iconColor?: string
    /** 按钮背景色 */
    buttonBgColor?: string
  }

  const props = withDefaults(defineProps<Props>(), {})

  const emit = defineEmits<{
    (e: 'click'): void
  }>()

  // 默认按钮配置
  const defaultButtons = {
    add: { icon: 'ri:add-fill', class: 'bg-theme/12 text-theme' },
    edit: { icon: 'ri:pencil-line', class: 'bg-secondary/12 text-secondary' },
    delete: { icon: 'ri:delete-bin-5-line', class: 'bg-error/12 text-error' },
    view: { icon: 'ri:eye-line', class: 'bg-info/12 text-info' },
    more: { icon: 'ri:more-2-fill', class: '' },
    comment: { icon: 'ri:chat-3-line', class: 'bg-purple-50 text-purple-600' },
    toggle: { icon: 'ri:pause-circle-line', class: 'bg-warning/12 text-warning' },
    approve: { icon: 'ri:check-line', class: 'bg-success/12 text-success' },
    reject: { icon: 'ri:ban-line', class: 'bg-warning/12 text-warning' },
    pause: { icon: 'ri:pause-circle-line', class: 'bg-info/12 text-info' },
    resume: { icon: 'ri:play-circle-line', class: 'bg-success/12 text-success' }
  } as const

  // 获取图标内容
  const iconContent = computed(() => {
    return props.icon || (props.type ? defaultButtons[props.type]?.icon : '') || ''
  })

  // 获取按钮样式类
  const buttonClass = computed(() => {
    const defaultClass = props.type ? defaultButtons[props.type]?.class : ''
    return [defaultClass, props.iconClass].filter(Boolean).join(' ')
  })

  const handleClick = () => {
    emit('click')
  }
</script>
