from django.urls import path
from .views import *
from random import randint

app_name = 'blog'


urlpatterns = [
    # post views
    path('', post_list, name="post_list"),
    path('post/<int:id>/', post_detail, name="post_detail"),
]
