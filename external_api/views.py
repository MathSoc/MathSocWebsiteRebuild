from django.http import HttpResponse
from external_api.models import Faculty, Student
from django.shortcuts import render
import json


def students(request):
    if request.method == "POST":
        if 'student' in request.POST:
            info = request.POST['student']
        else:
            return HttpResponse(json.dumps({
                                'error': "Improper format"}),
                                content_type='application/json')

        if (not 'quest_id' in info) or \
           (not 'faculty_id' in info) or (not 'term' in info):
            return HttpResponse(json.dumps({
                                'error': "Missing at least one parameter"}),
                                content_type='application/json')

        if Student.objects.filter(quest_id=info['quest_id']):
            return HttpResponse(json.dumps({
                                'error': "Quest id already present in system"}),
                                content_type='application/json')
        if not (Faculty.objects.filter(faculty_id=info['faculty_id'])):
            return HttpResponse(json.dumps({
                                'error': "Specified faculty not in system"}),
                                content_type='application/json')
        else:
            new_student = Student(quest_id=info['quest_id'],
                                  faculty_id=info['faculty_id'],
                                  term = info['term'])
            new_student.save()
            return HttpResponse(json.dumps({'success': "Student added to the school"}),
                                content_type='application/json')
    if request.method == "GET":
        return HttpResponse(json.dumps({'students': [student.as_json() for student in Student.objects.all()]}),
                            content_type='application/json')
    if request.method == "DELETE":
        Student.objects.all().delete()
        return HttpResponse(json.dumps({'success': "All students deleted"}),
                            content_type='application/json')


def student(request, quest_id):
    if request.method == "GET":
        response = Student.objects.filter(quest_id=quest_id)
        if response:
            return HttpResponse(json.dumps({'student': response[0].as_json()}),
                                content_type='application/json')
        else:
            return HttpResponse(json.dumps({'error': "student not found"}),
                                content_type='application/json')

def faculties(request):
    if request.method == "POST":
        print request.POST
        if 'faculty' not in request.POST:
            return HttpResponse(json.dumps({
                                'error': "Improper format"}),
                                content_type='application/json')
        info = request.POST['faculty']
        if 'desc' not in info:
            return HttpResponse(json.dumps({'error': "Missing description"}),
                                content_type='application/json')
        if Faculty.objects.filter(desc=info['desc']):
            return HttpResponse(json.dumps({'error': "A faculty with that description already exists"}),
                                content_type='application/json')
        else:
            print "MADE IT!"
            new_faculty = Faculty(desc=info['desc'])
            new_faculty.save()
            return HttpResponse(json.dumps({'success': "Faculty added to the school"}),
                                content_type='application/json')
    if request.method == "GET":
        return HttpResponse(json.dumps({'faculties': [faculty.as_json() for faculty in Faculty.objects.all()]}),
                            content_type='application/json')
    if request.method == "DELETE":
        Faculty.objects.all().delete()
        return HttpResponse(json.dumps({'success': "All faculties deleted"}),
                            content_type='application/json')


def faculty(request, faculty_id):
    if request.method == "GET":
        response = Faculty.objects.filter(pk=faculty_id)
        if response:
            return HttpResponse(json.dumps({'student': response[0].as_json()}),
                                content_type='application/json')
        else:
            return HttpResponse(json.dumps({'error': "faculty not found"}),
                                content_type='application/json')


def interface(request):
    return render(request, 'external_api/interface.html')