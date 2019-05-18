from django.urls import re_path
from booktest import views

urlpatterns = [
    re_path(r'^index$', views.index),
]

handler404 = views.page_not_found