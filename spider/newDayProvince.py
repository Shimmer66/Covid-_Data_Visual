import requests
import json
from bs4 import BeautifulSoup
import re
import datetime
import os
import time
import pymysql
import csv
# 数据库连接
config = {
    'host': '127.0.0.1'
    , 'user': 'root'
        , 'password': 'why..219'
    , 'database': 'Covid'
    , 'charset': 'utf8'
    , 'port': 3306  # 注意端口为int 而不是str
}
db = pymysql.connect(**config)
cursor = db.cursor()
# while True:

url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
save_path = ['spider/data/covid_city.csv', 'spider/data/covid_virus_trip.csv', 'spider/data/covid_rumor.csv']
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}


def save_db(table):
    sql = 'truncate table nowprovince'
    cursor.execute(sql)
    db.commit()

    for data in table:
        tablename = 'nowprovince'
        # 获取到一个以键且为逗号分隔的字符串，返回一个字符串
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=tablename, keys=keys, values=values)
        # 这里的第二个参数传入的要是一个元组
        if cursor.execute(sql, tuple(data.values())):
            print('users')
            db.commit()

def save_data(table):
    with open('data/newDayProvince.csv', 'w', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp)
        writer.writerow(table[1].keys())
        for line in table:
            writer.writerow(line.values())

def get_data():
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html.parser')
    get_data1 = soup.find_all('script', attrs={'id': 'getAreaStat'})
    get_data2 = get_data1[0].string
    RE = re.compile('\[.*\]')
    data_clear = re.findall(RE, get_data2)
    data_json = json.loads(data_clear[0])  # 读取json数据
    Number_of_China_provinces = len(data_json)  # 查看有几个省市，用于遍历。由常识可知，中华人民共和国有34个省级行政区域，包括23个省，5个自治区，4个直辖市，2个特别行政区。
    keys = ['province', 'confirmedCount', 'deadCount', 'curedCount']
    table = []
    for provinces in range(Number_of_China_provinces):
        provinceName = data_json[provinces]['provinceShortName']
        confirmedCount = data_json[provinces]['confirmedCount']
        deadCount = data_json[provinces]['deadCount']
        curedCount = data_json[provinces]['curedCount']
        values = []
        values.extend([provinceName, confirmedCount, deadCount, curedCount])
        data = {}
        data = dict(zip(keys, values))
        table.append(data)
    print(table)
    save_db(table)
    return table

if __name__ == '__main__':
    get_data()
