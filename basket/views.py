from django.shortcuts import render, redirect


def view_basket(request):
    """A view to return the basket page"""

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the product to the basket """

    qty = int(request.POST.get('qty'))
    redirect_url = request.POST.get('redirect_url')

    size = None
    # side = None
    # gender = None
    if 'product_size' in request.POST:
        size = request.POST.get('product_size')
    # if 'product_side' in request.POST:
    #     side = request.POST.get('product_side')
    # if 'product_gender' in request.POST:
    #     gender = request.POST.get('product_gender')
    basket = request.session.get('basket', {})

    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += qty
            else:
                basket[item_id]['items_by_size'][size] = qty
        else:
            basket[item_id] = {'items_by_size': {size: qty}}
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += qty
        else:
            basket[item_id] = qty

    request.session['basket'] = basket
    return redirect(redirect_url)

    # # Product with details: {item_id:{details:
    # # {'size':size, 'side':side, 'gender':gender, 'qty':qty}}}
    # if size or side or gender:
    #     # If the product being added to the basket
    #     # has either a size, side or gender:
    #     # Check if the product is already in the basket.
    #     if item_id in list(basket.keys()):
    #         # If so, check whether the details match
    #         # any of the other product details.
    #         # If so, increase the quantity.
    #         # If not, we add the product details to the details dict.
    #         print('basket')
    #     else:
    #         # If product is already in basket, add details dict
    #         # containing product details.
    #         # basket[item_id] = {'details': {
    #         #     'size': size,
    #         #     'side': side,
    #         #     'gender': gender,
    #         #     'qty': qty,
    #         # }}
    #         basket[item_id] = {'items_by_size': {size: qty}}
    # # Product without details: {item_id:qty}
    # else:
    #     # If the product doesn't have any details we
    #     # first check if the product is already in the basket.
    #     if item_id in list(basket.keys()):
    #         # If so, then we increase the quantity
    #         basket[item_id] += qty
    #     else:
    #         basket[item_id] = qty

    # request.session['basket'] = basket
    # return redirect(redirect_url)
