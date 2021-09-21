#生成各个省份地图



import os
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Map
os.chdir('//code_workplace/Pycharm/Covid_data_visual/templates')
data = pd.read_csv('/code_workplace/Pycharm/Covid_data_visual/spider/data/allDayCity.csv')
data1 = pd.DataFrame(data[~data.city.str.contains('境外|外地|省级|兵团|待明确')])
#
data1.reset_index(drop=True, inplace=True)
pd.set_option('display.max_rows', None)

province = list(pd.read_csv('/code_workplace/Pycharm/Covid_data_visual/spider/data/newDayProvince.csv')['provinceName'])

for i in province:
    confirm = []
    dead = []
    heal = []
    city = []
    # print(i)
    for j in range(len(data1)):
        # print(data['city'].isin(['境外', '外地', '省级', '兵团']))
        # print(data['province'][j])
        if (i == data1['province'][j]):
            confirm.append(int(data1['confirmedCount'][j]))
            dead.append(int(data1['deadCount'][j]))
            heal.append(int(data['curedCount'][j]))
            city.append(data1['city'][j])
    if (len(city) > 1):
        confirm.pop(0)
        dead.pop(0)
        heal.pop(0)
        city.pop(0)
    # print(city)
    print([list(z) for z in zip(city,confirm)])
    c = (

        Map()
            .add("累计确诊", [list(z) for z in zip(city, confirm)], i)

            .add("累计治愈", [list(z) for z in zip(city, heal)], i)
            .add("累计死亡", [list(z) for z in zip(city, dead)], i)

            .set_global_opts(
            title_opts=opts.TitleOpts(title="{}疫情地图".format(i)), visualmap_opts=opts.VisualMapOpts()
        )
            .render("{}地图.html".format(i))

    )

    #
