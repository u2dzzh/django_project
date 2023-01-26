from django.urls import path

from book.views import shop, register, json
from django.urls import converters

# 1. 定义转换器
class MobileConverter:# 手机号验证
    regex = '1[3-9]\d{9}'

    # 验证没有问题的数据, 给视图函数
    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return str(value)
# 2.注册转换器
from django.urls.converters import register_converter
# converter 转换器, type_name 使用名字
register_converter(MobileConverter, 'phone')

urlpatterns = [
    # <转换器名:变量名>
    # 本质是转换器对传入参数进行正则的验证
    path('<int:city_id>/<phone:shop_id>', shop),
    path('register/', register),
    path('json/', json),
]