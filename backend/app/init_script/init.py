# 数据库的初始化脚本

from backend.app.utils.dataBase import DATABASE
from backend.app.services.regions import region_name_dict
import bcrypt
from backend.app.config import INIT_PASSWORD


def init_region_table():
    db = DATABASE()
    columns = 'id INTEGER PRIMARY KEY AUTOINCREMENT, region_id TEXT UNIQUE NOT NULL, region_name TEXT NOT NULL'
    db.create_table('regions', columns)
    for region_name, region_id in region_name_dict.items():
        db.insert_data('regions', {'region_id': region_id, 'region_name': region_name})

# init_region_table()

def hash_password(password: str) -> str:
    """Hash a password for storing."""
    salt = bcrypt.gensalt()  # 生成随机盐
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # 存入数据库

def init_user_table():
    db = DATABASE()
    columns = 'id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL'
    db.create_table('users', columns)
    db.insert_data('users', {'username': 'admin', 'password': hash_password(INIT_PASSWORD)})

# init_user_table()