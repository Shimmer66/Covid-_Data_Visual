import os

import pandas as pd
from pyecharts.charts import Map
import pyecharts.options as opts
os.chdir('//code_workplace/Pycharm/Covid_data_visual/templates')

def world()->Map:
    #数据处理
    data=pd.read_csv('/code_workplace/Pycharm/Covid_data_visual/spider/data/country.csv')
    confirm=data['confirmedCount']
    heal=data['curedCount']
    dead=data['deadCount']
    province=data['province']
    heal_list=list(a for a in zip(province, heal))
    confirm_list=list(a for a in zip(province, confirm))
    dead_list=list(a for a in zip(province, dead))
    heal_sum = 0
    confirm_sum = 0
    dead_sum=0
    for i in range(len(heal)):
        heal_sum += heal[i]
        confirm_sum += confirm[i]
        dead_sum+=dead[i]
    # 副标题
    subtitle = "确诊数量：" + str(confirm_sum) + "例\n\n治愈数量：" + str(heal_sum) + "\n\n死亡数量："+ str(dead_sum) + "例"
    world_map= (
        Map(
            # 设置宽度，高度
            init_opts={"width": "1280px", "height": "800px"}
        )
            .add(
            "确诊数量",
            confirm_list,
            maptype="world",
            is_selected=True,
            is_map_symbol_show=False
        )
            .add(
            "治愈数量",
            heal_list,
            maptype="world",
            is_selected=False,
            is_map_symbol_show=False
        )
            .add(
            "死亡数量",
            dead_list,
            maptype="world",
            is_selected=False,
            is_map_symbol_show=False
        )
            # 系列配置
            .set_series_opts(
            # 不显示经纬度，设置颜色，字体大小
            label_opts={'is_show': 'False',
                        'color': '#fff', 'font_size': '18', 'position': 'left'},
        )
            # 全局配置
            .set_global_opts(
            # 视觉映射配置项
            visualmap_opts=opts.VisualMapOpts(min_=0, max_=int(
                heal_sum / 50)),
            # 设置左上角标题和副标题
            title_opts=opts.TitleOpts(
                title="", subtitle=subtitle, pos_left="50", pos_top="5%",
                title_textstyle_opts=opts.TextStyleOpts(font_size=15),
                subtitle_textstyle_opts=opts.TextStyleOpts(font_size=15, color='#222')
            ),
            # 图例设置
            legend_opts=opts.LegendOpts(
                selected_mode='single', pos_top="50", pos_bottom="5%", textstyle_opts=opts.TextStyleOpts(font_size=15)),
        )
    )
    return world_map

