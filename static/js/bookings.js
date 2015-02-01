// CSRF protection from alanhamlett: https://gist.github.com/alanhamlett/6316427
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (settings.type == 'POST' || settings.type == 'PUT' || settings.type == 'DELETE') {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    }
});

function populatePage() {
  var day = new Date();
  day.setDate(day.getDate() + 2);

  $(function() {
    $( "#datepicker" ).datepicker();
  });

  $("#datepicker").val((day.getMonth() + 1).toString() + "/" + (day.getDay() + 1).toString() + "/" + (1900 + day.getYear()).toString());
  $("#start_time").val((day.getHours()+1).toString() + ":00");
  $("#end_time").val((day.getHours()+2).toString() + ":00");
}

function draw_cal(cal) {
    $(".calenders > iframe").removeClass("active-calender");
    $("#" + cal).addClass("active-calender");
}

function was_booking(data) {
	if (data['result']) {
		alert("The booking has been made.")
	} else {
		alert("The booking failed either because it was already taken, or because you booked an unavailable time.")
	}
}

function validate_input() {
	var invalid_input = [];
	var today = new Date();

	date_fields = $('#datepicker').val().split('/');
	if (date_fields.length !== 3) { 
		return false; 
	}
	if (!(Date.parse(date_fields[0] + "/" + date_fields[1] + "/" + date_fields[2]))) { 
		return false;
	}
	day = new Date(date_fields[0] + "/" + date_fields[1] + "/" + date_fields[2]);
	end_day = new Date(date_fields[0] + "/" + date_fields[1] + "/" + date_fields[2]);

	start_time = $('#start_time').val()
	if (!(start_time.match('^[0-2]?[0-9](:[0-5][0-9])?( )?([pPaA][mM])?$'))) {
	    return false; 
	}
	start_time_suffix = start_time.substring(start_time.length-2, start_time.length);
	if (start_time_suffix.match('[pPaA][mM]')) {
		start_time = start_time.substring(0, start_time.length-2);
	}
	start_time_components = start_time.split(":").map(Number);
	if (start_time_suffix.match('[pPaA][mM]') && start_time_components[0] === 12 ) {
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

	end_time = $('#end_time').val()
	if (!(end_time.match('^[0-2]?[0-9](:[0-5][0-9])?( )?([pPaA][mM])?$'))) { 
		return false; 
	}
	end_time_suffix = end_time.substring(end_time.length-2, end_time.length);
	if (end_time_suffix.match('[pPaA][mM]')) {
		end_time = end_time.substring(0, end_time.length-2);
	}
	end_time_components = end_time.split(":").map(Number);
	if (end_time_suffix.match('[pPaA][mM]') && end_time_components[0] === 12 ) {
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

	return {start: day.toISOString(), end: end_day.toISOString(), calendar_id: $("#calendar_id").val(), eventname: $("#eventname").val(),
            contactname: $("#contactname").val(), contactemail: $("#contactemail").val(), organisation: $("#organisation").val()
    };
}

populatePage();

$("form").submit(function(event) {
	var validated_input = validate_input();
	if (validated_input) {
		event.preventDefault();
		$.ajax({
			type: "POST",
			url: post_url,
			data: validated_input,
			success: was_booking
		})
	}
});
