from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from tangent.models import Organization, Position
from services.models import BookingRequest
from oauth2client import tools
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
from django.core.urlresolvers import reverse
from httplib2 import Http
from io import open
import datetime
import logging
import sys
import os

logger = logging.getLogger(__name__)

# ---------- HELPERS -------------

def email_booking(booking, was_accepted):
    with open(os.path.join('tangent', 'templates', 'mail', 'booking_status.txt')) as f:
        mail_template = f.read()

    past_verb = "accepted"
    if not was_accepted:
        past_verb = "rejected"
    date_time_range = booking.start.strftime("%b %d %Y, %I:%M %p - ") + booking.end.strftime("%I:%M %p")
    try:
        send_mail(
            "MathSoc: Your Booking Request has been {status}".format(
                status=past_verb
            ),
            mail_template.format(
                contact_name=booking.contact_name,
                event_name=booking.event_name,
                date_time_range=date_time_range,
                status=past_verb
            ),
            from_email="mathsocbookings@gmail.com",
            recipient_list=[booking.contact_email],
            fail_silently=False
        )
        logger.info("EMAIL SUCCESSFULLY SENT")
    except Exception as e:
        logger.error("EMAIL SENT UNSUCCESSFULLY, error: {}".format(e))

def add_to_calendar(booking):
    # Certificate Fingerprint: 8634ef128fc6289f0e961aede36ad69498b515a8
    client_email = '122929914589-8rdj6ad0k11ts3av26jb7u9jhe06i13f@developer.gserviceaccount.com'
    credentials = ServiceAccountCredentials.from_p12_keyfile(
        client_email,
        'keys_and_pws/bookings_calendar_cert.p12',
        scopes=['https://www.googleapis.com/auth/calendar']
    )

    http_auth = credentials.authorize(Http())

    service = build('calendar', 'v3', http=http_auth)

    events = service.events().list(
        calendarId=booking.calendar_id,
        timeMin=booking.start.strftime("%Y-%m-%dT%H:%M:00-04:00"),
        timeMax=booking.end.strftime("%Y-%m-%dT%H:%M:00-04:00")
    ).execute()

    if not events[u'items']:
        try:
            event = {
                'summary': booking.event_name + " - " + booking.organisation,
                'start': {
                    'dateTime': booking.start.strftime("%Y-%m-%dT%H:%M:00"),
                    'timeZone': "America/Toronto"
                },
                'end': {
                    'dateTime': booking.end.strftime("%Y-%m-%dT%H:%M:00"),
                    'timeZone': "America/Toronto"
                },
                'attendees': [
                    {
                        'email': booking.contact_email,
                        'displayName': booking.contact_name,
                    }
                ],
            }
            created_event = service.events().insert(calendarId=booking.calendar_id, body=event).execute()
            return None
        except Exception as e:
            logger.error("Could not insert calendar event: {}".format(e))
            return "Received an error from the Google Calendar API when trying to add event"
    else:
        return "Event overlaps with another"

# Decorator that determines if a logged_in user is a site admin.
def is_staff(view_func):
    def inner(request, *args, **kwargs):
        if not request.user or not request.user.is_staff:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return inner

# --------- VIEW FUNCTIONS -------------------

@login_required
def home(request):
    user = request.user
    if not user.is_staff:
        organizations = Position.objects.filter(
            occupied_by = user.member
        ).select_related('organization')
    else:
        organizations = Organization.objects.all()
    can_post = user.is_staff or user.member.can_post()
    context_dict = {'organizations': organizations, 'can_post': can_post}
    return render(request, 'tangent/index.html', context_dict)


def organization(request, org_id):
    user = None
    org = Organization.objects.get(id=org_id)
    is_org_admin = request.user and request.user.member.is_org_admin(org)
    context_dict = {
        'org' : org,
        'is_org_admin': is_org_admin
    }
    return render(request,
                  'tangent/organization.html',
                  context_dict)

@login_required
def log(request):
    return render(request, 'tangent/log.html')

@login_required
def profile(request):
    return render(request, 'tangent/index.html')

@login_required
def help(request):
    return render(request, 'tangent/index.html')

@login_required
@is_staff
def website(request):
    return render(request, 'tangent/index.html')

@login_required
def bookings(request, show_all=False):
    if not show_all:
        requests = BookingRequest.objects.filter(
            end__gte=datetime.datetime.today()
        ).order_by('status', 'start')
    else:
        requests = BookingRequest.objects.order_by('-start')
    return render(request, 'tangent/bookings.html', {'requests': requests})

@login_required
def booking(request, booking_id):
    booking = get_object_or_404(BookingRequest, id=booking_id)
    return render(request, 'tangent/booking.html', {'booking': booking})

@login_required
@require_POST
def reject_booking(request, booking_id):
    booking = get_object_or_404(BookingRequest, id=booking_id)
    if booking.status != BookingRequest.REQUESTED_STATUS:
        return HttpResponseBadRequest("Can only reject bookings that are in the requested state")
    booking.status = BookingRequest.REJECTED_STATUS
    booking.save()
    email_booking(booking, was_accepted=False)
    messages.success(request, "Booking was sucessfully rejected")
    return HttpResponseRedirect(reverse('tangent_bookings'))

@login_required
@require_POST
def accept_booking(request, booking_id):
    booking = get_object_or_404(BookingRequest, id=booking_id)
    if booking.status != BookingRequest.REQUESTED_STATUS:
        return HttpResponseBadRequest("Can only accept bookings that are in the requested state")
    result = add_to_calendar(booking)
    if not result:
        booking.status = BookingRequest.ACCEPTED_STATUS
        booking.save()
        email_booking(booking, was_accepted=True)
        messages.success(
            request,
            "Booking was sucessfully accepted, it should now appear in the appropriate calendar"
        )
    else:
        messages.error(request, "Booking did not succeed, " + result)
    return HttpResponseRedirect(reverse('tangent_bookings'))
