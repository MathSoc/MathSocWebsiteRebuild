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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('order_key', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=256)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='', null=True, blank=True)),
                ('action', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BaseOrg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=256)),
                ('description', models.TextField(null=True, blank=True, default='')),
                ('office', models.CharField(max_length=32, default='MC 3038')),
                ('website', models.URLField(default='http://mathsoc.uwaterloo.ca')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=256, default='Comfy Lounge')),
                ('term', models.CharField(choices=[('W', 'Winter'), ('S', 'Spring'), ('F', 'Fall')], max_length=2)),
                ('general', models.BooleanField(default=False)),
                ('budget', models.BooleanField(default=False)),
                ('agenda', models.FileField(upload_to=tangent.models.meeting_upload_file_path, null=True, blank=True)),
                ('minutes', models.FileField(upload_to=tangent.models.meeting_upload_file_path, null=True, blank=True)),
                ('budget_file', models.FileField(upload_to=tangent.models.meeting_upload_file_path, null=True, blank=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('requested_refund', models.BooleanField(default=False)),
                ('used_resources', models.BooleanField(default=False)),
                ('do_not_email', models.BooleanField(default=False)),
                ('bio', models.TextField(null=True, blank=True, default='')),
                ('picture', models.ImageField(upload_to='profile_pictures', null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('resume', models.FileField(upload_to='resumes', null=True, blank=True)),
                ('cover_letter', models.TextField(null=True, blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(default='')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('file', models.FileField(upload_to=tangent.models.upload_file_to)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('responsibilities', models.TextField(null=True, blank=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('can_post', models.BooleanField(default=False)),
                ('can_edit', models.BooleanField(default=False)),
                ('can_manage_bookings', models.BooleanField(default=False)),
                ('can_create_meetings', models.BooleanField(default=False)),
                ('can_add_files_to_meetings', models.BooleanField(default=False)),
                ('key_holder', models.BooleanField(default=False)),
                ('want_applications', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PositionHolder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('term', models.IntegerField(default='1169')),
                ('occupied_by', models.ForeignKey(to='tangent.Member')),
                ('position', models.ForeignKey(to='tangent.Position')),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('organization', models.CharField(max_length=256)),
                ('amount', models.IntegerField()),
                ('description', models.TextField(default='')),
                ('website', models.URLField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('baseorg_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, auto_created=True, to='tangent.BaseOrg')),
                ('fee', models.IntegerField(default=200)),
            ],
            bases=('tangent.baseorg',),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('baseorg_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, auto_created=True, to='tangent.BaseOrg')),
                ('external', models.BooleanField(default=False)),
                ('affiliate', models.BooleanField(default=False)),
                ('sponsor', models.BooleanField(default=False)),
            ],
            bases=('tangent.baseorg',),
        ),
        migrations.AddField(
            model_name='position',
            name='primary_organization',
            field=models.ForeignKey(to='tangent.BaseOrg', null=True, default=None, blank=True),
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
            name='attendance',
            field=models.ManyToManyField(to='tangent.Member', blank=True),
        ),
        migrations.AddField(
            model_name='log',
            name='user',
            field=models.ForeignKey(to='tangent.Member'),
        ),
        migrations.AddField(
            model_name='baseorg',
            name='documents',
            field=models.ManyToManyField(to='tangent.OrganizationDocument', blank=True, default=None),
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
        migrations.AddField(
            model_name='meeting',
            name='organization',
            field=models.ForeignKey(to='tangent.Organization'),
        ),
        migrations.AddField(
            model_name='club',
            name='members',
            field=models.ManyToManyField(to='tangent.Member', blank=True),
        ),
    ]
