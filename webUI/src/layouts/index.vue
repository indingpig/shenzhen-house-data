<template>
  <div class="app-wrapper w-full h-full relative">
    <Sidebar class="h-full fixed w-48" />
    <div class="main-container ml-48 h-full relative">
      <NavigationBar class="h-[60px]" />
      <AppMain />
    </div>
  </div>
</template>

<script setup lang="ts">
import { AppMain, Sidebar, NavigationBar } from './components';
defineOptions({
  name: 'IndexLayout'
})
</script>

<style scoped></style>
