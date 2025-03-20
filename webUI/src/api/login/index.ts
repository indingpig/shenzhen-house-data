import { request } from '@/utils/service';
import type * as Login from './types';

/** 获取登录验证码 */
export function getLoginCodeApi() {
  return request<Login.LoginCodeResponseData>({
    url: 'auth/captchaImage',
    method: 'get',
  });
}

export function loginApi(data: Login.LoginRequestData) {
  return request<Login.LoginResponseData>({
    url: 'auth/login',
    method: 'post',
    data,
  });
}
