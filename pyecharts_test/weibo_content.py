import csv
import jieba
import pyecharts.options as opts
from pyecharts.charts import Page, Pie
from pyecharts.charts import WordCloud, Bar
from snownlp import SnowNLP

def wordyun() -> WordCloud:
    words_list = []
    with open('/code_workplace/Pycharm/Covid_data_visual/spider/data/weibo_content.csv', 'r', encoding='utf-8')as f:
        reader = csv.reader(f)
        for line in reader:
            words = list(jieba.cut(line[0]))
            words_list += words
    word = list(set(words_list))
    word.sort()
    stopwords = [line.strip() for line in
                 open('/code_workplace/Pycharm/Covid_data_visual//spider/data/hit_stopwords.txt',
                      encoding='UTF-8').readlines()]
    for ch in word:
        if ch in stopwords:
            word.remove(ch)

    value = []
    for w in word:
        value.append(words_list.count(w))

    data = []
    for i in range(len(value)):
        data.append((word[i], value[i]))
    c = (
        WordCloud()
            .add(series_name="", data_pair=data, word_size_range=[10, 100],
                 mask_image='/code_workplace/Pycharm/Covid_data_visual/static/image/zhong.jpeg', width='100%',
                 height='100%'
                 #
                 )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="微博词云图", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )

    )
    return c

def pie() -> Pie():
    with open('/code_workplace/Pycharm/Covid_data_visual/spider/data/weibo_content.csv', 'r', encoding='utf-8')as f:
        reader = csv.reader(f)
        value = []
        j = 0;
        z = 0;
        x = 0
        for line in reader:
            score = SnowNLP(line[0]).sentiments
            if score <= 0.4:
                x += 1
            elif 0.4 < score < 0.7:
                z += 1
            else:
                j += 1  # 积极
        value.append(j)
        value.append(z)
        value.append(x)
    x_data = ["积极", "消极", "中立"]
    data_pair = [list(z) for z in zip(x_data, value)]
    data_pair.sort(key=lambda x: x[1])
    c = (
        Pie(init_opts=opts.InitOpts())
            .add(
            series_name="微博情感统计",
            data_pair=data_pair,
            rosetype="radius",
            radius="55%",
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="微博情感统计",
                pos_left="center",
                pos_top="20",
                title_textstyle_opts=opts.TextStyleOpts(color="#000"),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
            .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            label_opts=opts.LabelOpts(color="rgba(0,0, 0, 0.6)"),
        )
    )
    return c

def emotion() -> Bar:
    yq = [];
    ym = [];
    fk = [];
    zg = [];
    mg = []
    with open('/code_workplace/Pycharm/Covid_data_visual//spider/data/weibo_content.csv', 'r', encoding='utf-8')as f:
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
    j_value = [];
    z_value = [];
    x_value = []
    for v in values:
        j = 0;
        z = 0;
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
                             legend_opts=opts.LegendOpts(is_show=True),
                             )
    )
    return c;

