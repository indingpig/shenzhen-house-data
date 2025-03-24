import os

API_PREFIX = "/api/v1"
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_PASSWORD = "dongfangshuye"
REDIS_DB = 0
REDIS_MAX_CONN = 50
INIT_PASSWORD = "12345678"

DB_PATH = os.path.join(os.path.dirname(__file__), '../instance/database.db')
LOG_PATH = os.path.join(os.path.dirname(__file__), '../logs/app.log')