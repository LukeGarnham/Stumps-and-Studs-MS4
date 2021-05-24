// Source: https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/a75791ce63bfce9a05f614d7712199c893063ed9/checkout/static/checkout/js/stripe_elements.js

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#04080F',
        fontFamily: '"Open Sans", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#FE7F2D',
        iconColor: '#FE7F2D'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle validation errors on the card element.
card.addEventListener('change', function(e) {
    var errorDiv = $('#card-errors');
    if (e.error) {
        var html = `
            <i class="fas fa-exclamation-triangle" style="color: #FE7F2D;"></i>
            <span class="fs-small" style="color: #FE7F2D;">
                ${e.error.message}
            </span>
        `;
        $(errorDiv).html(html);
        $('#submit-button').prop('disabled', true);
    } else {
        errorDiv.textContent = '';
        $('#submit-button').prop('disabled', false);
    }
});

// Handle Stripe payment when form is submitted.
// https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements#web-submit-payment
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    // Prevent default event when form is submitted.
    ev.preventDefault();
    // Disable the card so no more changes can be made.
    card.update({'disabled': true});
    $('#submit-button').prop('disabled', true);
    // Hide the form and show the loading-overlay.
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    // Create boolean variable for whether user has checked the save info box.
    var saveInfo = $('#id-save-info').is(':checked');
    // Get the csrf token from the form.
    var csrfToken = $('input[name="csrfmiddlewaretoken').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';
    $.post(url, postData).done(function() {
        // Call the Stripe confirmCardPayment function, passing the client secret and card details.
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    email: $.trim(form.email.value),
                    phone: $.trim(form.phone_number.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        state: $.trim(form.county.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    state: $.trim(form.county.value),
                    postal_code: $.trim(form.postcode.value),
                    country: $.trim(form.country.value),
                }
            },
        // Check the result of the confirmCardPayment function.
        }).then(function(result) {
                // If there's an error, show error to the customer in the #card-errors div.
                if (result.error) {
                    var errorDiv = $('#card-errors');
                    var html = `
                        <i class="fas fa-exclamation-triangle" style="color: #FE7F2D;"></i>
                        <span class="fs-small" style="color: #FE7F2D;">
                            ${result.error.message}
                        </span>
                    `;
                    $(errorDiv).html(html);
                    // Hide the loading-overlay and show the form.
                    $('#payment-form').fadeToggle(100);
                    $('#loading-overlay').fadeToggle(100);
                    // We also need to re-enable card field and submit-form button so users can try again.
                    card.update({'disabled': false});
                    $('#submit-button').prop('disabled', false);
                // If the payment is successfully processed, submit the form.
                } else {
                    if (result.paymentIntent.status === 'succeeded') {
                        form.submit();
                    }
                }
        });
    }).fail(function() {
        // Reload the page, the error will be in Django messages.
        location.reload();
    });

});
