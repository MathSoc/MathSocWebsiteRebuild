var calendar_codes = {
    "cnd": "qppn4tv70id73d9ib9gj3t7iio@group.calendar.google.com",
    "comfy": "uo9gqhdmiain37s82pa7n7dsck@group.calendar.google.com",
    "hallway": "ccrmlglti2hug3dg7c732kflbs@group.calendar.google.com",
    "new-proj": "t6jk1rnneup9pkg8kifs3ccl8k@group.calendar.google.com",
    "karaoke": "k0ki15rfeu4sq4cpb9ion6npdo@group.calendar.google.com"
}

/**
 * Swap the calendar which is currently being viewed
 */
function change_cal(cal) {
    $("#calendar").attr('src', 'https://www.google.com/calendar/embed?src=' + 
                                calendar_codes[cal] + '&ctz=America/Toronto');
}

function parseTime(text) {
    function pad_to_two_chars(number) {
        return (number > 9) ? number : "0" + number;
    }

    var hour = 0;
    var minutes = 0;

    if (/\d{1,2}:\d{1,2}/.test(text)) {
        var match = text.match(/(\d{1,2}):(\d{1,2})/);
        if (!match) return false;
        var hour = Number(match[1]);
        var minutes = Number(match[2]);
    } else if (/\d\d\d\d/.test(text)) {
        var hour = Number(text[0] + text[1]);
        var minutes = Number(text[2] + text[3]);
    } else if (/\d\d\d/.test(text)) {
        var hour = Number(text[0]);
        var minutes = Number(text[1] + text[2]);
    } else if (/\d\d/.test(text)) {
        var hour = Number(text[0] + text[1]);
    } else if (/\d/.test(text)) {
        var hour = Number(text[0]);
    }

    if (/[pP][mM]/.test(text) || (!/[aA][mM]/.test(text) && (hour < 9))) {
        if (hour != 12) hour += 12;
    }

    if (hour > 23 || hour < 0 || minutes < 0 || minutes > 59) return false;

    if (hour > 11) {
        if (hour != 12) hour -= 12;
        return hour + ":" + pad_to_two_chars(minutes) + " PM";
    } else if (hour === 0) {
        return "12:" + pad_to_two_chars(minutes) + " AM";
    } else {
        return hour + ":" + pad_to_two_chars(minutes) + " AM";
    }
}

function check_input(input) {
    var classes = input.classList;
    if (input.type === 'submit') return true;

    if (!input.value.length) {
        return false;
    }
    
    if (classes.contains("timepicker") > -1) {
        var text = input.value;
        if (/\d{1,2}:?\d{0,2} ?([pPaA][mM])?/.test(text)) {
            var parsed = parseTime(text);
            if (!parsed) return false;
            input.value = parsed;
        } else {
            return false;
        }
    }
    return true;
}

$().ready(function () {
    function toShortISO(date) {
        function pad(num) { return (num < 10) ? '0' + num : num};
        return date.getFullYear() + "-" + 
                pad(date.getMonth() + 1) + "-" + 
                pad(date.getDate());
    }

    var picker = new Pikaday({ 
        field: $('#datepicker')[0],
        onSelect: function() {
            $("#datepicker").val(toShortISO(picker.getDate()));
        },
        minDate: new Date()
    });

    $("form").on('submit', function (event) {
        var form = $(this);
        event.preventDefault();
        var inputs = $("form").find("input").toArray();
        var all_inputs_validated = true;
        for (var i = 0; i < inputs.length; i++) {
            console.log(inputs[i], inputs[i].value)
            if (!check_input(inputs[i])) all_inputs_validated = false;
        }
        if (all_inputs_validated) {
            $("form").off('submit')
            form.submit();
        }
    });

    $("form input").on('change', function (event) {
        check_input(event.target)
    });
});