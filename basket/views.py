from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


def view_basket(request):
    """A view to return the basket page"""

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the product to the basket """

    # Get the product from the Product model.
    product = get_object_or_404(Product, pk=item_id)
    # Get quantity and redirect_url from the submitted (POST) form.
    qty = int(request.POST.get('qty'))
    redirect_url = request.POST.get('redirect_url')

    size = None
    side = None
    gender = None
    # If there is a product size, side or gender in the submitted (POST) form
    # then assign them to variables. Also create strings for use in messages.
    if 'product_size' in request.POST:
        size = request.POST.get('product_size')
        size_str = f'Size {size.upper()} '
    else:
        size_str = ''
    if 'product_side' in request.POST:
        side = request.POST.get('product_side')
        side_str = f'{side.capitalize()}-Handed '
    else:
        side_str = ''
    if 'product_gender' in request.POST:
        gender = request.POST.get('product_gender')
        gender_str = f'{gender.capitalize()} '
    else:
        gender_str = ''
    basket = request.session.get('basket', {})

    # Product with details structure: {item_id:[
    #   {'size':size, 'side':side, 'gender':gender, 'qty':qty},
    # ]}
    if size or side or gender:
        # If the product being added to the basket
        # has either a size, side or gender:
        # Check if the product is already in the basket.
        if item_id in list(basket.keys()):
            # If so, cycle through the list of dicts.
            for item in basket[item_id]:
                # Check whether the details match a product already in basket.
                if (item['size'] == size and
                        item['side'] == side and item['gender'] == gender):
                    # If there is a product with same size, side & gender
                    # increment quantity and break out of loop.
                    # Check quantity doesn't exceed 99 before adding.
                    print(item['qty'])
                    print(qty)
                    if item['qty'] + qty > 99:
                        print('option 1')
                        item['qty'] = 99
                        messages.info(request, f'{size_str}{side_str}\
                            {gender_str}{product.name} quantity is \
                                limited to {item["qty"]}.')
                    else:
                        item['qty'] += qty
                        messages.success(request, f'Updated {size_str}{side_str}\
                            {gender_str}{product.name} quantity to \
                                {item["qty"]}.')
                    break
            else:
                # If no match found, apend the product details to the dict.
                # Add check to ensure frontend not bipassed.
                # Limit quantity to max of 99.
                if qty > 99:
                    qty = 99
                basket[item_id].append({
                    'size': size,
                    'side': side,
                    'gender': gender,
                    'qty': qty,
                })
                messages.success(request, f'Added {size_str}{side_str}'
                                 f'{gender_str}{product.name} to your basket.')
        else:
            # If product is not already in basket, add value to product key.
            # Create a list of dicts with one dict containing product details.
            # Add check to ensure frontend not bipassed.
            # Limit quantity to max of 99.
            if qty > 99:
                qty = 99
            basket[item_id] = [{
                'size': size,
                'side': side,
                'gender': gender,
                'qty': qty,
            }]
            messages.success(request, f'Added {size_str}{side_str}{gender_str}'
                             f'{product.name} to your basket.')
    else:
        # If the product doesn't have any details we
        # first check if the product is already in the basket.
        if item_id in list(basket.keys()):
            # If so, then we increase the quantity
            # Check quantity doesn't exceed 99 before adding.
            if basket[item_id] + qty > 99:
                basket[item_id] = 99
                messages.info(request, f'{product.name} quantity is \
                    limited to {basket[item_id]}.')
            else:
                basket[item_id] += qty
                messages.success(request, f'Updated {product.name} \
                                quantity to {basket[item_id]}.')
        else:
            # Add check to ensure frontend not bipassed.
            # Limit quantity to max of 99.
            if qty > 99:
                qty = 99
            basket[item_id] = qty
            messages.success(request, f'Added {product.name} to your basket.')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust the quantity of a product in
    the basket from within the basket page """

    # Get the product from the Product model.
    product = get_object_or_404(Product, pk=item_id)
    # Get quantity and redirect_url from the submitted (POST) form.
    qty = int(request.POST.get('qty'))

    size = None
    side = None
    gender = None
    # If there is a product size, side or gender in the submitted (POST) form
    # then assign them to variables. Also create strings for use in messages.
    if 'product_size' in request.POST:
        size = request.POST.get('product_size')
        size_str = f'Size {size.upper()} '
    else:
        size_str = ''
    if 'product_side' in request.POST:
        side = request.POST.get('product_side')
        side_str = f'{side.capitalize()}-Handed '
    else:
        side_str = ''
    if 'product_gender' in request.POST:
        gender = request.POST.get('product_gender')
        gender_str = f'{gender.capitalize()} '
    else:
        gender_str = ''
    basket = request.session.get('basket', {})

    if size or side or gender:
        # If the product being adjusted in the basket
        # has either a size, side or gender:
        # Iterate through the products list of dicts
        # to find the item with the same details.
        for item in basket[item_id]:
            if (item['size'] == size and
                    item['side'] == side and item['gender'] == gender):
                if qty > 0:
                    # If new quantity is greater than 0, update quantity.
                    # First need to check if quantity exceeds the max of 99.
                    if item['qty'] + qty > 99:
                        item['qty'] = 99
                        messages.info(request, f'{size_str}{side_str}\
                            {gender_str}{product.name} quantity is \
                                limited to {item["qty"]}.')
                    else:
                        item['qty'] = qty
                        messages.success(request, f'Updated {size_str}{side_str}\
                            {gender_str}{product.name} quantity to \
                                {item["qty"]}.')
                else:
                    # Otherwise, remove (delete) the item (dict).
                    basket[item_id].remove(item)
                    # If the list is empty, remove product from basket.
                    if basket[item_id] == []:
                        basket.pop(item_id)
                    messages.success(request, f'Removed {size_str}{side_str}\
                        {gender_str}{product.name} from your basket.')
    else:
        # If product has no size, side or gender, update quantity.
        if qty > 0:
            # If new quantity greater than 0, update quantity.
            # Check that quantity doesn't exceed the max of 99.
            if basket[item_id] + qty > 99:
                basket[item_id] = 99
                messages.info(request, f'{product.name} quantity is \
                    limited to {basket[item_id]}.')
            else:
                basket[item_id] = qty
                messages.success(request, f'Updated {product.name} \
                    quantity to {basket[item_id]}.')
        else:
            # Otherwise, remove (pop) item from list.
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name}'
                             ' from your basket.')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove a product from basket within the basket page """

    # Get the product from the Product model.
    product = get_object_or_404(Product, pk=item_id)
    # If there is a product size, side or gender in the submitted (POST) form
    # then assign them to variables. Also create strings for use in messages.
    size = request.POST.get('product_size')
    size_str = f'Size {size.upper()} '
    side = request.POST.get('product_side')
    side_str = f'{side.capitalize()}-Handed '
    gender = request.POST.get('product_gender')
    gender_str = f'{gender.capitalize()} '

    # If there is no data, JS passes through the variable as None in string
    # format.  Change to the None object.  Change strings for use in messages.
    if size == 'None':
        size = None
        size_str = ''
    if side == 'None':
        side = None
        side_str = ''
    if gender == 'None':
        gender = None
        gender_str = ''

    basket = request.session.get('basket', {})

    try:
        if size or side or gender:
            # If the product being removed from the basket
            # has either a size, side or gender:
            # Iterate through the products list of dicts
            # to find the item with the same details.
            for item in basket[item_id]:
                if (item['size'] == size and
                   item['side'] == side and item['gender'] == gender):
                    # Remove (delete) the dict.
                    basket[item_id].remove(item)
                    # If the list is empty, remove product from basket.
                    if basket[item_id] == []:
                        basket.pop(item_id)
                    messages.success(request, f'Removed {size_str}'
                                     f'{side_str}{gender_str}'
                                     f'{product.name} from your basket.')
        else:
            # If product has no size, side or gender,
            # remove product from basket.
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name}'
                             ' from your basket.')

        request.session['basket'] = basket
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
