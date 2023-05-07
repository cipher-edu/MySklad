from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('add_product/', add_product, name='add_product'),
    path('subtract_product/', subtract_product, name='subtract_product'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
    path('add_product_to_inventory/', add_product_to_inventory, name='add_product_to_inventory'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),

]
