# Create your views here.
from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
# request就是HttpRequest类型的对象
# request包含浏览器请求的信息
def index(request):
    print(request.method)
    print(request.path)
    return render(request, 'booktest/index.html', {})


def show_arg(request, num1):
    return HttpResponse(num1)

def login(request):
    return render(request, 'booktest/login.html', {})

def login_check(request):
    # request.POST  保存的是post提交的参数  QueryDict
    # request.GET  保存的是get提交的参数
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username + ":" + password)
    if username == 'yangdian' and password == '123456':
        return redirect('/index')
    return redirect('/login')