from django.shortcuts import render, redirect


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

    # Product with details: {item_id:[
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
