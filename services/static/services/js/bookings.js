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

function check_input(input) {
    var classes = input.classList;
    if (input.type === 'submit') return true;
    if (!input.value.length) {
        return false;
    }
    if (classes.contains("timepicker") > -1) {
        
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