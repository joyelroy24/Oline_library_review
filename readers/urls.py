from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reader_home,name='reader_home'),
    path('view_authors', views.view_authors,name='view_authors'),
    path('view_books',views.view_books,name='view_books')
]