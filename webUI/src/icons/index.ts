import { type App } from 'vue';
import SvgIcon from '@/components/SvgIcons/index.vue'; // Svg Component
// import 'virtual:svg-icons-register';

export function loadSvg(app: App) {
  app.component('SvgIcon', SvgIcon);
}
