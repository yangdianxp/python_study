from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from test1.models import BookInfo 

#def my_render(template_path, context_dict = {}):
#    temp = loader.get_template(template_path)
#    #模板渲染：产生标准的html内容
#    return HttpResponse(temp.render(context_dict))

# Create your views here.
# 定义视图函数
def index(request):
    return render(request, "test1/index.html", 
                  {"content":"hello world",
                   "list":list(range(1, 10))})


def index2(request):
    return HttpResponse('hello python')

def show_books(request):
    books = BookInfo.objects.all()
    return render(request, 'test1/show_books.html', {'books':books})

def detail(request, bid):
    book = BookInfo.objects.get(id=bid)
    heros = book.heroinfo_set.all()
    return render(request, "test1/detail.html", 
                  {'book':book, 'heros':heros})