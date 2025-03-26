import { type App } from 'vue';
import { loadElementPlusIcon } from './element-plus-icon';
import { loadElementPlus } from './element-plus';

export function loadPlugins(app: App) {
  loadElementPlusIcon(app);
  loadElementPlus(app);
}
