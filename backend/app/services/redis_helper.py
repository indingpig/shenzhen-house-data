import redis
import threading
import logging

class RedisHelper:
    _pool = None
    _lock = threading.Lock()
    def __init__(self, password, host='localhost', port=6379, db=0, max_connections=50):
        if RedisHelper._pool is None:
            with RedisHelper._lock:
                if RedisHelper._pool is None:
                    RedisHelper._pool = redis.ConnectionPool(
                        host=host,
                        port=port,
                        password=password,
                        db=db,
                        decode_responses=True,
                        max_connections=max_connections
                    )
        self.client = redis.Redis(connection_pool=RedisHelper._pool)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def set_captcha(self, captcha_id: str, answer: str, expire: int=120):
        try:
            self.client.setex(captcha_id, expire, answer)
            self.logger.info(f"Set captcha {captcha_id} with expiration {expire}s")
        except Exception as e:
            self.logger.error(f"Error setting captcha: {e}")

    def get_captcha(self, captcha_id: str):
        try:
            value = self.client.get(captcha_id)
            self.logger.info(f"Get captcha {captcha_id}: {value}")
            return value
        except Exception as e:
            self.logger.error(f"Error setting captcha: {e}")
            return None

    def delete(self, captcha_id: str):
        try:
            self.client.delete()
            self.logger.info(f"Delete captcha {captcha_id}")
        except Exception as e:
            self.logger.error(f"Error deleting captcha: {e}")

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