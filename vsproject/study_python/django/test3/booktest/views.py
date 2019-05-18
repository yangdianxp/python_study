# Create your views here.
from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
# request就是HttpRequest类型的对象
# request包含浏览器请求的信息
def index(request):
    return render(request, 'booktest/index.html', {})


def show_arg(request, num1):
    return HttpResponse(num1)