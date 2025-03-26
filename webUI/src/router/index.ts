import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router';
import nProgress from 'nprogress';
import { Local } from '@/utils/storage';
import 'nprogress/nprogress.css';

const Layouts = () => import('@/layouts/index.vue');

export const constantRoutes: RouteRecordRaw[] = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login/index.vue'),
  },
  {
    path: '/',
    component: Layouts,
    redirect: '/dashboard',
    children: [
      {
        path: 'dashboard',
        component: () => import('@/views/Dashboard/index.vue'),
        name: 'Dashboard',
        meta: {
          title: '首页',
          elIcon: 'Odometer',
          affix: true,
          alwaysShow: true,
        },
      },
    ],
  },
  {
    path: '/house',
    component: Layouts,
    redirect: '/house/data-index',
    name: 'HouseManage',
    meta: {
      title: '房产管理',
      elIcon: 'Shop',
      alwaysShow: true,
    },
    children: [
      {
        path: '/data-index',
        component: () => import('@/views/House/index.vue'),
        name: 'HouseData',
        meta: {
          title: '房产数据',
          elIcon: 'School',
          affix: true,
        },
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: constantRoutes,
});

router.beforeEach((to, from, next) => {
  nProgress.start();
  const token = Local.get('token');
  if (to.path !== '/login' && !token) {
    next({ path: '/login' });
  } else {
    next();
  }
});

router.afterEach(() => {
  nProgress.done();
});

export default router;
