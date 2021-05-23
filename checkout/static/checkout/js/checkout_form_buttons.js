// Script to handle checkout form next and previous buttons.

// Check the required input fields on the personal tab are complete when there is an input on any one of them and enable/disable delivery.
$('#personal :input[required]').on('input', function() {
    if (($('#id_full_name').val() != "") && ($('#id_email').val() != "") && ($('#id_phone_number').val() != "")) {
        $('#personal-to-delivery').prop('disabled', false);
        $('#delivery-tab').removeClass('disabled');
    } else {
        $('#personal-to-delivery').prop('disabled', true);
        $('#delivery-tab').addClass('disabled');
        $('#delivery-to-pay').prop('disabled', true);
        $('#pay-tab').addClass('disabled');
    }
});

// Move to delivery tab when next button on personal tab is clicked.
$('#personal-to-delivery').click(function(e) {
    e.preventDefault();
    $('#personal').removeClass("active show");
    $('#personal-tab').removeClass("active").attr("aria-selected", "false");
    $('#delivery').addClass("active show");
    $('#delivery-tab').addClass("active").attr("aria-selected", "true");
    if (($('#id_street_address1').val() != "") && ($('#id_town_or_city').val() != "") && ($('#id_country').val() != "")) {
        $('#delivery-to-pay').prop('disabled', false);
        $('#pay-tab').removeClass('disabled');
    }
});

// Move to personal tab when prev button on delivery tab is clicked.
$('#delivery-to-personal').click(function(e) {
    e.preventDefault();
    $('#delivery').removeClass("active show");
    $('#delivery-tab').removeClass("active").attr("aria-selected", "false");
    $('#personal').addClass("active show");
    $('#personal-tab').addClass("active").attr("aria-selected", "true");
});

// Check the required input fields on the delivery tab are complete when page loads and enable/disable pay.
$('#delivery :input[required]').on('load', function() {
    if (($('#id_street_address1').val() != "") && ($('#id_town_or_city').val() != "") && ($('#id_country').val() != "")) {
        $('#delivery-to-pay').prop('disabled', false);
        $('#pay-tab').removeClass('disabled');
    } else {
        $('#delivery-to-pay').prop('disabled', true);
        $('#pay-tab').addClass('disabled');
    }
});

// Check the required input fields on the delivery tab are complete when there is an input on any one of them and enable/disable pay.
$('#delivery :input[required]').on('input', function() {
    if (($('#id_street_address1').val() != "") && ($('#id_town_or_city').val() != "") && ($('#id_country').val() != "")) {
        $('#delivery-to-pay').prop('disabled', false);
        $('#pay-tab').removeClass('disabled');
    } else {
        $('#delivery-to-pay').prop('disabled', true);
        $('#pay-tab').addClass('disabled');
    }
});

// Move to pay tab when next button on delivery tab is clicked.
$('#delivery-to-pay').click(function(e) {
    e.preventDefault();
    $('#delivery').removeClass("active show");
    $('#delivery-tab').removeClass("active").attr("aria-selected", "false");
    $('#pay').addClass("active show");
    $('#pay-tab').addClass("active").attr("aria-selected", "true");
});

// Move to delivery tab when prev button on pay tab is clicked.
$('#pay-to-delivery').click(function(e) {
    e.preventDefault();
    $('#pay').removeClass("active show");
    $('#pay-tab').removeClass("active").attr("aria-selected", "false");
    $('#delivery').addClass("active show");
    $('#delivery-tab').addClass("active").attr("aria-selected", "true");
});