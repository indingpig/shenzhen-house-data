<template>
  <div class="navigation-bar">
    <HamBurger :is-active="isActive" @toggle-click="toggleSidebar" />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import HamBurger from '@/layouts/components/Hamburger/index.vue'
defineOptions({
  name: 'NavigationBar'
})
const isActive = ref<boolean>(false)
const toggleSidebar = () => {
  // appStore.toggleSidebar(false)
  console.log('toggleSidebar')
}
</script>

<style scoped></style>
