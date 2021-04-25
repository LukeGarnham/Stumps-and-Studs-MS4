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

    # For each item and quantity in basket,
    # retrieve product details from Product model.
    # Then sum up the total (cost), product count and basket_items.
    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'qty': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_data)
            for size, qty in item_data['items_by_size'].items():
                total += item_data * product.price
                product_count += item_data
                basket_items.append({
                    'item_id': item_id,
                    'qty': item_data,
                    'product': product,
                    'size': size,
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
