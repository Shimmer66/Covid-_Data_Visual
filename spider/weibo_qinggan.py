import csv
from snownlp import SnowNLP
import pandas as  pd
import os
os.chdir('//code_workplace/Pycharm/Covid_data_visual/templates')
from pyecharts import options as opts
from pyecharts.charts import Bar


from pyecharts import options as opts
from pyecharts.charts import Bar
def emotion()->Bar:
    yq = []
    ym = []
    fk = []
    zg = []
    mg = []
    with open('/code_workplace/Pycharm/Covid_data_visual/spider/data/weibo_content.csv', 'r', encoding='utf-8')as f:
        reader = csv.reader(f)
        for line in reader:
            content = line[0]
            if '疫情' in content:
                yq.append(content)
            if '疫苗' in content:
                ym.append(content)
            if '防控' in content:
                fk.append(content)
            if '中国' in content:
                zg.append(content)
            if '美国' in content:
                mg.append(content)
    values = []
    values.append(yq)
    values.append(ym)
    values.append(fk)
    values.append(zg)
    values.append(mg)
    j_value = []
    z_value = []
    x_value = []
    for v in values:
        j = 0
        z = 0
        x = 0
        for i in v:
            score = SnowNLP(i).sentiments
            if score <= 0.4:
                x += 1
            elif 0.4 < score < 0.7:
                z += 1
            else:
                j += 1  # 积极
        j_value.append(j)
        z_value.append(z)
        x_value.append(x)
    c = (
        Bar()
            .add_xaxis(["疫情", "疫苗", "防控", "中国", "美国"])
            .add_yaxis("积极", j_value, stack="stack1")
            .add_yaxis("中级", z_value, stack="stack1")
            .add_yaxis("消极", x_value, stack="stack1")

            .set_global_opts(title_opts=opts.TitleOpts(title="微博情感分析"),
                             toolbox_opts=opts.ToolboxOpts(),
                             legend_opts=opts.LegendOpts(is_show=False),
                             )
    )
    return c;



