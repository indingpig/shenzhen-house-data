import sqlite3
from datetime import datetime
from regions import region_name_dict
from decimal import Decimal


def init_db(db_name):
    conn = sqlite3.connect(db_name)
    conn.close()
    init_region_table(db_name)
    init_months_table(db_name)
    init_sales_table(db_name)

def init_region_table(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS regions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            region_id TEXT UNIQUE NOT NULL,
            region_name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def init_months_table(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS months (
            month_id INTEGER PRIMARY KEY AUTOINCREMENT,
            xml_date_month TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def init_sales_table(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
            month_id INTEGER NOT NULL,
            region_id TEXT NOT NULL,
            sales_area REAL NOT NULL,
            sales_count INTEGER NOT NULL,
            FOREIGN KEY (month_id) REFERENCES months(month_id),
            FOREIGN KEY (region_id) REFERENCES regions(region_id)
        )
    ''')
    conn.commit()
    conn.close()

def insert_sales_data(cursor, month, sale_data):
    sales_area = float(sale_data['sales_area'].quantize(Decimal('0.00'), rounding='ROUND_HALF_UP'))
    cursor.execute('''
        INSERT OR IGNORE INTO sales (month_id, region_id, sales_area, sales_count)
        VALUES (
            (SELECT month_id FROM months WHERE xml_date_month = ?),
            (SELECT region_id FROM regions WHERE region_id = ?),
            ?, ?
        )
    ''', (month, sale_data['region_id'], sales_area, sale_data['sales_count']))

def insert_region_data(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    for region_name, region_id in dict.items():
        cursor.execute('''
            INSERT INTO regions (region_id, region_name)
            VALUES (?, ?)
        ''', (region_id, region_name))
    conn.commit()
    conn.close()

def insert_data(db_name, target_data):
    conn = sqlite3.connect(db_name)
    try:
        # print(target_data)
        cursor = conn.cursor()
        month = datetime.strptime(target_data['xmlDateMonth'], '%Y年%m月').strftime('%Y-%m')
        # sale_data_list = []
        cursor.execute('''
            INSERT OR IGNORE INTO months (xml_date_month)
            VALUES (?)
        ''', (month,))
        shen_zheng_total_data = {
            'region_id': region_name_dict['深圳'],
            'sales_area': Decimal('0'),
            'sales_count': 0
        }
        for dataMj in target_data['dataMj']:
            for dataTs in target_data['dataTs']:
                if dataMj['name'] == dataTs['name']:
                    sale_data = {
                        'region_id': region_name_dict[dataMj['name']],
                        'sales_area': Decimal(str(dataMj['value'])),
                        'sales_count': dataTs['value']
                    }
                    shen_zheng_total_data['sales_area'] = Decimal(str(Decimal(shen_zheng_total_data['sales_area']) + Decimal(str(sale_data['sales_area']))))
                    shen_zheng_total_data['sales_count'] += sale_data['sales_count']
                    insert_sales_data(cursor, month, sale_data)
        insert_sales_data(cursor, month, shen_zheng_total_data)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        conn.close()

