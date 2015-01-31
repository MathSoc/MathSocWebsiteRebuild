from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=256)
    affiliations = models.CharField(max_length=256)
    positions = models.ManyToManyField(Position)


class Position(models.Model):
    title = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField()
    key_holder = models.BooleanField()

    current_holder = models.ForeignKey(User)

