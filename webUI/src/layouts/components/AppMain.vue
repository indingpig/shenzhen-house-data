<template>
  <section>
    <div class="app-scrollbar">
      <router-view v-slot="{ Component, route }">
        <transition name="fade-transform" mode="out-in">
          <keep-alive>
            <component :is="Component" :key="route.path" class="app-container-grow" />
          </keep-alive>
        </transition>
      </router-view>
    </div>
  </section>
</template>

<script setup lang="ts">
defineOptions({
  name: 'AppMain'
})
</script>

<style scoped></style>
