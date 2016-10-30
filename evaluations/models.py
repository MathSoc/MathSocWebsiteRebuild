from django.db import models


class CourseEvaluation(models.Model):
    # TODO Parse course evaluations and store info for each prof
    semester = models.IntegerField() # TODO error check and make sure this is a 4 digit integer

    file = models.FileField(upload_to='course_evaluations')

    def __str__(self):
        return self.semester
