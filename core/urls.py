from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('add_product/', add_product, name='add_product'),
    path('tovarlardan_chiqim/', subtract_product, name='subtract_product'),
    path('product_detail/<uuid:product_id>/', product_detail, name='product_detail'),
    path('user_detail/<uuid:username_id>/', user_detail, name='user_detail'),
    path('tavorlarga_kirim_qilish/', add_product_to_inventory, name='add_product_to_inventory'),
    path('delete_product/<uuid:product_id>/', delete_product, name='delete_product'),
    path('cervice/', clientservice, name='clientservice')

]
