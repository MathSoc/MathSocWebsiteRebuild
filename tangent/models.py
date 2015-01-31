from django.db import models
from django.contrib.auth.models import User
import os


def upload_file_to(self, filename):
    return os.path.join(
        "documents", "{name}".format(name=self.name), filename)


def meeting_upload_file_path(self, filename, classification='unknown'):
    return os.path.join("{org_name}", classification,
                        "{number}-{date}".format(org_name=self.organization.name,
                                                 number=self.number,
                                                 date=self.date.isoformat()),
                        filename)


class Announcement(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User)
    author_position = models.ForeignKey('Position')
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
    positions = models.ManyToManyField('Position')

    # of variable relevancy depending on classification
    member_count = models.IntegerField()
    fee = models.IntegerField()
    office = models.CharField(max_length=32)

    website = models.URLField()
    documents = models.ManyToManyField('OrganizationDocument')


class OrganizationDocument(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    # TODO if document is .tex generate pdf
    file = models.FileField(upload_to=upload_file_to)


class Position(models.Model):
    title = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField()
    key_holder = models.BooleanField(default=False)
    has_key = models.BooleanField(default=False)

    occupied_by = models.ForeignKey(User)


class Scholarships(models.Model):
    name = models.CharField(max_length=256)
    organization = models.CharField(max_length=256)
    amount = models.IntegerField()
    description = models.TextField()
    website = models.URLField()


class Meeting(models.Model):
    organization = models.ForeignKey('Organization')
    number = models.IntegerField()
    date = models.DateField()
    term = models.CharField(choices=(
        ('W', 'Winter'),
        ('S', 'Spring'),
        ('F', 'Fall')
    ), max_length=2)
    general = models.BooleanField(default=False)

    agenda = models.FileField(upload_to=meeting_upload_file_path)
    minutes = models.FileField(upload_to=meeting_upload_file_path)
