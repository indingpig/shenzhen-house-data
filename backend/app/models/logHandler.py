import logging
from backend.app.config import LOG_PATH

# 配置日志系统
log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
log_handler = logging.FileHandler(LOG_PATH, encoding="utf-8")
log_handler.setFormatter(log_formatter)
log_handler.setLevel(logging.INFO)

logger = logging.getLogger("app")
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)