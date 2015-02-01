# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEvaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('semester', models.IntegerField(max_length=4)),
                ('file', models.FileField(upload_to=b'course_evaluations')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('course_number', models.IntegerField(max_length=3)),
                ('subject', models.CharField(max_length=10)),
                ('semester', models.IntegerField(max_length=4)),
                ('file', models.FileField(upload_to=b'exams')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('empty', models.BooleanField(default=True)),
                ('locker_number', models.IntegerField(unique=True)),
                ('current_combo', models.CharField(max_length=6)),
                ('combo_number', models.IntegerField()),
                ('combo0', models.CharField(max_length=6)),
                ('combo1', models.CharField(max_length=6)),
                ('combo2', models.CharField(max_length=6)),
                ('combo3', models.CharField(max_length=6)),
                ('combo4', models.CharField(max_length=6)),
                ('owner', models.ForeignKey(to='tangent.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
