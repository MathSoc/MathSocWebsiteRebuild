from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import datetime
import os
import re
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


def get_time_from_string(request, timestr):
    start_time = re.split(' |:', timestr);

    hour = int(start_time[0])
    minutes = int(start_time[1])

    if hour < 1 or hour > 12 or minutes < 0 or minutes > 59:
        messages.error(request, "Invalid time given for start time")
        return render(request, 'services/bookings.html')

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
            return render(request, 'services/bookings.html')

        if request.POST['calendar_id'] not in calendar_ids:
            messages.error(request, "Invalid calendar selected")
            return render(request, 'services/bookings.html')

        if not re.match(r"\d{1,2}:\d\d [AP]M", request.POST['start-time']):
            messages.error(request, "Invalid format for starting time (correct example: 1:30 PM)")
            return render(request, 'services/bookings.html')

        if not re.match(r"\d{1,2}:\d\d [AP]M", request.POST['end-time']):
            messages.error(request, "Invalid format for end time (correct example: 1:30 PM)")
            return render(request, 'services/bookings.html')

        if not re.match(r"\d\d\d\d-\d\d-\d\d", request.POST['date']):
            messages.error(request, "Invalid date format (format is YYYY-MM-DD)")
            return render(request, 'services/bookings.html')

        if not request.POST['agreement'] == "on":
            messages.error(request, "Please agree to the Room and Equipment Booking Policy")
            return render(request, 'services/bookings.html')

        start = dateutil.parser.parse(request.POST['date'], yearfirst=True)
        start_time = get_time_from_string(request, request.POST['start-time'])

        start = datetime.datetime.combine(start.date(), start_time)

        now = datetime.datetime.now()
        if start < now:
            messages.error(request, "Please select a start time in the future")
            return render(request, 'services/bookings.html')

        end = dateutil.parser.parse(request.POST['date'], yearfirst=True)
        end_time = get_time_from_string(request, request.POST['end-time'])
        if end_time <= start_time:
            end += datetime.timedelta(days=1)

        end = datetime.datetime.combine(end.date(), end_time)

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

        return render(request, 'services/bookings.html')
    else:
        return render(request, 'services/bookings.html')


def equipment_booking_policy(request):
    return render(request, 'services/equipmentbooking.html')

def room_booking_policy(request):
    return render(request, 'services/roombooking.html')
