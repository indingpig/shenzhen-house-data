from PIL import Image, ImageDraw, ImageFont,ImageFilter
import random
import os
import uuid

# 使用相对路径
REQUIRED_FONTS = [
    os.path.join(os.path.dirname(__file__), '../fonts/Hanalei-Regular.ttf'),  # 相对路径引用 a.ttf
]

FONT_PATHS = [fp for fp in REQUIRED_FONTS if os.path.exists(fp)]


class Captcha:
    def __init__(self, width=160, height=60, font_size=36, font_paths=FONT_PATHS):
        self.answer = None
        self.expression = None
        self.draw = None
        self.width = width
        self.height = height
        self.font_size = font_size
        self.font_paths = font_paths
        self.uuid = self.generate_uuid()

    def generate_captcha(self):
        # 创建空白图片
        image = Image.new('RGB', (self.width, self.height), (255, 255, 255))
        self.draw = ImageDraw.Draw(image)
        self.expression, self.answer = self.get_math()
        print(f"验证码题目: {self.expression}, 答案: {self.answer}")
        x, y_base, char_sizes = self.get_char_width()
        self.distort(x, y_base, char_sizes)
        self.add_lines()
        self.add_points()
        # 模糊处理（让 OCR 更难识别）
        image = image.filter(ImageFilter.GaussianBlur(radius=0.6))
        image.show()
        # 保存图片
        # image.save("math_captcha_multiple_fonts.png")

    # 计算每个字符的宽度
    def get_char_width(self):
        total_text_width = 0
        char_sizes = []
        if not self.expression:
            raise ValueError('Please generate captcha first')
        if not self.draw:
            raise ValueError('Please generate captcha first')
        for char in self.expression:
            font_size = random.randint(30, 40)  # 每个字符随机字体大小
            font = ImageFont.truetype(random.choice(FONT_PATHS), font_size)
            bbox = self.draw.textbbox((0, 0), char, font=font)
            text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
            total_text_width += text_width + 5  # 适当增加间距
            char_sizes.append((font, text_width, text_height))
        # 计算起始 x 位置
        x = (self.width - total_text_width) // 2
        y_base = (self.height - max(h for _, _, h in char_sizes)) // 2
        return x, y_base, char_sizes

    # 随机颜色 & 扭曲字符
    def distort(self, x, y_base, char_sizes):
        for i, char in enumerate(self.expression):
            font, text_width, text_height = char_sizes[i]
            y_offset = random.randint(-5, 5)  # 让字符有轻微的上下偏移
            text_color = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))

            self.draw.text((x, y_base + y_offset), char, font=font, fill=text_color)
            x += text_width + random.randint(2, 6)  # 随机间距

    # 添加干扰线
    def add_lines(self):
        for _ in range(random.randint(3, 6)):
            x1, y1 = random.randint(0, self.width), random.randint(0, self.height)
            x2, y2 = random.randint(0, self.width), random.randint(0, self.height)
            line_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            self.draw.line((x1, y1, x2, y2), fill=line_color, width=2)

    # 添加噪点
    def add_points(self):
        for _ in range(random.randint(50, 100)):
            x, y = random.randint(0, self.width), random.randint(0, self.height)
            dot_color = (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200))
            self.draw.point((x, y), fill=dot_color)

    @staticmethod
    def get_math():
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
            num1 = num2 * random.randint(1, 10)  # 避免除法结果为小数
        expression = f"{num1} {operator} {num2} = ?"
        answer = int(eval(f"{num1} {operator} {num2}"))
        return expression, answer

    @staticmethod
    def generate_uuid():
        return random.randint(100000, 999999)

captcha_image = Captcha()
captcha_image.generate_captcha()