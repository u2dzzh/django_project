from django.db import models

# Create your models here.
"""
    id 系统默认生成
    1.模型类继承自 models.Model
    2.定义属性
        属性名=models.类型(选项)
        2.1 属性名对应的就是字段名
        2.2 类型联系MySQL类型
        2.3 选项  是否有默认值 是否唯一 ...
        CharField必须有max_length
        verbose_name 主要是admin站点使用
        decimal 货币类型
    3. 改变表的名称  
        默认表的名称  子应用名_类名  小写
        修改表
"""
class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name='书名')
    pub_date = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)
    # 修改表的名字
    class Meta:
        db_table = 'bookinfo'
        verbose_name = '书籍管理' # admin站点使用

