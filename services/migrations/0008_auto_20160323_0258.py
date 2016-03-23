# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_bookingrequest_calendar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrequest',
            name='status',
            field=models.IntegerField(choices=[(1, 'Requested'), (2, 'Accepted'), (3, 'Rejected')], default=1),
        ),
        migrations.AlterField(
            model_name='courseevaluation',
            name='file',
            field=models.FileField(upload_to='course_evaluations'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='file',
            field=models.FileField(upload_to='exams'),
        ),
    ]
