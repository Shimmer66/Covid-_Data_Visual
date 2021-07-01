import csv
import re
import requests
#微博ID
def get_id():
    id_list = []
    with open('/code_workplace/Pycharm/Covid_data_visual/spider/data/weibo_id.csv', 'r', encoding='utf-8')as f:
        reader = csv.reader(f)
        for line in reader:
            id_list.append(line[0])
    return id_list
#获取json内容
def get_content(id):
    url = 'https://m.weibo.cn/status/{}'.format(id)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    }
    r = requests.get(url=url, headers=headers).text
    return r
#保存微博数据
def save_data(id,r):
    with open('/code_workplace/Pycharm/Covid_data_visual/spider/data/weibo_content.csv', 'a', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        try:
            text = re.findall('"text":(.*)', r)[0].replace('\n', '')
            t = re.findall('[\u4e00-\u9fa5]', text)
            writer.writerow(id,[''.join(t)])
        except:
            pass
def main():
    with open('data/weibo_content.csv', 'w', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        writer.writerow(['content','id'])
    id_list = get_id()
    for id in id_list:
        r = get_content(id)
        save_data(id,r)


if __name__ == '__main__':
    main()
