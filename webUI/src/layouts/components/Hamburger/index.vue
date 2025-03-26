<template>
  <div @click="toggleClick">
    <el-icon :size="20" class="icon">
      <Fold v-if="props.isActive" />
      <Expand v-else />
    </el-icon>
  </div>
</template>

<script setup lang="ts">
import { ElIcon } from "element-plus";
import { Expand, Fold } from "@element-plus/icons-vue"
const props = withDefaults(defineProps<{
  isActive: boolean
}>(), {
  isActive: false
})
defineOptions({
  name: 'HamBurger'
})
const emit = defineEmits<{
  toggleClick: []
}>()
const toggleClick = () => {
  emit('toggleClick')
}
</script>

<style scoped></style>
