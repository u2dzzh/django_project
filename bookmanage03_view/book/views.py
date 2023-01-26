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