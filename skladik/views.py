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
