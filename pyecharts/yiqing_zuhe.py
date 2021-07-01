import os
import pandas as pd
from pyecharts.charts import Map, Map3D, Page
from pyecharts.globals import ChartType
os.chdir('//code_workplace/Pycharm/Covid_data_visual/templates')
import csv
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode
from confirmAdd import lin
from weibo_content import wordyun,pie,emotion
from world import world
from country import mapChina,map3dChina

def page_simple_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        mapChina(),
        map3dChina(),
        world(),
        lin(),
        pie(),
        wordyun(),
        emotion(),
    )
    Page.save_resize_html('aaaaaaaaa.html',
                          cfg_file="/code_workplace/Pycharm/Covid_data_visual/static/chart_config_all.json",
                          dest="all.html")


if __name__ == "__main__":
    page_simple_layout()
