from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/product/',views.product_add,name='add'),
    path('products/',views.product_list,name='product_list')
]




        