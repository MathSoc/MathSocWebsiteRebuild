from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from oat.helpers import is_society_member
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


class Member(models.Model):
    user = models.OneToOneField(User)

    #Services
    requested_refund = models.BooleanField(default=False)
    used_resources = models.BooleanField(default=False)

    # information about the member
    bio = models.TextField(default="", blank=True, null=True)
    picture = models.ImageField(blank=True, null=True, upload_to='profile_pictures')
    website = models.URLField(blank=True, null=True)

    # Will indicate interest for the current term, which will forward resume and cover letter
    interested_in = models.ManyToManyField('Position', blank=True)

    # for applications, and also so they have a place to host this stuff
    resume = models.FileField(upload_to='resumes', blank=True, null=True)
    cover_letter = models.TextField(default="", blank=True, null=True)

    def __str__(self):
        return self.user.username

    def is_society_member(self):
        return is_society_member(self.user.username)

    def can_post(self):
        return self.position_set.filter(
            can_post=True
        )

    def can_edit(self):
        return self.position_set.filter(
            can_edit=True
        )

    def is_org_admin(self, org):
        for position in org.position_set.filter(is_admin=True):
            if position.occupied_by.filter(id=self.id):
                return True
        return self.user.is_staff

def create_member(sender, instance, created, **kwargs):
    if created:
       member, created = Member.objects.get_or_create(user=instance)

post_save.connect(create_member, sender=User)

class Announcement(models.Model):
    # determines what order posts appear on the page
    # TODO order 0 means the header
    order_key = models.IntegerField(unique=True)
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Member)
    author_position = models.ForeignKey('Position')
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    # a link that will be used if people want more information or to act
    # TODO implement
    action = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Organization(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(default="", blank=True, null=True)
    affiliations = models.CharField(max_length=256, blank=True, null=True)
    classification = models.CharField(choices=(
        ('CLUB', 'Club'),
        ('SIC', 'Special Interest Coordinator'),
        ('AFFL', 'Affiliate'),
        ('FACL', 'Faculty'),
        ('EXTL', 'External'),
        ('MATH_MISC', 'Mathematics Society'),
        ('MATH_GOV', 'MathSoc Governance'),
        ('COMM', 'MathSoc Committee')
    ), max_length=32)

    members = models.ManyToManyField('Member', blank=True)
    fee = models.IntegerField(default=0)
    office = models.CharField(max_length=32, default="MC 3038")
    website = models.URLField(default='http://mathsoc.uwaterloo.ca')

    def __str__(self):
        return self.name


class OrganizationDocument(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(default="")
    date_added = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    organization = models.ForeignKey('Organization', default=None)

    # TODO if document is .tex generate pdf
    file = models.FileField(upload_to=upload_file_to)

    def __str__(self):
        return self.name


class Position(models.Model):
    title = models.CharField(max_length=256)
    responsibilities = models.TextField(blank=True, null=True)
    is_admin = models.BooleanField(default=False) # Can do anything (overrides all other permissions, only admins can manage members, organization info, etc)
    can_post = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False) # People who can post can only edit their own posts, these people can edit all announcements
    can_manage_bookings = models.BooleanField(default=False)
    can_create_meetings =  models.BooleanField(default=False)
    can_add_files_to_meetings = models.BooleanField(default=False)
    organization = models.ForeignKey('Organization', default=None)
    want_applications = models.BooleanField(default=False)

    key_holder = models.BooleanField(default=False)

    occupied_by = models.ManyToManyField(Member, blank=True, default=None)

    def __str__(self):
        return self.title + " - " + self.organization.name

    def members_list(self):
        members = self.occupied_by.all()
        if members:
            return self.title + ": " + \
                ', '.join([str(member) for member in members])
        return self.title + ": Vacant"



class Scholarship(models.Model):
    name = models.CharField(max_length=256)
    organization = models.CharField(max_length=256)
    #TODO amount should maybe be a char field for ranges
    amount = models.IntegerField()
    description = models.TextField(default="")
    website = models.URLField(default="")

    def __str__(self):
        return self.name


class Meeting(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=256, default="Comfy Lounge")
    organization = models.ForeignKey('Organization')
    term = models.CharField(choices=(
        ('W', 'Winter'),
        ('S', 'Spring'),
        ('F', 'Fall')
    ), max_length=2)
    general = models.BooleanField(default=False)
    budget = models.BooleanField(default=False)

    agenda = models.FileField(upload_to=meeting_upload_file_path, blank=True, null=True)
    minutes = models.FileField(upload_to=meeting_upload_file_path, blank=True, null=True)
    budget_file = models.FileField(upload_to=meeting_upload_file_path, blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.date.isoformat()


# TODO This may be unnecessary... However it makes me think of something else
class Log(models.Model):
    title = models.CharField(max_length=128)
    datetime = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    user = models.ForeignKey(Member)

    def __str__(self):
        return self.title
