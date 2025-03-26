<template>
  <div class="navigation-bar flex justify-between items-center">
    <HamBurger :is-active="isActive" @toggle-click="toggleSidebar" class="h-full flex justify-between items-center" />
    <div class="right-menu h-full">
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
import { ref } from 'vue';
import HamBurger from '@/layouts/components/Hamburger/index.vue'
// import { useLogin } from '@/hooks/useLogin';
// import { ElDropdown, ElDropdownMenu, ElDropdownItem, ElAvatar } from 'element-plus';
defineOptions({
  name: 'NavigationBar'
})
const isActive = ref<boolean>(false)
// const { logout } = useLogin()
const logout = () => {
  console.log('logout')
}
const toggleSidebar = () => {
  // appStore.toggleSidebar(false)
  console.log('toggleSidebar')
}
</script>

<style scoped></style>
