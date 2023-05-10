from django.contrib import admin
from .models import *
# Register your models here.
class Products(admin.ModelAdmin):
    list_display = ('id',)
admin.site.register(Product,Products)
admin.site.register(Transaction)
admin.site.register(Cash)
class Users(admin.ModelAdmin):
    list_display = ('id', 'username',)
admin.site.register(UserRegister,Users)
class User(admin.ModelAdmin):
    list_display = ('id',)
admin.site.register(UserService)