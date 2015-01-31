from django.db import models
from django.contrib.auth.models import User


# Create your models here.
import os


class Announcement(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User)
    author_position = models.ForeignKey(Position)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField()


class Organization(models.Model):
    name = models.CharField(max_length=256)
    affiliations = models.CharField(max_length=256)
    classification = models.CharField(choices=(
        ('CLUB', 'Club'),
        ('SIC', 'Special Interest Coordinator'),
        ('AFF', 'Affiliate'),
        ('SCOM', 'Standing Committee'),
        ('TCOM', 'Temporary Committee'),
        ('ECOM', 'External Committee'),
        ('MATHSOC', 'Mathematics Society'),
        ('COUNCIL', 'MathSoc Council'),
        ('OFFICE', 'MathSoc Office')
    ), max_length=8)
    positions = models.ManyToManyField(Position)

    # of variable relevancy depending on classification
    member_count = models.IntegerField()
    fee = models.IntegerField()
    office = models.CharField(max_length=32)

    website = models.URLField()
    documents = models.ManyToManyField(OrganizationDocument)


class OrganizationDocument(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    # TODO if document is .tex generate pdf
    file = models.FileField(upload_to=organization_upload_file_to)


def organization_upload_file_to(instance, filename):
    return os.path.join(
        "documents", "{name}".format(name=instance.name), filename)


class Position(models.Model):
    title = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField()
    key_holder = models.BooleanField()
    has_key = models.BooleanField()

    occupied_by = models.ForeignKey(User)


class Scholarships(models.Model):
    name = models.CharField(max_length=256)
    organization = models.CharField(max_length=256)
    amount = models.IntegerField()
    description = models.TextField()
    website = models.URLField()


class Meeting(models.Model):
    organization = models.ForeignKey(Organization)
    number = models.IntegerField()
    date = models.DateField()
    term = models.CharField(choices=(
        ('W', 'Winter'),
        ('S', 'Spring'),
        ('F', 'Fall')
    ))
    general = models.BooleanField(default=False)

    agenda = models.FileField(upload_to=meeting_upload_file_path(classification='agenda'))
    minutes = models.FileField(upload_to=meeting_upload_file_path(classification='minutes'))


def meeting_upload_file_path(classification='unknown'):
    return lambda instance, filename: \
        os.path.join(
            "{org_name}", classification, "{number}-{date}").format(org_name=instance.organization.name,
                                                                    number=instance.number,
                                                                    date=instance.date.isoformat())