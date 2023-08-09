from django.shortcuts import render
from .models import Items

def items_history(request):
    # Get all items from the database
    items = Items.objects.all()

    # Calculate creation and output histories
    creation_history = {}
    output_history = {}

    for item in items:
        # Check if the item has been created by a worker
        if item.items_creator:
            creator_name = item.items_creator.name  # Replace 'name' with the actual attribute of the Worker model representing the name of the worker.
            creation_history[creator_name] = creation_history.get(creator_name, 0) + 1

        # Check if the item has been sold (output)
        if item.items_outprice:
            output_history[item.items_name] = output_history.get(item.items_name, 0) + 1

    return render(request, 'history_template.html', {
        'creation_history': creation_history,
        'output_history': output_history,
    })

def calculate_profit(item):
    return item.items_outprice - item.items_inprice

#####

def calculate_profit(item):
    return item.items_outprice - item.items_inprice

def calculate_total_profit(items):
    total_profit = 0
    for item in items:
        total_profit += calculate_profit(item)
    return total_profit

def item_list(request):
    all_items = Items.objects.all()
    total_profit = calculate_total_profit(all_items)
    
    context = {
        'items': all_items,
        'total_profit': total_profit,
    }
    
    return render(request, 'item_list.html', context)

