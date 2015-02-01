# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import tangent.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('location', models.CharField(default=b'Comfy Lounge', max_length=256)),
                ('term', models.CharField(max_length=2, choices=[(b'W', b'Winter'), (b'S', b'Spring'), (b'F', b'Fall')])),
                ('general', models.BooleanField(default=False)),
                ('budget', models.BooleanField(default=False)),
                ('agenda', models.FileField(null=True, upload_to=tangent.models.meeting_upload_file_path, blank=True)),
                ('minutes', models.FileField(null=True, upload_to=tangent.models.meeting_upload_file_path, blank=True)),
                ('budget_file', models.FileField(null=True, upload_to=tangent.models.meeting_upload_file_path, blank=True)),
            ],
            options={
                'ordering': ['-date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('has_locker', models.BooleanField(default=False)),
                ('requested_refund', models.BooleanField(default=False)),
                ('is_volunteer', models.BooleanField(default=False)),
                ('bio', models.TextField(default=b'')),
                ('website', models.URLField(null=True, blank=True)),
                ('resume', models.FileField(upload_to=b'resumes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256)),
                ('description', models.TextField(default=b'', null=True, blank=True)),
                ('affiliations', models.CharField(max_length=256, null=True, blank=True)),
                ('classification', models.CharField(max_length=32, choices=[(b'Club', b'Club'), (b'Special Interest Coordinator', b'Special Interest Coordinator'), (b'Affiliate', b'Affiliate'), (b'Faculty', b'Faculty'), (b'External', b'External'), (b'Mathematics Society', b'Mathematics Society'), (b'MathSoc Council', b'MathSoc Council'), (b'MathSoc Office', b'MathSoc Office')])),
                ('member_count', models.IntegerField(default=0)),
                ('fee', models.IntegerField(default=0)),
                ('office', models.CharField(default=b'MC 3038', max_length=32)),
                ('website', models.URLField(default=b'http://mathsoc.uwaterloo.ca')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(default=b'')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('file', models.FileField(upload_to=tangent.models.upload_file_to)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('key_holder', models.BooleanField(default=False)),
                ('has_key', models.BooleanField(default=False)),
                ('occupied_by', models.ForeignKey(to='tangent.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('organization', models.CharField(max_length=256)),
                ('amount', models.IntegerField()),
                ('description', models.TextField(default=b'')),
                ('website', models.URLField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='organization',
            name='admin',
            field=models.ManyToManyField(related_name='admin', to='tangent.Position'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='documents',
            field=models.ManyToManyField(to='tangent.OrganizationDocument', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='meetings',
            field=models.ManyToManyField(to='tangent.Meeting', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='positions',
            field=models.ManyToManyField(related_name='position', to='tangent.Position'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='interested_in',
            field=models.ManyToManyField(to='tangent.Position'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='log',
            name='user',
            field=models.ForeignKey(to='tangent.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='announcement',
            name='author',
            field=models.ForeignKey(to='tangent.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='announcement',
            name='author_position',
            field=models.ForeignKey(to='tangent.Position'),
            preserve_default=True,
        ),
    ]
