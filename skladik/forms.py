from django import forms
from .models import Cash, Organizationsservice

class CreateProductForm(forms.Form):
    brand = forms.CharField(max_length=150)
    name = forms.CharField(max_length=150)
    inprice = forms.IntegerField()
    cash_value = forms.ModelChoiceField(queryset=Cash.objects.all())
    outprice = forms.IntegerField()
    value = forms.IntegerField()
    color = forms.CharField(max_length=50)
    creator = forms.CharField(max_length=50)

class DeliverProductForm(forms.Form):
    product_name = forms.CharField(max_length=150)
    product_value = forms.IntegerField()
    product_color = forms.CharField(max_length=35)
    service_category = forms.ModelChoiceField(queryset=Organizationsservice.objects.all())
