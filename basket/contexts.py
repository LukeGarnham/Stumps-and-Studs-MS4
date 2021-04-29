from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    """ Make elements of the basket available throughout site. """

    basket_items = []
    total = 0
    product_count = 0
    # Get basket from session memory or initiate empty dictionary.
    basket = request.session.get('basket', {})

    # For each item in basket, retrieve product details from Product model.
    # Then sum up the total (cost), product count and basket_items.
    for item_id, item_data in basket.items():
        # Check if the item data is an integer.
        if isinstance(item_data, int):
            # If so, increment variables accordingly.
            product = get_object_or_404(Product, pk=item_data)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'qty': item_data,
                'product': product,
            })
        else:
            # If item data not an integer, it will be a list of dicts.
            product = get_object_or_404(Product, pk=item_id)
            for item in item_data:
                # Cycle through each dict in list, increment variables.
                total += item['qty'] * product.price
                product_count += item['qty']
                basket_items.append({
                    'item_id': item_id,
                    'qty': item['qty'],
                    'product': product,
                    'size': item['size'],
                    'side': item['side'],
                    'gender': item['gender'],
                })

    # If there is something in the basket,
    # retrieve delivery cost from global settings.
    # Otherwise, set deliver cost to £0.
    if total != 0:
        delivery = Decimal(settings.STANDARD_DELIVERY_COST)
    else:
        delivery = 0
    grand_total = total + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
