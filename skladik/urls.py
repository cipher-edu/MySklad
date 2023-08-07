from django.urls import path
from .views import *
urlpatterns = [
    path('items/history/', items_history, name='items_history'),


]