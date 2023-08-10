from django.urls import path
from .views import *

urlpatterns = [
    path('product/list/', product_list, name='product_list'),
    path('create_product/', create_product, name='create_product'),
    path('deliver_product/<uuid:client_id>/',deliver_product, name='deliver_product'),
    path('client_history/<uuid:client_id>/', client_history, name='client_history'),
    path('create_client/', create_client, name='create_client'),
    path('client_details/<uuid:client_id>/', client_details, name='client_details'),
    path('client_list/', client_list, name='client_list'),
    path('end_service/<uuid:client_id>/', end_service, name='end_service')

    # Add more URL patterns as needed
]