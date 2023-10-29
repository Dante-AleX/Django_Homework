from django.contrib import admin
from django.urls import path, include
from myapp2 import views

urlpatterns = [
    path("", views.index, name='index'),
    path('all_orders/', views.all_orders, name='all_orders'), 
    path('ordered-products/<int:customer_id>/7/', views.get_ordered_products, {'days': 7}, name='ordered_products_7_days'),
    path('ordered-products/<int:customer_id>/30/', views.get_ordered_products, {'days': 30}, name='ordered_products_30_days'),
    path('ordered-products/<int:customer_id>/365/', views.get_ordered_products, {'days': 365}, name='ordered_products_365_days'),
]

