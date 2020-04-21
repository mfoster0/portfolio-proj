from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'), #this takes an int following the /blog/ portion of the URL and assigned it to blog_id eg. /blog/3
]