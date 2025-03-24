import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router';
import nProgress from 'nprogress';
import { Local } from '@/utils/storage';
import 'nprogress/nprogress.css';

const Layouts = () => import('@/layouts/index.vue');

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
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
            svgIcon: 'dashboard',
            affix: true,
          },
        },
      ],
    },
  ],
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
