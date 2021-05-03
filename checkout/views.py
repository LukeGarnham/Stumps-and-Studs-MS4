from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents

import stripe


def checkout(request):
    # Retrieve the keys from settings where (in turn)
    # they are retrieved from the environment.
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Check if there is any items in the basket in session memory.
    # If not, redirect user back to products.
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request,
                       "There's nothing in your basket at the moment.")
        return redirect(reverse('products'))

    # Use the basket_contents function in baskets/contexts.py
    # to get the current basket.  From it, assign the grand total to total.
    current_basket = basket_contents(request)
    total = current_basket['grand_total']

    # Stripe settings
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency = settings.STRIPE_CURRENCY,
    )

    # Check that a Stripe public key has been retrieved from settings.
    # If not, warn user that there is no Stripe public key in environment.
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is'
                         ' missing from the environment.')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
