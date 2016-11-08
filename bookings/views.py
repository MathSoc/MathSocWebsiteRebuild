from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
import logging
import datetime
import re
import pytz
import dateutil.parser

# Create your views here
from bookings.models import BookingRequest

logger = logging.getLogger(__name__)
EST = pytz.timezone('US/Eastern')

def get_time_from_string(request, timestr):
    start_time = re.split(' |:', timestr);

    hour = int(start_time[0])
    minutes = int(start_time[1])

    if hour < 1 or hour > 12 or minutes < 0 or minutes > 59:
        messages.error(request, "Invalid time given for start time")
        return render(request, 'bookings/bookings.html')

    if hour == 12:
        hour -= 12

    if start_time[2] == "PM":
        hour += 12

    return datetime.time(hour, minutes)

@login_required()
def bookings(request):
    if request.method == "POST":
        calendar_ids = {
            "cnd": "qppn4tv70id73d9ib9gj3t7iio@group.calendar.google.com",
            "comfy": "uo9gqhdmiain37s82pa7n7dsck@group.calendar.google.com",
            "hallway": "ccrmlglti2hug3dg7c732kflbs@group.calendar.google.com",
            "new-proj": "t6jk1rnneup9pkg8kifs3ccl8k@group.calendar.google.com",
            "karaoke": "k0ki15rfeu4sq4cpb9ion6npdo@group.calendar.google.com"
        }

        invalid_input = False

        def validate_input(type):
            if not request.POST[type]:
                messages.error(request, "Invalid entry for: " + type.replace("-", " ").title())
                invalid_input = True
                return False
            return True

        validate_input("contact-name")
        validate_input("contact-email")
        validate_input("organisation")
        validate_input("event-name")
        validate_input("contact-phone")

        if invalid_input:
            return render(request, 'bookings/bookings.html')

        if request.POST['calendar_id'] not in calendar_ids:
            messages.error(request, "Invalid calendar selected")
            return render(request, 'bookings/bookings.html')

        if not re.match(r"\d{1,2}:\d\d [AP]M", request.POST['start-time']):
            messages.error(request, "Invalid format for starting time (correct example: 1:30 PM)")
            return render(request, 'bookings/bookings.html')

        if not re.match(r"\d{1,2}:\d\d [AP]M", request.POST['end-time']):
            messages.error(request, "Invalid format for end time (correct example: 1:30 PM)")
            return render(request, 'bookings/bookings.html')

        if not re.match(r"\d\d\d\d-\d\d-\d\d", request.POST['date']):
            messages.error(request, "Invalid date format (format is YYYY-MM-DD)")
            return render(request, 'bookings/bookings.html')

        if not request.POST['agreement'] == "on":
            messages.error(request, "Please agree to the Room and Equipment Booking Policy")
            return render(request, 'bookings/bookings.html')

        start = dateutil.parser.parse(request.POST['date'], yearfirst=True)
        start_time = get_time_from_string(request, request.POST['start-time'])

        start = datetime.datetime.combine(start.date(), start_time)
        start = EST.localize(start)

        now = datetime.datetime.now(pytz.UTC)
        if start < now:
            messages.error(request, "Please select a start time in the future")
            return render(request, 'bookings/bookings.html')

        end = dateutil.parser.parse(request.POST['date'], yearfirst=True)
        end_time = get_time_from_string(request, request.POST['end-time'])
        if end_time <= start_time:
            end += datetime.timedelta(days=1)

        end = datetime.datetime.combine(end.date(), end_time)
        end = EST.localize(end)

        new_request = BookingRequest(
            calendar_id=calendar_ids[request.POST['calendar_id']],
            calendar=request.POST['calendar_id'],
            requesting_id=request.user.username,
            contact_name=request.POST['contact-name'],
            contact_email=request.POST['contact-email'],
            contact_phone=request.POST['contact-phone'],
            organisation=request.POST['organisation'],
            event_name=request.POST['event-name'],
            start = start,
            end = end)

        new_request.save()
        messages.success(request, "Booking request has been sucessfully submitted, you will be contacted (by e-mail) once it has been accepted.")

        return render(request, 'bookings/bookings.html')
    else:
        return render(request, 'bookings/bookings.html')


def equipment_booking_policy(request):
    return render(request, 'bookings/equipmentbooking.html')

def room_booking_policy(request):
    return render(request, 'bookings/roombooking.html')
