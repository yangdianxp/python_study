from django.urls import re_path
from booktest import views

urlpatterns = [
    re_path(r'^index$', views.index),
    #re_path(r'^showarg(\d+)', views.show_arg), # 捕获url参数：位置参数
    re_path(r'^showarg(?P<num>\d+)', views.show_arg), # 捕获url参数：位置参数,关键字参数
]