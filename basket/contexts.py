from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    # Get basket from session memory or initiate empty dictionary.
    basket = request.session.get('basket', {})

    # For each item and quantity in basket,
    # retrieve product details from Product model.
    # Then update the total (cost), produc count and basket_items.
    for item_id, qty in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += qty * product.price
        product_count += qty
        basket_items.append({
            'item_id': item_id,
            'qty': qty,
            'product': product,
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
