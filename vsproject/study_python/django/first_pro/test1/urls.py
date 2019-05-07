from django.urls import path, re_path
from test1 import views

urlpatterns = [
    re_path(r'^index$', views.index),
    re_path(r'^index2$', views.index2),
    re_path(r'^books$', views.show_books),
]