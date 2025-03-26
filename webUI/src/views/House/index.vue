<template>
  <div>
    123123
    <el-button @click="testQuery">请求</el-button>
  </div>
</template>

<script setup lang="ts">
import { getHouseApi } from '@/api/house'
defineOptions({
  name: 'HouseData'
})
const testQuery = () => {
  getHouseApi().then(res => {
    console.log(res)
  })
}
</script>

<style scoped></style>
