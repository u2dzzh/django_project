from django.contrib import admin

# Register your models here.
# 注册模型
from book.models import BookInfo,PeopleInfo
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
# 注册完成后重新运行