from django.shortcuts import render, reverse, redirect
from django.views.generic import CreateView
from .forms import *
# Create your views here.
class SingupView(CreateView):
    template_name = "registration/signup.html"
    form_class = NewUserform
    def get_success_url(self):
        return reverse('home')

def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
from .models import Product

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        Product.objects.create(name=name, price=price)
        return redirect('product_list')
    return render(request, 'add_product.html')

def subtract_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('product_list')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})