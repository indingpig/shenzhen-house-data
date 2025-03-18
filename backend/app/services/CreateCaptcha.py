from PIL import Image, ImageDraw, ImageFont
import random
import os

# 使用相对路径
REQUIRED_FONTS = [
    os.path.join(os.path.dirname(__file__), '../fonts/a.ttf'),  # 相对路径引用 a.ttf
    os.path.join(os.path.dirname(__file__), '../fonts/b.ttf')   # 相对路径引用 b.ttf
]

def generate_math_captcha(width=160, height=60):
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)
    if operator == '+':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif operator == '-':
        num1 = random.randint(1, 20)
        num2 = random.randint(1, num1)
    elif operator == '*':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    else:
        num2 = random.randint(1, 10)
        num1 = num2 * random.randint(1, 10) # 避免除法结果为小数
    expression = f"{num1} {operator} {num2} = ?"
    answer = int(eval(f"{num1} {operator} {num2}"))

    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()  # 可换成 ttf 字体
    draw.text((20, 20), expression, font=font, fill=(0, 0, 0))
    image.show()
    return expression, answer


question, answer = generate_math_captcha()
print(f"验证码题目: {question}, 答案: {answer}")