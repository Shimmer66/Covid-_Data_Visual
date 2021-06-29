import csv
import json
from urllib.parse import quote

import requests

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

def get_data(r,writer):
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


def main():
    province_list = get_province()
    with open('data/everyDayProvince.csv', 'a', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'province', 'confirm', 'dead', 'heal'])
        for province in province_list:
            r = get_content(province)
            # print(r)
            get_data(r,writer)


if __name__ == '__main__':
    main()
