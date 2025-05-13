<template>
  <div class="navigation-bar flex justify-between items-center">
    <HamBurger :is-active="appStore.sidebarStatus" @toggle-click="toggleSidebar"
      class="h-full flex justify-between items-center" />
    <div class="right-menu h-full flex items-center">
      <el-dropdown trigger="click" class="cursor-pointer">
        <el-avatar src="https://avatars.githubusercontent.com/u/21263805?v=4" />
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item>个人中心</el-dropdown-item>
            <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script setup lang="ts">
import HamBurger from '@/layouts/components/Hamburger/index.vue'
import { useAppStore } from '@/store/modules/app';
import { useLogin } from '@/hooks/useLogin';
// import { ElDropdown, ElDropdownMenu, ElDropdownItem, ElAvatar } from 'element-plus';
defineOptions({
  name: 'NavigationBar'
})
const appStore = useAppStore()
const { logout } = useLogin()
// const logout = () => {
//   console.log('logout')
// }
const toggleSidebar = () => {
  // appStore.toggleSidebar(false)
  appStore.toggleSidebarStatus()
}
</script>

<style lang="scss" scoped>
.navigation-bar {
  height: 60px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 0 20px;
}
</style>
