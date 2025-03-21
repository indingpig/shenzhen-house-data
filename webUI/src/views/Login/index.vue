<template>
  <div class="w-full h-full bg-black">
    <div class="w-full h-full bg-cover bg-center flex items-center justify-center" :style="bgStyle">
      <div class="w-96 p-8 rounded-lg login-form fixed overflow-hidden">
        <el-form :model="loginForm" label-position="top" class="flex flex-col justify-center gap-1">
          <h1 class="text-center text-2xl">欢迎来到海拉尔大陆</h1>
          <el-form-item prop="username">
            <el-input v-model.trim="loginForm.username" size="large" placeholder="用户名" :prefix-icon="User">
            </el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input v-model.trim="loginForm.password" size="large" placeholder="登录密码" :prefix-icon="Lock"
              show-password type="password"></el-input>
          </el-form-item>
          <el-form-item prop="code">
            <el-input v-model.trim="loginForm.code" size="large" placeholder="验证码" :prefix-icon="Key">
              <template #append>
                <el-image :src="codeUrl" @click="createCode">
                  <template #placeholder>
                    <el-icon>
                      <Picture />
                    </el-icon>
                  </template>
                  <template #error>
                    <el-icon>
                      <Loading />
                    </el-icon>
                  </template>
                </el-image>
              </template>
            </el-input>
          </el-form-item>
          <el-form-item>
            <el-button class="w-full" type="primary" size="large" @click="login">登录</el-button>
          </el-form-item>
        </el-form>
      </div>
      <el-button-group class="fixed bottom-2 right-10">
        <el-button size="default" color="#666" type="primary" @click="previous" :icon="ArrowLeftBold"
          circle></el-button>
        <el-button size="default" color="#666" type="primary" @click="next" :icon="ArrowRightBold" circle></el-button>
      </el-button-group>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useLogin } from '@/hooks/useLogin';
import { useUserStore } from '@/store/modules/user';
import { ElForm, ElFormItem, ElInput, ElButton, ElImage, ElIcon, ElButtonGroup } from 'element-plus';
import { User, Lock, Key, Picture, Loading, ArrowLeftBold, ArrowRightBold } from "@element-plus/icons-vue"
defineOptions({
  name: 'LoginPage'
})
const userStore = useUserStore()
const { bgStyle, loginForm, codeUrl, createCode, login, previous, next } = useLogin();
</script>

<style scoped lang="scss">
.login-form {
  box-shadow: 0px 5px 20px rgba(0, 0, 0, 1);
}

.login-form::after {
  content: "";
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background: rgba(255, 255, 255, 0.8);
  z-index: -1;
  filter: blur(30px);
}

:deep(.el-input) .el-input-group__append {
  cursor: pointer;
  padding: 0;
}
</style>
