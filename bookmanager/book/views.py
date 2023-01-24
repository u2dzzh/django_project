from django.shortcuts import render

# Create your views here.
"""
视图 就是python函数

视图函数有两个要求:  有请求 有响应
    1.第一个参数就是参数请求 这个请求就是 HttpRequest对象
    2.必须返回一个响应
"""
# request
from django.http import HttpRequest
from django.http import HttpResponse

# 期望用户输入http:127.0.0.1/8000/index 来访问视图函数
def index(request):
    return HttpResponse('ok')