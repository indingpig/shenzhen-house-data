from flask import jsonify, make_response, request
import json
from functools import wraps
# 定义通用的响应包装函数
def wrap_response(data=None, message=None, status_code=200, code=None):
    response_dict = {
        "status": status_code is 200,
        "success": message is None,
        "data": data,
        "code": code,
        "message": message if message else "",
    }
    print(data, message, status_code, message)
    response_json = json.dumps(response_dict, ensure_ascii=False)  # 确保中文字符不转换
    return make_response(response_json, status_code, {"Content-Type": "application/json"})

class BaseResource:
    """基础资源类，提供通用 API 响应"""

    @staticmethod
    def success(data=None, message=None, status_code=200, code=200):
        """返回成功响应"""
        return wrap_response(data, message, status_code=status_code, code=code)

    @staticmethod
    def error(data=None, message="Error", status_code=400, code=400):
        """返回失败响应"""
        return wrap_response(data, message, status_code, code)

    @staticmethod
    def paginate(queryset, page=1, per_page=10):
        """返回分页数据"""
        total = len(queryset)
        start = (page - 1) * per_page
        end = start + per_page
        data = queryset[start:end]

        return wrap_response({
            "total": total,
            "page": page,
            "per_page": per_page,
            "data": data
        })

    @staticmethod
    def validate_json(required_keys):
        """验证 JSON 请求体的装饰器"""

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                data = request.get_json()
                if not data:
                    return BaseResource.error(message="Missing JSON body", status_code=400)

                missing_keys = [key for key in required_keys if key not in data]
                if missing_keys:
                    return BaseResource.error(message=f"Missing keys: {', '.join(missing_keys)}", status_code=400)
                return func(*args, **kwargs, data=data)
            return wrapper
        return decorator

    @staticmethod
    def make_response(data=None, error=None, status_code=200):
        return wrap_response(data, error, status_code)