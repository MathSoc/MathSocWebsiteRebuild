from django.db import models

class Exam(models.Model):
    name = models.CharField(max_length=256)
    course_number = models.IntegerField() # TODO error check and make sure this is a 3 digit number
    subject = models.CharField(max_length=10)
    semester = models.IntegerField() # TODO Error check and make sure this is a 4 digit integer

    file = models.FileField(upload_to='exams')

    def __str__(self):
        return self.name