import csv
import json
import random
import time
import requests


def get_id(page):
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E7%96%AB%E6%83%85&page_type=searchall&page={}'.format(
        page)
    headers = {
        "Accept": "application/json, text/plain, */*",
        "MWeibo-Pwa": "1",
        "Referer": "https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E7%96%AB%E6%83%85",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "X-XSRF-TOKEN": "9aadcc",
    }
    time.sleep(random.random()*20)
    r = requests.get(url=url, headers=headers).text
    dict = json.loads(r)
    data_list = dict['data']['cards']
    with open('data/weibo_id.csv', 'a', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        for data in data_list:
            try:
                id = data['mblog']['id']
                writer.writerow([id])
            except:
                pass


def main():
    with open('data/weibo_id.csv', 'w', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
    for page in range(1, 107):
        print('==============={}================'.format(page))
        get_id(page)


if __name__ == '__main__':
    main()
