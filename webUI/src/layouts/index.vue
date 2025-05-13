<template>
  <div class="app-wrapper w-full h-full relative" :class="layoutClasses">
    <Sidebar class="h-full fixed w-48 side-bar" />
    <div class="main-container ml-48 h-full relative">
      <NavigationBar class="h-[60px]" />
      <AppMain />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { AppMain, Sidebar, NavigationBar } from './components';
import { useAppStore } from '@/store/modules/app';
defineOptions({
  name: 'IndexLayout'
})
const appStore = useAppStore()
const layoutClasses = computed(() => {
  return {
    'hidden-scrollbar': appStore.sidebarStatus,
  }
})
</script>

<style lang="scss" scoped>
.hidden-scrollbar {
  .side-bar {
    width: 64px;
  }

  .main-container {
    transition: all 0.3s;
    margin-left: 64px;
  }
}
</style>
