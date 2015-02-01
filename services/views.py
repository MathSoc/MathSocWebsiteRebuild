from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from oauth2client.client import SignedJwtAssertionCredentials
from httplib2 import Http
from django.http import HttpResponse
from apiclient.discovery import build
import os
import json


# Create your views here.
def home(request):
    return render(request, 'services/index.html')


@login_required
def exambank(request):
    return render(request, 'services/exambank.html')


@login_required()
def lockers(request):
    user = request.user

    if request.method == 'POST':
        Locker.objects.filter()
        return home(request)  # TODO Change to a thank you/validate page

    else:  # not a post request
        return render(request, 'services/lockers.html')


@login_required()
def evaluations():
    return render(request, 'services/evaluations.html')


@login_required()
def bookings(request):
    if request.method == "POST":
        calendar_id = request.POST['calendar_id']
        client_email = '122929914589-ca1mb5s955gq0kg49khg6gqndj4v179p@developer.gserviceaccount.com'
        with open(os.path.join('services', 'google_keys', 'calendar_private_key.p12')) as f:
            private_key = f.read()
        credentials = SignedJwtAssertionCredentials(client_email, private_key,
                                                    'https://www.googleapis.com/auth/calendar')
        http_auth = credentials.authorize(Http())

        service = build('calendar', 'v3', http=http_auth)

        events = service.events().list(calendarId=calendar_id, pageToken=None, timeMax=str(request.POST['end']),
                                       timeMin=str(request.POST['start'])).execute()
        if (not events[u'items']):
            print "here now"
            event = {
                'summary': str(request.POST['eventname']) + " - " + str(request.POST['organisation']),
                'start': {
                    'dateTime': str(request.POST['start'])
                },
                'end': {
                    'dateTime': str(request.POST['end'])
                },
                'attendees': [
                    {
                        'email': str(request.POST.get('contactemail', 'mathsocbookings@gmail.com')),
                        'displayName': str(request.POST.get('contactname', 'N/A')),
                    }
                ],
            }
            created_event = service.events().insert(calendarId=calendar_id, body=event).execute()
            return HttpResponse(json.dumps({'result': True}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'result': False}), content_type='application/json')
    else:
        return render(request, 'services/bookings.html')
