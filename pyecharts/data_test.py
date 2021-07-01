import pyecharts.options as opts
from pyecharts.charts import MapGlobe
from pyecharts.faker import POPULATION
import os
import pandas as pd
from pyecharts.charts import Map,Map3D,Tab
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType, ChartType
data = [x for _, x in POPULATION[1:]]
low, high = min(data), max(data)
print(data)
print(POPULATION[1:])
c = (
    MapGlobe()
    .add_schema()
    .add(
        type_=ChartType.BAR3D,
        maptype="world",
        series_name="World Population",
        data_pair=POPULATION[1:],
        is_map_symbol_show=False,
        label_opts=opts.LabelOpts(is_show=False),
    )
        .add(
        maptype="world",
        series_name="Worltion",
        data_pair=POPULATION[1:],
        is_map_symbol_show=False,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            min_=low,
            max_=high,
            range_text=["max", "min"],
            is_calculable=True,
            range_color=["lightskyblue", "yellow", "orangered"],
           title_opts=opts.TitleOpts(title="全国疫情分布")

        )
    )
    .render("map_globe_base.html")
)
