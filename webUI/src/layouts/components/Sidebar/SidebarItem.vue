<template>
  <div>
    <template v-if="!alwaysShowRootMenu && theOnlyOneChild && !theOnlyOneChild.children">
      <router-link v-if="theOnlyOneChild.meta" :to="theOnlyOneChild.path">
        <el-menu-item :index="theOnlyOneChild.path">
          <SvgIcon v-if="theOnlyOneChild.meta.svgIcon" :name="theOnlyOneChild.meta.svgIcon" />
          <component v-else-if="theOnlyOneChild.meta.elIcon" :is="theOnlyOneChild.meta.elIcon" class="el-icon" />
          <template v-if="theOnlyOneChild.meta.title" #title>
            {{ theOnlyOneChild.meta.title }}
          </template>
        </el-menu-item>
      </router-link>
    </template>
    <el-sub-menu v-else :index="props.item.path" teleported>
      <template #title>
        <SvgIcon v-if="props.item.meta?.svgIcon" :name="props.item.meta.svgIcon" />
        <component v-else-if="props.item.meta?.elIcon" :is="props.item.meta.elIcon" class="el-icon" />
        <span v-if="props.item.meta?.title">{{ props.item.meta.title }}</span>
      </template>
      <template v-if="props.item.children">
        <SidebarItem v-for="child in showingChildren" :key="child.path" :item="child" :base-path="child.path" />
      </template>
    </el-sub-menu>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { ElMenuItem, ElSubMenu } from 'element-plus';
import { type RouteRecordRaw } from "vue-router"
defineOptions({
  name: 'SidebarItem'
});
interface Props {
  item: RouteRecordRaw
  basePath?: string
}
const props = withDefaults(defineProps<Props>(), {
  basePath: ""
})
/** 是否始终显示根菜单 */
const alwaysShowRootMenu = computed(() => props.item.meta?.alwaysShow)

/** 显示的子菜单 */
const showingChildren = computed(() => {
  return props.item.children?.filter((child) => !child.meta?.hidden) ?? []
})

/** 显示的子菜单数量 */
const showingChildNumber = computed(() => {
  return showingChildren.value.length
})
/** 唯一的子菜单项 */
const theOnlyOneChild = computed(() => {
  console.log(showingChildren.value)
  const number = showingChildNumber.value
  switch (true) {
    case number > 1:
      return null
    case number === 1:
      return showingChildren.value[0]
    default:
      return { ...props.item }
  }
})
</script>

<style scoped></style>
