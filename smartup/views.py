from django.shortcuts import render, redirect
from .models import Product, SalesRecord
from .forms import *
def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        cost = request.POST['cost']
        product = Product.objects.create(name=name, cost=cost)
        return redirect('product_list')
    return render(request, 'add_product.html')

def subtract_product(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        quantity = int(request.POST['quantity'])
        product = Product.objects.get(id=product_id)
        product.quantity -= quantity
        product.save()
        return redirect('product_list')
    return render(request, 'subtract_product.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def sales_list(request):
    sales = SalesRecord.objects.all()
    return render(request, 'sales_list.html', {'sales': sales})
