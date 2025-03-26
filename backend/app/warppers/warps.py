from functools import wraps
# from flask import request
# from backend.app.config import API_PREFIX

# 存放需要鉴权的路由
protected_routes = set()


def auth_required(func):
    """自定义装饰器：标记需要鉴权的路由"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    # 由于 `request.blueprint` 不能在装饰器执行时访问，我们手动拼接 URL
    module_name = func.__module__.split(".")[-2]  # 获取 Blueprint 所在目录名
    url_prefix = f"/api/v1/{module_name}"  # 生成 Blueprint 对应的前缀
    full_route = f"{url_prefix}/{func.__name__}"  # 计算完整路径
    # 记录该路由需要鉴权
    protected_routes.add(full_route)
    return wrapper