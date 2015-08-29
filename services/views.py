from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from oauth2client.client import SignedJwtAssertionCredentials
from httplib2 import Http
from django.http import HttpResponse
from apiclient.discovery import build
import os
import json
import dateutil.parser


# Create your views here.
from services.models import Locker, Exam, BookingRequest
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
    exams = list(Exam.objects.filter(subject=subject, course_number=code))

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
            ret = {'result': "Your locker has been reserved. You will receive an email "
                             "soon with details."}
        else:
            ret = {'result': "You already have a locker"}

        return HttpResponse(json.dumps(ret), content_type='application/json')

    else:  # not a post request
        lockers = True if Locker.objects.filter(owner=None) else False
        contect_dict = {'lockers': lockers}
        return render(request, 'services/lockers.html', contect_dict)


@login_required()
def evaluations(request):
    return render(request, 'services/evaluations.html')

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
                messages.error("Invalid entry for: " + type.replace("-", " ").title())
                invalid_input = True
                return False
            return True

        validate_input("contact-name")
        validate_input("contact-email")
        validate_input("organisation")
        validate_input("event-name")
        validate_input("contact-phone")

        if not invalid_input:
            return render(request, 'services/bookings.html')

        if request.POST['calendar_id'] not in calendar_ids:
            messages.error("Invalid calendar selected")
            return render(request, 'services/bookings.html')

        if not re.match(r"\d{1,2}:\d\d [AP]M", request.POST['start-time']):
            messages.error("Invalid format for starting time (correct example: 1:30 PM)")
            return render(request, 'services/bookings.html')

        if not re.match(r"\d{1,2}:\d\d [AP]M", request.POST['end-time']):
            messages.error("Invalid format for end time (correct example: 1:30 PM)")
            return render(request, 'services/bookings.html')

        if not re.match(r"\d\d\d\d-\d\d-\d\d", request.POST['start-time']):
            messages.error("Invalid date format (format is YYYY-MM-DD)")
            return render(request, 'services/bookings.html')

        # calendar_id = request.POST['calendar_id']
        # client_email = '122929914589-ca1mb5s955gq0kg49khg6gqndj4v179p@developer.gserviceaccount.com'
        # with open(os.path.join('services', 'google_keys', 'calendar_private_key.p12')) as f:
        #     private_key = f.read()
        # credentials = SignedJwtAssertionCredentials(client_email, private_key,
        #                                             'https://www.googleapis.com/auth/calendar')
        # http_auth = credentials.authorize(Http())

        # service = build('calendar', 'v3', http=http_auth)

        # events = service.events().list(calendarId=calendar_id, pageToken=None, timeMax=str(request.POST['end']),
        #                                timeMin=str(request.POST['start'])).execute()
        # if not events[u'items']:
        #     print "here now"
        #     event = {
        #         'summary': str(request.POST['eventname']) + " - " + str(request.POST['organisation']),
        #         'start': {
        #             'dateTime': str(request.POST['start'])
        #         },
        #         'end': {
        #             'dateTime': str(request.POST['end'])
        #         },
        #         'attendees': [
        #             {
        #                 'email': str(request.POST.get('contactemail', 'mathsocbookings@gmail.com')),
        #                 'displayName': str(request.POST.get('contactname', 'N/A')),
        #             }
        #         ],
        #     }
        #     created_event = service.events().insert(calendarId=calendar_id, body=event).execute()
        #     return HttpResponse(json.dumps({'result': True}), content_type='application/json')
        # else:
        #     return HttpResponse(json.dumps({'result': False}), content_type='application/json')
    else:
        return render(request, 'services/bookings.html')


def equipment_booking_policy(request):
    return render(request, 'services/equipmentbooking.html')

def room_booking_policy(request):
    return render(request, 'services/roombooking.html')