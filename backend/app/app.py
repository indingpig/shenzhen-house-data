from flask import Flask, request
import logging
import os
from routes import all_blueprints  # 引入所有蓝图

app = Flask(__name__)
log_path = os.path.join(os.path.dirname(__file__), "../logs/app.log")
# 配置日志系统
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - [API: %(message)s]"
# )
log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
log_handler = logging.FileHandler(log_path, encoding="utf-8")
log_handler.setFormatter(log_formatter)
log_handler.setLevel(logging.INFO)

@app.before_request
def log_request():
    """ 在请求进入时记录日志 """
    app.logger.info(f"{request.method} {request.path}")

@app.after_request
def log_response(response):
    """ 在请求返回后记录日志 """
    app.logger.info(f"API: {request.path}, 状态码: {response.status_code}")
    return response

# 添加日志处理器到 Flask 的 logger
app.logger.addHandler(log_handler)
app.logger.setLevel(logging.INFO)

# 统一注册蓝图
for bp in all_blueprints:
    app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
