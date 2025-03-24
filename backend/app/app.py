from flask import Flask, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from backend.app.models.logHandler import logger
from routes import all_blueprints  # 引入所有蓝图
from backend.app.utils.dataBase import DATABASE

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "your-secret-key"  # 更换为安全的密钥
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
db = DATABASE()
app.config["DATABASE"] = db  # 把 Database 实例挂载到 app

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
