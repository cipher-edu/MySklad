from django.urls import path
from .views import *
urlpatterns = [
    path('items/history/', items_history, name='items_history'),
    path('item-list/', item_list, name='item_list'),

]