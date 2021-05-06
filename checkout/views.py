from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from basket.contexts import basket_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, something went wrong.  Your payment \
            cannot be processed right now.  Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    # Retrieve the keys from settings where (in turn)
    # they are retrieved from the environment.
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # If form has been submitted (POST) retrieve posted data.
    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            # Cycle through all items (kay, values) in basket dict.
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    # If value is integer then it has no details.
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            qty=item_data,
                        )
                        order_line_item.save()
                    # Otherwise, item has details (size, side, gender, qty).
                    else:
                        # Cycle through each item in the list.
                        for item in item_data:
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                product_size=item['size'],
                                product_side=item['side'],
                                product_gender=item['gender'],
                                qty=item['qty'],
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket doesn't exist in \
                            our database.  Please call us for assistance.")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
        else:
            messages.error(request, "Order not processed!  There was an error with your \
                form. Please double check your information and try again.")
    else:
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
            currency=settings.STRIPE_CURRENCY,
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


def checkout_success(request, order_number):
    """ Handle succussful checkout page. """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order sucessfully placed! \
        Your order number is {order_number}.  A confirmation \
        email has been sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
