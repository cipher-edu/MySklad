from django import forms
from .models import Product

class SubtractProductForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label=None)
    quantity = forms.IntegerField(min_value=1)
