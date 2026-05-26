import request from '@/utils/http'

/**
 * 登录
 * @param params 登录参数
 * @returns 登录响应
 */
export function fetchLogin(params: Api.Auth.LoginParams) {
  return request.post<Api.Auth.LoginResponse>({
    url: '/v1/auth/login',
    params
  })
}

/**
 * 获取用户信息
 * @returns 用户信息
 */
export function fetchGetUserInfo() {
  return request.get<Api.Auth.UserInfo>({
    url: '/v1/auth/me'
  })
}

/**
 * 注册
 * @param params 注册参数
 * @returns 用户信息
 */
export function fetchRegister(params: { username: string; password: string; email: string }) {
  return request.post<Api.Auth.UserInfo>({
    url: '/v1/auth/register',
    params
  })
}

export function changePassword(data: { old_password: string; new_password: string }) {
  return request.post<{ code: number; msg: string }>({
    url: '/v1/auth/change-password',
    data
  })
}
