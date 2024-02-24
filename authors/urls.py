from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('author_home', views.author_home,name='author_home'),
    path('author_manage_book',views.author_manage_book,name='author_manage_book')
]