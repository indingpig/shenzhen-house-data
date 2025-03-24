import bcrypt

def hash_password(password: str) -> str:
    """Hash a password for storing."""
    salt = bcrypt.gensalt()  # 生成随机盐
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # 存入数据库

def check_password(password: str, hashed_password: str) -> bool:
    """Check that the provided password matches the stored one."""
    #  bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


# 示例
# raw_password = "12345678"
# hashed_pw = hash_password(raw_password)
# print("Hashed Password:", hashed_pw)

# 校验密码
# print("Password Match:", check_password(raw_password, hashed_pw))  # True
# print("Password Match:", check_password("123456", hashed_pw))  # False


