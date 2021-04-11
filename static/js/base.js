$(document).ready(function() {

    var prevScrollpos = window.pageYOffset;
    // Functions to run whenever a page is scrolled.
    window.onscroll = function() {
        // Screenwidth is 17px out from actual screen width so adjustment made.
        var screenWidth = $(window).width() + 17;
        var currentScrollPos = window.pageYOffset;
        // If user has scrolled up on medium screens upwards.
        if (prevScrollpos > currentScrollPos && screenWidth >= 768) {
            // Show the navbar.
            $(".navbar").show("blind", 500);
        } else if (prevScrollpos < currentScrollPos && screenWidth >= 768) {
            // If user scrolls down on medium screens upwards hide the navbar.
            $(".navbar").hide("blind", 500);
        }
        prevScrollpos = currentScrollPos;
    };

    // Functions to run whenever the screen is resized.
    $( window ).resize(function() {
        var screenWidth = $(window).width() + 17;
        // If the screen width is less than 768px:
        if (screenWidth < 768) {
            // The navbar should always be visible when the menu button is clicked.
            $(".navbar").show();
        }
    });

});