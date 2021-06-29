import csv
province = []
value = []
import os
os.chdir('//code_workplace/Pycharm/Covid_data_visual/templates')
with open('/code_workplace/Pycharm/Covid_data_visual/spider/data/in_hubei.csv','r',encoding='utf-8')as f:
    reader = csv.reader(f)
    for line in reader:
        print(line[0])
        print(line[1])
        print(line[2])
        if line[0] == '20200110':
            province.append(line[1])
            value.append('{}%'.format(line[2]))
values = []
data = []
for i in range(len(province)):            
    values.append((province[i][:2],value[i]))
    data.append((province[i][:2],'湖北'))



from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

c = (
    Geo()
        .add_schema(
        maptype="china",
        itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"),
    )
        .add(
        "",
        values,
        type_=ChartType.EFFECT_SCATTER,
        color="white",
    )
        .add(
        "geo",
        data,
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="blue"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
    )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Geo-Lines-background"))
        .render("in_hubei.html")
)