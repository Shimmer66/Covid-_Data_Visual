from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "all.html")
def weibo(request):
    return render(request,'weibo.html')
def migration(request):
    return render(request,'migration.html')

def countrymap(request):
    return render(request, 'china_all.html')

def 台湾map(request):
    return render(request, '台湾地图.html')


def 广东map(request): return render(request, '广东地图.html')


def 香港map(request): return render(request, '香港地图.html')


def 上海map(request): return render(request, '上海地图.html')


def 福建map(request): return render(request, '福建地图.html')


def 浙江map(request): return render(request, '浙江地图.html')


def 云南map(request): return render(request, '云南地图.html')


def 四川map(request): return render(request, '四川地图.html')


def 北京map(request): return render(request, '北京地图.html')


def 江苏map(request): return render(request, '江苏地图.html')


def 陕西map(request): return render(request, '陕西地图.html')


def 天津map(request): return render(request, '天津地图.html')


def 内蒙古map(request): return render(request, '内蒙古地图.html')


def 河南map(request): return render(request, '河南地图.html')


def 辽宁map(request): return render(request, '辽宁地图.html')


def 重庆map(request): return render(request, '重庆地图.html')


def 澳门map(request): return render(request, '澳门地图.html')


def 湖北map(request): return render(request, '湖北地图.html')


def 山东map(request): return render(request, '山东地图.html')


def 山西map(request): return render(request, '山西地图.html')


def 甘肃map(request): return render(request, '甘肃地图.html')


def 海南map(request): return render(request, '海南地图.html')


def 宁夏map(request): return render(request, '宁夏地图.html')


def 黑龙江map(request): return render(request, '黑龙江地图.html')


def 河北map(request): return render(request, '河北地图.html')


def 湖南map(request): return render(request, '湖南地图.html')


def 安徽map(request): return render(request, '安徽地图.html')


def 新疆map(request): return render(request, '新疆地图.html')


def 江西map(request): return render(request, '江西地图.html')


def 吉林map(request): return render(request, '吉林地图.html')


def 广西map(request): return render(request, '广西地图.html')


def 贵州map(request): return render(request, '贵州地图.html')


def 青海map(request): return render(request, '青海地图.html')


def 西藏map(request): return render(request, '西藏地图.html')
