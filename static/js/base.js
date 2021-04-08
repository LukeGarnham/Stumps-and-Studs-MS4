$(document).ready(function() {

    let screenWidth = $(window).width();
    if (screenWidth < 768) {
        $(" #nav-search ").hide();
    }

    $( window ).resize(function() {
        let activeScreenWidth = $(window).width();
        if (activeScreenWidth >= 768) {
            $(" #nav-search ").show();
        } else {
            $(" #nav-search ").hide();
        }
      });

    $( "#search-button" ).on( "click", function() {
        $(" #nav-search ").toggle("blind", 500);
    });

});