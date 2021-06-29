import os
import pandas as pd
from pyecharts.charts import Map, Map3D, Page
from pyecharts.globals import ChartType
os.chdir('/code_workplace/Pycharm/Covid_data_visual/templates')
import csv
import pyecharts.options as opts
from pyecharts.charts import Line
import csv
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType
from in_hubei import geoIn
from out_hubei import geoOut
def page_simple_layout():
    page = Page(layout=Page.SimplePageLayout)
    page.add(
        geoIn(),
        geoOut()
    )
    page.render('migration.html')
    # Page.save_resize_html('test.html',
    #                       cfg_file="/code_workplace/Pycharm/Covid_data_visual/static/chart_config_all.json",
    #                       dest="migration.html")


if __name__ == "__main__":
    page_simple_layout()
