from django.shortcuts import render, redirect


def view_basket(request):
    """A view to return the basket page"""

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the product to the basket """

    qty = int(request.POST.get('qty'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += qty
    else:
        basket[item_id] = qty

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
