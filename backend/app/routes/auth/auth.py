from flask import Blueprint, jsonify, request, current_app
from datetime import datetime, timedelta
import requests
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
        return BaseResource.success(message="请先获取验证码",code=1100)
    correct_answer = redis_helper.get_captcha(uuid)
    redis_helper.delete(uuid)
    if not correct_answer:
        return BaseResource.success(message="验证码已过期，请重新获取", code=1100)
    if captcha.lower() != correct_answer:
        return BaseResource.success(message="验证码错误", code=1100)

    return BaseResource.success(data={"token": "fake_token"})

@auth_bp.route("/get_bing_picture", methods=["GET"])
def get_bing_picture():
    day = request.args.get("day")
    if not day:
        return BaseResource.error(message="ssd 不能为空", code=1100)
    day_now = datetime.now() - timedelta(days=int(day))
    ssd = day_now.strftime('%Y%m%d') + '_0700'
    """获取必应每日一图"""
    url = f'https://cn.bing.com/hp/api/v1/imagegallery?format=json&ssd={ssd}_0700&FORM=BEHPTB&ensearch=1'
    response = requests.get(url)
    if response.status_code != 200:
        return BaseResource.error(message="获取图片失败", code=1100)
    try:
        data = response.json()
        images_list = data.get('data').get('images')
        image = images_list[int(day)].get('imageUrls').get('landscape').get('ultraHighDef')
        return BaseResource.success(data={"url": image})
    except Exception as e:
        current_app.logger.error(
            f"API: {request.path}, 方法: {get_bing_picture.__name__}, 错误: {e}",
        )
        return BaseResource.error(message="获取图片失败", code=1100)