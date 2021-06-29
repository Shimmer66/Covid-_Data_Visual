import csv
import os

import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode



import csv
x= []
for i in range(10,30):
    x.append('2020.02.{}'.format(i))
all = []
print(x)
with open('/code_workplace/Pycharm/Covid_data_visual/spider/data/everyDayProvince.csv','r',encoding='utf-8')as f:
    reader = csv.reader(f)
    for line in reader:
        all.append(line)
        # print(all)
confirm_list = []
heal_list = []
dead_list = []
for i in x:
    # print(i)
    confirm = 0
    heal = 0
    dead =0
    for j in range(len(all)):
        # print(j)
        # print(all)
        # print(all[j][3])
        if all[j][0] == i:
            confirm += (int(all[j][2])-int(all[j-1][2]))
            heal += (int(all[j][4])-int(all[j-1][4]))
            dead += (int(all[j][3])-int(all[j-1][3]))
    confirm_list.append(confirm)
    heal_list.append(heal)
    dead_list.append(dead)
print(confirm_list)
print(heal_list)
print(dead_list)

import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

c = (
    Line()
        .add_xaxis(x)
        .add_yaxis("确诊", confirm_list)
        .add_yaxis("治愈", heal_list)
        .add_yaxis("死亡", dead_list)
        .set_global_opts(title_opts=opts.TitleOpts(title="全国每日新增情况"),
                         datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
                         )
        .render("confirm_day_add.html")
)