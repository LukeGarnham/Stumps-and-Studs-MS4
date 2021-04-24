from django.shortcuts import render


def view_basket(request):
    """A view to return the basket page"""

    return render(request, 'basket/basket.html')
