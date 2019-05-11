from django.db import models

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

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200, null=True)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)