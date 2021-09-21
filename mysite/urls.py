from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('other', views.other, name='other'),
    path('weibo', views.weibo, name='weibo'),
    path('migration', views.migration, name='migration'),
    # path('chinmapChina', views.chinmapChina, name='chinmapChina'),
    path('countrymap', views.countrymap, name='countrymap'),
    path('台湾map', views.台湾map, name='台湾map'),
    path('广东map', views.广东map, name='广东map'),
    path('香港map', views.香港map, name='香港map'),
    path('上海map', views.上海map, name='上海map'),
    path('福建map', views.福建map, name='福建map'),
    path('浙江map', views.浙江map, name='浙江map'),
    path('云南map', views.云南map, name='云南map'),
    path('四川map', views.四川map, name='四川map'),
    path('北京map', views.北京map, name='北京map'),
    path('江苏map', views.江苏map, name='江苏map'),
    path('陕西map', views.陕西map, name='陕西map'),
    path('天津map', views.天津map, name='天津map'),
    path('内蒙古map', views.内蒙古map, name='内蒙古map'),
    path('河南map', views.河南map, name='河南map'),
    path('辽宁map', views.辽宁map, name='辽宁map'),
    path('重庆map', views.重庆map, name='重庆map'),
    path('澳门map', views.澳门map, name='澳门map'),
    path('湖北map', views.湖北map, name='湖北map'),
    path('山东map', views.山东map, name='山东map'),
    path('山西map', views.山西map, name='山西map'),
    path('甘肃map', views.甘肃map, name='甘肃map'),
    path('海南map', views.海南map, name='海南map'),
    path('宁夏map', views.宁夏map, name='宁夏map'),
    path('黑龙江map', views.黑龙江map, name='黑龙江map'),
    path('河北map', views.河北map, name='河北map'),
    path('湖南map', views.湖南map, name='湖南map'),
    path('安徽map', views.安徽map, name='安徽map'),
    path('新疆map', views.新疆map, name='新疆map'),
    path('江西map', views.江西map, name='江西map'),
    path('吉林map', views.吉林map, name='吉林map'),
    path('广西map', views.广西map, name='广西map'),
    path('贵州map', views.贵州map, name='贵州map'),
    path('青海map', views.青海map, name='青海map'),
    path('西藏map', views.西藏map, name='西藏map'),

]
