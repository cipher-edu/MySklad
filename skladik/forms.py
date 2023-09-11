from django import forms
from .models import *

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = '__all__'
        widgets = {
            'items_brand': forms.TextInput(attrs={'class':'form-control col-md-4'}),
            'items_name': forms.TextInput(attrs={'class':'form-control col-md-4'}),
            'items_inprice': forms.TextInput(attrs={'class':'form-control col-md-4'}),
            'items_outprice': forms.TextInput(attrs={'class':'form-control col-md-4'}),
            'items_incash_value': forms.Select(attrs={'class':'form-control col-md-4'}),
            'items_value': forms.TextInput(attrs={'class':'form-control col-md-4'}),
            'items_color': forms.TextInput(attrs={'class':'form-control col-md-4'}),
            'items_creator': forms.TextInput(attrs={'class':'form-control col-md-4'}),
        }
class DeliverProductForm(forms.Form):
    product_name = forms.CharField(max_length=150)
    product_value = forms.IntegerField()
    product_color = forms.CharField(max_length=35)
    service_category = forms.ModelChoiceField(queryset=Organizationsservice.objects.all())


class EndserviceClientForm(forms.ModelForm):
    class Meta:
        model = EndserviceClient
        fields ='__all__'
class ClientEndServiceForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Clientadd.objects.all(), label="Select Client")
    product = forms.ModelChoiceField(queryset=CerviseClient.objects.none(), label="Select Product")

    def __init__(self, *args, **kwargs):
        super(ClientEndServiceForm, self).__init__(*args, **kwargs)
        if 'client' in self.data:
            try:
                client_id = int(self.data.get('client'))
                self.fields['product'].queryset = CerviseClient.objects.filter(client_name_id=client_id)
            except (ValueError, TypeError):
                pass
        elif self.instance and self.instance.client_name:
            self.fields['product'].queryset = CerviseClient.objects.filter(client_name_id=self.instance.client_name.id)
            
class ClientForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Clientadd.objects.all(), empty_label="Select a client")