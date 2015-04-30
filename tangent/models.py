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


class Member(models.Model):
    user = models.OneToOneField(User)

    #Services
    has_locker = models.BooleanField(default=False)  # redundant, repeated on Locker model (foreign key)
    requested_refund = models.BooleanField(default=False)
    used_resources = models.BooleanField(default=False)

    # information about the member
    bio = models.TextField(default="", blank=True, null=True)
    picture = models.ImageField(blank=True, null=True, upload_to='profile_pictures')
    website = models.URLField(blank=True, null=True)
    # the position title can be found by looking at the name on positions
    is_volunteer = models.BooleanField(default=False)  # slightly redundant

    # Will indicate interest for the current term, which will forward resume and cover letter
    interested_in = models.ManyToManyField('Position', blank=True, null=True)

    # for applications, and also so they have a place to host this stuff
    resume = models.FileField(upload_to='resumes', blank=True, null=True)
    cover_letter = models.TextField(default="", blank=True, null=True)

    def __unicode__(self):
        return self.user.username


class Announcement(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Member)
    author_position = models.ForeignKey('Position')
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return self.title


class Organization(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(default="", blank=True, null=True)
    affiliations = models.CharField(max_length=256, blank=True, null=True)
    classification = models.CharField(choices=(
        ('Club', 'Club'),
        ('Special Interest Coordinator', 'Special Interest Coordinator'),
        ('Affiliate', 'Affiliate'),
        ('Faculty', 'Faculty'),
        ('External', 'External'),
        ('Mathematics Society', 'Mathematics Society'),
        ('MathSoc Council', 'MathSoc Council')
    ), max_length=32)

    # of variable relevancy depending on classification
    #TODO this should maybe be a list of members
    member_count = models.IntegerField(default=0)
    fee = models.IntegerField(default=0)
    office = models.CharField(max_length=32, default="MC 3038")
    website = models.URLField(default='http://mathsoc.uwaterloo.ca')
    documents = models.ManyToManyField('OrganizationDocument', blank=True, null=True)

    def __unicode__(self):
        return self.name


class OrganizationDocument(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(default="")
    date_added = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    # TODO if document is .tex generate pdf
    file = models.FileField(upload_to=upload_file_to)

    def __unicode__(self):
        return self.name


class Position(models.Model):
    title = models.CharField(max_length=256)
    responsibilities = models.TextField(blank=True, null=True)
    organization = models.ForeignKey('Organization')
    is_admin = models.BooleanField(default=False)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    key_holder = models.BooleanField(default=False)
    has_key = models.BooleanField(default=False)

    occupied_by = models.ForeignKey(Member, blank=True, null=True)

    def __unicode__(self):
        return self.title


class Scholarship(models.Model):
    name = models.CharField(max_length=256)
    organization = models.CharField(max_length=256)
    #TODO amount should maybe be a char field for ranges
    amount = models.IntegerField()
    description = models.TextField(default="")
    website = models.URLField(default="")

    def __unicode__(self):
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

    def __unicode__(self):
        return self.date.isoformat()


# TODO This may be unnecessary... However it makes me think of something else
class Log(models.Model):
    title = models.CharField(max_length=128)
    datetime = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    user = models.ForeignKey(Member)

    def __unicode__(self):
        return self.title
