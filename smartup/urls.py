from django.urls import path
from . import views

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('subtract_product/', views.subtract_product, name='subtract_product'),
    path('product_list/', views.product_list, name='product_list'),
    path('sales_list/', views.sales_list, name='sales_list'),
]
