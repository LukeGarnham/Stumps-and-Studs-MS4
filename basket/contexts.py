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
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'product': product,
                'details': [{
                    'qty': item_data,
                }]
            })
        else:
            # If item data not an integer, it will be a list of dicts.
            product = get_object_or_404(Product, pk=item_id)
            basket_items.append({
                'item_id': item_id,
                'product': product,
                # Create an empty list to append each
                # product with it's specific details.
                'details': [],
            })
            # Cycle through each dict in list for this product.
            for item in item_data:
                # Increment total (£) and product count variables.
                total += item['qty'] * product.price
                product_count += item['qty']
                # Cycle through all basket dicts.
                for basket_item in basket_items:
                    # Find the dict for this item.
                    # Append the product details to in the detail list.
                    if basket_item['item_id'] == item_id:
                        basket_item['details'].append({
                            'qty': item['qty'],
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
