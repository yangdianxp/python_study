# Create your views here.
from datetime import date
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def page_not_found(request, excetion):
    return render_to_response("404.html")

# Create your views here.
def index(request):
    return render(request, 'booktest/index.html', {})