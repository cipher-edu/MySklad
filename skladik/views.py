from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum



def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

@login_required
def home(request):
    total_sum = Items.objects.aggregate(total_sum=Sum('items_inprice'))['total_sum']
    total_goods = Items.objects.count()
    total_goods_value = sum(item.items_inprice for item in Items.objects.all())
    total_goods_percent = (total_goods_value / total_goods) * 100 if total_goods > 0 else 0
    total_customers = Clientadd.objects.count()
    total_services_sum = EndserviceClient.objects.aggregate(total_sum=Sum('clien_service_price'))['total_sum']
    
    if total_customers > 0:
        avg_services_per_customer = total_services_sum / total_customers
    else:
        avg_services_per_customer = 0
    total_services = EndserviceClient.objects.count()

    context = {
        'total_sum':total_sum,
        'total_goods': total_goods,
        'total_goods_value': total_goods_value,
        'total_goods_percent': total_goods_percent,
        'total_customers': total_customers,
        'total_services': total_services,
        'total_services_sum': total_services_sum,
        'avg_services_per_customer': avg_services_per_customer
    }
    return render(request, 'index.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to dashboard view after successful login
        else:
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'registration/login.html', {'error_message': error_message})
    return render(request, 'registration/login.html')

@login_required 
def custom_logout(request):
    logout(request)
    return redirect(reverse('login'))  

@login_required
def calculate_reports(request):
    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        # Calculate product and output reports
        products = Items.objects.filter(items_creator=request.user)
        service_entries = EndserviceClient.objects.filter(
            product__client_name__ovner=request.user,
            product__client_name__client_reception_time__range=[start_date, end_date]
        )

        total_products = products.count()
        total_output = service_entries.count()

        return render(request, 'reports.html', {
            'start_date': start_date,
            'end_date': end_date,
            'total_products': total_products,
            'total_output': total_output,
        })

    return render(request, 'calculate_reports.html')

@login_required
def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            name = form.cleaned_data['name']
            inprice = form.cleaned_data['inprice']
            cash_value = form.cleaned_data['cash_value']
            outprice = form.cleaned_data['outprice']
            value = form.cleaned_data['value']
            color = form.cleaned_data['color']
            creator = form.cleaned_data['creator']
            cash_obj = Cash.objects.get(pk=cash_value.pk)  # Retrieve the selected Cash object
            new_product = Items(
                items_brand=brand,
                items_name=name,
                items_inprice=inprice,
                items_incash_value=cash_obj,
                items_outprice=outprice,
                items_value=value,
                items_color=color,
                items_creator=creator,
            )
            new_product.save()
            return redirect('product_list')  # Redirect to the product list view
    else:
        form = CreateProductForm()

    cash_values = Cash.objects.all()
    context = {'form': form, 'cash_values': cash_values}
    return render(request, 'create_product.html', context=context)

@login_required
def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list view
    else:
        form = CreateProductForm()

    return render(request, 'create_product.html', {'form': form})
# def deliver_product(request, client_id):
#     client = get_object_or_404(Clientadd, pk=client_id)
#     service_categories = Organizationsservice.objects.all()

#     if request.method == 'POST':
#         product_name = request.POST.get('product_name')
#         product_value = int(request.POST.get('product_value'))
#         product_color = request.POST.get('product_color')
#         service_category_id = request.POST.get('service_category')
#         service_category = get_object_or_404(Organizationsservice, pk=service_category_id)

#         new_service = CerviseClient(
#             client_name=client,
#             product_name=product_name,
#             product_value=product_value,
#             product_color=product_color,
#             service_catetegory=service_category,
#         )
#         new_service.save()

#         # Redirect to the client's details page
#         return redirect('client_details', client_id=client_id)

   
#     return render(request, 'deliver_product.html', {'service_categories': service_categories, 'client_id': client_id})

@login_required
def product_list(request,):
    products = Items.objects.all()
    context = {
        'products':products
    }
    return render(request, 'product_list.html', context=context )

# views.py
@login_required
def create_client(request):
    if request.method == 'POST':
        client_name = request.POST['client_name']
        client_phonenumber = request.POST['client_phonenumber']
        owner_id = request.POST['owner']
        
        owner = Worker.objects.get(pk=owner_id)

        new_client = Clientadd(
            client_name=client_name,
            client_phonenumber=client_phonenumber,
            ovner=owner,
        )
        new_client.save()

        messages.success(request, 'Mijoz muvofaqiyatli saqlandi. Mijozlar bazasiga o\'ting')  # Add a success message

        # return redirect('client_list')  # Redirect to the client list view

    owners = Worker.objects.all()
    return render(request, 'create_client.html', {'owners': owners})

@login_required
def client_list(request):
    clients = Clientadd.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

@login_required
def client_details(request, client_id):
    client = get_object_or_404(Clientadd, id=client_id)
    # client = Clientadd.objects.get(pk=client_id)
    return render(request, 'client_details.html', {'client': client })


# ...
@login_required
def end_service(request, client_id):
    if request.method == 'POST':
        client = Clientadd.objects.get(pk=client_id)
        product_id = request.POST['product_id']
        product = CerviseClient.objects.get(pk=product_id)
        product_defective = request.POST['product_defective']
        product_repaired = request.POST['product_repaired']
        product_not_repaired = request.POST['product_not_repaired']
        kuchadan_tovar = request.POST['kuchadan_tovar']
        sklad_item_id = request.POST['sklad_item']
        sklad_item = Items.objects.get(pk=sklad_item_id)
        cervice_item_price = int(request.POST['cervice_item_price'])
        clien_service_price = int(request.POST['clien_service_price'])
        topshiruvchi_id = request.POST['topshiruvchi']
        
        topshiruvchi_id = request.POST['topshiruvchi']
        try:
            topshiruvchi = Worker.objects.get(pk=topshiruvchi_id)
        except Worker.DoesNotExist:
            topshiruvchi = None  
        end_service_entry = EndserviceClient(
            client_name=client,
            product=product,
            product_defective=product_defective,
            product_repaired=product_repaired,
            produtct_not_repaired=product_not_repaired,
            kuchadan_tovar=kuchadan_tovar,
            sklad_item=sklad_item,
            cervice_item_price=cervice_item_price,
            clien_service_price=clien_service_price,
            topshiruvchi=topshiruvchi,  # Use the retrieved Worker instance
            coment=coment,
        )
        end_service_entry.save()

        return redirect('client_details', client_id=client_id)

    client = Clientadd.objects.get(pk=client_id)
    products = CerviseClient.objects.filter(client_name=client)
    sklad_items = Items.objects.all()
    workers = Worker.objects.all()

    product_id = request.GET.get('product_id')  # Retrieve the product_id from the GET parameters
    context = {
        'client': client,
        'products': products,
        'sklad_items': sklad_items,
        'workers': workers,
        'selected_product_id': product_id,  # Pass the selected product_id to the template
    }
    return render(request, 'end_service.html', context=context)

@login_required
def client_history(request, client_id):
    client = Clientadd.objects.get(pk=client_id)
    service_history = CerviseClient.objects.filter(client_name=client)

    return render(request, 'client_history.html', {'client': client, 'service_history': service_history})