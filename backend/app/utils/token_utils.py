from datetime import datetime, timedelta
from flask import current_app
from backend.app.models.logHandler import logger
from backend.app.services.redis_helper import RedisHelper
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
# from backend.app.app import app
# jwt = JWTManager(app)

def create_token(user_id: str, expire_seconds=3600):
    """生成 JWT token"""
    try:
        token = create_access_token(identity=user_id, expires_delta=timedelta(seconds=expire_seconds))
        with RedisHelper() as redis:
            redis.set_redis_data(user_id, token, expire_seconds)
        return token
    except Exception as e:
        logger.error(f"调用 create_token 函数错误: {e}")
        return None

def verify_token(token: str):
    """验证 JWT token"""
    try:
        user_id = get_jwt_identity()
        with RedisHelper() as redis:
            redis_token = redis.get_redis_data(user_id)
        if token == redis_token:
            return True, user_id
        else:
            return None, "Token 不匹配"
    except Exception as e:
        logger.error(f"调用 verify_token 函数错误: {e}")
        return None, str(e)

"""延长token过期时间"""
def extend_token_expire(user_id: str, expire_seconds=3600):
    try:
        with RedisHelper() as redis:
            redis.extend_data_expiry(user_id, expire_seconds)
        return True
    except Exception as e:
        logger.error(f"调用 extend_token_expire 函数错误: {e}")
        return False

"""拉黑token"""
def add_to_blacklist(token: str, expire_seconds=3600):
    try:
        with RedisHelper() as redis:
            redis.add_to_blacklist(token, expire_seconds)
        return True
    except Exception as e:
        logger.error(f"调用 add_to_blacklist 函数错误: {e}")
        return False

# JWT_SECRET_KEY = current_app.config['JWT_SECRET_KEY']

# def create_access_token(user_id: str, expire_minutes=60):
#     """生成 JWT Token"""
#     expire_time = datetime.utcnow() + timedelta(minutes=expire_minutes)
#     payload = {
#         "sub": user_id,
#         "exp": expire_time
#     }
#     token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")
#     return token, expire_minutes * 60  # 返回秒数
#
#
# def verify_token(token: str):
#     """验证 JWT Token"""
#     try:
#         payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
#         return payload["sub"], None
#     except jwt.ExpiredSignatureError:
#         return None, "Token has expired"
#     except jwt.InvalidTokenError:
#         return None, "Invalid token"
