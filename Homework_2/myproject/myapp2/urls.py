from django.contrib import admin
from django.urls import path, include
from myapp2 import views

urlpatterns = [
    path("", views.index, name='index'),
    path('all_orders/', views.all_orders, name='all_orders'),  
]

