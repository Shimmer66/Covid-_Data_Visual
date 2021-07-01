import os

from pyecharts.charts import Page

os.chdir('//code_workplace/Pycharm/Covid_data_visual/templates')
from rosecity import rose

def page_simple_layout():
    page = Page(layout=Page.SimplePageLayout)
    page.add(
        rose(),

    )
    page.render('other.html')


if __name__ == "__main__":
    page_simple_layout()
