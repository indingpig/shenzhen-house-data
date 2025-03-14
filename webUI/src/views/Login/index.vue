<template>
  <div>

  </div>
</template>

<script setup lang="ts">
import { useLogin } from '@/hooks/useLogin';
defineOptions({
  name: 'LoginPage'
})
const { bgImg } = useLogin()
</script>

<style scoped></style>
