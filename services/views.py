from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from oauth2client.client import SignedJwtAssertionCredentials
from httplib2 import Http
from django.http import HttpResponse
from apiclient.discovery import build
import os
import json


# Create your views here.
from services.models import Locker, Exam
from tangent.models import Member


def home(request):
    return render(request, 'services/index.html')


# @login_required()
def exambank(request):
    return render(request, 'services/exambank.html')


def get_courses(request):
    """
    @summary: Gets a list of all courses aggregated by subject code

    @returns:
        [{'code': SUBJECT_CODE,
          'courses': [COURSE_NUMBER, ...]},
          ...]
    """
    exam_aggr = {}
    exams = Exam.objects.all()
    for exam in exams:
        if exam.subject not in exam_aggr:
            exam_aggr[exam.subject] = []
        exam_aggr[exam.subject].append(exam.course_number)

    # note:
    # list(set(arr)) removes duplicate entries in a list
    ret = [{'code': code, 'courses': list(set(courses))} for (code, courses) in exam_aggr.iteritems()]

    response = HttpResponse(json.dumps(ret), content_type='application/json')
    return response


def get_exams(request):
    """
    @summary: Gets a list of all exams for a single course

    @args:
        subject [String]: of the course
        code [Integer]: of the course

    @returns:
        [ {'name': EXAM_NAME,
           'semester': SEMESTER}
          ...]
    """
    subject = request.GET['subject']
    code = int(request.GET['course'])
    exams = Exam.objects.get(subject=subject, course_number=code)

    if not isinstance(exams, list):
        exams = [exams]
    ret = [{'name': exam.name, 'semester': exam.semester} for exam in exams]

    response = HttpResponse(json.dumps(ret), content_type='application/json')
    return response


def get_exam(request, subject, course):
    """
    @summary: Serve the file for an exam

    @args:
        subject [String]: of the course of the exam
        code [Integer]: of the course of the exam
        semester [Integer]: of the exam

    @returns:
        the exam PDF {Binary Data}
        attachment; => saves automatically
    """
    code = int(course)
    name = request.GET['name']
    exam = Exam.objects.get(subject=subject, course_number=code, name=name)

    response = HttpResponse(exam.file, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="{0}_{0}_{0}.pdf"'.format(subject, code, name)
    response['Content-Disposition'] = 'filename="{0}_{0}_{0}.pdf"'.format(subject, code, name)
    return response


@login_required()
def lockers(request):
    # get_or_create returns a tuple (object, created) where created
    #   is a boolean
    member = Member.objects.get_or_create(user=request.user)[0]

    if request.method == 'POST':
        # Return JSON object which will be parsed
        if not member.has_locker:
            # give them a locker
            locker = Locker.objects.filter(owner=None)[0]
            locker.owner = member
            member.has_locker = True
            member.used_resources = True
            locker.save()
            member.save()
            ret = {'result': "Your locker has been reserved. You will recieve an email "
                             "soon with details."}
        else:
            ret = {'result': "You already have a locker"}

        return HttpResponse(json.dumps(ret), content_type='application/json')

    else:  # not a post request
        return render(request, 'services/lockers.html')


@login_required()
def evaluations(request):
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
        if not events[u'items']:
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
