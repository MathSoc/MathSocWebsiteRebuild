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
                ('image', models.ImageField(upload_to=b'')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('date', models.DateField()),
                ('term', models.CharField(max_length=2, choices=[(b'W', b'Winter'), (b'S', b'Spring'), (b'F', b'Fall')])),
                ('general', models.BooleanField(default=False)),
                ('agenda', models.FileField(upload_to=tangent.models.meeting_upload_file_path)),
                ('minutes', models.FileField(upload_to=tangent.models.meeting_upload_file_path)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('affiliations', models.CharField(max_length=256)),
                ('classification', models.CharField(max_length=8, choices=[(b'CLUB', b'Club'), (b'SIC', b'Special Interest Coordinator'), (b'AFF', b'Affiliate'), (b'SCOM', b'Standing Committee'), (b'TCOM', b'Temporary Committee'), (b'ECOM', b'External Committee'), (b'MATHSOC', b'Mathematics Society'), (b'COUNCIL', b'MathSoc Council'), (b'OFFICE', b'MathSoc Office')])),
                ('member_count', models.IntegerField()),
                ('fee', models.IntegerField()),
                ('office', models.CharField(max_length=32)),
                ('website', models.URLField()),
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
                ('description', models.TextField()),
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
                ('occupied_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scholarships',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('organization', models.CharField(max_length=256)),
                ('amount', models.IntegerField()),
                ('description', models.TextField()),
                ('website', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='organization',
            name='documents',
            field=models.ManyToManyField(to='tangent.OrganizationDocument'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='positions',
            field=models.ManyToManyField(to='tangent.Position'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meeting',
            name='organization',
            field=models.ForeignKey(to='tangent.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='announcement',
            name='author_position',
            field=models.ForeignKey(to='tangent.Position'),
            preserve_default=True,
        ),
    ]
