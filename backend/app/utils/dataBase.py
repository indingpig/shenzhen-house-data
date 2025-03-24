import sqlite3
from backend.app.models.logHandler import logger
from backend.app.config import DB_PATH

class DATABASE:
    def __init__(self, db_file=DB_PATH):
        self.path = db_file

    def connect(self):
        return sqlite3.connect(self.path)

    def create_table(self, table_name, columns):
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
                conn.commit()
        except Exception as e:
            logger.error(f'SQL 创建表错误，错误信息：{e}')
            return {"success": False, "error": str(e)}

    # 插入数据
    def insert_data(self, table, data):
        try:
            columns = ", ".join(data.keys())  # 获取列名
            placeholders = ", ".join(["?"] * len(data))  # 生成占位符
            values = tuple(data.values())  # 获取值
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(query, values)
                conn.commit()
                logger.info(f"成功插入数据: {data} 到 {table}")
                return {"success": True}
        except Exception as e:
            logger.error(f'SQL 插入数据错误，错误信息：{e}')
            return {"success": False, "error": str(e)}
    
    # 查询单条数据
    def fetch_one(self, sql, params=None):
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(sql, params)
                return cursor.fetchone()
        except Exception as e:
            logger.error(f'SQL 语句错误：{sql}，参数: {params}, 错误信息：{e}')
            return {"success": False, "error": str(e)}


    # 查询所有数据
    def fetch_all(self, sql, params=None):
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(sql, params)
                return cursor.fetchall()
        except Exception as e:
            logger.error(f'SQL 语句错误：{sql}，参数: {params}, 错误信息：{e}')
            return {"success": False, "error": str(e)}