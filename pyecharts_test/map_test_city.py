
import os

import pandas as pd
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.globals import ThemeType



province=['台湾','广东','香港','上海','福建','浙江','云南','四川','北京','江苏','陕西','天津','内蒙古','河南',
'辽宁','重庆','澳门','湖北','山东','山西','甘肃','海南','宁夏','黑龙江','河北','湖南','安徽','新疆',
'江西','吉林','广西','贵州','青海','西藏']
os.chdir('//code_workplace/Pycharm/Covid_data_visual/templates')
city=[]
confirm = []
heal = []
data=pd.read_csv('/code_workplace/Pycharm/Covid_data_visual/spider/data/allDayCity.csv')

data=data[~data['city'].str.contains(
'输入|待明确|外地|兵团')]

# ,'待明确','外地','输入'
#     print(line)
# print(data)
key=['city','confirmedCount','deadCount','curedCount']
table=[]
for i in province:
    print(" def {}map(request):".format(i),    "return render(request,'{}地图.html')".format(i))




for i in province:
    city=data[data['province'].str.contains(i)]
    # print(len(city))
    if(len(city)>1):
        city = city[~city['city'].str.contains(i)]
    city=city.drop(['province'],axis=1).values
    # print(len(city))
    # city=list(city)
    # if(len(city)>1):
    table.append(city.tolist())
# print(table)

b=[]
for line in table:
    a = []
    for i in line:
        value={}
        value=dict(zip(key, i))
        # print(value)
        a.append(value)
    b.append(a)
    # print(a)
    # province同上，是一个由省份名称组成的列表，如['河南'， '山西']
    # 切记，不要带省，只要名字就行

# confirmedCount = list(data["confirmedCount"])
# confirmedCount = [list(z) for z in zip(province, confirmedCount)]  # 累计确诊
# curedCo = list(data["curedCount"])  # 累计治愈
# curedCo = [list(z) for z in zip(province, curedCo)]  # 累计确诊
# deadCount = list(data["deadCount"])  # 累计死亡
# deadCount = [list(z) for z in zip(province, deadCount)]  # 累计确诊
zz=0
for i in b:
    city=[]
    confirmedCount=[]
    curedCo=[]
    deadCount=[]
    for j in i:
        # print(j['city'])
        city.append(j['city'])
        confirmedCount.append(j['confirmedCount'])
        curedCo.append((j['curedCount']))
        deadCount.append(j['deadCount'])
    # print(city)
    curedCo = [list(z) for z in zip(city, curedCo)]  # 累计确诊
    confirmedCount = [list(z) for z in zip(city, confirmedCount)]  # 累计确诊
    deadCount = [list(z) for z in zip(city, deadCount)]  # 累计确诊
    # print(deadCount)
    # print(curedCo)
    # print(confirmedCount)
    #
    # print(province[zz])
    # print(curedCo)
    province_city = (
        Map(init_opts=opts.InitOpts(width="1500px", height="800px", theme=ThemeType.VINTAGE))
            .add("累计确诊", confirmedCount, province[zz])
            .add("累计治愈", curedCo,  province[zz])
            .add("累计死亡", deadCount,  province[zz])
            .set_global_opts(
            title_opts=opts.TitleOpts(title= province[zz] + "地图"),
            visualmap_opts=opts.VisualMapOpts(
                min_=1,
                max_=17,
                is_piecewise=True
            )
        )
            .render(path=province[zz]+ "地图.html")
    )
    zz+=1
