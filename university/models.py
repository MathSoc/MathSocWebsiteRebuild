from django.db import models
from django.contrib.auth.models import User
from tangent.models import Member

class Course(models.Model):
    subject = models.CharField(max_length=10)
    course_number = models.IntegerField() # three digit number
    description = models.TextField(blank=True, null=True)


class Professor(models.Model):
    user = models.OneToOneField(User) # allow profs to edit their own profile

    name = models.CharField(max_length=256)
    biography = models.TextField(blank=True, null=True)
    website = models.CharField(max_length=256)
    picture = models.ImageField(blank=True, null=True, upload_to='profile_pictures')

    previous_courses = models.ManyToManyField(Course, blank=True)


class Exam(models.Model):
    professor = models.ForeignKey(Professor)
    semester = models.IntegerField() # TODO Error check and make sure this is a 4 digit integer

    course = models.ForeignKey(Course)
    publically_available = models.BooleanField(default=False)

    file = models.FileField(upload_to='exams')

    def __str__(self):
        return self.name


class CourseEvaluation(models.Model):
    # TODO Parse course evaluations and store info for each prof
    semester = models.IntegerField() # TODO error check and make sure this is a 4 digit integer

    file = models.FileField(upload_to='course_evaluations')

    def __str__(self):
        return self.semester


class Comment(models.Model):
    author = models.ForeignKey(Member)
    anonymous = models.BooleanField(default=False)

    subject = models.CharField(max_length=256)
    body = models.TextField()

    topic_course = models.ForeignKey(Course)
    topic_prof = models.ForeignKey(Professor, null=True, blank=True)
    topic_exam = models.ForeignKey(Exam, null=True, blank=True)
