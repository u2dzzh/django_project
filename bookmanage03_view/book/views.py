from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def shop(request, city_id, shop_id):
    print(city_id, shop_id)
    query_parameters = request.GET
    print(query_parameters)
    return HttpResponse("dining hall")


def register(request):
    data = request.POST
    print(data)
    return HttpResponse("ok")


def json(request):
    # 接受数据
    body = request.body
    # 将body的二进制数据转成str
    body_str = body.decode()
    # json形式的字符串转换为Python的字典
    import json
    body_dict = json.loads(body_str)
    print(body_dict)
    return HttpResponse("ok")

"""
第一次请求, 携带查询字符串
http:8.130.45.218:8000/set_cookies?name=stu&pwd=123
服务器接收到请求之后, 获取name, 服务器设置cookie信息, cookie信息包括name
浏览器接收到服务器的响应之后, 将cookie保存起来

第二次及以后的访问, 浏览器都会携带cookie信息, 服务器就可以读取cookie信息
"""

def set_cookies(request):
    # 获取查询字符串数据
    name = request.GET.get('name')
    # 服务器设置cookie信息
    # 通过响应对象设置
    response = HttpResponse('set_cookies',status=200)
    response.set_cookie('name', name)
    return response

def get_cookies(request):
    # 使用COOKIES方法  返回字典数据
    name = request.COOKIES['name']
    return HttpResponse(name)