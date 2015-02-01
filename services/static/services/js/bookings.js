/**
 * Initialize the jquery ui and pre-populate the time and date fields
 */
function populatePage() {
    var day = new Date();
    day.setDate(day.getDate() + 2);

    $(function () {
        $("#datepicker").datepicker();
        $("#start_time").timepicker({'timeFormat': 'hh:mmtt'});
        $("#end_time").timepicker({'timeFormat': 'hh:mmtt'});
    });

    $("#datepicker").val((day.getMonth() + 1).toString() + "/" + (day.getDay() + 1).toString() + "/" + (1900 + day.getYear()).toString());
    $("#start_time").val((day.getHours() + 1).toString() + ":00");
    $("#end_time").val((day.getHours() + 2).toString() + ":00");
}

/**
 * Swap the calendar which is currently being viewed
 */
function change_cal(cal) {
    $(".calendars > iframe").removeClass("active-calendar");
    $("#" + cal).addClass("active-calendar");
}

/**
 * Alert the status of the booking
 * e.g. if the returned AJAX doesn't return a result then the booking failed, likely due to user action
 */
function was_booking(data) {
    if (data.result) {
        alert("The booking has been made.");
    } else {
        alert("The booking failed either because it was already taken, or because you booked an unavailable time.");
    }
}

/**
 * validate the user input and returned it once it's been cleaned
 *
 * returns:
 *      {Dict} of the form data, or False if invalid
 */
function validate_input() {
    var invalid_input = [];
    var today = new Date();
    var time_regex = '^[0-2]?[0-9](:[0-5][0-9])?( )?([pPaA][mM])?$';

    var date_fields = $('#datepicker').val().split('/');
    var start_time = $('#start_time').val();
    var end_time = $('#end_time').val();

    // if the date field is incorrect or the start/end time are incorrect formats, fail
    if (date_fields.length !== 3 || !(Date.parse(date_fields[0] + "/" + date_fields[1] + "/" + date_fields[2])) || !start_time.match(time_regex) || !end_time.match(time_regex)) {
        return false;
    }
    var day = new Date(date_fields[0] + "/" + date_fields[1] + "/" + date_fields[2]);
    var end_day = new Date(date_fields[0] + "/" + date_fields[1] + "/" + date_fields[2]);

    var start_time_suffix = start_time.substring(start_time.length - 2, start_time.length);
    if (start_time_suffix.match('[pPaA][mM]')) {
        start_time = start_time.substring(0, start_time.length - 2);
    }
    var start_time_components = start_time.split(":").map(Number);
    if (start_time_suffix.match('[pPaA][mM]') && start_time_components[0] === 12) {
        start_time_components[0] = 0;
    }
    if (start_time_suffix.match('[pP][mM]')) {
        start_time_components[0] += 12;
    }
    if (start_time_components[0] > 23) {
        return false;
    }

    day.setHours(start_time_components[0]);
    if (start_time_components[1]) day.setMinutes(start_time_components[1]);

    if (day - today < 172800000) {
        return false;
    } // booking earlier in advance than 48 hours
    var end_time_suffix = end_time.substring(end_time.length - 2, end_time.length);
    if (end_time_suffix.match('[pPaA][mM]')) {
        end_time = end_time.substring(0, end_time.length - 2);
    }
    var end_time_components = end_time.split(":").map(Number);
    if (end_time_suffix.match('[pPaA][mM]') && end_time_components[0] === 12) {
        end_time_components[0] = 0;
    }
    if (end_time_suffix.match('[pP][mM]')) {
        end_time_components[0] += 12;
    }

    if (end_time_components[0] > 23) {
        return false;
    }

    end_day.setHours(end_time_components[0]);
    if (end_time_components[1]) end_day.setMinutes(end_time_components[1]);

    if ((start_time_components[0] === end_time_components[0]) &&
        ((start_time_components.length === 1 && end_time_components.length === 1) ||
            ((start_time_components.length === 2 && end_time_components.length === 2) && (start_time_components[1] === end_time_components[1])))) {
        return false;
    }

    // If end_time comes before start_time, end_day should be the next day
    if ((start_time_components[0] > end_time_components[0]) ||
        ((start_time_components[0] === end_time_components[0]) && ((start_time_components.length > end_time_components.length) ||
            (start_time_components[1] > end_time_components[1])))) {
        end_day.setDate(end_day.getDate() + 1);
    }

    return {'start': day.toISOString(),
        'end': end_day.toISOString(),
        'calendar_id': $("#calendar_id").val(),
        'eventname': $("#eventname").val(),
        'contactname': $("#contactname").val(),
        'contactemail': $("#contactemail").val(),
        'organisation': $("#organisation").val()
    };
}

populatePage();

$("form").submit(function (event) {
    var validated_input = validate_input();
    if (validated_input !== false) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: post_url,
            data: validated_input,
            success: was_booking
        });
    }
});
