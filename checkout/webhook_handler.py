from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product

import json
import time

# Source: https://github.com/Code-Institute-Solutions/boutique_ado_v1/
# blob/b5e178737596a1a1cf5be50345dc770b119918fd/checkout/webhook_handler.py

class StripeWH_Handler:
    """ Handles Stripe webhooks. """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event. """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle a successful webhook event from Stripe. """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details.
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    town_or_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | \
                    Success: Verified order already in database.',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    town_or_city=shipping_details.address.city,
                    county=shipping_details.address.state,
                    postcode=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(basket).items():
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
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | Error:  {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | Success: \
                Created order in webhook.',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle an unsuccessful webhook event from Stripe. """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
