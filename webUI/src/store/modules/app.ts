import { ref, watch } from 'vue';
import { pinia } from '@/store';
import { defineStore } from 'pinia';
import { Local } from '@/utils/storage';
import CacheKey from '@/utils/cache-key';

export const useAppStore = defineStore('app', () => {
  const local_cache = Local.get(CacheKey.SIDEBAR_STATUS);
  const sidebarStatus = ref<boolean>(local_cache === 'true');
  const handleSidebarStatus = (status: boolean) => {
    // sidebarStatus.value = !sidebarStatus.value;
    Local.set(CacheKey.SIDEBAR_STATUS, status);
  };
  watch(sidebarStatus, (value) => {
    handleSidebarStatus(value);
  });
  const toggleSidebarStatus = () => {
    sidebarStatus.value = !sidebarStatus.value;
  };

  return {
    sidebarStatus,
    toggleSidebarStatus,
  };
});

/**
 * 在 SPA 应用中可用于在 pinia 实例被激活前使用 store
 * 在 SSR 应用中可用于在 setup 外使用 store
 */
export function useUserStoreHook() {
  return useAppStore(pinia);
}
