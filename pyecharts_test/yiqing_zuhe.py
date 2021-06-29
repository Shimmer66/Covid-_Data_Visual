import os
import pandas as pd
from pyecharts.charts import Map, Map3D, Page
from pyecharts.globals import ChartType
os.chdir('//code_workplace/Pycharm/Covid_data_visual/templates')
import csv
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode


def lin() -> Line:
    background_color_js = (
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#c89'}, {offset: 1, color: '#06a'}], false)"
    )
    area_color_js = (
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#eb6'}, {offset: 1, color: '#3fb'}], false)"
    )

    x = []
    for i in range(1, 30):
        x.append('02-{}'.format(i))
    all = []
    with open('/code_workplace/Pycharm/Covid_data_visual/spider/data/everyDayProvince.csv', 'r', encoding='utf-8')as f:
        reader = csv.reader(f)
        for line in reader:
            all.append(line)
    confirm_list = []
    heal_list = []
    dead_list = []
    for i in x:
        confirm = 0
        heal = 0
        dead = 0
        for j in range(len(all)):
            if all[j][0] == '2020' and all[j - 1][0] == '2020':
                if '02' == str(all[j][1][:2]) and int(i[3:]) == int(all[j][1][3:]):
                    confirm += (int(all[j][3]) - int(all[j - 1][3]))
                    # print(all[j - 1])
                    #
                    # print(all[j])
                    # print(int(all[j][5]), int(all[j - 1][5]))
                    # print(int(all[j][5]) - int(all[j - 1][5]))
                    heal += (int(all[j][5]) - int(all[j - 1][5]))
                    dead += (int(all[j][4]) - int(all[j - 1][4]))
        confirm_list.append(confirm)
        heal_list.append(heal)
        dead_list.append(dead)

    c = (
        Line(init_opts=opts.InitOpts(bg_color=JsCode(background_color_js)))
            .add_xaxis(x)
            .add_yaxis("确诊", confirm_list, symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True, )
            .add_yaxis("治愈", heal_list, symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True, )
            .add_yaxis("死亡", dead_list, symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True)
            .set_global_opts(title_opts=opts.TitleOpts(title="全国每日新增情况"),
                             datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
                             )
            .render("confirm_day_add.html"))
    return c;


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
            # title_opts=opts.TitleOpts(title="{} 全国新型冠状病毒感染情况".format(date.replace('.','-'))),
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


def country() -> Map:
    data = pd.read_csv('/code_workplace/Pycharm/Covid_data_visual/spider/data/country.csv')
    confirm = data['confirmedCount']
    heal = data['curedCount']
    dead = data['deadCount']
    province = data['province']
    heal_list = list(a for a in zip(province, heal))
    confirm_list = list(a for a in zip(province, confirm))
    dead_list = list(a for a in zip(province, dead))
    heal_sum = 0
    confirm_sum = 0
    dead_sum = 0
    for i in range(len(heal)):
        heal_sum += heal[i]
        confirm_sum += confirm[i]
        dead_sum += dead[i]
    # 副标题
    subtitle = "确诊数量：" + str(confirm_sum) + "例\n\n治愈数量：" + str(heal_sum) + "\n\n死亡数量：" + str(dead_sum) + "例"
    world_map = (
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
                title_textstyle_opts=opts.TextStyleOpts(font_size=30),
                subtitle_textstyle_opts=opts.TextStyleOpts(font_size=18, color='#222')
            ),
            # 图例设置
            legend_opts=opts.LegendOpts(
                selected_mode='single', pos_top="50", pos_bottom="5%", textstyle_opts=opts.TextStyleOpts(font_size=18)),
        )

    )
    return world_map


def page_simple_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        amap(),
        bmap3d(),
        country(),
        lin()
    )

    # Page.save_resize_html("test.html",
    #                       cfg_file="/code_workplace/Pycharm/Covid_data_visual/static/chart_config_map.json",
    #                       dest="china_all.html")


if __name__ == "__main__":
    page_simple_layout()
