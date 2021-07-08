import csv
import json

import requests
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "BIDUPSID=D34E95D50B95D2C3486E16F1DEDFB86D; PSTM=1605748305; BAIDUID=D34E95D50B95D2C3D5112000A8F44BE0:FG=1; BAIDUID_BFESS=743D162601E3227638C7B4E34E8CC32B:FG=1; __yjs_duid=1_b4a2b36be319d6902e7102691e28e8011624432004957; BDRCVFR[9wJABgfFTHD]=Sgq2UtKbV53nvGbpa4WUvY; delPer=0; PSINO=2; H_PS_PSSID=34099_33968_31660_33848_34133_34073_33607_34107_34134_34118_22160; BA_HECTOR=ag2h2k05a42g81a0jq1gd7n6i0r; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PHPSESSID=rlv75vcu83nj57j08jpjm92f14; ab_sr=1.0.1_YzM0ODMwNTY0N2RlOTAyMWU4NGJkMTRjNGViMjZlZDQ5NzY4ZDIzN2IwNTEzODlkYjA0NDdjMzM1M2ZmZjQ0ZWM0YzY5YTM2YjVmMjhiZGE2ZTlkMWNkY2Q5MjI3NjNiYzYyNGFhMGU2NzNhMTM5YzczZmE4NGI3NWE0YTNkYjVlMWVmNDZmNDhmMWU4YTFkNzE4MDZiZTUwMDM4ODI5Mw==",
    "Host": "huiyan.baidu.com",
    "Referer": "https://qianxi.baidu.com/",
    "sec-ch-ua-mobile": "?0",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
}
#获取json数据
def get_date():
    url = 'https://huiyan.baidu.com/migration/historycurve.jsonp?dt=province&id=420000&startDate=20200110&endDate=20200315&type=move_in&callback=jsonp_1624497805942_5605632'
    r = requests.get(url=url, headers=headers).text
    dict = json.loads(r.replace('jsonp_1624497805942_5605632(', '').replace(')', ''))
    data_list = dict['data']['list']
    date_list = []
    for data in data_list:
        if int(data) >= 20200110:
            date_list.append(data)
    # print(date_list)
    return date_list

#流向湖北人口
def move_in(date):
    url = 'https://huiyan.baidu.com/migration/provincerank.jsonp?dt=province&id=420000&type=move_in&date={}&callback=jsonp_1624497580218_6515979'.format(
        date)
    r = requests.get(url=url, headers=headers).text
    dict = json.loads(r.replace('jsonp_1624497580218_6515979(', '').replace(')', ''))
    data_list = dict['data']['list']
    with open('data/in_hubei.csv', 'a', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        for data in data_list:
            province_name = data['province_name']
            invalue = data['value']
            writer.writerow([date, province_name, invalue])
#流出湖北人口
def move_out(date):
    url = 'https://huiyan.baidu.com/migration/provincerank.jsonp?dt=province&id=420000&type=move_out&date={}&callback=jsonp_1624498896026_5147408'.format(
        date)
    r = requests.get(url=url, headers=headers).text
    dict = json.loads(r.replace('jsonp_1624498896026_5147408(', '').replace(')', ''))
    data_list = dict['data']['list']
    with open('data/out_hubei.csv', 'a', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        for data in data_list:
            province_name = data['province_name']
            value = data['value']
            writer.writerow([date, province_name, value])
def main():
    with open('data/in_hubei.csv', 'w', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        writer.writerow(['date','province','rate'])
    with open('data/out_hubei.csv', 'w', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        writer.writerow(['date','province','rate'])
    date_list = get_date()
    for date in date_list:
        move_in(date)
        move_out(date)
if __name__ == '__main__':
    main()
