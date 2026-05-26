<template>
  <Icon v-if="icon" :icon="icon" v-bind="$attrs" />
</template>

<script setup lang="ts">
  import { Icon } from '@iconify/vue'

  defineOptions({ name: 'IconifyIconOffline' })

  interface Props {
    icon: string
  }

  defineProps<Props>()
</script>
