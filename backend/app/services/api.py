import requests
from datetime import datetime
from pathlib import Path


url = 'https://zjj.sz.gov.cn:8004/api/marketInfoShow/getEsfCjxxGsMonthData'

class GetHouseData:
    __json_file_folder__ = 'house_data'
    def __init__(self, url):
        self.url = url

    def get_house_data(self):
        response = requests.post(self.url)
        data = response.json()
        print(data)
        print(data['data']['xmlDateMonth'])

    @staticmethod
    def folder_files():
        file_path = Path(GetHouseData.__json_file_folder__)
        file_path.mkdir(parents=True, exist_ok=True)
        for item in file_path.iterdir():
            if item.is_file():
                print(item)

get_house_data = GetHouseData(url)

# get_house_data.get_house_data()
print(get_house_data.folder_files())