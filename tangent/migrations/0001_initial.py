# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tangent.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('order_key', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=256)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='', blank=True)),
                ('action', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('location', models.CharField(default='Comfy Lounge', max_length=256)),
                ('term', models.CharField(choices=[('W', 'Winter'), ('S', 'Spring'), ('F', 'Fall')], max_length=2)),
                ('general', models.BooleanField(default=False)),
                ('budget', models.BooleanField(default=False)),
                ('agenda', models.FileField(null=True, upload_to=tangent.models.meeting_upload_file_path, blank=True)),
                ('minutes', models.FileField(null=True, upload_to=tangent.models.meeting_upload_file_path, blank=True)),
                ('budget_file', models.FileField(null=True, upload_to=tangent.models.meeting_upload_file_path, blank=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('requested_refund', models.BooleanField(default=False)),
                ('used_resources', models.BooleanField(default=False)),
                ('bio', models.TextField(null=True, default='', blank=True)),
                ('picture', models.ImageField(null=True, upload_to='profile_pictures', blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('resume', models.FileField(null=True, upload_to='resumes', blank=True)),
                ('cover_letter', models.TextField(null=True, default='', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256)),
                ('description', models.TextField(null=True, default='', blank=True)),
                ('affiliations', models.CharField(null=True, max_length=256, blank=True)),
                ('classification', models.CharField(choices=[('CLUB', 'Club'), ('SIC', 'Special Interest Coordinator'), ('AFFL', 'Affiliate'), ('FACL', 'Faculty'), ('EXTL', 'External'), ('MATH_MISC', 'Mathematics Society'), ('MATH_GOV', 'MathSoc Governance'), ('COMM', 'MathSoc Committee')], max_length=32)),
                ('fee', models.IntegerField(default=0)),
                ('office', models.CharField(default='MC 3038', max_length=32)),
                ('website', models.URLField(default='http://mathsoc.uwaterloo.ca')),
                ('members', models.ManyToManyField(to='tangent.Member', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationDocument',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(default='')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('file', models.FileField(upload_to=tangent.models.upload_file_to)),
                ('organization', models.ForeignKey(default=None, to='tangent.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('responsibilities', models.TextField(null=True, blank=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('can_post', models.BooleanField(default=False)),
                ('can_edit', models.BooleanField(default=False)),
                ('can_manage_bookings', models.BooleanField(default=False)),
                ('can_create_meetings', models.BooleanField(default=False)),
                ('can_add_files_to_meetings', models.BooleanField(default=False)),
                ('want_applications', models.BooleanField(default=False)),
                ('key_holder', models.BooleanField(default=False)),
                ('occupied_by', models.ManyToManyField(to='tangent.Member', default=None, blank=True)),
                ('organization', models.ForeignKey(default=None, to='tangent.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('organization', models.CharField(max_length=256)),
                ('amount', models.IntegerField()),
                ('description', models.TextField(default='')),
                ('website', models.URLField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='interested_in',
            field=models.ManyToManyField(to='tangent.Position', blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meeting',
            name='organization',
            field=models.ForeignKey(to='tangent.Organization'),
        ),
        migrations.AddField(
            model_name='log',
            name='user',
            field=models.ForeignKey(to='tangent.Member'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='author',
            field=models.ForeignKey(to='tangent.Member'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='author_position',
            field=models.ForeignKey(to='tangent.Position'),
        ),
    ]
