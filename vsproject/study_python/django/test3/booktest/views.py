# Create your views here.
from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'booktest/index.html', {})


def show_arg(request, num1):
    return HttpResponse(num1)