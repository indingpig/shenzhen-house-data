from flask import Blueprint, jsonify, request
from backend.app.config import API_PREFIX
from backend.app.services.create_captcha import captcha_image
from backend.app.utils.response import BaseResource

auth_bp = Blueprint("auth", __name__, url_prefix=f"{API_PREFIX}/auth")

@auth_bp.route("/captchaImage", methods=["GET"])
def get_captcha_image():
    """获取验证码图片"""
    img_base64, uuid = captcha_image.generate_captcha()
    return BaseResource.success(data={"img": img_base64, "uuid": uuid})