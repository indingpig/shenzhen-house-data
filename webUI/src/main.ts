import '@/assets/scss/main.scss';
import '@/assets/main.css';
import 'element-plus/dist/index.css';
import 'element-plus/theme-chalk/dark/css-vars.css';
import { createApp } from 'vue';
import { loadPlugins } from '@/plugins';
import { loadSvg } from '@/icons';
import App from './App.vue';
import router from './router';
import { pinia } from '@/store';

const app = createApp(App);

app.use(pinia).use(router);
loadPlugins(app);
loadSvg(app);

router.isReady().then(() => {
  app.mount('#app');
});
