from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('author_reg',views.author_reg,name='author_reg'),
    path('reader_reg',views.reader_reg,name='reader_reg'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]