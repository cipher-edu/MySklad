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

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SubtractProductForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }