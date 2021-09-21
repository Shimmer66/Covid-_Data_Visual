import csv
import json
import re
import pymysql
import requests
# 数据库连接
import db
from bs4 import BeautifulSoup
db = pymysql.connect(**db.config)
cursor = db.cursor()
url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
save_path = ['spider/data/covid_city.csv', 'spider/data/covid_virus_trip.csv', 'spider/data/covid_rumor.csv']
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

def save_csv(table):
    with open('data/allDayCity.csv', 'w', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp)
        writer.writerow(table[1].keys())
        for line in table:
            writer.writerow(line.values())
def save_db(table):
    # # sql = 'truncate table nowcity'
    # cursor.execute(sql)
    # db.commit()

    for data in table:
        tablename = 'nowcity'
        # 获取到一个以键且为逗号分隔的字符串，返回一个字符串
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=tablename, keys=keys, values=values)
        # 这里的第二个参数传入的要是一个元组
        if cursor.execute(sql, tuple(data.values())):
            print('users')
            db.commit()
def get_data():
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html.parser')
    get_data1 = soup.find_all('script', attrs={'id': 'getAreaStat'})
    get_data2 = get_data1[0].string
    RE = re.compile('\[.*\]')
    data_clear = re.findall(RE, get_data2)
    data_json = json.loads(data_clear[0])  # 读取json数据
    Number_of_China_provinces = len(data_json)  # 查看有几个省市，用于遍历。
    # print(data_json)
    keys = ['province', 'city', 'confirmedCount', 'deadCount', 'curedCount']
    table = []
    for provinces in range(Number_of_China_provinces):
        provinceName = data_json[provinces]['provinceShortName']
        # print(''',provinceName,"'",end=',')
        cityName = data_json[provinces]['provinceShortName']
        totalConfirmedCount = data_json[provinces]['confirmedCount']
        totalDeadCount = data_json[provinces]['deadCount']
        totalCuredCount = data_json[provinces]['curedCount']
        values = []
        values.extend([provinceName, cityName, totalCuredCount, totalDeadCount, totalConfirmedCount])
        data = {}

        data = dict(zip(keys, values))
        table.append(data)
        for line in data_json[provinces]['cities']:
            # print( provinceName ,line)
            cityName = line['cityName']
            if cityName.endswith('盟') or cityName.endswith('区') or cityName.endswith('师'):
                print(cityName)
            else:
                cityName = cityName + '市'
            # print(cityName)

            # print(values)

            # print(type(cityName))
            confirmedCount = line['confirmedCount']
            deadCount = line['deadCount']
            curedCount = line['curedCount']
            values = []
            values.extend([provinceName, cityName, confirmedCount, deadCount, curedCount])
            data = {}
            print(values)
            data = dict(zip(keys, values))
            table.append(data)
            # print(data)
    print(table)
    save_db(table)
    # return table

if __name__ == '__main__':
    get_data()
