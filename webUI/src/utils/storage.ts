import Cookies from 'js-cookie';
import { isJson } from './other';

const __NEXT_NAME__ = 'data-house';
/**
 * window.localStorage 浏览器永久缓存
 * @method set 设置永久缓存
 * @method get 获取永久缓存
 * @method remove 移除永久缓存
 * @method clear 移除全部永久缓存
 */
export const Local = {
  // 查看 v2.4.3版本更新日志
  setKey(key: string) {
    return `${__NEXT_NAME__}:${key}`;
  },
  // 设置永久缓存
  set<T>(key: string, val: T) {
    if (val === null) return;
    if (typeof val === 'string') {
      window.localStorage.setItem(Local.setKey(key), val);
      return;
    }
    window.localStorage.setItem(Local.setKey(key), JSON.stringify(val));
  },
  // 获取永久缓存
  get(key: string) {
    const json = <string>window.localStorage.getItem(Local.setKey(key));
    if (isJson(json)) return JSON.parse(json);
    return json;
  },
  // 移除永久缓存
  remove(key: string) {
    window.localStorage.removeItem(Local.setKey(key));
  },
  // 移除全部永久缓存
  clear() {
    window.localStorage.clear();
  },
};

/**
 * window.sessionStorage 浏览器临时缓存
 * @method set 设置临时缓存
 * @method get 获取临时缓存
 * @method remove 移除临时缓存
 * @method clear 移除全部临时缓存
 */
export const Session = {
  // 设置临时缓存
  set<T>(key: string, val: T) {
    if (key === 'token') return Cookies.set(key, JSON.stringify(val));
    window.sessionStorage.setItem(Local.setKey(key), JSON.stringify(val));
  },
  // 获取临时缓存
  get(key: string) {
    if (key === 'token') return Cookies.get(key);
    const json = <string>window.sessionStorage.getItem(Local.setKey(key));
    if (json === null) return json;
    return JSON.parse(json);
  },
  // 移除临时缓存
  remove(key: string) {
    if (key === 'token') return Cookies.remove(key);
    window.sessionStorage.removeItem(Local.setKey(key));
  },
  // 移除全部临时缓存
  clear() {
    Cookies.remove('token');
    window.sessionStorage.clear();
  },
};
