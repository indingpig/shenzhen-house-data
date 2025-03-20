from flask import Flask
from routes import all_blueprints  # 引入所有蓝图

app = Flask(__name__)

# 统一注册蓝图
for bp in all_blueprints:
    app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
