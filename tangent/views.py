from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from tangent.models import BaseOrg, Club, Member, Organization, Position, PositionHolder
from tangent.forms import AddMembersForm
from bookings.models import BookingRequest
from oauth2client import tools
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
from django.core.urlresolvers import reverse
from httplib2 import Http
from io import open
from guardian.core import ObjectPermissionChecker
from itertools import chain
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
        timeMin=booking.start.isoformat(),
        timeMax=booking.end.isoformat()
    ).execute()
    logger.info("{}".format(events))

    if not events[u'items']:
        try:
            event = {
                'summary': booking.event_name + " - " + booking.organisation,
                'start': {
                    'dateTime': booking.start.strftime("%Y-%m-%dT%H:%M:00"),
                    'timeZone': booking.start.tzinfo._tzname
                },
                'end': {
                    'dateTime': booking.end.strftime("%Y-%m-%dT%H:%M:00"),
                    'timeZone': booking.end.tzinfo._tzname
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


# Decorator that verifies if a logged_in user is an organization's admin
# and provides the view_function in question with that org
def org_admin_interface(cls, perm):
    def decorator(view_func):
        def inner(request, org_id, *args, **kwargs):
            org = get_object_or_404(cls, id=org_id)
            has_perm = request.user and request.user.has_perm(perm, org)
            if not has_perm:
                raise PermissionDenied
            return view_func(request, org, *args, **kwargs)
        return inner
    return decorator

# --------- VIEW FUNCTIONS -------------------

@login_required
def home(request):
    user = request.user
    clubs = Club.objects.all()
    orgs = Organization.objects.all()
    checker = ObjectPermissionChecker(user)
    checker.prefetch_perms(orgs)
    post_orgs = []
    membership_orgs = []
    post_clubs = []
    membership_clubs = []
    for org in orgs:
        if checker.has_perm('add_announcements', org):
            post_orgs.append(org)
        if checker.has_perm('attach_positions', org):
            membership_orgs.append(org)
    for club in clubs:
        if checker.has_perm('add_announcements', club):
            post_clubs.append(club)
        if checker.has_perm('attach_positions', club):
            membership_clubs.append(club)
    context_dict = {
        'post_orgs': post_orgs, 
        'membership_orgs': membership_orgs,
        'post_clubs': post_clubs,
        'membership_clubs': membership_clubs
    }
    return render(request, 'tangent/index.html', context_dict)

def render_members(request, org, is_club):
    positions = org.position_set.all()
    position_holders = PositionHolder.get_position_and_holders_list(positions)
    return render(
        request,
        'tangent/org_members.html',
        {
            'is_club': is_club,
            'org': org,
            'position_holders': position_holders,
            'add_members_form': AddMembersForm()
        }
    )

@login_required
@org_admin_interface(Organization, perm='attach_positions')
def org_members(request, org):
    return render_members(request, org, is_club=False)

@login_required
@org_admin_interface(Club, perm='attach_positions')
def club_members(request, club):
    if request.method == "POST":
        return add_club_members(request, club)
    return render_members(request, club, is_club=True)

def add_club_members(request, club):
    old_count = club.members.count()
    members = []
    if request.POST['add_member_list']:
        watids = request.POST['add_member_list'].split()
        for watid in watids:
            member, created = Member.objects.get_or_create_from_username(watid)
            members.append(member)
        club.members.add(*members)
        messages.success(
            request,
            "{} members have been added.".format(club.members.count() - old_count)
        )
    return redirect('tangent_club_members', club.id) 

def attach_positions(request, org):    
    if request.POST['position_title'] and request.POST['attach_positions_list']:
        position = org.position_set.get(
            title=request.POST['position_title']
        )
        watids = request.POST['attach_positions_list'].split()
        for watid in watids:
            member, created = Member.objects.get_or_create_from_username(watid)
            ph = PositionHolder.objects.get_or_create(
                term=settings.CURRENT_TERM, position=position, occupied_by=member
            )
        messages.success(
            request,
            "Positions have been attached to the users for the current term."
        )

@login_required
@require_POST
@org_admin_interface(Club, perm='attach_positions')
def club_attach_positions(request, club):
    attach_positions(request, club)
    return redirect('tangent_club_members', club.id)

@login_required
@require_POST
@org_admin_interface(Organization, perm='attach_positions')
def org_attach_positions(request, org):
    attach_positions(request, org)
    return redirect('tangent_org_members', org.id)

@login_required
@org_admin_interface(Club, perm='attach_positions')
def club_society_members(request, club):
    count = 0
    for member in club.members.all():
        if member.is_society_member():
            count += 1
    return HttpResponse(count)

def render_announcements(request, org, is_club):
    can_post = request.user.has_perm('add_announcements', org)
    can_manage = request.user.has_perm('manage_announcement', org)
    can_promote = request.user.has_perm('can_promote')
    return render(
        request, 
        'tangent/announcements.html', 
        {
            'is_club': is_club,
            'can_post': can_post,
            'can_manage': can_manage,
            'can_promote': can_promote,
            'org': org
        }
    )

@login_required
@org_admin_interface(Organization, perm='add_announcements')
def org_announcements(request, org):
    return render_announcements(request, org, is_club=False)

@login_required
@org_admin_interface(Club, perm='add_announcements')
def club_announcements(request, club):
    return render_announcements(request, club, is_club=True)

@login_required
def profile(request):
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
    print(booking.start)
    print(booking.end)
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
