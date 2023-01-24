from django.db import models
class BookInfo(models.Model):
    # 模型类需要继承models.Model
    # 系统会自动生成id字段
    # 字段   字段名=model.类型(选项)
    # 字段名实际就是数据表的字段名
    name = models.CharField(max_length=10) # varchar(10)
    def __str__(self):
        return self.name

# 人物
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束  人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
# Create your models here.
