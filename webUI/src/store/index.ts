import { createPinia, type PiniaPluginContext } from 'pinia';
import { toRef, ref } from 'vue';
import { ElMessage } from 'element-plus';

const myPlugin = ({ store }: PiniaPluginContext) => {
  if (!store.$state.hasOwnProperty('hello')) {
    store.$state.hello = ref<string>('hello world');
  }
  store.hello = toRef(store.$state, 'hello');
  store.$reset = () => {
    store.hello = 'hello world';
  };
  store.$message = ({ message, type }: { message: string; type: 'success' | 'warning' | 'info' | 'error' }) => {
    ElMessage({
      message,
      type: type,
    });
  };
};

const pinia = createPinia();

pinia.use(myPlugin);

export { pinia };
