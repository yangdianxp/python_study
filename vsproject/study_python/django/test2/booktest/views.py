from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from booktest.models import BookInfo

# Create your views here.
def index(request):
    books = BookInfo.objects.all()
    return render(request, 'booktest/index.html',
                  {'books':books})

def create(request):
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1990, 1, 1)
    b.save()
    #return HttpResponse('ok')
    return redirect('/index')

def delete(request, bid):
    book = BookInfo.objects.get(id=bid)
    book.delete()
    #return HttpResponseRedirect('/index')  #重定向
    return redirect('/index')