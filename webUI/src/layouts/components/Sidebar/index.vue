<template>
  <div>
    <el-scrollbar class="h-full">
      <el-menu class="h-full" mode="vertical" :collapse="isCollapse" :unique-opened="true" :default-active="activeMenu">
        <SidebarItem v-for="route in constantRoutes" :key="route.path" :item="route" :base-path="route.path" />
      </el-menu>
    </el-scrollbar>
  </div>
</template>

<script setup lang="ts">
import { ElMenu, ElScrollbar } from 'element-plus';
import { computed } from 'vue';
import SidebarItem from '@/layouts/components/Sidebar/SidebarItem.vue';
import { constantRoutes } from '@/router';
import { useRoute } from "vue-router"
import { useAppStore } from '@/store/modules/app';
defineOptions({
  name: 'SidebarIndex'
})
const route = useRoute()
const activeMenu = computed(() => {
  const {
    meta: { activeMenu },
    path
  } = route
  return activeMenu ? activeMenu : path
})
const appStore = useAppStore()
const isCollapse = computed(() => {
  return appStore.sidebarStatus
})
</script>

<style lang="scss" scoped>
.el-scrollbar {
  :deep(.el-scrollbar__view) {
    height: 100%;
  }
}
</style>
