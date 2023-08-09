# your_app_name/templatetags/your_app_name_filters.py

from django import template

register = template.Library()

@register.filter(name='calculate_profit')
def calculate_profit(item):
    return item.items_outprice - item.items_inprice
