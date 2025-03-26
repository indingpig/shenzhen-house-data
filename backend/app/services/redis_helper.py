import redis
import threading
import logging
from backend.app.config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_DB, REDIS_MAX_CONN

class RedisHelper:
    _pool = None
    _lock = threading.Lock()
    def __init__(self):
        if RedisHelper._pool is None:
            with RedisHelper._lock:
                if RedisHelper._pool is None:
                    RedisHelper._pool = redis.ConnectionPool(
                        host=REDIS_HOST,
                        port=REDIS_PORT,
                        password=REDIS_PASSWORD,
                        db=REDIS_DB,
                        decode_responses=True,
                        max_connections=REDIS_MAX_CONN
                    )
        self.client = redis.Redis(connection_pool=RedisHelper._pool)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    """设置redis数据"""
    def set_redis_data(self, data_id: str, data: str, expire: int=120):
        try:
            self.client.setex(data_id, expire, data)
            self.logger.info(f"Set data_id {data_id} with expiration {expire}s")
        except Exception as e:
            self.logger.error(f"Error setting data_id: {e}")

    def get_redis_data(self, data_id: str):
        try:
            value = self.client.get(data_id)
            self.logger.info(f"Get data_id {data_id}: {value}")
            return value
        except Exception as e:
            self.logger.error(f"Error getting data_id: {e}")
            return None

    def extend_data_expiry(self, data_id: str, new_expire: int = 3600):
        try:
            data_token = self.get_redis_data(data_id)
            if data_token:
                self.client.expire(data_id, new_expire)
                self.logger.info(f"Extend data_id {data_id} expiry to {new_expire}s")
        except Exception as e:
            self.logger.error(f"Error extending data_id expiry: {e}")

    def add_to_blacklist(self, token: str, expire: int):
        try:
            self.client.setex(f"blacklist:{token}", expire, "revoked")
            self.logger.info(f"Added token to blacklist, expires in {expire} seconds")
        except Exception as e:
            self.logger.error(f"Error adding token to blacklist: {e}")

    def is_token_blacklisted(self, token: str) -> bool:
        """检查 Token 是否在黑名单中"""
        return self.client.exists(f"blacklist:{token}") > 0

    def delete(self, data_id: str):
        try:
            self.client.delete(data_id)
            self.logger.info(f"Delete data_id {data_id}")
        except Exception as e:
            self.logger.error(f"Error deleting data_id: {e}")

    def acquire_lock(self, lock_name, expire=5):
        """获取 Redis 分布式锁"""
        try:
            result = self.client.set(lock_name, "locked", ex=expire, nx=True)
            if result:
                self.logger.info(f"Acquired lock: {lock_name}")
                return True
            else:
                self.logger.warning(f"Failed to acquire lock: {lock_name}")
                return False
        except Exception as e:
            self.logger.error(f"Error acquiring lock: {e}")
            return False

    def release_lock(self, lock_name):
        """释放 Redis 分布式锁"""
        try:
            self.client.delete(lock_name)
            self.logger.info(f"Released lock: {lock_name}")
        except Exception as e:
            self.logger.error(f"Error releasing lock: {e}")

    def exists(self, key):
        return self.client.exists(key)

    def ttl(self, key):
        return self.client.ttl(key)

    def keys(self, pattern):
        return self.client.keys(pattern)

    def close(self):
        self.client.close()
        self.logger.info("Redis connection closed")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()