from django.urls import re_path
from booktest import views

urlpatterns = [
    re_path(r'^index$', views.index),
    re_path(r'^create$', views.create),
    re_path(r'^delete/(\d+)$', views.delete),
    re_path(r'^areas$', views.areas),  # 自关联案例
]