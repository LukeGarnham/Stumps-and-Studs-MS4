from django.shortcuts import render, redirect, reverse, HttpResponse


def view_basket(request):
    """A view to return the basket page"""

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the product to the basket """

    # Get quantity and redirect_url from the submitted (POST) form.
    qty = int(request.POST.get('qty'))
    redirect_url = request.POST.get('redirect_url')

    size = None
    side = None
    gender = None
    # If there is a product size, side or gender in the submitted (POST) form
    # then assign them to variables.
    if 'product_size' in request.POST:
        size = request.POST.get('product_size')
    if 'product_side' in request.POST:
        side = request.POST.get('product_side')
    if 'product_gender' in request.POST:
        gender = request.POST.get('product_gender')
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
                    item['qty'] += qty
                    break
            else:
                # If no match found, apend the product details to the dict.
                basket[item_id].append({
                    'size': size,
                    'side': side,
                    'gender': gender,
                    'qty': qty,
                })
        else:
            # If product is not already in basket, add value to product key.
            # Create a list of dicts with one dict containing product details.
            basket[item_id] = [{
                'size': size,
                'side': side,
                'gender': gender,
                'qty': qty,
            }]
    else:
        # If the product doesn't have any details we
        # first check if the product is already in the basket.
        if item_id in list(basket.keys()):
            # If so, then we increase the quantity
            basket[item_id] += qty
        else:
            basket[item_id] = qty

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust the quantity of a product in
    the basket from within the basket page """

    # Get quantity and redirect_url from the submitted (POST) form.
    qty = int(request.POST.get('qty'))

    size = None
    side = None
    gender = None
    # If there is a product size, side or gender in the submitted (POST) form
    # then assign them to variables.
    if 'product_size' in request.POST:
        size = request.POST.get('product_size')
    if 'product_side' in request.POST:
        side = request.POST.get('product_side')
    if 'product_gender' in request.POST:
        gender = request.POST.get('product_gender')
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
                    item['qty'] = qty
                else:
                    # Otherwise, delete the item (dict).
                    del item
                    if basket[item_id] == []:
                        basket.pop(item_id)
    else:
        # If product has no size, side or gender, update quantity.
        if qty > 0:
            # If new quantity greater than 0, update quantity.
            basket[item_id] = qty
        else:
            # Otherwise, remove (pop) item from list.
            basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove a product from basket within the basket page """

    # If there is a product size, side or gender in the submitted (POST) form
    # then assign them to variables.
    size = request.POST.get('product_size')
    side = request.POST.get('product_side')
    gender = request.POST.get('product_gender')

    # If there is no data, JS passes through the variable as None in string
    # format.  Change to the None object.
    if size == 'None':
        size = None
    if side == 'None':
        side = None
    if gender == 'None':
        gender = None

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
                    if basket[item_id] == []:
                        basket.pop(item_id)
        else:
            # If product has no size, side or gender, update quantity.
            basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
