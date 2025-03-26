from flask import Flask, request
from flask_bcrypt import Bcrypt
from backend.app.warppers.warps import protected_routes
from flask_jwt_extended import JWTManager
from backend.app.models.logHandler import logger
from routes import all_blueprints  # 引入所有蓝图
from backend.app.utils.dataBase import DATABASE
from backend.app.utils.token_utils import verify_token
from backend.app.utils.response import BaseResource

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "your-secret-key"  # 更换为安全的密钥
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
db = DATABASE()
app.config["DATABASE"] = db  # 把 Database 实例挂载到 app

@app.before_request
def check_token():
    print(protected_routes, request.path)
    """ 在请求进入时检查 Token """
    if request.path in protected_routes:
        authorization = request.headers.get("Authorization")
        print(authorization)
        if not authorization:
            return BaseResource.error(message='Token 不能为空', code=401)
        token = authorization[7:]
        try:
            verify_token(token)
        except Exception as e:
            logger.error(f"Token 验证失败: {e}")
            return BaseResource.error(message='Token 验证失败', code=401)

@app.before_request
def log_request():
    """ 在请求进入时记录日志 """
    app.logger.info(f"{request.method} {request.path}")

@app.after_request
def log_response(response):
    """ 在请求返回后记录日志 """
    # app.logger.info(f"API: {request.path}, 状态码: {response.status_code}")
    logger.info(f"API: {request.path}, 状态码: {response.status_code}")
    return response


# 统一注册蓝图
for bp in all_blueprints:
    app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
