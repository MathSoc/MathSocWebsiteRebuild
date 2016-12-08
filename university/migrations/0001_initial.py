# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tangent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('anonymous', models.BooleanField(default=False)),
                ('subject', models.CharField(max_length=256)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(to='tangent.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=10)),
                ('course_number', models.IntegerField()),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseEvaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('semester', models.IntegerField()),
                ('file', models.FileField(upload_to='course_evaluations')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('semester', models.IntegerField()),
                ('publically_available', models.BooleanField(default=False)),
                ('file', models.FileField(upload_to='exams')),
                ('course', models.ForeignKey(to='university.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('biography', models.TextField(null=True, blank=True)),
                ('website', models.CharField(max_length=256)),
                ('picture', models.ImageField(upload_to='profile_pictures', null=True, blank=True)),
                ('previous_courses', models.ManyToManyField(to='university.Course', blank=True)),
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
            field=models.ForeignKey(to='university.Exam', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='topic_prof',
            field=models.ForeignKey(to='university.Professor', null=True, blank=True),
        ),
    ]
