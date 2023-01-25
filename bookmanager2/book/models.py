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
    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    # 定义一个有序字典  枚举类型
    GENDER_CHOICE = (
        (1,'male'),
        (2,'female')
    )
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)
    # 系统会自动为外键添加_id
    """
    外键的级联操作  主表对从表  1对多
    主表的一条数据 如果删除了  从表有关联的数据 关联的数据处理
    SET_NULL  置空
    抛出异常    不让删除
    CASCADE    级联删除, 一起删除
    """
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'
    def __str__(self):
        return self.name