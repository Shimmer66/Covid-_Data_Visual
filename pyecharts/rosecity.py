import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Pie
def rose()->Pie:
    data = pd.read_csv('/code_workplace/Pycharm/Covid_data_visual/spider/data/newDayProvince.csv')
    data = data.sort_values(by="confirmedCount", ascending=True)
    province = list(data["provinceName"])
    province = province[0:10]
    confirmedCount = list(data["confirmedCount"])
    confirmedCount = confirmedCount[0:10]
    confirmedCount = [list(z) for z in zip(province, confirmedCount)]  # 累计确诊


    color = ['#FAE927', '#E9E416', '#C9DA36', '#9ECB3C', '#6DBC49',
             '#37B44E', '#3DBA78', '#14ADCF', '#209AC9', '#1E91CA',
             '#2C6BA0', '#2B55A1', '#2D3D8E', '#44388E', '#6A368B'
                                                         '#7D3990', '#A63F98', '#C31C88', '#D52178', '#D5225B',
             '#D02C2A', '#D44C2D', '#F57A34', '#FA8F2F', '#D99D21',
             '#CF7B25', '#CF7B25', '#CF7B25']
    pie = (
        Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))  ##设置大小，因为要展示字，所以需要大一点
            .add('', confirmedCount
                 , rosetype='area'  ### radius：扇区圆心角展现数据的百分比，半径展现数据的大小
                 # area：所有扇区圆心角相同，仅通过半径展现数据大小
                 , radius=['25%', '95%']  # 饼图的半径，第一项是内半径，第二项是外半径，百分比表示相对位置
                 , center=['50%', '60%']  # 饼图的中心（圆心）坐标，饼图放在页面的哪个位置，数组的第一项是横坐标，第二项是纵坐标，百分比表示相对位置
                 )
            .set_global_opts(title_opts=opts.TitleOpts(title='    中国  \n 确诊病例最少 \n 的十个城市'  # 大标题，\n表示换行符

                                                       , title_textstyle_opts=opts.TextStyleOpts(color='black'
                                                                                                 , font_size=20
                                                                                                 , font_style='normal'
                                                                                                 , font_weight='bold'
                                                                                                 ,
                                                                                                 font_family='Microsoft Yahei')
                                                       , subtitle_textstyle_opts=opts.TextStyleOpts(color='black'
                                                                                                    , font_size=37
                                                                                                    , font_style='normal'
                                                                                                    , font_weight='bolder'
                                                                                                    )
                                                       , pos_left='43%'
                                                       , pos_top='55%'
                                                       )
                             , legend_opts=opts.LegendOpts(is_show=False)

                             )
            .set_series_opts(label_opts=opts.LabelOpts(position='inside'
                                                       # ,font_size
                                                       , font_style='normal'
                                                       , font_weight='bolder'
                                                       , formatter="{b}:{c}例",
                                                       )
                             )
            .set_colors(color)  ##设置颜色系列
    )
    return pie
