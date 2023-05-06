from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('add/', add_product, name='add_product'),
    path('subtract/<int:product_id>/', subtract_product, name='subtract_product'),

]
