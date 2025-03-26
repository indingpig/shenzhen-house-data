<template>
  <div>
    <el-scrollbar>
      <el-menu mode="vertical" :collapse="false" :unique-opened="true">
        <SidebarItem v-for="route in constantRoutes" :key="route.path" :item="route" :base-path="route.path" />
      </el-menu>
    </el-scrollbar>
  </div>
</template>

<script setup lang="ts">
import { ElMenu, ElScrollbar } from 'element-plus';
import SidebarItem from '@/layouts/components/Sidebar/SidebarItem.vue';
import { constantRoutes } from '@/router';
console.log(constantRoutes)
defineOptions({
  name: 'SidebarIndex'
})
</script>

<style scoped></style>
