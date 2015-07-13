from django.db import models


class Faculty(models.Model):
    desc = models.TextField()

    def as_json(self):
        return {'id': self.pk,
                'desc': self.desc}


class Student(models.Model):
    quest_id = models.TextField(primary_key=True)
    faculty_id = models.ForeignKey(Faculty, related_name="student_faculty")
    term = models.CharField(max_length=2)

    def as_json(self):
        return {'quest_id': self.quest_id,
                'faculty': Faculty.objects.filter(pk=self.faculty_id)[0].as_json(),
                'term': self.term}