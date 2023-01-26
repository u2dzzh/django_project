from django.db import models

# Create your models here.
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
    # 在一对多的关系模型中, 系统会自动添加一个  关联模型类名小写_set
    # 在此例中, BookInfo与PeopleInfo 是一对多的关系 , 因此在本类中会有
    # peopleinfo_set=[PeopleInfo, PeopleInfo, ...]

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