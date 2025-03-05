import sqlite3
from datetime import datetime
import json
from regions import region_name_dict
from db_def import init_db, insert_region_data, insert_data
from pathlib import Path

db_file = 'hello.db'
json_file_folder = 'house_data'

def import_file(dir_path):
    file_path = Path(dir_path)
    for item in file_path.iterdir():
        if item.is_file():
            open_file(item)

def open_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    target_data = json_data['data']
    insert_data(db_file, target_data)
if __name__ == '__main__':
    # 初始化数据库
    # init_db(db_file)
    # 插入地区数据
    # insert_region_data('hello.db', region_name_dict)
    import_file(json_file_folder)
