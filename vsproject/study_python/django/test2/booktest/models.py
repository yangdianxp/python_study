from django.db import models

class BookInfoManager(models.Manager):
    def all(self):
        books = super().all()
        books = books.filter(isDelete=False)
        return books

    def create_book(self, btitle, bpub_date):
        book = BookInfo()
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()
        return book

# Create your models here.
class BookInfo(models.Model):
    #btitle = models.CharField(max_length=20)
    btitle = models.CharField(max_length=20, unique=True, db_index=True, db_column='title')
    bprice = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    #bpub_date = models.DateField()
    #bpub_date = models.DateField(auto_now_add=True)
    bpub_date = models.DateField(auto_now=True)
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    # book = models.Manager() # 自定义一个Manager类对象
    objects = BookInfoManager() # 

    #@classmethod
    #def create_book(cls, btitle, bpub_date):
    #    obj = cls()
    #    obj.btitle = btitle
    #    obj.bpub_date = bpub_date
    #    obj.save()
    #    return obj

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200, null=True)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)

#"""
## 多对多关系
## 新闻类型类
#class NewsType(models.Model):
#    type_name = models.CharField(max_length=20)
#    # 关系属性，代表类型下面的信息
#    type_news = models.ManyToManyField('NewsInfo')

## 新闻类
#class NewsInfo(models.Model):
#    title = models.CharField(max_length=120)
#    pub_date = models.DateTimeField(auto_now_add=True)
#    content = models.TextField()
#    # 关系属性，代表信息所属的类型
#    # news_type = models.ManyToManyField('NewsType')


## 一对一关系
#class EmployeeBasicInfo(models.Model):
#    name = models.CharField(max_length=20)
#    gender = models.BooleanField(default=False)
#    age = models.IntegerField()

#    employee_detail = models.OneToOneField('EmployeeDetailInfo')

## 员工详细信息类
#class EmployeeDetailInfo(models.Model):
#    # 联系地址
#    addr = models.CharField(max_length=256)
#    # employee_basic = models.OneToOneField('EmployeeBasicInfo')
#"""

class AreaInfo(models.Model):
    atitle = models.CharField(max_length=20)
    # 关系属性，代表当前地区的父级地区
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)