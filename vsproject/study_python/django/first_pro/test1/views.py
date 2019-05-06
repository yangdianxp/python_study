from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 定义视图函数
def index(request):
    # 进行处理，和M和T进行交互
    return HttpResponse('老铁，没毛病')

def index2(request):
    return HttpResponse('hello python')