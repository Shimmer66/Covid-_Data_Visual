import csv
import json
from urllib.parse import quote

import pymysql
import requests
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
def get_province():
    url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare'
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "api.inews.qq.com",
        "Origin": "https://news.qq.com",
        "Referer": "https://news.qq.com/",
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
    }

    r = requests.get(url=url, headers=headers).text
    dict = json.loads(r)
    data_list = dict['data']['provinceCompare']
    province_list = []
    for data in data_list:
        province_list.append(data)
    return province_list




def get_content(province):
    url = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province={}&'.format(quote(province))
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "api.inews.qq.com",
        "Origin": "https://news.qq.com",
        "Referer": "https://news.qq.com/",
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
    }
    r = requests.get(url=url, headers=headers).text
    return r

def save_csv(r,writer):
    dict = json.loads(r)
    data_list = dict['data']
    for data in data_list:
        data['year']=str(data['year'])+'.'+data['date']
        date = data['year']
        # print(date)
        province = data['province']
        confirm = data['confirm']
        dead = data['dead']
        heal = data['heal']

        writer.writerow([date, province, confirm, dead, heal])
        # print(1)
def save_db(table):
    b=['date', 'province', 'confirm', 'dead', 'heal']
    dict_data = json.loads(table)
    data_list = dict_data['data']

    for data in data_list:
        a = []
        data['year']=str(data['year'])+'.'+data['date']
        date = data['year']
        print(date)
        a.append(date)
        a.append(data['province'])
        a.append(data['confirm'])
        a.append( data['dead'])
        a.append(data['heal'])
        z=dict(zip(b, a))
        # print(z)
        # date,province,confirm,dead,heal
        data =  dict( zip(['date', 'province', 'confirm', 'dead', 'heal'], a))
        print(data)
        tablename = 'alldayprovince'
        # 获取到一个以键且为逗号分隔的字符串，返回一个字符串
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=tablename, keys=keys, values=values)
        # 这里的第二个参数传入的要是一个元组
        if cursor.execute(sql, tuple(data.values())):
            # print('users')
            db.commit()

def main():
    province_list = get_province()
    with open('data/everyDayProvince.csv', 'a', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'province', 'confirm', 'dead', 'heal'])
        for province in province_list:
            r = get_content(province)
            # print(r)
            save_db(r)


if __name__ == '__main__':
    main()
