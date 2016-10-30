(function ($) {
    "use strict";

    window.console.log("run with ", post_url);

    var booked = function (data) {
        window.console.log("wasbooking");
        if (data.result) {
            window.console.log("data.result");
            window.alert(data.result);
        }
    };

    $("form").submit(function (event) {
        event.preventDefault();
        window.console.log("onclick");
        $.ajax({
            type: "POST",
            url: post_url,
            data: {'lockers': 'lockers'},
            success: booked
        });
    });
})(jQuery); // end of jQuery name space