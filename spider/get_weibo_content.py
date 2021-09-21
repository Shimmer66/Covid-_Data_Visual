import csv
import re

import pymysql
import requests
import db
# 数据库连接

db = pymysql.connect(**db.config)
cursor = db.cursor()
def get_id():
    id_list = []
    with open('data/weibo_id.csv', 'r', encoding='utf-8')as f:
        reader = csv.reader(f)
        for line in reader:
            id_list.append(line[0])
    return id_list

def save_db(id,r):
    # sql = 'truncate table weibo'
    # cursor.execute(sql)
    # db.commit()
    try:
        text = re.findall('"text":(.*)', r)[0].replace('\n', '')
        t = re.findall('[\u4e00-\u9fa5]', text)
        content = ''.join(t)
        # print()
        b = ['weiboid', 'content']
        a = []
        a.append(id)
        a.append(content)
        tablename = 'weibo'
        data = dict(zip(b, a))
        print(data)
        # 获取到一个以键且为逗号分隔的字符串，返回一个字符串
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=tablename, keys=keys, values=values)
        # 这里的第二个参数传入的要是一个元组
        if cursor.execute(sql, tuple(data.values())):
            print('users')
            db.commit()

    except:
        pass


def get_content(id):
    url = 'https://m.weibo.cn/status/{}'.format(id)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    }
    r = requests.get(url=url, headers=headers).text
    return r


def save_csv(id,r):
    with open('/code_workplace/Pycharm/Covid_data_visual/spider/data/weibo_content.csv', 'a', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        try:
            text = re.findall('"text":(.*)', r)[0].replace('\n', '')
            t = re.findall('[\u4e00-\u9fa5]', text)
            writer.writerow([id,''.join(t)])
        except:
            pass





def main():
    with open('/code_workplace/Pycharm/Covid_data_visual/spider/data/weibo_content.csv', 'a', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        writer.writerow(['content','id'])
    id_list = get_id()
    for id in id_list:
        print('===================={}=================='.format(id))
        r = get_content(id)
        save_db(id,r)


if __name__ == '__main__':
    main()