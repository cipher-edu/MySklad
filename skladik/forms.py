from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

class NewUserform(UserCreationForm):
    class Meta:
        model = User
        fields  = ("username",)
        field_classes = {'username':UsernameField}

#  Ishchi yaratish uchun forma
class Worker(forms.ModelForm):
    class Meta:
        model = Ishchilar
        fields = "__all__"
# To'lov turi formasi
class Cash(forms.ModelForm):
    
    class Meta:
        model = Cash
        fields = "__all__"
#servise turlari
class Service(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = "__all__"

#prodeuct qushish
class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

#klient registratsiya

class RegisterClient(forms.ModelForm):
    class Meta:

        model = UserRegister
        fields = "__all__"

#service Client
class ReceptionUser(forms.ModelForm):
    class Meta:
        model = UserReseption
        fields =  "__all__"

# service client

class CerviceUser(forms.ModelForm):

    class Meta:
        model = UserCervice
        fields = '__all__'
