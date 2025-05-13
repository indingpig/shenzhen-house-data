import { ref } from 'vue';
import { pinia } from '@/store';
import { defineStore } from 'pinia';
import { useRouter } from 'vue-router';
import { Local } from '@/utils/storage';

export const useUserStore = defineStore('user', () => {
  const token = ref<string>(Local.get('token') || '');
  const username = ref<string>('');
  const router = useRouter();
  const logout = () => {
    Local.remove('token');
    token.value = '';
    router.push('/login');
  };
  return {
    token,
    username,
    logout,
  };
});

/**
 * 在 SPA 应用中可用于在 pinia 实例被激活前使用 store
 * 在 SSR 应用中可用于在 setup 外使用 store
 */
export function useUserStoreHook() {
  return useUserStore(pinia);
}
