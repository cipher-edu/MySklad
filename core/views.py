
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.forms import modelform_factory
from .models import Product
from django.views.generic import CreateView
from .forms import *
# Create your views here.
class SingupView(CreateView):
    template_name = "registration/signup.html"
    form_class = NewUserform
    def get_success_url(self):
        return reverse('index')

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    context = {'form': form, 'action': 'Add'}
    return render(request, 'add_subtract_product.html', context)

def subtract_product(request):
    if request.method == 'POST':
        form = SubtractProductForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.quantity = -transaction.quantity
            transaction.added = False
            transaction.product.quantity += transaction.quantity
            transaction.product.save()
            transaction.save()
            return redirect('index')
    else:
        form = SubtractProductForm()
    context = {'form': form, 'action': 'Subtract'}
    return render(request, 'add_subtract_product.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    transactions = Transaction.objects.filter(product=product).order_by('-date')
    context = {'product': product, 'transactions': transactions}
    return render(request, 'product_detail.html', context)

def add_product_to_inventory(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.added = True
            transaction.product.quantity += transaction.quantity
            transaction.product.save()
            transaction.save()
            return redirect('index')
    else:
        form = AddProductForm()
    context = {'form': form}
    return render(request, 'add_product_to_inventory.html', context)

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        Transaction.objects.filter(product=product).delete()
        product.delete()
        return redirect('index')

    # return render(request, 'delete_confirmation.html', {'product': product})