from __future__ import unicode_literals
import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from university.models import Exam


@login_required()
def evaluations(request):
    return render(request, 'evaluations/evaluations.html')

# @login_required()
def exambank(request):
    return render(request, 'exambank/exambank.html')


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
    ret = [{'code': code, 'courses': list(set(courses))} for (code, courses) in exam_aggr.items()]

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
