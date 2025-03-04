import sqlite3
import json

region_name_dict = {
    '南山': 'nanShan',
    '福田': 'fuTian',
    '罗湖': 'luoHu',
    '宝安': 'baoAn',
    '龙岗': 'longGang',
    '盐田': 'yanTian',
    '坪山': 'pingShan',
    '光明': 'guangMing',
    '龙华': 'longHua',
    '大鹏': 'daPeng',
    '深圳': 'shenZhen',
    '深汕': 'shenShan'
}


def get_ts_data_json():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM ts_data
        ORDER BY month ASC
    ''')
    result = cursor.fetchall()
    conn.close()
    # for region_name, value, month in result:
    en_region = sorted(set(region_name_dict.values()))
    print(en_region)

if __name__ == '__main__':
    data_list = []
    get_ts_data_json()
