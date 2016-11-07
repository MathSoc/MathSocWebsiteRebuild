# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('course_number', models.IntegerField()),
                ('subject', models.CharField(max_length=10)),
                ('semester', models.IntegerField()),
                ('file', models.FileField(upload_to='exams')),
            ],
        ),
    ]
