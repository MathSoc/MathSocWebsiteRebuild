# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tangent', '0002_auto_20161107_0619'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anonymous', models.BooleanField(default=False)),
                ('subject', models.CharField(max_length=256)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(to='tangent.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=10)),
                ('course_number', models.IntegerField()),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('semester', models.IntegerField()),
                ('publically_available', models.BooleanField(default=False)),
                ('file', models.FileField(upload_to='exams')),
                ('course', models.ForeignKey(to='university.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('biography', models.TextField(null=True, blank=True)),
                ('website', models.CharField(max_length=256)),
                ('picture', models.ImageField(null=True, upload_to='profile_pictures', blank=True)),
                ('previous_courses', models.ManyToManyField(to='university.Course', null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='professor',
            field=models.ForeignKey(to='university.Professor'),
        ),
        migrations.AddField(
            model_name='comment',
            name='topic_course',
            field=models.ForeignKey(to='university.Course'),
        ),
        migrations.AddField(
            model_name='comment',
            name='topic_exam',
            field=models.ForeignKey(null=True, to='university.Exam', blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='topic_prof',
            field=models.ForeignKey(null=True, to='university.Professor', blank=True),
        ),
    ]
