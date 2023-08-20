from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('product/list/', product_list, name='product_list'),
    path('create_product/', create_product, name='create_product'),
    path('deliver_product/<uuid:client_id>/',deliver_product, name='deliver_product'),
    # path('client_history/<uuid:client_id>/', client_history, name='client_history'),
    path('create_client/', create_client, name='create_client'),
    path('client_details/<uuid:client_id>/', client_details, name='client_details'),
    path('client_list/', client_list, name='client_list'),
    path('end_service/<uuid:client_id>/', end_service, name='end_service'),
    path('calculate_reports/', calculate_reports, name='calculate_reports'),
    path('client/history/<uuid:client_id>/', client_history, name='client_history'),
    path('404/', custom_404_view, name='custom_404'),
    path('login/', user_login, name='login'),
    path('logout/', custom_logout, name='custom_logout'),
    # Add more URL patterns as needed
]


handler404 = 'skladik.views.custom_404_view'