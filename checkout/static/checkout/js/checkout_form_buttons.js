// Check the required input fields on the personal tab all have values.  If so, enable delivery tab and next button.  Else disable both.
function checkPersonalDetails() {
    if (($('#id_full_name').val() != "") && ($('#id_email').val() != "") && ($('#id_phone_number').val() != "")) {
        $('#personal-to-delivery').prop('disabled', false);
        $('#delivery-tab').removeClass('disabled');
    } else {
        $('#personal-to-delivery').prop('disabled', true);
        $('#delivery-tab').addClass('disabled');
        $('#delivery-to-pay').prop('disabled', true);
        $('#pay-tab').addClass('disabled');
    }
}

// Check the required input fields on the delivery tab all have values.  If so, enable pay tab and next button.  Else disable both.
function checkDeliveryDetails() {
    if (($('#id_street_address1').val() != "") && ($('#id_town_or_city').val() != "") && ($('#id_country').val() != "")) {
        $('#delivery-to-pay').prop('disabled', false);
        $('#pay-tab').removeClass('disabled');
    } else {
        $('#delivery-to-pay').prop('disabled', true);
        $('#pay-tab').addClass('disabled');
    }
}

// Call checkPersonalDetails whenever there is an input on any of the required fields on the Personal tab.
$('#personal :input[required]').on('input', function() {
    checkPersonalDetails();
});

// Call checkDeliveryDetails whenever there is an input on any of the required fields on the Delivery tab.
$('#delivery :input[required]').on('input', function() {
    checkDeliveryDetails();
});

// Move to delivery tab when next button on personal tab or delivery tab button is clicked and call checkDeliveryDetails.
$('#personal-to-delivery, #delivery-tab').click(function(e) {
    e.preventDefault();
    $('#personal').removeClass("active show");
    $('#personal-tab').removeClass("active").attr("aria-selected", "false");
    $('#delivery').addClass("active show");
    $('#delivery-tab').addClass("active").attr("aria-selected", "true");
    checkDeliveryDetails();
});

// Move to personal tab when prev button on delivery tab is clicked and call checkPersonalDetails.
$('#delivery-to-personal, #personal-tab').click(function(e) {
    e.preventDefault();
    $('#delivery').removeClass("active show");
    $('#delivery-tab').removeClass("active").attr("aria-selected", "false");
    $('#personal').addClass("active show");
    $('#personal-tab').addClass("active").attr("aria-selected", "true");
    checkPersonalDetails();
});

// Move to pay tab when next button on delivery tab is clicked.
$('#delivery-to-pay, #pay-tab').click(function(e) {
    e.preventDefault();
    $('#delivery').removeClass("active show");
    $('#delivery-tab').removeClass("active").attr("aria-selected", "false");
    $('#pay').addClass("active show");
    $('#pay-tab').addClass("active").attr("aria-selected", "true");
});

// Move to delivery tab when prev button on pay tab is clicked and call checkDeliveryDetails.
$('#pay-to-delivery, #delivery-tab').click(function(e) {
    e.preventDefault();
    $('#pay').removeClass("active show");
    $('#pay-tab').removeClass("active").attr("aria-selected", "false");
    $('#delivery').addClass("active show");
    $('#delivery-tab').addClass("active").attr("aria-selected", "true");
    checkDeliveryDetails();
});