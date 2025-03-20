<template>
  <svg class="svg-icon">
    <use :href="symbolId" />
  </svg>
</template>

<script setup lang="ts">
import { computed, withDefaults } from 'vue';
interface Props {
  prefix?: string
  name: string
}

defineOptions({
  name: 'SvgIcons'
});

const props = withDefaults(defineProps<Props>(), {
  prefix: '#icon-',
  name: ''
});

const symbolId = computed(() => `#icon-${props.name}`);
</script>

<style scoped lang="scss">
.svg-icon {
  width: 1em;
  height: 1em;
  fill: currentColor;
  overflow: hidden;
}
</style>
