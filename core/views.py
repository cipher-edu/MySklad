
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.forms import modelform_factory
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from .forms import *
# Create your views here.
class SingupView(CreateView):
    template_name = "registration/signup.html"
    form_class = NewUserform
    def get_success_url(self):
        return reverse('index')
@login_required
def index(request):
    user = UserService.objects.all()
    products = Product.objects.all()
    total_value_price = sum(product.price for product in products)
    total_value_quantity = sum(product.quantity for product in products)
    context = {
        'user':user,
        'products':products,
        'total_value_price':total_value_price,
        'total_value_quantity':total_value_quantity
    }
    return render(request, 'index.html', context)

def add_product(request):
    products = Product.objects.all()
    total_value_price = sum(product.price for product in products)
    total_value_quantity = sum(product.quantity for product in products)
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    context = {
        'form': form, 
        'action': 'Add',
        'total_value_price':total_value_price,
        'total_value_quantity':total_value_quantity
        }
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

def clientservice(request):
    form = CerviseClientForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.added = True
            transaction.product.quantity -= transaction.quantity
            transaction.product.save()
            transaction.save()
            return redirect('index')
    else:
        form = CerviseClientForm()
    context = {
    }
    return render(request, 'clientservice.html', context=context)

def user_detail(request, username_id):
    user = UserService.objects.get(id=username_id)
    transactions = Transaction.objects.filter(user=user).order_by('-date')
    context = {'user': user, 'transactions': transactions}
    return render(request, 'clientdetail.html', context)

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        Transaction.objects.filter(product=product).delete()
        product.delete()
        return redirect('index')

    # return render(request, 'delete_confirmation.html', {'product': product})