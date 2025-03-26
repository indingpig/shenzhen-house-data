from backend.app.services.create_captcha import captcha_image
from backend.app.services.redis_helper import RedisHelper


def create_captcha():
    """生成验证码"""
    img_base64, uuid, answer = captcha_image.generate_captcha()
    with RedisHelper() as redis_helper:
        redis_helper.set_redis_data(uuid, answer)
    return img_base64, uuid


def check_captcha(uuid=None, code=None):
    """校验验证码"""
    if not uuid or not code:
        return False, '请先获取验证码'
    with RedisHelper() as redis_helper:
        correct_answer = redis_helper.get_redis_data(uuid)
        redis_helper.delete(uuid)
    if not correct_answer:
        return False, '验证码已过期，请重新获取'
    if code.lower() == correct_answer:
        return True, '验证码正确'