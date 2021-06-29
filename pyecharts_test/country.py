import os

import pandas as pd
from pyecharts.charts import Map, Map3D
from pyecharts.globals import ChartType

os.chdir('//code_workplace/Pycharm/Covid_data_visual/templates')
import pyecharts.options as opts
from pyecharts.commons.utils import JsCode


def bmap3d() -> Map3D:
    BarPlace1 = {}
    data = pd.read_csv('/code_workplace/Pycharm/Covid_data_visual/spider/data/newDayProvince.csv')
    confirm = list(data['confirmedCount'])
    province = list(data['provinceName'])
    heal = list(data['curedCount'])
    heal_sum = 0
    confirm_sum = 0
    dead_sum = 0
    for i in range(len(heal)):
        heal_sum += heal[i]
        confirm_sum += confirm[i]

    # 副标题
    subtitle = "确诊数量：" + str(confirm_sum) + "例\n\n治愈数量：" + str(heal_sum) + "例"
    # print(list(confirm))
    BarPlace = {'黑龙江': [127.9688, 45.368], '上海': [121.4648, 31.2891],
                '内蒙古': [110.3467, 41.4899], '吉林': [125.8154, 44.2584],
                '辽宁': [123.1238, 42.1216], '河北': [114.4995, 38.1006],
                '天津': [117.4219, 39.4189], '山西': [112.3352, 37.9413],
                '陕西': [109.1162, 34.2004], '甘肃': [103.5901, 36.3043],
                '宁夏': [106.3586, 38.1775], '青海': [101.4038, 36.8207],
                '新疆': [87.9236, 43.5883], '西藏': [91.11, 29.97],
                '四川': [103.9526, 30.7617], '重庆': [108.384366, 30.439702],
                '山东': [117.1582, 36.8701], '河南': [113.4668, 34.6234],
                '江苏': [118.8062, 31.9208], '安徽': [117.29, 32.0581],
                '湖北': [114.3896, 30.6628], '浙江': [119.5313, 29.8773],
                '福建': [119.4543, 25.9222], '江西': [116.0046, 28.6633],
                '湖南': [113.0823, 28.2568], '贵州': [106.6992, 26.7682],
                '广西': [108.479, 23.1152], '海南': [110.3893, 19.8516],
                '广东': [113.28064, 23.125177], '北京': [116.405289, 39.904987],
                '云南': [102.71225, 25.040609], '香港': [114.165460, 22.275340],
                '澳门': [113.549130, 22.198750], '台湾': [121.5200760, 25.0307240]}
    a = []
    for item in province:
        b = []
        for i in BarPlace[item]:
            # print(i)

            b.append(i - 0.5)
        a.append(b)
    # print(a)
    BarPlace1 = dict(zip(province, a))
    # print(BarPlace1)

    for item in [list(z) for z in zip(province, confirm)]:
        BarPlace[item[0]].append(item[1])
        # print(dicts_all)
        # print(item)
    # print(BarPlace)
    for item in [list(z) for z in zip(province, heal)]:
        BarPlace1[item[0]].append(item[1])
    # print(BarPlace1)
    c = (
        Map3D()

            .add_schema(
            is_show_ground=True,
            shading='lambert',
            # 地面颜色。
            ground_color='#f1cabd',
            itemstyle_opts=opts.ItemStyleOpts(
                color="rgb(230,200,55)",
                opacity=1,
                border_width=0.8,

                border_color="rgb(230,94,90)"),
            map3d_label=opts.Map3DLabelOpts(
                is_show=False,
                formatter=JsCode(
                    "function(data){return data.name + " " + data.value[2];}")),
            emphasis_label_opts=opts.LabelOpts(
                is_show=False,
                color="#fff",
                font_size=10,
                background_color="rgba(2,23,11,0)"),
            light_opts=opts.Map3DLightOpts(
                main_color="#fff",
                main_intensity=1.2,
                main_shadow_quality="high",
                is_main_shadow=False,
                main_beta=10,
                ambient_intensity=0.3))
            .add(
            series_name="累计确诊",
            data_pair=list(zip(list(BarPlace.keys()), list(BarPlace.values()))),
            type_=ChartType.BAR3D,
            bar_size=1,

            is_animation=True,
            animation_duration_update=1000,
            animation_easing_update="cubicOut",
            label_opts=opts.LabelOpts(
                is_show=True,
                formatter=JsCode(
                    "function(data){return data.name + ' ' + data.value[2];}")))
            .add(
            series_name="累计治愈",
            data_pair=list(zip(list(BarPlace1.keys()), list(BarPlace1.values()))),
            type_=ChartType.BAR3D,
            bar_size=1,
            is_animation=True,
            animation_duration_update=1000,
            animation_easing_update="cubicOut",

            label_opts=opts.LabelOpts(
                is_show=True,

                formatter=JsCode(
                    "function(data){return data.name + ' ' + data.value[2];}")))
            .set_global_opts(title_opts=opts.TitleOpts(title="全国疫情分布", subtitle=subtitle, pos_left="50", pos_top="5%",
                                                       title_textstyle_opts=opts.TextStyleOpts(font_size=30),
                                                       subtitle_textstyle_opts=opts.TextStyleOpts(font_size=18,
                                                                                                  color='#222')),
                             visualmap_opts=opts.VisualMapOpts(min_=0, max_=int(
                                 heal_sum / 50)), )

    )
    return c


def amap() -> Map:
    data = pd.read_csv('/code_workplace/Pycharm/Covid_data_visual/spider/data/newDayProvince.csv')
    province = list(data["provinceName"])
    # province=Faker.provinces
    confirmedCount = list(data["confirmedCount"])
    confirmedCount = [list(z) for z in zip(province, confirmedCount)]  # 累计确诊
    curedCo = list(data["curedCount"])  # 累计治愈
    curedCo = [list(z) for z in zip(province, curedCo)]  # 累计确诊
    deadCount = list(data["deadCount"])  # 累计死亡
    deadCount = [list(z) for z in zip(province, deadCount)]  # 累计确诊
    # print(deadCount)
    # print(curedCo)
    # print(confirmedCount)
    # print(Faker.provinces)
    # print(Faker.values())
    c = (
        Map()
            .add("累计确诊", confirmedCount, "china")
            .add("累计治愈", curedCo, "china")
            .add("累计死亡", deadCount, "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="全国新型冠状病毒感染情况"),
            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                              pieces=[
                                                  {'min': 5000, 'label': '>5000人'},
                                                  {'min': 1000, 'max': 4999, 'label': '1000-4999人'},
                                                  {'min': 500, 'max': 999, 'label': '500-999人'},
                                                  {'min': 100, 'max': 499, 'label': '100-499人'},
                                                  {'min': 1, 'max': 99, 'label': '1-99人'},
                                                  {'min': 0, 'max': 0, 'label': 0}
                                              ]),
        )

    )
    return c
