from flask import Blueprint, jsonify, request
from backend.app.config import API_PREFIX
from backend.app.services.create_captcha import captcha_image
from backend.app.utils.response import BaseResource
from backend.app.services.redis_helper import RedisHelper

auth_bp = Blueprint("auth", __name__, url_prefix=f"{API_PREFIX}/auth")
redis_helper = RedisHelper()  # 🔥 在接口文件中实例化 RedisHelper

@auth_bp.route("/captchaImage", methods=["GET"])
def get_captcha_image():
    """获取验证码图片"""
    img_base64, uuid, answer = captcha_image.generate_captcha()
    redis_helper.set_captcha(uuid, answer)
    return BaseResource.success(data={"img": img_base64, "uuid": uuid})


@auth_bp.route("/login", methods=["POST"])
def login():
    """登录"""
    data = request.json
    username = data.get("username")
    password = data.get("password")
    captcha = data.get("code")
    uuid = data.get("uuid")
    print(username, password, captcha, uuid)
    # 校验验证码
    if not captcha or not uuid:
        return BaseResource.error(message="请先获取验证码")
    correct_answer = redis_helper.get_captcha(uuid)
    redis_helper.delete(uuid)
    if not correct_answer:
        return BaseResource.error(message="验证码已过期，请重新获取")
    if captcha.lower() != correct_answer:
        return BaseResource.error(message="验证码错误")

    return BaseResource.success(data={"token": "fake_token"})