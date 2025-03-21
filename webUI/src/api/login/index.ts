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

export function getBingImgApi(day: number) {
  return request({
    url: 'auth/get_bing_picture',
    method: 'get',
    params: { day },
  }) as Promise<{ url: string }>;
}
