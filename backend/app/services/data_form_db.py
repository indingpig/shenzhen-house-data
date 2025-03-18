import sqlite3
from datetime import datetime
import json
def calculate_salary(
    salary,
    shebao_base=None,
    gjj_base=None,
    gjj_rate=0.05,
    other_deduction=0
):
    """
    计算深圳社保、公积金、个人所得税及税后工资
    :param salary: 税前月薪
    :param shebao_base: 社保基数（默认等于salary）
    :param gjj_base: 公积金基数（默认等于salary）
    :param gjj_rate: 公积金缴存比例（5%-12%）
    :param other_deduction: 其他专项附加扣除（如子女教育等）
    :return: 包含各项金额的字典
    """
    # 设置社保和公积金基数
    shebao_base = shebao_base if shebao_base is not None else salary
    gjj_base = gjj_base if gjj_base is not None else salary

    # 计算社保个人缴纳部分（养老8% + 医疗2% + 失业0.5%）
    shebao_personal = shebao_base * (0.08 + 0.02 + 0.005)  # 合计10.5%

    # 计算公积金个人部分
    gjj_personal = gjj_base * gjj_rate

    # 计算应纳税所得额（5000为个税起征点）
    taxable_income = salary - shebao_personal - gjj_personal - 5000 - other_deduction
    taxable_income = max(taxable_income, 0)  # 确保不为负数

    # 计算个人所得税（使用2023年最新税率表）
    if taxable_income <= 0:
        tax = 0
    else:
        tax_rates = [
            (3000, 0.03, 0),
            (12000, 0.10, 210),
            (25000, 0.20, 1410),
            (35000, 0.25, 2660),
            (55000, 0.30, 4410),
            (80000, 0.35, 7160),
            (float('inf'), 0.45, 15160)
        ]
        for limit, rate, deduction in tax_rates:
            if taxable_income <= limit:
                tax = taxable_income * rate - deduction
                break
        tax = max(tax, 0)  # 确保不为负数

    # 计算税后工资
    after_tax_salary = salary - shebao_personal - gjj_personal - tax

    return {
        "社保个人缴纳": round(shebao_personal, 2),
        "公积金个人缴纳": round(gjj_personal, 2),
        "应纳税所得额": round(taxable_income, 2),
        "个人所得税": round(tax, 2),
        "税后工资": round(after_tax_salary, 2)
    }

# 使用示例
result = calculate_salary(
    salary=17800,
    shebao_base=17800,  # 可修改为实际社保基数
    gjj_base=17800,     # 可修改为实际公积金基数
    gjj_rate=0.05,      # 公积金比例范围5%-12%
    other_deduction=0   # 可添加专项附加扣除
)

print("计算结果：")
for key, value in result.items():
    print(f"{key}: {value}元")