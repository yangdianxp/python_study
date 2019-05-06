from django.db import models
# 设计和表对应的类
# Create your models here.

# 图书类
class BookInfo(models.Model):
    # 图书名称，CharField说明是一个字符串，max_length指定字符串最大长度
    btitle = models.CharField(max_length=20)
    # 出版日期 DateField说明是一个日期类型
    bpub_date = models.DateField()

    def __str__(self):
        return self.btitle

# 英雄人物类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=128)
    #建立外键
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.hname